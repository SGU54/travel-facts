# Art-direction briefs — Barcelona, Without the Traps. (pilot, 2026-10-24)

Dialect: L'Entrada — the admission ticket (DESIGN-NOTES.md). Grammar: the Atelier's
6-column grid. Machine form: `briefs.json` (what compose.py reads). Baseline to beat:
the 2026-10-20 release, 45pp, one recipe per page.

SEQUENCE  cover · B D · B E · F · B D · B E · B D · B D · B D D · A C ×7 · B E · B D · B E · B E E · E · B D · B · E E · E

Reading it aloud: the front half alternates essay openers with working or instrument
pages; the seven decisions run A → C each (opener with the ticket, then a plate or
figure page); the back half is instrument-heavy by nature (horizons, plan, failure
modes, wallet, before-you-book) and B pages break it up. No letter three times
running except D.

## The seven decisions (A → C)

| id | book № | title | hero | stub | decisive row | page C opens with | inset | pull | stamp |
|---|---|---|---|---|---|---|---|---|---|
| d01 | 01 | Where to Base | figure (neighbourhood map) | EIXAMPLE | El Born (atmosphere) | the map | band A03 | "There are no bad areas on this list." | — |
| d02 | 02 | The Apartment Question | band h-d02 | HUTB | valid HUTB only | the bleed | closer p-d02 | "It is law on a countdown." | Nov 2028 · Phase-out |
| d03 | 03 | The Money-Trap Web | figure (the trap web) | 4 | none — four equal gates | the figure | band h-d03 | "Your own bank will almost always do better." | Rose 1 Apr 2026 |
| d05 | 04 | Sequencing the Days | band h-d05 | 3 | Sagrada → morning | the bleed | closer p-d05 | "wedged into a morning it becomes a commute with a view" | — |
| d06 | 05 | The Gaudí Fork | band A04 | 2+1 | one house | the bleed | closer p-d06 | "Two is a schedule. Four is a timetable" | 2026 · Centenary year |
| d07 | 06 | Which Day Trip | figure (day-trip map) | MONTSERRAT | Montserrat | the map | band A05 | "Montserrat leads because it is the least substitutable." | — |
| d08 | 07 | How Not to Eat Like a Tourist | band h-d08 | MENÚ | menú del día | the bleed | closer A06 | "Eating late here is not an affectation." | See the Field Sheet |

Every decision: page A = eyebrow · H1 · standfirst with the chapter number as
counterweight → the verdict ticket (call + decisive exception) → the ledger instrument
→ the first paragraph with the margin carrying READ WITH and the marks key. Page C =
the hero (bleed band or figure) → the reasoning on four columns with the inset and the
pull in the margin → the forks → the volatile row with the stamp → the closer where kept.

## The essays

| id | title | archetype | hero | band → | closer | pull / margin |
|---|---|---|---|---|---|---|
| contract | The Contract | B D | pull "A guide that refuses to commit…" | inset ¶0 | keep | — |
| howto | How to Read This | B E | half-band | — | keep | marks key is the instrument |
| contents | Contents | F | the ticket frame (CSS) | — | — | — |
| ground | The Ground | B D | half-band A02 | — | keep | pull ¶1 "The city does not need to hide anything…"; read-with d03; marks |
| fly | Before You Fly | B E | number 2 "bookings that truly bind" | inset ¶0 | keep | marks |
| dayzero | Day Zero | B D | number 6 "hours" | inset ¶0 | keep | pull "Resist the timed sight."; read-with d03 |
| timing | Timing | B D | figure (the year) | inset ¶1 | keep | read-with horizons |
| setpieces | The Set Pieces | B D D | half-band | — | keep | pull "A booked ticket is not the same as a solved visit."; read-with d06; marks |
| horizons | The Horizons | B E | figure | inset ¶0 | keep | — |
| risk | How Worried Should You Be? | B D | number 4 "named places" | inset ¶0 | keep | pull "Anything sudden…is the tell"; marks |
| plan | The Plan | B E | figure (the week) | inset ¶0 | keep | — |
| fail | Failure Modes | B E E | figure (consequence) | inset ¶0 | keep | — |
| wallet | The Wallet Card | E | half-band; the card as a ticket | — | — | — |
| back | What This Won't Tell You | B D | number 4 "things this book refuses to do" | inset ¶0 | — | — |
| then | Barcelona, Then | B | half-band A07 | — | — | — |
| beforeyoubook | Decide these first | E E | half-band | — | — | — |
| fs | Field Sheet | E | unchanged | — | — | — |

## Decisions the maquettiste wrote back (2026-10-24, renders 1–4)

