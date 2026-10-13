# Stage E — The image brief

**Never generate images, never pull from a platform API, never ship a hatched
placeholder in a paid PDF.**

There are TWO routes to the files, and the first one is usually available:

**A. The site's own library — look there FIRST.** Every live site already has
`<site>/content/batch-*/images/`, downloaded and licensed for the article batches, with
`batch-NN-images.md` naming each batch's topics. Barcelona had **276 photographs, 168 of
them usable landscape**, sitting unused while its book shipped with six. Mine that before
you ask for anything.

**B. New sourcing** — the user picks, via the contact-sheet artifact (see the
travel-empire skill, Stage 4 §3). Use it only for what the library genuinely lacks.

Either way you emit a brief; route A just means you can fill most of it yourself.

## The sequence

```
1. finish the text + figures        (stages C and D)
2. decide the slots                 → which pages ARGUE better with a photograph
3. emit `dossier-images.md`         → the brief, in the chat, alphanumerically ordered
4. USER hands back the files        → dropped in /mnt/user-data/uploads
5. resize → img/ → base64 → wire    → each with a caption that ARGUES
6. re-render, re-gate               → overflow, sizes, no placeholders
```

## Mining the site's library — contact-sheet it and LOOK

The filenames are stock slugs (`pexels-fotoblend-30991552.jpg`) and say nothing. You
cannot pick from a listing; you have to see the pictures.

```python
# filter to what a plate can actually use, then build sheets of 20 and READ them
for p in sorted(glob.glob('batch-*/images/*')):
    im = Image.open(p); w, h = im.size
    if w/h < 1.25 or w < 1200: continue        # a 2.0in band needs ratio >= 1.5
    cands.append(p)
# 5 x 4 tiles, each labelled with its index and batch, saved as sheet-NN.png
```

No ImageMagick on this machine — PIL does it. Then read each sheet and catalogue what is
actually in frame. Budget one pass: 168 candidates is nine sheets.

**Check your picks against what the book already uses.** Four of the first eight picks on
Rome/Barcelona duplicated an existing plate — two aerial grids, two of the same monastery,
two tapas counters. Render the existing `img/*.jpg` as a sheet too and compare before
cropping.

**Crop to the aspect the SLOT needs, not to 3:2 by reflex.** A head band prints 6.8 × 2.0 in
— a 3.4:1 strip. Cover-fitting a 3:2 file into that throws away the middle of the frame;
crop to the strip deliberately, biased to keep the subject (a skyline sits above centre).

**Build the FIRST-pass sheet pre-cropped to that strip, not as full frames.** Judging a
candidate at full frame and judging it in the band it will actually print as are two
different questions, and they can disagree: a photo that reads as the obvious pick
uncropped can turn out to repeat something the chapter already says once you see the
real crop, while a photo that looked unremarkable full-frame can be the one that answers
what the text doesn't. Offer 2-3 vertical/horizontal offsets of a tall or wide source as
separate candidates in the same sheet, each already cropped to the slot's aspect — not
one thumbnail of the untouched photo. See layout-architect.md §0 for the Morocco case
this was paid for by.

## A head image must MEAN something

The band over "The ground: a city you can walk across" — captioned *"A kilometre and a
half, end to end. The core is the argument, and it is walkable"* — was **a plate of
carbonara**. It passed every gate: the gates count images, they cannot see subject.

A head band is the one image in a chapter that has to carry the argument rather than
decorate it. Caption it with what the plate is DOING for that chapter, in the book's own
register, and if the picture cannot do that job, pick another picture.

## Head bands, plates, and the PL. series

| | class | numbered? | moved by the compositor? |
|---|---|---|---|
| chapter head band | `.photo.band` | **no** | never |
| mid-chapter band | `.photo.band` | no | never |
| numbered plate | `.photo.wide` | **PL. A…** | yes — fed, snugged, filled |
| closing plate | `.photo.closing` | PL. A… | yes |

