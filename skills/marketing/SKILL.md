---
name: marketing
description: >
  The marketer + adaptive designer for a site's paid guide (the dossier PDF). Owns the
  THINKING the conversion layer renders: the persuasion craft (hook lines, sales-page
  copy, sentence-level pull) and the design adaptation (composing every surface in THAT
  site's visual identity from its tokens, so no surface ever reads as a bolted-on ad).
  Consumes the dossier build's A3 outputs (name, thesis, raw hooks, decisions, failure
  modes) and the site's tokens.css; produces the finished copy + per-site surface styling
  that travel-empire Stage 5c (references/5c-conversion.md) mounts. Also owns the
  site-wide placement doctrine (which pages get a surface, intent-gated). Scope: selling
  the guide, on the site. NOT email, social, or traffic acquisition (add later when
  designed). Triggers: write/strengthen the hooks, guide ad copy, sales page copy, style
  the guide surfaces for [site], adapt the ads to the design, plan the guide placements,
  marketing pass on [site].
---

# Marketing — sell the guide, in the site's own voice

One site → one guide → one marketer. This skill is the person whose whole job is
selling this PDF: what every surface SAYS (persuasion) and how it LOOKS on this
specific site (design adaptation). It decides values; travel-empire Stage 5c renders
them. Never confuse the seam: plumbing (slots, fail-closed config, /go/ routing, the
admin toggle) is 5c's; the copy and the look are yours.

**Terminology lock (fleet-wide): "ad" = the site's own ad for its guide. There is NO
third-party advertising anywhere.** Every surface points at the guide.

```
INPUTS   dossier A3 outputs: name, thesis, raw hooks, decisions, failure modes
         the site's tokens.css + a look at the LIVE site (not the dossier's palette)
         article-list.json swamps + tags (which articles carry which door)
STAGE M1 HOOKS      mint/strengthen every hook line through the three-part test
                    (references/hooks.md)
STAGE M2 ADAPT      compose each surface in this site's identity; echo an existing
                    CTA block; pass the "looks like an ad = failed" test
                    (references/adaptation.md)
STAGE M3 SALES PAGE the /guide page's copy architecture — the biggest single piece
                    of persuasion on the site (references/sales-page.md)
STAGE M4 PLACE      the site-wide surface map, intent-gated, one per page
                    (references/surface-map.md)
OUTPUT   finished copy (hooks, band/aside/inline lines, sales-page sections) +
         per-surface CSS in the site's tokens → handed to 5c's config + design pass
```

## The non-negotiables

**1. Strong comes from specificity and the open loop — never volume.** No false
urgency, no countdowns, no "LIMITED", no fear theater. The tension in every line must
be REAL (an expert would nod at the stake). This is the Pull-high/Trust-high corner of
the writing gate, applied to persuasion: a line that hypes fails Trust; a line that
merely describes fails Pull. Both failures ship nothing.

**2. A surface that looks like an ad has failed.** These are the site recommending its
own deeper work — a publisher pointing at its own book. Editorial voice, the site's own
CTA grammar, the cover artifact doing the visual selling. If a reader could mistake it
for a third-party unit, redo it.

**3. Adapt to the LIVE site, not the dossier.** The dossier's printed palette is the
BOOK's identity; the site's is in tokens.css and on screen. Proven the hard way: a
Greece band in the dossier's dark cream read as bolted-on; rebuilt in the live
mint-and-slate chrome — echoing the site's existing "Build my trip" CTA block — it read
as native. Always look at the rendered site before styling anything.

**4. Copy is swamp-aware.** Each surface leads with the door that matches its context
(the article's swamp tag; a category's theme; the trip tool's task). Same guide,
different door. Never one generic line everywhere.

**5. Honesty about what's proven: nothing.** Every line and placement is hypothesis
until common.link_clicks and checkout sales speak. Write to the craft, ship on one
site, let the data cut what doesn't earn its place. Never present a strong line as a
proven one.

**6. The reader's article was already paid for.** The article fully answered its
question before any surface appears (the swamp doctrine, travel-empire SKILL.md). The
marketing layer sells the CONNECTIONS and the sequence — never withholds, never teases
the answer the article owed.

## Quick reference

| you're doing | read |
|---|---|
| writing or strengthening hook lines | `references/hooks.md` |
| styling the surfaces for a site | `references/adaptation.md` |
| writing the /guide sales page | `references/sales-page.md` |
| deciding which pages get a surface | `references/surface-map.md` |
| the render contract you feed | travel-empire `references/5c-conversion.md` |
| where the raw inputs come from | dossier SKILL.md, Stage A3 |

## Definition of done (one site)

Every hook passes the three-part test and the honesty guardrail; every surface is
styled from this site's tokens and passes the not-an-ad test (screenshot judgment);
the sales page follows the copy architecture with real numbers from the build; the
placement map is applied intent-gated (dry pages stay dry); the finished values are
handed to 5c's `guide` config + design pass; nothing claims to be proven.
