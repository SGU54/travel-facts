# Stages D and E — the figures, the essays, the back matter, the plates

**State: 31 pages rendered, text and drawings complete. Photographs outstanding.**

## The book, in reading order

| pages | what |
|---|---|
| 1 | cover (type only — it is the cover already published on the sales page) |
| 2 | the key page: how to read this, and the four provenance marks |
| 3–4 | **Essay · the calendar** — placed *before* the eight so it can govern them |
| 5–23 | the eight decisions |
| 24–25 | **Essay · money** — the flat ATM fee, and why cadence is a routing decision |
| 26–27 | **Essay · entry** — the fine is capped, the ban is not |
| 28 | **Essay · the north**, handed back |
| 29–30 | what this book refused, and why |
| 31 | the Field Sheet — two cut-out cards, 3.25 × 4.5in |

## The four drawn figures

- **FIG. 2** (D02) — one serviced island is two legs; one un-serviced island is three, each
  separately timetabled, doubled by the return.
- **FIG. 3** (D03) — seven places against four unrelated measurements. The break falls in the
  same column every time. This is the book's whole argument in one drawing.
- **FIG. 4** (D04) — the BKK→DMK gap as five steps, with the road leg drawn to a 0–150 minute
  scale: 45–60 off-peak against 90–150 in traffic.
- **FIG. 5** (calendar essay) — three calendars on one axis. February and March are the north
  at its best and the north at its worst, in the same weeks.

FIG. 1 stays a ledger rather than a drawing: it carries reported values, not a relationship.

## The finding that earned an essay

Nine separate corpus articles say, independently, that the north's burning season runs
roughly February to April. The north's *best* season runs November to February. No beach
calendar mentions the overlap, and a November–December trip that wants Chiang Mai and the
Gulf islands has picked the north's best month and the Gulf's wettest stretch at once.
The previous edition never made this point.

## Defects found by looking, not by reasoning

1. **The `in traffic` bar label was drawn outside the viewBox.** The bar ends at the column
   edge, so a label placed after it was silently clipped. Measured containment means
   computing that, not noticing it afterwards. The scale is now inset by a label column.
2. **Paper on `accent` measures 4.45:1** — under AA for a 12px label reversed out of the bar.
   Changed to `accent_deep` (7.29:1). Measured, not eyeballed.
3. **`· changes the choice` was a CSS `content` string**, so it appeared on an essay ledger
   whose own text says the page contains no choice. The wording is now data per table.
4. **The feather pass lied in its log** — see `stage-c.md`. Fixed there; with figures added,
   the "loosening" it used to report disappears entirely, because the tails now carry drawings.

## Stage E — the plates

`slots.json` defines ten slots: one per decision, one for the calendar essay, one for the
money essay. That is a plate every three pages against `e-image.md`'s one-per-six floor,
the first inside the opening 12%, and five in each half. The cover stays type-only.

Twenty candidates (two per slot) were sourced from Pexels, downloaded, **looked at** as two
contact sheets, and shortlisted. Three firm rejections on the doctrine rules:

- **A07-5** — a BTS train carrying a large cat-food advertisement. Brand signage.
- **A10-4** — an identifiable young man at a row of ATMs. Recognisable face.
- **A08-1** — a shoe rack that is plainly **Japanese**, not Thai. No usable Thai
  shoes-removed frame exists on either library, so slot A08 became *the door itself* and
  the brief was rewritten to say so rather than forcing a wrong-country image.

The picker is published as an artifact: two candidates per slot, each with its argument and
its shot brief, click to choose, and a copyable line of picks at the foot.
Candidates are embedded as data URIs — the artifact CSP blocks every external image host,
so a link list would have rendered as twenty broken frames.

**Next, once the picks are in:** download at full size, `validate-images.py` (portraits and
soft files fail), resize to 1500px, embed, place each plate *with the paragraph it argues
for* — never at the top of a page by default and never ahead of a drawn figure —
write captions that argue, re-render, then Stage G `audit-release.py`.
