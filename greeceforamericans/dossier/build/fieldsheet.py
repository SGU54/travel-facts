# -*- coding: utf-8 -*-
"""fieldsheet.py — the dated companion. Describes what it CARRIES, never a page count
(bug: Rome promised 6 pages, shipped 2). Only real verified values under a press-time
date; everything else is "confirm in your travel week" with the official source named —
never a blank cell, never "verify". Volatile figures live HERE, not in the Book.
"""

FIELD_SHEET = dict(
   id="fs", eyebrow="THE FIELD SHEET · EDITION 2026.Q1",
   q="The dated companion — check it in your travel week.",
   standfirst="The Book holds what lasts. This holds what moves — and where to confirm it the week you fly, because by then it will have moved again.",
   intro=[
     "This sheet carries the volatile layer the Book deliberately omits: the figures that change within a season. It is not a price list to trust on sight — it is a structured checklist of exactly what to confirm and where the official source lives. Verified values are dated; everything else names the authority to check. When this sheet and the Book disagree, this sheet is newer, and wins.",
     "Survey method, stated plainly: the durable ranges and structural facts below were read from the articles on greeceforamericans.com and cross-checked against the Book's decisions. ▲ SURVEYED 06/25. The live figures — this year's fares and schedules — are yours to confirm in your travel week via the official sources named in each row.",
   ],
   # sections: (title, [(item, what_to_confirm, where)])
   sections=[
     ("FERRIES — CONFIRM THE WEEK YOU SAIL", [
       ("Piraeus → Santorini", "Fast ~5 h / conventional ~8 h — confirm this season's sailings & fares", "the operators' own sites / a ferry aggregator ◆"),
       ("Piraeus → Mykonos", "~3–5 h by sea — confirm departures & whether fast is running", "operator schedules ◆"),
       ("Piraeus → Naxos / Paros", "~3–5 h — frequent in peak, thinner in shoulder", "operator schedules ◆"),
       ("Inter-island hops (Cyclades)", "Short & frequent in summer; reduced off-peak", "operator schedules ◆"),
       ("Cancellation policy", "Fast catamarans cancel first in meltemi; operators rebook or refund", "your operator's terms ◇"),
     ]),
     ("DOMESTIC FLIGHTS — WHEN THE LEG IS LONG", [
       ("Athens ↔ Santorini (JTR)", "~45 min — confirm this season's frequency & fare", "airline sites ◆"),
       ("Athens ↔ Crete (HER/CHQ)", "~1 h — often beats the 9 h overnight ferry", "airline sites ◆"),
       ("Island ↔ island direct", "Limited; most route via Athens — confirm before relying on one", "airline sites ◆"),
     ]),
     ("ENTRY (U.S. CITIZENS) — CHECK BEFORE BOOKING", [
       ("Visa", "None for ≤90 days in any 180 across Schengen", "official EU / U.S. State Dept ◇"),
       ("Passport validity", "Check issue AND expiry dates well before booking", "your passport ◇"),
       ("EES biometric border", "Now rolling out — facial image + fingerprints on entry; no fee", "official EU EES page ◇"),
       ("ETIAS", "Not in force; no launch date announced — apply only via the official EU site if it ever does", "the official EU ETIAS site ◇"),
     ]),
     ("SEASON — THE SHAPE, NOT THE FORECAST", [
       ("Shoulder (May–Jun, Sep–Oct)", "Thinner crowds, calmer wind, warm sea — the recommended window", "▲ STABLE"),
       ("Peak (Jul–Aug)", "Highest crowds & prices; strongest meltemi; fast ferries most disrupted", "▲ STABLE"),
       ("Late-season closures", "Some small-island businesses wind down late Oct onward — confirm your island", "your accommodation ◆"),
     ]),
     ("MONEY — HABITS, NOT AMOUNTS", [
       ("Card prompt", "Always choose EUROS — decline dynamic currency conversion", "◇ STABLE"),
       ("Tipping", "Round up; ~no percentage expected", "◆ STABLE"),
       ("Caldera premium", "Rim-view rooms cost markedly more than inland/beach for the same island", "◆ STABLE"),
     ]),
   ],
)
