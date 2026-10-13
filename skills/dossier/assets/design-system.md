# The dossier design system

**Every project inherits its own site's brand tokens.** Rome used La Tavola (its site's
palette) so the PDF and romeforamericans.com read as one brand. Lisbon will use Lisbon's.
The *structure* below is the constant; the four colours are the variable.

## Tokens

```css
--paper:#F6EEDB;  --ink:#2B241A;   --accent:#8A3324;  --gilt:#C9A84C;
--muted:#7A6B4E;  --soft:#9C8C6B;  --line:#DED0AF;    --line-soft:#E7DCC0;
--display:'IM Fell English';  --body:'Sorts Mill Goudy';  --mono:'IBM Plex Mono';
```

Four colours, three faces. **IM Fell English has NO bold weight** — never `font-weight:bold`
on it; the browser will synthesize a smeared fake. All three are open-licensed via Google
Fonts. Tints for maps derive from the four (zone, stone, water); don't introduce new hues.

**Check before shipping:** `grep -ric "anthropic\|claude\|--ds-" build/` → only filesystem
paths may match. A paid product must carry the client's brand, not the toolchain's.

## Page

The page is produced by the paged page model — real `@page` margins (92/82/72/82), the
sheet painted by the page div, furniture in margin boxes on every page. The verbatim CSS
and the renderer contract live in references/page-spec.md; the design authority over the
whole page is references/layout-architect.md. The legacy fixed `.page` div (0.85in
padding, overflow:hidden) is retired — everything except the cover flows.

## The baseline and the spacing scale (layout-architect.md §2 is authoritative)

**One vertical unit: 22.5px** (body 13.4px / 22.5px line — exactly one body leading in
the whole book; a second leading anywhere is a bug). Every vertical space is a step of
the scale — never an invented value:

```
6 · 11 · 17 · 22.5 (one line) · 34 · 45 · 68
```

Between blocks ≥ 22.5; within a block ≤ 17. Feathering (the renderer's per-chapter
TIGHT/LOOSE cards) moves a chapter ±1 notch from this baseline, never further and never
globally.

## The scale (measured, shipped)

| element | size | leading |
|---|---|---|
| cover title | 92–112px | 1.0 |
| h1 | 44px | 1.06 |
| standfirst | 18px italic | 1.45 |
| body | 13.4px | 1.68 |
| ledger cell | 12px | 1.5 |
| pull quote (side) | 17.5px | 1.46 |
| aside | 11.3px | 1.62 |
| note | 11px | 1.66 |
| mono label / eyebrow | 10px | 1.4 |
| **caption** | **12px** | **1.42** |
| ledger cell | 12px | 1.42 |

**A caption is not decoration, so it is not sized like decoration.** This table
used to specify **7.5px** — in a system whose own type ramp says "8 is the print
floor — never below", and in the same file that corrects external reviewers with
"8px is the floor for print". The doctrine contradicted itself twice on one page.

Worse, 8px was not a sufficient floor either. **8 CSS px is 6 printed points.**
Greece p13 set the two-line explanation of its route comparison at ~5.6pt; Rome
p7 and Turkey p26 caption at ~6pt. Those captions carry the information needed to
read the largest object on the page. The ramp was assigning the smallest type in
the book to the text that explains the biggest thing in it.

**The governing rule is FINAL PRINTED SIZE, including SVG transforms** — not the
`font-size` you declared. Turkey p36 declares 11–13px inside an SVG that is then
scaled down: it prints at ~5.8pt. Measure after transforms, at Letter size.

Caption text uses the **body** face, not mono: mono is for identifiers and short
keys. Apparatus tracking stays within 0–0.06em, and explanations are sentence
case — small + capitals + generous tracking is three difficulties at once.

## Page shape — half-empty pages are what "basic" means

Greece was called "stale, too basic." Two wrong diagnoses were tried first, and both are
worth knowing because they are the obvious ones:

1. **"It's too thin"** — wrong. Greece's prose pages carry *more* ink than Rome's (1.2% vs 0.9%).
2. **"Every page is a slab to the trim edge"** — wrong, and wrong because the *instrument*
   was wrong. Scanning the rendered PDF for its lowest ink finds the **folio**, and reports
   ~96% for every book ever made. Measure the DOM, exclude absolutely-positioned furniture.

**The real number:**

| | median fill | pages under 65% | range |
|---|---|---|---|
| Rome (reads well) | **71%** | 5 of 49 | 57–90% |
| Greece (reads stale) | **60%** | **25 of 41** | **18–92%** |

