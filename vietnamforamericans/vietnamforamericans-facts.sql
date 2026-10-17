-- travel-facts/vietnamforamericans/vietnamforamericans-facts.sql
-- Append-only seed of every fact spanned in vietnamforamericans.com article batches.
-- Run in the Supabase SQL editor with the SERVICE ROLE (anon is RLS-blocked by design).
-- Idempotent: safe to re-run the whole file any time.
--
-- scope = 'vietnam' = SITE.dbSchema, NOT the folder name. Wrong scope orphans every row.
-- Every string literal doubles its single quotes (Postgres escaping).

-- Batch-01 — 2026-10-12 (post second-gate round 2; facts.json corrected in 6 places)

-- documents.passport_validity — do-americans-need-a-visa-for-vietnam
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'documents.passport_validity', '"six months'' validity beyond your arrival date"'::jsonb, 'verified', now(),
        'https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Vietnam.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- safety.advisory_level — is-vietnam-safe-for-americans
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'safety.advisory_level', '"Level 1 — Exercise Normal Precautions"'::jsonb, 'verified', now(),
        'https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Vietnam.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- safety.consular_access — is-vietnam-safe-for-americans
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'safety.consular_access', '"routinely delayed, often by several weeks"'::jsonb, 'verified', now(),
        'https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Vietnam.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- safety.drug_laws — is-vietnam-safe-for-americans
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'safety.drug_laws', '"substances used legally in another country can still lead to arrest in Vietnam"'::jsonb, 'verified', now(),
        'https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Vietnam.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- safety.emergency_numbers — is-vietnam-safe-for-americans
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'safety.emergency_numbers', '"113 for traffic police, 115 for an ambulance"'::jsonb, 'verified', now(),
        'https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Vietnam.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- safety.main_risk — is-vietnam-safe-for-americans
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'safety.main_risk', '"petty crime is common, especially in popular tourist locations"'::jsonb, 'verified', now(),
        'https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Vietnam.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- safety.malaria — vietnam-health-and-vaccines
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'safety.malaria', '"no transmission in Hanoi, Ho Chi Minh City, Da Nang, Hai Phong, Nha Trang or Quy Nhon"'::jsonb, 'verified', now(),
        'https://wwwnc.cdc.gov/travel/destinations/traveler/none/vietnam')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- safety.uxo — is-vietnam-safe-for-americans
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'safety.uxo', '"landmine risk is low in urban and populated areas, including tourist destinations"'::jsonb, 'verified', now(),
        'https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Vietnam.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- safety.vaccines_recommended — vietnam-health-and-vaccines
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'safety.vaccines_recommended', '"Hepatitis A, Hepatitis B, and typhoid for most travelers"'::jsonb, 'verified', now(),
        'https://wwwnc.cdc.gov/travel/destinations/traveler/none/vietnam')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- safety.vaccines_required — vietnam-health-and-vaccines
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'safety.vaccines_required', '"no proof of vaccination is needed at the border"'::jsonb, 'verified', now(),
        'https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Vietnam.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- transport.driving_licence — is-vietnam-safe-for-americans
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'transport.driving_licence', '"invalid in Vietnam"'::jsonb, 'verified', now(),
        'https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Vietnam.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- transport.driving_penalty — renting-a-motorbike-in-vietnam
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'transport.driving_penalty', '"a fine, arrest, or jail"'::jsonb, 'verified', now(),
        'https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Vietnam.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- transport.traffic_laws — renting-a-motorbike-in-vietnam
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'transport.traffic_laws', '"zero alcohol while driving"'::jsonb, 'verified', now(),
        'https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Vietnam.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- transport.unlicensed_insurance — renting-a-motorbike-in-vietnam
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'transport.unlicensed_insurance', '"your travel insurance may not pay your medical bills"'::jsonb, 'verified', now(),
        'https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Vietnam.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- visa.entry_gates — do-americans-need-a-visa-for-vietnam
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'visa.entry_gates', '"every international airport in Vietnam"'::jsonb, 'verified', now(),
        'https://en.baochinhphu.vn/viet-nam-adds-41-international-border-gates-for-e-visa-holders.htm')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- visa.fee — do-americans-need-a-visa-for-vietnam
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'visa.fee', '"$25 for single entry or $50 for multiple entry"'::jsonb, 'verified', now(),
        'https://vn.usembassy.gov/vietnamese-visas-and-entry-exit/')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- visa.max_stay_days — do-americans-need-a-visa-for-vietnam
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'visa.max_stay_days', '"90 days"'::jsonb, 'verified', now(),
        'https://evisa.gov.vn/faq')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- visa.passport_validity_rule — do-americans-need-a-visa-for-vietnam
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'visa.passport_validity_rule', '"30 days shorter than your passport''s remaining validity"'::jsonb, 'verified', now(),
        'https://evisa.gov.vn/faq')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- visa.phu_quoc_exception — do-americans-need-a-visa-for-vietnam
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'visa.phu_quoc_exception', '"30 days or less on the island of Phu Quoc"'::jsonb, 'verified', now(),
        'https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Vietnam.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- visa.processing_time — do-americans-need-a-visa-for-vietnam
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'visa.processing_time', '"3 to 5 working days"'::jsonb, 'verified', now(),
        'https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Vietnam.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- ============================================================
