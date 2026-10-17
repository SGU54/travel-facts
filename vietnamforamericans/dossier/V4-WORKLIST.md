# Vietnam, End to End. — v4 worklist (from the 2026-10-17 Stage A pass)

Nothing in v3 is wrong against facts.json (73 keys). v4 is additions. Each row names the build file,
the claim, its provenance mark and the fact key that supports it. Shelf-life decides the document.

| # | where | add | mark | key / source |
|---|---|---|---|---|
| 1 | D06 The northern leg (content.py) | The forecast rule for a two-day window: calm → the bay overnight; cloud, wind or warning → Ninh Bình, sleep there; the port authority grounds every boat at once, operators only refund; Ninh Bình from the same hotel the same morning | ◇ | transport.halong_boat_suspensions, transport.hanoi_halong_drive |
| 2 | D06 figure | A two-day ledger: bay overnight vs Ninh Bình, in hours on the road and hours on the water, with the cancellation asymmetry as the third column | — | derived from #1 |
| 3 | D07 Hội An/Huế (content.py) | Huế's nights as a rule: history 2, +1 for the DMZ, beach-and-food 1 on the way through with the Hải Vân train, ≤7 days a pass-through; the central-coast "pool of nights" by trip length | ● | hue articles + itineraries (synthesis, assumptions named) |
| 4 | Set piece: Phong Nha (content3.py) | Three bands of cave; four days' cost and what it displaces; Sơn Đoòng is a trip you plan a holiday around | ● | phong-nha article; price → Field Sheet only |
| 5 | Field Sheet | Sơn Đoòng expedition price and length (operator figure) | ◆ | services.son_doong_expedition |
| 6 | D04 Ride, pillion, driver | Pillion with a licensed rider is the lawful two-wheel form; helmets for rider and passenger, strap fastened; driving unlicensed is itself a prohibited act; red means stop, no right on red without an arrow | ◇ | transport.helmets_all_riders, transport.no_licence_prohibited_act, transport.red_light_no_turn |
| 7 | D03 The e-visa form | The Cambodian side: a Cambodian e-visa works only at Bavet (Mộc Bài); the Châu Đốc boat needs a Cambodian visa by another route; name the river exit on the Vietnamese form | ◇ | transport.cambodia_evisa_ports |
| 8 | Hospital ledger (content2.py) | Row: "the cocktail in the bucket" — methanol from licensed bars and shops in tourist areas; taste does not reveal it; blurred vision the next day is a hospital, not a hangover | ◇ | safety.methanol, safety.emergency_numbers, services.medical_facilities_hanoi |
| 9 | Before You Fly (content4.py) | Box for Vietnamese Americans: enter, fly domestically and exit on one passport; a child of Vietnamese parentage may need a Vietnamese passport or exit visa; notarised consent for a Vietnamese minor without both parents; the five-year exemption paper for repeat trips | ◇ | documents.same_passport, documents.child_exit, documents.minor_exit_consent, visa.overseas_vietnamese_exemption |
| 10 | Money chapter | Cite the dong-only rule as law (SBV Circular 32/2013), not custom | ◇ | money.legal_tender_dong_only |
| 11 | Hotels/registration line | Add that the law puts the declaration on the host within 12 h (24 h remote) and requires no passport surrender | ◇ | documents.hotel_registration_law |
| 12 | SITE.guide hooks | Two raw hooks (band, aside, inline) for `halong-or-ninh-binh` and `hue-how-long` — in DELIVERABLES.md; the marketing skill strengthens before site.ts | — | — |

Gates after the build: audit-release.py on the new build dir; re-read every changed page; re-upload
book + phone + sheet to the `guides` bucket; bump `state.json.guide.revisions`. Rhythm: +5–7 pages
wants one more plate (two if a Phong Nha page opens a chapter) — the images folder now holds the
batch 21–23 photographs, 26 more landscape frames.

Timing (★ operator): fold into the January 2027 Field Sheet reissue (clock starts 2027-01-01), or
build v4 now. Recommendation: January, because v3 contains no error and the Sheet reissue already
forces a render and an upload.
