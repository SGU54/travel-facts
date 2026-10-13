#!/usr/bin/env node
/** Explicit selection of published sources; preserve full H2 blocks and their names. */
import { readFileSync } from 'node:fs';
import { isMain, options, readJSON, articlesFrom, localAdapter, webURL, atomicWrite, distinctOutput, sha256 } from './runtime.mjs';
const HELP = `Usage: node scripts/leadmagnet-data.mjs EXPORT.json CONFIG.json OUTPUT.json [--suggest]
Config schema_version 2: domain=https://host, tripDays, itinerary={slug,blocks:[{heading,startDay,endDay}]},
 beforeYouGo={heading,slots:[{title,slug,heading}]}, backCover={heading,blurb,links:[{label,slug}]}.
Selected articles must explicitly be published. Exact source H2 titles and complete block text are retained.
Day mappings must cover 1..tripDays exactly. No place/title overrides or automatic winner selection.
--suggest produces suggestions only, never a buildable manifest. No network or DB access.`;

function nonempty(value, field) { if (typeof value !== 'string' || !value.trim()) throw new Error(`${field} must be a nonempty string`); return value; }
function noPlaceholders(value, path = 'config') {
  if (typeof value === 'string' && /\{\{|\b(?:FILL|TODO|TBD)\b/.test(value)) throw new Error(`Unresolved placeholder: ${path}`);
  if (value && typeof value === 'object') for (const [key, child] of Object.entries(value)) if (!key.startsWith('_')) noPlaceholders(child, `${path}.${key}`);
}
export function compileLeadmagnet(raw, cfg, provenance = {}) {
  const articles = articlesFrom(raw);
  if (!cfg || cfg.schema_version !== 2) throw new Error('Lead-magnet config schema_version 2 and explicit source mapping are required');
  noPlaceholders(cfg);
  if (!webURL(cfg.domain) || new URL(cfg.domain).protocol !== 'https:' || new URL(cfg.domain).pathname !== '/' || new URL(cfg.domain).search || new URL(cfg.domain).hash) throw new Error('domain must be an absolute HTTPS origin');
  const domain = new URL(cfg.domain).origin;
  if (!Number.isInteger(cfg.tripDays) || cfg.tripDays < 1 || cfg.tripDays > 365) throw new Error('tripDays must be an integer 1–365');
  if (cfg.days || !cfg.itinerary || !Array.isArray(cfg.itinerary.blocks) || !cfg.itinerary.blocks.length) throw new Error('Use explicit itinerary.slug and itinerary.blocks; legacy days/heuristic config is not accepted');
  const bySlug = new Map(articles.map(a => [a.slug, a]));
  const sections = new Map();
  function source(slug) {
    const a = bySlug.get(slug);
    if (!a) throw new Error(`Selected source slug absent from export: ${slug}`);
    if (a.status !== 'published') throw new Error(`${slug}: selected source must explicitly have status published`);
    nonempty(a.title, `${slug}.title`); nonempty(a.content, `${slug}.content`);
    if (!sections.has(slug)) sections.set(slug, localAdapter({ mode: 'sections', html: a.content, base_url: `${domain}/article/${encodeURIComponent(slug)}` }));
    return a;
  }
  function section(slug, heading) {
    const a = source(slug); nonempty(heading, `${slug}.heading`);
    const hits = sections.get(slug).filter(s => s.heading === heading);
    if (hits.length !== 1) throw new Error(`${slug}: exact H2 heading must occur once: ${heading} (found ${hits.length})`);
    if (hits[0].unsupported?.length) throw new Error(`${slug}: selected section contains ${hits[0].unsupported.join(', ')}; compose a structured PDF section explicitly instead of flattening it`);
    if (!hits[0].body.trim()) throw new Error(`${slug}: source section is empty: ${heading}`);
    return { body: hits[0].body, url: `${domain}/article/${encodeURIComponent(slug)}`, copiedFrom: { slug, title: a.title, heading, contentSha256: sha256(a.content), bodySha256: sha256(hits[0].body) } };
  }
  const itinerary = source(cfg.itinerary.slug);
  if (itinerary.destination && cfg.site?.destination && itinerary.destination !== cfg.site.destination) throw new Error('Declared source destination differs from configured destination');
  let nextDay = 1;
  const days = cfg.itinerary.blocks.map((block, i) => {
    if (['place', 'region', 'title', 'body', 'morning', 'afternoon', 'evening'].some(key => key in block)) throw new Error('Do not relabel or replace source blocks; use their exact heading and full source text');
    if (!Number.isInteger(block.startDay) || !Number.isInteger(block.endDay) || block.startDay !== nextDay || block.endDay < block.startDay || block.endDay > cfg.tripDays) throw new Error('Itinerary day ranges must cover the trip in order without gaps or overlaps');
    const copied = section(itinerary.slug, block.heading);
    const namedRange = block.heading.match(/^(?:days?|jours?|d[ií]as?)\s+(\d+)(?:\s*[-–—]\s*(\d+))?\b/i);
    if (namedRange && (Number(namedRange[1]) !== block.startDay || Number(namedRange[2] || namedRange[1]) !== block.endDay)) throw new Error(`Mapped days do not match the source heading: ${block.heading}`);
    nextDay = block.endDay + 1;
    return { n: i + 1, title: block.heading, startDay: block.startDay, endDay: block.endDay, ...copied };
  });
  if (nextDay !== cfg.tripDays + 1) throw new Error(`Itinerary mapping ends on day ${nextDay - 1}, but tripDays is ${cfg.tripDays}`);
  const slots = cfg.beforeYouGo?.slots;
  const links = cfg.backCover?.links;
  if (!Array.isArray(slots) || !Array.isArray(links)) throw new Error('beforeYouGo.slots and backCover.links must be explicit arrays');
  const items = slots.map(s => {
    if ('body' in s || 'role' in s || 'signals' in s) throw new Error('Before-you-go slots require an explicit slug and H2 heading, without body overrides or signals');
    return { title: nonempty(s.title, 'slot.title'), ...section(s.slug, s.heading) };
  });
  const backLinks = links.map(l => {
    const a = source(l.slug);
    return { label: nonempty(l.label, 'link.label'), url: `${domain}/article/${encodeURIComponent(a.slug)}`, sourceTitle: a.title };
  });
  return {
    schema_version: 2, tripDays: cfg.tripDays,
    site: { ...cfg.site, domain }, cover: cfg.cover || { title: itinerary.title }, atAGlance: cfg.atAGlance || null,
    beforeYouGo: { heading: cfg.beforeYouGo.heading, items }, days, costs: cfg.costs || null,
    backCover: { heading: cfg.backCover.heading, blurb: cfg.backCover.blurb, links: backLinks }, theme: cfg.theme || {},
    provenance: { ...provenance, generatedAt: new Date().toISOString(), sourceTitle: itinerary.title },
    review: { status: 'pending', factual: 'pending', destinationAndDayMapping: 'pending', visual: 'pending', links: 'pending', note: 'Source copying and structural checks do not verify travel facts or endorse a route. Inspect every rendered page and selected source before distribution.' },
  };
}
export function suggestions(raw, cfg) {
  const articles = articlesFrom(raw);
  return { kind: 'suggestions-only', buildable: false, tripDays: cfg.tripDays ?? null,
    candidates: articles.filter(a => a.status === 'published' && typeof a.content === 'string').map(a => ({ slug: a.slug, title: a.title, headings: localAdapter({ mode: 'sections', html: a.content }).map(s => s.heading) })) };
}
export function main(argv) {
  if (argv.includes('--help')) { console.log(HELP); return 0; }
  const args = options(argv, [], ['--suggest']);
  if (args.positional.length !== 3) throw new Error(HELP);
  const [exportPath, configPath, output] = args.positional;
  distinctOutput(output, [exportPath, configPath]);
  const raw = readJSON(exportPath), cfg = readJSON(configPath);
  const data = args['--suggest'] ? suggestions(raw, cfg) : compileLeadmagnet(raw, cfg, { exportSha256: sha256(readFileSync(exportPath)), configSha256: sha256(readFileSync(configPath)) });
  atomicWrite(output, JSON.stringify(data, null, 2) + '\n');
  console.log(`${args['--suggest'] ? 'Suggestions only' : 'Draft manifest'} written: ${output}`);
  return 0;
}
if (isMain(import.meta.url)) { try { process.exitCode = main(process.argv.slice(2)); } catch (e) { console.error(e.message); process.exitCode = 1; } }
