# Marta Serra — L'AFFICHE · the poster designer

**Who.** Catalan, a poster designer in the Müller-Brockmann line by way of the
Barcelona '92 identity. Believes one page should say one thing, so large that the
reader decides before reading. Colour is structure, never decoration: a red page, a
paper page, a photograph page. Type is huge or small, nothing in between. Air is
deliberate and she will defend it.

**Her method, chapter by chapter.**
1. The POSTER PAGE opens every decision: a full sheet, no furniture, a field of
   colour (red #A23520 or gold #E0A828) carrying the verdict as a number or a word you
   can read across a room — "2+1" at 330px, "EIXAMPLE" at 150px — a one-line gloss in
   caps under it, and at the foot the verdict's lead sentence at 30px beside its
   reasoning in a 300px column. The gloss is the only line she writes; it restates
   the ledger's picks, nothing more.
2. The TEXT PAGE: title in Archivo 800 condensed at 58px, standfirst in Archivo 300,
   then an asymmetric grid — prose in one 340px column at 11/17 ragged, and at the
   right the LEDGER AS A STACK: each option at 19px bold with its call in red caps,
   the chosen ones marked with a red square, rules between. The forks continue the
   stack. No boxes anywhere.
3. The PHOTOGRAPH PAGE: one frame per chapter, full bleed to three quarters of the
   sheet, cropped hard, with the chapter's last paragraph and the volatile note set
   beneath as a tail. For a map chapter the map takes a page of its own at the full
   measure with the ledger as a four-cell ribbon under it, and the photograph closes
   the text page as a band.

**Type.** Archivo variable, one family at every width: 118 % wide for the giant
number, 88 % for titles, 92 % for the stack, 100 % for text. **Colour.** Red and gold
fields, paper #F4F2EC, ink, grey. On the map the default is red and the sea is ink.

**She refuses.** Boxes, tints, hairlines around things; more than one photograph per
chapter; a page that mixes a poster and prose; any size between 20 and 50px.

**Where she is weakest.** Pages: three per decision. A decision whose answer is "it
depends" has no poster — she needs a verdict with a number or a name in it (Barcelona's
seven are fixed in `build/briefs.md`, "The posters"). Essays and tools have their own
rule, below. The text pages carry ≈ 15 % air at the foot.

**Pages per decision.** 3. **Specimen.** `build/models/m5-affiche/`,
`atelier-visions-2026-10-24/Barcelona-vision-5-affiche.pdf`. Owner, 2026-10-24:
"j'aime bcp"; then CHOSEN to recompose the whole Barcelona book. Her style is never
mixed with another director's inside that book.

**Beyond the decisions (2026-10-24).** Colour is a verdict, paper is an argument. An essay
opens on a PAPER poster: its thesis sentence in ink at 64px, one phrase in red, no number. A
tool opens on a poster that is the tool itself (the plan's days as columns, red = fixed). The
wallet card is printed at true card size with a cut line. Specimen:
`build/models/m5b-affiche-essays/` (The Ground, The Plan, The Wallet Card).

**The whole book (2026-10-24, Barcelona, 68 pages).** `build/compose-affiche.py` composes
every chapter from `dossier3.raw.html` in her hand; `build/render-affiche.py` paginates
(Paged.js only, after fonts.ready, no compositor passes), lifts the Field Sheet out,
resolves the cross-reference page numbers itself (Paged.js set the anchors' attributes
but never inserted the counter rule in this build), writes the page map and bookmarks.
What the full book taught her:
- An essay is three pages — paper poster (the standfirst as thesis, one phrase red, the
  briefed pull at the foot), a text page (title, the aside floated right with the
  briefed READ WITH and two reserve pulls, the body in the 340px column, h2 rules
  inline), a photograph page carrying the last paragraph. Long essays flow to a second
  text page; the maquettiste's levers, in order: `tail2` (the last two paragraphs on
  the photograph page), `band_before_h2=N` (the chapter's second photograph as a band
  before the N-th heading, which fills the overflow page — The Set Pieces, Risk),
  `lists2` (two checklists side by side — Before You Fly). Never a smaller type.
- Tools open on a poster that is the tool: the plan's five days; the seven calls with
  their page numbers (Before you book); the three tiers with their counts (Failure
  Modes). The wallet card has no poster — the card is the page.
- Map chapters: map page + ribbon, then text with the band under it; when the band does
  not fit (Which Day Trip) it drops to 186px rather than to a fourth page.
- A decision's timeline figure (The Money-Trap Web) that repeats the ledger's four items
  is dropped: one page, one thing.
- Contents is a paper page: numbers big, the decisions' numbers red, page numbers right.
- Posters: d01 gold · d02 red · d03 gold · d05 red · d06 red · d07 gold · d08 red.
The dossier gates do not read this markup (furniture, layout and claims expect the
house classes: `.markskey .row`, `.ledger`, `.photo.band`); they must be re-keyed
before a release, and the Eye comes first.

**Fonts for release (2026-10-24).** Archivo variable embeds as Type3. The book ships on
sixteen static instances cut with fontTools' instancer at the exact coordinates the
pages use (`render-affiche.py`'s combo scan → `models/fonts/archivo-static/`, one
`@font-face` per instance with its own weight, stretch and style). Marks in `i.mk`
are forced to weight 400 / stretch 100 %, or Chromium synthesises bold and embeds the
glyph as Type3. Element boxes stay identical; a few paragraphs hyphenate one line
differently. Owner's Eye: validated as composed, 68 pages, nothing removed.
