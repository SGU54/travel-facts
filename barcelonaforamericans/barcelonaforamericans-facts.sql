-- barcelonaforamericans-facts.sql
-- Append-only idempotent seed for common.facts (scope: barcelona).
-- Run against the shared fleet Supabase project (schema: common), e.g. via the
-- Supabase SQL editor or `psql`. Safe to re-run: ON CONFLICT (scope, key) upserts.
--
-- FIXED 2026-09-10 (first run attempt failed): common.facts' facts_status_check
-- constraint only allows 'verified' | 'provisional' | 'needs_review' — this file
-- originally used facts.json's own status vocabulary ('verify_recommended',
-- 'agreed_stable'), which doesn't exist on this table. Confirmed via
-- `select pg_get_constraintdef(oid) from pg_constraint where conname =
-- 'facts_status_check'` in the Supabase SQL editor after the Postgres logs
-- showed the exact failing row. Both were remapped to 'provisional' (the
-- closest meaning: not independently source-verified yet). Since this was one
-- multi-row INSERT per batch, the constraint violation rolled back the WHOLE
-- batch — nothing was partially written before this fix.
--
-- Batch 1 — 2026-09-10: retrofit of the site's first 5 fact-DB-worthy articles
-- (bringing-medication-into-spain, transport-strikes-in-spain,
-- renting-a-car-in-spain-law-vs-desk, bringing-spanish-purchases-into-the-us,
-- e-scooters-in-barcelona-rules). These 14 keys are already spanned live in
-- those articles' content (<span class="fact" data-fact="...">) — lib/facts.ts
-- will substitute the current value here at render time; if this seed hasn't
-- run yet, the spans fail closed to their written fallback text (identical to
-- these values), so publishing this is safe at any time.

