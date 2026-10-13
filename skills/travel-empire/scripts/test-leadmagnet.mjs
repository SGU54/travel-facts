#!/usr/bin/env node
import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtempSync, writeFileSync, existsSync, readFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { spawnSync } from 'node:child_process';
import { createRequire } from 'node:module';
import { compileLeadmagnet, suggestions } from './leadmagnet-data.mjs';
import { buildHTML, renderLeadmagnet, validateManifest } from './build-leadmagnet.mjs';
import { here, sha256, localAdapter } from './runtime.mjs';
const source = () => [{ slug: 'one-day-example', status: 'published', title: 'One day in Example City', content: '<h2>Day 1 — Old Town</h2><p>FIRST paragraph in full, including &amp; text.</p><h3>Later</h3><p>MIDDLE paragraph is equally important.</p><p>LAST paragraph must survive.</p><h2>Money basics</h2><p>Use a dated local budget.</p><p>Keep the full second paragraph too.</p>' }];
const config = () => ({ schema_version: 2, domain: 'https://example.test', tripDays: 1, site: { brandName: 'Example', destination: 'Example City', edition: 'Synthetic test' }, cover: { title: 'Example City', titleLine2: 'in one day', subtitle: 'A synthetic source test' }, itinerary: { slug: 'one-day-example', blocks: [{ heading: 'Day 1 — Old Town', startDay: 1, endDay: 1 }] }, beforeYouGo: { heading: 'Before departure', slots: [{ title: 'Money', slug: 'one-day-example', heading: 'Money basics' }] }, backCover: { heading: 'More', links: [{ label: 'Full route', slug: 'one-day-example' }] } });
const provenance = { exportSha256: sha256('synthetic source'), configSha256: sha256('synthetic config') };
const manifest = () => compileLeadmagnet(source(), config(), provenance);
test('Explicit sources preserve every paragraph and heading in order', () => { const d = manifest(); assert.match(d.days[0].body, /FIRST[\s\S]*Later[\s\S]*MIDDLE[\s\S]*LAST/); assert.match(d.beforeYouGo.items[0].body, /second paragraph/); assert.equal(d.days[0].title, 'Day 1 — Old Town'); assert.equal(d.review.status, 'pending'); });
test('Missing publication status does not become published', () => { const a = source(); delete a[0].status; assert.throws(() => compileLeadmagnet(a, config()), /published/); });
test('Wrong itinerary duration cannot pass on keyword score', () => { const c = config(); c.tripDays = 7; c.itinerary.blocks[0].endDay = 7; assert.throws(() => compileLeadmagnet(source(), c), /source heading/); });
test('Destination and title overrides are rejected', () => { const c = config(); c.itinerary.blocks[0].place = 'Another City'; assert.throws(() => compileLeadmagnet(source(), c), /relabel/); const a = source(); a[0].destination = 'Another City'; assert.throws(() => compileLeadmagnet(a, config()), /destination/); });
test('Required sections cannot silently disappear', () => { const c = config(); c.beforeYouGo.slots[0].heading = 'Not present'; assert.throws(() => compileLeadmagnet(source(), c), /exact H2/); });
test('Ambiguous or empty H2 sections fail', () => { const a = source(); a[0].content += '<h2>Money basics</h2><p>duplicate</p>'; assert.throws(() => compileLeadmagnet(a, config()), /found 2/); a[0].content = '<h2>Day 1 — Old Town</h2><h2>Money basics</h2><p>other</p>'; assert.throws(() => compileLeadmagnet(a, config()), /empty/); });
test('Legacy heuristics and unresolved template fields are not buildable', () => { assert.throws(() => compileLeadmagnet(source(), { days: [] }), /schema_version/); const c = config(); c.cover.title = 'FILL'; assert.throws(() => compileLeadmagnet(source(), c), /placeholder/); });
test('Suggestions do not masquerade as a manifest', () => { const d = suggestions(source(), { tripDays: 7 }); assert.equal(d.buildable, false); assert.equal(d.schema_version, undefined); assert.throws(() => validateManifest(d)); });
test('Changed copied text and relabelled headings are detected before rendering', () => { const d = manifest(); d.days[0].body += 'Added unsupported sentence.'; assert.throws(() => buildHTML(d), /text changed/); const e = manifest(); e.days[0].title = 'A different city'; assert.throws(() => buildHTML(e), /relabelled/); });
test('HTML uses complete copy, escaped text and natural pagination', () => { const d = manifest(); d.cover.title = '<script>literal title</script>'; const result = buildHTML(d); assert.ok(result.html.includes('&lt;script&gt;literal title&lt;/script&gt;')); assert.ok(result.html.includes('LAST paragraph must survive.')); assert.doesNotMatch(result.html, /overflow\s*:\s*hidden|height\s*:\s*11in|verified at publish time/); });
test('Unsafe or unreadable theme tokens fail', () => { const d = manifest(); d.theme = { paper: '#ffffff', ink: '#ffffff' }; assert.throws(() => buildHTML(d), /contrast/); d.theme = { bodyFont: 'Georgia; color:red' }; assert.throws(() => buildHTML(d), /font token/); });
test('HTML-only explicitly produces no PDF', async () => { const dir = mkdtempSync(join(tmpdir(), 'travel-html-test-')); try { const out = join(dir, 'proof.pdf'); const r = await renderLeadmagnet(manifest(), out, { htmlOnly: true }); assert.equal(r.mode, 'html-only'); assert.equal(r.pdfVerified, false); assert.equal(existsSync(out), false); assert.ok(existsSync(r.html)); } finally { rmSync(dir, { recursive: true, force: true }); } });
test('Missing explicit browser fails without replacing an existing PDF', async () => { const dir = mkdtempSync(join(tmpdir(), 'travel-missing-browser-')); try { const out = join(dir, 'proof.pdf'); writeFileSync(out, 'previous edition'); await assert.rejects(renderLeadmagnet(manifest(), out, { chrome: join(dir, 'missing-chromium') }), /does not exist/); assert.equal(readFileSync(out, 'utf8'), 'previous edition'); } finally { rmSync(dir, { recursive: true, force: true }); } });
test('Combined CLI does not commit a new manifest when PDF generation fails', () => { const dir = mkdtempSync(join(tmpdir(), 'travel-all-test-')); try { const input = join(dir, 'export.json'), cfg = join(dir, 'config.json'), out = join(dir, 'output'); writeFileSync(input, JSON.stringify(source())); writeFileSync(cfg, JSON.stringify(config())); const r = spawnSync(process.execPath, [join(here, 'build-leadmagnet-all.mjs'), input, cfg, out, '--chrome', join(dir, 'missing')], { encoding: 'utf8' }); assert.equal(r.status, 1); assert.equal(existsSync(join(out, 'leadmagnet.json')), false); assert.equal(existsSync(join(out, 'leadmagnet.pdf')), false); } finally { rmSync(dir, { recursive: true, force: true }); } });
let browserPath = null;
try { const req = createRequire(join(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES || here, '_travel-test.cjs')); const api = req('playwright'); const candidate = process.env.TRAVEL_EMPIRE_TEST_CHROME || api.chromium.executablePath(); if (existsSync(candidate)) browserPath = candidate; } catch {}
test('A real local browser conserves all source text across PDF pages', { skip: !browserPath }, async () => { const dir = mkdtempSync(join(tmpdir(), 'travel-render-test-')); try { const d = manifest(); d.days[0].body = Array.from({ length: 60 }, (_, i) => `Paragraph ${i}: full source copy must survive every page boundary.`).join('\n'); d.days[0].copiedFrom.bodySha256 = sha256(d.days[0].body); const out = join(dir, 'proof.pdf'); const r = await renderLeadmagnet(d, out, { chrome: browserPath }); assert.ok(r.pages > 3); assert.equal(r.sourceTextConserved, true); const pdf = localAdapter({ mode: 'pdf', path: out }); assert.match(pdf.text, /Paragraph 59/); } finally { rmSync(dir, { recursive: true, force: true }); } });
test('Tables do not lose their column relationships in a text extraction', () => {
  const a = source(); a[0].content = a[0].content.replace('<p>LAST paragraph must survive.</p>', '<table><tr><th>Type</th><th>Price</th></tr><tr><td>Daily</td><td>90</td></tr></table>');
  assert.throws(() => compileLeadmagnet(a, config()), /structured PDF section/);
});
test('List order and existing link destinations survive extraction', () => {
  const a = source(); a[0].content = a[0].content.replace('<p>LAST paragraph must survive.</p>', '<ol><li>Reserve first</li><li>Arrive second</li></ol><p>Read <a href="/article/practical-details">the details</a>.</p>');
  const d = compileLeadmagnet(a, config()); assert.match(d.days[0].body, /1\. Reserve first[\s\S]*2\. Arrive second/); assert.ok(d.days[0].body.includes('https://example.test/article/practical-details'));
});
function syntheticPDF() {
  const streams = [
    'BT /F1 12 Tf 72 720 Td (Keep ratio 1 / 2. FIRST) Tj ET\nBT /F1 9 Tf 280 20 Td (1 / 2) Tj ET',
    'BT /F1 12 Tf 72 720 Td (SECOND with 90 in the body.) Tj ET\nBT /F1 9 Tf 280 20 Td (2 / 2) Tj ET',
  ];
  const objects = [
    '<< /Type /Catalog /Pages 2 0 R >>',
    '<< /Type /Pages /Kids [3 0 R 5 0 R] /Count 2 >>',
    '<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 7 0 R >> >> /Contents 4 0 R >>',
    `<< /Length ${streams[0].length} >>\nstream\n${streams[0]}\nendstream`,
    '<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 7 0 R >> >> /Contents 6 0 R >>',
    `<< /Length ${streams[1].length} >>\nstream\n${streams[1]}\nendstream`,
    '<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>',
  ];
  let output = '%PDF-1.4\n'; const offsets = [0];
  for (let i = 0; i < objects.length; i++) { offsets.push(Buffer.byteLength(output)); output += `${i + 1} 0 obj\n${objects[i]}\nendobj\n`; }
  const xref = Buffer.byteLength(output); output += `xref\n0 ${objects.length + 1}\n0000000000 65535 f \n${offsets.slice(1).map(n => String(n).padStart(10, '0') + ' 00000 n \n').join('')}trailer\n<< /Size ${objects.length + 1} /Root 1 0 R >>\nstartxref\n${xref}\n%%EOF\n`;
  return output;
}
test('Coordinate-based PDF body extraction excludes footers and retains the same numbers in body text', () => {
  const dir = mkdtempSync(join(tmpdir(), 'travel-pdf-body-test-'));
  try { const path = join(dir, 'two-pages.pdf'); writeFileSync(path, syntheticPDF()); const pdf = localAdapter({ mode: 'pdf', path, margins: { top: 50.4, bottom: 54 } }); const normalize = value => value.replace(/\s+/g, ''); assert.equal(pdf.pages, 2); assert.ok(normalize(pdf.bodyText).includes('FIRSTSECOND')); assert.ok(pdf.bodyText.includes('Keep ratio 1 / 2.')); assert.ok(pdf.bodyText.includes('90')); assert.equal((pdf.bodyText.match(/1 \/ 2/g) || []).length, 1); assert.equal(pdf.bodyText.includes('2 / 2'), false); assert.equal(normalize(pdf.text).includes('FIRSTSECOND'), false); } finally { rmSync(dir, { recursive: true, force: true }); }
});
