# Stage 1 — Architecture

Produce an **empty, correct site + admin + the approved article list**. Every rule here
exists because the bug it prevents was actually hit and paid for. Deep detail lives in
`references/architecture/` — open each file at its phase, not before.

## Core principle: template, not project

Build the template once; every new site is **clone → configure → pour content**. The
template is a NEUTRAL monorepo skeleton (uploaded as a ZIP into the chat — private repo):
it carries structure and behavior, NO site identity. `scripts/skeleton-check.mjs` fails the
build if any component smuggles in a hardcoded mark or a previous site's identity.

## Kickoff (the front door)

A site is built in ONE chat, end to end — this stage, then Stages 2–4 in the same
conversation, with Stage 5 (design) last. Needed to start: this skill + the template ZIP.
facts.json is NOT needed to start (it's built in Stage 2 from this stage's article list).
The site is built on the template's **neutral minimalist look** and only restyled at the end.
Kickoff prompt shape (fill project, domain, destination, audience):

> Build and fill the site for project **<project>** (domain **<domain>**) — a
> **<destination>** travel site for **<audience>**, in this one chat, end to end, using the
> **travel-empire** skill. I've uploaded the neutral template repo zip.
> Work in this order, STOP for my input at each ★:
> 1. ★ Categories — derive the structure from this destination's shape; I approve.
> 2. ★ Article list — 60–80 articles (title + slug + category); I approve.
> 3. Build the empty site on the MINIMALIST TEMPLATE LOOK (SITE_CONFIG, schema + seed,
>    full admin, setup runbook) — no custom design yet.
> 4. Continue into Stage 2 (facts), Stage 3–4 (write + publish the batches).
> 5. ★ Design LAST — once the real site + content exist, restyle it into a distinct
>    identity (3 directions; I pick), applied to the actual built components.

First action on kickoff is the CATEGORIES step — never jump to design or config. Design is
the FINAL stage, applied to the real built site (see Stage 5 / `architecture/design-step.md`).

## Build order (never deviate) — planning before plumbing, design LAST

The site is built on the template's **neutral minimalist look**. No custom design happens in
Stage 1 — it's the final stage (Stage 5), applied to the real built site.

| Phase | What | Read |
|-------|------|------|
| 1 ★ Categories | Derive structure from the destination's SHAPE (below). Becomes the seed. | `architecture/schema-and-seed.md` |
| 2 ★ Article list | 60–80 articles (title + slug + category_slug), tiered by buying intent. THE content contract. | `architecture/article-plan.md` |
| 3 Config | Site values into SITE_CONFIG (incl. `dbSchema`, `planningSlug`, `affiliates`, `media.host` + `.folder` as DISTINCT values, `contact.email` left EMPTY). Design tokens stay at the template's minimalist defaults until Stage 5. | `architecture/site-config.md` |
| 4 Schema | Create the site's OWN Postgres schema; run migration; seed approved categories. | `architecture/schema-and-seed.md` + `assets/schema.sql`, `assets/seed.sql` |
| 5 Admin | Ship the FULL admin feature set — never a subset. | `architecture/admin-spec.md` |
| 6 Services | R2 folder needs no provisioning — it is born from its first object (host ≠ folder — hard rule 10); Vercel project + domain + env on BOTH apps, `R2_*` on admin only. | `architecture/setup-runbook.md` |
| 7 Verify | Preview deploy: admin loads, menu renders from DB, `/sitemap.xml` lists real URLs. | `architecture/setup-runbook.md` |

Design is **Stage 5**, after content is live — see `architecture/design-step.md`. It restyles
the real, populated site, so the approved look is the one that actually ships.

Before writing ANY Next.js file, read `architecture/app-router-rules.md` — every gotcha in
it cost hours (CSS `@import` order, no `cookies()` in layout.tsx, no HTML form
action/method, exact route.ts paths).

## Destination shape — a country is NOT a city

