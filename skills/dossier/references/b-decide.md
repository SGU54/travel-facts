# Stage B — The decisions

The decisions ARE the product — but ONLY if they clear the bar in `references/model.md`.
Read that first if you haven't. A decision earns its place only when it lands in the
bottom-right cell: **NON-OBVIOUS** to a diligent amateur (they read the blogs and Reddit and
still wouldn't know it) **AND HIGH-STAKES** (getting it wrong costs real money, a day, or
the trip). A true, clean, sourced decision that fails either test is what made the first
cold build forgettable. Before writing any decision, apply the test:

- **Is it non-obvious?** If a single free article in the corpus already states it flatly,
  it's obvious — the free web has it. The paid value is the SYNTHESIS across articles that no
  one article makes. Cut or demote the obvious ones.
- **Is it high-stakes?** Name what believing the naive model costs. If the honest answer is
  "not much," it's trivia — cut it.
- **What's the naive model?** The default plan a *sharp* first-timer actually arrives with —
  mined from the corpus's own "many visitors think / common mistake" material, NOT invented.
  A strawman nobody believes is worse than no naive model. If a sharp friend wouldn't
  actually hold the belief, you're strawmanning — fix it.

The single sharpest decision is your **free hook** (model.md) — usually the one that follows
from the organising fact. Identify it; it sells the rest.

## What makes a decision (not a chapter)

A decision is a question the reader is **already Googling**, answered with **visible
arithmetic** and a verdict that **can be disagreed with**. Rome's thirteen:

```
Base      Where should you actually stay?
Arrival   Train, taxi, or transfer from the airport?
Transit   Do you need transit tickets at all?
Tickets   The city pass, or pay as you go?
Booking   What must be booked in advance — and how far?
Money     Cards or cash — and the one question that costs you money?
Time      Three days or four — what does the fourth buy?
Season    When should you go — and what does it cost you?
Eating    How do you avoid eating badly in a city this good at food?
Risk      How worried should you be?
Flights   Nonstop or connection — does the flight decide day one?
Tickets   Arena floor, underground, or the standard ticket?
Evening   Is aperitivo dinner, or a prelude to it?
```

**Decisions do not transfer between destinations.** "Roma Pass or not" has no Lisbon
analogue. Each project needs its own few hours of real analysis — that's the per-site cost
and it's why this is defensible.

## The shape

```python
DECISION = {
 "n":"01", "cat":"Base",
 "q":"Where should you actually stay?",
 # cols is a LIST, one entry per cell, and len(cols) must equal len(row) for
 # every row. It was a free string ("WALK · PRICE") and nothing tied it to the
 # cells: Rome p12 shipped the header "WALK TO CORE / CHARACTER / PRICE" over
 # two-cell rows, so "WALK TO CORE" sat above the character descriptions, the
 # walk minutes sat under "CHARACTER · PRICE", and there was no price on the
 # page at all. Three headers, two columns, on the book's flagship decision.
 "cols":["Area and character", "Walk to core"],
 "units":["", "minutes on foot"],  # the unit belongs in the header, not the cell
 "lede":"...",                    # the reframe: why the obvious answer is wrong
 "table_title":"The trade-off, scored · first-time American, 3 days",
 "rows":[("option — what it is <span class='mk est'>●</span>","13")],

 # ── the comparison contract — fill this BEFORE styling anything ──────────
 "compare":{
   "traveller":"first-time American, 3 nights, two adults",
   "alternatives":["Centro Storico","Monti","Trastevere","Prati","Termini"],
   "unit":"minutes on foot, one way, door to core",
   "includes":"walking only",
   "excludes":"transit fare, time waiting",
   "uncertainty":"±4 min by route chosen",
 },

 "verdict":"<strong>The call.</strong> Then the reasoning, 60-90 words.",
 # scope / default / reversal are THREE different things — see "The verdict
 # must be losable" below.
 "scope":"you are choosing a neighbourhood at all",
 "for":["then it's yes → ..."],
 "against":["then it's no → ..."],
 "note":"<span class='mk vol'>◆ VOLATILE</span> what to re-check, and where.",
}
```

## The comparison contract

**A ledger certifies a comparison. It must not certify one that was not made.**
The doctrine promises visible arithmetic; the object above used to require only
prose, rows, a verdict and exceptions — never comparable units, never a
calculation linking the rows to the call. So a well-set table could sit under an
unsupported inference and make it *harder* to notice, not easier.

Before the ledger is styled, every consequential comparison declares its
`compare` block, and then:

1. **One unit per column**, named in the header. Never compare a number against a
   number measured differently.
