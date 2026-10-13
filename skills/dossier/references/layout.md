# Stage F.5 — LAYOUT: how the book fills its pages

This stage exists because a book can pass every content gate and still look amateur:
empty pages, a heading stranded at the foot of a page, a figure marooned on a sheet of
its own, a photograph shrunk to a stamp to fit a box it never needed. Greece shipped all
four. They are not writing problems and not image problems — they are **layout** problems,
and the fix is one principle applied four ways.

## The principle: a page is not a unit of content. The ARGUMENT is.

The instinct is to give each thing its own `page()` call: the essay a page, its figure a
page, the photo a page. That produces a book where every page is 55-60% full, because a
piece of content almost never happens to be exactly one page tall. Rome's decisions each
needed 1.33-1.56 pages and were given 2 — half a page wasted, twelve times, **six blank
pages**. Greece's "Ground" essay filled 59% of its page and its route graph sat alone on
the next, above an unrelated photo.

**The fix is FLOW.** Emit a chapter as one `<div class="flow">` and let the print engine
paginate it: a section ends where it ends and the next begins underneath. See d-draw.md
for the `.flow` CSS (break-inside rules, orphans/widows, the verdict-never-splits guard).

Measured result on Greece: **41pp → 34pp, median page fill 60% → 84%**, same words.
The page count was never a corpus limit. It was this.

## The four defects, and the test for each

### 1. Empty pages / half-empty pages
**Test** (audit-page-shape.py): median content fill ≥ 66% (Rome, which reads well, is 71%),
and no more than ~25% of pages under 65%.
**Cause**: fixed `page()` calls for content that doesn't tile evenly.
**Fix**: flow the chapter. Do NOT fix it with bigger type or fatter margins — that is
padding in a suit, and audit-page-shape.py is calibrated to catch it (a fuller page of
9.9pt beats an emptier page of 12pt).

### 2. A heading stranded at the foot of a page
**Test**: no `h1`/`h2` in the bottom 12% of any page with no body line beneath it.
**Cause**: a break lands right after a heading.
**Fix**: `break-after:avoid` on `h1`, `.dnum`, `.standfirst`; `break-before:avoid` on the
first paragraph after a heading. A heading and its first two lines are one indivisible unit.

### 3. A figure or photo marooned on a page of its own
**Test**: no page whose only content is one figure or one plate (0 words of body, and — for
a photo — no arguing figure beside it). Greece p35 was `page(plate("A04"))`: a whole sheet
holding one photograph.
**Cause**: a visual placed with its own `page()` call instead of inside the prose that
introduces it.
**Fix**: a visual is emitted INSIDE the flow, right after the paragraph it illustrates.
Then it falls under that paragraph when it fits (Greece FIG.1: the essay filled 59%, the
graph is 384px, it drops onto the same page and the page reaches 85%) and pushes to the
next page only when it genuinely doesn't. The engine decides; you don't guess.

### 4. A photograph shrunk to a stamp
**Test** (see e-image.md): every plate renders at ≥ 60% of the column width.
**Cause**: a photo forced into a box whose aspect it doesn't match, or two visuals fighting
for one page so both shrink.
**Fix**: one visual per page-region, sized to the column (landscape → full width; the plate
follows the arguing figure, it doesn't share its row). A page carrying a figure AND a photo
is the smell — split them across the flow so each gets its width.

## The order to apply this (avoids the thrash I fell into)

Do NOT hand-tune `SPLIT = {...}` sets or nudge individual pages. That is a loop that never
converges — every fix moves the overflow somewhere else. Instead:

1. **Flow each chapter.** Decisions, operations, the ground essay — each becomes one
   `.flow` div with its visuals inside the prose.
2. **Set the fragmentation rules once** (d-draw.md): headings don't strand, tables/figures/
   verdicts don't split, orphans/widows ≥ 3.
3. **Render, then measure** with audit-page-shape.py. Let the print engine place the breaks.
4. **Only then** look at what's left. A genuinely over-full page (a 7-row ledger + a tall
   figure) is a content decision — cut a row or simplify the figure — not a page you shove.

The whole point of flow is that step 4 is nearly empty. If you find yourself maintaining a
list of which pages break where, you have reverted to fixed pages and lost the plot.

## Running furniture (superseded — the paged model)

Furniture is no longer a renderer template problem. The paged page model
(page-spec.md) puts the running head and folio in `@page` margin boxes that exist on
every page, chapter starts and continuations alike, with the paper painted by the page
div itself. The old caveat about header/footer templates and folio-on-cover is obsolete:
named pages (`@page cover{margin:0}`) unfurnish the cover cleanly, and openers suppress
their running head via a renderer handler. See references/layout-architect.md for the
full sheet contract.

## Chapter breaks and figure placement (learned from the Rome build)

**Every chapter starts on a fresh page.** A chapter is `<section class="dec chap">` in the
flow; give it `break-before:page` (except the first). Without this, chapters begin wherever
the previous one ended — a table starts at a page foot and its last row orphans onto the next
page, exactly the "hazardous" placement that makes a book feel unedited.

```css
.flow .chap{ break-before:page; }
.flow .chap:first-child{ break-before:avoid; }
```

**A chapter's figure is emitted INSIDE the prose, after the paragraph that introduces
it** (`fig_after`, default 2) — never after all the body. A figure emitted at the chapter's
end will be marooned on its own page whenever it doesn't fit the tail, stranding the text
before it. (This is doctrine #22 applied to chapters, not just decisions.)

**A figure renders exactly once — guard against double-emit.** The Rome build drew four
figures twice (FIG.3, 5, 9, 10) because a figure was referenced BOTH by a chapter's `fig`
key AND by a decision or a dedicated renderer (render_failure, a plate). Track emitted figure
keys and skip repeats:

```python
_EMITTED = {}
def fignum(key):            # lazy: first emit gets the next number, in appearance order
    if key not in _EMITTED:
        _EMITTED[key] = len(_EMITTED) + 1
    return _EMITTED[key]
def fig_block(key, ...):
    if key in _EMITTED and already_drawn:  # never draw the same figure twice
        return ""
```

Number figures by APPEARANCE ORDER, not a pre-assigned static map — a fixed map plus
placement-in-chapter-order produces out-of-sequence captions (Rome showed 1,3,2,3,4,5…).

**Chapter tails are finished by the FEATHERING pass, not by hand.** The renderer
(render-paged.py) measures every chapter's tail after pagination and plays one of three
cards per chapter — TIGHT (pull a small spill back), FEED (move the chapter's plate to
the end as a tall closing plate that fills the tail), LOOSE (open the leading a notch so
a thin tail receives enough lines) — bounded at ±1 notch from the baseline and decided
by measurement every build. Every chapter also carries an endmark (◆) so a legitimate
partial tail reads closed, not empty. The full system and its bounds:
references/layout-architect.md §4. If a tail survives feathering under a third of the
sheet, that is the signal to add the figure or ledger row the corpus already supports —
a Stage B/C decision, not a layout patch. NOTE: first fix any double-margin
(page-spec.md) — much apparent "empty tail" is really wasted margin.
