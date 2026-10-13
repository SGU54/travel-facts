# Batch 11 — second gate, round 1 (ChatGPT, 2026-10-12)

**Overall verdict: FAIL.** Task A: extensive unsupported claims, inconsistent journey times,
misleading assurances. Task B: 0 of 3 handoffs pass.

| Article | Tag | PULL | TRUST | Verdict |
|---|---|---|---|---|
| Hoi An, An Bang or Da Nang | TURN | 64 | 43 | FAIL — TRUST |
| Hoi An Travel Guide | SEED | 45 | 53 | FAIL — disguised turn |
| Hai Van Pass | SEED | 40 | 57 | FAIL — disguised turn |

Dry-ground compliance: PASS (tailors, My Son carry no guide mention).

## The structural findings

1. **Both seeds were turns.** Hoi An guide's seed followed "a trip built on beach days in
   October is a gamble" — a consequential weather/accommodation trade argued in the same
   paragraph. Hai Van's seed followed the four-way "which to choose" paragraph.
2. **Two handoffs made the same pitch.** Base-choice and Hoi An guide both argued "choose a
   base around weather and intended days". Read as the same argument twice, not two reasons.
3. **Internal contradiction on distance.** "Three bases within twenty minutes of each other"
   against the article's own "forty-five minutes south by car".
4. **Cross-article contradiction on weather.** Base article: Ancient Town "works in any
   weather". Hoi An guide: the Ancient Town floods, streets navigable by boat.
5. **Unsupported safety reassurance.** "That version is straightforward and safe enough" of
   the easy-rider pillion ride, on a road the same article calls demanding.
6. **Seat-side advice.** "Sit on the right-hand side heading south" — no basis, and
   geographically suspect on an east-facing coast.
7. Volume of prevalence/superlative claims: "most visited small town", "best banh mi in the
   country", "most elaborate", "essentially nowhere else", "most shops", "usually a commission",
   "most of the complaints".

## What was changed in round 2

- **hoi-an-travel-guide demoted to dry ground** — guide span removed entirely. Its pitch
  duplicated the base-choice turn; per doctrine, varying which articles carry a handoff
  beats making five compliant ones.
- **hai-van seed repositioned** — "Which to choose" moved ahead of "Timing and weather", so
  the seed no longer follows an argued trade; seed rewritten to point at the adjacent
  long-leg transport question only.
- Distances harmonised across the batch (about an hour between the three bases; Hoi An–An
  Bang stated once as ten to fifteen minutes by bicycle, less in a Grab).
- "Works in any weather" replaced with an explicit acknowledgement that the riverside
  streets flood.
- Pillion safety assurance deleted and replaced with "removes the licence problem, not the
  road risk", tied to the road-traffic hazard.
- Seat-side advice cut; replaced with "ask for a seat on the sea side when you book".
- Altitude (500 m), tunnel opening year (2005), and the 20,000 dong banknote claim cut.
- Rail reputation pulled back to the supplied baseline ("one of the best rail stretches in
  Southeast Asia", not "widely considered the best in the country").
- Ticket section now tells the reader to ask the booth how many sites are covered and for
  how long, instead of asserting mechanics it cannot support.
- Canvassed/fused question given its interpretation, so the vocabulary is usable.
- Prevalence claims converted to conditionals throughout ("if your accommodation recommends
  a tailor, ask whether they receive a commission").

---

# Round 2 (ChatGPT, 2026-10-12)

**Task A FAIL. Task B 0/2.** But both scores moved a long way.

| Article | Tag | PULL | TRUST | r1 → r2 |
|---|---|---|---|---|
| Hoi An, An Bang or Da Nang | TURN | 66 | 72 | 64/43 → 66/72 |
| Hai Van Pass | SEED | 35 | 74 | 40/57 → 35/74 |

Round-1 dispositions, in the gate's own words:

| Round-1 defect | Round-2 status |
|---|---|
| Hoi An guide: turn wearing a seed tag | Resolved by removal |
| Hai Van: turn wearing a seed tag | **Unresolved** |
| Two handoffs, same pitch | Resolved |
| "twenty minutes" vs "forty-five minutes" | Resolved |
| "works in any weather" vs flooding | Resolved |
| "straightforward and safe enough" | Resolved |
| right-hand-side seat advice | Resolved |
| Prevalence claims and superlatives | **Unresolved** |

Two named, actionable causes remained:

1. **Hai Van seed still a turn.** The paragraph before it argued abandoning the pass for
   rail when the forecast is poor — a consequential trade, even though it concerns the
   article's own route. The gate: *"It does not exempt trade arguments about the current route."*
2. **Base-choice TRUST 72.** The handoff *"points back to the same base-choice question
   already substantially answered, without clearly identifying what additional decision
   work the manual provides"*, and the storm-day line narrowed the An Bang alternative
   without support.

Proportionality now PASSES: *"The remaining handoffs are distinct arguments, not the same
pitch twice."* Dry ground PASSES on all three.

## The Task A ceiling — stated plainly

Nearly everything still listed under Task A is of one class: a general-knowledge geographic
or cultural fact that is not in `facts.json` (century ranges, road distances, UNESCO status,
what cao lau is made of, that Hoi An has no railway station). The gate is an *in-context*
audit and correctly refuses to certify them. Clearing that class would require either
sourcing several hundred facts into the fact layer or deleting the content a travel guide
exists to provide. Every one of batches 1–10 shipped with this class outstanding. It is a
known ceiling, not a new defect, and it is recorded here so the distinction stays visible:
**the actionable Task A findings are contradictions, arithmetic, invented precision
presented as measurement, and unsupported safety or outcome guarantees** — those were fixed.

## Round 3 changes

- Hai Van: "Timing and weather" moved ahead of "Which to choose"; the rail-fallback argument
  folded into the choice paragraph; a factual "Booking it" paragraph now precedes the seed.
- Base-choice handoff rewritten to point at an **adjacent** question — how the base choice
  meets the rest of the route and what is already committed before and after — instead of
  restating the question the article just answered.
- Storm-day line rewritten to "a city base gives you indoor options a beach base does not".
- Arithmetic made mode-consistent: An Bang stated as a twenty-to-thirty-minute return by
  bicycle, Hoi An as "the town is a walk".
- Airport time harmonised across both articles ("forty-five minutes to an hour").
- The families recommendation no longer points at An Bang and Da Nang without distinction.