Categories are derived per destination: **country** → cities/regions primary axis +
cross-cutting themes; **city** → neighborhoods + day-trips; **region/route** → stops/legs.
The 6 functional mains (Things to Do, Itineraries, Where to Stay, Food & Drink, Getting
Around, Plan Your Trip) are a default backbone that flexes — never force a city taxonomy
onto a country or vice-versa.

## Non-negotiable architecture rules (each was paid for in production)

- **Single source of truth:** domain, colours, fonts, affiliate IDs ONLY in SITE_CONFIG; no
  hardcoded domains/URLs anywhere.
- **Schema-isolated, schema-pinned** (hard rule 4 in SKILL.md): own Postgres schema, never
  `public`; every client pinned via `db: { schema: SITE.dbSchema }`; schema exposed in the
  Data API and in the Extra search path. A bare `createClient` silently reads/writes the
  wrong site (real bugs: empty sitemap, mis-targeted link injection).
- **Database-driven navigation:** menu from `categories` via `getNavigation()`, never a
  hardcoded navigation.ts.
- **Foreign keys, not name strings:** articles → `category_id`. Renames must never break links.
- **Slugs come from the DB, never typed by hand:** homepage/hero/quick-links generated from
  real rows (guessed slugs shipped broken links once).
- **Versioned schema:** all schema in `supabase/migrations/*.sql`; never ad-hoc UI changes.
- **Imagery is content-driven and curated:** category tiles render
  `categories.featured_image` (gradient fallback); homepage hero is hand-curated via
  `is_featured` + `featured_order` — never auto-"newest N". These columns ship in the schema
  from day one.

Proven components ship in the template unchanged: `getNavigation()`, DB-driven Header,
HeroSlideshow, CategoryTiles, globals.css with correct import order, and the FULL admin
(dashboard, articles manager, editor, media library with usage-checked delete, category
management with tile-image picker, Homepage-hero curation, Export + Batch-update) — see
`architecture/admin-spec.md`.

## Definition of done (Stage 1)

- Repo cloned + named; schema created in its OWN Postgres schema, exposed + in search path;
  migration + seed run with the approved destination-shaped categories; RLS read policies
  for `anon` on categories + articles (or the menu is empty)
- Distinct per-site design NOT done yet — site runs on the template's minimalist look; tokens
  stay at template defaults (design is Stage 5). No hardcoded identity anywhere
  (`skeleton-check` passes); `contact.email` empty; media `host` and `folder` set as
  DISTINCT values in SITE_CONFIG
- Full admin shipped per spec; R2 folder (no provisioning needed); Vercel
  linked, canonical URL (www vs apex) consistent across redirect + `NEXT_PUBLIC_SITE_URL`,
  env on BOTH apps
- Preview verified: admin loads, login works, menu renders from DB, `/sitemap.xml` lists
  real article URLs
- **Article list approved** and saved as `article-list.json` (schema_version 4) — every
  `category_slug` resolving in the DB (pre-flight: one query now beats a broken import later)
- **Swamp list drafted + article list tagged** (same file, same approval): 5–10 real,
  high-stakes, connected decisions of the destination in the top-level `swamps` array —
  hypothesis-grade, an experienced traveler would nod at each — and every article tagged
  `swamp` + `handoff` (`turn`/`seed`/`none`). Most articles are `none`: dry ground stays
  dry. The tags are what Stage 3 writes handoffs from; the dossier build later confirms or
  re-ranks the swamps (its cold-mine wins). Doctrine: SKILL.md "The guide is the center."
- **Opportunity gate run on the whole article list** — every row carries a verdict
  (REJECT / INVESTIGATE / PRODUCE / STRUCTURAL) with a written reason, and
  `predictions.json` exists with one row per PRODUCE candidate, filed BEFORE any writing.
  Nothing enters Stage 2 unscored. Method and thresholds: `references/1c-opportunity-gate.md`
- **`state.json` initialized** from `assets/state-template.json` with
  `stage: "facts", batch: 0` — both files pushed by the user to `travel-facts/<project>/`
- Site is EMPTY and CORRECT → continue in this same chat into Stage 2 (`2-facts.md`)
