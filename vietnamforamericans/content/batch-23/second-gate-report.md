# Batches 21–23 — second gate (in-session, 2026-10-17)

Thirteen gap-topic articles (the 2026-10-17 SERP promotions), written as three batches: 21 (five
central/northern decision pages), 22 (south, safety and health), 23 (culture and the
Vietnamese-American page). **Deviation from the batch-20 method:** no external model was pasted;
the session ran the contradiction hunt itself against facts.json (73 keys), corrections #1–#8 and
the live neighbours (hue-travel-guide, halong-bay-day-trip-vs-overnight-cruise, chau-doc-cambodia-
border-crossing, overland-border-crossings-vietnam, dmz-vinh-moc-tunnels-tour-from-hue,
ninh-binh-day-trip-from-hanoi, do-americans-need-a-visa-for-vietnam, vietnam-itinerary-14-days).

## Mechanical gates
- `check-batch.py`: all guards passed on all three batches (48 distinct fact keys corpus-wide, no
  span clash, no withholding, no certainty escalation, excerpts clean).
- `validate-batch.mjs --list --facts`: the only FAILs are the thirteen `IMAGE_SLOT` comments,
  which Stage 4 converts; answer-first gate passes (every H2 opening block ≥ 40 words, no
  pronoun openers; 45 over-long openers were split at a sentence boundary). Batch 23 carries the
  "3 articles (expected 5)" warning by design.
- `validate-facts.mjs`: 73 of 73 verified, 0 errors, after five keys were added for these
  articles (visa.overseas_vietnamese_exemption, documents.same_passport,
  documents.minor_exit_consent, safety.methanol, services.son_doong_expedition).

## Contradictions found and fixed
1. **two-days-from-hanoi-halong-or-ninh-binh** said late spring to early autumn was the bay's
   calm window; the live Ha Long article says summer brings storm cancellations and October–
   November give the best odds. Rewritten to agree: late spring and early autumn into November,
   summer busiest and storm-prone, winter fog.
2. **mekong-delta-beyond-can-tho** asserted a Cambodian visa on arrival at the river post; not
   primary-verified (only transport.cambodia_evisa_ports is). Now says "a Cambodian visa obtained
   by another route".
3. **ha-giang-loop-ride-pillion-or-car** called police checkpoints on the loop "real" (no
   source) and Ha Giang "a long day" from Hanoi (LP 2016 lead says ~6 h by expressway). Softened
   to "police do stop riders" and "most of a day".
4. **exotic-menu-words-to-know**: "US customs will take off you" → "is likely to seize"
   (the certainty was unsupported).
5. **returning-to-vietnam-vietnamese-american**: a muddled banknote sentence replaced with the
   dong-pricing rule (money.legal_tender_dong_only); the dialect generalisation hedged.

## Cross-checks that passed
- Hue day counts agree with hue-travel-guide ("one full day … two days … more than two for a
  specific interest") and with the 14-day itinerary's two Hue days.
- The Chau Doc visa logic (e-visa must name the river crossing as exit; single entry is spent)
  matches chau-doc-cambodia-border-crossing and overland-border-crossings-vietnam.
- DMZ stop descriptions agree with dmz-vinh-moc-tunnels-tour-from-hue (civilian tunnels,
  original dimensions, 10–12 h day); the new page adds Truong Son, Quang Tri and the per-stop
  verdicts rather than repeating the tour logistics.
- Corrections: #2 (IDP not relitigated — the State statement is the position), #5 (no 45-day
  claim), #6 ("decision manual" gloss, byte-identical), #7 (registration duty stated, no
  invented consequence), #8 (SFO–SGN the only nonstop; LAX described as one-stop) all honoured.
- Moon's "stop if the drink tastes off" methanol rule was NOT imported: the FCDO says taste
  and smell do not reveal methanol. Logged in disputes.md.

## Pull × Trust (turn and seed articles)
| article | handoff | Pull | Trust | note |
|---|---|---|---|---|
| ha-giang-loop-ride-pillion-or-car | turn | 72 | 88 | answer given in full (pillion / car / not self-ride); stake = inconsistent insurance across roads; handoff to the road-by-mode system |
| two-days-from-hanoi-halong-or-ninh-binh | turn | 70 | 90 | forecast rule given; stake = month decides more than this pair; handoff to the month × region table |
| how-many-days-for-hue | turn | 68 | 90 | rule stated three ways; stake = the shared pool of central-coast nights; handoff to the allocation |
| mekong-delta-beyond-can-tho | seed | — | 92 | one sentence, in the day-count section |
| returning-to-vietnam-vietnamese-american | seed | — | 90 | one sentence, in the single-trip subsection |

All pass the gate (turn: Pull ≥ 60 and Trust ≥ 80; seed: Trust ≥ 80). Scores are the session's,
not an external model's, and are a craft check, not a revenue estimate.

## Open items for Stage 4
- Thirteen hero + thirteen in-body images (alt text in alt-batch-NN.json).
- Seed SQL appended for 15 newly spanned keys (`vietnamforamericans-facts.sql`, 48 rows total).
- After publishing, `scripts/apply-swamp-tags.mjs --apply` must carry halong-or-ninh-binh and
  hue-how-long into the DB.