-- Batch-02 — 2026-10-12 (customs allowances, Decree 134/2016/ND-CP via customs.gov.vn)
-- Appended; batch-01 block above is unchanged.
-- ============================================================

-- customs.alcohol — vietnam-customs-and-duty-free-rules
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'customs.alcohol', '"1.5 litres of spirits at 20% ABV or above, or 2 litres under 20%, or 3 litres of beer"'::jsonb, 'verified', now(),
        'https://www.customs.gov.vn/index.jsp?pageId=2311&id=84471&cid=4203')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- customs.alcohol_overflow — vietnam-customs-and-duty-free-rules
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'customs.alcohol_overflow', '"A single bottle that goes over the limit by no more than one litre passes duty-free in its entirety"'::jsonb, 'verified', now(),
        'https://www.customs.gov.vn/index.jsp?pageId=2311&id=84471&cid=4203')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- customs.goods_value — vietnam-customs-and-duty-free-rules
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'customs.goods_value', '"a total customs value of 10,000,000 dong per entry"'::jsonb, 'verified', now(),
        'https://www.customs.gov.vn/index.jsp?pageId=2311&id=84471&cid=4203')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- customs.prohibited_list — vietnam-customs-and-duty-free-rules
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'customs.prohibited_list', '"changed on 5 September 2026, when Decree 292/2026 replaced Decree 69/2018"'::jsonb, 'verified', now(),
        'https://www.customs.gov.vn/index.jsp?pageId=2311&id=84471&cid=4203')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- customs.tobacco — vietnam-customs-and-duty-free-rules
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'customs.tobacco', '"200 cigarettes, or 250 grams of shredded tobacco, or 20 cigars"'::jsonb, 'verified', now(),
        'https://www.customs.gov.vn/index.jsp?pageId=2311&id=84471&cid=4203')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- customs.traveller_chooses — vietnam-customs-and-duty-free-rules
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'customs.traveller_chooses', '"if you are over the allowance, you choose which items count inside it and which are declared"'::jsonb, 'verified', now(),
        'https://www.customs.gov.vn/index.jsp?pageId=2311&id=84471&cid=4203')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- documents.currency_declaration — vietnam-customs-and-duty-free-rules
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'documents.currency_declaration', '"more than 15,000,000 dong, or more than 5,000 US dollars in foreign currency"'::jsonb, 'verified', now(),
        'https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Vietnam.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- documents.exit_control — vietnam-visa-extension-guide
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'documents.exit_control', '"including a medical emergency, you will likely pay overstay fines and face delays getting permission to leave"'::jsonb, 'verified', now(),
        'https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Vietnam.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- visa.no_extension_in_country — vietnam-visa-extension-guide
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'visa.no_extension_in_country', '"Vietnam does not allow you to renew or extend an e-visa while you are in the country"'::jsonb, 'verified', now(),
        'https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Vietnam.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- ============================================================
-- batch-03 — 2026-10-12 (appended)
-- ============================================================

-- safety.air_quality — best-time-to-visit-vietnam
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'safety.air_quality', '"air pollution is a significant problem in Vietnam’s major cities, especially Hanoi"'::jsonb, 'verified', now(),
        'https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Vietnam.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- ============================================================
-- batch-04 — 2026-10-12 (appended)
-- ============================================================

-- identity.timezone — flights-to-vietnam-from-us
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'identity.timezone', '"Vietnam has a single time zone and does not observe daylight saving"'::jsonb, 'verified', now(),
        'https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Vietnam.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- ============================================================
-- batch-06 — 2026-10-12 (appended)
-- ============================================================

-- documents.police_registration — where-to-stay-in-hanoi
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'documents.police_registration', '"every visitor must have their overnight address registered with the local police"'::jsonb, 'verified', now(),
        'https://vn.usembassy.gov/vietnamese-visas-and-entry-exit/')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- ============================================================
-- batch-20 — 2026-10-12 (appended)
-- ============================================================

-- visa.port_must_match — vietnam-and-cambodia-combined-itinerary
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'visa.port_must_match', '"The entry and exit location on an e-visa must match the port chosen in the application"'::jsonb, 'verified', now(),
        'https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Vietnam.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- ============================================================
-- batch-21 — 2026-10-17 (appended)
-- ============================================================

