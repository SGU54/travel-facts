-- travel-facts/baliforamericans/baliforamericans-facts.sql
-- Append-only seed of every fact spanned in baliforamericans.com articles. Idempotent upserts.
-- scope = 'bali' = SITE.dbSchema. The DB value REPLACES the span text at render, so each key has one canonical wording.

-- Batch-01 — 2026-10-13

-- visa.type — do-americans-need-a-visa-for-bali
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'visa.type', '"buy it online in advance or at the airport on arrival"'::jsonb, 'verified', now(),
        'https://travel.state.gov/en/international-travel/travel-advisories/indonesia.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- visa.activities_allowed — do-americans-need-a-visa-for-bali
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'visa.activities_allowed', '"selling goods or services, or being paid by anyone in Indonesia"'::jsonb, 'verified', now(),
        'https://evisa.imigrasi.go.id/web/visa-selection')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- visa.fee — do-americans-need-a-visa-for-bali
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'visa.fee', '"IDR 500,000"'::jsonb, 'verified', now(),
        'https://ngurahrai.imigrasi.go.id/layanan-wna/')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- visa.max_stay_days — do-americans-need-a-visa-for-bali
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'visa.max_stay_days', '"30 days, extendable once for another 30 days"'::jsonb, 'verified', now(),
        'https://evisa.imigrasi.go.id/web/visa-selection')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- visa.overstay_penalty — do-americans-need-a-visa-for-bali
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'visa.overstay_penalty', '"IDR 1,000,000 per day"'::jsonb, 'verified', now(),
        'https://travel.state.gov/en/international-travel/travel-advisories/indonesia.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- visa.extension_fee — do-americans-need-a-visa-for-bali
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'visa.extension_fee', '"IDR 500,000 per application"'::jsonb, 'verified', now(),
        'https://www.imigrasi.go.id/biaya_imigrasi/index')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- visa.validity_to_enter — do-americans-need-a-visa-for-bali
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'visa.validity_to_enter', '"90 days"'::jsonb, 'verified', now(),
        'https://evisa.imigrasi.go.id/web/visa-selection')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- documents.passport_validity — do-americans-need-a-visa-for-bali
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'documents.passport_validity', '"6 months beyond your arrival date and have 2 blank pages"'::jsonb, 'verified', now(),
        'https://id.usembassy.gov/bali/')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- documents.emergency_passport — do-americans-need-a-visa-for-bali
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'documents.emergency_passport', '"a visa obtained before arrival"'::jsonb, 'verified', now(),
        'https://id.usembassy.gov/bali/')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- documents.onward_ticket — do-americans-need-a-visa-for-bali
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'documents.onward_ticket', '"an outbound ticket from Indonesia"'::jsonb, 'verified', now(),
        'https://evisa.imigrasi.go.id/web/visa-selection')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- visa.tourist_levy — do-americans-need-a-visa-for-bali
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'visa.tourist_levy', '"IDR 150,000 per person"'::jsonb, 'verified', now(),
        'https://travel.state.gov/en/international-travel/travel-advisories/indonesia.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- visa.tourist_levy_terms — bali-tourist-levy-explained
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'visa.tourist_levy_terms', '"once per trip"'::jsonb, 'verified', now(),
        'https://lovebali.baliprov.go.id/faq')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- visa.tourist_levy_exemptions — bali-tourist-levy-explained
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'visa.tourist_levy_exemptions', '"holders of diplomatic and official visas, transport crew, holders of Indonesian stay permits, and holders of family unification, student and golden visas"'::jsonb, 'verified', now(),
        'https://lovebali.baliprov.go.id/faq')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- visa.tourist_levy_enforcement — bali-tourist-levy-explained
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'visa.tourist_levy_enforcement', '"being refused service at tourist attractions"'::jsonb, 'verified', now(),
        'https://bmc.baliprov.go.id/news/11462')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- safety_health.medication_import — bringing-medication-into-bali
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'safety_health.medication_import', '"90 days'' use for prescribed medicine"'::jsonb, 'verified', now(),
        'https://sertifikasicdob.pom.go.id/wasdisobat/faq/')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- safety_health.drug_laws — bringing-medication-into-bali
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'safety_health.drug_laws', '"some prescription medications, including those for ADHD, are illegal in Indonesia"'::jsonb, 'verified', now(),
        'https://travel.state.gov/en/international-travel/travel-advisories/indonesia.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- customs.alcohol_allowance — bali-customs-alcohol-and-vape-rules
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'customs.alcohol_allowance', '"1 liter of alcohol"'::jsonb, 'verified', now(),
        'https://www.beacukai.go.id/barang-penumpang')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- customs.duty_free_goods_value — bali-customs-alcohol-and-vape-rules
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'customs.duty_free_goods_value', '"USD 500 per person per arrival"'::jsonb, 'verified', now(),
        'https://www.beacukai.go.id/barang-penumpang')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- customs.tobacco_allowance — bali-customs-alcohol-and-vape-rules
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'customs.tobacco_allowance', '"200 cigarettes, or 25 cigars, or 100 grams of tobacco"'::jsonb, 'verified', now(),
        'https://www.beacukai.go.id/barang-penumpang')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- customs.vape_allowance — bali-customs-alcohol-and-vape-rules
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'customs.vape_allowance', '"30 ml of open-system liquid, or 12 ml of closed-system liquid"'::jsonb, 'verified', now(),
        'https://www.beacukai.go.id/barang-penumpang')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- customs.excess_destroyed — bali-customs-alcohol-and-vape-rules
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'customs.excess_destroyed', '"destroyed on the spot by the customs officer"'::jsonb, 'verified', now(),
        'https://www.beacukai.go.id/barang-penumpang')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- customs.cash_declaration — bali-customs-alcohol-and-vape-rules
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'customs.cash_declaration', '"IDR 100,000,000 or more"'::jsonb, 'verified', now(),
        'https://www.beacukai.go.id/faq-impor-pembawaan-uang-tunai')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- getting_around.driving_permit — renting-a-scooter-in-bali
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'getting_around.driving_permit', '"a US driver''s license alone is not recognized in Indonesia"'::jsonb, 'verified', now(),
        'https://travel.state.gov/en/international-travel/travel-advisories/indonesia.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- getting_around.licence_must_match_vehicle — renting-a-scooter-in-bali
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'getting_around.licence_must_match_vehicle', '"a license matching the type of vehicle driven"'::jsonb, 'verified', now(),
        'https://jdih.kemenkeu.go.id/api/download/fulltext/2009/22TAHUN2009UU.htm')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- getting_around.traffic_penalties — renting-a-scooter-in-bali
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'getting_around.traffic_penalties', '"4 months'' detention or a fine of IDR 1,000,000 for riding without the required license"'::jsonb, 'verified', now(),
        'https://jdih.kemenkeu.go.id/api/download/fulltext/2009/22TAHUN2009UU.htm')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- Batch-02 — 2026-10-13

