#!/usr/bin/env node
/**
 * validate-batch.mjs — Stage 4, steps 0 and 7.
 * Runs every MECHANICAL quality-gate check so the human checklist stays judgment-only.
 * Inspection is read-only, so simple pattern checks are allowed here (the DOM-only hard
 * rule applies to MUTATION).
 *
 * Usage:
 *   node scripts/validate-batch.mjs <import-batch-NN.json> [--folder <media-folder>] [--disclosure "<site disclosure string>"]
 *   node scripts/validate-batch.mjs <import-batch-NN.json> --list article-list.json   # + the 3b gates
 *   node scripts/validate-batch.mjs <import-batch-NN.json> --facts facts.json [--as-of YYYY-MM-DD]
 *   node scripts/validate-batch.mjs --preflight <import-batch-NN.json>     # category check vs DB
 *
 * --list enables the gates that need the plan (references/3b-vein-and-citability.md):
 * answer-first, pre-join (vein), guide-span. Without it they SKIP — a v4 list with no
 * vein block is a valid site, not a failure.
 *
 * --facts checks provenance (source, date checked, scope) for every <span class="fact"
 * data-fact="KEY"> actually present in the batch, via validate-facts.mjs (2026-10-11 merge
 * from the GPT rewrite — see SKILL-CHANGES.md). If fact spans exist and --facts is NOT
 * given, this is a hard FAIL (a marked claim with nothing to check it against is worse
 * than an unmarked one). Without any fact spans in the batch, --facts is a no-op.
 *
 * Preflight needs SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, SUPABASE_DB_SCHEMA in env
 * (load them from apps/admin/.env.local — never inline on the command line).
 * If they're absent, preflight warns and skips rather than failing.
 */
import { readFileSync } from "node:fs";

const args = process.argv.slice(2);
const preflight = args.includes("--preflight");
const file = args.find(a => a.endsWith(".json"));
const opt = (flag) => { const i = args.indexOf(flag); return i >= 0 ? args[i + 1] : null; };
if (!file) { console.error("Usage: node scripts/validate-batch.mjs [--preflight] <import-batch-NN.json> [--folder f] [--disclosure s]"); process.exit(1); }

const raw = JSON.parse(readFileSync(file, "utf8"));
const articles = Array.isArray(raw) ? raw : raw.articles;
if (!Array.isArray(articles)) { console.error("Import file must be an array or {articles:[...]}"); process.exit(1); }

const fails = [], warns = [];
const F = (slug, msg) => fails.push(`FAIL  ${slug}: ${msg}`);
const W = (slug, msg) => warns.push(`warn  ${slug}: ${msg}`);

const strip = html => html.replace(/<[^>]*>/g, " ").replace(/\s+/g, " ").trim();
const AFFIL = /booking\.com|getyourguide|gyg\.me|viator\.com|skyscanner|safetywing|ivisa|tp\.media|travelpayouts/i;
const FROZEN = /(?:[€$£¥]\s?1|1\s?(?:USD|EUR|GBP))\s?(?:=|≈|equals|is about)\s?[\d.,]+|exchange rate (?:of|is) [\d.,]/i;
const disclosureArg = opt("--disclosure");
const DISCLOSURE_FALLBACKS = [/affiliate links/i, /enlaces de afiliado/i, /liens d.affiliation/i, /affiliate-links/i];

async function preflightCheck() {
  const { SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, SUPABASE_DB_SCHEMA } = process.env;
  if (!SUPABASE_URL || !SUPABASE_SERVICE_ROLE_KEY || !SUPABASE_DB_SCHEMA) {
    console.warn("preflight: Supabase env not set (load apps/admin/.env.local) — SKIPPING DB checks.");
    return;
  }
  const h = { apikey: SUPABASE_SERVICE_ROLE_KEY, Authorization: `Bearer ${SUPABASE_SERVICE_ROLE_KEY}`, "Accept-Profile": SUPABASE_DB_SCHEMA };
  const get = async t => { const r = await fetch(`${SUPABASE_URL}/rest/v1/${t}?select=slug`, { headers: h }); if (!r.ok) throw new Error(`${t}: HTTP ${r.status}`); return new Set((await r.json()).map(x => x.slug)); };
  const cats = await get("categories");
  const existing = await get("articles");
  for (const a of articles) {
    if (!cats.has(a.category_slug)) F(a.slug, `category_slug "${a.category_slug}" not in DB schema "${process.env.SUPABASE_DB_SCHEMA}"`);
    if (existing.has(a.slug)) W(a.slug, "slug already in DB (import will skip it — idempotent)");
  }
  console.log(`preflight: ${cats.size} categories, ${existing.size} existing articles checked (schema ${SUPABASE_DB_SCHEMA}).`);
}

