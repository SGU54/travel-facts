# Stage 1c — The opportunity gate (run BEFORE any article is written)

The article list says what a destination *should* cover. This gate says what this domain can
actually **win**. It runs on `article-list.json` after the taxonomy and vein derivations, and
before Stage 2. Nothing gets written until every row carries a verdict.

Every number in this file was measured on the fleet's own GSC data (6 sites, 449 pages with
impressions, 28-day window, Sept 2026). Nothing here is imported doctrine.

---

## The finding this gate exists for

The fleet's hit rate is already good — the Turkey batches 16-21 put **16 of 26 visible pages
in the top 10 (62 %)**. The problem is that those wins are worthless: across all 133 fleet
pages ranking ≤20, the **median page sees 6 impressions a month**. Only 8 pages in the whole
fleet exceed 100.

The cause is an inverse relationship between volume and rankability at this authority level:

| Page's monthly impressions | pages | median position | % in top 20 |
|---|---|---|---|
| 0–5 | 179 | 36.0 | 36 % |
| 5–20 | 94 | 32.2 | 37 % |
| 20–50 | 66 | 48.6 | 32 % |
| 50–100 | 37 | 62.6 | 11 % |
| 100–300 | 66 | 62.0 | 12 % |
| 300+ | 7 | 72.5 | **0 %** |

**Do not read this as "aim low."** Expected value per published article, hit rate × average
impressions of the wins:

| Target | hit rate | avg. impressions of wins | **expected impressions per article** |
|---|---|---|---|
| tiny queries (<20/mo) | 37 % | 5 | **1.9** |
| medium (20–100) | 24 % | 37 | **9.1** |
| real volume (100–300) | 11 % | 178 | **19.6** |

Chasing volume is **10× better per article written**, even though most attempts fail. A gate
that maximises hit rate optimises the metric the fleet is already best at and makes the real
problem worse.

**So: volume is the target variable, winnability is the filter. Never the reverse.**

Above ~300 monthly impressions, the fleet has never ranked anything in the top 20. Treat
300 as a ceiling, not a goal.

---

## Keep these evidence types distinct (2026-10-11 addition)

Before touching the tables above, know what each number in them actually is. Conflating
these is the single most common way this gate lies to you:

| Evidence | What it establishes | What it does NOT establish |
|---|---|---|
| GSC impressions | Observed appearances of this site's links under the selected filters | Total searches for the query, or demand the site has not yet reached |
| GSC average position | Impression-weighted position within the chosen report | A fixed rank for every user, or for every query the page could answer |
| Keyword-tool estimate | That tool's own estimate, for its market/period/method | Guaranteed Google impressions, clicks or sales |
| Search results inspected now | The observed results, intent and formats for that query today | A universal SERP, or proof a future page will displace those results |
| Guide/affiliate clicks | Movement to a linked destination | A purchase, profit, or causal uplift from the placement |
| Stripe transaction data | Recorded purchases, refunds and credited revenue | Which article caused the purchase, unless attribution actually connects them |

The tables below (R1 back-test, the impressions/position bands, the expected-impressions
figures) are real measured statistics on the fleet's own GSC export — keep using them. What
they are NOT is a calibrated probability for any single future candidate; see the note on
`p_top20` under "The prediction record."

---

## The unit is the QUERY, not the topic

`turkey-atm-withdrawal-real-cost` sits at position 8. `atm-fees-thailand-real-cost` sits at
52. Same topic, same audience, same engine. They are not competing for the same queries: the
Turkey page captured a small easy one (15 impressions), the Thailand page a bigger contested
one (104).

A topic label hides the whole battle. Score queries.

---

## Rule R1 — commodity nouns (hard reject)

Back-tested on the 73 fleet pages with ≥100 impressions: **98 % precision** (42 rejected, 41
genuinely losing, 1 false reject). It lifts the hit rate on what survives from **11 % to
24 %**, and costs nothing — it reads the working title alone.

Reject any candidate whose title contains, about a place:

> hotel · hotels · beach · beaches · villa · resort · rooftop · where to stay ·
> things to do · best … · top … · restaurants · markets · neighbourhoods · museums ·
> itinerary · N days / N weeks · airport to city · visa · is X safe · first-timers

These SERPs are owned — by Booking, TripAdvisor, Lonely Planet, government portals, or
Google's own modules. The fleet has 43 such pages carrying 10 800 impressions and producing
approximately zero clicks. They are not near-misses; the median sits around position 70.

**The reject is on the title, not the subject.** A traveller does need to know about
accommodation areas and entry rules. Cover them from an angle R1 does not reject, or accept
that the page is structural and will not rank — and mark it `structural: true` so it never
pollutes the hit-rate measurement.

---

