#!/usr/bin/env node
/**
 * rename-batch.mjs — R2 edition of the old upload-batch.mjs image step.
 *
 * Same brain as upload-batch.mjs: it reads import-batch-NN.json to learn the
 * expected object keys (featured hero + in-body images, in order), takes a
 * folder of images sorted by download order, checks the counts line up, and
 * shows you the mapping before doing anything.
 *
 * The ONE difference: instead of uploading to a CDN under the right name, it
 * copies the files into an output folder ALREADY RENAMED to the target keys.
 * You then push that folder to R2 with a plain rclone copy.
 *
 * Sorting (unchanged from upload-batch.mjs):
 *   - if EVERY filename starts with a number → sort by that number
 *   - otherwise → sort by file modification date (download order)
 *
 * Usage:
 *   node rename-batch.mjs <images-folder> <import-batch-NN.json> [out-folder]
 *   node rename-batch.mjs ./images ./import-batch-05.json --apply
 *
 * Without --apply it only previews. Nothing is written until you confirm.
 */

import fs from 'fs';
import path from 'path';

const args = process.argv.slice(2).filter((a) => a !== '--apply');
const APPLY = process.argv.includes('--apply');

if (args.length < 2) {
  console.error('Usage: node rename-batch.mjs <images-folder> <import-batch-NN.json> [out-folder] [--apply]');
  process.exit(1);
}

const absDir = path.resolve(args[0]);
const absJson = path.resolve(args[1]);
const outDir = path.resolve(args[2] || path.join(absDir, '..', 'renamed'));

if (!fs.existsSync(absDir)) { console.error(`Images folder not found: ${absDir}`); process.exit(1); }
if (!fs.existsSync(absJson)) { console.error(`import.json not found: ${absJson}`); process.exit(1); }

// ── 1. Ordered target keys straight from import.json ─────────────────────────
const parsed = JSON.parse(fs.readFileSync(absJson, 'utf8'));
const articles = Array.isArray(parsed) ? parsed : parsed.articles;
if (!Array.isArray(articles)) {
  console.error('import.json must be an array or { "articles": [...] }.');
  process.exit(1);
}

const targets = [];
const seen = new Set();
const push = (key, title, kind) => {
  if (seen.has(key)) return;
  seen.add(key);
  targets.push({ key, title, kind });
};

for (const a of articles) {
  // explicit ordered list wins (hero + in-body, in slot order)
  if (Array.isArray(a.image_ids) && a.image_ids.length) {
    a.image_ids.forEach((pid, i) =>
      push(pid.split('/').pop(), a.title, pid === a.featured_image || i === 0 ? 'hero' : 'in-body'));
    continue;
  }
  // hero: featured_image is a path; the object key is its last segment
  if (a.featured_image) push(a.featured_image.split('/').pop(), a.title, 'hero');
  // in-body: one key per IMAGE_SLOT_n comment, named <slug>-n
  const body = a.content || a.html || '';
  for (const m of body.matchAll(/<!--\s*IMAGE_SLOT_(\d+)\s*:/g)) {
    push(`${a.slug}-${m[1]}`, a.title, 'in-body');
  }
  // already-converted bodies: pick up real <img> keys too
  for (const m of body.matchAll(/\/articles\/([a-z0-9-]+)["'\s]/g)) {
    push(m[1], a.title, 'in-body');
  }
}

if (targets.length === 0) {
  console.error('No image keys found in import.json.');
  process.exit(1);
}

// ── 2. Images, sorted by download order (numeric prefix wins over file date) ─
const IMG = /\.(jpe?g|png|webp|gif|avif)$/i;
let files = fs.readdirSync(absDir).filter((f) => IMG.test(f) && !f.startsWith('._'));
if (files.length === 0) { console.error(`No image files found in ${absDir}`); process.exit(1); }

const allNumbered = files.every((f) => /^\d+/.test(f));
if (allNumbered) {
  files.sort((a, b) => parseInt(a, 10) - parseInt(b, 10));
} else {
  files.sort(
    (a, b) => fs.statSync(path.join(absDir, a)).mtimeMs - fs.statSync(path.join(absDir, b)).mtimeMs
  );
}

// ── 3. Count check — stop before writing anything if it doesn't line up ──────
if (files.length !== targets.length) {
  console.error(`\n⚠  Count mismatch: ${files.length} image(s) in the folder, but import.json expects ${targets.length}.\n`);
  console.error('import.json expects (in order):');
  targets.forEach((t, i) => console.error(`  ${i + 1}. ${t.key}  [${t.kind}]`));
  console.error('\nImages found (sorted):');
  files.forEach((f, i) => console.error(`  ${i + 1}. ${f}`));
  console.error('\nMake the counts match, then re-run. Nothing was written.');
  process.exit(1);
}

// ── 4. Preview ───────────────────────────────────────────────────────────────
const pairs = files.map((f, i) => ({
  file: f,
  ext: path.extname(f).toLowerCase(),
  ...targets[i],
}));

console.log(`\nSorted by ${allNumbered ? 'numeric prefix' : 'file date (download order)'}.`);
console.log(`Mapping ${pairs.length} image(s):\n`);
for (const [i, p] of pairs.entries()) {
  console.log(`  ${String(i + 1).padStart(2)}. ${p.file}`);
  console.log(`      → ${p.key}${p.ext}  [${p.kind}]  —  ${p.title}`);
}

// ── 5. Write ─────────────────────────────────────────────────────────────────
if (!APPLY) {
  console.log(`\nDry run. Nothing written. Re-run with --apply to copy into:\n  ${outDir}\n`);
  process.exit(0);
}

const MIME = { '.jpg':'image/jpeg', '.jpeg':'image/jpeg', '.png':'image/png',
               '.webp':'image/webp', '.gif':'image/gif', '.avif':'image/avif' };

fs.mkdirSync(outDir, { recursive: true });
const groups = new Map();          // mime -> subfolder
let n = 0;
for (const p of pairs) {
  const mime = MIME[p.ext] || 'application/octet-stream';
  const sub = path.join(outDir, mime.replace('/', '-'));   // e.g. image-jpeg/
  if (!groups.has(mime)) { fs.mkdirSync(sub, { recursive: true }); groups.set(mime, sub); }
  // ── THE KEY IS THE BARE public_id: NO EXTENSION. ──
  // Fleet rule: articles reference <folder>/articles/<slug>-n with no suffix,
  // so the object name must match exactly or the URL 404s.
  fs.copyFileSync(path.join(absDir, p.file), path.join(sub, p.key));
  n++;
}

console.log(`\n✓ ${n} file(s) copied, renamed WITHOUT extension, grouped by type:\n`);
for (const [mime, sub] of groups) console.log(`  ${sub}   → ${mime}`);
console.log('\nNext — push each group to R2 with its Content-Type set explicitly');
console.log('(no extension means rclone cannot infer it, so it must be passed):\n');
for (const [mime, sub] of groups) {
  console.log(`  rclone copy "${sub}" r2:fleet-media/${'<site>'}/articles/ \\`);
  console.log(`    --header-upload "Content-Type: ${mime}" \\`);
  console.log('    --s3-no-check-bucket --no-traverse --ignore-times\n');
}
