# The compositor — the passes that finish a page

Paged.js breaks the flow into sheets. It does not *compose* them: it leaves stranded
tails, figures alone on a page, headings cut off from their text, tables split one row
short. Every one of those is fixed by a measured pass in `render-paged.py` (Rome:
`render4.py`), and every pass is **measured on the rendered DOM, never hand-listed**.

Read this at Stage F, before you start moving things by hand.

---

## The one rule the passes exist to serve

> **CSS never moves content BACKWARDS.** A figure or table that misses the page before
> it by a tenth of an inch simply stays where it fell. There is no CSS for "pull this
> back if it almost fits" — so the 85–90 % ratio rule cannot express itself without a
> pass that measures the gap and takes it from somewhere.

---

## The levers, and the order they run in

The order is not arbitrary. Each pass changes where everything after it falls, so a
later pass measuring a layout an earlier one will change is wasted work.

| # | pass | what it fixes | floor |
|---|---|---|---|
| 1 | **widow / heading** | a heading separated from its text | band → 1.2 in |
| 2 | **fit** | a table split away from the figure that introduces it | band, then art → 85 % |
| 3 | **feather / tight / loose** | a chapter spilling a few orphan lines | ~2 lines/page |
| 4 | **tail-feed** | a chapter's last sheet left two-thirds empty | — |
| 5 | **flat-feed** | a fed plate that stranded its own sheet | 85 % width |
| 6 | **snug** | a figure taking a sheet the page before could hold | 85 % |
| 7 | **fill** | a closing plate cut to the page it actually closes | 6.6 in cap |

### FURNITURE BEFORE ARGUMENT

When a pass needs space, it takes it in this order:

1. **the white** — a band's bottom margin, a lede's margin-bottom
2. **the head band** — furniture; a photograph giving up a quarter-inch is invisible
3. **the art** — never below 85 %, which is where a map's labels stop being readable

Half an inch off a photograph costs the reader nothing. Half an inch off a scale map
costs its labels. Rome's pull-back had this order from the start; every later pass
copies it.

**But a band has a floor too.** Cutting bands to 1.2 in left five Rome chapters opening
on a strip barely half the designed height — a head image too narrow to read as an
image, paid on every copy to save a page break nobody sees. `BAND_FLOOR = 2.0` now, and
where the art lever cannot reach, the figure falls to the next page. That is fine: every
chapter already carries a closing plate there.

---

## What Chromium and Paged.js actually do

Verified on Chromium 153. Do not re-derive these.

**`break-after: avoid` WORKS. `break-before: avoid` is silently dropped.** The first is
the correct general rule for headings — `h2, h3 { break-after: avoid }` — and it fixes
the ugly half of the problem on its own.

**`break-after: avoid` on a head band is a trap.** It welds the band to whatever follows,
and on a decision chapter that is a scale map and its ledger — so the opener could not
hold all three and Paged.js pushed band, map and table off together, leaving the kicker,
title and standfirst alone on an empty sheet.

**Nested `break-inside: avoid` pushes a block that fits.** Wrapping a plate and an
endmark in an avoiding wrapper while the figure already had one moved the whole wrapper
to the next sheet, though it measured 3.32 in against 3.69 in of free column. Keep the
wrapper for grouping; let the inner element's own avoid do the work.

**`break-inside: avoid` on a TABLE is all-or-nothing and its fit test is conservative.**
A 3.28 in table in 3.40 in of column was still refused outright. Switch that one table
to `break-inside: auto` and it fills the page it belongs on; with rows that fit, nothing
actually splits.

**Paged.js SPLITS an element across sheets, one fragment per page.**
- A paragraph becomes two `<p>`s. Anything comparing across the seam must group
  fragments by `data-ref`.
- **A section's `id` survives only on its FIRST fragment.** Any query like
  `el.closest('section.dec').id` returns `''` on a continuation page. Resolve through
  `data-ref` across every `.pagedjs_page_content`. This trap cost four separate passes
  before it was recognised — each one ran, found nothing, and reported success.

