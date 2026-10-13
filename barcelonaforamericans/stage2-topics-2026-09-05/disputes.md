# Disputes — human ruling required (curated, hard cap 5)

Panel: claude, deepseek, grok. reconcile.mjs's raw mechanical pass flagged 22/23 fields as
"disputed" because it does exact-string comparison on prose — three independently-written
paragraphs are never byte-identical even in full agreement. This file keeps only the fields
where the panel gave **substantively different answers**, i.e. an actual fact conflict, not a
wording difference. The other ~17 fields were merged into `facts.json` directly.

---

## RESOLVED 2026-09-06

### 1. `health_care.medication_import.prescription_medication_rules` — is there a day/quantity limit?
**RESOLVED — ~3-month supply confirmed.** The user supplied a Google AI Overview citing
es.usembassy.gov, AEMPS, and bu.edu; rather than trust that summary, I fetched two of the
underlying pages directly: `aemps.gob.es`'s own text states controlled-substance permits are
capped at "la cantidad necesaria para el tratamiento durante tres meses" (3 months), and
BU Madrid's institutional page states the same 3-month figure for general prescriptions plus
the "no mailed refills" rule. Written into `facts.json` as `verify_recommended` (not `verified`)
because the general-prescription case is confirmed by an institutional, not government, page.

### 2. `health_care.medication_import.controlled_substances_note` — which mechanism, exactly?
**RESOLVED — grok's specific AEMPS procedure checks out.** Fetched `aemps.gob.es` directly:
it confirms the permit/certificate scheme by name and the 3-month cap in its own Spanish text.
BU Madrid corroborates the operational detail (apply ≥10 days ahead, PDF documents, passport +
itinerary + prescription + doctor's certificate). Written into `facts.json` as `verified`. One
loose end: the application email has two spellings across sources
(`Estupefacientes@aemps.es` vs `estupefacientes_viajeros@aemps.es`) — flagged in
`_open_questions`, confirm the live address before publishing it in an article.

### 3. `ferries_balearics.operators` — does GNV run Barcelona–Balearics?
**RESOLVED — grok was right.** Fetched `gnv.it` directly: GNV's own site lists Barcelona-Palma
de Mallorca, Barcelona-Ibiza, AND Barcelona-Mahón (Menorca) among its routes. Written into
`facts.json` as `verified`, all three operators (Baleària, Trasmediterránea, GNV) now listed.
Also corrected `to_menorca` — a direct Barcelona-Mahón service exists, not routed-via-Mallorca
only as the panel had guessed.

---

### 4. `public_holidays_closures.catalonia_regional_holidays` — is Sant Jordi a public holiday?
**RESOLVED — Sant Jordi is NOT an official holiday.** govern.cat and ajuntament.barcelona.cat
both blocked automated fetches (403/418), so I used publicholidays.es's 2026 Catalonia calendar
as a third-party check: Sant Jordi (Apr 23) is explicitly absent from the official list, and
Easter Monday is confirmed as a genuine Catalonia-specific regional holiday. deepseek conflated
the book-and-rose cultural festival with a legal day off; claude and grok were right. Written
into `facts.json` as `verified` (with a note to re-check the actual Generalitat DOGC/BOE
publication for the specific travel year, since this used a third-party aggregator, not the
primary government source, which blocked the fetch).

---

### 5. `public_holidays_closures.barcelona_local_holidays` — what's the SECOND local holiday?
**RESOLVED — Whit Monday, for 2026 specifically.** `ajuntament.barcelona.cat` (primary source)
blocked automated fetches (418), so `gremicat.es` was used as a third-party check: it confirms
Barcelona's two 2026 local-holiday dates as May 25 and September 24. May 25, 2026 checks out
astronomically as Whit Monday (Pentecost Monday). grok was right; deepseek's Santa Eulàlia
(Feb 12) was wrong for this year. Written into `facts.json` as `verified`, WITH a hard caveat:
the council re-picks its 2 local days every year, so this is 2026-specific and must be
re-checked for any future travel year rather than copied forward.

---

## All 5 disputes resolved (2026-09-06)

`facts.json` now has zero `status: "disputed"` fields for this batch. Remaining caveats live in
its `_open_questions` (AEMPS email spelling, exact ferry timetables/fares, EU compensation
percentages, hospital cost ranges — all ordinary serve_live/verify_recommended items, not
panel disagreements). Ready for the writing stage on these 6 articles, subject to those
open-question checks at write time.
