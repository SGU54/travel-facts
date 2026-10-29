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

**Ruth's recheck** (`_studio/ruth/recheck-v2.md`): 0 blockers, 6 majors. Answered: the before-you-book plans rebuilt from The Plan (arrival day, then its five days in order; three days = The Plan compressed); the Sagrada Família wording now says re-check the official site (no list of authorized distributors is published; resold tickets are refused); p10's "arithmetic" promise corrected; the Field Sheet carries Ruth's official values read 2026-10-25 (T-casual €13.00, Sagrada €26.00, Park Güell €18.00; Hola stays "check current"); when the €5.90 metro ticket still wins (from T1); El Prat's caption names only what the frame shows; the Park Güell frame prints once (the 2+1 poster keeps it). Owner's: M1 (phone reading), M9 (own-site overlap), the listing's "68 pages" (the book is 66).

**Closing pages without a true picture** — first a red field with the poster's call (it printed the poster's sentence twice), then the chapter's name (the layout gate read it as a stranded opener on Failure Modes, whose tail had no words). Marta's final rule: a decision keeps its verdict word in gold on the ink field; an essay closes on its name on the red field; a closing with under 200 characters of text has no page — its words join the prose.

Final: **66 pages**, cover says 66, Field Sheet one sheet, six gates green, Brunner 20 (0 blockers; 11 `side`, 4 `runt`, 3 `foot`, 2 `hole`), fidelity 0 printed twice, apparatus 0, Marta 0 KILL (8 `system` notes inside the Season II posters). Candidate: `../atelier-studio-2026-10-25/`. Not published.

## 2026-10-26 — after release

**Owner on provenance:** the book's photographs came from Unsplash and Pexels (free licences, no attribution). Recorded on the six kept frames; the exact pages were not kept at download. New frames are recorded with their Unsplash page, photographer and licence (`media` skill `search.py` → `adopt.py`).

**Owner on Ruth's M9** (what the book sells beyond the free site): *the book is a decision manual that helps American travelers make the calls; it holds the links between the free guides, which the site never makes; and the Field Sheet keeps the volatile figures current.* p3 already says this ("Each of the calls that follows connects facts the free articles leave scattered…"), and How to Read This presents the Field Sheet. M9 closed by the owner's statement.

**Unsplash refill (2026-10-26, owner: "peut-on en chercher sur unsplash pexels pour les marges et les fermetures"):** `media` skill `search.py` on 20 slots (13 closings, 7 margins), 9 vetted candidates each (Unsplash+ excluded, originals measured, fleet duplicates excluded). Marta filled 3 and left 17 typographic (already-printed subjects, a verdict word no frame can name, brand names or strangers' faces, unplaceable lanes, places the text never names): How to Read This closes on the Passeig de Gràcia wayfinding post before La Pedrera (p7); Timing on Barceloneta under cloud (p21); a margin frame of Park Güell's serpentine bench beside the Park Güell section (p24, which then closes in its prose). Blind look clean on all three; provenance recorded (images.unsplash.com id, Unsplash License). Her tool: 9 frames, 0 KILL; `text_is_subject` exempts a sign photographed for its words when the corner lies in the subject box; a `coast` category (a beach is not a city view). 66 pages, six gates green. Pexels not searched: no API key, and Unsplash answered the slots that a true frame could fill.

**Whole frames inside the text (owner, 2026-10-26: "the image is set in the middle"):** a fixed band height shrank A03/A05/p-contract and centred them while the caption ran the full width. Full measure (652) pushed the text to 68 pages; *Marta:* the frame prints whole on the 340 column, flush left, its caption beside it in the margin, on its foot (pp. 27, 42, 51). The owner approved it. Brunner notes the column above the caption is open beside the picture (accepted by the owner).

Republished 2026-10-26 (owner: "républie le pdf en entier"): Stripe storage and Etsy files replaced; site, Stripe image and R2 previews unchanged (same cover and preview pages).

## 2026-10-26 — phone edition and the joins (owner: "partant pour la partie 3 et 4")

**Phone edition** (`phone.py` → `Barcelona-Without-the-Traps-phone.pdf`): the same words (manuscript + writer.py + Brunner's US style), the same pictures (only the frames the book prints, Marta's captions), one column on a 3.6 × 7.2 in page at 11 pt (≈16 CSS px on a phone), white sheet. Drawn figures much wider than tall turn a quarter on their own page ("Turn your phone sideways"); square maps stay upright. The Field Sheet closes it. 24 bookmarks, fonts all named (bold italic never synthesised: `font-synthesis:none`), no Type3. Text checked against the manuscript: complete (the only differences are US spellings).

**The joins** (`_studio/writer/joins.json`, owner's M9 answer made visible): each decision carries "What the free guides never connect" — one sentence naming 2–3 of the site's free articles and the connection none of them makes, which is the call. Quotes checked word for word against corpus.json; 17 article URLs return 200. The writer flags D01 as the weakest join (the site's "Where to Stay" already makes the Eixample call), D05 next. Placed on each decision's closing page beside the note (decisions without a map) and on the map page under the ribbon (D01, D06, 400 px measure): a first placement beside the forks pushed four decisions onto an extra page. In the phone edition, right after the verdict. Book still 66 pages, six gates green.

## 2026-10-28 — Hannah's rights pass (studio card 36, approved by the owner)

- 12 printed frames, each now with author, original page, licence and date read (`_studio/marta/pictures.json`, `_studio/marta/credits.json`).
- Re-found by perceptual hash and confirmed on unsplash.com (not Unsplash+): Sagrada Família nave (William Rudolph), Montserrat (M I S S S U), the Bunkers del Carmel (Zuoranyi), El Prat (Tobias), La Rambla from above (Ronni Kurtz), the signpost (Ruan Martinelli), Barceloneta under cloud (Olesia Libra).
- Replaced, same subject: the Eixample from above → Logan Armstrong; Park Güell's gatehouses (poster vignette) → Martijn Vonk; Casa Batlló (poster vignette) → Juhi Sewchurran; Park Güell's bench (page not recoverable) → Diego Machiaveli; the beach promenade (original under GFDL 1.2 only, unusable in a paid PDF) → Lucrezia Carnelos, located Barcelona; its caption now names only what it shows ("A Barcelona beachfront under its palms…", Torre Mapfre removed).
- Credits: a "Photographs" paragraph on the last page (p66); still 66 pages. Bookmarks restored (`add-outline.py`, 24); six release gates green (`_studio/release-2026-10-28.txt`).
- Shipped: `../atelier-release-2026-10-28/` (locked, 8 MB); bucket `guides/Barcelona/barcelona-without-the-traps.pdf` replaced, read back identical; Etsy listing 4599529208 file replaced; site preview p37 re-cut (new key `barcelona-guide-preview-2026-10-28-2-gaudi-fork`, site commit 80b60f3). Field Sheet unchanged.
