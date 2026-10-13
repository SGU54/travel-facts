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
