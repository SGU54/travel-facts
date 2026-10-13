#!/usr/bin/env node
/** Offline HTML -> PDF with natural pagination, copy conservation and output verification. */
import { existsSync, readFileSync, renameSync, rmSync, mkdtempSync, mkdirSync } from 'node:fs';
import { dirname, resolve, join, basename } from 'node:path';
import { pathToFileURL } from 'node:url';
import { createRequire } from 'node:module';
import { isMain, options, readJSON, localAdapter, webURL, atomicWrite, distinctOutput, sha256 } from './runtime.mjs';
const HELP = `Usage: node scripts/build-leadmagnet.mjs DATA.json OUTPUT.pdf [--chrome=/absolute/path] [--html-only]
Requires a schema_version 2 manifest from leadmagnet-data, local Playwright + a local Chromium browser,
Python lxml/pypdf (scripts/requirements.txt). TRAVEL_EMPIRE_PYTHON overrides Python.
--html-only explicitly writes an HTML proof; it does NOT create or verify a PDF.
No browser downloads or external page requests. Every PDF page still requires visual review.
A failed render never replaces a previous PDF. Successful generation is not publication approval.`;
const esc = v => String(v ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const norm = v => String(v).normalize('NFKC').replace(/\s+/gu, '');
const hashPattern = /^[0-9a-f]{64}$/;

export function validateManifest(d) {
  if (!d || d.schema_version !== 2 || !Array.isArray(d.days) || !d.days.length || !d.review || !d.provenance) throw new Error('A complete schema_version 2 source-mapped manifest is required');
  if (!Number.isInteger(d.tripDays) || d.tripDays < 1 || !webURL(d.site?.domain)) throw new Error('Manifest needs a valid tripDays and site.domain');
  if (!hashPattern.test(d.provenance.exportSha256 || '') || !hashPattern.test(d.provenance.configSha256 || '')) throw new Error('Manifest lacks source-export/config provenance hashes');
  if (!d.cover?.title || typeof d.cover.title !== 'string') throw new Error('Manifest cover title is required');
  const all = [...d.days, ...(d.beforeYouGo?.items || [])];
  for (const block of all) {
    if (typeof block.body !== 'string' || !block.body.trim() || !webURL(block.url) || !block.copiedFrom?.heading || !hashPattern.test(block.copiedFrom?.contentSha256 || '')) throw new Error('Every copied block needs complete text, an absolute URL and source provenance');
    if (sha256(block.body) !== block.copiedFrom.bodySha256) throw new Error('Copied block text changed after source extraction; regenerate and review');
  }
  let next = 1;
  for (const day of d.days) {
    if (day.title !== day.copiedFrom.heading) throw new Error('Source itinerary heading was relabelled');
    if (day.startDay !== next || !Number.isInteger(day.endDay) || day.endDay < day.startDay) throw new Error('Invalid manifest day coverage');
    next = day.endDay + 1;
  }
  if (next !== d.tripDays + 1) throw new Error('Manifest day coverage differs from tripDays');
  for (const l of d.backCover?.links || []) if (!webURL(l.url) || !l.label) throw new Error('Back-cover links need labels and absolute HTTP(S) URLs');
  return all;
}
function themeTokens(theme = {}) {
  const defaults = { ink: '#252A2C', paper: '#FFFCF7', accent: '#804631', muted: '#5F625F', line: '#D8D4CC' };
  for (const k of Object.keys(defaults)) {
    if (theme[k]) {
      if (!/^#(?:[0-9a-f]{3}|[0-9a-f]{6})$/i.test(theme[k])) throw new Error(`Theme ${k} must be a 3- or 6-digit hex color`);
      defaults[k] = theme[k];
    }
  }
  function light(hex) { let h = hex.slice(1); if (h.length === 3) h = h.split('').map(x => x + x).join(''); return [0, 2, 4].map(i => parseInt(h.slice(i, i + 2), 16) / 255).map(v => v <= .04045 ? v / 12.92 : ((v + .055) / 1.055) ** 2.4).reduce((v, c, i) => v + c * [.2126, .7152, .0722][i], 0); }
  function ratio(a, b) { const x = light(a), y = light(b); return (Math.max(x, y) + .05) / (Math.min(x, y) + .05); }
  if (ratio(defaults.ink, defaults.paper) < 4.5 || ratio(defaults.muted, defaults.paper) < 4.5 || ratio(defaults.accent, defaults.paper) < 4.5) throw new Error('Text colors must provide at least 4.5:1 contrast against paper');
  for (const [key, fallback] of [['bodyFont', 'Georgia, serif'], ['displayFont', 'Georgia, serif']]) {
    const value = theme[key] || fallback;
    if (typeof value !== 'string' || !/^[\w\s,'"-]+$/.test(value)) throw new Error(`Unsafe font token: ${key}`);
    defaults[key] = value;
  }
  return defaults;
}
export function buildHTML(d) {
  const copied = validateManifest(d);
  const t = themeTokens(d.theme);
  const url = value => `<a class="source" href="${esc(value)}">${esc(value)}</a>`;
  const block = b => `<div class="copy" data-copy-hash="${sha256(b.body)}">${esc(b.body)}</div><p class="source-title">${esc(b.copiedFrom.title)} · ${esc(b.copiedFrom.heading)}</p>${url(b.url)}`;
  const glance = d.atAGlance ? `<section class="chapter"><h2>${esc(d.atAGlance.heading)}</h2>${(d.atAGlance.facts || []).map(f => `<p><strong>${esc(f.value)}</strong> — ${esc(f.label)}</p>`).join('')}<p>${esc(d.atAGlance.howToUse)}</p></section>` : '';
  const before = d.beforeYouGo?.items?.length ? `<section class="chapter"><h2>${esc(d.beforeYouGo.heading)}</h2>${d.beforeYouGo.items.map(b => `<article><h3>${esc(b.title)}</h3>${block(b)}</article>`).join('')}</section>` : '';
  const days = d.days.map(b => `<section class="chapter"><p class="eyebrow">${b.startDay === b.endDay ? `Day ${b.startDay}` : `Days ${b.startDay}–${b.endDay}`} · ${d.tripDays}-day trip</p><h2>${esc(b.title)}</h2>${block(b)}</section>`).join('');
  const costs = d.costs ? `<section class="chapter"><h2>${esc(d.costs.heading)}</h2><p>${esc(d.costs.intro)}</p>${(d.costs.tiers || []).map(c => `<article><h3>${esc(c.name)}</h3>${c.perDay ? `<p><strong>${esc(c.perDay)}</strong> per day</p>` : ''}${c.total ? `<p><strong>${esc(c.total)}</strong> for the trip</p>` : ''}${c.figure ? `<p>${esc(c.figure)}</p>` : ''}<p>${esc(c.note)}</p></article>`).join('')}<p>${esc(d.costs.footnote)}</p>${d.costs.checklist?.length ? `<h3>${esc(d.costs.checklistHeading)}</h3><ul>${d.costs.checklist.map(v => `<li>${esc(v)}</li>`).join('')}</ul>` : ''}${d.costs.mechanics?.length ? `<h3>${esc(d.costs.mechanicsHeading || 'Money mechanics')}</h3>${d.costs.mechanics.map(v => `<h4>${esc(v.title)}</h4><p>${esc(v.body)}</p>`).join('')}` : ''}</section>` : '';
  const back = `<section class="chapter"><h2>${esc(d.backCover?.heading || 'Sources and further reading')}</h2><p>${esc(d.backCover?.blurb)}</p>${(d.backCover?.links || []).map(l => `<article><h3>${esc(l.label)}</h3>${url(l.url)}</article>`).join('')}<p class="small">Edition: ${esc(d.site.edition || '')}. Source snapshot: ${esc(d.provenance.generatedAt || '')}.</p></section>`;
  const html = `<!doctype html><html lang="${esc(d.site.language || 'en')}"><head><meta charset="utf-8"><title>${esc(d.cover.title)}</title><style>
@page{size:Letter;margin:.7in .75in .75in}*{box-sizing:border-box}html{background:${t.paper}}body{margin:0;color:${t.ink};font:11pt/1.52 ${t.bodyFont};font-variant-ligatures:none;overflow-wrap:anywhere;hyphens:none}main{max-width:7in;margin:auto}h1,h2,h3,h4{font-family:${t.displayFont};line-height:1.2;break-after:avoid}h1{font-size:46pt;margin:.3in 0}h2{font-size:25pt;color:${t.accent};margin:0 0 .25in}h3{font-size:16pt;margin:.25in 0 .1in}p,li{orphans:3;widows:3}p{margin:.12in 0}.chapter{break-before:page;padding-top:.1in}.cover{min-height:8in;padding-top:.55in}.eyebrow{font:9pt/1.5 sans-serif;letter-spacing:.06em;color:${t.muted}}.copy{white-space:pre-line;orphans:3;widows:3}.source{display:block;font:9pt/1.45 sans-serif;overflow-wrap:anywhere;color:${t.accent}}.source-title,.small{font:9pt/1.45 sans-serif;color:${t.muted}}article{margin:.25in 0}.route{border-top:2px solid ${t.line};padding-top:.2in;margin-top:.5in}a{color:${t.accent}}@media screen{body{padding:32px}main{background:${t.paper}}.chapter{margin-top:48px;border-top:1px solid ${t.line};padding-top:32px}}
</style></head><body><main><section class="cover"><p class="eyebrow">${esc(d.site.brandName || d.site.domain)} · ${esc(d.site.edition)}</p><h1>${esc(d.cover.title)}${d.cover.titleLine2 ? `<br>${esc(d.cover.titleLine2)}` : ''}</h1><h2>${esc(d.cover.subtitle)}</h2><p>${esc(d.cover.blurb)}</p><div class="route"><p>${esc(d.cover.routeLabel)}</p>${(d.cover.stops || []).map(s => `<p><strong>${esc(s.name)}</strong> · ${esc(s.meta)}</p>`).join('')}</div></section>${glance}${before}${days}${costs}${back}</main></body></html>`;
  return { html, copied };
}
async function playwrightModule() {
  try { return await import('playwright'); } catch {}
  const modules = process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES;
  if (modules) {
    try { const req = createRequire(join(modules, '_travel-runtime.cjs')); return await import(pathToFileURL(req.resolve('playwright')).href); } catch {}
  }
  throw new Error('Playwright is unavailable. Install the optional dependency in package.json, or request --html-only; no PDF was produced');
}
export async function renderLeadmagnet(d, output, opts = {}) {
  const { html, copied } = buildHTML(d);
  const htmlPath = output.replace(/\.pdf$/i, '') + '.html';
  if (opts.htmlOnly) { atomicWrite(htmlPath, html); return { mode: 'html-only', html: htmlPath, pdf: null, pdfVerified: false }; }
  if (!/\.pdf$/i.test(output)) throw new Error('PDF output path must end in .pdf');
  if (opts.chrome && !existsSync(opts.chrome)) throw new Error('Explicit Chromium executable does not exist; no PDF was produced');
  const api = await playwrightModule();
  const chromium = api.chromium || api.default?.chromium;
  if (!chromium) throw new Error('Playwright Chromium API unavailable');
  mkdirSync(dirname(resolve(output)), { recursive: true });
  const tempDir = mkdtempSync(join(dirname(resolve(output)), '.leadmagnet-'));
  const tempPDF = join(tempDir, basename(output));
  let browser;
  try {
    browser = await chromium.launch({ headless: true, ...(opts.chrome ? { executablePath: opts.chrome } : {}), timeout: 30000 });
    const page = await browser.newPage({ viewport: { width: 816, height: 1056 }, deviceScaleFactor: 1 });
    await page.route('**/*', route => route.abort());
    await page.setContent(html, { waitUntil: 'load' });
    await page.emulateMedia({ media: 'print' });
    await page.evaluate(() => document.fonts.ready);
    const preflight = await page.evaluate(() => {
      const issues = [];
      for (const el of document.querySelectorAll('main, main *')) {
        const css = getComputedStyle(el), r = el.getBoundingClientRect();
        if (['hidden', 'clip'].includes(css.overflowX) || ['hidden', 'clip'].includes(css.overflowY)) issues.push('clipping style');
        if (el.clientWidth && el.scrollWidth > el.clientWidth + 2) issues.push('horizontal overflow');
        if (r.width > 0 && (r.left < -2 || r.right > innerWidth + 2)) issues.push('element outside printable viewport');
      }
      return { issues: [...new Set(issues)], text: document.body.innerText };
    });
    if (preflight.issues.length) throw new Error(`HTML preflight failed: ${preflight.issues.join(', ')}`);
    for (const b of copied) if (!norm(preflight.text).includes(norm(b.body))) throw new Error('Source text is missing from the rendered HTML');
    await page.pdf({ path: tempPDF, preferCSSPageSize: true, printBackground: true, displayHeaderFooter: true, headerTemplate: '<span></span>', footerTemplate: '<div style="width:100%;text-align:center;font-size:9px;color:#555"><span class="pageNumber"></span> / <span class="totalPages"></span></div>' });
    if (!existsSync(tempPDF) || readFileSync(tempPDF).subarray(0, 5).toString() !== '%PDF-') throw new Error('Renderer did not create a valid PDF file');
    const pdf = localAdapter({ mode: 'pdf', path: tempPDF, margins: { top: 50.4, bottom: 54 } });
    if (!pdf.pages || !pdf.text.trim()) throw new Error('Generated PDF is empty');
    for (const b of copied) if (!norm(pdf.bodyText).includes(norm(b.body))) throw new Error('Source text is missing or reordered in the PDF body; inspect pagination/fonts before retrying');
    renameSync(tempPDF, output);
    atomicWrite(htmlPath, html);
    const result = { mode: 'pdf', pdf: output, html: htmlPath, pages: pdf.pages, sourceTextConserved: true, htmlOverflowChecked: true, pdfSha256: sha256(readFileSync(output)), manifestContentSha256: sha256(JSON.stringify(d)), manifestHashMethod: 'sha256(JSON.stringify(parsedManifest))', visualReview: 'pending', publicationReady: false };
    atomicWrite(output + '.checks.json', JSON.stringify(result, null, 2) + '\n');
    return result;
  } finally { if (browser) await browser.close(); rmSync(tempDir, { recursive: true, force: true }); }
}
export async function main(argv) {
  if (argv.includes('--help')) { console.log(HELP); return 0; }
  const args = options(argv, ['--chrome'], ['--html-only']);
  if (args.positional.length !== 2) throw new Error(HELP);
  const [input, output] = args.positional;
  distinctOutput(output, [input]); distinctOutput(output.replace(/\.pdf$/i, '') + '.html', [input]); distinctOutput(output + '.checks.json', [input]);
  const result = await renderLeadmagnet(readJSON(input), output, { chrome: args['--chrome'], htmlOnly: args['--html-only'] });
  console.log(JSON.stringify(result, null, 2)); return 0;
}
if (isMain(import.meta.url)) main(process.argv.slice(2)).then(code => { process.exitCode = code; }).catch(e => { console.error(`Lead-magnet build failed: ${e.message}`); process.exitCode = 1; });
