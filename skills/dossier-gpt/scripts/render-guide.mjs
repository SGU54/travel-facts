#!/usr/bin/env node
/** Render the explicitly declared book/sheet documents without editorial rewrites.
 * Usage: node render-guide.mjs BUILD_DIR
 * release.json: {documents:[{id,html,pdf,critical_json?}]}
 * critical_json defaults to <id>-critical.json and must exist. A verified draft
 * replaces the output only after page-count and source/PDF text checks pass.
 */
import fs from 'node:fs';
import path from 'node:path';
import {createRequire} from 'node:module';
import {fileURLToPath, pathToFileURL} from 'node:url';
import {spawnSync} from 'node:child_process';
import {gunzipSync} from 'node:zlib';

const here = path.dirname(fileURLToPath(import.meta.url));
const require = createRequire(import.meta.url);

function playwright() {
  try { return require('playwright'); } catch (_) {}
  for (const root of [process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES,
    path.join(path.dirname(process.execPath), 'node_modules')].filter(Boolean)) {
    try { return require(path.join(root, 'playwright')); } catch (_) {}
  }
  throw Error('Node Playwright is unavailable. Install playwright and its Chromium browser.');
}

function inside(build, relative, mustExist = true) {
  if (typeof relative !== 'string' || !relative || path.isAbsolute(relative) || relative.includes('\0'))
    throw Error('Document paths must be non-empty paths relative to the build directory.');
  const absolute = path.resolve(build, relative);
  if (!absolute.startsWith(build + path.sep)) throw Error('Path escapes build directory: ' + relative);
  let ancestor = absolute;
  while (!fs.existsSync(ancestor)) ancestor = path.dirname(ancestor);
  const real = fs.realpathSync(ancestor);
  if (real !== build && !real.startsWith(build + path.sep))
    throw Error('Path follows a symlink outside build directory: ' + relative);
  if (mustExist && (!fs.existsSync(absolute) || !fs.statSync(absolute).isFile()))
    throw Error('Missing input file: ' + relative);
  return absolute;
}

function python(command) {
  const executable = process.env.CODEX_PRIMARY_RUNTIME_PYTHON || 'python3';
  const proc = spawnSync(executable, command, {encoding: 'utf8', maxBuffer: 16 * 1024 * 1024});
  if (proc.error) throw Error('Python could not run: ' + proc.error.message);
  return proc;
}

