# Stage 4 — Publishing

Get a written, second-gated batch of 5 live: clean → build import → images → import as
draft → internal links → affiliates → validate → human review → publish. Commands run from
the repo root; R2 + Supabase creds load from `apps/admin/.env.local` (never inline
keys on the command line — hard rule 4).

**Update `state.json.batch_status` after every step below** (`cleaned` → `imported` →
`linked` → `monetized` → `published`) and have the user push it. This is what makes a
half-finished batch resumable.

## 0. Pre-flight

`node scripts/validate-batch.mjs --preflight <batch-dir>` — confirms every `category_slug`
in this batch resolves in the DB and that `schema_version`s match. One query now beats a
broken import later.

## 1. Clean (DOM, never regex — hard rule 3)

Normalise with a parser (cheerio/DOMParser): proper H2→H3→H4 hierarchy (demote runaway
sibling-H2 chains); merge orphaned single-sentence paragraphs; strip empty tags, stray
`wp-block-*` classes, `<strong>` inside headings. Production scar that justifies the rule:
raw string replacement once spliced a link into the middle of the word "simplifican" and
broke an `<img>` tag. Treat content as a tree, always. **PRESERVE feature blocks** (`feature-*` classes, `data-*` attributes, `<details>/<summary>`, `tiktok-embed` blockquotes) — see `references/5-features.md`. **PRESERVE the span contracts:** `span.fact` (fact-spans), `span.aff` (affiliate slots), and `span.guide` (guide handoffs, hard rule 15) must pass through cleaning byte-identical — element, class, `data-*`, and inner text. Stripping a guide-span silently kills the name backfill sitewide.

## 2. Build `import-batch-NN.json` (the contract, schema_version 3)

Array (or `{ "articles": [...] }`) of 5 objects:

```json
{
  "slug": "stable-slug",
  "title": "Article title",
  "content": "<p>Full article HTML…</p>",
  "category_slug": "visas-and-documents",
  "excerpt": "1–2 sentence summary",
  "featured_image": "<site-folder>/articles/<slug>-hero"
}
```

- `featured_image` is a **bare object key** (prefixed with `SITE_CONFIG.media.folder`), with
  NO extension — see hard rule 10; in-body images become full delivery URLs at step 3.
- `category_slug` resolves to `category_id` via the import API (FK — must exist; pre-flight
  caught this). Never a name string. A `status` field, if present, is IGNORED — everything
  lands as **draft**.

## 3. Images — the ONE mechanism: `scripts/upload-batch.mjs` (site repo)

This is the only image path; the old IMAGE_SLOT-injector flow is retired. The script reads
import-batch-NN.json to learn each article's expected IDs (hero + in-body, in order), takes
a folder of images sorted by download order, previews the mapping table, and uploads to
Cloudflare R2 only after you confirm. Count mismatch → it STOPS and shows both lists. Re-runs
safe (overwrite=true).

**Prerequisite:** `upload-batch.mjs` imports the S3 client. If the repo hasn't installed it,
the run dies with `ERR_MODULE_NOT_FOUND: '@aws-sdk/client-s3'`. Once per repo:
```
npm install @aws-sdk/client-s3
```
The R2 endpoint carries the jurisdiction: `<account>.eu.r2.cloudflarestorage.com`. Omitting
the `.eu.` yields a host that does not resolve and fails at TLS handshake.
Creds still come from `apps/admin/.env.local` (never inline on the CLI — hard rule 4).

```
node scripts/upload-batch.mjs <images-folder> <import-batch-NN.json>
```

Produce a `batch-NN-images.md` manifest (ordered, matching the IDs) so the user knows
exactly what to download and in what order.

### 3.5 Convert slots → real figure tags (MANDATORY — the #1 broken-site cause)

`upload-batch.mjs` ONLY uploads to R2. It does NOT touch the article body. You MUST
now rewrite the body (via the DOM, never regex) so every `<!-- IMAGE_SLOT_n -->` becomes a
real figure tag:

