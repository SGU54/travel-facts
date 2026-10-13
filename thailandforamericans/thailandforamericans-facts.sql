-- thailandforamericans — common.facts upsert
-- Run in the Supabase SQL editor with the service role.
-- Written 2026-09-19, after the visa rollback took effect on 15 Sep 2026.
--
-- Schema, read from supabase/common/SETUP_common.sql rather than assumed:
--   common.facts (scope, key, value jsonb, status, checked_at, source_url, note)
--   status must be one of 'verified' | 'provisional' | 'needs_review'
--   unique (scope, key)
--   scope is SITE.dbSchema  ->  'thailand'   (NOT 'thailandforamericans')
--
-- IMPORTANT, from apps/site/lib/facts.ts: a 'needs_review' fact is treated as
-- ABSENT and will not substitute, and the span's ENTIRE inner text is replaced
-- by the value. So each value below is written to read correctly inline in the
-- sentence that carries it.

insert into common.facts (scope, key, value, status, checked_at, source_url, note) values

 ('thailand', 'entry.visa_free_days',
  '"30 days"'::jsonb, 'verified', now(),
  'https://www.thaievisa.go.th/',
  'In force 15 Sep 2026: the 60-day exemption introduced in 2024 was rolled back to 30 days for most nationalities including the US. Cabinet 19 May 2026; Ministry of Interior notices in the Royal Gazette 31 Aug 2026. The "admitted until" stamp is what governs on the day.'),

 ('thailand', 'entry.visa_free_extension',
  '"one 30-day extension at an immigration office, about 1,900 baht"'::jsonb,
  'provisional', now(),
  'https://www.immigration.go.th/',
  'Applied for inside Thailand before the current permission expires; approval is at immigration discretion. Gives roughly 60 days maximum per entry. Fee is commonly cited rather than officially published, hence provisional.'),

 ('thailand', 'entry.land_border_limit',
  '"two visa-exempt entries per calendar year"'::jsonb,
  'provisional', now(),
  'https://www.immigration.go.th/',
  'New with the 15 Sep 2026 rules and applies to LAND borders only; arrivals by air and sea are not limited. Does not affect a normal fly-in holiday. Provisional: one source states it explicitly, a second is silent on it.'),

 ('thailand', 'money.atm_fee',
  '{"min":220,"max":350,"unit":"฿"}'::jsonb,
  'provisional', now(), null,
  'Flat per-withdrawal foreign-card fee, no longer one number: ~250฿ on Visa, up to ~350฿ on Mastercard at the same machine, some banks still 220, AEON (in Big C and Lotus''s) about 150. Renders as "฿220–350" via factValueToText''s min/max form, which reads correctly in both money-in-thailand-guide sentences ("a fee of about ... per transaction"). Referenced by data-fact="money.atm_fee"; the key did not exist before today, so those spans had only ever shown their fallback of 220฿.')

on conflict (scope, key) do update
  set value      = excluded.value,
      status     = excluded.status,
      checked_at = now(),
      source_url = excluded.source_url,
      note       = excluded.note,
      updated_at = now();

-- verify
select key, value, status, checked_at
  from common.facts
 where scope = 'thailand'
 order by key;