function sanitizedHTML(html) {
  // Scripts are not manuscript content. Original HTML scripts must not run;
  // pagination is injected explicitly after assets are ready. An unclosed
  // script is rejected instead of guessing which following content is prose.
  const cleaned = html.replace(/<script\b[^>]*>[\s\S]*?<\/script\s*>/gi, '');
  if (/<script\b/i.test(cleaned)) throw Error('Unclosed or unsupported script element in source HTML.');
  if (!/<head\b/i.test(cleaned) || !/<body\b/i.test(cleaned))
    throw Error('Source HTML must contain explicit head and body elements.');
  if (/\bon[a-z]+\s*=\s*["']/i.test(cleaned))
    throw Error('Inline event handlers are not supported in printable manuscript HTML.');
  return cleaned;
}

async function main() {
  if (process.argv.length !== 3 || process.argv[2] === '--help') {
    console.log('Usage: node render-guide.mjs BUILD_DIR\nReads release.json documents [{id,html,pdf,critical_json?}].');
    return process.argv[2] === '--help' ? 0 : 2;
  }
  const build = fs.realpathSync(path.resolve(process.argv[2]));
  const manifest = JSON.parse(fs.readFileSync(path.join(build, 'release.json'), 'utf8'));
  if (!Array.isArray(manifest.documents) || !manifest.documents.length)
    throw Error('release.json must explicitly declare a non-empty documents array.');
  const ids = new Set(), outputs = new Set();
  const documents = manifest.documents.map(doc => {
    if (!doc || typeof doc.id !== 'string' || !/^[a-z0-9][a-z0-9_-]*$/i.test(doc.id) || ids.has(doc.id))
      throw Error('Each document needs a unique simple id.');
    ids.add(doc.id);
    const html = inside(build, doc.html), pdf = inside(build, doc.pdf, false);
    const critical = inside(build, doc.critical_json || `${doc.id}-critical.json`);
    if (html === pdf || outputs.has(pdf)) throw Error('Output paths must be unique and different from sources.');
    outputs.add(pdf);
    if (!/\.html?$/i.test(html) || !/\.pdf$/i.test(pdf)) throw Error('Expected HTML source and PDF output extensions.');
    return {...doc, html, pdf, critical, content: sanitizedHTML(fs.readFileSync(html, 'utf8'))};
  });
  const polyfill = path.resolve(here, '../assets/paged.polyfill.js.gz');
  if (!fs.existsSync(polyfill)) throw Error('Bundled Paged.js is missing: ' + polyfill);
  const polyfillText = gunzipSync(fs.readFileSync(polyfill)).toString('utf8');
  const pw = playwright();
  const launch = {headless: true, args: ['--no-sandbox', '--font-render-hinting=none']};
  if (process.env.DOSSIER_CHROMIUM_EXECUTABLE)
    launch.executablePath = process.env.DOSSIER_CHROMIUM_EXECUTABLE;
  const browser = await pw.chromium.launch(launch);
  const reports = [];
  try {
    for (const doc of documents) {
      const context = await browser.newContext({viewport: {width: 816, height: 1056}});
      const page = await context.newPage();
      const errors = [];
      const temporaryHTML = path.join(path.dirname(doc.html), `.render-${doc.id}-${process.pid}.html`);
      const draft = doc.pdf + '.unverified.pdf';
      try {
        await page.emulateMedia({media: 'print'});
        page.on('pageerror', error => errors.push(error.message));
        page.on('requestfailed', request => errors.push('Asset request failed: ' + request.url()));
        await page.route('**/*', route => {
          const url = route.request().url();
          if (/^https?:/i.test(url)) {
            errors.push('External asset must be supplied locally: ' + url);
            return route.abort();
          }
          return route.continue();
        });
        await page.addInitScript(() => { window.PagedConfig = {auto: false}; });
        fs.writeFileSync(temporaryHTML, doc.content, {encoding: 'utf8', flag: 'wx'});
        await page.goto(pathToFileURL(temporaryHTML).href, {waitUntil: 'load', timeout: 60000});
        await page.evaluate(async () => {
          await document.fonts.ready;
          const failedFonts = [...document.fonts].filter(font => font.status === 'error');
          if (failedFonts.length) throw Error('A manuscript font failed to load.');
          await Promise.all([...document.images].map(async image => {
            await image.decode();
            if (!image.naturalWidth) throw Error('Image did not decode: ' + image.src);
          }));
        });
        if (errors.length) throw Error(errors.join('\n'));
        await page.addScriptTag({content: polyfillText});
        const pageCount = await page.evaluate(async () => {
          const timeout = new Promise((_, reject) => setTimeout(() => reject(Error('Pagination timed out.')), 60000));
          const flow = await Promise.race([window.PagedPolyfill.preview(), timeout]);
          const count = document.querySelectorAll('.pagedjs_page').length;
          if (!count || count !== flow.total) throw Error('Paginator produced an invalid page count.');
          return count;
        });
        if (errors.length) throw Error(errors.join('\n'));
        fs.mkdirSync(path.dirname(doc.pdf), {recursive: true});
        await page.pdf({path: draft, printBackground: true, preferCSSPageSize: true,
          displayHeaderFooter: false, outline: true, tagged: true,
          margin: {top: '0', bottom: '0', left: '0', right: '0'}});
        const countResult = python(['-c',
          'import fitz,sys; d=fitz.open(sys.argv[1]); print(len(d)); d.close()', draft]);
        if (countResult.status !== 0 || Number(countResult.stdout.trim()) !== pageCount)
          throw Error('DOM/PDF page counts differ or PDF parser is unavailable: ' + countResult.stderr);
        const checked = python([path.join(here, 'audit-content.py'), doc.html, draft,
          '--critical-json', doc.critical, '--json']);
        let integrity;
        try { integrity = JSON.parse(checked.stdout); }
        catch (_) { throw Error('Content audit did not return JSON: ' + checked.stderr); }
        if (checked.status !== 0 || integrity.status !== 'PASS') {
          fs.writeFileSync(doc.pdf + '.content-audit.json', JSON.stringify(integrity, null, 2) + '\n');
          throw Error(`Content audit ${integrity.status} for ${doc.id}; review ${draft} and ${doc.pdf}.content-audit.json`);
        }
        fs.renameSync(draft, doc.pdf);
        reports.push({id: doc.id, html: path.relative(build, doc.html), pdf: path.relative(build, doc.pdf),
          pages: pageCount, content_status: integrity.status});
        console.log(`RENDERED ${doc.id}: ${pageCount} pages; content conservation PASS`);
      } finally {
        if (fs.existsSync(temporaryHTML)) fs.unlinkSync(temporaryHTML);
        await context.close();
      }
    }
  } finally { await browser.close(); }
  fs.writeFileSync(path.join(build, 'render-report.json'), JSON.stringify({documents: reports}, null, 2) + '\n');
  console.log('Rendering complete. Run audit-release.py before any delivery.');
  return 0;
}

main().then(code => { process.exitCode = code; }).catch(error => {
  console.error('RENDER BLOCKED: ' + String(error.stack || error));
  process.exitCode = 2;
});