```html
<figure><img src="https://<HOST>/cdn-cgi/image/format=auto,width=1200/<FOLDER>/articles/<slug>-n" alt="descriptive alt" loading="lazy" /></figure>
```

- `<HOST>` = `SITE_CONFIG.media.host` (`img.sgfleetmedia.com`) — NOT the folder (hard rule 10).
- `<FOLDER>` = `SITE_CONFIG.media.folder` (e.g. `thailandforamericans`).
- **`width=1200` is mandatory, not decoration.** With no width, Cloudflare serves the ORIGINAL
  at full resolution — several megabytes into a 700px column. Every migrated site has body
  images without a width; no new article may.
- No `q_auto` equivalent is emitted: Cloudflare's quality scale is 1-100 and defaults to 85.
  Options must be emitted in SORTED order — two equivalent URLs in different orders are billed
  as two separate transformations.
- Hero = `featured_image` = the `-hero` id, template-rendered, **not** in the body. In-body
  figures use the `-1`, `-2`, … suffixes in order. Keep `loading="lazy"` on every img; alt
  from the slot brief. `mediaUrl()` in `packages/config/site.ts` builds the URL.
- Leave `<!-- AFFILIATE_SLOT -->` comments in place — the affiliate stage consumes them.

**Pass condition: grep the finished import JSON for `IMAGE_SLOT` → ZERO matches.** A surviving
comment renders as a blank gap on the live page (bodies render via `dangerouslySetInnerHTML`).
Real Thailand bug: 159 in-body images shipped as comments and were invisible until converted.

### Hand the user a CONTACT SHEET, not a list of links

**This is the standing workflow.** A markdown file of gallery-search URLs makes the user
click through every result just to *see* a photo. Instead:

1. **Look at the candidates yourself.** Search, open each promising result, visually
   verify it matches the brief, and check it is really free (not Unsplash+) and really
   the right country before including it.
2. **Publish a visual picker as an Artifact** — organised by batch, then by hero/body
   slot, one card per candidate with its caption and a link to its source page. The user
   reviews and marks picks in the page; the choices persist, and they copy a summary back
   into chat.
3. **Two candidates per slot** wherever two genuinely good options exist. A slot with one
   strong option after real searching can ship with one — do not force a weak second just
   to reach two.
4. **Flag the hard slots** in the same artifact, with a distinct visual note, and
   recommend the background-photo + AI-prompt route rather than forcing a poor fit.

Technical note: Unsplash's `og:image` meta tag on a photo's detail page, with the query
string stripped, gives a clean CDN path (`images.unsplash.com/photo-<id>`) that takes
resize/compression parameters — good enough to render a card without downloading.

> Confirmed as the ongoing standard by the user, twice: the first contact sheet drew
> explicit positive feedback and one addition (the second candidate per slot).

**Before you source anything new, check what the project already has.**
`<site>/content/batch-*/images/` accumulates every photograph downloaded for every
previous batch. One project's dossier shipped with six plates while 168 usable landscape
frames sat in that folder. The same applies in reverse: images sourced for the book are
available to the articles.

### If you fall back to links, the manifest carries CANDIDATE SEARCH LINKS, not just briefs

The user sources images by hand (no stock-photo API), so the manifest must do the
"what do I even search for" work for them. For **each** expected image (hero + any in-body),
the manifest entry has three parts:

1. **The target** — the object key (bare, no extension) and the download order number.
2. **A one-line brief** — what the image should show, framed for the article's subject and
   audience (e.g. "welcoming sunlit piazza, no recognizable faces" for a safety article —
   never crime/police imagery).
3. **2–4 candidate links** the user clicks through to pick + download from.

**Link rules (learned from real runs — follow exactly):**
- **Use Unsplash and Pexels only.** Their gallery-search URLs are *constructed* and always
  resolve: `https://unsplash.com/s/photos/<query>` and
  `https://www.pexels.com/search/<query>/` (URL-encode spaces as `%20`). Include a specific
  verified photo-page link too when web_search surfaced one (e.g.
  `https://unsplash.com/photos/<slug-id>`), since those are pre-vetted single shots.
