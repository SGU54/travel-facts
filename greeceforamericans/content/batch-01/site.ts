// packages/config/site.ts
// ─────────────────────────────────────────────────────────────────────────────
// SINGLE SOURCE OF TRUTH for greeceforamericans.com
//
// ░░ DESIGN LOGIC — "COME UP FOR AIR" ░░  (locked 2026; do not reskin casually)
// THESIS: Greece, for a nervous American first-timer, reads as a sequence of
//   sea-crossings — you don't drive it, you surface from it. The site is built as
//   a DESCENT and the relief of coming up for air. The promise is quiet competence:
//   "we've done the planning, all that's left is to breathe."
// PALETTE comes from the WATER COLUMN, not from postcard blue-and-white:
//   abyss/deep (chrome) → shallows/sea (primary) → aqua (signature) → light → salt
//   (reading surface). One warm coral is reserved, used sparingly.
// SIGNATURE: an immersive hero (ambient bubbles + caustic light + a waterline
//   break between the airy island index and the deep-water guides). Motion is the
//   one bold thing; everything else stays calm and legible. prefers-reduced-motion
//   MUST disable all of it. Article bodies are always the light SALT surface.
// TYPE: Cormorant (display, immersive/editorial) + Outfit (body, calm sans) +
//   Spline Sans Mono (utility voice — ferry legs, durations, prices, USD/EUR).
// CHROME is dark (green-deep), READING is light (bone/salt). This is intentional
//   and the template's bg-green-deep/text-bone (chrome) + bg-bone/text-ink (body)
//   contract already delivers it with no component changes.
// Full rationale + the rules that govern edits live in DESIGN-NOTES.md at repo root.
// SECRETS NEVER LIVE HERE (see .env.example).
// ─────────────────────────────────────────────────────────────────────────────

export const SITE = {
  domain: 'greeceforamericans.com',
  destination: 'Greece',
  language: 'en',
  audience: 'American first-time visitors',

  // ── Postgres schema (DB isolation) ──────────────────────────────────────────
  dbSchema: 'greece',                 // own schema, exposed in Data API + search path

  planningSlug: 'plan-your-trip',

  ui: {
    tagline: 'The first trip to Greece, planned by Americans who’ve done it.',
    heroEyebrow: 'For first-time American travelers',
    heroTitle: 'Come up for air.',
    heroLead: 'Athens, the islands, and the ferries between them — planned end to end, with prices in dollars and the jargon translated. You just have to show up and swim.',
    heroImage: '',                    // photoless animated hero by default (DB hero overrides)
    searchPlaceholder: 'Search Santorini, ferries, Athens…',
    searchPlaceholderShort: 'Search…',
    searchButton: 'Search',
    readMore: 'Read more',
    latestArticles: 'Latest guides',
    sections: 'Explore Greece',
    exploreCategory: 'Explore section',
    menu: 'Menu',
    home: 'Home',
    allRightsReserved: 'All rights reserved',
    footerBlurb: 'The first-timer’s guide to Greece for American travelers — Athens, the Cyclades, and Crete, planned end to end.',
    noArticlesYet: 'Guides are coming soon.',
    backToHome: 'Back to home',
    searchResults: 'Search results',
    searchEmpty: 'Nothing found. Try a different search.',
  },

  destinationsRibbon: ['Athens', 'Santorini', 'Naxos', 'Paros', 'Mykonos', 'Crete'],

  quickLinks: [
    { icon: 'passport', label: 'Visas & entry',  caption: 'ESTA-style ETIAS, passports, Schengen', slug: 'visas-and-entry' },
    { icon: 'plane',    label: 'Getting there',  caption: 'Flights from the US to Athens',          slug: 'flights-and-arrival' },
    { icon: 'coins',    label: 'Money & costs',  caption: 'Euros, cards, tipping, daily budget',    slug: 'money-and-costs' },
    { icon: 'calendar', label: 'When to go',     caption: 'Season by season, crowds & heat',        slug: 'when-to-go' },
  ],

  contact: {
    email: 'hello@greeceforamericans.com',
  },

  brand: {
    name: 'Greece for Americans',
    // ── "Come Up For Air" tokens — water-column palette (see DESIGN-NOTES.md) ──
    // KEYS are the semantic roles the theme/Tailwind plumbing expects; VALUES are
    // this site's chosen palette. Chrome is dark, reading surface is light.
    palette: {
      primary:     '#137A86',  // SEA — primary on light (buttons, links): AA on salt-white
      primaryDeep: '#04202F',  // DEEP — dark chrome (header, footer, hero base)
      accent:      '#62D8CC',  // AQUA — bright signature accent (mostly on dark chrome)
      accentDeep:  '#0E6E78',  // SHALLOWS — accent for text on light
      highlight:   '#9FE8E0',  // LIGHT — hero eyebrow, dots, on-dark highlights & selection
      surface:     '#F3F6F4',  // SALT — light reading surface (article body, cards, page bg)
      surfaceAlt:  '#E8F0EE',  // paler salt — alt cards / hovers
      ink:         '#0B2A38',  // INK — body text on light
      inkSoft:     '#50707A',  // muted ink
      line:        '#D3DEDA',  // hairlines on light
    },
    fonts: { display: 'Cormorant', body: 'Outfit' },

    // Display device: the immersive hero is the signature (defined in globals.css
    // via .motif-bg + the hero-descent styles). 'custom' = this site supplies its
    // own signature look rather than the generic inlay/rule.
    signature: 'custom' as '' | 'inlay' | 'rule' | 'custom',

    header: {
      ribbon: ['Athens', 'Santorini', 'Naxos', 'Paros', 'Mykonos', 'Crete'],
      showTagline: true,
      signatureBand: false,
    },

    quickLinksStyle: 'cards' as 'none' | 'cards' | 'list' | 'rail' | 'panel',
  },

  media: {
    // NOTE: 'cloud' is the R2 CLOUD NAME (account id), NOT the folder.
    // This account is co-hosted; the cloud name is 'dsrkwieur'. The per-site
    // FOLDER is 'greeceforamericans' (see folder below). Env overrides in prod.
    cloud: process.env.NEXT_PUBLIC_MEDIA_HOST ?? 'dsrkwieur',
    folder: 'greeceforamericans',
    presets: {
      articles: 'greeceforamericans_articles',
      media: 'greeceforamericans_media',
    },
  },

  // Affiliate programs available for THIS site (keys live in env, never here).
  // Greece-relevant: hotels, tours/tickets, flights, and ferries (the island layer).
  affiliates: {
    hotels: 'booking',
    tours: 'getyourguide',
    flights: 'skyscanner',
    ferries: 'ferryhopper',
    // Mandatory disclosure (US site → English). validate-batch.mjs checks for its
    // presence in any article carrying affiliate links. Placed near the first
    // affiliate link / info box.
    disclosure:
      'This article contains affiliate links. If you book through them we earn a small commission at no extra cost to you.',
  },
} as const;

export type SiteConfig = typeof SITE;

export function mediaUrl(
  publicId: string | null | undefined,
  transform = 'f_auto,q_auto'
): string | null {
  if (!publicId) return null;
  const id = publicId.includes('/') ? publicId : `${SITE.media.folder}/${publicId}`;
  return `https://img.sgfleetmedia.com/${SITE.media.cloud}/image/upload/${transform}/${id}`;
}
