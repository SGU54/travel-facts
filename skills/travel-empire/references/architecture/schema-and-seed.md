# Schema &amp; Seed — detail + the navigation function

The canonical SQL lives in `assets/schema.sql` and `assets/seed.sql`. This file explains
how the website turns that schema into a database-driven menu and non-empty category pages.

## Categories are DERIVED per destination (not a fixed template)

The seed is an OUTPUT of the build chat's categories step (Phase 2), not a fixed list. The
structure flexes to the destination's shape — a country organises by cities/regions, a city by
neighborhoods + day-trips, a route by stops (see the "Destination shape" rule in SKILL.md and
`references/article-plan.md`). `assets/seed.sql` ships a NEUTRAL placeholder encoding only the
universal backbone (the 6 functional mains); replace its names/slugs with the approved,
destination-shaped structure before running it. The 6-main backbone is a sensible default, but
the subcategories — and sometimes the mains — are decided per destination.

## Postgres schema isolation (co-hosting many sites in one Supabase project)

Supabase's free tier caps projects (2 at time of writing), so multiple sites are co-hosted
in ONE Supabase project, each in its OWN Postgres schema (e.g. `japan`, `morocco`), NOT
`public`. The schema name is the single source of truth in `SITE_CONFIG` (`SITE.dbSchema`),
and the shared Supabase client in `packages/db` is created with `db: { schema: SITE.dbSchema }`
so EVERY `.from(...)` query targets that schema automatically.

**THE RULE: every Supabase client in the codebase must be schema-pinned.** This is the most
common cross-site bug. Three real failures all had the same root cause — a client created with
a bare `createClient(url, key)` and no `db.schema`, which silently reads/writes the `public`
schema instead:
- `sitemap.ts` built its own raw client → shipped an EMPTY sitemap (zero articles found).
- `scripts/inject-links.mjs` built its own raw client → found zero articles / risked touching
  another site's data on `--apply`.
- Any one-off script or route that calls `createClient` directly.

So: import the shared `supabase` / `createServiceClient()` from `packages/db` (already pinned),
or, in a standalone script, pass `{ db: { schema: process.env.SUPABASE_DB_SCHEMA || '<schema>' } }`
explicitly. Never call `createClient` without the schema.

Supabase setup that MUST accompany this (or the API 500s / returns nothing):
- Settings → API → **Exposed schemas**: add the site's schema alongside `public`.
- Add the schema to the **Extra search path** too (this was the fix when an exposed schema
  still returned "Invalid schema").
- Each table is created INSIDE the schema (`create table <schema>.categories ...`), or the
  schema is set as the search path when running `assets/schema.sql`.

## The navigation function (ships in packages/db)

The site menu is built from the `categories` table — never a hardcoded `navigation.ts`.
Main categories are those with `parent_id` null; children are matched by `parent_id`;
order comes from `display_order`.

```ts
export interface NavItem {
  label: string;
  href: string;
  children: { label: string; href: string }[];
}

export async function getNavigation(): Promise<NavItem[]> {
  const { data, error } = await supabase
    .from('categories')
    .select('id, name, slug, parent_id, display_order, featured_image')
    .order('display_order', { ascending: true })
    .order('name', { ascending: true });
  if (error || !data) return [];

  const mains = data.filter((c) => c.parent_id === null);
  return mains.map((main) => ({
    label: main.name,
    href: `/category/${main.slug}`,
    children: data
      .filter((c) => c.parent_id === main.id)
      .map((child) => ({ label: child.name, href: `/category/${child.slug}` })),
  }));
}
```

`layout.tsx` (async server component) calls `getNavigation()` and passes the result to a
client `Header`. Adding/deleting a category in the admin changes the live menu — the admin
is the single source of truth.

## Category pages aggregate children (no empty main pages)

A main category page must show articles from the main AND all its child categories.
With foreign keys this is one query:

```ts
export async function getPostsByCategorySlug(slug: string) {
  const { data: cat } = await supabase
    .from('categories').select('id').eq('slug', slug).maybeSingle();
  if (!cat) return [];

  // ids = this category + its children
  const { data: kids } = await supabase
    .from('categories').select('id').eq('parent_id', cat.id);
  const ids = [cat.id, ...(kids ?? []).map((k) => k.id)];

  const { data } = await supabase
    .from('articles').select('*')
    .in('category_id', ids)
    .eq('status', 'published')
    .order('published_at', { ascending: false });
  return data ?? [];
}
```

This is the design fix for the bug where main category pages came up empty because we
matched on category *name* and articles were tagged with subcategory names.

## Homepage hero + Featured Guides — two distinct things

The homepage top is now TWO parts, not one slideshow:

1. **The hero** — a DESIGNED intro panel (eyebrow + display headline + lead). Flat
   brand-color "motif" background with the sun/identity motif by default. Optionally a
   DEDICATED darkened landing PHOTO behind it (see "Editable homepage hero" in
   5-features.md). It is NOT an article slideshow.
2. **The "Featured Guides" band** — a STATIC grid below the hero (FeaturedGrid.tsx:
   one big lead card + two stacked secondaries, ticket-stub style). This is what the
   `is_featured` + `featured_order` lineup now feeds. The admin page that manages it is
   labelled "Featured Guides" (NOT "Homepage hero" — that label was misleading).

WHY (lessons from site #2): a rotating slideshow buries everything past slide 1 and the
sun motif ghosts badly over photos. A static featured band shows the brand statement AND
the article imagery at once, nothing hidden. Keep HeroSlideshow.tsx in the repo (unused on
the homepage) so nothing breaks, but the homepage uses the intro panel + FeaturedGrid.

The curation logic is unchanged — `getFeaturedArticles()` still prefers the flagged lineup
in order and falls back to recent-with-image, so the Featured band is never empty but fully
controllable:

```ts
export async function getFeaturedArticles(limit = 3) {
  const { data: picked } = await supabase.from('articles').select('*')
    .eq('status', 'published').eq('is_featured', true)
    .not('featured_image', 'is', null)
    .order('featured_order', { ascending: true, nullsFirst: false })
    .order('published_at', { ascending: false }).limit(limit);
  if (picked && picked.length) return picked;          // curated lineup
  const { data } = await supabase.from('articles').select('*')   // fallback
    .eq('status', 'published').not('featured_image', 'is', null)
    .order('published_at', { ascending: false }).limit(limit);
  return data ?? [];
}
```

A ticket-edge "ruban" (`<div className="cosmati-inlay" />`) sits directly BELOW the hero;
PracticalStrip no longer carries one at its top (avoid a double ruban after the band).

## Category tiles — real photos, gradient fallback

The "Destinations" block renders each main category's `featured_image` (bare object key,
turned into a URL via `mediaUrl()`), with a dark overlay so the label stays legible. When
a category has no image yet it falls back to a palette gradient — so the grid is never broken
while images are being filled in. Images are assigned in the admin category manager (a
"Set image" button per main, using the shared MediaPicker).

## Admin: category management

The admin reads main categories from the DB (those with `parent_id` null), shows them as
section headers with a clear "MAIN" badge (not assignable), and lists subcategories under
each with a "move to" dropdown. Adding a category with no parent creates a main category
that appears in the site menu. Deleting a category never deletes its articles
(`on delete set null`). Each MAIN category also has a "Set image" control (shared MediaPicker)
that stores a bare object key in `featured_image` for its Destinations tile.