**Head bands are unnumbered on purpose.** They are furniture, like the kicker: numbering
them numbers the chapters and exhausts the PL. series on decoration.

**Stamp the plate letters AFTER the body is assembled**, in reading order — never from
the slot id. A builder that defines sections out of order (one defines two chapters
*after* the field sheet) produces a counter that runs out of reading order, and the claims
gate checks exactly that: no label twice, no gap.

```python
MARK = 'PL. \u00a7'          # a placeholder emitted by photo()
...
i = k + len(MARK)            # len(), NOT a hard 6 — '§' is 1 char, 2 bytes.
                             # The hard 6 ate the '<' of </span> and every caption
                             # printed as "PL. L/SPAN>".
```

## Coverage — what the fleet actually carries

Pages carrying a photograph, measured as image XObjects per page:

```
Rome 74%   Japan 67%   Thailand 63%   Greece 62%   Turkey 57%   Morocco 45%
```

A book at **17 %** (Barcelona, before) is visibly thinner than its siblings and its PDF is
2 MB against their 10–18. If a book is far below that band, the fix is plates, not CSS.

## SHAPE FIRST — landscape, or it will not work

**Every plate is 3:2 landscape, ≥1600px.** Non-negotiable, and here's the arithmetic that
makes it so:

```
the text column is 6.8in wide.
  a 3:2 landscape at full width  →  4.5in tall   = 49% of the text block   ✓ a plate
  a 4:3 landscape                →  5.1in tall   = 55%                     ✓ workable
  a 2:3 PORTRAIT                 → 10.2in tall   = 109% — taller than the page ✗
```

A portrait can only be fitted by capping its height — which leaves it **~200px wide in a
653px column**, a stamp floating in cream with 480px of dead space beside it. There is no
CSS that fixes this; Rome burned an hour proving it. The fix is the file, not the layout.

**Put it in the brief, and gate it before the build:**

```bash
python3 scripts/validate-images.py img/            # fails on portraits, soft files, wide crops
python3 scripts/validate-images.py img/ --fix      # crops to 3:2 at the densest band
```
`--fix` finds where the detail actually lives (an edge-energy scan by band) rather than
blind-centring — on Rome's al-banco shot the bottom third was empty shadow, so the correct
crop was 14–58%, not the middle. Originals are kept in `img/_originals/`.

The build refuses portraits outright:
```python
if ar and ar < 0.9:
    raise ValueError(f"{slot} is {ar:.2f} (portrait). Crop to ~1.5 before building.")
```

## Choosing the slots — a photo must do work prose can't

A slot exists only where the image is **evidence for an argument the page is already making**.
Rome's four earned their place:

| slot | the argument it proves |
|---|---|
| cover | the whole centre in one frame — the book's thesis |
| the queue | "security cannot be bought; it can only be out-scheduled" |
| the monument + city | "one ticket, one morning, not three visits" |
| the underground | Decision 12's tier fork, made real |

If the page reads identically without the image, **it's decoration — cut the slot**.

**But there is a floor, and Rome hit it from below.** v2 shipped 9 plates: **1 in the first
half, 8 in the second**, with a **15-page text-only run straight through the decisions** —
the analytical heart, and the exact stretch where a skimming buyer decides. Ten refinement
loops missed it because every loop read *pages*; this is a defect of the *sequence*.

**The coverage rule:**

| | |
|---|---|
| plates, minimum | **1 per 6 pages** (a 50pp book wants 8–12) |
| the longest text-only run | **≤ 6 pages** |
| photographs per half | neither half more than 3× the other |
| the first plate | inside the first 12% — it's the sample a buyer sees |
| any 8-page window | at least one visual of *some* kind |

Gate it: `python3 scripts/audit-rhythm.py dossier3.html`

**The decisions are the hardest stretch and the most important.** Fourteen identically
structured pages in a row will lose the reader no matter how good each one is. Every third
or fourth decision wants *something* — a plate, a small figure, a section drawing. Budget
those slots at Stage B, not after the fact when the pages are already full.

