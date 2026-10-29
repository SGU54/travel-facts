# Desk — Barcelona, Without the Traps. (Affiche, Season II posters)

The log of what Elias Brunner asked and Marta Serra decided. Protocol: atelier/references/desk.md.

## 2026-10-25 — first merged build

Brunner's first proof on the released book: 52 faults (22 glyph, 21 runt, 4 measure, 3 hole, 2 ladder).

**Brunner's standing fixes, now in every build** (`compose-affiche.py`, "Elias Brunner"):
- glyph ×22 — real quotes and apostrophes set in the text at compose (`brunner_set`).
- runt ×21 — the last words of a paragraph glued when the tail is short; a hard hyphen in the last word made non-breaking; three short words kept together.
- ladder ×2 — `hyphenate-limit-chars: 7 3 3`, `orphans/widows: 2`.

**Handed to Marta, and her answers:**
- p56 · measure (the Plan's day sheet ran ~104 characters a line) → *Marta:* the day sheet keeps her reading measure, the 340px column (`.dayrow p{max-width:340px}`).
- p14 · hole (Before You Fly: the grid aligned rows, leaving a hole beside the long item) → *Marta:* the heading spans both lists, and a checklist is two columns that read down, balanced by length (`list_cols`), not a row grid.
- p61 · hole (The Wallet Card: the right list ends above the cards) → *Marta:* "the two lists end where their facts end; the short column's air is mine" (`data-air` on `.wgrid`).
- p59 · hole → not a hole: the group heading's rule spans the row (Brunner's proof fixed to read a heading's rule as occupied).

**Marta's Season II posters** replace the seven decision posters (`marta2.py` ← `models/m9-marta-II`).
Found on the way and fixed: a poster exactly the sheet's height split onto two pages (1px rounding;
posters set to 1055px); the Eixample grid drawn past the trim pushed its poster to a new page (now a
pattern inside the sheet); images nested in Form XObjects by the blend modes hid them from the book
gate's rhythm check (detector made recursive); the verdict on the new posters tagged `.verdict`.

**Result:** 68 pages (unchanged), Brunner 0 faults, six release gates green, fonts all named static
Archivo instances + Noto Symbols 2. Desk empty. Next: the owner's Eye.

## 2026-10-25 — the whole specimen (owner: "de la couverture à la fin")

- The cover is now Season II: the Eixample grid, one block gold, "One block of the grid is yours. Decision 01 says which." (`marta2.cover()`).
- Each decision's closing photograph (d02, d03, d05, d06, d08) is printed duotone in the book's two inks with its verdict overprinted in gold — HOTEL, 4, 3, 2+1, 20:30 (`photo_page(..., duo=sid)`). d01 and d07 close on a band under the map, unchanged.
- Posters and cover end at 1055px; a shadow of their own colour paints the last pixel row (MONTSERRAT's in ink).
- Result: 68 pages, Brunner 0 faults, six release gates green, 21 named TrueType faces. Desk empty.

## 2026-10-25 — owner's look: two points

- **Cover not like the specimen** (owner: the other blocks oversized beside a right-sized gold one). Cause: the grid had been drawn as an SVG `<pattern>` (to stop Paged.js splitting the poster); some PDF viewers draw a Chrome pattern at another scale. Now the grid is a 288-dpi image of the same polygons (`eixample_grid` in m9 build.py), the gold/red block a vector on top — identical in every viewer, and Paged.js cannot split an image. Cover and EIXAMPLE checked against the specimen.
- **Photographs in the 2+1 squares (p38)** — *Marta:* yes, as an exception to "one photograph per chapter", because each photo sits inside a shape that carries the verdict: the two full squares hold the two ticketed sites in black and white (Sagrada Família's nave, Park Güell's monumental zone); the empty square stays "the house you choose" — Casa Batlló in gold, inside the outline.
- 68 pages, Brunner 0, six gates green.
