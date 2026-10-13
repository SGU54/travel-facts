# Turkey — batch plan for the paid guide

Built from the A2 mine on the 2026-07-27 export (72 published, 61,897 words,
mean 859). Not from a target article count.

---

## Why the count wasn't the problem

Thailand failed the dossier viability check **at 80 articles / 67,306 words** —
almost exactly where Turkey is now, with the same mean article length. The
constraint was never volume. It is that each article resolves its own question
and prescribes, leaving nothing for a book to connect.

Turkey is in that shape, and further along than Thailand was: **five of its
strongest decisions are already made in free articles.**

| dead | killed by |
|---|---|
| Balloon slack | `turkey-itineraries-overview`: *"Always give Cappadocia at least two nights (three is better) so a weather-cancelled balloon morning isn't [wasted]"* — **and the same call is in the free lead-magnet PDF** |
| Lira / DCC | `money-in-turkey`: *"Always pay and withdraw in lira, never the offered dollar conversion"* (×2) |
| Taxi meter | *"Always insist on the meter"* — 3 articles |
| Season | `best-time-to-visit-turkey`: *"The short answer: spring and fall are ideal nearly everywhere"* (13 prescriptive sentences) |
| Where to drive | `renting-car-turkey`: *"avoid driving in Istanbul altogether"* + *"best enjoyed on the open coast road, not in city gridlock"* |

Those are gone. A book that charges for them is charging for the blog.

**So the risk of writing 49 more articles the same way is not that they don't
help — it is that each one that answers its own question kills another
decision.** That happened on Thailand: a retrofit article wrote *"the sensible
answer is fewer, larger withdrawals"* and killed D-money, under a skeleton
whose first rule was don't make the call. `check-noconnect.py` exists because
of it, and no article entered a batch after that without an exit-0.

---

## What is actually open

Measured in dedicated-article words (the metric that stopped lying on
Thailand; floor 3,000). All four are open — no call-making sentence found.

| swamp | now | target | gap |
|---|---|---|---|
| **S-coast** — which base, and the moves between | 2,593 | 3,000+ | small |
| **S-licence** — the licence chain (US licence / IDP / rental desk / insurer) | 1,778 | 3,000+ | medium |
| **S-transit** — internal moves funnel through Istanbul, on separate tickets, against a fixed return | 1,662 | 3,000+ | medium |
| **S-insure** — medical exposure and what a policy excludes | 932 | 3,000+ | **largest** |

`S-licence` is the Thailand D-ride shape exactly: the placement call is spent,
but the licence↔insurance-exclusion chain is stated in halves and never lined
up. `S-insure` is the widest gap and the highest stakes.

## Page target: >40 pages — the calls

Thailand is the only real datapoint: **5 decisions / ~5,500 book words / 23
pages** = 239 words per page, ~1,100 book words per decision.

The instinct is "more decisions." Run the arithmetic and that is wrong:

    7 decisions x 1,100 words (Thailand depth) =  7,700  ->  32 pages
    7 decisions x 1,400 words                  =  9,800  ->  41 pages
    7 decisions x 1,600 words                  = 11,200  ->  47 pages
    6 decisions x 1,600 words                  =  9,600  ->  40 pages

**>40 pages comes from DEPTH PER DECISION, not decision count.** Thailand's
1,100 words per decision was thin because its corpus was thin — the book could
only carry what the articles supported. Seven decisions at 1,400–1,600 clears
40 pages, and a decision worked to 1,600 words (real cost ledger, worked
example, failure-mode set, one figure) is a *better* decision, not a padded
one. Nine shallow decisions would be the padding the model warns about; seven
deep ones are the product.

### CALL 1 — seven swamps, each worked to 1,400–1,600 book words. Target 41–47 pages.

### CALL 2 — S-calendar gets its batch, but runs second.

Batch 16 was S-insure: biggest gap, highest stakes, zero risk of not being a
real decision. It establishes the pattern. Batch 17 is S-calendar, the
speculative one, so failure costs 10 articles and the remaining 39 can be
re-pointed. **And if it dies, six decisions at 1,600 words still hits 40
pages** — the target survives losing it. That is why it is worth the bet.

### CALL 3 — the margin line comes out of the lead-magnet PDF.

*"Leave 3+ hours for the IST connection on separate tickets"* is the sharpest
call S-transit has, and it is currently given away in a free 12-page PDF that
already carries five other "worth knowing" tips. Regenerate without it.