const usedFactKeys = [];

function contentChecks() {
  const folder = opt("--folder");
  if (!articles.length) { F("batch", "empty batch — zero articles"); return; }
  if (articles.length !== 5) W("batch", `${articles.length} articles (expected 5)`);
  for (const a of articles) {
    const slug = a.slug || "(no slug)";
    for (const k of ["slug", "title", "content", "category_slug", "excerpt", "featured_image"])
      if (!a[k]) F(slug, `missing "${k}"`);
    if (!a.content) continue;
    const c = a.content;

    const words = strip(c).split(" ").filter(Boolean).length;
    if (words < 800 || words > 1600) F(slug, `${words} words — outside the sanctioned 800–1600 envelope`);
    else if (words < 1000 || words > 1200) W(slug, `${words} words — outside the 1000–1200 default band (OK only for sanctioned types)`);

    const internal = [...c.matchAll(/<a\s[^>]*href="\/article\/([^"]+)"/g)].map(m => m[1]);
    if (internal.length > 3) F(slug, `${internal.length} internal links (max 3)`);
    if (internal.includes(a.slug)) F(slug, "links to itself");
    const dupes = internal.filter((s, i) => internal.indexOf(s) !== i);
    if (dupes.length) F(slug, `double-links target(s): ${[...new Set(dupes)].join(", ")}`);
    if (/<h[1-4][^>]*>(?:(?!<\/h)[\s\S])*?<a\s/i.test(c)) F(slug, "link inside a heading");

    if (/<!--\s*IMAGE_SLOT/i.test(c)) F(slug, "unresolved IMAGE_SLOT comment");
    for (const img of c.match(/<img\b[^>]*>/g) || [])
      if (!/alt="[^"]+"/.test(img)) F(slug, "an <img> lacks descriptive alt text");
    if (folder && a.featured_image && !a.featured_image.startsWith(folder))
      F(slug, `featured_image not under folder "${folder}"`);

    if (FROZEN.test(strip(c))) F(slug, "frozen exchange-rate / serve_live value detected in prose");

    if (AFFIL.test(c)) {
      const hasDisc = disclosureArg ? c.includes(disclosureArg) : DISCLOSURE_FALLBACKS.some(r => r.test(c));
      if (!hasDisc) F(slug, "affiliate link(s) present but no disclosure found");
    }
    if (/sex tourism|red.light guide/i.test(strip(c))) F(slug, "prohibited content pattern (hard rule 7) — review immediately");
    if ("status" in a) W(slug, "'status' field present — import API ignores it (always draft)");

    for (const m of c.matchAll(/<span\b[^>]*class="[^"]*\bfact\b[^"]*"[^>]*data-fact="([^"]*)"/g)) {
      if (!/^[\w.[\]-]+$/.test(m[1])) F(slug, `fact span has an invalid data-fact key: "${m[1]}"`);
      else usedFactKeys.push(m[1]);
    }

    // ── feature blocks (references/5-features.md) ──
    for (const m of c.matchAll(/class="feature-map"[^>]*data-points='([^']*)'/g)) {
      try {
        const pts = JSON.parse(m[1]);
        if (!Array.isArray(pts) || !pts.length) throw new Error("empty");
        for (const p of pts) {
          if (!p.name || typeof p.lat !== "number" || typeof p.lng !== "number" ||
              Math.abs(p.lat) > 90 || Math.abs(p.lng) > 180)
            throw new Error(`bad point ${JSON.stringify(p)}`);
        }
        if (pts.length > 10) W(slug, `feature-map has ${pts.length} points (>10 gets cluttered)`);
      } catch (e) { F(slug, `feature-map data-points invalid: ${e.message}`); }
    }
    for (const m of c.matchAll(/class="feature-price"[^>]*?data-amount="([^"]*)"[^>]*?data-currency="([^"]*)"/g)) {
      if (!isFinite(parseFloat(m[1]))) F(slug, `feature-price amount "${m[1]}" not numeric`);
      if (!/^[A-Za-z]{3}$/.test(m[2])) F(slug, `feature-price currency "${m[2]}" not 3-letter ISO`);
    }
    for (const m of c.matchAll(/<section[^>]*class="[^"]*feature-faq[^"]*"[^>]*>([\s\S]*?)<\/section>/g)) {
      const qa = (m[1].match(/<details[^>]*>\s*<summary/g) || []).length;
      if (!qa) F(slug, "feature-faq section has no <details><summary> pairs");
      else if (qa < 3) W(slug, `feature-faq has only ${qa} Q&A (3–6 recommended)`);
    }
    for (const m of c.matchAll(/<blockquote[^>]*class="[^"]*tiktok-embed[^"]*"([^>]*)>/g)) {
      if (!/cite="https:\/\/www\.tiktok\.com\//.test(m[1])) F(slug, "tiktok-embed missing a tiktok.com cite URL");
    }
  }
}

