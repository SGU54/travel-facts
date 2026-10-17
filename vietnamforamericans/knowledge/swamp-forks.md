# Swamps × decision forks — 2026-10-17

The ten swamps in `article-list.json` mapped to the 74 unresolved forks in `decision-gaps.md` (DK #1–34, LP #35–58, Moon #59–74), with what the three books say, what `facts.json` now settles, and what the decision manual still owes. Input for the next dossier Stage A pass. Five fork clusters have no swamp and are proposed at the end.

| swamp | forks | books' positions | now settled by facts.json | still owed to the reader |
|---|---|---|---|---|
| north-south-routing | #1, #35, #40, #41, #63, #66 | DK and Moon run north→south, LP south→north; none gives a reason. Three different "best month" answers. | `transport.us_nonstop_routes` (SFO–SGN is the only nonstop, so a West Coast nonstop traveller starts south), `transport.rail_hanoi_hcmc`, `transport.tet_trains`, `calendar.tet_dates` | A rule keyed to gateway × month × party: when the nonstop decides it, when the weather decides it, when neither does. |
| halong-bay-cruise-choice | #9, #59, #62, #68 | Moon: Sep–early Dec; Halong OR Ninh Binh for short trips; winter weather sidelines boats. DK/LP sell the mist. | `transport.halong_boat_suspensions`, `transport.hanoi_halong_drive` (2.5 h, not 4) | Day vs overnight in days-cost terms (a day cruise still costs two days); a cancellation-risk statement for Dec–Feb dates; Bai Chay walk-up vs Hanoi booking. |
| visa-choice | #30, #53 (passport) — all three books' visa chapters are obsolete | VOA letters, embassy visas, "rubber stamp" extensions. | Already settled before this pass (visa.*); `documents.hotel_registration_law` closes the passport fork | Nothing new; keep corrections #3, #4, #5, #7. |
| motorbike-or-driver | #29, #39, #49, #72, #73 | DK "licence rarely asked", LP "IDP now valid", Moon "pay the fine". Easy Rider pillion (LP) is the only publishable form. | `transport.red_light_no_turn`, `transport.helmets_all_riders`, `transport.no_licence_prohibited_act`, existing driving_licence / unlicensed_insurance | A clean close: the fork is not rent-vs-drive, it is pillion-with-a-licensed-rider vs car-with-driver vs skip; Ha Giang loop options (#39). |
| long-leg-transport | #3, #38, #40, #63 | LP: fly ≈ sleeper price beyond Nha Trang; open-tour trade-offs; Moon: train replaces a hotel night. | `transport.rail_hanoi_hcmc` (33–34 h, upper berth cheapest, 60-day booking), `transport.tet_trains` (no blackout), `transport.metro_*` | A per-leg verdict table (Hanoi–Hue, Hue–Danang, Danang–Nha Trang, Nha Trang–HCMC) by party size and sleep tolerance. |
| mekong-day-vs-overnight | #7, #11, #57, #64, #65 | Moon alone maps the second axis (Vinh Long, Sa Dec, Tram Chim, Chau Doc) and prices it in days; CDC settles malaria for the deltas. | `safety_health.malaria` (deltas: no prophylaxis), `transport.cambodia_evisa_ports` (the Chau Doc river crossing does NOT take a Cambodian e-visa; Bavet does) | Day vs two-night vs onward-to-Cambodia, keyed to interest (markets, birds, Khmer culture) and to the e-visa port rule. |
| cash-vs-card | #24, #25, #26, #55, #69 | DK/LP "USD widely accepted"; four tipping opinions; ATM figures all stale. | `money.legal_tender_dong_only`, `money.banknotes` (500k/20k lookalikes); corrections #1 | How much cash per day by region, stated structurally; reconvert-or-spend-down threshold. |
| hoian-base-choice | #5, #8, #36, #47, #60 | Hue: zero days (Moon), one night (LP), two days (DK). Hai Van by pass, tunnel or train. Danang's own night never weighed. | `transport.international_airports` (DAD is a gateway), `transport.helmets_all_riders` (pillion on the pass) | Nights per base by trip length and by beach/history/food weighting; Hue's day count as a named rule. |
| sapa-trek-choice | #10, #45, #46 | Moon and growers' calendars: harvest Sep–Oct (LP's November is wrong); Sapa vs Bac Ha vs Mai Chau ranked on different axes. | nothing (harvest is observation-grade; kept structural) | Which base for a first-timer with three days; when an independent walk is enough. |
| tet-timing | #18, #44, #67 | DK "participate", Moon "poor visit", LP "train blackout" (now false). | `calendar.tet_dates` (2027-02-06, 2028-01-26, 2029-02-13), `calendar.tet_2027_holiday` (4–10 Feb 2027), `calendar.public_holidays`, `transport.tet_trains` | A net-gain verdict for a 10-day first-timer whose dates touch Tet; the book-ahead window. |

## Fork clusters with no swamp (proposed)

| proposed id | forks | why it qualifies | risk |
|---|---|---|---|
| halong-or-ninh-binh | #59, #62 | A genuine either/or for every 7–10-day trip; Moon frames it, nobody resolves it. | Title is place-vs-place (R2); must be written as a *time* decision ("two days from Hanoi: boat or rowboat"). |
| hue-how-long | #36, #60 | Three books, three answers (0/1/2 days); every itinerary article trips on it. | Low search volume; mostly dossier material. |
| which-month-which-region | #17, #42, #66 | Three books, three national answers; the grid already exists in geo.ts; the verdict layer does not. | Overlaps best-time-to-visit; belongs in the dossier, not a new article. |
| mekong-which-axis | #64, #65 | Moon's second axis is unwritten anywhere on the site. | Fold into mekong-day-vs-overnight rather than a new swamp. |
| phong-nha-detour | #37, #61 | 4–5 days for the country's "best up-and-coming destination" vs what it displaces; no article exists. | New destination article first (see candidates), swamp later. |

Recommendation: add **halong-or-ninh-binh** and **hue-how-long** as swamps; treat the other three as dossier sections under existing swamps.
