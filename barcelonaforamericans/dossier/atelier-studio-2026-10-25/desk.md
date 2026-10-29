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

## 2026-10-25 — the studio of three: second edition in `build-studio/` (owner: "reproduis Barcelone avec les nouveaux personnages")

Brunner's proof on the edition on sale (new tools): **290 faults, 5 blockers**; fidelity: the 14 "lost" paragraphs are the Field Sheet (printed as its own document — checked separately), 4 paragraphs printed twice (photo captions repeated as pulls).

**Brunner → writer (US house style, `brunner_set.us_house`, shared by every book):** 49 British spellings (grey, licence, defence, traveller, authorised…) → US; "decision 03" → "Decision 03"; months spelled out; period and comma inside the quote; scare quotes double; 8:30pm → 8:30 p.m.; 16:00 → 4 p.m. in prose; dinner hours say p.m.; `lang="en-US"`.

**Brunner → Marta, her answers (`studio.py`):**
- captions in capitals (×81) → *Marta:* a caption is a sentence: sentence case; a label in capitals holds six words or fewer, a longer one is set in lower case; text typed in capitals over six words (figure titles) → sentence case, names kept.
- display tracking closing word spaces (×80) → *Marta:* tracking tightens letters, never words: word-spacing .09–.16 em on display type.
- the five "cut" captions → four were fragments without their period (now ended); the fifth was a real contradiction: the map caption read "the default in gold … — the pick in red" on a map recoloured red → "in red", suffix removed (d01, d07 maps, their SVG titles too).
- FIG. 6 horizons: title over the axis, a label past the panel, "two gold bars" printed red → axis under the bars, long labels inside their bars, text and caption say red.
- display lines and paragraphs ending on one word → the last two words travel together (≤12/14 letters); a poster line never begins with a dash.
- the empty margin beside text (×13) → *Marta:* the margin runs with the text: "Read with" and the first pull at the top; the next pulls and **The calls this chapter decides** after each h2, after a figure when there is one (a figure clears the float), or at the top when there is neither; never beside a two-column checklist (it runs full width).
- Brunner's tool fixed on the way: a `<br>` is a word break (cover "WITHOUTTHE"); a provenance mark before its period is punctuation; a legend swatch is not a scatter dot.

Result so far: 290 → **22 faults, 0 blockers**, 68 pages. Open: 11 `side`, 5 `foot`, 2 `hole`, 4 `runt` — Marta's margin pictures (waiting on her ledger).

**Ruth's first reading** (`_studio/ruth/critic.md`): SHIP AFTER FIXES — 2 blockers, 10 majors, 21 minors. The writer's answers are `writer.py` (each edit with Ruth's id and its source; an edit that stops matching stops the build): B1 one numbering of days (the arrival day holds nothing timed; the before-you-book plans start at "Arrival day"); B2 the Sagrada Família resale wording made true to the basilica's conditions 3.9/4.3; M2 "arithmetic" → reasoning shown, sums on the Sheet; M3 the Sheet's tax table complete (3★ €7.00, apartments €9.50, a two-people five-nights example) and dated October 2026; M4 the T-casual still reaches the airport by Rodalies R2 Nord or bus; M5 the bed books early in the centenary year; M6 the card-issuer numbers on the checklist; M10 112 and the passport's three months. M1 (phone reading), M9 (own-site overlap) → owner. M7, M8 → Marta.

**Marta's ledger** (`_studio/marta/pictures.json`, blind look on source-window crops): 24 printed frames → 6 kept, 18 killed (5 AI-made, 4 wrong place, 2 with legible corner text, 3 soft, 4 a false caption or no job), 1 replacement (p-d06, Park Güell's gatehouses), 3 moves (La Rambla to the risk chapter, El Prat to Day Zero, the Bunkers del Carmel to the last closing). `marta_pics.py` applies it: a decision's closing keeps its verdict word in gold on the ink field; an essay's closing sets its call on the red field. A caption prints once (the poster foot no longer repeats it). Her tool on the new render: 0 KILL; 8 `system` notes, all inside the Season II posters the owner approved (handed to the owner).

**Gates:** the rhythm gate counted full-sheet posters and fields as "text-only" once the photographs went; a full-sheet page is composition, not a text desert — the gate reads `_fullsheet.json` (build-studio copy). Six release gates green; fonts all named (Type0), no Type3; 24 bookmarks; Field Sheet on one sheet.

Result: 67 pages, Brunner 20 (0 blockers: 11 `side`, 4 `runt`, 3 `foot`, 2 `hole` — the margin needs true photographs the library does not have), fidelity 0 printed twice.