// ─────────────────────────── BEGIN 3b GATES ───────────────────────────
// references/3b-vein-and-citability.md — answer-first · pre-join · guide-span.
// Self-contained: paste this block + the `--list` line in the usage header into any
// other copy of validate-batch.mjs (the template repo carries its own).

const BANNED_OPENERS = /^(it|its|it's|this|that|that's|these|those|they|here|the same|as (?:mentioned|noted|discussed|explained|we saw|above))\b/i;

function firstBlockAfterEachH2(html) {
  // FAQ/feature sections carry their own shape — they are not answer-first chunks.
  const body = html.replace(/<section[^>]*class="[^"]*feature-[^"]*"[^>]*>[\s\S]*?<\/section>/gi, " ");
  const out = [];
  const re = /<h2\b[^>]*>([\s\S]*?)<\/h2>([\s\S]*?)(?=<h2\b|$)/gi;
  let m;
  while ((m = re.exec(body))) {
    const heading = strip(m[1]);
    const after = m[2];
    const p = after.match(/<p\b[^>]*>([\s\S]*?)<\/p>/i);
    out.push({ heading, text: p ? strip(p[1]) : "" });
  }
  return out;
}

function answerFirstChecks(a) {
  const slug = a.slug || "(no slug)";
  const blocks = firstBlockAfterEachH2(a.content);
  if (!blocks.length) { W(slug, "no <h2> found — answer-first gate had nothing to check"); return; }
  for (const b of blocks) {
    const label = b.heading.slice(0, 42);
    if (!b.text) { F(slug, `H2 "${label}" has no paragraph under it (answer-first)`); continue; }
    const n = b.text.split(/\s+/).filter(Boolean).length;
    if (n < 25) { F(slug, `H2 "${label}" opens on ${n} words — under the 25-word floor (answer-first)`); continue; }
    if (BANNED_OPENERS.test(b.text))
      F(slug, `H2 "${label}" opens on a back-reference ("${b.text.split(/\s+/)[0]}…") — restate the subject (answer-first)`);
    if (n < 40 || n > 80) W(slug, `H2 "${label}" opening block is ${n} words (target 40–80)`);
    const head = b.text.split(/(?<=[.!?])\s/)[0] || b.text;
    if (!/\d/.test(head) && !/(?!^)\b[A-Z][a-z]{2,}/.test(head))
      W(slug, `H2 "${label}" opening sentence names no entity and gives no number`);
  }
}

function veinChecks(a, vein, planned) {
  const slug = a.slug || "(no slug)";
  if (!vein || !Array.isArray(vein.pieces) || !vein.pieces.length) return;
  const max = Number.isInteger(vein.max_pieces_per_article) ? vein.max_pieces_per_article : 2;
  const text = strip(a.content);
  const fires = (p, s) => { try { return new RegExp(p.match, "i").test(s); } catch { return false; } };
  for (const p of vein.pieces) { try { new RegExp(p.match, "i"); } catch { W(slug, `vein piece "${p.id}" has an invalid match regex — skipped`); } }

  // MENTION (article level) is only a signal — a keyword metric lies (10 recorded cases).
  const mentioned = vein.pieces.filter(p => fires(p, text)).map(p => p.id);
  if (mentioned.length > max)
    W(slug, `mentions ${mentioned.length} vein pieces (${mentioned.join(", ")}) — check the passages below actually stay separate`);

  // JOIN (2-sentence window) is the real pre-join: this is where the guide's work gets given away.
  const sents = text.split(/(?<=[.!?])\s+/).filter(Boolean);
  let worst = { n: 0, ids: [], win: "" };
  for (let i = 0; i < sents.length; i++) {
    const win = sents.slice(i, i + 2).join(" ");
    const ids = vein.pieces.filter(p => fires(p, win)).map(p => p.id);
    if (ids.length > worst.n) worst = { n: ids.length, ids, win };
  }
  if (worst.n > max)
    F(slug, `pre-join: ${worst.n} vein pieces (${worst.ids.join(", ")}) joined inside 2 sentences — cut the JOINING sentence, keep the facts. → "${worst.win.slice(0, 120)}…"`);

  const tagged = planned && planned.piece;
  if (tagged && tagged !== "none" && !mentioned.includes(tagged))
    W(slug, `tagged piece "${tagged}" but its match never fires — the article may not actually feed the vein`);
}

