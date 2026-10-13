# Stage 5c — The conversion layer (the guide's own surfaces)

Renders the on-site surfaces that sell this site's guide. Runs during/after Stage 5
design, only on a site whose guide has a checkout link. Doctrine: SKILL.md "The guide
is the center." Terminology: **"ad" = this site's own ad for its guide. There is no
third-party advertising anywhere in the fleet** — every surface points at the guide.

**Scope is a contract — and it splits with the marketing skill:**
- **5c (this file) owns the MOUNTS**: the components, where each renders in the page
  tree, the config contract, the gates, and the `/go/` measurement plumbing. The
  machinery.
- **The marketing skill owns the THINKING that fills them**: the hook copy (M1), the
  per-site visual adaptation (M2), the sales-page copy (M3), and **the site-wide
  placement doctrine — which pages get which surface, intent-gated (M4)**.

When this file says "the placement doctrine decides X," it means: read the marketing
skill's `surface-map.md`, don't re-derive it here. 5c builds the slots; marketing
decides which fire on which page and what they say. Keep that line clean — if 5c
starts specifying hook wording or 5c starts inventing placement rules, the two skills
have drifted into each other.

NOT under this stage at all: email, social, traffic acquisition, analytics
dashboards. If a task here seems to need an external ad unit, the task is misread.

## The seven surfaces

Built in two waves. The **core four** are the article/route surfaces; the **M4 three**
are the higher-intent placements added once the core works.

| # | surface | slot | job |
|---|---------|------|-----|
| 0 | `/guide` sales page | route | the destination — everything else points here |
| 1 | end-of-article band | `article-end` | close the finished reader (hottest lead) |
| 2 | inline marker | `article-inline` | contextual door at the swamp's bite point |
| 3 | sticky aside | `article-aside` | ambient persistent presence (rides with TOC) |
| 4 | category band | `category-foot` | foot of a **logistics** category listing |
| 5 | tool callout | `build-my-trip` | under the trip-builder result (peak intent) |
| 6 | home band | `home-primaryslot` | homepage prime slot (replaces free magnet) |

**Placement is intent-gated, ONE primary band per page — see marketing
`surface-map.md` for the authoritative map.** The rule 5c enforces mechanically:

