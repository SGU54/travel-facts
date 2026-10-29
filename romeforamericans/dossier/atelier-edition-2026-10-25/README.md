# Rome, Solved. — the whole book in Clàudia Ferrer's hand (2026-10-25)

The owner chose L'Édition for Rome after the five-hand sample. This is the complete
recompose of the shipped 64-page edition: every chapter, the same words, the same
photographs, the same figures, in her vocabulary and La Tavola's palette.

| file | what |
|---|---|
| `Rome-Solved-edition.pdf` | the Book, 70 pages, with bookmarks, locked (read, print and copy only) |
| `Rome-FieldSheet-edition.pdf` | the dated annex, one sheet, same hand, locked |
| `contact-sheet.png` | all 70 pages in a row |
| `contact-sheet-shipped-64pp-for-comparison.png` | the shipped La Tavola edition, for the arm's-length look |
| `eye/figures/figN-pNN.png` | every figure captured large (220 dpi), for the figure check by eye |
| `figure-text.json` | the measured result of the "figure text whole" rule, per label |
| `pages.json` | the page map (every element's box per page) |

**How the book is built in this hand.** A chapter opens on its photograph, in colour, to
the trim; under it the section label, the title in Fraunces, the standfirst in
Newsreader italic, and for a decision IN SHORT — the call's first sentence and its
reasoning — in the right column. The body runs in two columns of Newsreader with a
Fraunces drop cap on the lede; the ledger sits in a tinted sidebar inside the flow; the
figures run at the full measure with a bold-lead caption; the forks are italic
questions; the volatile note is a ruled footer line; the chapter's second photograph
closes it, sized to fill the last page. The service pages — contents, the checklist,
the stay and day-trip cards, the failure tiers, the wallet card, decide-these-first,
the Field Sheet — keep the same faces and the tint, ruled rather than boxed.

**Where the words come from.** No source for the shipped edition exists on this
machine, so the book was read back from its own PDF: roles from its typographic
contract, photographs by page, every vector figure converted to SVG with its paths and
its labels at their printed positions. Nothing was rewritten.

**Figure text whole.** Every figure label is the book's, set in DM Sans on a paper halo,
measured at render against its frame, the page body, the other labels and every
stroked line: no label is cut or crossed. Thirteen lines pass under a haloed label
(gridlines under a bar's value, the metro line under TERMINI) — hidden by the halo,
listed in `figure-text.json` for the Eye. The Pantheon label of FIG. 3 was moved whole
off the walk line; TERMINI sits inside its frame.

**Two-column pagination.** Paged.js cannot paginate CSS multicol, so the two-column body
is packed by the maquettiste before rendering (`pack-edition.py`): every paragraph is
measured once at column width, lines pour into column 1, column 2, next page; a
paragraph splits only at a line boundary; a full-measure item balances the columns
above it. Hyphenation is off in this hand.

**Gates.** The six dossier gates are green on this build (furniture, book, layout,
ai-smell, claims, depth), with the opener pages declared as plates in `_fullsheet.json`
and the layout gate taught that the page after an opener plate carries the title only
as its running head. Green is production, not design: nothing is released until the
owner's Eye.

Sources: `dossier/build-v2/extract-rome.py`, `compose-edition.py`, `pack-edition.py`,
`render-edition.py`; the director's file is
`~/.claude/skills/atelier/references/directors/claudia-ferrer-edition.md`; the rule is in
`~/.claude/skills/atelier/references/gates.md`, "Figure text whole".

## Owner's review, 2026-10-25 — three defects, fixed

1. **Lost drop caps** ("ix weeks" for "Six weeks", p4, p6 and others). The shipped book
   sets each chapter's initial as a separate 39px glyph; the extractor now rejoins it to
   the first paragraph on its page, and a paragraph the shipped book broke across two
   pages is rejoined too. Every paragraph now starts whole (checked by script).
2. **Photographs repeated or wrong.** Two causes: a chapter that ended short was closed
   on a detail of its own opening frame (rule removed — a chapter closes only on a second
   frame it actually has); and on pages carrying two photographs the files were matched
   to their places in the wrong order (now matched by position on the page).
3. **Pages deletable in a viewer.** Both PDFs are now saved with AES-256 encryption, an
   empty reader password and an owner password kept in the build (`_pdf-owner-password.txt`):
   reading, printing and copying text stay allowed; changing, assembling or deleting
   pages does not. `lock-pdf.py` does it last, after the bookmarks. Locked copies of the
   Barcelona release were made too (`…-locked.pdf` beside the originals).

Also fixed on the way: the two-column packer assumed paragraph margins the browser did
not apply (text overflowed its columns); column paragraphs now carry the margins the
packer measured. Six gates green on the 70-page build.

## Owner's review, 2026-10-25 (second look) — photographs and an audit

Asked by the owner: two photographs. Found by the audit that followed: the ledgers, the
wallet card and two more photographs. All fixed; text changed on ten pages only (13, 17,
19, 22, 25, 27, 30, 32, 35, 63), every chapter starts where it did, six gates green.

1. **Decision 07 (p29) opened on SIM cards** — inherited from the shipped book; the
   chapter is cards or cash. Now the card reader (the site's `cash-cards-tipping-rome` hero);
   the wallet card, which had that frame, now closes on coffee and coins (`tipping-in-italy`).
2. **Termini (p20) had white bands** baked into the file itself; trimmed (`img/termini-trim.jpeg`).
3. **Every decision ledger was misaligned.** The extractor tied a value set a hair above its
   label to the previous row, and a label the shipped book wrapped in its narrow column
   became one row per line ("mostly on foot", "(Decision", "01) ●"). Verdicts sat beside the
   wrong option in d02–d09 (e.g. d05 put "no line to skip" on St Peter's, not the Borghese).
   `extract-rome.py` now collects, groups labels up to their mark, and pairs each value to
   the nearest row; checked row by row against the shipped PDF. d01's heads named three
   columns over two; now BASE · CHARACTER / WALK TO CORE.
4. **The wallet card table** shifted every answer after "Must-book, weeks / ahead?" by one
   row; now paired by position.
5. **Two wrong-city photographs inherited from the shipped book**: Decision 09 (Ostia vs
   Pompeii) opened on Florence → Ostia Antica; "Where to stay, assessed" opened on a
   Bangkok hostel → Rome's rooftops (both the site's own heroes).

All swaps live in `compose-edition.py` (`PHOTO_SWAP`); source images untouched. The
previous PDF is in `_previous-2026-10-25-0227/`.
