import { readFileSync, writeFileSync, mkdirSync, renameSync, rmSync } from 'node:fs';
import { resolve, dirname, basename, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';
import { createHash, randomUUID } from 'node:crypto';

export const here = dirname(fileURLToPath(import.meta.url));
export const isMain = url => Boolean(process.argv[1]) && resolve(process.argv[1]) === fileURLToPath(url);
export const sha256 = value => createHash('sha256').update(value).digest('hex');
export const readJSON = path => { try { return JSON.parse(readFileSync(path, 'utf8')); } catch (e) { throw new Error(`Cannot read JSON ${path}: ${e.message}`); } };
export const validSlug = value => typeof value === 'string' && /^[\p{L}\p{N}]+(?:-[\p{L}\p{N}]+)*$/u.test(value);
export function options(argv, valueFlags = [], switches = []) {
  const result = { positional: [] };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--') { result.positional.push(...argv.slice(i + 1)); break; }
    if (!a.startsWith('--')) { result.positional.push(a); continue; }
    const equal = a.indexOf('=');
    const flag = equal < 0 ? a : a.slice(0, equal);
    if (switches.includes(flag) && equal < 0) { result[flag] = true; continue; }
    if (!valueFlags.includes(flag)) throw new Error(`Unknown option ${flag}`);
    const value = equal < 0 ? argv[++i] : a.slice(equal + 1);
    if (!value || value.startsWith('--')) throw new Error(`Missing value for ${flag}`);
    result[flag] = value;
  }
  return result;
}
export function localAdapter(request) {
  const python = process.env.TRAVEL_EMPIRE_PYTHON || process.env.CODEX_PRIMARY_RUNTIME_PYTHON || 'python3';
  const r = spawnSync(python, [join(here, 'html-tools.py')], { input: JSON.stringify(request), encoding: 'utf8', maxBuffer: 32 * 1024 * 1024 });
  if (r.error) throw new Error(`Cannot start Python (${python}): ${r.error.message}`);
  if (r.status !== 0) throw new Error((r.stderr || 'HTML/PDF adapter failed').trim());
  try { return JSON.parse(r.stdout); } catch { throw new Error('HTML/PDF adapter returned invalid JSON'); }
}
export function atomicWrite(path, content) {
  mkdirSync(dirname(resolve(path)), { recursive: true });
  const temp = join(dirname(resolve(path)), `.${basename(path)}.${randomUUID()}.tmp`);
  try { writeFileSync(temp, content); renameSync(temp, path); } finally { rmSync(temp, { force: true }); }
}
export function distinctOutput(output, inputs) {
  if (inputs.some(input => resolve(input) === resolve(output))) throw new Error('Output must differ from every input file');
}
export function articlesFrom(raw, { published = false } = {}) {
  const articles = Array.isArray(raw) ? raw : raw?.articles;
  if (!Array.isArray(articles) || articles.length === 0) throw new Error('A nonempty article array or {articles:[...]} is required');
  const seen = new Set();
  for (const a of articles) {
    if (!a || typeof a !== 'object' || !validSlug(a.slug)) throw new Error('Every article needs a valid single-segment slug');
    if (seen.has(a.slug)) throw new Error(`Duplicate article slug: ${a.slug}`);
    seen.add(a.slug);
    if (published && a.status !== 'published') throw new Error(`${a.slug}: selected article must explicitly have status published`);
  }
  return articles;
}
export function webURL(value, { relative = false } = {}) {
  if (typeof value !== 'string' || !value.trim() || /[\u0000-\u0020\\]/.test(value)) return false;
  if (relative && /^\/(?!\/)/.test(value)) return true;
  try { const u = new URL(value); return ['https:', 'http:'].includes(u.protocol) && !u.username && !u.password; } catch { return false; }
}