- **Do NOT include Wikimedia Commons category links unless you have verified each one
  resolves** with a search first. Guessed `Category:...` paths are frequently wrong (they use
  exact, unintuitive names) — a dead link costs the user a click and erodes trust in the
  manifest. Default: skip Wikimedia; Unsplash + Pexels cover the subjects.
- **These are pages to PICK from, not guaranteed direct-download URLs.** State this in the
  manifest. The user still eyeballs each chosen image for: live, ≥1600px landscape, license
  OK (Unsplash/Pexels = free commercial, no attribution), and **no recognizable faces or
  brand/logo signage** (the project's standing image rule).
- To build good links, run a few `web_search` queries for the batch's distinct subjects
  (landmarks, food, neighborhoods) and lift the specific photo-page URLs that come back;
  pair each with the constructed gallery link as a fallback.
- **Queries are photo-TAG words (subject + place), NEVER a slugified brief sentence.** Build
  from the concrete subject: `thailand-temple`, `bangkok-street-food`, `railay-beach` — strip
  articles/adjectives, keep noun + locale. Give 2–3 angles per slot. (Real bug: manifests once
  slugified the brief sentence and truncated it, producing searches like
  `visitors%20appropriately%20dressed%20at` and `a%20montage%20feel%20of` that returned
  garbage.) Do TWO searches before giving up on a slot — reformulate if the first is thin.
- **Flag hard/composite slots with ⚠ and give a fallback.** Some briefs describe a scene that
  barely exists free ("shoes outside a temple") or isn't one photo at all ("a montage of
  temple, mountains and island"). Mark ⚠ and tell the user: widen to the strongest single
  on-theme shot rather than hunting the literal scene. A strong thematic image beats a forced
  literal one.

Hero-per-article is the project default; only add in-body candidate links when the article
actually carries `IMAGE_SLOT` comments. Keep the manifest in download order so it lines up
with `upload-batch.mjs`.

## 4. Import (bulk, draft, idempotent)

POST import-batch-NN.json to the admin import API — or from the terminal use the template's
CLI companion, which talks to the SAME authenticated admin API (identical behaviour:
category_slug resolution, upsert-by-slug):

```
node scripts/articles-batch.mjs update import-batch-NN.json
```

Idempotent — existing slugs are skipped, so re-running a batch is safe. Everything lands as
draft (hard rule 5). (`articles-batch.mjs export` also exists for the offline-edit
round-trip: export a cluster → edit JSON → update.) → state `imported`.

## 5. Internal links — resolve the map, then inject (site repo)

Two scripts, then the injector. **Publish FIRST** — all three read the PUBLISHED DB
and validate every target slug; run them before publishing and nothing resolves.
Sequence: import (draft) → **publish** → 5a resolve → 5 inject → 5b Start Here.
All take `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`, `SUPABASE_DB_SCHEMA` from
env (never inline — hard rule 4).

### 5a. Build the map — `scripts/pick-links.mjs`

Replaces hand-authoring `links-map.json`. It reads the corpus and, per article,
derives a subject phrase → **prose-verifies** it (keeps only phrases that occur
in ≥1 OTHER article's body — the load-bearing filter; a phrase no other article
says is dead weight) → resolves the target → **drops ambiguous ties** (top two
too close, e.g. "bangkok" → 5 guides). No review gate: confident phrases
auto-link, ambiguous ones auto-drop. It writes `scripts/links-map.json`.

```
node scripts/pick-links.mjs              # dry — glance at the log (linked N, dropped M)
node scripts/pick-links.mjs --apply      # writes scripts/links-map.json
```

- **Plan-first.** If `article-list.json` declares `links` (see article-plan.md),
  they're merged on top: a declared `{phrase,slug}` overrides the resolved
  target AND rescues a phrase the resolver dropped as ambiguous. Declared intent
  always wins; the resolver only fills what the plan left unsaid. The script
  auto-finds `article-list.json` next to it, or pass `--plan <file>`.
- Conservative by default (favor dropping over guessing). `--gap N` loosens/
  tightens (higher = stricter, fewer links); `--max-per-target N` caps phrases
  per slug (default 3).
- **You may still hand-add exotic domain phrases** the script can't infer
  ("Blue Cruise", "whirling dervishes") — append them to `links-map.json`, or
  better, declare them as `links` in the plan so they survive a re-run.
- Healthy result (Thailand, 80 articles): ~69 clean phrases, the 4 genuinely
  ambiguous ones dropped — matching the quality of a hand-made map.
- **Orphans are OK — do NOT force them.** An ambiguous phrase becomes NO link,
  never a bad one. Orphans are still reached via nav + homepage.

### 5. Inject — `scripts/inject-links.mjs` (unchanged)

DOM-based injector; reads `scripts/links-map.json` (`[{ "phrase", "slug" }]`).
Walks **text nodes only** (skips h1–h4, a, img, figure, code), wraps the first
safe occurrence, max 3 links/article, never self-links or double-links a target,
validates every target against the DB, schema-pinned via `.env`.

```
node scripts/inject-links.mjs            # dry run — eyeball the preview
node scripts/inject-links.mjs --apply    # write
```

**Gotcha:** the injector reads `scripts/links-map.json` specifically. If 5a wrote
it elsewhere, copy it there first, or the dry run shows **0 links** and looks broken.

### 5-facts. Seed any new facts (if the batch spanned them)

If Stage 3 appended a block to `travel-facts/<project>/<site>-facts.sql`, run that block now
(SQL editor, service role). Until it runs, the batch's fact-spans render their written
fallback text (harmless but static). The file is append-only and idempotent (upserts) —
re-running the whole file is safe. After seeding, the DB owns the values; the weekly
checker (`scripts/check-facts.mjs`, pass 3) maintains them.

### 5b. Start Here path — `scripts/pick-start-here.mjs`

Picks the homepage six-step first-timer path (entry → season → route → anchor
city → money → safety) from published articles and writes `SITE.ui.startHere`.
**Plan-first:** an article declared with a `role` (see article-plan.md) wins its
step outright; unfilled roles fall back to scoring. <3 steps resolved → the
section stays hidden (fine for a young site — hard rule 12).

```
node scripts/pick-start-here.mjs         # dry — review the 6 picks + reasoning
node scripts/pick-start-here.mjs --apply # writes SITE.ui.startHere (preserves hand-tuned labels)
```

Also ensure `SITE.ui.startHereSection.heading` is set (the section needs it).

Always dry-run first. → state `linked`.

## 6. Affiliates

Separate explicit phase — read `references/affiliates.md`. Programs only from
`SITE_CONFIG.affiliates`, THIS site's IDs, disclosure mandatory. → state `monetized`.

## 7. Validate, review, publish

1. `node scripts/validate-batch.mjs <batch-dir>` — all mechanical checks (word counts, link
   caps, disclosure, frozen-rate detection, alt text, slug existence). Must pass before
   human review.
2. `node scripts/check-images.mjs` — **MANDATORY GATE.** Exits 1 if any referenced image
   fails to resolve, so it can be wired into CI.

   This exists because nothing else ever confirmed, after the fact, that an image REACHES the
   CDN. `validate-batch` checks the JSON; `upload-batch` checks the file COUNT; neither asks
   whether a key actually serves. The gap was invisible for months: one dead image on Thailand,
   **sixty on Turkey** — thirty published articles each missing a hero and a body image,
   shipping a broken image at full width the whole time. Root cause was an upload that exceeded
   a size limit and failed silently.

   Reading the result: **200** = fine. **404** = never uploaded — upload it, or remove the tag.
   A reference left EMPTY renders nothing (the helper returns null and the block is skipped),
   whereas a reference left BROKEN renders a visibly broken image. Empty beats broken.

3. Human reviews each article against the judgment-only quality gate in SKILL.md.
4. Publish via the admin. For large sites use the admin's **bulk-publish** (Publish-all-drafts,
   or filter by category) instead of row-by-row — it only promotes drafts and is idempotent, so
   re-running is safe (see `admin-spec.md`). → state `published`, advance `batch`. When the LAST
   batch publishes (all of `article-list.json` live), go to **Stage 5 — Design**
   (`stage: "design"`), NOT `done`. The site has been on the minimalist template look; now
   it gets its identity, applied to the real, populated site.
