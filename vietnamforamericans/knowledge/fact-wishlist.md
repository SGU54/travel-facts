# Fact wishlist — what the guidebooks quantify that facts.json does not

Purpose: the books' VALUES are stale, but the SET of things a guidebook bothers to pin down is a map of what travellers end up needing. facts.json (40 keys, 2026-10-12) is almost entirely entry/customs/safety from State Dept, CDC and Customs. The book quantifies ~60 things; most fall outside those categories. Each row below is a fact key we do not hold, the book's page that raised it, and the official or primary source that would settle it. Priority = how often our articles would cite it.

Status legend: **P1** cited by 5+ articles or a swamp · **P2** cited by 2–4 · **P3** nice to have.

## Money (none of these exist in facts.json)
| key | raised by | settle with | priority |
|---|---|---|---|
| money.legal_tender_and_usd_pricing | DK p254, p276 | State Bank of Vietnam circular on foreign-currency pricing/payment | P1 |
| money.hotel_vat_and_service_charge | DK p234 | Ministry of Finance VAT rate (temporary 8% in 2024–25); hotel-industry practice | P2 |
| money.exchange_counter_rules | DK p276 | SBV list of licensed exchange agents; legality of gold-shop exchange | P2 |
| money.atm_structural_rule | DK p276 | already corrections #1 — keep structural only; a bank's OWN foreign-card schedule would be the first primary source ever found | P1 |
| money.card_acceptance_structure | DK p276 | no primary source; mark as observation-grade | P2 |
| money.note_denominations_in_circulation | DK p277 | SBV banknote list (which notes are current, which polymer) — needed for the 20k/500k lookalike warning | P1 |
| money.dual_pricing_at_sites | DK p272 | ticket boards of Hue, Hoi An, My Son, Cu Chi (official site pages) | P2 |

## Time, season, calendar
| key | raised by | settle with | priority |
|---|---|---|---|
| calendar.public_holidays_current_year | DK p37 | Government holiday schedule (annual decision on Tet/National Day swap days) | P1 |
| calendar.tet_dates_next_3_years | DK p34 | lunar calendar; needed by tet-timing swamp and the planner | P1 |
| calendar.tet_closure_duration_structural | DK p34 | Labour Code (5 days off) + observed shop closures | P1 |
| climate.month_by_region_normals | DK p38–39 | NCHMF / WMO normals — geo.ts already holds tables; record the SOURCE | P1 |
| climate.typhoon_season_central | DK p38 | NCHMF; US Navy JTWC climatology | P2 |
| climate.hot_season_extremes | DK p38 | NCHMF | P3 |
| festivals.dated_list | DK p34–37 | provincial tourism boards per festival; Dalat Flower Festival biennial rule | P2 |

## Transport (facts.json has only licence/traffic-law keys)
| key | raised by | settle with | priority |
|---|---|---|---|
| transport.international_airports_list | DK p280 | ACV / CAAV list of international airports | P1 |
| transport.airport_to_city_distance_and_modes | DK p10, p11, p280 | ACV airport pages; Hanoi bus 86 / HCMC bus 109 operators; Grab | P1 |
| transport.us_nonstop_routes | DK p280 | vietnamairlines.com (already verified SFO–SGN only; make it a KEY, not a note) | P1 |
| transport.domestic_airlines_current | DK p282 | CAAV licensed carriers | P2 |
| transport.rail_hcmc_hanoi_duration_and_classes | DK p282 | dsvn.vn timetable + class list | P1 |
| transport.rail_train_numbering_direction | DK p282 | dsvn.vn (book parity claim disputed) | P3 |
| transport.rail_sapa_private_carriages | DK p282 | dsvn.vn + operator sites | P2 |
| transport.bus_booking_channels | DK p283 | Vexere / 12Go / Futa as current channels; no primary source beyond operators | P2 |
| transport.main_bus_stations_current | DK p283 | HCMC/Hanoi DoT: new Mien Dong, My Dinh, Nuoc Ngam, Giap Bat | P2 |
| transport.car_with_driver_requirement | DK p283, p285 | Road Traffic Law: foreigners' driving rights; corroborates driving_licence key from the hire side | P1 |
| transport.metro_lines_open | not in book (blind spot) | HCMC Metro Line 1 (Dec 2024), Hanoi 2A + 3 | P1 |
| transport.ride_hailing_legal_status | not in book | Decree on ride-hailing; Grab/Xanh SM/Be | P1 |
| transport.land_border_gates_for_evisa | DK p281 | already facts.json visa.entry_gates — add the per-gate NAMES as a sub-key | P2 |
| transport.cambodia_boat_crossing | DK p281 | Vinh Xuong gate on the e-visa list; operator schedules | P2 |
| transport.ferries_phu_quoc_cat_ba | DK p283, p185 | operator sites (Superdong, Phu Quoc Express; Cat Ba routes) | P2 |
| transport.helmet_and_pillion_law | DK p285 | Road Traffic Law 2024 (in force 2025) — extend getting_around.traffic_laws | P2 |

