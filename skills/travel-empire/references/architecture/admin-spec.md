# Admin panel — the full spec (ship this in the template)

The admin is a Next.js (App Router) CMS in `apps/admin`, proven across the site portfolio.
Ship the WHOLE feature set below in the template — it is not a "nice to have", it is the
editing surface the content pipeline depends on. Every item here exists because it was built
and used.

## Shell + auth
- **Every page wrapped in `AdminShell`** — persistent sidebar (Dashboard, Hero image, Featured Guides,
  Articles, + New, Media, Bulk import, Export, Batch update, Categories) + Log out. NO page is
  a nav dead-end. (The bulk-import page was once the only page outside the shell — a dead end.
  Never again: every route uses AdminShell.)
- **Auth gate** — `Login` page + `middleware.ts` + `lib/auth.ts` protect the whole admin.

## Dashboard (server component, live from DB)
- Stat cards: article counts (total / live / draft / archived), category count, site domain,
  live status.
- Recent-articles list (with status badges, links to edit).
- Quick actions + categories sidebar + external links to the live site and the Supabase project.

## Articles manager
- List with **search** (by title), **status filter** (all / published / draft / archived),
  **sort** (newest / A-Z).
- Per-row **Edit** + **Archive** (with confirm).

## Article editor
- Title, **auto-slug** (transliterate non-Latin scripts, e.g. Cyrillic to Latin), category
  (main/sub optgroups), status, excerpt, HTML content (raw HTML textarea — deliberate, suits
  the bulk pipeline; NOT a WYSIWYG).
- **Featured image**: upload / pick from library / paste URL-or-public_id, with preview;
  stored as a bare **object key** (no extension).
- **Body-image management**: a position-indexed visual thumbnail list under the content box.
  Each body image (an `<img>` in the content HTML, stored as a full delivery URL) has
  **Replace** (via the shared MediaPicker) and **Remove**. Managed by POSITION/index — done
  with a DOM parser (DOMParser), NEVER regex — so duplicate srcs are handled correctly.
- **Insert image into body** (upload or from library).
- **Danger zone**: Archive (recoverable) vs **hard-delete behind a typed "DELETE" confirmation**;
  Restore for archived.

## Media library
- Grid of all uploads (paginated — see app-router-rules); upload; copy key / URL.
- **Usage badge on every tile** — `used x N` (how many articles reference it) or `unused`,
  computed in ONE batched DB pass when the page loads (`/api/media-usage?map=1&ids=...`).
- **"Unused only" filter** with a live count.
- **Single delete — usage-checked**: before destroy, check which articles reference the image
  (as `featured_image` == public_id OR the public_id appears in `content`). If used, BLOCK and
  list the articles to fix first; if unused, confirm then destroy.
- **Bulk delete** of all unused (each re-checked server-side before destroy).
- **Server-side guard**: the upload API's DELETE re-checks usage and returns 409 `in_use` if
  referenced (UI checks too, but the server is authoritative — a scripted call can't orphan an
  image mid-article). Honest scope: the check covers references INSIDE articles, so wording is
  "not used in any article", not "safe everywhere".

## Categories manager
- Add (auto-slug), main/sub (parent) structure, move between parents, delete (articles become
  uncategorised, NOT deleted). Top-level categories form the site menu (via `getNavigation()`).