### CALL 4 — the balloon returns as a node, not a decision.

The slack call (*"give Cappadocia two nights"*) is spent, in the corpus AND the
PDF. But what a cancellation actually *costs* is untouched anywhere: whether
the operator refunds or rebooks, whether prepaid activity cover pays, and what
it does to a fixed onward flight. That is S-insure crossed with S-transit — the
balloon becomes the worked example inside two decisions instead of a dead
decision of its own. Turkey's most distinctive hook comes back, sharper.

## The batches — RE-CUT after batch 17 (2026-07-27)

Numbering continues Turkey's own counter (corpus build ended at batch 15).

**Two swamps died, and the shape changed.** S-calendar failed Gate A (0
cross-swamp joins, no option structure). S-regional-season turned out to be
pre-connected all along — eight resolving sentences the first mine missed
because "lean toward late spring", "suits the cultural half" and "you're not
tied to beach season" weren't in the prescriptive regex.

**Five swamps survive**, and each was re-tested against its OWN decision rather
than its topic:

| swamp | now | why it is open |
|---|---|---|
| S-insure | **6,035 DONE** | batch 16 |
| S-transit | 1,662 | the separate-ticket / connection / fixed-return call is made nowhere |
| S-licence | 1,778 | corpus states the licence question in halves and hedges it; never joins it to the insurance condition |
| S-coast | 2,593 | no which-base call anywhere |
| S-east | 852 | access and season stated separately, hedged, never resolved |

### The page consequence

    5 decisions x 1,600 book words  =  8,000  ->  33 pages
    5 decisions x 2,000 book words  = 10,000  ->  42 pages   <- the target

Five decisions cannot reach 40 pages at Thailand's depth. They reach it at
**2,000 book words each** — a chapter with a real cost ledger, a worked example,
a failure-mode set and a figure. That is a harder book to write and a better one
to read than nine thin chapters would have been. It also needs a deeper corpus
per swamp: roughly 6,000-7,000 dedicated words, not 3,000.

### Allocation

| batch | swamp | n | dedicated words: now → target |
|---|---|---|---|
| ~~16~~ | ~~S-insure~~ | 5 | **932 → 6,035 DONE** |
| ~~17~~ | ~~S-calendar~~ | 5 | written, Gate A failed, folded into the corpus |
| 18–19 | **S-transit** | 10 | 1,662 → ~7,000 |
| 20–21 | **S-licence** | 10 | 1,778 → ~7,000 |
| 22–23 | **S-east** | 10 | 852 → ~6,000 |
| 24–25 | **S-coast** | 10 | 2,593 → ~7,500 |

50 articles total, matching the original budget. Corpus ends at ~122 published.

## Hard rules for every article

1. **Report mechanics, never make the call.** The call is the book's.
2. **`check-noconnect.py` exit 0 before import.** No exceptions — this replaced
   my discipline after it failed once.
3. **Facts from `facts.json` only.** A null fact deletes its sentence; it is
   never softened to "sometimes".
4. **No drift-prone value in a heading, title or excerpt** (they can't carry a
   span — the Turkey 150-day error is exactly this).
5. **Panel prompts name the previous failure with numbers.** On Thailand that
   moved deepseek from 24/40 unearned "verified" to 9/30 all officially sourced,
   where the abstract rule had failed.

## Two gates

**Gate A — after batch 17 (S-calendar), the speculative one.** Run it early
precisely because it might not be a real decision. If it fails, re-point
batches 18–25 at the six that are known-open instead of discovering the problem
at the end.

- dedicated words > 3,000 (from 209)
- at least 3 articles carrying a genuine option structure, not a warning
- if either fails: **drop S-calendar, drop to six swamps**, and accept ~34–36
  pages rather than pad

**Gate B — after batch 20, with roughly half the budget spent.**

- `check-noconnect.py` exit 0 on everything written so far
- S-insure and S-transit both > 3,000 dedicated words
- articles joining ≥2 swamp legs: 1–4 (0 = still absent, >4 = re-pre-connected)

If the join count fails, **stop and re-plan** rather than spend the rest.

## One thing to fix outside the batches

The free lead-magnet PDF makes **two** calls the book would want: the balloon
first-morning rule, and *"Leave 3+ hours for the IST connection on separate
tickets"* — which is the S-transit margin call. The PDF is regenerable; the
margin line should come out of the next edition or S-transit ships pre-spent.
