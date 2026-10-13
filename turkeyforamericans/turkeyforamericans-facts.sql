-- turkeyforamericans — common.facts seed
-- Run in the Supabase SQL editor with the service role.
-- Written 2026-09-23 after a fleet audit found 119 fact-span keys with no row
-- anywhere in Turkey's scope chain (factScopes = ['turkey','global']).
--
-- ONLY NINE ARE SEEDED, DELIBERATELY. Of those 119 keys:
--   · 93 carry DIFFERENT fallback text in different spans — paraphrases written
--     to fit each sentence, not values. facts.ts replaces the span's ENTIRE
--     inner text, so one value cannot serve both a mid-sentence clause and an
--     FAQ answer. Seeding those would break the prose it is meant to protect.
--     Example, money.contactless_availability, same article, two spans:
--       "Contactless payment is widely available, particularly in major cities…"
--       "Yes, widely, especially in cities and tourist areas…"
--   · of the 26 consistent ones, most are whole explanatory paragraphs tagged as
--     facts — a category error, not a value that ages.
--
-- What remains below is the set that is genuinely a VALUE, genuinely volatile,
-- and reads correctly wherever its span sits. Everything else is left on its
-- written fallback, which is what fail-closed is for.
--
-- Schema, read from supabase/common/SETUP_common.sql:
--   common.facts (scope, key, value jsonb, status, checked_at, source_url, note)
--   status ∈ 'verified' | 'provisional' | 'needs_review'  — needs_review NEVER substitutes
--   scope is SITE.dbSchema → 'turkey'

insert into common.facts (scope, key, value, status, checked_at, source_url, note) values

 ('turkey', 'safety.advisory_level',
  '"Level 2 — Exercise Increased Caution"'::jsonb, 'verified', now(),
  'https://travel.state.gov/en/international-travel/travel-advisories/turkey.html',
  'Read from the advisory itself 2026-09-23. Date issued 09 June 2026. Stated reasons: terrorism, armed conflict, and arbitrary detentions.'),

 ('turkey', 'safety.do_not_travel_areas',
  '"the border region with Syria and Iraq"'::jsonb, 'verified', now(),
  'https://travel.state.gov/en/international-travel/travel-advisories/turkey.html',
  'The advisory''s own wording: "Do not travel to the border region with Syria and Iraq due to risk of terrorism and armed conflict." It gives NO distance. The article previously said "within 10 km (6 miles)", a boundary the source does not set; corrected 2026-09-23.'),

 ('turkey', 'entry.visa_free_days',
  '"90 days within any 180-day period"'::jsonb, 'provisional', now(), null,
  'As written in the articles; not re-verified against a primary source in this pass.'),

 ('turkey', 'entry.passport_validity',
  '"six months beyond your date of entry, with one blank page"'::jsonb, 'provisional', now(), null,
  'As written in the articles; not re-verified against a primary source in this pass.'),

 ('turkey', 'calendar.ramadan_next',
  '"8 February to 8 March 2027"'::jsonb, 'provisional', now(), null,
  'Lunar date, shifts about 11 days earlier each year — re-check before each season. Used in ramadan-in-turkey-what-changes and how-turkeys-holiday-calendar-is-set.'),

 ('turkey', 'calendar.ramazan_bayram_next',
  '"9-11 March 2027, preceded by a half-day from 13:00 on 8 March"'::jsonb, 'provisional', now(), null,
  'Lunar; re-check annually.'),

 ('turkey', 'calendar.kurban_bayram_next',
  '"16-19 May 2027, preceded by a half-day from 13:00 on 15 May"'::jsonb, 'provisional', now(), null,
  'Lunar; re-check annually.'),

 ('turkey', 'health.vaccines',
  '"No vaccines are required for entry to Turkey from the US"'::jsonb, 'provisional', now(), null,
  'As written; re-check against CDC guidance before each season.'),

 ('turkey', 'insurance.exclusion_motorcycle',
  '"Standard travel policies commonly exclude or restrict motorbike, scooter and quad use"'::jsonb,
  'provisional', now(), null,
  'Category statement rather than a figure, but consistent across its spans and the kind of claim that moves with the market.')

on conflict (scope, key) do update
  set value      = excluded.value,
      status     = excluded.status,
      checked_at = now(),
      source_url = excluded.source_url,
      note       = excluded.note,
      updated_at = now();

-- Housekeeping: a row under a scope no site resolves. factScopes() is
-- [dbSchema, ...factRegions, 'global'], so Thailand reads 'thailand', never
-- 'thailandforamericans'. The correctly-scoped row already exists.
delete from common.facts where scope = 'thailandforamericans';

-- verify
select scope, key, value, status, checked_at::date
  from common.facts
 where scope = 'turkey'
 order by key;