INSERT INTO common.facts (scope, key, value, status, source_url, note, checked_at)
VALUES
  ('barcelona', 'mobility.escooter_helmet_law_effective_date', '{"text": "February 1, 2025"}'::jsonb, 'verified',
   'https://www.barcelona.cat/mobilitat/en/safe-mobility',
   'Barcelona municipal VMP ordinance — helmet mandatory for every e-scooter rider since this date. Spanned x2 in e-scooters-in-barcelona-rules.',
   now()),

  ('barcelona', 'mobility.escooter_sidewalk_fine', '{"text": "€500"}'::jsonb, 'verified',
   'https://www.barcelona.cat/mobilitat/en/safe-mobility',
   'Fine for riding an e-scooter on a sidewalk/pedestrian area. Spanned x5 in e-scooters-in-barcelona-rules.',
   now()),

  ('barcelona', 'mobility.escooter_bike_lane_speed_limit', '{"text": "25 km/h"}'::jsonb, 'verified',
   'https://www.barcelona.cat/mobilitat/en/safe-mobility',
   'Max speed on road-level bike lanes. Spanned x2.',
   now()),

  ('barcelona', 'mobility.escooter_path_speed_limit', '{"text": "10 km/h"}'::jsonb, 'verified',
   'https://www.barcelona.cat/mobilitat/en/safe-mobility',
   'Max speed on pavement-level cycle paths and designated park routes. Spanned x3.',
   now()),

  ('barcelona', 'mobility.escooter_insurance_mandate_date', '{"text": "July 25, 2025"}'::jsonb, 'verified',
   'https://www.barcelona.cat/mobilitat/en/safe-mobility',
   'Date insurance became mandatory for e-scooter riders under Spain''s Automobile Insurance Act. Spanned x2.',
   now()),

  ('barcelona', 'transport.strike_minimum_service_range', '{"text": "50-75%"}'::jsonb, 'verified',
   'https://www.timeout.com/news/spain-train-strikes-what-are-your-rights-as-a-traveller-and-can-you-claim-compensation-020926',
   'Typical mandated minimum-service range for a rail strike under Royal Decree-Law 17/1977. Spanned x2 in transport-strikes-in-spain.',
   now()),

  ('barcelona', 'transport.strike_recent_ave_strike_capacity', '{"text": "73%"}'::jsonb, 'provisional',
   'https://www.timeout.com/news/spain-train-strikes-what-are-your-rights-as-a-traveller-and-can-you-claim-compensation-020926',
   'Capacity a specific recent AVE/long-distance strike ran at — a dated example, not a standing rule; re-verify or retire at next check. Spanned x1.',
   now()),

  ('barcelona', 'transport.strike_cercanias_peak_service', '{"text": "75%"}'::jsonb, 'verified',
   'https://www.timeout.com/news/spain-train-strikes-what-are-your-rights-as-a-traveller-and-can-you-claim-compensation-020926',
   'Cercanías commuter minimum service during peak hours in a strike. Spanned x2.',
   now()),

  ('barcelona', 'transport.strike_cercanias_offpeak_service', '{"text": "50%"}'::jsonb, 'verified',
   'https://www.timeout.com/news/spain-train-strikes-what-are-your-rights-as-a-traveller-and-can-you-claim-compensation-020926',
   'Cercanías commuter minimum service off-peak in a strike. Spanned x2.',
   now()),

  ('barcelona', 'transport.strike_refund_window_days', '{"text": "30 days"}'::jsonb, 'verified',
   'https://www.timeout.com/news/spain-train-strikes-what-are-your-rights-as-a-traveller-and-can-you-claim-compensation-020926',
   'EU passenger-rights refund window for a strike-cancelled train. Spanned x2.',
   now()),

  ('barcelona', 'transport.bac_limit_standard', '{"text": "0.05%"}'::jsonb, 'verified', NULL,
   'Spain BAC limit for standard drivers, stricter than most US states. Spanned x1 in renting-a-car-in-spain-law-vs-desk.',
   now()),

  ('barcelona', 'transport.bac_limit_novice', '{"text": "0.03%"}'::jsonb, 'verified', NULL,
   'Spain BAC limit for novice drivers. Spanned x1.',
   now()),

  ('barcelona', 'customs.jamon_import_regulation_code', '{"text": "9 CFR 94.31"}'::jsonb, 'provisional',
   'https://www.aphis.usda.gov/sites/default/files/approved-spanish-ham-processing-plants.pdf',
   'US federal regulation banning personal-luggage import of cured Spanish ham. Primary regulation text itself did not parse cleanly this round (facts.json note) — re-verify citation directly on aphis.gov before promoting to verified. Spanned x1.',
   now()),

  ('barcelona', 'health.medication_personal_use_supply_limit', '{"text": "3-month"}'::jsonb, 'provisional',
   'https://www.aemps.gob.es/industria-farmaceutica/comercio-exterior/medicamentos-destinados-al-tratamiento-de-los-viajeros/?lang=en',
   'Personal-use medication supply cap for travelers (ordinary + controlled substances, same cap). Spanned x5 in bringing-medication-into-spain.',
   now()),

  ('barcelona', 'health.aemps_application_lead_time_days', '{"text": "10 days"}'::jsonb, 'verified',
   'https://www.aemps.gob.es/industria-farmaceutica/comercio-exterior/medicamentos-destinados-al-tratamiento-de-los-viajeros/?lang=en',
   'Minimum lead time to apply to AEMPS for a controlled-substance travel permit. Spanned x3.',
   now())

ON CONFLICT (scope, key) DO UPDATE SET
  value       = EXCLUDED.value,
  status      = EXCLUDED.status,
  source_url  = EXCLUDED.source_url,
  note        = EXCLUDED.note,
  checked_at  = EXCLUDED.checked_at,
  updated_at  = now();

