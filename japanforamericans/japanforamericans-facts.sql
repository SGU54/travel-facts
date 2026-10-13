-- travel-facts/japanforamericans/japanforamericans-facts.sql
-- Append-only seed of every fact spanned in japanforamericans.com article batches.
-- Run in the Supabase SQL editor with the SERVICE ROLE (anon is RLS-blocked by design).
-- Idempotent: safe to re-run the whole file any time.
--
-- IMPORTANT: scope = 'japan' — this is SITE.dbSchema (packages/config/site.ts),
-- confirmed by reading packages/db/common.ts's factScopes(), NOT the project
-- folder name 'japanforamericans'. Using the wrong scope silently orphans the
-- rows: the site's render path (apps/site/lib/facts.ts) only ever queries
-- ['japan', 'global'], never 'japanforamericans'.

-- ============================================================
-- Batch-01 retrofit (pilot) — 2026-09-10
-- Source: travel-facts/japanforamericans/facts.json (pipeline-standard copy
-- of FINAL.json), re-checked against current sources during this batch.
-- ============================================================

-- entry.visa_free_days — do-americans-need-visa-japan
-- facts.json: country_facts.visa.by_nationality[0].max_stay_days, status "verified"
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('japan', 'entry.visa_free_days', '"90 days"'::jsonb, 'verified', now(),
        'https://www.mofa.go.jp/j_info/visit/visa/short/novisa.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- entry.passport_validity — do-americans-need-visa-japan
-- facts.json: country_facts.documents.passport_validity_required, status "verify_recommended"
-- -> 'provisional' (direct map, per 3-writing.md — not self-promoted to verified
-- since the primary MOFA page blocked automated fetch; corroborated via secondary
-- sources only, so kept honest at the facts.json-flagged tier).
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('japan', 'entry.passport_validity', '"valid for the duration of your stay"'::jsonb, 'provisional', now(),
        'https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Japan.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- safety.advisory_level — is-japan-safe-for-americans
-- facts.json: country_facts.safety_health.advisory_level, status "verified"
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('japan', 'safety.advisory_level', '"Level 1 — Exercise Normal Precautions"'::jsonb, 'verified', now(),
        'https://travel.state.gov/content/travel/en/traveladvisories/traveladvisories/japan-travel-advisory.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- money.declare_threshold — money-in-japan-cash-cards-ic
-- facts.json: country_facts.money.currency_import_export_limit, status "verify_recommended" -> 'provisional'
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('japan', 'money.declare_threshold', '"¥1,000,000"'::jsonb, 'provisional', now(),
        'https://www.customs.go.jp/english/')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- money.tax_free_change_date — money-in-japan-cash-cards-ic
-- New fact added to facts.json during this batch (not in the original 5-source
-- panel) — verified directly against japan.travel, status "verified".
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('japan', 'money.tax_free_change_date', '"November 1, 2026"'::jsonb, 'verified', now(),
        'https://www.japan.travel/en/ca/news/changes-are-coming-to-tax-free-shopping-in-japan/')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- ============================================================
-- Batch B (transit depth) — 2026-09-16
-- Source: travel-facts/japanforamericans/facts.json -> depth_facts, merged from a
-- 3-member panel (claude/deepseek/grok) with all 5 disputes ruled against official
-- pages. See disputes-extension.md for the rulings and the panel scorecard.
--
-- STATUS IS A DIRECT MAP of facts.json's own flag — verify_recommended -> 'provisional',
-- verified -> 'verified'. AI research is never self-promoted to verified.
--
-- ⚠ VOLATILITY: Japanese rail pricing rose ~70% on 1 Oct 2023 and rises again for
-- OVERSEAS-AGENCY purchases on 1 Oct 2026 (online is unaffected). Every rail figure
-- below is short-lived by design — that is exactly why these are spans and not prose.
-- ============================================================

-- rail.pass_7day_ordinary — regional-jr-passes-vs-national
-- depth_facts.rail_passes.national_pass_variants, status "verified" (official page fetched 2026-09-16)
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('japan', 'rail.pass_7day_ordinary', '"¥50,000"'::jsonb, 'verified', now(),
        'https://japanrailpass.net/en/purchase/price/')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- rail.pass_7day_overseas_oct2026 — regional-jr-passes-vs-national
-- depth_facts.rail_passes.national_pass_price_change_2026, status "verified"
-- NOTE: applies to overseas-agency purchases only. Online stays at rail.pass_7day_ordinary.
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('japan', 'rail.pass_7day_overseas_oct2026', '"¥53,000"'::jsonb, 'verified', now(),
        'https://japanrailpass.net/en/purchase/price/')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- rail.tokyo_kyoto_reserved — regional-jr-passes-vs-national, japan-rail-route-cost-without-pass
-- depth_facts.rail_passes.tokyo_kyoto_one_way_cost, status "verify_recommended"
-- Hikari reserved, the fastest service the national pass covers. Break-even arithmetic
-- in both articles divides by THIS figure — if it changes, recompute the prose claim.
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('japan', 'rail.tokyo_kyoto_reserved', '"about ¥13,850"'::jsonb, 'provisional', now(),
        'https://global.jr-central.co.jp/')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- rail.nozomi_supplement_tokyo_kyoto — regional-jr-passes-vs-national
-- depth_facts.rail_passes.nozomi_mizuho_rule, status "verify_recommended"
-- Figure came from one panel member only; the RULE is agreed, the NUMBER is not.
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('japan', 'rail.nozomi_supplement_tokyo_kyoto', '"around ¥4,960"'::jsonb, 'provisional', now(),
        'https://japanrailpass.net/')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- transit.ic_max_balance — mobile-suica-american-iphone
-- depth_facts.ic_cards.balance_limits_and_refund, status "verify_recommended"
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('japan', 'transit.ic_max_balance', '"¥20,000"'::jsonb, 'provisional', now(),
        'https://www.jreast.co.jp/multi/en/pass/suica.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- transit.ic_card_deposit — mobile-suica-american-iphone
-- depth_facts.ic_cards.physical_card_availability, status "verify_recommended"
-- DISPUTED then ruled: unregistered cards resumed sale 1 March 2025 (grok correct,
-- deepseek wrong). If sales are suspended again this value becomes meaningless, not stale.
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('japan', 'transit.ic_card_deposit', '"¥500"'::jsonb, 'provisional', now(),
        'https://www.jreast.co.jp/multi/en/')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- transit.tokyo_subway_ticket_24h — ic-card-day-pass-or-single-ticket
-- depth_facts.ic_cards.day_passes_tokyo, status "verify_recommended"
-- The TOURIST Tokyo Subway Ticket (Metro + Toei), not the Metro-only 24-hour ticket.
-- Whole panel got this wrong; ruled against current sources 2026-09-16.
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('japan', 'transit.tokyo_subway_ticket_24h', '"¥1,000"'::jsonb, 'provisional', now(),
        'https://www.tokyometro.jp/en/ticket/travel/index.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- transit.kyoto_day_pass — ic-card-day-pass-or-single-ticket
-- depth_facts.ic_cards.day_passes_kyoto, status "verify_recommended"
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('japan', 'transit.kyoto_day_pass', '"about ¥1,100"'::jsonb, 'provisional', now(),
        'https://www.city.kyoto.lg.jp/')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- transit.welcome_suica_validity — ic-card-day-pass-or-single-ticket
-- depth_facts.ic_cards.welcome_suica, status "verify_recommended"
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('japan', 'transit.welcome_suica_validity', '"28 days"'::jsonb, 'provisional', now(),
        'https://www.jreast.co.jp/multi/en/pass/welcomesuica.html')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- ═══════════════════════════════════════════════════════════════════════════
-- BATCH C (2026-09-17) — Green Car tier keys for green-car-or-ordinary-japan-rail-pass
-- All four come from depth_facts.rail_passes.national_pass_variants and
-- .national_pass_price_change_2026, both status "verified" (japanrailpass.net official
-- price page fetched 2026-09-16). Current prices valid through 30 September 2026.
-- ═══════════════════════════════════════════════════════════════════════════

-- rail.pass_7day_green — green-car-or-ordinary-japan-rail-pass
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('japan', 'rail.pass_7day_green', '"¥70,000"'::jsonb, 'verified', now(),
        'https://japanrailpass.net/en/purchase/price/')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- rail.pass_14day_ordinary — green-car-or-ordinary-japan-rail-pass
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('japan', 'rail.pass_14day_ordinary', '"¥80,000"'::jsonb, 'verified', now(),
        'https://japanrailpass.net/en/purchase/price/')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- rail.pass_14day_green — green-car-or-ordinary-japan-rail-pass
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('japan', 'rail.pass_14day_green', '"¥110,000"'::jsonb, 'verified', now(),
        'https://japanrailpass.net/en/purchase/price/')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;

-- rail.pass_7day_green_overseas_oct2026 — green-car-or-ordinary-japan-rail-pass
-- NOTE: applies to overseas-agency purchases only. Online stays at rail.pass_7day_green.
insert into common.facts (scope, key, value, status, checked_at, source_url)
values ('japan', 'rail.pass_7day_green_overseas_oct2026', '"¥74,000"'::jsonb, 'verified', now(),
        'https://japanrailpass.net/en/purchase/price/')
on conflict (scope, key) do update set
  value = excluded.value, status = excluded.status,
  checked_at = excluded.checked_at, source_url = excluded.source_url;
