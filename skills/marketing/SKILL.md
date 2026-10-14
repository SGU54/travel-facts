---
name: marketing
description: >
  The marketer + adaptive designer for a site's paid guide (the dossier PDF). Owns the
  THINKING the conversion layer renders: the persuasion craft (hook lines, sales-page
  copy, sentence-level pull), the design adaptation (every surface composed in THAT
  site's identity from its tokens), the site-wide placement doctrine (which pages get a
  surface, intent-gated) — and, since 2026-10, the MEASUREMENT that decides which of
  those earned their place (M5). Consumes the dossier build's A3 outputs and the site's
  tokens.css; produces finished copy + per-site surface styling that travel-empire Stage
  5c mounts, plus the weekly funnel line. Scope: selling the guide, on the site. NOT
  email, social, or traffic acquisition. Triggers: write/strengthen the hooks, guide ad
  copy, sales page copy, style the guide surfaces for [site], adapt the ads to the
  design, plan the guide placements, marketing pass on [site], did the surfaces earn
  their place, funnel for [site].
---

# Marketing — sell the guide, in the site's own voice, and know whether it worked

One site → one guide → one marketer. This skill decides what every surface SAYS and how
it LOOKS; travel-empire 5c renders it; **M5 measures it**. Never confuse the seam:
plumbing (slots, fail-closed config, /go/ routing, the admin toggle) is 5c's; the copy,
the look and the verdict are yours.

**Terminology lock (fleet-wide): "ad" = the site's own ad for its guide. There is NO
third-party advertising anywhere.** Every surface points at the guide.

```
INPUTS   dossier A3 outputs: name, thesis, raw hooks, decisions, failure modes
         the site's tokens.css + a look at the LIVE site (render-check screenshots, not the PDF)
         article-list.json swamps + tags AND articles.swamp in the DB (they must agree)
STAGE M1 HOOKS      mint/strengthen every hook line through the three-part test (hooks.md)
STAGE M2 ADAPT      compose each surface in this site's identity; pass the not-an-ad test (adaptation.md)
STAGE M3 SALES PAGE the /guide page's copy architecture (sales-page.md)
STAGE M4 PLACE      the site-wide surface map, intent-gated, one per page (surface-map.md)
STAGE M5 MEASURE    the funnel line, weekly, from the three instruments — and the cut list
OUTPUT   finished copy + per-surface CSS → 5c's config + design pass; a dated funnel line in state.json
```

## The non-negotiables

**1. Strong comes from specificity and the open loop — never volume.** No false urgency,
no countdowns, no fear theater.

**2. A surface that looks like an ad has failed.**

**3. Adapt to the LIVE site, not the dossier.** Screenshot the real article page first
(`render-check.mjs` captures it with fonts awaited — a shot before `document.fonts.ready`
lies, and on one site the fonts never load at all).

**4. Copy is swamp-aware — and the swamp must be in the DB.** The surfaces read
`articles.swamp`. A site with hooks for four doors and two tagged rows (Rome, 2026-10) has
written copy nobody will see. M4 ends with the gate: `swamp_tagged / published ≥ 0.25`.

**5. Honesty about what's proven: nothing, until M5 says otherwise.** Every line and
placement is hypothesis until the funnel line moves.

**6. The reader's article was already paid for.** The marketing layer sells the
CONNECTIONS and the sequence — never withholds, never teases.

## M5 — Measure (the stage that was missing)

"Data cuts, not opinions" named `common.link_clicks` as the judge. On 2026-10-14 that log
could not tell crawlers from readers (5,031 of 6,565 rows unclassifiable; the remainder
≥ 70 % crawlers). Until `proposals/03-link_clicks-bot-backfill.sql` and hard rule 18 land,
the judge is **the three instruments together**, read weekly:

| stage | instrument | number that matters |
|---|---|---|
| landings | Search Console (28 d clicks) + Vercel Web Analytics (visitors) | visitors/site/week |
| sales-page reach | Vercel Analytics `/guide` visitors | /guide visitors ÷ visitors |
| intent | `link_clicks` role=guide, `is_bot=false`, UA plausible, referer present — per `item` | clicks per surface ÷ page views of pages carrying that surface |
| checkout | Stripe `checkout.sessions` at the real price, excluding `metadata.purpose=e2e-test` | sessions ÷ sales-page clicks |
| purchase | Stripe paid sessions / `guide_entitlements` | sales |

`scripts/funnel.py --days 7` prints the first, third and fourth; the Vercel numbers are
the dashboard (API with `VERCEL_TOKEN` is AUTOMATION-MAP A-7). Write the line into
`state.json.funnel[]` dated. **Cut rule:** a surface with zero plausible clicks over 1,000
page views in 30 days is removed from that site's map — the map is code you ADAPT, so a
dead door is a one-line edit, logged.

**What the 2026-10-14 line says:** fleet-wide ≈ 408 human visitors/week, ≈ 6–15 of them
reach a `/guide`, 0 open checkout, 0 buy. The sales page and hooks are not the bottleneck;
nothing M1–M4 can do changes a funnel that empty at the top. M5's first job on each site is
therefore to say so plainly and hand the week to travel-empire's distribution work
(SELLING.md), not to rewrite copy.

## Quick reference

| you're doing | read |
|---|---|
| writing or strengthening hook lines | `references/hooks.md` |
| styling the surfaces for a site | `references/adaptation.md` |
| writing the /guide sales page | `references/sales-page.md` |
| deciding which pages get a surface | `references/surface-map.md` |
| measuring and cutting | this file, M5 |
| the render contract you feed | travel-empire `references/5c-conversion.md` |
| where the raw inputs come from | dossier SKILL.md, Stage A3 |

## Definition of done (one site)

Every hook passes the three-part test; every surface styled from this site's tokens and
passes the not-an-ad screenshot test; the sales page follows the architecture with real
numbers from the build; the placement map applied intent-gated AND `articles.swamp` tagged
to match (gate ≥ 25 %); the finished values handed to 5c and `fleet-gate GUIDE` green; a
dated funnel line written; nothing claims to be proven.
