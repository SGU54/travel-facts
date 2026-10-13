# SITE_CONFIG — the single source of truth

Everything site-specific lives in ONE typed config file in `packages/config`. Change the
site by editing this file. No domain, colour, font, or affiliate ID is hardcoded anywhere
else. This is the rule that ends the "a stale URL/identity keeps reappearing" class of bugs.

```ts
// packages/config/site.ts  —  SKELETON. Fill every <placeholder> per project.
export const SITE = {
  domain:      '<site-domain>',            // e.g. japanforamericans.com
  destination: '<destination>',            // e.g. Japan
  language:    '<iso>',                    // ISO code; drives <html lang> (e.g. 'en', 'ru')
  audience:    '<audience>',               // e.g. American travelers

  // Postgres schema for this site's data (co-hosting many sites in one Supabase
  // project — see schema-and-seed.md). The shared db client pins every query to it.
  dbSchema:    '<schema>',                 // e.g. 'japan' — NOT 'public'

  // The one non-destination main category, excluded from the "Destinations" tiles.
  planningSlug: 'plan-your-trip',

  brand: {
    name:   '<Brand Name>',
    // Design tokens default to the MINIMALIST TEMPLATE look during Stages 1–4.
    // They are replaced per-site in the DESIGN stage (Stage 5), applied to the
    // real built site — NOT chosen up front. Until then, leave the template defaults.
    palette: { /* template minimalist defaults until Stage 5 design */ },
    fonts:   { display: '<template default>', body: '<template default>' },
  },

  // Contact email ships EMPTY — header/footer guard on it, so nothing renders.
  // Populate ONLY if the user explicitly asks for a public contact address (hard rule 11).
  contact: { email: '' },

  media: {
    // host ≠ folder (hard rule 10). `host` is the fleet-wide delivery domain;
    // `folder` is THIS site's path segment. NEVER set host = folder — it makes
    // every body image 404. Build URLs via mediaUrl() so the host lives in
    // exactly one place. No presets: an R2 folder is born from its first object,
    // so there is nothing to provision.
    host:   process.env.NEXT_PUBLIC_MEDIA_HOST ?? 'img.sgfleetmedia.com',
    folder: '<site-slug>',                 // all this site's images live here (NOT the host)
  },

  // Homepage quick-link strip → Plan-your-trip subcategories. Each slug MUST exist
  // in the seed (else the link is dead). Keep in sync with seed.sql.
  quickLinks: [
    { icon: 'passport', label: '<Visa & entry>',  slug: 'visas-and-documents' },
    { icon: 'plane',    label: '<Getting there>', slug: 'flights-and-arrival' },
    { icon: 'coins',    label: '<Money>',         slug: 'money-and-costs' },
    // … per project
  ],

  // Affiliate programs available for THIS site (content pipeline reads these; the
  // actual keys live in env, never here).
  affiliates: {
    hotels: 'booking',
    tours:  'getyourguide',
    flights: 'skyscanner',
    // … per project (rail, insurance, visa, etc.)
  },

  // NOTE: NO hardcoded image URLs and NO hardcoded article slugs here.
  // The hero, quick-links and menu are generated from the database at runtime.
} as const;
```

## Theme tokens

The brand colours/fonts flow into Tailwind config and globals.css from this one place,
so each site is themed by editing tokens in ONE spot. The tokens are PER-SITE and must be
chosen fresh for each project. There is NO default palette or font. Do not carry any prior
site's identity (or any single look) into a new site. Reusing one
identity across many sites is what makes them look mass-produced and leaves an obvious shared
footprint. The PLUMBING (how tokens flow into Tailwind/CSS) is reused; the VALUES (colours,
fonts, article styling) are decided per site in the design step below.

```ts
brand: {
  name:    '<Brand Name>',
  palette: { /* primary, accent, surface, ink … chosen for THIS site */ },
  fonts:   { display: '<DisplayFont>', body: '<BodyFont>' },  // chosen for THIS site
},
```

## Design step (decide the look BEFORE filling tokens)

Every site gets its own visible design, driven by its destination + audience. Before filling
the brand tokens:

1. Propose 3 DISTINCT design directions tailored to the destination and audience — different
   palettes, type pairings, and moods. Not three shades of one idea; three genuinely
   different takes.
2. The user picks one (or mixes). That choice fills the brand tokens.
3. North star: CLARITY FIRST. The design serves the reader — legible type, strong contrast,
   fast scanning, obvious navigation, mobile-first. A distinctive look never comes at the cost
   of readability. Pretty-but-hard-to-read fails the gate.

The engine (DB-driven nav, hero, admin, schema) is identical across sites; the design is the
deliberately-different layer on top. Build the plumbing once, choose the look every time.

## Rules

- **One config per site.** Never scatter site values across files.
- **Design is per-site.** Tokens here are this site's chosen identity, decided in the design
  step — never copied from a previous build.
- **Generated, not typed.** Homepage hero, quick-links and the nav menu are built from
  real database rows (featured articles, categories) — never from hand-typed slugs. If an
  article doesn't exist in the DB, it cannot be linked, so links can't break.
- **Domain naming** must feel native to the target language/audience. Good: `vmarokko.com`
  ("v Marokko" = "to Morocco" in Russian); `japanforamericans` (clear destination+audience).
  Bad: `moroccoguia.com` (mixes English + Spanish).