- **Tile image per MAIN category**: a "Set image" / "Change image" control (shared MediaPicker)
  stores a bare object key in `categories.featured_image`, rendered on the site's
  "Destinations" tiles (gradient fallback when unset). The categories PUT must allow
  `featured_image` (it was once dropped from the allow-list → silent no-save; don't regress).

## Featured Guides manager (dedicated page)
- A single page to CURATE the homepage "Featured Guides" band — hand-picked, not
  "newest N with an image" (which drifts on its own as you publish). This is the page
  formerly labelled "Homepage hero"; renamed because it manages the featured-article
  CARDS, not the hero image.
- Shows the current lineup as **draggable cards** (thumbnail + title + position); a list of
  **candidates** (published articles with a featured image, not yet featured) to add; remove
  to drop. Drag to set order; Save writes the lineup.
- Backed by `is_featured` + `featured_order` on `articles`. The site's `getFeaturedArticles()`
  shows featured-in-order, falling back to recent-with-image when none are flagged (never empty).
- Save rewrites the whole lineup atomically (clear all featured, then set the chosen set with
  `featured_order = index`), so the page reflects exactly what the site shows.

## Hero image manager (dedicated page)
- A page to set the homepage HERO BACKGROUND IMAGE (a dedicated landing photo, picked from
  the media library via the shared MediaPicker) — separate from the Featured Guides band.
- Backed by the single-row `site_settings` table (see 5-features.md "Editable homepage hero"),
  read/written via the `hero-settings` API. Preview + Save + Remove (remove → flat motif hero).
- The public site resolves DB image → `SITE.ui.heroImage` config fallback → flat motif.

## APIs (the contract the content pipeline + scripts use)
- **articles** — GET (search/sort/status), POST, PUT (set `published_at` on FIRST publish only;
  allow-list includes `is_featured`, `featured_order`), DELETE (archive by default; hard with `?hard=1`).
- **categories** — CRUD; main/sub; PUT allow-list includes `featured_image`.
- **homepage** — GET (current Featured Guides lineup + addable candidates), POST `{slugs:[]}`
  (set the ordered lineup; clears then applies). (Route still named `homepage`; the UI label
  is "Featured Guides".)
- **hero-settings** — GET (current site_settings row), POST `{hero_image, hero_eyebrow?,
  hero_title?, hero_lead?}` (upserts the single row). Uses `createServiceClient` (schema-pinned).
- **import** — bulk; ALWAYS draft; idempotent (skips existing slugs); resolves
  `category_slug`->`category_id` (FK); JSON only; maxDuration 60.
- **articles/bulk-publish** — POST; body `{ids:[...]}` (explicit) OR `{all:true, search?,
  category_id?}` (filter-driven). ONLY flips `draft`->`published` (never un-archives, never
  re-publishes an already-published article); idempotent; stamps `published_at` on first
  go-live only; touches only `status`. No schema change, no new deps. Built for empire-scale
  publishing (80 articles one-by-one is untenable).
- **export** — GET; emits the article set as JSON in the EXACT import shape (round-trip safe);
  filters by `category_slug`, `status`, `slugs`; `?download=1` for a file. (Inverse of import.)
- **batch-update** — POST; same shape as import but UPDATES by slug (upsert, no dup), STATUS
  PRESERVED by default (`preserve_status`), optional `allow_create`. For offline bulk edits.
- **upload** — POST (PutObject to R2), GET (ListObjectsV2, paginated), DELETE (scoped to this site's folder, 403 otherwise)
  (destroy + server-side usage guard).
- **media-usage** — GET `?public_id=` (detail) and `?map=1&ids=` (batch count map in one pass).
- **auth/login**.

## Admin rules (each is a bug we paid for)
- Every page in AdminShell — no dead ends.
- Bulk-publish UI in ArticlesManager: checkbox on DRAFT rows only (published/archived rows get
  none), a select-all-drafts header control, and a Publish-selected / Publish-all-drafts action
  bar with a result toast. Additive — never disturbs the existing single-row actions.
- Body images managed by position-indexed visual list, replace/remove via shared MediaPicker,
  DOM-parser not regex.
- Media delete is usage-checked (article scan of featured + body), with a server-side guard,
  single + bulk, plus usage badges + unused filter.
- Hard delete only behind a typed "DELETE" confirmation; archive is the default, reversible.
- Raw-HTML editor is deliberate (bulk pipeline feeds HTML) — do NOT add a WYSIWYG.
- The Featured Guides band is curated via the Featured Guides page (`is_featured`/`featured_order`), never
  auto-"newest N"; category tiles use `categories.featured_image`. Both PUT allow-lists must
  include these fields, or saves silently no-op (a bug already paid for).
- Every DB client (routes AND standalone scripts) is schema-pinned to `SITE.dbSchema` — a bare
  `createClient` reads `public` and silently returns nothing / writes the wrong schema.
