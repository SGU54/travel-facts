# Stage A — Thailand, mined. 2026-09-18

Corpus: `dossier/corpus.json` — the full admin export, **97 articles / 83,533 words**.
83 published + **14 drafts** (12,164w) that were written but never published for
lack of photographs. The previous book used both; this build uses the same set.

## The headline: the shipped book is half-built

`audit-depth.py` against `thailand-covered.pdf` (23pp) and this corpus:

```
✗ pages / article  0.24   (floor 0.40)
✗ words / article  79     (floor 120)
✗ corpus used      9.2%   (floor 11.0%)
THIN — the corpus supports ~48pp; this book is 23.
```

For scale, the same measure on its siblings: Rome 0.52 pp/article, Greece 0.51,
and the fleet model is ≈0.50. Thailand shipped **0.24**. This is not a stale
edition — it is the failure mode `a-mine.md` was written to prevent, and it would
not pass Stage G today.

## Category inventory

| art | words | category |
|---|---|---|
| 9 | 8,069 | health-and-safety *(4 drafts)* |
| 8 | 6,981 | islands-beaches *(1)* |
| 6 | 5,668 | city-transport *(3)* |
| 7 | 5,460 | flights-trains *(4)* |
| 5 | 4,164 | entry-and-visa *(2)* |
| 5 | 4,132 | chiang-mai-north |
| 4 | 3,928 | money-and-costs |
| 4 | 3,331 | stay-islands |
| 4 | 3,324 | itineraries-by-interest |
| 4 | 3,318 | bangkok |
| 3 | 2,928 | ferries-islands |
| 3 | 2,893 | one-week |
| 3 | 2,658 | two-weeks |
| 3 | 2,639 | stay-bangkok |
| 3 | 2,569 | where-to-go |
| 3 | 2,530 | street-food-markets |
| 3 | 2,434 | central-thailand |
| 3 | 2,427 | temples-culture |
| 2 | 1,756 | etiquette-culture |
| 2 | 1,676 | ethical-wildlife |
| 2 | 1,644 | when-to-go |
| 2 | 1,643 | dishes-what-to-order |
| 2 | 1,618 | connectivity |
| 2 | 1,617 | nature-adventure |
| 2 | 1,608 | drinks-nightlife |
| 1 | 884 | stay-north |
| 1 | 824 | beaches-islands |
| 1 | 810 | isan-northeast |

**The 14 drafts are not marginal.** They are concentrated in exactly the veins the
book's spine needs: transit and the islands (distances, no-scooter, Grab coverage,
car rental, BKK↔DMK, flights vs the overnight train, air to the south, baggage
rules), medical (care, evacuation from the islands, what insurance covers) and
entry (refusal/overstay, extension). Four of the nine health-and-safety articles
and four of the seven flights-trains articles are drafts.

## The decision shortlist

| verdict | words | art | vein |
|---|---|---|---|
| **STRONG** | 13,737 | 15 | **RIDE** — scooter, car, Grab: what you may legally drive and are insured for |
| **STRONG** | 11,444 | 13 | **SEQUENCE** — how a week or two actually allocates |
| **STRONG** | 11,136 | 13 | **BASE** — which island, which side, how many |
| VIABLE | 8,388 | 10 | **TRANSIT** — how the legs connect: flights, trains, ferries, two airports |
| VIABLE | 8,069 | 9 | **INSURE** — exposure, evacuation, what a policy answers |
| VIABLE | 5,957 | 7 | **CITY** — Bangkok: where to sleep, how to cross it |
| VIABLE | 5,859 | 7 | **CULTURE** — temples, etiquette, wildlife ethics |
| VIABLE | 5,781 | 7 | **EAT** — ordering, markets, what is worth queueing for |
| THIN | 5,016 | 6 | NORTH — Chiang Mai as a different trip |
| THIN | 4,164 | 5 | ENTRY — visa exemption, extension, refusal, overstay |
| THIN | 3,928 | 4 | MONEY — the fee stack, cash, cards |
| THIN | 1,644 | 2 | SEASON |
| THIN | 1,618 | 2 | CONNECT |

## Two structural errors in the shipped book

**1. It wrote a THIN vein as a decision.** The old book's Decision 04 is ENTRY —
4,164 words, below the 5,500 floor. `a-mine.md`: *"THIN < 5,500w → do NOT write
it; it will pad."*

**2. It never wrote its third-strongest vein.** SEQUENCE carries **11,444 words
across 13 articles** — one-week, two-weeks, itineraries-by-interest, where-to-go —
and the book has no sequencing decision at all. This is the same miss `a-mine.md`
records for Rome ("2 more STRONG veins on a second pass that it had walked past").

Three more VIABLE veins — CITY, CULTURE, EAT, 17,597 words between them — are
likewise unwritten as decisions.

## The plan

**Eight decisions**, in corpus-weight order: RIDE, SEQUENCE, BASE, TRANSIT,
INSURE, CITY, CULTURE, EAT. Drop ENTRY as a decision and fold what it establishes
into the essays and the Field Sheet, where an exemption rule belongs.

Honest estimate: **97 × 0.5 ≈ 48 pages**, i.e. roughly double the shipped book —
reached by writing the unmined veins and drawing the figures the corpus supports,
**not** by padding. `audit-book.py`'s page-shape check fails inflated type and air.

## What this destination CANNOT support — for the back-matter page

- **A ranked list of islands.** The corpus describes them; it does not compare them
  on one ruler, and inventing a score would be exactly the fake certainty the
  model refuses.
- **A Chiang Mai / northern trip.** 5,016 words is a chapter, not a decision. The
  north is named as a separate trip and handed back, explicitly.
- **Current prices.** MONEY is thin at 3,928w and prices belong on the Field Sheet
  regardless.
- **A season calendar.** 1,644 words. Say what the two seasons do and stop.
- **Hotel and restaurant names.** Unchanged fleet-wide.

## Next

Stage A2 (the organising fact) → A3 (the name: *Thailand, Covered.* is already
set and the cover exists) → B (the eight decisions, each under the new comparison
contract in `b-decide.md`) → C → D → **E, which needs photographs from you** → F → G.

Note for Stage E: the 14 drafts were never published *because there were no
photographs*. Stage E requires landscape photographs the user selects. That
constraint has not gone away, and it is the one input this build cannot generate.
