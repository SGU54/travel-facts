# Barcelona, Without the Traps. — the whole book in Marta Serra's hand (2026-10-24)

The owner chose L'Affiche (Marta Serra) for Barcelona. This is the complete recompose:
every chapter, the same words as the 2026-10-20 release and model 2, in her vocabulary.

| file | what |
|---|---|
| `Barcelona-Without-the-Traps-affiche.pdf` | the Book, 68 pages, with bookmarks |
| `Barcelona-FieldSheet-affiche.pdf` | the dated annex, one sheet, same hand |
| `contact-sheet.png` | all 68 pages in a row |
| `contact-sheet-model-2-for-comparison.png` | model 2 (L'Entrada, 49 pages), for the arm's-length look |
| `fieldsheet-contact.png` | the sheet |
| `pages.json` | the page map the maquettiste measured (every element's box per page) |

**How the book is built in this hand.** Decisions: a red or gold poster (the call as a
number or a word — EIXAMPLE, HOTEL, 4, 3, 2+1, MONTSERRAT, 20:30), a text page (one
340px column, the ledger as a stack, the forks), a photograph page (the last paragraph
and the volatile note under the frame); map chapters give the map a page with the
ledger as a ribbon. Essays: a paper poster (the standfirst as thesis, one phrase in
red, the briefed pull at the foot), a text page with the briefed read-with and pulls
floated right, a photograph page. Tools open on a poster that is the tool: the plan's
five days, the seven calls with page numbers, the three tiers of failure. The wallet
card is the card. Contents is a paper page with the decisions' numbers in red.

**Measured.** No page under 60 % full outside the posters and photograph pages. Cross-
reference page numbers resolved after pagination (26 of 26). One photograph per
chapter, none repeated.

**Gates.** The six dossier release gates are green on this build (furniture, book,
layout, ai-smell, claims, depth), after being re-keyed to the hand: the renderer
declares its full-sheet pages in `_fullsheet.json` (posters and photograph pages carry
no furniture, like the cover) and the layout and claims scripts learned the hand's
class names. Green is production, not design: the owner's Eye has not happened, and
nothing is released. Variable fonts embed as Type3 (no family name) — static Archivo
instances before shipping.

Sources: `dossier/build/compose-affiche.py`, `render-affiche.py`, `add-outline.py`;
the director's file is `~/.claude/skills/atelier/references/directors/marta-serra-affiche.md`;
the poster words are in `build/briefs.md`, "The posters"; the gate contract is in
`dossier/references/g-audit.md`, "Full-sheet plates".

## The Eye — owner, 2026-10-24 evening

**Validated as composed (68 pages).** Claude's arm's-length note raised the page count
(≈ 21 posters + ≈ 16 full-page photographs) and proposed trimming to ≈ 55; the owner
chose to keep the book exactly as it is. Only remaining step before release: static
Archivo instances instead of the variable font (Type3 embedding).

**Done 2026-10-24, late (the one remaining step).** Sixteen static Archivo instances
were cut from the variable font with fontTools at exactly the weight × width × style
coordinates the book uses (`build/models/fonts/archivo-static/`), and the book was
re-rendered on them. The PDF now embeds named TrueType faces (Archivo-w400-wd100,
…-w800-wd118, …) and Noto Sans Symbols 2 for the marks; no Type3, no system fallback
(fssplit's "separate sheet" label had been falling back to Courier). The six gates are
green again. Page by page, every element's box is identical to the validated render
(0 of 68 pages moved); the only visible difference is that a handful of paragraphs
hyphenate one line differently, because a static instance rounds its advance widths
slightly differently from the variable font. The Field Sheet is one sheet, same faces.