-- safety_health.advisory_level — is-bali-safe
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'safety_health.advisory_level', '"Level 2, Exercise increased caution"'::jsonb, 'verified', now(),
        'https://travel.state.gov/en/international-travel/travel-advisories/indonesia.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- safety_health.zika_notice — is-bali-safe
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'safety_health.zika_notice', '"Level 2 travel health notice for Zika in Bali"'::jsonb, 'verified', now(),
        'https://wwwnc.cdc.gov/travel/destinations/traveler/none/indonesia')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- safety_health.malaria — is-bali-safe
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'safety_health.malaria', '"no malaria transmission in the resort areas of Bali, in Ubud, or in the Gili Islands"'::jsonb, 'verified', now(),
        'https://wwwnc.cdc.gov/travel/destinations/traveler/none/indonesia')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- safety_health.emergency_numbers — is-bali-safe
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'safety_health.emergency_numbers', '"112 for the unified emergency line, 110 for police, 119 for an ambulance and 113 for fire"'::jsonb, 'verified', now(),
        'https://diskominfo.badungkab.go.id/artikel/49056-call-center-112-kabupaten-badung')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- safety_health.us_consular_agency_bali — is-bali-safe
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'safety_health.us_consular_agency_bali', '"+62-361-233-605"'::jsonb, 'verified', now(),
        'https://travel.state.gov/en/international-travel/travel-advisories/indonesia.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- culture.tourist_circular — bali-rules-for-tourists
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'culture.tourist_circular', '"Governor''s Circular No. 7 of 2025"'::jsonb, 'verified', now(),
        'https://bmc.baliprov.go.id/news/11462')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- when_to_go.nyepi_2027 — nyepi-bali-day-of-silence
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'when_to_go.nyepi_2027', '"Monday, March 8, 2027"'::jsonb, 'verified', now(),
        'https://setneg.go.id/baca/index/inilah_skb_3_menteri_libur_nasional_dan_cuti_bersama_2027')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- when_to_go.nyepi_data_shutdown — nyepi-bali-day-of-silence
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'when_to_go.nyepi_data_shutdown', '"24 hours, from 6 a.m. to 6 a.m."'::jsonb, 'verified', now(),
        'https://cloud-ng.baliprov.go.id/landing-baliprov/2026/03/Nomor-2-Tahun-2026-SE-Menteri-tentang-Himbauan-Untuk-Melaksanakan-Seruan-bersama-tentang-Pelaksanaan-Rangkaian-Hari-Suci-Nyepi-Tahun-Caka-1948-di-Provinsi-Bali-Tahun-2026.pdf')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- safety_health.vaccines — vaccines-and-animal-bites-in-bali
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'safety_health.vaccines', '"hepatitis A, hepatitis B and typhoid"'::jsonb, 'verified', now(),
        'https://wwwnc.cdc.gov/travel/destinations/traveler/none/indonesia')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- Batch-03 — 2026-10-13