## Rule R2 — place-versus-place comparisons (hard reject)

A comparison shape is not by itself a winner. What is compared decides it:

- **Options and procedures win.** `fast-vs-slow-ferries-greece` → position 8.8 ·
  `taxis-uber-car-barcelona` → 9.3 · `colosseum-vs-vatican-where-to-stay` → 13.3.
- **Places lose.** `santorini-vs-mykonos` → 85.4 · `naxos-vs-paros` → 76.8 ·
  `krabi-vs-phuket` → 58.2 · `casa-batllo-vs-casa-mila` → 61.3.

Comparing two destinations puts the page against every travel publisher alive. Comparing two
ways of doing one thing puts it against nobody.

---

## Rule R3 — canonical owner (flag, never auto-reject)

If a single organisation is the obvious authority on the query — a monument's own ticketing
site, a rail operator, an airline, a government department — the SERP is usually theirs.
Fleet evidence: `leonardo-express-fiumicino-trains` 48.5 · `colosseum-underground` 66.6 ·
`hagia-sophia-blue-mosque` 66.0 · `flights-from-us-to-greece` 35.9.

But applying this as a hard reject kills real winners — it would have rejected
`camp-nou-tour-guide` (8.4) and `grab-in-thailand-guide` (17.4). So R3 routes to
**INVESTIGATE**, never to REJECT. The question to answer by hand: *does the canonical owner
actually answer the traveller's question, or only sell the ticket?* If it only sells, the
question is open.

---

## Verdicts

Every row in `article-list.json` gets exactly one:

- **REJECT** — R1 or R2 fires. Record the rule and the phrase that triggered it. Not written.
- **INVESTIGATE** — R3 fires, or estimated volume is unknown. Needs one SERP look before a
  decision. Batch these; do not resolve them one at a time.
- **PRODUCE** — survives R1 and R2, estimated volume between 50 and 300 a month.
- **STRUCTURAL** — needed for the site to make sense (entry rules, money, getting around)
  but expected to lose. Written, excluded from hit-rate measurement.

A verdict without a written reason is not a verdict. The gate must be able to say *why* it
refused an article, or it is a score, not a decision.

---

## Where the volume estimate comes from

In descending order of usefulness, all free:

1. **The fleet's own GSC query exports.** Every query the site already appears on has a real
   impression count and a real position. This is the only source where volume and winnability
   are measured together, on this domain. Mine it before anything else.
2. **Bing Webmaster Tools** — free, gives actual search-volume figures, no ad account needed.
3. **Google Keyword Planner** — ranges only without an active campaign, still enough to sort.
4. **Autocomplete and People-Also-Ask** — for shape and phrasing, not for volume.

A paid SERP API (DataForSEO and similar bill fractions of a cent per query) is worth adding
only once the gate has proven it predicts. Five hundred candidates cost a few euros — the
constraint is not budget, it is knowing what to ask for.

---

## The prediction record

Before the batch is written, append one row per candidate to
`travel-facts/<project>/predictions.json`:

```json
{
  "slug": "...", "title": "...", "decided_on": "2026-09-04",
  "volume_estimate": 180, "volume_source": "bing-wmt",
  "verdict": "PRODUCE",
  "rules_fired": [],
  "confidence": "medium — no commodity noun, procedure not place, no canonical owner",
  "risk": "query may be seasonal"
}
```

**No invented numeric probability field (`p_top20`, `p_top10`, ...).** A single-candidate
"35% chance of top 20" has no calibration evidence behind it — it is qualitative confidence
wearing a number's clothes, and it will be read as more certain than it is once it is in a
JSON file (2026-10-11 fix — see SKILL-CHANGES.md). Write the confidence qualitatively, with
the reason, instead. The fleet-level back-tested rates above (R1's 98% precision, the
hit-rate-by-band table) ARE real statistics and stay numeric; what changes is only the
per-candidate prediction row, which was never actually measuring the same thing.

**These rows are never rewritten after publication.** A prediction edited once the result is
known is not a prediction. Measure at day 14, 30, 60 and 90: indexed, impressions, query
count, weighted position, best position, top-50/20/10/5, clicks.

The first experiment's success criterion is **not traffic**. It is whether this gate's
verdicts separate what ranks from what does not. A page predicted a confident PRODUCE that
lands at 75 is the most valuable observation available — it names something the rules do
not see.

---

## What this gate does not know

It has never been run prospectively. R1's 98 % precision is retrospective, on pages already
published and already ranked; the SERPs were not captured at publication time, so the rules
describe an outcome, not a prediction. Everything above is a hypothesis with a back-test,
which is more than the article list had before and less than a model.

Twenty candidates through the gate, predictions filed, then measured, is what turns it into
knowledge. Until then it is a well-founded guess.