5. First batch of a new site: submit the sitemap to Search Console (Domain property, DNS
   TXT verification).

## 8. Stage 5 — Design (after all batches are live)

Read `references/architecture/design-step.md`. Restyle the BUILT, populated site into a
distinct per-site identity — verifying each change against the live homepage, a category page,
and a long article on mobile + desktop. Tokens go into SITE_CONFIG now (replacing the template
minimalist defaults), and ship the standard feature set (5-features.md). When the user approves the look, the site is design-complete; proceed to the go-live checklist (§9). Terminal stage after launch is `stage: "live"`.

## 9. Go-live checklist (before flipping the site live)

Run through this explicitly — these are the things that silently break or look wrong on launch:

- [ ] **`NEXT_PUBLIC_SITE_URL`** set in Vercel (production), e.g. `https://thesite.com` — **no
      trailing slash**, canonical host (match www vs non-www to how it actually serves). Then
      **redeploy** — env vars only take effect on a new build. Without this, sitemap, robots,
      RSS, canonical URLs, and JSON-LD all emit `example.com`.
- [ ] **Articles published, not draft** — confirm in the DB / by loading a category and an
      article on the live domain. Drafts won't appear on the site, in the sitemap, or in search.
- [ ] **Hero image set** (admin `site_settings` or `SITE.ui.heroImage`), and category
      `featured_image`s where used — else the hero falls back to the flat motif.
