# Batch 12 — second gate (ChatGPT, 2026-10-12)

**Task A: revise (4 actionable). Task B: 1 PASS, 1 at 78 with an exact repair supplied.**

The gate prompt was changed this batch to require the report be split into
**Section 1 — actionable** (contradictions, arithmetic, invented precision, safety/outcome
guarantees) and **Section 2 — the ceiling** (everything not in facts.json, as a compact list
with one example per claim type). The report came back **9,900 characters instead of 42,000**
and every Section 1 item was real and came with its own fix. Keep this prompt shape.

## Section 1 — all four fixed

1. *"The last stretch to Hoi An is a car either way"* contradicted the bus and easy-rider
   options offered later. → "If you take the train, you continue from Da Nang to Hoi An by car."
2. The excerpt counted four versions; the body presents five. → "several".
3. *"ten to twelve hours door to door"* became *"the twelve hours of driving"* later in the
   same article. → "without devoting a full day to an excursion".
4. *"costs nothing"* — an unqualified no-charge assurance about the Citadel's public streets.
   → the cost claim removed.

Plus the prevalence claims the gate listed in Section 2 and that were cheap to drop: "where most
visitors to Da Nang stay", "the three most visited tombs", "the part of the day most visitors
remember", "the stop most people come for", "visitors consistently report... at all of them",
"the best-preserved major building", "the landmark most often photographed".

## Task B

| Article | Tag | TRUST | Result |
|---|---|---|---|
| where-to-stay-hoian-danang | SEED | 78 | FAIL — handoff spanned two sentences |
| hue-to-hoian-how-to-travel | SEED | 90 | **PASS** |

The 78 was not a trust problem: *"Core answer withheld: No. Adjacent question: Yes.
Consequential trade immediately before: No."* It failed only because the adjacent question was
introduced in one sentence and the manual named in a second. The gate's own one-sentence repair
was adopted verbatim.

**Proportionality: PASS** — *"Distinct pitches... They are not the same argument repeated."*
**Dry ground: PASS** on all three.

## Note on the Hai Van tunnel

The gate observed the motorbike exclusion is consistent with the baseline but "is not stated"
in the batch-12 articles. That is correct and deliberate — the hue-to-hoian article points
riders at the pass, not the tunnel, so the exclusion is not load-bearing there. It is stated in
`hai-van-pass-guide` (batch 11).
