# Stage D.5 — THE COVER: earn it, don't template it

The cover is the one page a buyer sees before deciding. It is worth a disproportionate
share of the design budget, and it is the page most likely to be phoned in. Greece's first
cover was **1.4% ink — the title on a blank sheet.** That is not a cover; it is a title
page that wandered to the front.

## The cover makes the organising distinction VISIBLE; the interior figure proves it

> This rule used to read "The cover must ARGUE the book's thesis", and the books
> took it literally: Rome's cover carries a walk-radius map whose ring labels
> print at **~2.96pt** and whose "Pantheon" prints at **3.88pt**. At a 180px-wide
> preview — how most buyers first meet it — that label is about **one screen
> pixel**. A cover asked to argue produced a miniature analytical page whose
> premises cannot be read at any size a buyer sees.

A cover promises; the interior proves. So:

- **One primary visual device.** Turkey's cover carries a condensed title, ruled
  assertions *and* a route network — more competing components than either other
  book.
- **No figure caption on the cover**, and **at most three short diagram labels**.
- Any label that remains targets **≥24 CSS px at final cover size**. If it does
  not fit, **remove the label — do not shrink it**.
- A simplified, explicitly diagrammatic derivative of the computed geography is
  allowed and encouraged. The full figure lives inside. **Do not present the
  simplified version as a scale map.**
- Set the promise line around **22–24px**.
- **Check the finished cover at 180px and 240px wide**, not only at print size.
  That is the gallery, the store listing and the email.

The computation still informs the cover. It just stops being the cover.

This is the whole rule. A travel guide's default cover is a pretty photo of the place. A
DECISION manual's cover is the argument that makes it worth money. The test:

> Could this cover sit on any book about this destination? If yes, it is decoration. It
> must be reproducible ONLY by someone who did this book's specific analysis.

Rome's cover is a one-kilometre ring drawn from real coordinates, because Rome's thesis is
**scale** — the centre is smaller than you think. You cannot draw that ring without the
walk-times, so the cover is the moat, visible before you open it.

Greece's thesis is not scale, it is a **trade governed by a wind**. So its cover options
were all arguments, not scenery:
- **the wind map** — the meltemi as streamlines behind the real route it cancels
- **the asymmetry** — the same trip drawn twice, one order costing an afternoon, the other
  costing the flight home
- **the ledger** — the single decision table, marked, verdict showing: the book's own
  instrument on its face

Each is unclonable without the data. Each states the thesis in one look. THAT is a cover.

## Derive the cover from the organising fact (a2-shape.md)

The organising fact you found at Stage A2 dictates the cover device:

| organising fact | the cover argues it as |
|---|---|
| scale (compact city) | a distance ring / a one-unit map drawn to real coords |
| a network (islands, transit) | the graph itself — real nodes, real edges, real distances |
| a force (wind, season, tide) | the force drawn as the ground the whole page sits on |
| a sequence (a country) | the ordering, with the cost of getting it wrong shown |
| a single fork | the two branches, with what each buys |

Do not reach for a photograph. A photograph is the ONE cover any competitor can also buy
from the same stock library — it proves nothing about your analysis.

## Build it as a computed figure, not a one-off

The cover lives in `maps.py` beside the other figures, computed from `geo.py`'s real
coordinates — `COVER_<NAME>()`. The distances on it are calculated at build time, so if a
coordinate changes the cover redraws. That is what makes it unclonable AND maintainable:
a hand-drawn cover rots; a computed one stays true.

## The cover gets its own render pass — check these, on the RENDERED pdf

The standalone SVG lies. Greece's cover looked right in isolation and had three defects the
PDF exposed:
1. **contrast/hierarchy** — the wind streamlines came out as hard teal competing with the
   route; they had to drop to ~0.4 opacity and 0.8px so the argument sits on top and the
   texture sits behind. Rule: the thesis line is 100% weight; everything supporting it is
   demonstrably lighter.
2. **fonts in SVG** — a mono/display face bound by `@font-face` needs its family named in
   the SVG `font-family` too, or it silently falls back to serif. Render and read the
   labels; do not trust that they inherit.
3. **full bleed** — the cover is `position:absolute; top:0; left:0; width:8.5in;
   height:11in` with zero page padding, or it inherits the body margin and sits in a frame.

Ink budget: a cover that is arguing something lands around **6-9% ink** (Greece's ledger
option was 8.2%). A cover under ~2% is type on paper — send it back.

## Do NOT skimp here to save time

The cover is the single highest-leverage page in the book and the one a hurried builder
shortchanges first. Budget real iterations: draft the device, render it in the PDF, read it
at thumbnail size (a buyer's first look), and fix contrast and hierarchy before moving on.
Two rounds on the cover is normal. Zero rounds is how you ship a title page.


## The subtitle sells the promise — it is not a description of the book

The title names the organising fact ("Greece, in Order"). The SUBTITLE must carry the
buyer's promise — what THEY get, framed around the dominant edge (see model.md's tally).
It is the highest-leverage sentence on the cover after the title.

- **Wrong** (describes the book, meta): "The decisions that decide a first trip."
- **Wrong** (generic benefit): "Your essential Greece planning guide."
- **Right** (money-dominant destination): "What a first trip really costs — and where the
  money leaks." / "The reality behind the price of a Greek island week."
- **Right** (experience-dominant destination): "Which of it is actually worth your time —
  and which is the photo everyone regrets."

The promise leads with whatever the corpus tally says the dominant edge is. Money leads
ONLY when the tally says money. Do not default to a savings promise on a destination whose
gaps are about taste, not cost.