# THE LAYOUT ARCHITECT — the design authority for the book

**Read this before Stage C and again before Stage F.** It is the layer that thinks about
the page the way a book designer does, BEFORE anything renders. The other references carry
rules; this one carries the point of view the rules serve, and it is authoritative over
them: where page-spec.md, layout.md, or design-system.md conflict with this file, this
file wins. It exists because a build once passed every structural gate and still read as
"generated" — inconsistent margins, furniture that appeared on some pages and not others,
pages that were legal and still looked undesigned.

## The point of view

This book is a paid object. The reader's trust in the *argument* is transferred from the
*object*: a page that holds its shape says "someone decided this," and a page that doesn't
says "a machine emitted this," regardless of how good the prose is. So the design has one
governing idea:

> **Every sheet is the same instrument playing different bars.** One grid, one baseline,
> one furniture system, one spacing scale — and inside that constancy, deliberate variety:
> a full-bleed cover, image-dominant closing pages, dense ledger spreads, airy tails.
> Variety on top of constancy reads designed. Variety instead of constancy reads broken.

The test for any page is never "which rule does this violate?" It is:

> **Across body pages, the outer text edges and the furniture positions coincide.
> Within each reading mode, equivalent roles share a measure, a hierarchy and a
> spacing logic. Any departure is named and has a purpose.**

If yes, the book has a page. If no, it has 47 separate documents.

**This test used to also demand that the BASELINE coincide** — "margins, runhead,
folio, and baseline." That part was dropped, for two reasons. It was never true
of this system: the same file prescribes a 22.5px line, an 11px paragraph
after-space and other non-multiples, then permits tight/loose feathering — so the
phase cannot survive an arbitrary sequence of paragraphs, tables and figures. And
it measured the wrong thing. Greece p35 keeps sheet and furniture perfectly while
a tiny timeline floats in a large empty rectangle; Rome p44 aligns its "wallet
card" impeccably to a column that makes it physically unusable. **Constancy
certifies the container, not the fitness of what is in it.**

So: **four reading modes**, one sheet.

| mode | the reader's task | what varies |
|---|---|---|
| essay | follow an argument | narrow prose measure, generous leading |
| decision | find the call, check the exception | opener pack, ledger, verdict block |
| reference table | locate an item, do the check, reach the source | fixed column contracts, full width |
| carry object | use it away from the book | its own named panel geometry |

Their outer sheet never changes. Their inner arrangement answers different
questions. **Variety on top of constancy still reads designed** — the principle
survives; it was the baseline absolute that had to go. Do not try to simulate a
document-wide baseline grid with unsupported line-grid CSS, per-line positioning
or spacer insertion; keep leading regular *locally* instead.

## 0 · The chapter is the budget — plan it before you draft it

**Every chapter breaks to a fresh page** (the opener convention, §1). That one fact means
a chapter's total height — prose + every figure + every photo it carries — is not a
number the render discovers afterward, it is a number the author is choosing while
writing. Treat it that way: before Stage C commits a chapter's final prose, hold a
one-line brief for it —

