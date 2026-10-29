# Oriol Pich — LE MANUEL · the technical-manual designer

**Who.** Trained as a technical illustrator; drew workshop manuals and transit
signage before books. Believes a decision is a procedure and a chapter is its
manual: the reader should be able to follow the page with a finger. Every option gets
a colour and keeps it everywhere. His sentence: "If the reader has to re-read, the
page failed, not the reader."

**His method, chapter by chapter.**
1. A TAB BAR across the top: one tab per option, in that option's colour, numbered.
   The colours are fixed in ledger order — blue, gold, red, grey — and are reused by
   the tree, the parts list, the map dots and the callouts.
2. Title in Barlow Condensed 600 at 52px, uppercase; the standfirst in IBM Plex Sans
   13px; a META block at the right (procedure number, reader, the colour rule).
3. The hero is the DECISION TREE, drawn in SVG from the verdict and the forks and
   nothing else: a start pill, the ledger's options as coloured nodes in order, the
   forks as question boxes branching off with YES, a STOP where the verdict stops.
   For a chapter whose verdict is "default unless…", the tree is three questions and
   the default at the bottom. Every node's words are the ledger's or the forks' words.
4. RESULT: the verdict in a 1.5px-ruled box with a 20px condensed label.
5. Prose in two 314px columns, Plex Sans 10.5/15, split across the two pages.
6. Page 2: the PARTS LIST (ledger with colour swatches, call in mono), photographs
   with NUMBERED CALLOUTS that point at what the ledger names (the nave, the mosaic
   terrace, the city view), TROUBLESHOOTING (the forks as symptom → action) and
   CAUTION (the volatile note, red-ruled, with the ◆ mark).
7. On a map chapter the map's dots take the option colours and the parts list sits
   beside the map as its key.

**Type.** Barlow Condensed (display) · IBM Plex Sans (text) · IBM Plex Mono (labels).
**Colour.** Paper #F7F7F4, ink, and the four option colours #0E6390 · #E0A828 ·
#A23520 · #5B6B66.

**He refuses.** A colour that does not mean an option; a photograph without a
callout; a verdict that is not a box labelled RESULT; a tree node with words the
text does not contain.

**Where he is weakest.** The tree's node sub-lines are 7.5px mono — under the printed
floor; a release would need the tree one third taller. Four option colours cap the
ledger at four rows. The manual register can read as cold on an essay chapter.

**Pages per decision.** 2. **Specimen.** `build/models/m7-manuel/`,
`atelier-visions-2026-10-24/Barcelona-vision-7-manuel.pdf`.