-- Batch 2 — 2026-09-10: retrofit of the remaining 10 fact-DB-worthy articles
-- (ferries-barcelona-to-balearics, when-ferries-cancel-balearics,
-- what-closes-spanish-public-holidays, through-ticket-vs-separate-ticket-spain,
-- domestic-flights-in-spain, buying-ceramics-in-spain-getting-it-home,
-- pharmacies-clinics-er-barcelona, spain-hospital-billing-what-to-expect,
-- spain-insurance-exclusions-activities, if-you-have-an-accident-in-spain),
-- plus one retroactive addition to renting-a-car-in-spain-law-vs-desk (batch 1's
-- article) for transport.idp_cost_estimate, which turned out to be the same
-- literal "$20" AAA-permit figure already sitting in that article's prose too —
-- reused across both rather than creating a duplicate fact. 27 new keys, 41 spans.
--
-- NOTE on the two dated holiday keys: Barcelona's city council picks its own two
-- local holidays EVERY YEAR (the article says so explicitly — "not guaranteed to
-- repeat"), so barcelona_whit_monday_2026_date / barcelona_la_merce_2026_date are
-- year-scoped BY DESIGN — a real key/value pair to retire and replace with a
-- *_2027_date sibling next year, not a value the weekly checker should just
-- overwrite in place like an ordinary drifting fact.

INSERT INTO common.facts (scope, key, value, status, source_url, note, checked_at)
VALUES
  ('barcelona', 'ferries.mallorca_conventional_duration', '{"text": "6–8.5 hours"}'::jsonb, 'provisional', NULL,
   'Conventional (non-fast) ferry crossing time Barcelona → Palma de Mallorca. Panel-sourced, not independently fetched from an operator timetable — schedules drift by season. Spanned x2 in ferries-barcelona-to-balearics.',
   now()),

  ('barcelona', 'ferries.mallorca_fast_duration', '{"text": "2.5–3.5 hours"}'::jsonb, 'provisional', NULL,
   'Fast-ferry crossing time Barcelona → Palma de Mallorca, where offered. Spanned x2.',
   now()),

  ('barcelona', 'ferries.ibiza_duration', '{"text": "8–10 hour range"}'::jsonb, 'provisional', NULL,
   'Overnight conventional ferry crossing time Barcelona → Ibiza; no confirmed same-day fast option on this leg. Spanned x1.',
   now()),

  ('barcelona', 'ferries.menorca_conventional_duration', '{"text": "7–10 hours"}'::jsonb, 'provisional', NULL,
   'Conventional ferry crossing time Barcelona → Mahón (Menorca); route is seasonal, mostly summer. Spanned x1.',
   now()),

  ('barcelona', 'ferries.menorca_fast_duration', '{"text": "3.5–5.5 hours"}'::jsonb, 'provisional', NULL,
   'Fast-ferry crossing time Barcelona → Mahón (Menorca), where offered. Spanned x1.',
   now()),

  ('barcelona', 'ferries.peak_season_booking_lead_time', '{"text": "weeks to months ahead"}'::jsonb, 'provisional', NULL,
   'Recommended booking lead time for July–August Balearic ferry sailings, especially for a cabin or car space. Spanned x2.',
   now()),

  ('barcelona', 'ferries.eu_passenger_rights_regulation_number', '{"text": "1177/2010"}'::jsonb, 'verified',
   'https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32010R1177',
   'EU Regulation (EC) No 1177/2010 on the rights of passengers traveling by sea — governs ferry cancellation/delay refund and re-routing rights. Spanned x2 in when-ferries-cancel-balearics.',
   now()),

  ('barcelona', 'holidays.sant_jordi_date', '{"text": "April 23"}'::jsonb, 'verified', NULL,
   'Sant Jordi (book-and-rose festival) — a beloved civic celebration but explicitly NOT an official public holiday; shops/offices stay open. Fixed annual date. Spanned x2 in what-closes-spanish-public-holidays.',
   now()),

  ('barcelona', 'holidays.barcelona_whit_monday_2026_date', '{"text": "May 25"}'::jsonb, 'provisional', NULL,
   'One of Barcelona city council''s two self-designated local holidays for 2026. YEAR-SCOPED KEY — the council resets this annually; do not assume it repeats in 2027 without checking the current year''s designation. Spanned x2.',
   now()),

  ('barcelona', 'holidays.barcelona_la_merce_2026_date', '{"text": "September 24"}'::jsonb, 'provisional', NULL,
   'Barcelona''s own patron-saint festival, its biggest annual celebration — the second of the city council''s two self-designated local holidays for 2026. YEAR-SCOPED KEY, see whit_monday note above. Spanned x2.',
   now()),

  ('barcelona', 'holidays.sant_joan_date', '{"text": "June 24"}'::jsonb, 'verified', NULL,
   'Sant Joan / St John''s Day — Catalonia regional holiday, fixed annual date. Spanned x1.',
   now()),

  ('barcelona', 'holidays.diada_catalunya_date', '{"text": "September 11"}'::jsonb, 'verified', NULL,
   'Diada Nacional de Catalunya (National Day of Catalonia) — regional holiday, fixed annual date. Spanned x1.',
   now()),

  ('barcelona', 'holidays.sant_esteve_date', '{"text": "December 26"}'::jsonb, 'verified', NULL,
   'Sant Esteve / Boxing Day — Catalonia regional holiday, fixed annual date. Spanned x1.',
   now()),

  ('barcelona', 'transport.combinado_cercanias_validity_window', '{"text": "3-4 hours"}'::jsonb, 'verified',
   'https://www.seat61.com/train-travel-in-spain.htm',
   'Validity window (around the long-distance train''s departure/arrival) for the free connecting Cercanías ride bundled with a Renfe long-distance or iryo ticket. Spanned x2 in through-ticket-vs-separate-ticket-spain.',
   now()),

  ('barcelona', 'transport.flight_time_bcn_seville', '{"text": "1 hour 20 minutes"}'::jsonb, 'provisional', NULL,
   'Approximate Iberia/Vueling flight time Barcelona → Seville — general-knowledge estimate, not fetched from a live schedule. Spanned x2 in domestic-flights-in-spain.',
   now()),

  ('barcelona', 'transport.train_time_bcn_seville', '{"text": "5.5+ hours"}'::jsonb, 'provisional', NULL,
   'Approximate train time Barcelona → Seville (no direct high-speed line covers this route well). Spanned x1.',
   now()),

  ('barcelona', 'transport.train_time_bcn_valencia', '{"text": "under 2 hours"}'::jsonb, 'provisional', NULL,
   'Approximate AVE time Barcelona → Valencia. Spanned x1.',
   now()),

  ('barcelona', 'transport.train_time_bcn_madrid', '{"text": "2.5-3 hours"}'::jsonb, 'provisional', NULL,
   'Approximate AVE time Barcelona → Madrid, city-center to city-center. Spanned x1.',
   now()),

  ('barcelona', 'shopping.la_bisbal_distance_from_bcn', '{"text": "1.5-2 hours"}'::jsonb, 'provisional', NULL,
   'Approximate travel time from Barcelona to La Bisbal d''Empordà, Catalonia''s own ceramics town near Girona. Spanned x1 in buying-ceramics-in-spain-getting-it-home.',
   now()),

  ('barcelona', 'emergency.police_number', '{"text": "112"}'::jsonb, 'verified', NULL,
   'EU-wide emergency number (police/ambulance/fire), English-speaking operators. Spanned x4 in pharmacies-clinics-er-barcelona, x1 in spain-hospital-billing-what-to-expect, x5 in if-you-have-an-accident-in-spain.',
   now()),

  ('barcelona', 'transport.idp_cost_estimate', '{"text": "$20"}'::jsonb, 'provisional', NULL,
   'Approximate AAA fee for an International Driving Permit — a rough, unverified estimate (facts.json flags it as general knowledge, not independently priced this round). Spanned x1 in renting-a-car-in-spain-law-vs-desk, x1 in spain-insurance-exclusions-activities.',
   now())

ON CONFLICT (scope, key) DO UPDATE SET
  value       = EXCLUDED.value,
  status      = EXCLUDED.status,
  source_url  = EXCLUDED.source_url,
  note        = EXCLUDED.note,
  checked_at  = EXCLUDED.checked_at,
  updated_at  = now();

-- mobility.escooter_insurance_mandate_date already exists from Batch 1
-- (value "July 25, 2025") — spain-insurance-exclusions-activities reuses the
-- SAME key with a vaguer written fallback ("July 2025"); resolving it to the
-- more precise stored value is a strict improvement, not a conflict. No new
-- row needed here — Batch 1's upsert above already covers this key.

-- Batch 3 — 2026-09-10: retrofit extended to the ORIGINAL batch-1-15 corpus (72
-- articles, written before this session, pre-dating the fact-DB mechanism
-- entirely). Scanned all 72 for repeated point-value facts (prices, durations,
-- dates, percentages); found candidates in 27 articles. 52 new keys below, plus
-- 5 spans reusing the ALREADY-EXISTING eu.schengen_stay fact (scope 'eu', value
-- "90 days within any 180-day period") across etias-ees-americans-spain,
-- flights-to-barcelona-from-us and travel-insurance-spain-trip — no new row
-- needed for that one; this site's scope chain (SITE.factRegions = ['eu',
-- 'schengen']) already resolves it via packages/db/common.ts's factScopes().
--
-- IMPORTANT DISCOVERY: many of these articles already carry a SEPARATE,
-- pre-existing live mechanism for EUR amounts — <span class="feature-price"
-- data-amount="X" data-currency="EUR"> — which ArticleEnhancer.tsx uses to
-- append a live "(≈ $X today)" USD conversion client-side. That span's
-- data-amount attribute is NOT touched by lib/facts.ts's resolveContent(), so
-- nesting a span.fact inside/around a .feature-price span would let the two
-- mechanisms drift out of sync (the visible EUR text could update via the fact
-- DB while the USD conversion keeps computing off the stale data-amount). The
-- retrofit script explicitly skips any text node inside .feature-price —
-- every value below is spanned ONLY at its plain-text repeat mention(s)
-- elsewhere in the same article, never inside the existing live-price widget.
-- 19 of these 27 articles have at least one .feature-price span left
-- deliberately un-touched for this reason.
--
-- All statuses set to 'provisional' (not 'verified') — every value here was
-- extracted from already-published prose, not independently re-fetched from
-- an official source this session, unlike Batches 1-2's health/transport-law
-- facts. Some `note` fields flag genuine cross-article inconsistencies found
-- along the way (e.g. transit.taxi_airport_flat_fare vs bcn-airport-to-city's
-- taxi framing) — these are pre-existing content issues surfaced by this
-- retrofit, not something this SQL fixes; flag for editorial review.