- **length**: a rough word count, converted to pages at this book's own measured rate
  (depth gate's words/page, from the last cold build — not a guess)
- **figures**: how many, which kind (map / photo), and which SIZE CLASS each one is
  (compact mid-chapter band vs a 4.35in closing plate) — decided here, not discovered
  as a feathering emergency at Stage F
- **closing image, explicitly yes or no**: if the chapter's estimated tail lands under
  ~70% of the sheet (bug #31) and the chapter holds a candidate plate, assign it as the
  closing image NOW. If the tail is a short, closed verdict apparatus with nothing left
  to show, leave it short on purpose — a legitimate chapter end (§4) is not a defect and
  does not need a plate manufactured to hide it.

**A plate has a STANDARD size and a FLEXIBLE size — pick by measuring, not by reflex.**
The class default (5.4in for a `.closer`, 2.2in for a `.photo` head band) is sized for
the common case: a chapter whose own prose already uses most of its sheet, where the
standard plate is what closes the remaining fifth or so. It is not a law of nature, and
applying it blind produces both failures seen this session, in opposite directions:

- **too small a remainder for it**: Japan's ryokan chapter (c06) had only 5.17in left
  on its tail page before the plate — the standard 5.4in (plus its own margin) didn't
  fit and silently spilled the chapter onto a THIRD page, trading one stub for another,
  worse one. Caught only by diffing the rendered page count against what shipped before.
- **too much remainder for it**: a chapter whose tail is nearly empty BEFORE any plate
  (prose used, say, only a third of the sheet) gets a standard-size plate sitting above
  a lingering blank strip — the stub moves below the image instead of disappearing.

The rule: measure the tail's free height before the plate. **Target ≥75% fill of the
sheet with the plate included.** If the standard size cannot reach that (overflows the
remaining space, case 1) or leaves it well short (case 2), size THIS plate to the actual
free height instead of the class constant — bounded on both sides (roughly 4.5–6.5in for
a `.closer`) so a plate never shrinks to a sliver or balloons past a sensible read. Scope
the override to that one figure (`figure.closer.XXclose img{ height:_in; }` — note the
doubled class for specificity, `figure.closer img` alone outranks a bare `.XXclose img`
and the override silently does nothing), not the shared class. c06's fix (4.85in, shrunk
to fit) is the worked example; the same measurement, run the other way, is the fix the
next too-empty tail needs.

This is deliberately NOT a renderer heuristic (no change to the SNUG pass in
render-paged.py): the lesson of this session's own debugging — the table-fragmentation
bug, the feather pass making a stub worse by "loosening" a section it could not actually
help — is that automated layout correction is a safety net for small error, not a
substitute for someone measuring the actual page and choosing. Do this at the chapter
brief stage, by hand, the same way the brief itself is decided by hand.

This is not a second layout pass competing with feathering (§4). Feathering is the
renderer's safety net for being off by a notch; it measures every chapter and corrects
±1 notch, automatically, every build — it was never meant to rescue a chapter whose
figure budget was never decided, and asking it to do that is how Japan's "Decide these
first" annex shipped a table split across a page turn with the preceding page a third
empty: nobody had asked, while writing that chapter, "does this table's shape survive
its own page." Plan the budget so feathering only ever nudges; do not plan on feathering
to invent one.

**Judge an image candidate in the band it will print as, not as a full frame.** A photo
that reads perfectly at full frame can be the wrong pick once cropped to a 2.0in head
band or a 3.4:1 strip — the crop changes what's actually in it, and "does this answer
what the text doesn't already say" is a question you can only answer honestly against
the real crop. Build the contact sheet pre-cropped to the slot's aspect (several
vertical offsets of the same frame are different candidates, not one), not as thumbnails
of the untouched photo (see e-image.md). Caught on Morocco's Fez chapter: full-frame,
Bab Bou Jeloux (the city gate, already named in the chapter's own table) read as the
obvious pick; band-cropped side by side next to a medersa courtyard, the gate turned out
to repeat the table and the medersa was the one frame in the whole library that answered
the half of the chapter's own title ("the scholar's city") nothing else did.

**Any instrument that must not split — a ledger, a decision table, a checklist — is a
markup decision made HERE, before a line of it is written, not a CSS property applied
to whatever tag Stage C happened to use.** `break-inside:avoid` on a `<table>` inside
this book's paginated, multicol-based render is a real, separate Chromium limitation —
table fragmentation under break-inside:avoid in a multicol context is unreliable
regardless of how much free space the page actually has, and no amount of shrinking or
CSS tightening reaches it, because the table can be shoved to the next page even when it
visibly fits. A `<div>` grid with `display:grid` and `break-inside:avoid` on each row
does not carry this limitation. If a chapter's instrument is rows that must stay
together, mark it up as a grid from the first draft, not a table discovered to be
unbreakable only after it ships broken.

## 1 · The sheet contract (the page model)

The book is paginated by a real pagination engine (Paged.js) into actual page divs before
printing — see page-spec.md for the mechanism and the graveyard of approaches that don't
work in this Chromium. What matters here is the *contract* every sheet signs:

- **The paper reaches all four trim edges.** No white band of any width, ever. The page
  div itself is the paper, so this holds by construction — but it is gated anyway
  (`audit-furniture.py`), because three previous mechanisms held it "by construction" too
  and shipped white bands.
- **The column is constant**: body lives in 92–984px vertically, 82px side margins, on
  every page — chapter starts and continuations alike. Margins are a property of the
  PAGE, never of the chapter.
- **The instrument width is not the reading width.** The 652px column is what
  *tables and figures* may use. Running prose gets an inner measure:

  ```css
  .prose      { max-width: 520px; }      /* left-aligned in the column */
  .prose p    { font-size: 15px; line-height: 22.5px; }
  ```

  At 13.4px across the full column, ordinary prose lines ran **104–117
  characters** in all three shipped books — a table's measure applied to an
  essay. Leading separates lines; it does not shorten the journey back to the
  start of the next one. Target **65–85 characters** on a full line, check it in
  each brand's actual face, and if a face misses the target **narrow the measure
  before shrinking the type**. Do not fill the freed 132px with decoration, and
  do not recover the resulting page count by making the text smaller again.
  Apply `.prose` to paragraph runs, not to a wrapper that also holds the ledger.
- **Furniture is per-page**: running head in the head band, folio in the foot band, on
  every interior page. The running head carries the book title left and the current
  chapter right (set by the chapter, repeated by the page).
- **Named exceptions are named**: the cover (`page: cover`, full bleed, no furniture) and
  the annex (`page: annex`, same bands, its own bottom clearance). An exception the CSS
  can't name is a bug, not a design.

### The opener convention

A chapter-opening page **suppresses its running head** (the folio stays). The opener
announces itself — eyebrow, H1, standfirst; a runhead repeating the same words 40px above
them is the tell of a template, not a book. The renderer enforces this mechanically: any
page whose content carries an H1 is an opener (chapters always break to a fresh page, so
an H1 can only sit at a page top).

## 2 · The grid: one baseline, one scale, one ramp

### Baseline

Body type is **13.4px on a 22.5px line** — and 22.5px is *the* vertical unit of the book.
There is exactly one body leading. (The pre-architect build ran the flow at 1.72 and the
spec at 1.68 — two books interleaved. Reconciling them recovered roughly a line per page.)

### Spacing scale

Every vertical space in the book is one of these steps, chosen from the baseline:

```
  6   ·  hairline gap (caption padding, rule offsets)
 11   ·  half-line    (paragraph after-space, list items)
 17   ·  ¾-line       (figure/table entry, standfirst padding)
 22.5 ·  ONE LINE     (inter-block minimum — below this, blocks weld)
 34   ·  1½ lines     (H2 approach, section-internal breathing)
 45   ·  2 lines      (major transitions inside a page)
 68   ·  3 lines      (only the chapter-open stack uses this much)
```

The rule that matters: **any gap between two blocks ≥ one line (22.5px), and any gap
within a block ≤ ¾-line.** That single asymmetry is what makes a page parse at arm's
length. An ad-hoc value ("26px felt right") is how the previous files accumulated
nineteen different margins; when a space needs tuning, move it to the adjacent step, don't
invent a twentieth value.

### Type ramp

One ramp, ratio ≈ 1.27 between working steps, three faces with fixed jobs:

```
  10   mono      eyebrow, short key, ledger header  (see the floor note below)
  12   body      caption, necessary annotation       (body face — mono is for keys)
  10   mono      furniture (runhead), marks
  12   mono      folio
  11   mono      H2 — a LABEL, visibly subordinate to H1, never the display face
  12   body      ledger cells, asides
  13.4 body      BODY — the reference note; everything is sized relative to it
  17   display-i standfirst
  19   display   H3
  39/44 display  H1 (chapter question) — one per section
  ~104 display   cover title only
```

The display face carries *statements* (titles, verdict lead-ins), the body face carries
*argument*, the mono face carries *apparatus* (labels, keys, furniture, marks). A
piece of text set in the wrong face is a hierarchy error even at the right size.

**The floor is a PRINTED size, not a declared one.** 8 CSS px = 6 printed points,
which is too small for anything a reader must actually read; it was also
contradicted by `design-system.md`'s own 7.5px caption row. Essential text —
captions, keys, annotations that explain a figure — sits at **12px/17px minimum**,
table headers and secondary annotations at **11px/15px**. Nothing that carries
information goes below that, and the check is the size **after every SVG
transform**, measured on a Letter-sized page. Calling a caption subordinate does
not make its content optional.

## 3 · Composition: where things sit and why

### The decision opener answers before it narrates

An essay opener serves a FIRST reading. A decision is visited a second time, by a
reader with a different task: *find the decision, recover the default, check
whether the exception applies.* Today that task inherits the essay's pagination —
Greece asks its question on p11 and prints the call on **p13**; Rome asks on p11
and calls on p12; Turkey asks on p22 and calls on p23.

So a decision chapter gets its own opener, distinct from the essay opener:

```
eyebrow  →  the question  →  [default + its decisive exception]  →  the reasoning
```

The block holds the EXISTING call in one or two sentences plus its decisive
exception. It is not a new promotional summary, and it is **generated from the
same editorial data as the later verdict** — never maintained as a second answer
that can drift from the first.

```css
.decision-open { break-inside: avoid; border-left: 3px solid var(--accent);
                 padding: 17px; font-size: 15px; line-height: 22.5px; }
```

Keep the whole opener pack under **300px**. If it does not fit, **edit it** — do
not clip it. The drop cap may open the reasoning paragraph that follows; never
the verdict. Genuinely discursive chapters keep the existing essay opener.



**A chapter opens as a fixed stack**: eyebrow → H1 → standfirst → rule → drop-capped first
paragraph. Openers are the book's most repeated composition; their sameness is the
constancy the rest of the variety stands on. Never improvise an opener.

**A figure sits under the prose that introduces it** — inside the flow, after its
paragraph (chapters default to after paragraph 2; override with `fig_after` when the
introducing paragraph is elsewhere). A figure emitted after ALL the prose is a figure the
engine will maroon on its own page whenever it doesn't fit the tail — which is how a
near-full-page figure strands ten lines of text on a page that's 75% air.

**The arguing figure outranks the photograph.** On any page holding both, the figure that
carries the argument comes first in reading order; the plate paces, it never leads.

**A plate can close a chapter.** A tall (4.35in) full-column photograph, caption, endmark,
air below: that is a designed closing-image page, and it is where a chapter's plate goes
when the tail would otherwise strand a fragment (see feathering, below). A plate alone at
2.55in at the TOP of an otherwise empty page is not this — it is a marooned photo.

**Whitespace is spent, not left over.** The air under a closing plate, the third of a page
below a decision's verdict apparatus, the empty lower half of the annex — each is either
*closed* (by the endmark, the ◆ that tells the reader "this section chose to stop here")
or it is a defect. The endmark is what converts a partial page from absence into air:
every chapter and decision carries one.

**When is a page doing too much?** Two visuals fighting for one page (both shrink); a
ledger, a verdict, AND a figure stacked with under-one-line gaps; an H2 within 3 lines of
the page foot. The fix is a content decision — cut a row, move the plate — never "make it
fit" by shrinking type or gaps below the scale.

**When is a page doing too little?** Body ink ending in the top third with no closural
device; a figure alone with no words; a tail of fewer than ~6 lines. These are what the
feathering pass exists to remove — and any that survive it are the signal to add the
figure or ledger row the corpus already supports (that is a Stage B/C decision, not a
layout patch).

## 4 · Feathering — the compositor's three cards

Real books are finished by a compositor who pulls widows back and feeds thin pages. The
render does the same, **by measurement, every build, never by a hand-kept list** (a
hand-kept list of page fixes is the split-set antipattern — it never converges). After
pagination the renderer measures every chapter's tail fragment and plays, per chapter:

1. **TIGHT** — the tail is smaller than what tightening can recover (≈48px per preceding
   page, +90px per tall plate the chapter holds): set the chapter one notch tighter
   (22px leading, 10px paragraph space, plates to 2.3in) and the tail pulls back onto the
   page entirely. If tightening fails to clear the tail, it is reverted and escalated —
   a 2-line orphan is worse than the 6-line one you started with.
2. **FEED** — the tail is too big to pull back and the chapter holds a plate: the plate
   moves to the chapter's end as a 4.35in **closing plate**. The tail becomes an
   image-dominant closing page instead of a stranded fragment.
3. **LOOSE** — no plate to feed and the tail is under ~42% of the column: the chapter is
   set one notch more open (24px leading) so the tail page receives enough lines to read
   set rather than abandoned.

The bounds are the point: tight and loose are ±1 notch from the baseline, defined here,
applied per chapter — never global, never further. A book whose whole colour changed to
fix one tail has been padded, and audit-page-shape is calibrated to catch exactly that.

Tails the cards can't fix (a complete verdict apparatus landing at ~35–40% of the sheet)
are legitimate chapter tails — closed by the endmark, they read as the book breathing.
The stub gate draws the line at a third of the sheet: below that is a fragment, not a
tail.

## 5 · Before render / after render

**Before writing layout code**, walk this list — it is the difference between designing
and debugging:

- [ ] every vertical value you're about to write is on the spacing scale
- [ ] every font-size is on the ramp, in the face the ramp assigns
- [ ] every figure/plate is emitted INSIDE the prose, after its introducing paragraph
- [ ] every section carries an `id`, an `rh-src`, and an endmark
- [ ] anything special about a page is expressible as a named `@page` — if it isn't,
      redesign it until it is
- [ ] nothing in the body typesets what the furniture owns (chapter name, folio, title)

**After render**, two gates in order:

1. `scripts/audit-furniture.py dossier.pdf` — the sheet contract, checked on EVERY page:
   painted to the trim, furnished, body inside the column. This is the gate that catches
   the continuation-page failure class: mechanisms that furnish chapter starts and strand
   the pages after them.
2. `scripts/audit-book.py <build-dir>` — the composition verdict: fill, consistency,
   stubs, rhythm, marks, cover, geometry, depth.

A build that passes both can still be improved — the gates are the floor. The ceiling is
the overlay test at the top of this file, and the honest read of a spread at arm's
length: does it look like someone chose this? If a page passes every gate and the answer
is still no, the defect is upstream in this file's terms — name which principle it
violates, fix the system, and let the next build inherit the fix.