-- transport.no_licence_prohibited_act — ha-giang-loop-ride-pillion-or-car
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'transport.no_licence_prohibited_act', '"driving without the licence the law requires is itself a listed prohibited act"'::jsonb, 'verified', now(),
        'https://english.luatvietnam.vn/an-ninh-trat-tu/law-on-road-traffic-order-and-safety-2024-no-36-2024-qh15-360844-d1.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- transport.helmets_all_riders — ha-giang-loop-ride-pillion-or-car
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'transport.helmets_all_riders', '"every rider and every passenger on a motorbike must wear a helmet with the chin strap fastened"'::jsonb, 'verified', now(),
        'https://english.luatvietnam.vn/an-ninh-trat-tu/law-on-road-traffic-order-and-safety-2024-no-36-2024-qh15-360844-d1.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- services.son_doong_expedition — phong-nha-which-cave-tour
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'services.son_doong_expedition', '"a six-day, five-night expedition priced at VND 80,000,000, about USD 3,000, per person"'::jsonb, 'verified', now(),
        'https://oxalisadventure.com/cave/son-doong-cave/')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- transport.hanoi_halong_drive — two-days-from-hanoi-halong-or-ninh-binh
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'transport.hanoi_halong_drive', '"about 2.5 hours since the expressway and the Bach Dang bridge opened in 2018"'::jsonb, 'verified', now(),
        'https://hanoitimes.vn/ha-long-hai-phong-expressway-officially-opens-to-traffic-470.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- transport.halong_boat_suspensions — two-days-from-hanoi-halong-or-ninh-binh
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'transport.halong_boat_suspensions', '"the provincial waterways port authority stops issuing departure permits to every tourist vessel, day boats and overnight cruises alike"'::jsonb, 'verified', now(),
        'https://voh.com.vn/xa-hoi/tam-dung-toan-bo-tau-du-lich-tren-vinh-ha-long-do-bao-so-3-606092.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- ============================================================
-- batch-22 — 2026-10-17 (appended)
-- ============================================================

-- safety.methanol — counterfeit-spirits-drinking-safely
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'safety.methanol', '"deaths and serious illness from drinks containing methanol, bought in licensed bars, shops and hotels in tourist areas"'::jsonb, 'verified', now(),
        'https://www.gov.uk/foreign-travel-advice/vietnam/safety-and-security')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- services.medical_facilities_hanoi — counterfeit-spirits-drinking-safely
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'services.medical_facilities_hanoi', '"Family Medical Practice, International SOS and Raffles Medical as English-speaking clinics with emergency medicine"'::jsonb, 'verified', now(),
        'https://www.gov.uk/government/publications/list-of-medical-facilities-in-vietnam/list-of-medical-facilities-in-hanoi-and-northern-provinces')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- transport.cambodia_evisa_ports — mekong-delta-beyond-can-tho
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'transport.cambodia_evisa_ports', '"Crossing into Cambodia on a Cambodian e-visa works only at Bavet, the road crossing on the Ho Chi Minh City to Phnom Penh bus route"'::jsonb, 'verified', now(),
        'https://recberlin.mfaic.gov.kh/en-us/border-crossings')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- ============================================================
-- batch-23 — 2026-10-17 (appended)
-- ============================================================

-- visa.overseas_vietnamese_exemption — returning-to-vietnam-vietnamese-american
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'visa.overseas_vietnamese_exemption', '"a visa-exemption paper valid for up to five years, with a six-month stay on each entry"'::jsonb, 'verified', now(),
        'https://english.luatvietnam.vn/decree-no-82-2015-nd-cp-dated-september-24-2015-of-the-government-prescribing-visa-exemption-for-overseas-vietnamese-and-foreigners-who-are-spouses-98640-doc1.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- documents.same_passport — returning-to-vietnam-vietnamese-american
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'documents.same_passport', '"enter and exit Vietnam on the same passport, and travel domestically on the passport you entered with"'::jsonb, 'verified', now(),
        'https://travel.state.gov/en/international-travel/travel-advisories/vietnam.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- documents.child_exit — returning-to-vietnam-vietnamese-american
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'documents.child_exit', '"a Vietnamese passport or a Vietnamese exit visa is required by the Vietnamese government in the event your child needs to exit Vietnam"'::jsonb, 'verified', now(),
        'https://vn.usembassy.gov/vietnamese-visas-and-entry-exit/')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- documents.minor_exit_consent — returning-to-vietnam-vietnamese-american
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'documents.minor_exit_consent', '"notarised consent is required for every Vietnamese minor, including dual US citizens, to travel without a parent or guardian"'::jsonb, 'verified', now(),
        'https://travel.state.gov/en/international-travel/travel-advisories/vietnam.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- documents.hotel_registration_law — returning-to-vietnam-vietnamese-american
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'documents.hotel_registration_law', '"the host must declare a foreign guest''s temporary residence to the local police within 12 hours of arrival, or 24 hours in remote areas"'::jsonb, 'verified', now(),
        'https://english.luatvietnam.vn/law-no-47-2014-qh13-on-entry-exit-transit-and-residence-of-foreigners-in-vietnam-87925-doc1.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- calendar.tet_dates — returning-to-vietnam-vietnamese-american
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'calendar.tet_dates', '"6 February 2027"'::jsonb, 'verified', now(),
        'https://www.hko.gov.hk/en/gts/time/calendar/text/files/T2027e.txt')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- transport.us_nonstop_routes — returning-to-vietnam-vietnamese-american
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('vietnam', 'transport.us_nonstop_routes', '"Vietnam Airlines'' San Francisco to Ho Chi Minh City flight"'::jsonb, 'verified', now(),
        'https://info.flightmapper.net/route/YY_SFO_SGN')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;
