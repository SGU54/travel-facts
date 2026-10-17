# Vietnam — Stage A / A2 / A3 record · 2026-10-14

## Stage A — the corpus

100 published articles, 88,492 words (corpus.json, exported 2026-10-14 from schema `vietnam`).
Yield model: 100 × 0.5 ≈ **50 pages**. Guide-spans stripped before every tally (39 spans).

Category inventory (words): hanoi 6,110 · hoi-an-da-nang 6,081 · ho-chi-minh-city 4,958 ·
flights-trains 4,532 · best-time-to-visit 4,468 · nha-trang-phu-quoc 4,388 · temples-history
4,370 · nature-trekking 4,365 · halong-bay-sapa 4,278 · entry-and-visa 3,902 · mekong-delta
3,515 · dishes 3,408 · safety-and-health 2,980 · two-weeks-plus 2,773 · north-south-route
2,711 · street-food 2,684 · hue 2,662 · money 1,862 · grab 1,793 · one-week 1,781 ·
connectivity 1,751 · motorbikes 1,723 · beaches 1,706 · etiquette 1,691 · coffee 1,688 ·
singletons 814–932 each.

Edge tally (raw cues): MONEY 465 · EXPERIENCE 392 · BREAKAGE 127 · EXTRACTION 15.
Read: Vietnam is cheap, so the money cues are *prices*, not *losses*. The high-stakes
material is BREAKAGE (refused at the gate, voided insurance, a cancelled bay, a seat that
does not exist at Tết) and the **day economy** — a thousand-mile country on a two-week
clock. The cover promise leads with *order and days*, not savings.

Synthesis checks (audit-synthesis.py):
- month × direction × visa-port × nonstop → scattered 19/4/21/15 of 100, joined in **0** → HEADROOM 7.4 (STRONG; the nonstop theme is a 4-article fact, flagged thin, which is the point: nobody connects it).
- day economy (Sapa hours / cruise vs day trip / Can Thơ / internal flights) → 21/27/13/15, joined in 5 → HEADROOM 2.7, STRONG.

## Stage A2 — the shape

**Shape:** a one-way corridor through a country (sequencing), not a city.
**Organising fact:** Vietnam runs three climates at once down a single 1,650 km line, and
the direction you travel it is locked by the international ticket and the e-visa form —
both normally bought before anyone has looked at a weather table.
**What this audience gets wrong:** books SFO→SGN (the only US nonstop) or an open-jaw into
Hanoi, fills in the e-visa with a port and a duration, and only then discovers that October
puts the centre in its storm season, that a Mekong overnight costs two days it no longer has,
that a US licence and an IDP are both invalid, and that none of those can be changed from
inside the country.
**Cover device:** the country as a vertical line from real coordinates with the three
season bands beside it — the "which third is in season when" figure.
**Standard chapters that don't apply:** the walk-time terrain chapter (a country has no
walk thesis). Replaced by THE GROUND (the three-climate line) and a SEQUENCING decision.
Transit-reality page becomes "the legs" (fly/train/sleeper by distance).

## Decisions (shortlist, with veins)

| # | decision | vein | words |
|---|---|---|---|
| 01 | Days: how many do you really have, and how many regions do they buy? | itineraries ×6 + flights | ~6,300 STRONG |
| 02 | Month and direction — which end do you start from? (FREE HOOK) | best-time, weather, n-to-s, flights, itineraries | ~8,200 STRONG |
| 03 | The e-visa form as the first route commitment | visa ×3, overland, Châu Đốc, Cambodia, customs, airport | ~7,500 STRONG |
| 04 | Ride, pillion, driver — the licence and the insurer | motorbike, driver, safety, Hải Vân, Hà Giang, cities | ~7,300 VIABLE+ |
| 05 | Fly, train or sleeper — by leg | train, domestic flights, sleeper, Hanoi–Sapa, Huế–Hội An | ~5,400 VIABLE |
| 06 | The northern leg: the bay, Ninh Bình or Sapa | Hạ Long ×2, day trips, Ninh Bình, Cát Bà, Sapa ×4 | ~8,600 STRONG |
| 07 | Hội An, An Bàng or Đà Nẵng — and the tailor's two days | base, Hội An, tailors, stay, Đà Nẵng, Mỹ Sơn, Marble Mts | ~7,000 VIABLE |
| 08 | The last block: Mekong overnight, Phú Quốc, Côn Đảo, or the city | Mekong ×3, Châu Đốc, Côn Đảo, Phú Quốc, HCMC | ~6,200 VIABLE |
| 09 | Which beach, by month | PQ vs NT, PQ, NT, resorts, Mũi Né, beaches, Côn Đảo | ~6,000 VIABLE |
| 10 | Tết: through it or around it | Tết, festivals + mentions in 19 articles | ~2,600 (scatter 19) VIABLE-by-scatter |
| 11 | Cash: how much, and where the card stops | money, tipping, customs-cash + mentions in 38 articles | ~3,700 (scatter 38) VIABLE-by-scatter |

Refused (THIN or not a decision): a Grab chapter (it is a rule, not a fork); war sites as a
decision (experience, no losable call — folded into the set pieces); connectivity (a rule);
packing (a checklist, folded into Before You Fly); water puppets / Train Street (trivia cell).

