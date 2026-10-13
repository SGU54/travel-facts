# Feature blocks (Stages 3–4)

The template ships an enhancer system: articles can carry plain-HTML **feature blocks**
that the site hydrates into interactive maps, live currency, FAQ schema, and TikTok
embeds. They flow through import/clean/link untouched. Conventions:

## Map — `feature-map`

```html
<div class="feature-map" data-points='[
  {"name":"Senso-ji","lat":35.7148,"lng":139.7967,"note":"Go before 9am"},
  {"name":"Tokyo Skytree","lat":35.7101,"lng":139.8107}
]'></div>
```

- Use in itineraries (numbered route pins), where-to-stay (neighborhood pins), day-trips.

### Interactive map implementation (React-Leaflet) — the real contract

The `feature-map` div is inert HTML in the stored article; a client component hydrates it into
an interactive Leaflet map. **Pins come from the block's own `data-points` JSON** — the same
attribute shown in the block above. No DB table, no article fields; the coordinates travel in
the article HTML and flow through import/clean/link untouched.

**The pieces (Thailand repo — replicate per site):**
- `lib/leaflet.ts` — exports `renderMap(el, points, { numbered })`, the SINGLE place Leaflet
  initializes. Both consumers below call it; keep all Leaflet setup (tiles, marker icons, bounds)
  here so there's one source of truth. Returns the `LeafletMap` (or null on failure).
- `lib/mapData.ts` — the `MapPoint` type: `{ name: string; lat: number; lng: number; note?: string }`.
- `components/ThaiMap.tsx` — a `'use client'` React component taking `points: MapPoint[]`, plus
  `height`, `numbered`, `className`. **Lazy:** an `IntersectionObserver` (rootMargin 300px) defers
  `renderMap` until the block nears the viewport, so the map library costs nothing up front. Use
  this for maps placed directly in TSX (e.g. a dedicated map area).
- `components/ArticleEnhancer.tsx` — a `'use client'` component (mounted once per article, scoped
  to `.article-content`) that hydrates the feature blocks that live INSIDE article HTML. For maps:
  finds every `.feature-map`, `parsePoints(dataset.points)` (validates name/lat/lng, range-checks,
  drops malformed), sets a default height (380px), clears fallback text, calls `renderMap`. It also
  hydrates `.feature-converter` and `.feature-price` via `lib/rates.ts` (ECB/Frankfurter). This is
  what makes maps work "in multiple places" — any article carrying a `feature-map` block gets one.

**Leaflet-in-Next rules that always apply:**
- **Client-only.** Leaflet touches `window`; components are `'use client'`. If you ever place a
  map via `next/dynamic`, use `{ ssr: false }` or SSR throws `window is not defined`.
- **CSS + marker icons.** Import `leaflet/dist/leaflet.css`; fix the default-marker-icon path (the
  known Leaflet+bundler issue) or supply a custom `L.icon` inside `renderMap`, or markers break.
- **Deps.** `leaflet` + `react-leaflet` in `apps/site/package.json`; pin react-leaflet's major to
  the installed React major.
- **A11y.** The map container gets `role="region"` + `aria-label`. Map is chrome, so it's exempt
  from "no motion behind paragraphs," but don't autoplay animation.

**⚠ React 18 Strict Mode double-mount (a real scar — handle it):** in dev, effects mount → clean up
→ remount. A naive `renderMap().then(...)` from the tear-down mount will still write to the DOM and
leave a half-hydrated block the remount then skips. Both components guard against this:
- `ThaiMap` captures a local `cancelled` flag per effect; on cleanup it sets `cancelled` and
  `map.remove()`, and the async `.then` bails if `cancelled`.