- [ ] **Verify the deploy** — latest Vercel build green; homepage, a category, a long article all
      load on the real domain, on **mobile and desktop**.
- [ ] **Sitemap/robots/RSS sanity** — open `/sitemap.xml` (real domain + article URLs present),
      `/robots.txt`, `/feed.xml`. (A browser-extension `<script>` injected into the XML view is a
      local artifact, not in the served file — check in incognito if unsure.)
- [ ] **Spot-check YMYL facts** on a couple of live articles — anything that was
      `verify_recommended` in facts.json (visa rule, best months, safety level). These are the
      facts that hurt most if wrong and lots of readers land on them.
- [ ] **Submit the sitemap to Google Search Console** — Domain property (DNS TXT verify), submit
      `https://thesite.com/sitemap.xml`. "Couldn't fetch" right after submission is normal; it
      clears within a day. Indexing is gradual (days–weeks).
- [ ] **Affiliates** — if monetizing, confirm the affiliate step ran with THIS site's IDs and the
      disclosure renders. (Often deferred to just after launch — that's fine; it's the next step.)

When live + sitemap submitted → `stage: "live"`. Record the URL and launch date in state.json.

## 9b. Lead magnet — built at the DESIGN step (pointer)

The lead-magnet PDF is produced during the DESIGN step, not here — because design runs
AFTER all batches are published (the "design moved to the end" order), so by design
time the corpus is complete and the brand tokens are set: everything the PDF needs.
Building it there means the PDF inherits the finished identity and ships enabled in the
repo handed over.

See `architecture/design-step.md` → "Build the lead magnet here" for the full step. In
brief: `node scripts/build-leadmagnet-all.mjs <export.json> <site>-config.json <out-dir>`
copies the explicitly-named sections (config `schema_version: 2` — see
`references/5-features.md`), writes `leadmagnet.json`, renders the PDF; then move the PDF
to `apps/site/public/`, set `SITE.leadMagnet.enabled:true` + `pdfUrl`. Re-run any time
content changes.