## WHERE the plate sits — Greece got this wrong and it read as stale

Greece dumped every plate at the **top of the page, above everything**, and the result reads
like a stock header. Two specific failures:

```
p6:  PHOTO → its caption → THE ROUTE GRAPH → the graph's caption
     the plate outranked the figure that carries the page's whole argument.

p8:  PHOTO of Piraeus → prose about the Fira-to-Oia cliff path
     the caption and the paragraph beneath it are about different islands.
```

**The rules, in order of authority:**

1. **The ARGUING figure leads the page.** On a page with a route graph, a section drawing
   or a data grid, *that* is the lead. A photograph is not automatically the lead figure —
   it earns the position only when the photo IS the evidence (Rome's queue, the hypogeum).
2. **A plate sits WITH the paragraph it argues for**, not at the top by default. If the
   prose beside it is about somewhere else, the plate is in the wrong place — that is a
   slot error, not a layout one. (Rome caught this: a caption about the eating filter was
   sitting on the failure-modes list.)
3. **Never open a page on a photo and then bury its figure.** The reader meets the
   decoration before the argument and files the whole book as a brochure.
4. **A photo page drops its pull quote.** The caption already argues; stacking both blew
   three pages on Rome. `pull = "" if k in PHOTOS_FOR`.
5. **The caption is an argument, not a description.** Not "St Peter's Square, busy." Instead:
   *"Free to enter — and no ticket in existence skips this."*

**Gate it:** for every plate, read its caption and the first sentence of the paragraph next
to it aloud. If they are about different things, move the plate.

## Slot IDs and plate letters MUST agree

**This cost three rounds on Rome.** The brief numbers slots `A01…A10`. The book letters
plates `PL. A…PL. I` **in page order**. They do not correspond:

```
  A07 (espresso) sits on p30  → prints as PL. E
  A06 (trattoria) sits on p31 → prints as PL. F
  A08 (trastevere) on p33     → prints as PL. G
```
So "swap E and G" means one thing to the person picking photos and another to the person
reading the PDF. Two names for the same slot, and no way to see the mismatch.

**Fix it in the build — letter plates by SLOT, not by page:**
```python
# WRONG — page order. A06 and A07 swap letters depending on where they land.
_photn=[0]
def photo(slot, cap, cls="band"):
    _photn[0]+=1
    letter = chr(64+_photn[0])

# RIGHT — the slot IS the identity. A07 is always PL. G, wherever it prints.
def photo(slot, cap, cls="band"):
    letter = chr(64 + int(slot[1:]))      # A01→A, A07→G
```

**And name the files by slot.** Rome's first hand-off used `E.jpg` / `F.png` (plate letters)
and went to the wrong slots twice. `A06.jpg` / `A07.jpg` / `A08.png` was unambiguous
immediately. **Put the slot ID in the brief's filename line and ask for it back.**

## The brief format — emit EXACTLY this, in the chat

Alphanumeric IDs, in order. The user downloads in that order so the mapping is positional
and unambiguous.

```markdown
# <Project> — dossier image brief · Edition YYYY.MM

6 images. **Name each file for its slot** — `A01.jpg`, `A02.jpg`, … — and hand them back.
Order alone is not enough: it breaks the moment one upload fails or one slot is re-picked.

**Every pick must be LANDSCAPE — 3:2 or 4:3, ≥1600px wide.** A vertical phone shot cannot
be used: it needs 7in of height to fill the column and always renders as a stamp. If the
only good frame of a subject is vertical, say so and I'll crop it — but landscape first.

Also: free-commercial licence (Pexels/Unsplash), **no recognizable faces**, **no brand or
logo signage**, no selfie-stick tourists *unless the crowd is the argument*.

---

### A01 · cover · `cover`
**Argument it must prove:** <the book's thesis, in one line>
**Shot:** <framing, light, what must be in frame, what must not>
**Orientation:** landscape, wide — it sits in a 1.6in evidence strip
**Search:**
- https://unsplash.com/s/photos/<tag-query>
- https://www.pexels.com/search/<tag-query>/
- <a specific verified photo-page URL if web_search surfaced one>

### A02 · <chapter> · `<slug>`
...
```

**Link rules — follow exactly (from the article-batch runs):**
- **Unsplash and Pexels only.** Gallery-search URLs are constructed and always resolve:
  `https://unsplash.com/s/photos/<query>` · `https://www.pexels.com/search/<query>/`
  (URL-encode spaces as `%20`).
- Include a **specific verified photo-page** link when `web_search` surfaced one — those are
  pre-vetted single shots.
- **No Wikimedia Commons** unless you verified each link resolves. Guessed `Category:` paths
  are usually wrong and a dead link erodes trust in the whole brief.
- **Queries are photo-TAG words** (subject + place): `rome-colosseum-aerial`,
  `st-peters-square-queue`. **Never** a slugified brief sentence.
- State plainly that these are **pages to pick from**, not direct downloads.

## The slot ID and the plate letter are NOT the same thing

**This caused three wrong installs on Rome.** The brief numbers **slots** (`A06`, `A07`);
the book letters **plates** in *page order* (`PL. A`, `PL. B`…). They do not correspond:

| slot | what the brief asks for | prints as |
|---|---|---|
| A06 | trattoria-lane | **PL. F** |
| A07 | espresso-banco | **PL. E** |
| A08 | trastevere-dusk | **PL. G** |

A07 sits on p30 and A06 on p31, so A07 letters first. The user, reading the PDF, says
"E should go to G" — reasoning from letters — and is describing a slot swap that is wrong.

**Rules:**
- **Always speak in slot IDs** (`A07`), never plate letters, when discussing which image
  goes where. Files must be named `A07.jpg`.
- **Print the slot ID next to the plate letter** in the caption while drafting, or letter
  plates by slot rather than by page.
- Before installing anything, print the mapping and check the caption against the image:
  `slot → plate → page → caption`. A caption that lies is worse than no photograph.

## Wiring the returned files

```python
# resize to print width, keep the aspect
from PIL import Image
im = Image.open(src).convert('RGB')
r = 1500/im.size[0]
im.resize((1500,int(im.size[1]*r)), Image.LANCZOS).save(f'img/{name}.jpg', quality=86, optimize=True)
```

```python
# base64-embed so the PDF is self-contained
import base64
def _img(name):
    with open(f'{BUILD}/img/{name}.jpg','rb') as fh:
        return 'data:image/jpeg;base64,'+base64.b64encode(fh.read()).decode()

_fign=[0]
def photo(name, cap, cls="wide"):
    _fign[0]+=1
    return (f'<figure class="photo {cls}"><img src="{_img(name)}"/>'
            f'<figcaption><span class="fign">FIG. {_fign[0]}</span> &nbsp;{cap}</figcaption></figure>')
```

Heights that worked on Letter: `.photo.wide img{height:2.25in}` ·
`.photo.band img{height:2.35in}` · always `object-fit:cover`.

## The gate

```
□ every slot filled — grep the render for `.ph` → ZERO placeholders in a paid PDF
□ every image loads — check `img.complete && naturalWidth>0`, not just the tag count
□ every caption argues (read them aloud; a description = a rewrite)
□ **every caption is TRUE of its image** — print `slot → plate → page → caption` and check
  each one. Rome nearly shipped "across the bridge at blue hour" over an espresso machine.
□ an empty upload is silent: check every file's byte count. A08 arrived as 2 bytes (a bare
  newline) and looked like a fetch bug for ten minutes.
□ no photo page also carries a pull quote
□ licenses confirmed per file before the product is sold
□ re-run the render gates (stage F) — images change page fill
```

**Licensing:** Pexels/Unsplash permit commercial use, but confirm each individual file's
license before selling. The collection-level license is not a per-file guarantee.