- `ArticleEnhancer` uses a `live = { current: true }` object (NOT a captured boolean — a stale
  captured flag from the torn-down mount would block the remount's writes), gates every deferred
  DOM write on `live.current`, and **only stamps the persistent `data-tfaHydrated` marker AFTER the
  work lands** — so a torn-down mount never leaves a block that looks hydrated but isn't.
Replicating either pattern per site is fine; the principle is: gate async DOM writes on the current
mount, and only set the "done" marker after the write succeeds.
- **Coordinates are FACTS** (hard rule 1): well-known landmark coordinates are
  `agreed_stable`-class knowledge and may be written directly; for anything obscure, omit
  the map rather than guess. 2–10 points; valid JSON in single quotes; `note` optional.

## Live price — `feature-price` (the serve_live implementation)

```html
…costs <span class="feature-price" data-amount="18" data-currency="EUR">€18</span>…
```

- Local price marked up once; the site appends "(≈ $20 today)" from the live ECB rate.
- This is HOW money is written: stable local prices get the span; exchange RATES are still
  never written into prose at all. `data-amount` numeric, `data-currency` 3-letter ISO.

## Converter — `feature-converter`

```html
<div class="feature-converter" data-from="USD" data-to="EUR">100 USD ≈ … EUR (enable JavaScript)</div>
```

One per money/budget article, near the top. Fallback text inside the div is mandatory.

## FAQ — `feature-faq` (auto-generates FAQPage JSON-LD)

```html
<section class="feature-faq">
  <h2>FAQ</h2>
  <details><summary>Question?</summary><div><p>Answer.</p></div></details>
</section>
```

- 3–6 Q&As at the END of most articles, phrased the way the audience actually searches.
  Answers 1–3 sentences, facts from facts.json. Native `<details>` = works without JS;
  the site emits FAQPage structured data from it automatically.

## TikTok — standard embed

```html
<blockquote class="tiktok-embed" cite="https://www.tiktok.com/@handle/video/ID" data-video-id="ID">
  <a href="https://www.tiktok.com/@handle/video/ID">Watch on TikTok</a>
</blockquote>
```

Only embed OWN-brand videos (cross-promoting the project's TikTok), max 1–2 per article.

## Essentials bar (architecture-side, not in articles)

`SITE_CONFIG.essentials` (homeCurrency, localCurrency, items[]) drives the `EssentialsBar`
component — values from facts.json `agreed_stable` facts ONLY, set during Stage 1 config.
Also feeds the enhancer's home/local currency.

## Pipeline rules

- **Cleaning (Stage 4) must PRESERVE feature blocks**: never strip `feature-*` classes,
  `data-*` attributes, `<details>/<summary>`, or `tiktok-embed` blockquotes.
- **Link injection** already skips non-text nodes; feature blocks are safe.
- **validate-batch.mjs** mechanically checks every block (JSON parses, lat/lng numeric and
  in range, ISO currency, FAQ structure, TikTok cite) — run it before review as always.

## Editable homepage hero (admin + DB) — `site_settings`

Make the homepage hero IMAGE (and optionally eyebrow/title/lead) editable from the admin,
with no redeploy. This is the standard pattern for ANY homepage element you want editable.

Layers (all five ship in the template as of v2):
- **DB**: a single-row `site_settings` table (id boolean PK, singleton check), with columns
  hero_image / hero_eyebrow / hero_title / hero_lead / updated_at. Migration
  `0002_site_settings.sql` — created UNQUALIFIED, with GRANTS + RLS (see the migration
  discipline in schema-and-seed.md and setup-runbook Phase 1). Run it per site in the
  site's schema (set search_path first).
- **API**: `apps/admin/app/api/hero-settings/route.ts` (GET/POST) using `createServiceClient`
  (auto-pins SITE.dbSchema, so it writes the right schema with no per-call work).
- **Admin UI**: `apps/admin/app/hero-image/page.tsx` — REUSES the existing MediaPicker
  ({open,onClose,onSelect:(publicId,url)=>void}); preview + save + remove. Do NOT build a
  new picker.
- **Public read**: `getHeroSettings()` in packages/db/queries.ts, with a SAFE try/catch
  fallback → returns empty if the table doesn't exist yet, so the site never breaks if the
  migration hasn't run.
- **Resolution order** in page.tsx: DB value → SITE.ui.heroImage config fallback → flat motif.

The hero photo MUST be a dedicated landing image (not an article photo), rendered under a
heavy dark gradient (~30–62%, darker toward the text band) with per-element text-shadows on
eyebrow/lead; drop the sun motif when a photo is set (photo + motif is too busy).

This pattern generalizes: future editable bits (announcement bar, theme toggles) go in the
same single-row site_settings table.

## Standard site-wide UX/SEO feature set (ship these by DEFAULT)

Beyond the in-article feature blocks above, every site should ship the following baseline of
chrome/UX/SEO components. These were added by hand on the Turkey build and should instead be part
of the template/standard so each site has them from the start. All are **no-API / no-cost** and
must typecheck clean. Group them so they're not forgotten:

**Article reading experience**
- **Reading time** — computed from content word count (~225 wpm). Show in the article meta row
  AND on article cards. (`lib/article.ts: readingTimeMinutes`.)
- **Table of contents** — auto-built from the article's `<h2>`s, sticky in a sidebar, scroll-spy
  highlight (IntersectionObserver). Only render for 3+ sections. Desktop only. Inject stable `id`s
  into the h2s server-side so anchors work. (`lib/article.ts: extractHeadings` + `TableOfContents`.)
- **Reading progress bar** — thin accent line fixed to viewport top, fills on scroll.
- **Back-to-top** — floating button after scrolling down.
- **End-of-article CTA** — link to the itinerary picker / a next step.

**Navigation / structure**
- **Breadcrumbs** — Home / Category / Title on article + category pages (light & dark variants).
- **Styled 404** (`app/not-found.tsx`) — on-brand, with the signature motif + links home/search.

**SEO (structured data + feeds)**
- **JSON-LD**, emitted via a small `lib/jsonld.tsx` helper:
  - `Organization` + `WebSite` (with `SearchAction`) in the root layout.
  - `Article` + `BreadcrumbList` on every article.
  - `FAQPage` ONLY when the article has 2+ real Q&A pairs (extract from question-style h2s or the
    `feature-faq` block) — never emit empty/fake FAQ schema.
- **Canonical URL + per-page OpenGraph** in each page's metadata.
- **RSS feed** at `app/feed.xml/route.ts` (recent articles) + a discovery `<link>` in layout.
- **sitemap.ts + robots.ts** already ship — they depend on `NEXT_PUBLIC_SITE_URL` (see go-live).

**Accessibility**
- **Skip-to-content link** + `<main id="main">` in the layout.
- Visible focus states, `prefers-reduced-motion` guards (template ships these).
- `loading="lazy"` on below-fold images; `fetchPriority="high"` on the above-fold hero image.

**Homepage planning value (grounded in facts.json — static, no API)**
- **Trust strip** — 3–4 headline facts (visa rule, flight time, best months, guide count). The
  guide count can be live from `getPublishedSlugs().length`.
- **Best-time strip** — a 12-month visual of when to visit, ratings from `when_to_go.best_months`.
- **Cost cheatsheet** — the 2–3 daily-budget tiers from `costs.*`, framed as ranges with an honest
  "rates move, check a converter" nudge (never a fixed promise).
- **Itinerary picker** — the client-side router described in design-step.md (days × interests →
  real articles). Make these editable via `SITE.ui.*` config with sensible defaults baked in.

Keep all of the above driven by config/tokens and verified against real content (every routed slug
must exist). They are the difference between "a list of articles" and a site that feels designed
and useful.

## Lead magnet — the free email-gated PDF (ship at every launch)

A proven conversion feature: offer a free, well-designed PDF (a printable itinerary
built from content you ALREADY have) in exchange for an email. The email goes to the
newsletter provider; the download is revealed instantly on submit. No backend, no
email round-trip, no cost.

**The two halves:**

1. **Generate the PDF — EXPLICIT source selection, from the article export (2026-10-11
   rewrite — see SKILL-CHANGES.md).** Relevance-SCORING picked sections automatically; it
   had no check that the picked source's own destination matched the site being built, and
   a wrong/stale export file could silently feed one site's itinerary into another's
   config. The rewrite removes scoring entirely in favor of explicit, verified selection:
   - `scripts/leadmagnet-data.mjs EXPORT.json CONFIG.json OUTPUT.json [--suggest]` requires
     config `schema_version: 2`: `domain` (absolute `https://` origin), `tripDays`,
     `itinerary.slug` (the exact source article — no scoring, no day-count heuristic) with
     `itinerary.blocks: [{heading, startDay, endDay}]` naming each block's EXACT existing
     `<h2>` heading text, which must occur exactly once in that article and must cover
     `1..tripDays` contiguously with no gaps or overlaps. `beforeYouGo.slots` and
     `backCover.links` name `{slug, heading}` the same explicit way — no signal-term
     scoring, no "best match wins." A selected source must explicitly carry
     `status: "published"`. The script copies each named section's text verbatim (via the
     Python HTML adapter, `scripts/html-tools.py` — needs `pip install -r
     scripts/requirements.txt`) and stamps `contentSha256`/`bodySha256` provenance hashes
     per block into the output manifest, so a later edit to the source article is visible
     rather than silently baked into a stale PDF. Run with `--suggest` first on an
     unfamiliar corpus — it reports candidate slugs/headings without producing a buildable
     manifest, so you pick explicitly rather than guessing blind.
   - `<config.json>` (`assets/leadmagnet-config-template.json`, schema_version 2) declares
     the explicit slug/heading map, cover/glance copy, cost tiers, theme. Disagree with a
     pick? Change the named `slug`/`heading` directly — there is no scoring to tune.
   - Then `scripts/build-leadmagnet.mjs DATA.json OUTPUT.pdf [--chrome=/path] [--html-only]`
     renders the schema_version 2 manifest to PDF via local Playwright + a local Chromium
     (`TRAVEL_EMPIRE_PYTHON` overrides the Python interpreter), inheriting the site's brand
     tokens (`theme` block); `--html-only` writes a reviewable HTML proof without attempting
     a PDF. A failed render never replaces a previous PDF. The cover is a FULL-BLEED POSTER
     on the site's own dark chrome — set `theme.coverInk` / `theme.coverPaper` to retune it
     (defaults derive from `accentDeep` / `paper`, so each site gets its own, never a
     borrowed one). `scripts/build-leadmagnet-all.mjs EXPORT.json CONFIG.json OUT_DIR`
     chains both steps.
   - **Cost pages: find the real figures BEFORE designing the page.** Search in this
     order — (1) `common.facts` key `money.cost_tiers` (the canonical home for
     drift-prone figures, rendered live by `CostCheatsheet.tsx`), (2)
     `SITE.ui.costTiers` / `costSection` (config fallback + the site's own copy),
     (3) the site components (`CostCheatsheet`, `TripBudget` — how it's framed and
     how trip totals are computed), (4) article HTML LAST, which is often empty by
     design. Mirror the site's tiers and copy so the PDF reads as the same
     publication. A tier card renders `perDay`/`total` as a price table, or
     `figure` + `note` as a titled point — it never prints a labelled slot with no
     value behind it. Only if all four sources are empty is the corpus genuinely
     priceless; then change what the page IS (e.g. money mechanics: fees, DCC,
     tipping) rather than shipping the furniture of a price table with the prices
     removed.
   - **Check the rendered artifact, not just the config.** Rasterize the PDF and
     look at each page; measure fill (lowest content row as % of page height) —
     under ~65% the page reads as padding and should be merged. Every layout bug
     found on Thailand (empty time-slot labels, a `DAY 1 OF 3` kicker on a 7-day
     trip, two half-empty front pages) was invisible in the source files.

2. **Gate + deliver** — `components/LeadMagnet.tsx` + `app/api/subscribe/route.ts`
   (both ship in the template). CAPTURE-ONLY by default — you OWN the list in your
   Supabase; no email provider needed to launch.
   - `LeadMagnet.tsx` reads `SITE.leadMagnet` (`enabled`, `title`, `subtitle`,
     `blurb`, `pages`, `pdfUrl`, `cta`). Disabled or no `pdfUrl` → renders nothing.
   - On submit it POSTs to `/api/subscribe`, then reveals the `pdfUrl` download
     immediately (the reader gets the PDF instantly; the POST just confirms capture).
   - The route upserts the email into `common.subscribers` (migration
     `0009_subscribers.sql` — attributed by `site_key`, like `link_clicks`, so the
     list is queryable across the fleet and yours to keep). Only env needed:
     `SUPABASE_SERVICE_ROLE_KEY` (server-only). Fail-soft: a DB hiccup still reveals
     the download.
   - **Sending a welcome email is OPTIONAL and OFF by default.** A clearly-marked
     block at the end of the route is where a sender plugs in later — Cloudflare
     Email Service (sends from any Cloudflare routing domain → fits a multi-domain
     fleet) or Resend (clean API, but free tier = 1 domain, so a multi-site fleet
     needs paid). No rush; the list collects from day one. See the template's
     `docs/LEAD_MAGNET_SETUP.md`.
   - **Placement — coordinated with the guide (5c-conversion.md).** On a site
     WITH a live paid guide, the free magnet must NOT compete with paid surfaces on
     the same page: it lives in the FOOTER site-wide, and takes the homepage prime
     slot ONLY as the fallback when the guide is dark (`{guide.live ? <GuideHomeBand/>
     : <LeadMagnet/>}`). Do NOT drop it inline in the article body when a paid guide
     is live — that recreates free-vs-paid head-to-head (the balance the placement
     doctrine exists to prevent). On a site with NO paid guide, the old default is
     fine: homepage after `BestTimeStrip`, footer, and optionally inline. The
     `variant="inline"` prop still exists; just don't use it in article bodies
     alongside a live guide.

**NOTE:** the leadMagnet is the FREE gated PDF; `ProductPromo` is for PAID products
only (Gumroad/Lemon Squeezy). They're separate — don't route the free PDF through
ProductPromo (it's a direct link with no email gate).

**Launch step:** fill `SITE.leadMagnet` + set `SITE.newsletter.enabled` with a real
`endpoint`, generate the PDF from the destination's flagship itinerary, host it, drop
its URL in `pdfUrl`. One email-list-building asset per site, at ~zero marginal cost.

## Affiliate slots — the monetization layer (placed at writing, managed centrally)

Articles carry affiliate SLOTS by intent, never URLs. A slot names a ROLE; the
vendor, the site's aff_id, and the actual link are resolved at render through the
/go/ route. A slot becomes a live link ONLY when its role is configured (enabled
program + policy + this site's enabled credential with a real id) — otherwise it
renders as plain prose (fail-closed). So slots are placed generously up front and
light up as approvals land, fleet-wide, with zero article edits.

**Writing (3-writing.md):** the writer drops slots where a reader is ready to act —
`<span class="aff" data-aff="hotels">stay in Trastevere</span>`,
`<span class="aff" data-aff="tours" data-item="colosseum">skip-the-line tickets</span>`.
Roles = the KEYS of SITE.affiliates (hotels/tours/flights/rail/insurance). Inner text
is real, complete prose (the fallback). Role-only = search-style (always resolves);
`data-item` only for a specific product the vendor supports.

**Render:** `apps/site/lib/affiliate.ts` (`resolveAffiliates`) resolves slots after
facts, before heading extraction — DOM-based, fail-closed. Live role → `/go/{role}/
{item|_}` link with `rel="sponsored nofollow noopener"` + `.aff-link` (styled per
site in the design step). Dormant role → unwrapped to prose. `getConfiguredAffiliate
Roles()` (db) is the one query that decides.

**Management (two surfaces, same tables):** `packages/affiliate-admin/` ships a
drop-in `AffiliateManager` + `makeAffiliateActions`. Fleet console (pass `fleet`):
programs/vendors/URL-templates + fleet-default policy + any site's credentials.
Admin (pass `siteKey`): this site's ids + overrides. The on-switch is a row in
`affiliate_site_credentials`. Or set it by SQL — see `AFFILIATE_ACTIVATION.sql`.

**Design step:** decide how `.aff-link` looks in this site's identity (inline accent
+ outbound affordance by default; can be a card). Same slot, site-coherent look.
