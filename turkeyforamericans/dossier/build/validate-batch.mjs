#!/usr/bin/env node
/**
 * validate-batch.mjs — Stage 4, steps 0 and 7.
 * Runs every MECHANICAL quality-gate check so the human checklist stays judgment-only.
 * Inspection is read-only, so simple pattern checks are allowed here (the DOM-only hard
 * rule applies to MUTATION).
 *
 * Usage:
 *   node scripts/validate-batch.mjs <import-batch-NN.json> [--folder <cloudinary-folder>] [--disclosure "<site disclosure string>"]
 *   node scripts/validate-batch.mjs --preflight <import-batch-NN.json>     # category check vs DB
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

function contentChecks() {
  const folder = opt("--folder");
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

(async () => {
  if (preflight) await preflightCheck().catch(e => F("preflight", e.message));
  else contentChecks();
  warns.forEach(w => console.warn(w));
  fails.forEach(f => console.error(f));
  console.log(`\n${fails.length ? "❌ " + fails.length + " failure(s)" : "✅ mechanical checks passed"} — ${warns.length} warning(s).`);
  if (!fails.length && !preflight) console.log("Proceed to the human judgment gate (SKILL.md).");
  process.exit(fails.length ? 1 : 0);
})();
