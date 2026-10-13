# Stage B — Develop useful decisions

Sections: [Form](#choose-the-right-form) · [Comparisons](#make-comparisons-fair) ·
[Exceptions](#make-exceptions-usable-and-consistent) · [Writing](#write-the-answer-for-the-reader) ·
[Completion](#completion-check)

Read references/model.md and references/evidence-contract.md. Answer real reader
questions with enough evidence and practical detail to choose. A familiar question can
deserve space. Do not invent a naive traveler, a dramatic loss or a false controversy to
make advice appear valuable.

## Choose the right form

Use a decision when reasonable alternatives suit different conditions. Use a rule,
checklist, explanation or itinerary when that form serves the reader better. No section
needs a contrarian verdict, numerical score or comparison table merely to fit a template.

Before drafting a decision, define:

| Element | Required meaning |
|---|---|
| Question and scope | Who needs this choice and under which trip assumptions |
| Alternatives | Real options the reader could reasonably choose |
| Comparison | The criteria, evidence and boundaries that distinguish the options |
| Default | The recommendation for the stated profile, with its reason |
| Default conditions | Conditions under which that recommendation holds |
| Exceptions | A changed condition and the resulting alternative action |
| Execution | How to act, including a consequential eligibility or booking step |
| Uncertainty | Missing evidence, variable input or unresolved conflict |

Link consequential facts and shared rules to their canonical evidence.json entries.
The build's content schema may encode these elements differently; preserve their meanings
in the rendered output. Keep scope separate from an exception: someone who is not renting
a car is outside a car-hire decision, not a counterexample to its recommendation.

## Make comparisons fair

Write the comparison contract before styling the table. Declare the traveler profile,
party size, dates or season, alternatives, units, time boundaries, inclusions, exclusions
and material uncertainty. Use qualitative criteria when numbers would invent precision.

1. **Use the same unit and boundaries.** Compare door-to-door journeys with door-to-door
   journeys, or visit durations with visit durations. Include waiting, transfers and the
   final approach when those affect the result.
2. **State who pays.** Distinguish per-person, per-party, per-vehicle, per-night and per-stay
   amounts. Include children, luggage or mandatory fees when they change the comparison.
3. **Show the calculation when the call depends on it.** Recompute headline differences
   and totals from the displayed inputs. Separate a compulsory cost made visible from an
   avoidable surcharge saved.
4. **Use honest uncertainty.** Label estimates, observed ranges and dated worked examples.
   Do not invent disruption probabilities, customer outcomes or precise crowd patterns.
   Compare plausible scenarios and recovery margins when probabilities are unavailable.
5. **Let the evidence constrain the call.** If the inputs do not establish a general
   winner, recommend by profile or identify the missing input. Do not turn a personal
   preference into a claim about what most visitors do or remember.

Keep cols as a list with one entry per actual column. Each row must have exactly that
many cells. Put units in headers or a clear caption. A missing value needs an explicit
meaning; do not fabricate one to complete a table. Do not label qualitative judgments
"scored" unless a useful, disclosed scoring method really exists.

## Make exceptions usable and consistent

Use distinct labels such as **This suits you if** and **Choose another option if**.
Each exception must name both the condition and the alternative action. An acknowledged
preference, mobility need or family constraint must be allowed to change the result.
Avoid two differently named boxes that merely repeat the same side of the choice.

Apply the printed exceptions yourself. Check that the answer still agrees across the
table, explanation, figure, itinerary, summary and carry card. If a summary cannot retain
a consequential exception, make it conditional or refer clearly to the full decision.
Do not compress "check whether your ticket includes this service" into "buy another
ticket." Update the shared rule first and review every dependent occurrence.

For operational advice, distinguish states that require different actions:

- Tickets **not yet released**, **sold out**, **temporarily unavailable** and a venue
  **closed** are different situations. Give a fallback that applies to the actual state.
- A route that depends on an escalator, lift, seasonal service or particular station needs
  the applicable status and an alternative when that dependency fails.
- A listing's claimed identifier is not independent verification of its validity or its
  match to an address. Explain the actual verification step when recommending one.
- A flexible day can absorb an excursion only if travel days, bookings and available time
  really permit the swap. State arrival, departure, nights and full days consistently.

## Write the answer for the reader

Lead with the decision and its consequence in plain language. Use enough reasoning to
make the choice assessable; do not impose a word quota or dramatize an ordinary trade-off.
Avoid declaring a section the book's most important page. Cross-reference the actual
calculation, source or procedure when the reader needs it, using working links and page
references generated from the final build.

Choose visuals by explanatory need: a map for geography, a small table for comparable
options, or a diagram for branching steps. A photograph can orient or convey atmosphere;
it does not prove an access rule, operating condition or service quality. Keep it accurate
and describe its provenance honestly.

## Completion check

Confirm that the reader can identify the default, recognize an applicable exception and
carry out the resulting action. Check the comparison and the most consequential inputs,
then trace the decision into every summary. Keep unresolved limitations visible. A
mechanical validator can confirm fields and links; an editorial read must assess whether
the recommendation follows from the evidence.