INSERT INTO common.facts (scope, key, value, status, source_url, note, checked_at)
VALUES
  ('barcelona', 'transport.bus_time_bcn_tossa', '{"text":"90 minutes"}'::jsonb, 'provisional', NULL,
   'Direct bus travel time from Barcelona Estació del Nord to Tossa de Mar. Source: costa-brava-day-trip, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'transport.train_time_bcn_figueres', '{"text":"55 minutes"}'::jsonb, 'provisional', NULL,
   'Renfe train time Barcelona Sants to Figueres-Vilafant. Source: figueres-dali-day-trip, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'attraction.dali_museum_ticket_price', '{"text":"€18"}'::jsonb, 'provisional', NULL,
   'Dalí Theatre-Museum adult admission (includes the Dalí Jewels collection). Source: figueres-dali-day-trip, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'transport.train_time_figueres_girona', '{"text":"15 minutes"}'::jsonb, 'provisional', NULL,
   'Same high-speed line links Figueres-Vilafant and Girona; shared fact, spanned in both articles. Source: figueres-dali-day-trip / girona-day-trip, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'transport.train_time_bcn_girona_highspeed', '{"text":"38 minutes"}'::jsonb, 'provisional', NULL,
   'AVE/AVANT high-speed travel time Barcelona Sants to Girona. Source: girona-day-trip, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'transport.train_fare_bcn_girona_avant', '{"text":"€17"}'::jsonb, 'provisional', NULL,
   'AVANT one-way fare Barcelona-Girona (the value pick vs pricier AVE, same speed). Source: girona-day-trip, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'transport.train_fare_bcn_girona_regional', '{"text":"€11"}'::jsonb, 'provisional', NULL,
   'Slower regional (R/MD or R11) one-way fare Barcelona-Girona, no reservation needed. Source: girona-day-trip, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'transport.journey_time_bcn_montserrat', '{"text":"1.5 hours"}'::jsonb, 'provisional', NULL,
   'Whole journey time each way (train/cable-car or rack railway) Barcelona-Montserrat. Source: montserrat-day-trip, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'attraction.montserrat_train_rack_railway_price', '{"text":"€28.80"}'::jsonb, 'provisional', NULL,
   'Combined train + rack railway return fare, adult, all zones. Source: montserrat-day-trip, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'transport.train_time_bcn_sitges', '{"text":"35–45 minutes"}'::jsonb, 'provisional', NULL,
   'Commuter train travel time Barcelona to Sitges. Source: sitges-day-trip, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'transport.sitges_train_frequency', '{"text":"15–30 minutes"}'::jsonb, 'provisional', NULL,
   'Train frequency on the Barcelona-Sitges commuter line. Source: sitges-day-trip, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'transport.train_fare_bcn_sitges', '{"text":"€4.60"}'::jsonb, 'provisional', NULL,
   'One-way commuter train fare Barcelona-Sitges (Zone 4). Source: sitges-day-trip, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'transport.cruise_shuttle_fare_bcn', '{"text":"€3"}'::jsonb, 'provisional', NULL,
   'T3 Portbus/Cruise Bus shuttle one-way fare, cruise terminal to La Rambla. Source: one-day-in-barcelona-cruise, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'tax.tourist_tax_5star', '{"text":"€12.00"}'::jsonb, 'provisional', NULL,
   'Barcelona tourist tax per person per night, 5-star hotels. Article states these are the official figures. Source: barcelona-tourist-tax-explained (also best-hotels-first-timers-barcelona, luxury-hotels-barcelona), extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'tax.tourist_tax_4star', '{"text":"€8.40"}'::jsonb, 'provisional', NULL,
   'Barcelona tourist tax per person per night, 4-star hotels. Source: barcelona-tourist-tax-explained (also best-hotels-first-timers-barcelona), extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'tax.tourist_tax_effective_date', '{"text":"April 2026"}'::jsonb, 'provisional', NULL,
   'Date the current tourist-tax rates took effect (1 April 2026). Source: barcelona-tourist-tax-explained (also best-hotels-first-timers-barcelona, luxury-hotels-barcelona), extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'tax.tourist_tax_licensed_apartment', '{"text":"€9.50"}'::jsonb, 'provisional', NULL,
   'Barcelona tourist tax per person per night, licensed tourist apartments. Source: barcelona-tourist-tax-explained, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'tax.tourist_tax_hostel', '{"text":"€6.00"}'::jsonb, 'provisional', NULL,
   'Barcelona tourist tax per person per night, youth hostels. Source: barcelona-tourist-tax-explained, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'food.real_paella_cook_time', '{"text":"30–45 minutes"}'::jsonb, 'provisional', NULL,
   'Minimum genuine cook-to-order time for real paella (vs suspiciously fast tourist-trap paella). Source: paella-barcelona-tourist-traps, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'transit.tcasual_10_ride_price', '{"text":"€13"}'::jsonb, 'provisional', NULL,
   'T-casual 10-ride Zone 1 card price. Source: barcelona-metro-transit-guide, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'transit.tcasual_per_ride_price', '{"text":"€1.30"}'::jsonb, 'provisional', NULL,
   'Effective per-ride cost on a T-casual card. Source: barcelona-metro-transit-guide, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'transit.single_ride_fare', '{"text":"€2.65"}'::jsonb, 'provisional', NULL,
   'Single Zone 1 metro/bus ticket price. Source: barcelona-metro-transit-guide, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'transit.hola_barcelona_48h_price', '{"text":"€18"}'::jsonb, 'provisional', NULL,
   'Hola Barcelona unlimited-ride pass, 48-hour tier (includes airport). Source: barcelona-metro-transit-guide, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'transit.airport_ticket_price', '{"text":"€5.90"}'::jsonb, 'provisional', NULL,
   'Special Airport Ticket surcharge for the L9 Sud airport metro leg. Source: barcelona-metro-transit-guide, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'transit.zone1_transfer_window_minutes', '{"text":"75 minutes"}'::jsonb, 'provisional', NULL,
   'Free-transfer window on a single validated Zone 1 fare. Source: barcelona-metro-transit-guide, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'transit.aerobus_fare', '{"text":"€7.45"}'::jsonb, 'provisional', NULL,
   'Aerobús one-way fare, airport to Plaça de Catalunya. Source: bcn-airport-to-city, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'transit.r2_train_fare', '{"text":"€5"}'::jsonb, 'provisional', NULL,
   'R2 Nord commuter train fare, Terminal 2 to Sants/Passeig de Gràcia. Source: bcn-airport-to-city, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'transit.taxi_fare_airport_from', '{"text":"€30"}'::jsonb, 'provisional', NULL,
   'Lower end of the metered taxi fare range, airport to city center. Source: bcn-airport-to-city, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'transit.taxi_fare_airport_minimum', '{"text":"€21"}'::jsonb, 'provisional', NULL,
   'Official airport minimum taxi fare (makes very short hops cost the same). Source: bcn-airport-to-city, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'transit.taxi_incity_fare_low', '{"text":"€8"}'::jsonb, 'provisional', NULL,
   'Lower end of a typical in-city metered taxi fare range. Source: taxis-uber-car-barcelona, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'transit.taxi_airport_flat_fare', '{"text":"€39"}'::jsonb, 'provisional', NULL,
   'Flat-rate taxi fare zone from the airport to the center per this article. NOTE: differs from bcn-airport-to-city''s metered ~€30-45 / €21-minimum framing -- a pre-existing site inconsistency this retrofit surfaces but does not resolve. Source: taxis-uber-car-barcelona, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'transit.avlo_lowest_fare', '{"text":"€7"}'::jsonb, 'provisional', NULL,
   'Cheapest advance Avlo (Renfe budget brand) one-way fare, when booked far ahead. Source: trains-from-barcelona, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'transit.recommended_arrival_buffer_minutes', '{"text":"20–30 minutes"}'::jsonb, 'provisional', NULL,
   'Recommended arrival buffer before a high-speed departure (airport-style boarding/luggage scan). Source: trains-from-barcelona, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'event.pope_leo_xiv_barcelona_visit_dates', '{"text":"June 9–10"}'::jsonb, 'provisional', NULL,
   'Pope Leo XIV apostolic visit dates to Barcelona, June 2026 (Gaudí centenary). Source: barcelona-2026-gaudi-centenary, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'entry.etias_fee_estimate', '{"text":"€20"}'::jsonb, 'provisional', NULL,
   'Expected ETIAS authorization fee once launched (three-year validity), paid once. Source: etias-ees-americans-spain, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'money.recommended_cash_buffer', '{"text":"€20–40"}'::jsonb, 'provisional', NULL,
   'Recommended cash-on-hand buffer for small bars, market stalls, tips. Source: money-cards-tipping-barcelona, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'money.foreign_transaction_fee_typical', '{"text":"3%"}'::jsonb, 'provisional', NULL,
   'Typical foreign-transaction-fee surcharge many US cards charge (often waived on travel cards). Source: money-cards-tipping-barcelona, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'money.recommended_tip_percentage', '{"text":"5–10%"}'::jsonb, 'provisional', NULL,
   'Recommended tip for a nice dinner with good service in Barcelona (well below US norms). Source: money-cards-tipping-barcelona, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'insurance.recommended_medical_coverage_minimum', '{"text":"€30,000"}'::jsonb, 'provisional', NULL,
   'Common benchmark minimum medical coverage (the Schengen-visa standard, a useful floor for US tourists even though they''re visa-exempt). Source: travel-insurance-spain-trip, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'attraction.casa_batllo_base_ticket_price', '{"text":"€29"}'::jsonb, 'provisional', NULL,
   'Casa Batlló base online ticket, dynamic/tiered pricing starting point. Source: casa-batllo-vs-casa-mila, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'attraction.casa_mila_essential_ticket_price', '{"text":"€25"}'::jsonb, 'provisional', NULL,
   'Casa Milà (La Pedrera) Essential daytime ticket with audio guide, starting price. Source: casa-batllo-vs-casa-mila, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'attraction.park_guell_adult_ticket_price', '{"text":"€18"}'::jsonb, 'provisional', NULL,
   'Park Güell Monumental Zone adult timed-entry ticket. Source: park-guell-tickets-guide, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'attraction.park_guell_entry_window_minutes', '{"text":"30 minutes"}'::jsonb, 'provisional', NULL,
   'Entry window from a booked timed slot before the QR code expires. Source: park-guell-tickets-guide, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'attraction.sagrada_familia_base_ticket_price', '{"text":"€26"}'::jsonb, 'provisional', NULL,
   'Basic timed entry with audio guide, Sagrada Família. Source: sagrada-familia-tickets-guide, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'attraction.sagrada_familia_tower_access_addon', '{"text":"€10"}'::jsonb, 'provisional', NULL,
   'Tower access add-on over standard entry, Sagrada Família (Nativity or Passion facade). Shared fact, spanned in both articles. Source: sagrada-familia-tickets-guide / sagrada-familia-towers-guide, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'festival.la_merce_dates_range', '{"text":"September 23–27"}'::jsonb, 'provisional', NULL,
   'La Mercè festival date range, Barcelona''s biggest annual celebration (distinct from the single official city-council holiday day within it). Source: barcelona-festivals-events, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'attraction.articket_bcn_price', '{"text":"€38"}'::jsonb, 'provisional', NULL,
   'Articket BCN combined pass price (skip-the-line entry to six major art museums). Source: best-museums-barcelona, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'attraction.articket_bcn_validity', '{"text":"12 months"}'::jsonb, 'provisional', NULL,
   'Articket BCN pass validity window. Source: best-museums-barcelona, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'attraction.camp_nou_tour_price_low', '{"text":"€28"}'::jsonb, 'provisional', NULL,
   'Camp Nou / Barça Immersive Tour, lower end of ticket-tier pricing. Source: camp-nou-tour-guide, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'attraction.camp_nou_tour_price_high', '{"text":"€36"}'::jsonb, 'provisional', NULL,
   'Camp Nou / Barça Immersive Tour, upper end of ticket-tier pricing. Source: camp-nou-tour-guide, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'attraction.picasso_museum_ticket_price', '{"text":"€12"}'::jsonb, 'provisional', NULL,
   'Picasso Museum permanent-collection admission, starting price. Source: picasso-museum-barcelona, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now()),

  ('barcelona', 'attraction.picasso_museum_visit_duration', '{"text":"2 hours"}'::jsonb, 'provisional', NULL,
   'Recommended visit duration (1.5-2 hours), upper bound. Source: picasso-museum-barcelona, extracted from already-published prose (not independently re-verified against a live official source this session).',
   now())

ON CONFLICT (scope, key) DO UPDATE SET
  value       = EXCLUDED.value,
  status      = EXCLUDED.status,
  source_url  = EXCLUDED.source_url,
  note        = EXCLUDED.note,
  checked_at  = EXCLUDED.checked_at,
  updated_at  = now();
