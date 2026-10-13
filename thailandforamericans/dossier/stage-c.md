# Stage C — the eight decisions, written and set

**State: 21 pages rendered.** Cover · key page · eight decisions. No figures, no
photographs, no essays, no Field Sheet yet.

| # | decision | pages | ledger unit | decisive row |
|---|---|---|---|---|
| — | How to read this (key page) | 2 | the four provenance marks | — |
| 01 | RIDE — what may you drive | 3–4 | what each option *requires and excludes* — **no price column** | Scooter (the endorsement) |
| 02 | SEQUENCE — how many islands fit | 5–7 | nights that survive the transfers | Bangkok + one un-serviced island |
| 03 | BASE — which island | 8–10 | FIG. 1, four axes, seven places | none — the *column* is decisive, not a row |
| 04 | TRANSIT — who owns the failure | 11–13 | who rebooks you when a leg fails | separate ticket, the other Bangkok airport |
| 05 | INSURE — what a policy answers | 14–15 | the Thai scenario each coverage answers | direct billing vs reimbursement |
| 06 | CITY — Bangkok, by line | 16–17 | access to a transit line, one instrument for all four | Riverside / Old Town |
| 07 | CULTURE — the door and the elephant | 18–19 | what a venue requires of the animal | the word “sanctuary” |
| 08 | EAT — eating well | 20–21 | what each place is reliably good at | the street stall (turnover) |

Every claim traces to a named corpus article; `src` on each decision records them.
Where the corpus supplies a sentence better than a paraphrase, it is quoted.

## What the writing refused

- **No price column on Decision 01.** Fares are reported ranges that differ by
  island. Rome p12 shipped a ledger certifying a comparison nobody made.
- **No island ranking on Decision 03.** The corpus describes; it does not score.
  FIG. 1 puts the axes side by side and stops.
- **No named insurer, hotel, restaurant, stall or elephant venue** anywhere.
  Decision 07 carries the corpus's own *test* (riding) instead of a list, because
  a filter survives the year between writing and travelling and a list does not.
- **No confident last-flight time from the southern airports.** The corpus says
  it is not reliably documented, and the book says so too.

## Three defects found by looking at the render, not by reasoning about it

1. **The cover did not bleed to the trim.** `height:100%` has no resolved parent
   height under Paged.js, so it fell back to `min-height` and left a paper strip
   down the right edge and along the foot. Fixed by painting the *sheet*
   (`.pagedjs_page:has(.cover)`) — the page box is the only box that is exactly
   the trim size.
2. **The end mark was `◆`, which is also the volatile-value mark** in the
   provenance key, three inches up the same page. A glyph may not mean two things
   in one book. The section now ends with a rule.
3. **The feather pass was inert, and lied in the log.** It matched the literal
   string `class="dec chap"`; these sections are `class="dec"`, so every pass was
   a no-op — and its assertion passed anyway because the word "tight" happens to
   occur in Decision 07's prose ("see-through or very tight"). Rewritten to match
   by id and to raise if the section is not found. With it working, the book went
   22 → 20 pages. **This is the recurring defect class again: something was
   configured, nothing read it, and no error appeared anywhere.**

Two smaller ones: the ledger was splitting into equal thirds under
`table-layout:fixed` (a column of short labels starving two columns of
sentences — column widths are now declared), and `.call` / `.forks` drew rules at
560–600px while the ledger above them drew one at 652px, putting two right edges
on the same page. The rules now span the text column; the *text* inside keeps the
520px reading measure.

## What the tails are telling us

Decisions 02, 03 and 04 each end with a page carrying only the two fork lists and
the note. That is not a defect to tune away — it is where Stage D's figures go:

- **02** — the leg-count diagram: one serviced island vs one un-serviced, drawn
  as legs rather than distance.
- **03** — the line itself, drawn: the seven places on the airstrip/medical axis.
- **04** — the fifty-kilometre gap: BKK → DMK as five steps, not one arrow.

## Next

Stage D (three figures) → essays and Field Sheet → Stage E photographs, sourced
with the contact-sheet artifact method (two candidates per slot, visual picker) →
Stage F full render → Stage G `audit-release.py`.

Page budget: 97 articles × 0.5 ≈ 48pp. Decisions and front matter account for 21.
The balance is figures, essays, plates and the Field Sheet — **written material
and drawn material, not inflated type.** The feather pass is bounded to ±1px of
leading and ±2px of paragraph spacing for exactly that reason; type size never
moves.