function guideSpanChecks(a, planned) {
  const slug = a.slug || "(no slug)";
  if (!planned) return;
  const handoff = planned.handoff || "none";
  const spans = [...a.content.matchAll(/<span\b[^>]*class="[^"]*\bguide\b[^"]*"[^>]*>([\s\S]*?)<\/span>/gi)];
  const named = spans.filter(m => /data-guide="name"/i.test(m[0]));
  if (handoff === "none" && spans.length) F(slug, `handoff "none" but ${spans.length} guide-span(s) present`);
  if (handoff !== "none" && !named.length) F(slug, `handoff "${handoff}" but no <span class="guide" data-guide="name">`);
  if (spans.length > 2) F(slug, `${spans.length} guide-spans (max 2)`);
  for (const m of named) if (!strip(m[1])) F(slug, "guide-span has empty gloss text (fail-closed contract broken)");
  if (/\{\{/.test(a.content)) F(slug, "literal {{ token in content — the span contract replaces tokens");
}

function listChecks() {
  const listPath = opt("--list");
  if (!listPath) { console.log("(--list not given → answer-first / vein / guide-span gates skipped)"); return; }
  let list;
  try { list = JSON.parse(readFileSync(listPath, "utf8")); }
  catch (e) { F("list", `cannot read --list ${listPath}: ${e.message}`); return; }
  const vein = list.vein || null;
  const byslug = new Map((list.articles || (Array.isArray(list) ? list : [])).map(x => [x.slug, x]));
  if (!vein) console.log("(list has no vein block → pre-join gate skipped; v4 lists are valid)");
  for (const a of articles) {
    if (!a.content) continue;
    const planned = byslug.get(a.slug);
    if (!planned) W(a.slug, "slug not in article-list.json — plan and batch have diverged");
    answerFirstChecks(a);
    veinChecks(a, vein, planned);
    guideSpanChecks(a, planned);
  }
}
// ──────────────────────────── END 3b GATES ────────────────────────────

async function factsCheck() {
  const factsArg = opt("--facts");
  const uniqKeys = [...new Set(usedFactKeys)];
  if (!uniqKeys.length) return;
  if (!factsArg) { F("facts", `${uniqKeys.length} fact span(s) marked but no --facts registry given — nothing checks their provenance`); return; }
  let validateFacts;
  try { ({ validateFacts } = await import("./validate-facts.mjs")); }
  catch (e) { F("facts", `cannot load validate-facts.mjs: ${e.message}`); return; }
  let registry;
  try { registry = JSON.parse(readFileSync(factsArg, "utf8")); }
  catch (e) { F("facts", `cannot read --facts ${factsArg}: ${e.message}`); return; }
  const asOf = opt("--as-of") || new Date().toISOString().slice(0, 10);
  const result = validateFacts(registry, { asOf, usedKeys: uniqKeys });
  for (const e of result.errors) F("facts", `${e.path || ""}: ${e.message}`);
  for (const w of result.warnings) W("facts", `${w.path || ""}: ${w.message}`);
}

(async () => {
  if (preflight) await preflightCheck().catch(e => F("preflight", e.message));
  else { contentChecks(); listChecks(); await factsCheck(); }
  warns.forEach(w => console.warn(w));
  fails.forEach(f => console.error(f));
  console.log(`\n${fails.length ? "❌ " + fails.length + " failure(s)" : "✅ mechanical checks passed"} — ${warns.length} warning(s).`);
  if (!fails.length && !preflight) console.log("Proceed to the human judgment gate (SKILL.md).");
  process.exit(fails.length ? 1 : 0);
})();