## Entry and documents (gaps beside the existing keys)
| key | raised by | settle with | priority |
|---|---|---|---|
| documents.hotel_passport_practice | DK p233 | US Embassy guidance; no law requires surrender — needed to answer "do I hand over my passport" | P1 |
| documents.arrival_card_abolished | DK p280 | Immigration Dept: confirm no paper card; pre-arrival e-declaration is the only form | P2 |
| customs.outbound_parcel_inspection | DK p278–279 | Vietnam Post / Customs export rules for personal parcels | P2 |
| customs.wildlife_products_export | DK p245 | CITES + US Fish & Wildlife import rules (the US side matters more) | P3 |
| customs.antiques_export_permit | not in book | Ministry of Culture rules on exporting antiques/artefacts — a real trap for buyers of "old" lacquer | P2 |

## Health (gaps beside CDC keys)
| key | raised by | settle with | priority |
|---|---|---|---|
| health.hospital_payment_up_front | DK p274 | US Embassy medical-assistance page (lists clinics; states payment expectations) | P1 |
| health.international_clinics_list | DK p274 | US Embassy list of medical facilities (Hanoi, HCMC, Danang) | P1 |
| health.dengue_current_guidance | DK p275 | CDC Vietnam page (vaccine stance) | P2 |
| health.tap_water | DK p275 | already disputed in disputes.md; CDC "do not drink tap water" line is citable | P1 |
| health.air_quality_live_source | facts.json notes it; no key | IQAir / US Embassy AirNow monitors as the named live source | P2 |

## Connectivity and daily life
| key | raised by | settle with | priority |
|---|---|---|---|
| connectivity.carriers_and_esim | DK p278 | Viettel / VinaPhone / MobiFone official tourist-SIM pages; eSIM support | P1 |
| connectivity.blocked_services | DK p278 | no primary source; observation-grade (some news sites); VPN legality | P3 |
| daily.electricity_plugs | DK p273 | IEC world plugs (A/C/F, 220 V 50 Hz) — turn the dispute into a verified key | P1 |
| daily.shop_and_market_hours_structural | DK p254 | market websites (Ben Thanh, Dong Xuan) — structural only | P3 |
| daily.toilet_paper_bin_rule | DK p275 | observation-grade; no source | P3 |
| daily.address_slash_convention | DK p279 | observation-grade; stable | P3 |
| daily.tipping_norms | DK p235, p243 | no primary source exists; keep as structural observation (already disputed) | P1 |

## Sights (prices the book printed that we would need live)
| key | raised by | settle with | priority |
|---|---|---|---|
| sights.hue_citadel_ticket | DK p272 | Hue Monuments Conservation Centre | P2 |
| sights.hoi_an_old_town_ticket | DK p272 | Hoi An tourism office | P2 |
| sights.my_son_ticket | DK p272 | official site | P2 |
| sights.cu_chi_ticket_and_hours | DK p11 | official site | P2 |
| sights.ho_chi_minh_mausoleum_hours_and_closure | DK p10 | mausoleum management board (annual autumn closure for maintenance) | P1 |
| sights.notre_dame_hcmc_restoration_status | DK p60 | Archdiocese of HCMC | P2 |
| sights.halong_bay_entry_fee | DK p185 | Quang Ninh provincial fee schedule | P2 |
| sights.perfume_pagoda_festival_window | DK p34 | Hanoi tourism; lunar dates | P3 |

## How to use this file
- Each P1 row is a candidate `facts.json` key for the next facts build (travel-empire Stage 2 / fleet facts checker). Add the key only when a primary source is found; otherwise it stays here.
- Rows marked "observation-grade" can never become verified facts; they become structural prose rules, like corrections #1.
- Later books (LP 2017, Moon, Insight) will add rows; keep the "raised by" column so provenance survives.

