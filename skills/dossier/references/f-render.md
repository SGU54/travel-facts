# Stage F — Render and gate

## The render (the paginated model)

The book is paginated **in the browser** by Paged.js into real page divs, THEN printed.
Do not print the raw flow: this Chromium cannot furnish or paint flowed pages (the
graveyard of dead mechanisms is in page-spec.md). The driver is
`scripts/render-paged.py` — copy it into the build with `assets/paged.polyfill.js` and run:

```
python3 render-paged.py            # dossier3.html + paged.polyfill.js → dossier.pdf
```

What the driver does, and why each step is load-bearing:

1. Injects the polyfill with `PagedConfig={auto:false}` — pagination must not start
   before fonts exist, or every measurement is wrong.
2. Registers the **opener handler** — any page whose content holds an H1 gets its
   running head suppressed (chapter openers announce themselves).
3. `await document.fonts.ready`, then **pre-decodes every image**, then `preview()` and
   waits on its promise (never a sleep).
4. Runs the **feathering loop** (layout-architect.md §4): measures every chapter's tail
   fragment, applies TIGHT / FEED / LOOSE per chapter, re-paginates, up to 4 passes.
5. Prints with `prefer_css_page_size=True, print_background=True, margin=0`, and
   **asserts DOM page count == PDF page count** — a mismatch means a page split or
   vanished in print.

**Feeding rules the paginator imposes (hard-won):**
- **Fonts and photos by FILE URL, never base64.** Megabytes of data-URI stall the CSS
  parse for minutes and make the measure loop end the book early — silently, no error,
  a different truncation point per run. If the book comes out short, check this first.
- **One CSS selector per named string** (`.rh-src` only) — two selectors setting the
  same string shadow each other and the running head goes stale.
- The build HTML stays engine-pure: the polyfill and handlers are injected at render
  time by the driver, never written into dossier3.html.

## THE GATES — run all of them, every time

```
python3 scripts/audit-furniture.py dossier.pdf     # the sheet contract, EVERY page
python3 scripts/audit-book.py <build-dir>          # the composition verdict (runs the rest)
```

`audit-furniture.py` is first because it catches the class of failure that a glance at
page 1 always misses: chapter-START pages correct, CONTINUATION pages unpainted,
unfurnished, and 2px from the trim. It checks, per page: paper to all four trim edges;
folio on every interior page; runhead on every non-opener page; body inside 92–984px.
It fails the pre-paged architecture on nearly every page — that is the point.

`audit-book.py` then gives the single clean/clumsy verdict (fill, consistency, stubs,
rhythm, marks, cover, geometry, depth).

## Then verify by EXTRACTING, not by looking

```python
from pypdf import PdfReader
r = PdfReader(PDF)
print(len(r.pages), 'pages |', sum(len(p.extract_text().split()) for p in r.pages), 'words')
print(r.pages[0].extract_text())     # ← this is what caught "COLOSSEUM" clipped to "COL"
```

Text extraction catches what the eye and the DOM both miss: labels rendered outside the
canvas, clipped strings, missing figures, and a TOC whose target-counters resolved to 0
(a broken anchor id). **Run it on the cover, the TOC, and any figure-heavy page.**

Two extraction checks specific to this model:

- **TOC numbers**: every row must show a non-zero folio. A `0` means the row's `href`
  doesn't match a section `id` (the paginator resolved nothing).
- **Runheads**: dump the head-band words of every page; continuation pages must carry
  the CURRENT chapter, never the previous one (the stale-string symptom of the
  two-selector bug above).

## Spacing that ships (the scale — layout-architect.md §2 is authoritative)

```
one baseline           22.5px  (body 13.4/22.5 — the book's ONE leading)
scale                  6 · 11 · 17 · 22.5 · 34 · 45 · 68
eyebrow → title        19px    (17-step + rule offset)
figure → next block    22.5px  ← .map AND .photo, same rule, or captions weld
caption                7.5px, 10px off its figure, 8px rule gap
```

**The test:** every gap between blocks is at least one baseline; a page whose blocks sit
closer reads as one undifferentiated mass.
