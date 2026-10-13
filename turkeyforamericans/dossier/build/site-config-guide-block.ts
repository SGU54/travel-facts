// packages/config/site.ts — SITE.guide
// ─────────────────────────────────────────────────────────────────────────────
// Stage A3 deliverable. IDENTITY fields only — the operator fields (ads on/off,
// checkout URL, price) live in site_settings and are managed from the admin
// Guide panel, so flipping the guide live never needs a redeploy.
//
// FAIL-CLOSED: every Stage 5c surface renders nothing until identity is complete
// AND the admin toggle is on AND a checkout URL is set. Filling this block alone
// changes nothing on the live site.
//
// TWO FORMS OF THE NAME, deliberately:
//   name          "Turkey, Worked Out."   — cover, sales page, config, titles
//   in-prose       Turkey, Worked Out     — inside guide-spans, no terminal period
// The period is part of the fleet's title convention (Rome, Solved. / Thailand,
// Covered.) but a period mid-sentence reads as a false sentence break. The
// backfill payload writes the short form into the 30 spans; this config carries
// the full one.
// ─────────────────────────────────────────────────────────────────────────────

guide: {
  name: 'Turkey, Worked Out.',

  thesis:
    "Turkey's highest-stakes decisions all share a property nobody mentions: " +
    'the number you would look up does not exist. This book does the reasoning ' +
    "the lookup can't.",

  cover: '',        // Stage E — Cloudinary public_id once the cover renders
  pages: '',        // Stage F — set from the rendered PDF, never estimated
  decisions: 5,
  failureModes: 0,  // Stage C counts these; never guessed ahead
  figures: 0,       // Stage D counts these

  // Keyed by the swamp ids in travel-facts article-list.json. RAW — accurate
  // first, punchy second. The marketing skill (references/hooks.md: name the
  // wrong move → concrete-image stake → open loop) strengthens these before
  // they ship. A demoted swamp gets no hook and its surfaces fall back to the
  // thesis, which is the intended fail-open behaviour.
  hooks: {
    'S-insure':
      'A Turkish hospital will treat you before it bills you — and no published ' +
      'tariff anywhere tells you what the bill will be.',
    'S-transit':
      'Neither Istanbul airport publishes a minimum connection time. Every ' +
      'figure you have seen was invented by someone.',
    'S-licence':
      'Four parties decide whether you may drive in Turkey, they require four ' +
      'different things, and only three of them can be looked up.',
    'S-customs':
      'The hundred-year rule everyone repeats is not in Turkish law — and the ' +
      'statute it is not in carries five to twelve years.',
    'S-money2':
      'One Turkish bank publishes its foreign-card ATM charge. It is a ' +
      'percentage, and it runs to twenty-five.',
    // 'S-calendar' — deliberately absent. Gate A demoted it (zero cross-swamp
    // joins, no option structure). Its surfaces fall back to the thesis.
  },

  asideHooks: {},        // Stage 5c pass M2 — shorter, for the 230px article rail
  inlineHooks: {},       // Stage 5c pass M3 — the mid-article marker
  decisionTeasers: [],   // Stage B fills these from the shipped decisions
  previewImages: [],     // optional "see inside" spreads, fail-closed if empty
},
