# Setup Runbook — Phases 0–4 (empty correct site)

The repeatable sequence to stand up a new site. Target: under ~90 minutes of active work
once the template exists. Clone the template repo (the clean, current monorepo), then fill
`SITE_CONFIG` — every site-specific value lives there.

> These runbook phases cover the BUILD/SETUP steps (the hands-on, outside-the-chat work).
> They run AFTER the in-chat planning (design → categories → article list) is approved. The
> phase numbers below are local to this runbook, not the 8-step order in SKILL.md.

## Phase 0 — Clone (10 min)
- `git clone` the template into a new repo named for the site.
- Two apps inside: `apps/site`, `apps/admin`. Confirm both install: `npm install`.
- Strip nothing by hand — the template carries NO site identity; everything specific is set
  in `SITE_CONFIG` and the per-site design step.

## Phase 1 — Schema (10 min)
- Decide the site's Postgres schema (`SITE.dbSchema`, e.g. `japan`) — co-hosted sites each
  get their own schema, never `public` (see schema-and-seed.md).
- In Supabase → SQL Editor, create the schema and run `assets/schema.sql` then `assets/seed.sql`
  inside it (`create schema if not exists <schema>;` then set search_path, or qualify tables).
- **Expose the schema to the Data API:** Settings → API → add `<schema>` to **Exposed schemas**
  AND to the **Extra search path** (both — an exposed-but-not-in-search-path schema still
  returned "Invalid schema" in practice).
- **RLS read policies:** if RLS is on, add an `anon` SELECT policy on `categories` and
  `articles` (the public site reads via the anon key) — else the menu/articles come up empty
  even though the admin (service role) works.
- Replace the seed's placeholder names/slugs with the project's real taxonomy (from its
  facts.json), in the site's language. Keep the 6-main structure.
- Verify: 6 main categories (`parent_id` null) + their subcategories exist.
- See `schema-and-seed.md` for the verification query and the `getNavigation()` function.

### Adding a NEW table later (e.g. site_settings) — migration discipline
Cost a failed migration on site #2. Before writing any new migration:
- **Read the existing migrations first** (`supabase/migrations/0001_init.sql`, and any
  0002+). Match their conventions exactly — do NOT write from memory of "how Supabase
  usually works."
- **search_path**: the Supabase SQL editor defaults to the `public` schema (the #1 cause
  of "column/table not found" or the table landing in the wrong schema). Put
  `set search_path to <schema>;` at the TOP of the migration, then create tables UNQUALIFIED
  (same as 0001). Everything else is schema-agnostic via `current_schema()`.
- **Every new table needs THREE things, not just CREATE TABLE:**
  1. the table,
  2. GRANTS (anon/authenticated SELECT, service_role all),
  3. RLS enable + an explicit anon-read policy.
  Omit (2) or (3) and you get the silent trap: works in the admin (service_role bypasses
  RLS) but the public site reads NOTHING (RLS-by-default blocks anon; missing grants 500).
- Number the file to continue the sequence (0002_, 0003_, …). The template ships
  `0002_site_settings.sql` as the canonical example.

## Phase 2 — Config (20 min)
- Fill `packages/config/site.ts` (`SITE_CONFIG`): domain, language, audience, brand
  colours, fonts, media folder, affiliate programs. See `site-config.md`.
- Confirm no hardcoded domains/URLs remain anywhere in the codebase.

## Phase 3 — Services (20 min)
- **R2:** nothing to provision. A folder is born from its first object, so
  `SITE.media.folder` simply starts being used. The bucket (`fleet-media`) and the delivery
  host already exist fleet-wide.
- **Vercel:** create two projects (site + admin) or one with two roots; point the domain
  (`www` + apex) to the site; set the admin subdomain (`admin.<domain>`).
- **Canonical URL:** pick www or apex and make everything agree — the Vercel redirect,
  `NEXT_PUBLIC_SITE_URL`, and therefore the sitemap/robots/canonical tags. A mismatch
  (sitemap lists apex while the site 308-redirects to www) muddies indexing.
- **Env vars:** Supabase URL + anon key + service role key on BOTH apps, plus
  `NEXT_PUBLIC_MEDIA_HOST` on both. The three `R2_*` secrets go on the **ADMIN ONLY** — the
  site merely reads public URLs and never needs write credentials. Also `ADMIN_PASSWORD`,
  `ADMIN_SESSION_SECRET`, any affiliate keys. Missing env on one app is a classic "works
  locally, breaks on deploy" trap. Vercel freezes these at BUILD time, so **redeploy after
  adding any of them**. (Schema is NOT an env var — it lives in `SITE.dbSchema`.)

## Phase 4 — Verify (15 min)
- Deploy a **preview** build (not production) first.
- Check: admin loads, login works, the public site menu **renders from the database**
  (add a test category in the admin → it appears in the menu within the revalidate window).
- Check article/category/home pages render with `revalidate = 60`.
- **Sitemap check (critical):** load `/sitemap.xml` — it must list real `/article/...` URLs,
  not just the static pages. An empty sitemap means a DB client wasn't schema-pinned (the
  recurring bug). Confirm `/robots.txt` allows crawling and points to the sitemap.
- Submit the sitemap in Google Search Console (verify the domain via a DNS TXT record).
- Only then promote to production.

### Launch specifics (from site #2's go-live)
- **If the domain is registered WITH Vercel**, you don't touch any registrar: just add the
  apex domain in the SITE project (apps-site, NOT apps-admin) → Settings → Domains. Vercel
  auto-configures apex + www + DNS records + SSL. Adding just the apex is enough; Vercel
  wires www to it. (External registrar = copy Vercel's A/CNAME records there instead.)
- **Add the domain to the SITE project only** — confirm it's apps-site, not apps-admin.
- **Sitemap sanity**: it generates from the DB, so it populates once live; confirm it ends
  with `</urlset>` (not cut off) and the count ≈ articles + static pages. A `magic-eden`/
  wallet `<script>` you may see in the rendered XML is a BROWSER EXTENSION, not your site.
- **robots.txt** should be `User-Agent: * / Allow: /` plus a `Sitemap:` line — that line lets
  Google auto-discover the sitemap.
- **Set expectations with the user**: after submitting, Search Console shows ~0 indexed for
  days–weeks. That's Google's crawl pace, not a setup error. Don't chase it.

## Definition of done
The site is **empty and correct**: schema seeded, config filled, services wired, admin
working, menu DB-driven, preview verified. Continue (same chat) into `travel-content`.