- **Article page:** the aside (#3) is ambient and rides every article. The *band*
  slot is mutually exclusive — a **swamp** article shows the paid end band (#1); a
  **dry** article shows the site's Keep-planning / Build-your-trip band instead;
  **never both dark bands stacked.** The inline slot splits BY BREAKPOINT
  (v5.1, mounted in article/[slug]):
    · **desktop (`lg+`)**: the inline *marker* (#2), swamp articles ONLY —
      connective copy needs a door;
    · **phone (`lg:hidden`)**: the inline *card* (#2b, `GuideInlineCard`) on
      EVERY live article, dry included — the phone has no rail, so these
      readers never meet the aside; the swamp decides what the surface SAYS
      (asideHooks[swamp] → asideHooks.default → thesis), not whether it shows.
      Never both at one breakpoint.
  So: swamp article = end band + aside + inline(marker|card); dry article =
  keep-planning band + aside (+ card on phone); density stays <= 2 besides the
  aside at any breakpoint.
- **Category page:** the band (#4) renders ONLY on logistics categories (Where to
  Stay, Getting Around, Itineraries, Plan Your Trip) via a wet-map; dry categories
  (Food, Things to Do) render nothing.
- **Homepage:** the paid home band (#6) takes the prime slot when the guide is live;
  the free lead magnet is the fallback shown only when the guide is dark (and stays
  site-wide in the footer regardless).
- **Trip-builder:** the callout (#5) under the planner result — the site's peak
  sequencing intent.
- **Free lead magnet:** footer only (+ homepage dark-fallback). It never competes
  with a paid surface on the same page. This separation is the free/paid balance —
  paid owns high-intent real estate, free catches everyone else for the list.

## The config contract (fail-closed, like affiliates)

The contract splits IDENTITY (config, set once at guide build) from OPERATOR
fields (DB, flippable from the admin with no redeploy). Do not put price /
checkout / the toggle back into config — the whole point is that going
live/dark is an admin action, not a deploy.

**IDENTITY — `SITE_CONFIG.guide`, ships EMPTY on every new site:**

```ts
guide: {
  name:         '',   // from dossier Stage A3, user-confirmed (same string the
                      // admin "Name backfill" writes into every guide-span)
  thesis:       '',   // one-line master hook, from A3 (strengthened by marketing M1)
  cover:        '',   // object key -- WEB export of the dossier cover, ~2000px, inside the
                      // site's folder, NEVER at the bucket root. A print export is ~158
                      // megapixels and Cloudflare refuses anything over 100 (error 9413).
                      // host != folder (hard rule 10). Build URLs via mediaUrl().
                      // NOTE: an id with no slash gets the site folder prepended;
                      // a ROOT upload must carry its version prefix (e.g.
                      // 'v1784608353/Cover_ab12') so the slash skips the prepend.
                      // '' = the CSS MiniCover fallback -- a cover is NOT required
                      // to go live.
  pages:        '',   // e.g. '47 pages'
  decisions:    0,    // REAL count from the shipped build -- never invented (#1)
  failureModes: 0,    // REAL count
  figures:      0,    // REAL count

  // Hook doors. All swamp id -> line. Marketing M1 writes these; 5c only reads them.
  hooks:        {} as Record<string,string>, // BAND-shaped (image + twist, 2 beats)
  asideHooks:   {} as Record<string,string>, // SHORTEST form (a question) -- aside.
                                             // The 'default' key is the no-swamp
                                             // variant the phone InlineCard uses.
  inlineHooks:  {} as Record<string,string>, // CONNECTIVE line (bridges article ->
                                             // guide synthesis; not a repeat of hook)
  inlineCtas:   {} as Record<string,string>, // benefit CTA per swamp for the inline
                                             // surface (never the guide's title)
  teaserBySwamp: {} as Record<string,number>,// swamp -> index into decisionTeasers,
                                             // so the aside leads with the reader's door

  decisionTeasers: [] as string[], // real decisions, named by question -- richer aside
  previewImages:   [] as string[], // object keys of REAL spreads -- "see inside"
},
```

**OPERATOR — `site_settings` (migrations 0005 + 0006), managed from the admin
"Guide" panel:** `guide_ads_enabled` (THE switch), `guide_checkout_url`,
`guide_price`, `guide_cover` (optional override of the config cover; '' =
fall back to config — clearing the picker is non-destructive).

**The gates, exactly as `apps/site/lib/guide.ts` implements them:**
`guideConfigured()` = `name && thesis` (identity present), and
`state.live` = `guideConfigured() && guide_ads_enabled && checkout_url !== ''`.
Cover is NOT gated (MiniCover CSS fallback). Every surface (INCLUDING the
`/guide` route and its sitemap entry) renders nothing / 404s unless
`state.live`. A site whose guide isn't built shows clean articles, no dead
widgets, no empty sales page -- exactly how dormant affiliate roles behave.

**Per-surface hooks fail OPEN.** Each variant map is optional: a surface falls back
to the band `hooks`, then to `thesis`, never to broken/empty copy.

```ts
// apps/site/lib/guide.ts -- the resolver returns a GuideState; surfaces read it.
export const hookFor = (state, swamp?: string | null) =>
  (swamp && state.hooks?.[swamp]) || state.thesis || '';
// aside uses:  (swamp && state.asideHooks[swamp]) || hookFor(state, swamp)
// inline uses: state.inlineHooks[swamp] || hookFor(state, swamp)
```

`getGuideState()` reads config + the DB settings row (`ads_enabled`, `checkout_url`,
`price`) and returns `{ live, name, thesis, price, cover, pages, decisions,
failureModes, figures, hooks, asideHooks, inlineHooks, decisionTeasers,
previewImages }`. All seven components consume this one object.

## Caching -- the surfaces gate on a runtime toggle, so DON'T static-cache the gate

`ads_enabled` can flip at any moment from the admin. Any page whose *live-ness*
depends on it must read the current state per request, or the first request after a
toggle serves a stale result:

- **`/guide` MUST be `export const dynamic = 'force-dynamic'`.** With ISR
  (`revalidate`), the first click after going live serves the `notFound()` that was
  cached while the guide was dark -- the **first-click-404 bug**. Force-dynamic fixes it.
- **`/go/guide/[src]` is already `force-dynamic`** (a redirect always runs fresh).
- **Article pages** stay on their normal `revalidate` (e.g. 60s) -- a briefly-stale
  surface after a toggle self-corrects within the window, and keeping article pages
  static preserves performance on the highest-traffic pages. Acceptable trade.

## Where the article's swamp comes from at render

`article-list.json` (schema v4) is repo-side; the render layer reads the DB. One
migration -- **Stage 1 territory (hard rule 9), run as a Stage 1 addendum, never from
a content stage:**

```sql
alter table <site_schema>.articles
  add column if not exists swamp text;  -- null = dry ground
```

Stage 4's import step carries `swamp` from the article list into the import JSON and
the upsert. Pre-doctrine articles have null -> treated as dry. No backfill of live
sites uninvited. Tagging an article's swamp after the fact is a targeted UPDATE --
Postgres forbids ORDER BY/LIMIT directly on UPDATE, so match one row via a subquery:
`update <schema>.articles set swamp='base' where id = (select id from ... order by ...
limit 1);`

## Measurement -- reuse `/go/`, build nothing

Click-logging to `common.link_clicks` already exists (the `/go/` route, wired at
fleet onboarding). Guide clicks follow the SAME path-segment grammar as affiliates --
one `src` per surface so per-surface conversion is queryable:

```
/go/guide/end-band?article=<slug>          -> log, 302 -> /guide
/go/guide/inline?article=<slug>            -> log, 302 -> /guide
/go/guide/aside?article=<slug>             -> log, 302 -> /guide
/go/guide/home                             -> log, 302 -> /guide
/go/guide/build-tool                       -> log, 302 -> /guide
/go/guide/category-<category-slug>         -> log, 302 -> /guide
/go/guide/sales-page                       -> log, 302 -> SITE.guide.checkout_url
```

`guide` is a reserved role in the /go/ handler: internal sources redirect to the
sales page; `sales-page` (the buy button) redirects to checkout. The handler logs
`role='guide'`, `item=src`, `article` slug and redirects -- it accepts ANY `src`, so
new surfaces (like `category-<slug>`) are captured automatically with no handler
change. **Do not build attribution beyond the click** -- sales truth lives in the
checkout provider's dashboard.

Every surface reads `state.live` and returns `null` when dark, so the /go/ links
never appear on a dark site.

## The core four -- mounts

- **#0 `/guide` sales page** (`app/guide/page.tsx`, async server, `force-dynamic`):
  `notFound()` unless `state.live`. Structure is the marketing skill's M3
  architecture (hero cover+thesis -> the stake from real failure modes -> what's-inside
  with the REAL decisions/failureModes/figures counts -> provenance marks -> refusals ->
  Field Sheet promise -> close). Exactly TWO buy CTAs (hero + close), routed through
  `/go/guide/sales-page`. Optional "see inside" section renders the `previewImages`
  spreads, fail-closed (nothing until filled). Sitemap: include `/guide` ONLY when
  ready. The COPY is marketing's; 5c owns the route, the gate, the caching, the CTAs'
  plumbing.
- **#1 end band** (`components/guide/GuideEndBand.tsx`, server): mounted in the
  article template AFTER the body, in the mutually-exclusive band slot (see placement
  rule above). Dark ground -> saffron-type kicker legal; wax-red CTA. `/go/guide/end-band`.
- **#2 inline marker** (`components/guide/GuideInlineMarker.tsx`, server): swamp
  articles only, mounted between body chunks via a **read-only h2-boundary split of
  the render copy (never injected into the stored HTML string, hard rule 3)**. The
  LIGHTEST surface -- a connective keyline (no box), using `inlineHooks`. `/go/guide/inline`.
- **#3 sticky aside** (`components/guide/GuideAside.tsx`, server; sticky via CSS):
  mounted in the TOC rail. **The aside and the TOC must share ONE sticky wrapper**
  (`<div className="sticky top-24 space-y-8">` around both, with `TableOfContents`
  passed `sticky={false}`) -- two independently-sticky siblings overlap (the
  sidebar-overlap bug). The richer aside carries a larger cover, `decisionTeasers`,
  a FILLED CTA, and the short `asideHooks` question. `/go/guide/aside`.

### The h2-split (surface #2 mechanism)

```ts
// apps/site/lib/split-article.ts -- split rendered HTML before the Nth h2 (1-based),
// with a DOM parser. Returns [whole, ''] when there are too few h2s (marker then
// simply doesn't render mid-body). The stored article is NEVER mutated.
```

```tsx
const showInline = state.live && article.swamp;   // swamp-tagged pages only
const [a, b] = showInline ? splitAtH2(bodyHtml, 2) : [bodyHtml, ''];
<div dangerouslySetInnerHTML={{ __html: a }} />
{showInline && b && <GuideInlineMarker state={guide} slug={article.slug} swamp={article.swamp} />}
{b && <div dangerouslySetInnerHTML={{ __html: b }} />}
```

If the split lands badly on a given article, the fix is the split index, not
hand-placed HTML.

## The M4 three -- mounts

- **#4 category band** (`components/guide/GuideCategoryBand.tsx`): mounted at the foot
  of the category listing (`app/category/[slug]/page.tsx`). Self-gates on a wet-map
  (category slug -> swamp door); returns `null` for dry categories. Its wet-map is the
  5c-side mechanism; WHICH categories are wet and which door each opens is the
  marketing surface-map's call — the map SHIPS with fleet-default entries
  (where-to-stay→base, getting-around→arrival, itineraries/plan-your-trip→booking)
  that the marketing pass ADAPTS to this site's category slugs and swamp ids;
  an entry that matches nothing on this site never fires (fail-closed). A door
  no category opens (e.g. Rome's `money`) is only reachable through articles —
  tag them or accept it dark. Dark ground, `/go/guide/category-<slug>`.
- **#5 tool callout** (`components/guide/GuideToolCallout.tsx`): mounted under the
  planner result in `app/build-my-trip/page.tsx`. Uses the sequencing (booking) door.
  `/go/guide/build-tool`.
- **#6 home band** (`components/guide/GuideHomeBand.tsx`): mounted in the homepage
  prime slot with the free lead magnet as the `!state.live` fallback:
  `{guide.live ? <GuideHomeBand/> : <div...><LeadMagnet/></div>}`. Dark featured
  treatment, the cover doing the visual selling. `/go/guide/home`.

## Design rules (this is design work, not widget work)

- **Every surface derives from THIS site's tokens.css** -- the same identity Stage 5
  shipped. Greece's surfaces belong to "Come Up For Air"; Rome's to "La Tavola". A
  generic widget shipped across sites has already failed. This is the marketing
  skill's M2 (adaptation) -- done against the LIVE rendered site, not the dossier's
  printed palette, and it must echo the site's EXISTING CTA grammar (the free
  lead-magnet button is the template to rhyme with).
- **A surface that looks like an ad has failed.** These are the site recommending its
  own deeper work -- a publisher pointing at its own book. Editorial voice, never
  banner grammar; the cover (a real designed artifact) does the visual selling. The
  cold "does this read as an ad?" screenshot check is the operator's permanent gate.
- **Watch the token traps** (each caught real bugs): a "decorative only" token used as
  text/CTA fails AA; an accent that's legal only on dark grounds leaks onto paper; a
  display face with no bold weight can't take `font-extrabold`; a token that exists in
  `tokens.css` as a CSS var is NOT automatically a Tailwind utility. Sample the REAL
  token names, don't assume.
- Copy: plain verbs, the hook line, the name, benefit-CTAs (not "See {name}" but
  "See the sequence that gets you home"). No urgency theater, no countdown, no
  "LIMITED". The buy CTA is wax-red (the site's primary action hue), echoing the free
  magnet's button shape.
- Quality floor: AA contrast against this site's palette, real characters not
  entities, keyboard focus visible, no fake affordances (hard rule 12), never
  static-as-live (hard rule 13 -- the price is config, shown as configured, fine).

## Definition of done (Stage 5c, one site)

`SITE.guide` filled (name from A3, checkout link live, cover uploaded incl. correct
version-prefix if root, thesis + all hook maps in, real counts); migration run,
import carries `swamp`; `/guide` renders (force-dynamic) and is in the sitemap;
per-page placement holds (swamp article = end band + aside + inline; dry article =
keep-planning band + aside; logistics category = band; homepage = paid band; trip
tool = callout; free magnet footer-only); never two dark bands stacked; TOC + aside
share one sticky wrapper (no overlap); every link routes through `/go/guide/*` and
rows land in `common.link_clicks`; all surfaces restyled to this site's identity in
the design pass (marketing M2); with `SITE.guide` emptied / `ads_enabled` off, every
surface disappears and `/guide` 404s (the fail-closed proof -- test it).

## What NOT to do

No third-party ads (they don't exist here). No email/social/traffic work under this
stage's name. No surfaces inside the body HTML string. No retrofit of live sites
uninvited. No new analytics (reuse /go/; the checkout provider owns sales truth).
No hardcoded guide name or destination anywhere -- config only, sourced from A3 (the
one label that names the destination reads `The {SITE.destination} guide`). **Do not
write hook copy or invent the placement map here** -- that's the marketing skill; 5c
mounts what marketing produces. **Do not static-cache `/guide`** (first-click-404).
Reference example for every surface, fully built: the Rome repo ("Rome, Solved." /
"La Tavola") -- the template inherits its shape, empty.