- **Every decision: page A = opener + ticket + ledger, ALL prose after the hero.** The
  briefs asked for the first paragraph on page A (the specimen's look). In flow, a
  paragraph or a margin wrapper that missed page A by a few lines sat alone on a sheet
  before the bleed — three stub pages in render 1, two in render 3. Nothing the
  estimator could predict; moving the prose after the hero removes the failure class.
  Cost: page A fills ~70–80% and closes on the ledger. Keep this until the compositor
  can measure page A itself.
- **One `.mg` wrapper per paragraph slot.** Two consecutive margin items opened a row
  with an empty column 1 (engine.md §1).
- **d01 / d07: the photograph is a closer (`photo wide`), not a band** — re-briefed
  `inset: closer`. The band regex in the summary had misread them.
- **Marks glyphs**: Noto Sans Symbols 2 on every `.mk` context; the TOC's bare ◆ and the
  sheet cells are wrapped at compose time.
- **Sequence string**: wallet is B E, before-you-book is B E — not E E E.
- **Pairing by floats, not grid rows** (render 5): the inset beside a short paragraph
  stretched the grid row and left air under the prose. Floats fixed it (engine.md §1).
- **`.vol` class clash** (render 6): the volatile row's class matched the book's own
  `.mk.vol` mark, so every ◆ in running text rendered as a flex block on its own line
  (visible in d03's ledger). Renamed `.volrow`.
- **Three closers dropped** (dayzero, setpieces, plan): the compositor filled each onto a
  sheet of its own with zero words — a photograph with no job. The chapters now close
  on their prose and the endmark.
- **Prose measure**: 13px / 20px on 426.7px (≈ 75 characters). Pages 44 → ~57; the
  cost of the margin, as the doctrine says. Not recovered by shrinking type.

## Model 2 (2026-10-24) — what changed after the owner's look at model 1

Owner's verdict on model 1: pages 22 and 28 carried only the previous chapter's
volatile row; page 11 ran prose beside an empty margin with a four-column plate;
"15–20 % of the expected level". Model 2 adds the measured loop (atelier-loop.py):
a reserve of pull sentences per chapter, the closeblock, the closing-plate lever, the
first paragraph back on page A verified by measurement, and plates on prose pages at
six columns. Iteration log: `_loop-1.log`; levers chosen: `levers.json`.

## Eye
(one line per chapter after the owner's look: `eye: pass <date>` or `eye: redo — <what>`)

## The posters — Marta Serra · L'Affiche (owner's director for this book, 2026-10-24)

The decision posters for the recompose (essays and tools: see `models/m5b-affiche-essays/`).
Rule for this book: Marta Serra's hand only — no element from another director's vocabulary
(no §-numbers, no tinted sidebar, no tiles, no option colours), whatever a page seems to need.

| id | poster | gloss (one line, from the verdict) |
|---|---|---|
| d01 | EIXAMPLE | First trip, no special agenda — and it isn't close. |
| d02 | HOTEL | Or an apart-hotel. The apartment only with a HUTB number. |
| d03 | 4 | Four gates, four moves: bed tax, airport ticket both ways, euros, a bank machine. |
| d05 | 3 | Three anchors. The rest floats. Arrival day holds nothing timed. |
| d06 | 2+1 | Two ticketed Gaudí sites. One house. The rest from the street. |
| d07 | MONTSERRAT | It out-memories the city, and has no substitute within reach. |
| d08 | 20:30 | Dinner on Spanish time — the rule that puts you in the right rooms. |

d08 decided 2026-10-24 (owner delegated): **20:30** over MENÚ DEL DÍA — the manuscript says
the clock "quietly determines the other three"; the menú stays the text page's lead rule.

## The Affiche recompose (2026-10-24) — what the maquettiste did

Whole book composed in Marta Serra's hand: `compose-affiche.py` → `render-affiche.py`
(→ `dossier.pdf` 68 pp + `fieldsheet.pdf` 1 sheet, page map `_pages-affiche.json`,
pages in `_affiche/`). Package: `dossier/atelier-affiche-2026-10-24/`.
Levers pulled, by chapter: fly `lists2 + tail2` · timing `tail2` · setpieces
`band_before_h2=2` · horizons `tail2` · risk `band_before_h2=3` · plan = poster, text
(intro + three rules + band), day sheet, photo page with "Substituting" · fail = tiers
poster, two-column list, photo page · d03 = photograph decision (timeline dropped) ·
d07 = map, text with the band at 186px · beforeyoubook = seven-calls poster, questions
+ fallbacks, shapes + band · contents = paper page.
Cross-reference page numbers are resolved after pagination (Paged.js's target-counter
never inserted its rule here). Gates: ai-smell PASS, depth PASS; furniture / book /
layout / claims FAIL because they key on L'Entrada's classes — to re-key before release.
Pages under 60 %: none (p67 before-you-book was 56 % before the shapes moved).