**An automatic hyphen IS a DOM character — but only after the split.** `hyphens: auto`
draws the hyphen at layout time, so no text walk inside one element sees it. When
Paged.js breaks a word across sheets it **appends U+2011 to the fragment it leaves
behind**. Test for `[­‐‑]$` — never a plain `-`, because breaking at an
authored hyphen is legitimate.

**Chromium has no `hyphenate-limit-last: page`** (nor `-lines`, nor `-chars`). A word
hyphenated across a page turn cannot be prevented in CSS; it has to be measured, and the
remedy is `hyphens: manual` on that one paragraph.

**Chromium has no `target-counter`.** Rome writes its folios back from a measured probe.
A row whose target it cannot resolve is *skipped*, so the row keeps whatever static text
it had — see fieldsheet-split.md for how that printed a page number for a chapter that
had left the book.

---

## Ratios: express them as WIDTH, not height

Reducing a replaced element's **width** scales its height by the same ratio, and needs
no measurement at all:

```css
figure.flat svg, figure.flat img { width: 85%; height: auto; margin: 0 auto; }
```

Three attempts to measure a plate's natural height and set `--flat` in inches all died
on the id-on-first-fragment trap above. The width form has no such failure mode.

**An arguing figure must be CAPPED, because its viewBox is not a page budget.** A map
drawn on a 600×560 board is 6.35 in tall at full column width — so the map, its head band
and its ledger could never share a sheet. `width:auto; height:auto` with **both** maxima
set is the one combination that constrains a replaced element while preserving its ratio;
`width:100%` plus `max-height` simply distorts.

```css
figure svg { display:block; margin:0 auto; width:auto; height:auto;
             max-width:100%; max-height:4.6in; }
.decision figure svg { max-height:3.5in; }
/* a decision that gives up its head band gives the space to the map */
.decision:not(:has(.photo.band)) figure svg { max-height:5.15in; }
```

`:has()` is safe — these books render in Chromium only.

---

## The closing plate is cut to the page it closes

Not to one standard height. A chapter ending high on its last sheet gets a taller plate;
one ending low gets a short one. Measure the free column and size the plate to it.

**Cap it at ~6.6 in.** A 3:2 landscape grown to a full 6.8 × 9.2 in portrait page throws
away more than half the frame. On a sheet the plate owns, split the leftover column
above and below instead — that reads as a composed full-page plate rather than a picture
that ran out.

**A plate's own margin fallback must match the base rule.** A new `.fill` rule whose
`margin-top` fallback was 30 px instead of `.photo`'s own 13 px added 17 px above
thirteen plates and pushed five onto fresh sheets — 46 pages became 51 for a reason
invisible in the book.

**A fed plate that lands alone on a sheet has defeated its own purpose.** Promoting a
plate to `closing` also INFLATES it (min-height, a deep margin, padding, a rule), and
that inflation is often the only reason it could not stay on the page before. Feed it
*flat* instead — still moved to the chapter's end, but at its natural height.
**Un-feeding it entirely is wrong**: the plate returns to the middle of the chapter and
the tail page is left holding nothing but the endmark.

---

## Furniture must be invisible to the movable-block passes

A head band, a mid-chapter band and a closing plate are placed on purpose. If a pass
collects one as a movable figure it will resize or relocate it.

**Every new furniture class has to be added to BOTH lists** — the block scan *and* the
shrink rewriter. Adding `figure.band` to only the first let the shrink step set
`art.style.width = 'auto'` **inline**, which beats any stylesheet rule, and a
full-column band rendered as a narrow portrait stamp at the photo's own ratio.

```js
if (el.classList.contains('head') || el.classList.contains('closer')
    || el.classList.contains('band')) return;
```

---

## Sizing a band into a gap is exact

2.4 in overshot a 2.76 in gap and the whole band moved to the next sheet; 2.2 in fitted.
Measure the gap, then pick the height — do not guess and re-render.

And shrinking is **not monotonic**: a shorter figure pulls more text up onto the page and
eats the gain. If two successive reductions do not land it, the lever is wrong, not the
value.