-- money.qr_payments_us — money-in-bali-cash-cards-atms
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'money.qr_payments_us', '"Thailand, Malaysia, Singapore, Japan, South Korea and China"'::jsonb, 'verified', now(),
        'https://www.bi.go.id/id/fungsi-utama/sistem-pembayaran/ritel/kanal-layanan/qris/qris-antarnegara/default.aspx')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- money.bill_tax_badung — money-in-bali-cash-cards-atms
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'money.bill_tax_badung', '"10%"'::jsonb, 'verified', now(),
        'https://bapenda.badungkab.go.id/storage/bapenda/file/Surat%20Edaran%20No.973.14315%20Bapenda.pdf')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- connectivity.phone_registration — indonesia-phone-registration-for-tourists
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'connectivity.phone_registration', '"up to 90 days"'::jsonb, 'verified', now(),
        'https://www.beacukai.go.id/faq-impor-registrasi-imei')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- Batch-04 — 2026-10-13

-- visa.extension_process — extending-a-bali-visa-on-arrival
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'visa.extension_process', '"a photograph and an interview at an immigration office"'::jsonb, 'verified', now(),
        'https://imigrasi.go.id/siaran_pers/2025/05/28/tekan-angka-pelanggaran-keimigrasian-wna-wajib-ke-kantor-imigrasi-untuk-perpanjangan-izin-tinggal')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- safety_health.narcotics_law_penalties — indonesia-drug-laws-for-travelers
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'safety_health.narcotics_law_penalties', '"4 to 12 years in prison"'::jsonb, 'verified', now(),
        'https://e-pharm.kemkes.go.id/front/pdf/UU352009.pdf')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- safety_health.methanol_poisoning — arak-and-methanol-in-bali
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'safety_health.methanol_poisoning', '"1 to 72 hours"'::jsonb, 'verified', now(),
        'https://www.cdc.gov/yellow-book/hcp/environmental-hazards-risks/poisonings-envenomations-and-toxic-exposures-during-travel.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- Batch-08 — 2026-10-13

-- when_to_go.climate_normals — best-time-to-visit-bali
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('bali', 'when_to_go.climate_normals', '"about 1 inch of rain in July and about 14 inches in January"'::jsonb, 'verified', now(),
        'https://ds.data.jma.go.jp/gmd/tcc/tcc/products/climate/normal/parts/NrmMonth_e.php?stn=97230')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;
