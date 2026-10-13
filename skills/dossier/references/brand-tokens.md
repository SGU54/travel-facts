# Where the brand tokens come from

**There is no registry of them.** Checked, on the real fleet:
- `common.sites` (the fleet registry) holds `site_key`, `domain`, `admin_url`, click data —
  **no palette, no fonts, nothing about design.**
- There is no `state.json` in the site repos or in `fleet_ops`.
- The site's `globals.css` holds the **site's** tokens — which are NOT the book's (see below).

So for a project that has never shipped a dossier, **the tokens do not exist yet. You derive
them, in this session, and the user approves them.** That is a real step of the work, not a
lookup.

## The lookup order

```
1. assets/brands/<project>.json          ← EXISTS only if this project shipped a dossier before.
                                            Rome has one. A new project does not.
2. the site repo's apps/site/app/globals.css
                                         ← gives you the HUE FAMILY and the site's voice.
                                            Never copy the hex values verbatim.
3. derive → show the user → get approval → WRITE assets/brands/<project>.json
                                         ← so edition 2 and every other session inherits it.
```

## globals.css is the ONLY file you need

The user attaches `apps/site/app/globals.css` — not the repo. It carries the full named
palette **and the design intent, in its comments**, which is what you actually derive from:

```css
--bone:    #F4EEE2;   /* surface — travertine cream */
--ink:     #241C16;   /* text — espresso */
--green:   #6E2B2B;   /* primary — porphyry oxblood */
--saffron: #C9A227;   /* highlight — gilt */
```

The names ARE the brief. "Travertine", "porphyry", "espresso" tell you the destination's
material world; a hex alone doesn't.

## Rome's actual derivation — every book token traces to a site token

| role | site | book | why it moved |
|---|---|---|---|
| paper | `#F4EEE2` travertine cream | `#F6EEDB` | warmed — screens are cooler than paper |
| ink | `#241C16` espresso | `#2B241A` | lifted slightly — pure espresso goes muddy in ink |
| accent | `#6E2B2B` porphyry oxblood | `#8A3324` | saturated — oxblood dies at 40% coverage |
| gilt | `#C9A227` | `#C9A84C` | softened — screen gold is harsh on cream stock |
| line | `#D8CBB3` warm hairline | `#DED0AF` | near-identical; hairlines already work |

**Nothing was invented.** Four site tokens → four book tokens, each moved for a stated
print reason, everything else a tint. That's the whole method — do this, show the user the
before/after table, and get approval.

## Why you can't just copy the site (Rome proved it)

| | the site | the book |
|---|---|---|
| ink | `#241C16` | `#2B241A` — darkened for ink on paper |
| display | Cormorant Garamond | **IM Fell English** — 17th-c revival, chosen for the register |
| body | Source Sans 3 | **Sorts Mill Goudy** — reads at length, justified, at 13px |

The book is **the same brand translated for print**, not a screenshot of the website. A screen
palette goes muddy at 8.5×11, and a webfont picked for 16px on a phone is the wrong voice for
a paid manual.

## Deriving a print palette for a NEW project

Worked example — `greeceforamericans`, which has no brand file:

```
1. unzip the site repo → read apps/site/app/globals.css
   → pull the hue family. Say Greece's site is whitewash + Aegean blue.
2. build the four:
   paper   = the site's background, warmed for paper       (never pure white — it greys)
   ink     = the site's text colour, DARKENED ~1 step      (screens are backlit; paper isn't)
   accent  = the site's primary, saturated enough to survive 40% ink coverage
   gilt    = a metallic/secondary for rules and rings
3. derive the tints from those four ONLY: zone, stone, line, line-soft, water.
   No new hues. Rome has 12 tokens and 4 origins.
4. pick three faces, all open-licensed (Google Fonts):
   display — real historical weight, matched to the destination's register
   body    — survives 13px justified over 14k words
   mono    — data, labels, the provenance marks
5. SHOW the user: the four swatches, the three faces, and one rendered sample page.
6. on approval → write assets/brands/<project>.json
```

**Do not start Stage C or D before step 6.** Rebuilding the CSS after the prose is written is
how you get the "my fix didn't apply" class of bug (see the bug log).

## The check that must pass before shipping

```bash
grep -ric "anthropic\|claude\|--ds-\|copper\|kraft" build/    # → only filesystem paths may match
```
A paid product carries the client's brand, not the toolchain's.
## The check that must pass before shipping

```bash
grep -ric "anthropic\|claude\|--ds-\|copper\|kraft" build/    # → only filesystem paths may match
```
A paid product carries the client's brand, not the toolchain's.