---

# Lonely Planet 2016 — additional fact keys (2026-10-16)

Rows LP quantifies that neither facts.json nor the DK list above holds.

| key | raised by | settle with | priority |
|---|---|---|---|
| transport.airport_access_fee_sgn | LP p357 (vehicle access ticket added to taxi fare) | ACV / SGN fee schedule | P2 |
| transport.airport_bus_routes_current | LP p19, p357 (routes 152/17 in 2016) | HCMC and Hanoi bus operators (109, 86 today) | P1 |
| transport.train_classes_and_berth_pricing | LP p496 (SE/TN; upper berth cheapest) | dsvn.vn | P1 |
| transport.train_booking_window_days | LP p497 (60–90 days) | dsvn.vn | P2 |
| transport.tet_train_suspension_days | LP p497 (nine days) | dsvn.vn annual notice | P1 |
| transport.train_child_fares | LP p496 (under 2 free, 2–9 half) | dsvn.vn | P2 |
| transport.bus_average_speed_structural | LP p492 (~50 km/h) | observation-grade; expressway list from MoT | P3 |
| transport.open_tour_operators_current | LP p493 | Sinh Tourist, Futa, Vexere listings | P2 |
| transport.land_gate_hours | LP p489 (7–5; Cambodia 8–8) | Immigration Dept gate list | P2 |
| transport.cambodia_laos_visa_on_arrival_rules | LP p489 | Cambodian e-visa / Lao VOA official pages | P1 |
| transport.china_border_rail_services | LP p491 (Hanoi–Nanning daily) | China Railway / dsvn.vn | P3 |
| transport.urban_speed_limit_and_right_on_red | LP p495 (50 km/h; no right on red) | Road Traffic Law 2024 | P2 |
| transport.seatbelt_law | LP p495 (none in 2016) | Road Traffic Law 2024 (now mandatory) | P2 |
| transport.helmet_passenger_rule | LP p495 | Road Traffic Law | P2 |
| transport.metro_lines_open | LP p357 box | HCMC Metro Line 1 (Dec 2024); Hanoi 2A, 3 | P1 |
| money.hotel_tax_service_structure | LP p479 ("++") | hotel practice; VAT law | P2 |
| money.dong_export_rule | LP p482 (cannot take dong out) | State Bank regulation on carrying VND across the border | P2 |
| money.card_surcharge_structural | LP p482 (~3%) | observation-grade | P3 |
| calendar.tet_date_window | LP p458 (19 Jan–20 Feb) | lunar calendar | P1 |
| calendar.hue_festival_format | LP p26 (biennial then; annual now) | huefestival.com | P2 |
| calendar.danang_fireworks_dates | LP p26 | DIFF official | P2 |
| health.dengue_hospitalisations_structural | LP p500 | WHO / MoH figures | P3 |
| health.state_hospital_foreigner_licence | LP p499 | MoH list of licensed facilities | P2 |
| health.private_clinics_list | LP p499 | US Embassy medical list | P1 (dup of earlier row; raise priority) |
| health.rabies_igg_availability | LP p501 | US Embassy / clinic info | P2 |
| health.ice_safety_structural | LP p500 | observation-grade; CDC tap-water line | P2 |
| safety.uxo_statistics | LP p484 (150,000 t; 40,000 casualties; Quang Tri) | MAG / VNMAC | P2 |
| safety.riptide_beaches_with_lifeguards | LP p479 | provincial beach management | P3 |
| daily.lunch_closure_hours | LP p483 (noon–1.30) | observation-grade | P3 |
| daily.museum_monday_closures | LP p55 | each museum | P2 |
| daily.mobile_carriers_and_tourist_sims | LP p484 (Viettel, Vinaphone, Mobifone) | carrier pages | P1 (dup; keep) |
| daily.homestay_licensing_rule | LP p478 | Ministry of Culture, Sports and Tourism | P2 |
| legal.lgbt_marriage_law_status | LP p481 (2015 law) | Law on Marriage and Family 2014 | P3 |
| culture.minority_population_share | LP p457 (14 m / 14%) | GSO census 2019 | P2 |
| culture.catholic_share | LP p459 (8–10%) | GSO census religion table | P3 |