## Stage A3 — the name (★ user confirms)

Pattern: destination + promise of resolution. Proposed:
1. **Vietnam, End to End.** — the country's length and the whole trip resolved (default)
2. Vietnam, in Sequence.
3. Vietnam, Top to Bottom.

Thesis line: *A thousand-mile country, two weeks, three seasons that never agree — the order
that keeps the trip whole.*

Hooks by swamp id (raw, accurate first) are emitted in DELIVERABLES.md after Stage C.

## Image library

196 files on the volume (batches 01–10 under `upload/`, 11–20 under `images/`); 176 landscape
≥1200px. Contact sheets `_sheets/sheet-00..04` (b11–20) and `sheet-10..13` (b01–10), index in
`_sheets/index.json`. Plates chosen in build/content*.py by slot.

---

# Stage A pass · 2026-10-17 (after batches 21–23 and the knowledge-first exercise)

Input: `STAGE-A-INPUT-2026-10-17.md`. Corpus re-exported: **113 published articles, 118,230 words**
(guide-span paragraphs stripped before every tally). Yield model 113 × 0.5 ≈ 56 pages; the shipped
v3 runs 73, so the constraint is editorial. Depth: v3 uses 19.8k of 118k words (16.7 %, floor 11 %).

## Check of the v3 release against the eight new facts — nothing to retract

| fact | v3 says | verdict |
|---|---|---|
| transport.red_light_no_turn | nothing on turning on red | no conflict; the rule can be added to D04's "if you ride anyway" |
| transport.tet_trains | no blackout claim | no conflict (the LP blackout was never imported) |
| transport.us_nonstop_routes | "the only nonstop … San Francisco to Ho Chi Minh City" | agrees |
| transport.hanoi_halong_drive | no hours printed for the road | no conflict; the 2.5 h figure strengthens D06 |
| transport.cambodia_evisa_ports | "provided the e-visa named a river exit" (Vietnamese side only) | agrees; the Cambodian side (e-visa works only at Bavet) is missing — add |
| calendar.tet_dates / tet_2027_holiday | "In 2027 Tết falls on 6 February, holiday 4–10 February" | agrees |
| money.legal_tender_dong_only | "always đồng" (DCC context) | agrees; the legal basis can be cited |
| documents.hotel_registration_law | "registered with the local police … a homestay host is responsible" | agrees with Law 47/2014 Art 33 |

The three book-vs-book forks: Hạ Long season — v3 says October is the clearest month (agrees with
Moon's Sep–early Dec and the site); Sapa harvest — v3 says "September: the terrace harvest" (agrees);
passport at the desk — v3 says the hotel takes it for registration (agrees, and the law now adds
that no surrender is required, only the host's declaration).

## Synthesis checks on the 113-article corpus

| thesis (themes) | scattered in | joined in | HEADROOM |
|---|---|---|---|
| month × direction × visa port × nonstop (the v3 spine) | 41/36/22/5 | 0 | **11.5** (was 7.4 at 100 articles) |
| bay suspension × Ninh Bình × winter fog × two-day window | 9/20/46/26 | 2 | **5.9 STRONG** — the `halong-or-ninh-binh` swamp is a real decision, not a sub-point |
| licence × insurer × Hà Giang/Hải Vân pillion × helmet/police | 23/19/27/17 | 7 | 2.3 STRONG but partly pre-joined (D04 already exists; the new articles join it) |
| same passport × exemption paper × minor consent × registration (the Vietnamese-American reader) | 13/6/22/19 | 1 | 4.6 but THIN raw material (6 articles) — a box, not a decision |

## What the thirteen new articles add to the vein

- **halong-or-ninh-binh** (new swamp): the forecast rule, the port-authority grounding as the asymmetry, Ninh Bình as the same-morning fallback, and the 2.5 h road. Extends D06.
- **hue-how-long** (new swamp): the three-book disagreement resolved by interest (history 2 nights / DMZ 3 / beach-and-food 1 / ≤7 days a pass-through), and the "pool of central-coast nights" framing. Extends D07.
- **Phong Nha**: a four-day cost and what it displaces; Sơn Đoòng as a trip, not a stop (volatile price → Field Sheet). New set piece under D06/D07.
- **D04**: pillion with a licensed rider is the only lawful two-wheel form; helmets for every rider and passenger (Law 36/2024 Art 33); no licence is itself a prohibited act (Art 9); red means stop.
- **D03**: the Cambodian e-visa works only at Bavet, so the Châu Đốc river exit needs a Cambodian visa by another route — the one line v3 lacks.
- **Hospital ledger**: methanol (FCDO: licensed bars and shops in tourist areas; taste does not reveal it) — a failure-mode row and a rule (beer and sealed wine by default; spirits only where the supply chain is the reputation).
- **Before You Fly box for Vietnamese Americans**: same-passport rule, child exit document, notarised consent for minors, the five-year exemption paper. Four verified keys, thin corpus — one page, marked ◇.
- Not for the book: street names, funerals, exotic menu words, allergies, mobility (experience/reference cell; the site has them).

Estimated v4 delta: **+5 to +7 pages**, no retractions, two new hooks.
