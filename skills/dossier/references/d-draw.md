# Stage D — Draw

**Every figure is our own artwork, computed from real public coordinates.** No platform
tiles, no stock diagrams, nothing republished. This is what makes the book unclonable: a
competitor can't put your cover on theirs without having written your chapter one.

## Compute first, draw second

```python
import math
LM = {"Pantheon":(41.8986,12.4769), "Colosseum":(41.8902,12.4922), ...}
def km(a,b):
    (la1,lo1),(la2,lo2)=LM[a],LM[b]; R=6371; p=math.pi/180
    dx=(lo2-lo1)*p*math.cos((la1+la2)*p/2); dy=(la2-la1)*p
    return R*math.hypot(dx,dy)*1.25          # 1.25 = street factor, not crow-flies
def mins(a,b): return round(km(a,b)/4.5*60)   # 4.5 km/h walking
```

Rome's numbers came out validating the book's own claims: Monti→Colosseum 9 min,
Termini→Pantheon 34 min, the core 1.2 × 1.65 km. **If the geography contradicts your thesis,
the thesis is wrong.**

## The figure set that earned its place

| figure | the argument it replaces |
|---|---|
| the ORGANISING-FACT figure | Rome: zones + 1km ring. A country: the route graph with real\n  frequencies. Draw the fact from a2-shape.md, not Rome's. |
| the trap ring | original intel; nobody publishes this |
| transit reality | draw the hole where the centre is |
| 6 × neighborhood locators | "15–25 min from the centro" made instant |
| the week grid | closures as a pattern |
| the month strip | the season decision, seen |
| the order-of-ops flow | the set-piece day |
| the decision tree | replaces an hour of forum reading |
| 7 × distance maps | "X is close, Y isn't" |
| a section drawing | what a photo *can't* show — under the floor, or what stood here |

**Argue against the obvious figure.** Rome refused to print a metro plan: it's free at every
station and it contradicts the walk-everywhere thesis. The transit-reality map argues instead.

## Label placement — the collision problem

Labels collide with each other AND with marker dots. Solve it once:

```python
class _Boxes:
    """Reserve every marker + fixed label FIRST; then place the rest around them."""
    def __init__(self): self.b=[]
    def _hit(self,x0,y0,x1,y1):
        return any(min(x1,a1)-max(x0,a0)>1 and min(y1,c1)-max(y0,c0)>1
                   for (a0,c0,a1,c1) in self.b)
    def add(self,x0,y0,x1,y1): self.b.append((x0,y0,x1,y1))
    def place(self, x, y, text, fs, anchor="start", tries=None):
        w=len(text)*fs*0.58; h=fs
        if tries is None:
            tries=[(0,0,anchor),(0,-fs-3,anchor),(0,fs+5,anchor),
                   (0,0,"end" if anchor=="start" else "start"),
                   (0,fs+7,"middle"),(0,-fs-9,"middle")]
        for dx,dy,an in tries:
            xx,yy=x+dx,y+dy
            x0 = xx if an=="start" else (xx-w/2 if an=="middle" else xx-w)
            if not self._hit(x0,yy-h*0.78,x0+w,yy+h*0.24):
                self.add(x0,yy-h*0.78,x0+w,yy+h*0.24); return xx,yy,an
        x0 = x if anchor=="start" else (x-w/2 if anchor=="middle" else x-w)
        self.add(x0,y-h*0.78,x0+w,y+h*0.24); return x,y,anchor
```

**Order matters: dots and fixed labels reserve their boxes in a pass 0**, before any
placeable label is positioned. Rome's badges-and-labels-in-one-loop bug meant an early badge
blocked a later label with no recourse.

**Target the condition, not the category.** "All inside-ring labels point inward" flipped four
correct labels to fix one. The real condition was: *inside the ring AND the outward text would
cross the rim*.

## Verify with geometry, not with your eyes

```python
# 1. no label outside the canvas
# 2. no label box overlapping another label box
# 3. no dot centre strictly inside a glyph box  ← the STRICT test; a label
#    beside its own dot is correct design, not a collision
```
Rome's first detector reported 36 phantom collisions because it was loose. The strict one
found 2 real ones.

**But a character-count estimate can only PROPOSE a position — it cannot certify
containment.** Greece p35 shipped its plan figure with the payoff annotation
running off the canvas: the printed line ends `THE NIGHT THAT SAVES THE FLIGH`,
inside a rectangle with ample unused space above and below. Rule 1 was already in
this file; nothing measured it.

After the fonts have loaded, measure each `<text>` element's real
`getBBox()`, transformed into the ROOT SVG coordinate system, against the viewBox
with 16 units of clearance. Anchor a right-hand annotation at
`x = viewBoxWidth - 24` with `text-anchor="end"` and wrap it into explicit
`<tspan>` lines rather than letting it run. **Fail the build on overflow; never
`overflow:hidden`** — hiding it is how a truncated sentence reaches a paid page.

## The figure prints at the size it prints at

One root `viewBox` matched to the intended width — `viewBox="0 0 652 H"` with
`width:100%; height:auto; display:block` — and **no nested whole-figure scale
transform**. A transform is why Turkey p36's remedy labels declare 11–13px and
print at ~5.8pt, below even the old floor: checking the declaration told you
nothing.

At 652 units wide, essential labels are **at least 12 units**. If they do not fit:
increase the figure height, wrap the labels, or move a long source line into an
HTML caption at the caption size. **Reduce the type last, and never below the
printed floor.** Turkey p36 had an empty lower half of the page while its labels
were unreadable — the space was spent on internal padding. Keep internal padding
only where it prevents a real collision, and inspect the result at actual Letter
size.

## Sizes

The rendered height comes from the **viewBox aspect**, not from CSS. A 660×120 viewBox
renders ~119px and looks stunted next to a 660×300 figure at 293px. Design the viewBox for
the job: `band` ≈ 660×240, `wide` ≈ 660×300, a section drawing ≈ 660×270.

## Print weight

Screen values die on paper. A 1.5px dashed line at `1.5 7` spacing rendered 0.87% ink and was
nearly invisible. Ring lines want ~2.2px at `3 6`; labels want 11–13px in a ~700-unit viewBox.
**Measure the ink**, don't trust the preview.


## The `.flow` section — the mechanism behind layout.md

A chapter that flows is one `<div class="flow">` holding its sections as `<div class="dec">`
blocks; the print engine paginates it. The CSS that makes it behave (tuned on this
Chromium — others differ):

```css
.flow{ padding:0.5in 0.78in; font: <body>; }      /* symmetric pad clears the
                                                       header/footer template band */
.flow .dec + .dec{ margin-top:26px; }              /* space between sections */

/* headings never strand at the foot of a page */
.flow h1, .flow .dnum, .flow .standfirst{ break-after:avoid; }

/* these never split across the fold */
.flow table, .flow figure, .flow .forlist, .flow .note{ break-inside:avoid; }

/* the verdict is the payload: never split, never start a page headless */
.flow .verdict{ break-inside:avoid; }
.flow .verdict + .forlist{ break-before:avoid; }

/* typographic minimum */
.flow p{ orphans:3; widows:3; }
```

Emit visuals INSIDE the flow, right after the paragraph they argue — never as a standalone
`page()`. The engine drops them onto the current page when they fit and pushes them over
when they don't. That single behaviour fixes empty pages, stranded figures, and
figure-plus-photo pile-ups at once. Then render and run `audit-page-shape.py`; do not
hand-tune break points (bug 24).