2. **Same boundaries on both sides.** Rome p27 printed "Ostia beats Pompeii for a
   short trip by eleven hours" — twelve hours *door-to-door for the whole Pompeii
   excursion* minus one hour of *Ostia travel alone*, while its own ledger calls
   Ostia "half a day". The preference may well survive; the eleven hours does not.
3. **Per-person or per-party, stated.** Rome pp15–16 compares a €14 fare, a ~€27
   total and a €55 vehicle under a heading reading "PARTY OF TWO, LUGGAGE". Two
   €14 fares are €28 on their own.
4. **Recompute every headline number from the rows.** If the sentence says a
   figure the table cannot produce, the sentence is wrong.
5. **Risk is not a number you invented.** Where there is no defensible
   probability, compare explicit disruption scenarios and recovery margins
   instead. Turkey p38 asserts an asymmetry between a coach leg and a flight leg
   without a route, an arrival margin or a delayed-coach scenario.
6. **If the comparison does not establish the call, narrow the call.** Withholding
   a conclusion is a legitimate outcome of this stage.

**Rules:**
- **Every ledger gets a column header, and the header is structural.** Reject a
  row whose cell count differs from `len(cols)`; do not pad, do not invent a
  value to fill a column you named. Rome shipped 13 unlabelled number columns
  through ten refinement loops and a full audit before an outside reviewer caught
  it — and then shipped three headers over two columns anyway, because the header
  was still only a string.
- **All openings must differ.** Rome had two decisions opening "This is the most/highest…" —
  self-important, and the template shows. Check them as a set, not one at a time.
- **The verdict is a conclusion, not an essay** — no drop cap on it.
- **Cross-reference** — "the arithmetic is on p.17". The manual feel comes from the network.

## Budget a visual while you choose the decisions

**This is where the rhythm defect is born.** Fourteen decisions written back-to-back become
fourteen identically structured pages, and no later loop can fix it — by then every page is
full. Rome v2 shipped a 15-page text-only run straight through its decisions.

As you pick the decisions, mark which ones **carry a visual**:

| the decision turns on… | it wants |
|---|---|
| a place, a distance, a route | a locator or a distance map |
| a number that moves over time | a strip or a grid (the month bars) |
| a fork inside one object | a section drawing (the Colosseum tiers) |
| a habit at a counter or a door | **a plate** — the photo IS the evidence |
| a rule with a threshold | the ledger alone is fine — leave it clean |

**Target: something visual on every third or fourth decision.** Not decoration — a decision
that can't carry a figure honestly is a decision whose ledger is doing the work, and that's
fine. But three in a row with nothing is a wall.

## The best lede is a scene, not a claim

Rome's booking decision went from *"This is the highest-impact page in this book"* to:

> *"Nearly every ruined morning in Rome starts the same way: an American arrives at a major
> sight expecting to buy a ticket at the door."*

## The verdict must be losable

If the verdict can't be argued with, it isn't a decision — it's a fact, and facts belong in
the essays. The opening contract: *"so you can disagree with us and still come out ahead."*

**Three different things, three different fields.** `for`/`against` collapsed
them, and the collapse is why the books diverge here: some let the reader change
the decision, others merely sort readers into those who need the chapter and
those who do not.

| field | question it answers | not this |
|---|---|---|
| `scope` | is this decision yours at all? | Turkey p28's "you have no intention of driving. There is no middle case" is a scope exclusion dressed as a reversal |
| verdict | what we call, and why | — |
| `for` / `against` | **what changed fact flips the call, and to what** | Rome p24 files "you're tempted to pre-buy euros" under OVERRULE IT IF, then gives that reader the original advice — so nothing was overruled |

**Every reversal names the alternative action and the changed assumption.** "When
ours is wrong for you" and "when the other call is right" describe the *same*
side; if both boxes lean one way, one of them is decoration.

**A rule with no real alternative is not a decision.** Greece p31's "Have a sunset
plan, not a sunset hope" is advice almost nobody could rationally oppose. Ship it
as a rule or a checklist; manufacturing a losable decision around it wastes the
device's credibility for the decisions that are genuinely contested.

**An acknowledged preference must be allowed to reach the verdict.** Greece p20's
ledger recognises Mykonos for nightlife and the call still concludes "Two
headliners is the expensive way to be disappointed twice." That reader was seen
and then overruled without a route out.

**Test it, don't just declare it.** Apply each printed exception yourself and
check that the verdict, the figure and the carry card all change consistently.
Presence of the fields is mechanical and `audit-layout.py` can see it; validity
is an editorial read and no script substitutes.
