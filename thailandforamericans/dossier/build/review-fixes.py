# -*- coding: utf-8 -*-
"""review-fixes.py — the 2026.09 editorial review, items 1-15.

The review's instruction was: do not rewrite the book broadly. These are targeted.
Every edit asserts a single match, so a silent miss is impossible.
"""
import json, re, sys
p = "content.py"; s = open(p, encoding="utf-8").read()
E = []

# ── 1 + 15. WHAT THE CORPUS IS. The book quoted sentences and attributed them to
# "the corpus" without ever saying what that is. It is this site's own published
# reporting — the same desk. That is fine, and it has to be stated, because a
# quotation from oneself is not corroboration. It also makes #12 a real problem.
E.append((
 '   ("What this book will not do",',
 '''   ("Where the quotations come from",
    "This book is built from 97 articles published on thailandforamericans.com "
    "— the same desk, not an outside authority. Sentences in quotation marks are "
    "verbatim from those articles, and the ledger at "
    "<strong>thailandforamericans.com/sources</strong> lists every one, so any "
    "{off} or {sur} claim can be traced to the page it came from. Where a claim "
    "rests on something other than that reporting, the source is named in the "
    "line itself."),
   ("What this book will not do",'''))

E.append((
 '    ("sur", "Consistent across every article surveyed. The corpus says it more than once, independently."),',
 '    ("sur", "Stated consistently across the reporting behind this book. Repetition by one desk is consistency, not corroboration."),'))
E.append((
 '    ("off", "A published figure, reported as published — a fare band, a flight time, an airport rule."),',
 '    ("off", "A reported figure, passed on as reported — a fare band, a flight time, an airport rule. Traceable in the source ledger."),'))
E.append((
 '    ("est", "Derived. The corpus supplies the parts; the conclusion is this book\'s."),',
 '    ("est", "Derived. The reporting supplies the parts; the conclusion is this book\'s, and is arguable."),'))

# ── 2. FOUR MEASUREMENTS. The prose said "weather exposure"; FIG. 3 measures
# ground transport. And they are not "unrelated" — air access and booking
# structure plainly bear on each other.
E.append((
 '   "Four unrelated measurements, air access, medical capability, booking "\n   "structure and weather exposure, draw the same line through the same seven "',
 '   "Four separately observed measures — air access, medical capability, how "\n   "many booked legs a journey takes, and what moves you around once you are "\n   "there — draw the same line through the same seven "'))

# ── 3. INSURANCE CERTAINTY. The book itself later says wordings differ.
E.append((
 '   "you rent anyway → you have chosen to carry the medical cost yourself; decide "\n   "that deliberately rather than at the counter",',
 '   "you rent anyway → ride as though a motorbike claim would be refused, because "\n   "outside your policy\'s licence condition it may be; decide that deliberately "\n   "rather than at the counter",'))

# ── 4. HIGHEST PRIORITY. Nothing in this book may read as "delay treatment".
E.append((
 '''   "<strong>Buy the policy for the evacuation line rather than the medical line, "
   "and then call the assistance number before treatment, not after.</strong> "
   "That "
   "one call is what decides whether the hospital bills your insurer or bills you."''',
 '''   "<strong>Buy the policy for the evacuation line rather than the medical "
   "line.</strong> In an emergency, get treated first: nothing on this page is a "
   "reason to delay care. Whenever circumstances allow — and for anything that is "
   "not an emergency they usually do — <strong>call the assistance line before "
   "the billing is arranged</strong>. That call is what decides whether the "
   "hospital bills your insurer or bills you."'''))

# ── 5. SEPARATE TICKETS. The proposition is that the connection is unprotected,
# not that rebooking is impossible.
E.append((
 '   "separate contracts: no rebooking, no compensation, no through-checked bag. "\n   "The ticket is forfeit and a new one has to be bought."',
 '   "separate contracts: the onward carrier owes you nothing for a connection "\n   "missed because the inbound ticket failed, and the bag is not through-checked. "\n   "Plan as though the replacement ticket is yours to buy."'))

# ── 6. The prose said "only filter" while the table applies five tests.
E.append((
 '   "<strong>Carry a scarf or a sarong, and use riding as your only filter on an "\n   "elephant venue.</strong> One instantly covers shoulders or wraps as a skirt; "\n   "the other settles an ethics question that no amount of marketing language will."',
 '   "<strong>Carry a scarf or a sarong, and use riding as the first filter on an "\n   "elephant venue.</strong> One instantly covers shoulders or wraps as a skirt; "\n   "the other ends the search early: if a venue offers rides, stop there. Passing "\n   "that test is necessary, not sufficient — the table names what else to read."'))

# ── 7. Describe the practice, not an inferred mental state.
E.append((
 '    "a training process that breaks a young elephant\'s spirit; heavy seats can damage the spine over time",',
 '    "a training process built on coercion and restraint; heavy seats can damage the spine over time",'))

# ── 8. "No second instrument" then five more instruments.
E.append((
 '   "is simultaneously the quality test and the safety test. There is no second "\n   "instrument to learn."',
 '   "is simultaneously the quality test and the safety test. The queue is the "\n   "first inspection; the rest of this page is the second."'))
E.append((
 '   "simultaneously the quality test and the safety test."},',
 '   "the first inspection you can make from the pavement."},'))

# ── 9. The sentence as written denies that street food is cheap.
E.append((
 '   "Street food in Thailand is not the cheap option. \\"Vendors often specialize "',
 '   "Street food in Thailand is not merely the cheap option. \\"Vendors often specialize "'))

# ── 10. The chapter measures transit access, not personal safety.
E.append((
 '   "<strong>If you want the single safest first choice, book near Asok and stop "\n   "deciding.</strong>',
 '   "<strong>If you want the lowest-friction first choice, book near Asok and stop "\n   "deciding.</strong>'))

# ── 11. "Scored" contradicts the stated refusal to rank.
E.append((
 '   "they fly over or under the traffic.\\" {sur} Every district below is scored on "\n    "that and nothing else, because everything else about them is preference."',
 '   "they fly over or under the traffic.\\" {sur} Every district below is compared on "\n    "that and nothing else, because everything else about them is preference."'))

# ── 13. The Field Sheet dropped the condition the body states.
E.append((
 '       "than being found. Under 90 days is a fine and no ban. A few hours caused "',
 '       "than being found. <strong>On voluntary departure</strong>, under 90 days "\n       "is a fine and no ban; being caught is harsher. A few hours caused "'))

for old, new in E:
    if s.count(old) != 1:
        sys.exit(f"NO MATCH ({s.count(old)}):\n{old[:150]}")
    s = s.replace(old, new)
open(p, "w", encoding="utf-8").write(s)
print(f"  applied {len(E)} edits to content.py")

# ── the same two corrections in the drawing and its caption
pf="figures.py"; f=open(pf,encoding="utf-8").read()
F=[("Four unrelated measurements. The break falls in the same place ",
    "Four separately observed measures. The break falls in the same place "),
   ("Four unrelated measurements break between Ao Nang and ",
    "Four separately observed measures break between Ao Nang and "),
   ('"Air access, medical capability, booking structure and ground transport are "\n     "measured by four different industries that do not consult one another. They "',
    '"Air access, medical capability, booking structure and ground transport are "\n     "recorded by four different industries that do not consult one another. They "')]
for old,new in F:
    if f.count(old)!=1: sys.exit(f"FIG NO MATCH ({f.count(old)}): {old[:90]}")
    f=f.replace(old,new)
open(pf,"w",encoding="utf-8").write(f)
print(f"  applied {len(F)} edits to figures.py")