Greece's pages are **two-thirds empty and no two are the same height**. Rome holds 66–86%
on nearly every page — that consistency is what makes it read as a designed object. A book
where one page stops at 18% and the next at 92% has no page at all.

**This is the page-count complaint wearing a different hat.** 80 articles → 41 pages → each
page carrying 60% of what it could. The fix for all three is the same and it is at Stage A/B:
**more argument per page.** Another ledger row. The second-pass decision. The figure the
corpus already supports. Not bigger type, not fatter margins — those are padding in a suit.

Gate it: `python3 scripts/audit-page-shape.py dossier3.html`

## Rhythm

```css
.eyebrow{margin-bottom:19px}
h1.t{margin-bottom:19px}
.standfirst{margin-bottom:22px;padding-bottom:20px;border-bottom:1px solid var(--line-soft)}
.map,.photo{margin:4px 0 22px}        /* BOTH — never style one alone */
.map figcaption,.photo figcaption{margin-top:10px;padding-top:8px;
  border-top:1px solid var(--line-soft)}
.aside,.pull.side{margin:20px 0}
```

**Every inter-block gap must be at least one baseline (22.5px).** Under it, the page reads
as one mass — that's the "everything is stitched together" symptom.

## Provenance marks

```css
.mk{font-family:var(--mono);font-size:9px}
.mk.est{color:var(--accent)}   /* ● ESTABLISHED */
.mk.off{color:var(--gilt)}     /* ◇ OFFICIAL */
.mk.sur{color:var(--muted)}    /* ▲ SURVEYED */
.mk.vol{color:var(--soft)}     /* ◆ VOLATILE */
```
Split `ESTABLISHED` into `STRUCTURAL` (geography doesn't change) vs `STABLE` (the ordering
holds, the figure lives on the Sheet) where a page needs the distinction — they're different
confidence claims.

## Ledger

**Three variants, each with a fixed column contract.** The system specified tint,
rules and padding but never widths by information role — so content-driven table
layout decided them, and the same three semantic columns were distributed
differently on facing pages (Greece p42: "What to confirm" wrapped into a strip
while the source description took the width).

Use semantic `<table>` with `<colgroup>`, `table-layout:fixed; width:100%`,
`font-variant-numeric:tabular-nums` on number columns, cell type **≥12px/17px**,
padding 9px vertical / 12px horizontal.

| variant | columns | note |
|---|---|---|
| **options** | option/qualification 72% · value 28% | unit goes in the heading |
| **comparison** | criterion 40% · alternative 30% · alternative 30% | mark the row that changes the choice |
| **field sheet** | item 30% · action/value 46% · source 24% | same across all its sections; allow URL wrap |

**Show which row decides.** Turkey p23 gives "Passport control — unavoidable /
unavoidable" the same weight as the rows where responsibility actually changes.
Label the decisive row in TEXT — "Changes the choice" — plus a heavier top rule
and restrained tint. **Never encode significance in colour alone.**

**Mark the default only where the verdict supplies one.** Do not invent a score,
do not suppress a genuinely equal row, and do not manufacture a preference to
complete the visual template.


```css
.led-h{font-family:var(--mono);font-size:8px;letter-spacing:.18em;text-transform:uppercase;
  color:var(--soft);display:flex;justify-content:space-between;align-items:baseline;
  margin-top:6px;padding-bottom:8px;border-bottom:1px solid var(--line)}
.led-h .cols{color:var(--muted);letter-spacing:.12em}   /* ← the column header. Mandatory. */
.led td{padding:7px 0;border-bottom:1px solid var(--line-soft);line-height:1.5}
```

## Figures

```css
.map svg,.photo img{width:100%;display:block;border:1px solid var(--line-soft)}
.photo.wide img{height:2.25in;object-fit:cover}
.photo.band img{height:2.35in;object-fit:cover}
.fign{color:var(--accent);letter-spacing:.16em}   /* FIG. n */
```
Figure height comes from the **viewBox aspect**, not CSS. See `d-draw.md`.

## What external reviewers get wrong about this system

- **A4 (596×842pt)** — wrong; this is a US product, 8.5×11.
- **0.38in margins** — no binding allowance, gutter-tight.
- **6px mono labels** — decorative at that size. (The floor used to be stated as
  8px here. That was wrong twice: this same file specified 7.5px captions, and
  8 CSS px is only 6 printed points. Essential text is **12px/17px**, measured
  after SVG transforms. A reviewer who says the apparatus is too small is right.)
- **Drop cap on a verdict** — a drop cap opens a chapter, not a conclusion.
