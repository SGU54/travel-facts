-- ═══════════════════════════════════════════════════════════════════════════
-- travel-facts/greeceforamericans/greece-facts.sql
-- Fact seeds for greeceforamericans (site schema: greece). Append-only.
-- Run with service role against the shared Supabase project. Safe to replay.
--
-- ⚠ SCOPE NOTE: every row below is scope 'eu' — SHARED fleet-wide. Any EU site
-- (rome, barcelona, …) whose spans reference these keys resolves them too.
-- That is intended (one row maintains the whole EU fleet). Existing rows
-- eu.etias_fee and eu.schengen_stay are ALREADY live (checker work) and are
-- deliberately NOT re-emitted here — the DB is their source of truth.
--
-- Status mapping per docs/fact-emission.md:
--   verify_recommended (facts.json) → 'provisional'
--   verified (official source actually checked at emit) → 'verified'
-- ═══════════════════════════════════════════════════════════════════════════

-- ── retrofit batch (2026-07-12) — greeceforamericans re-platform Part 1 ──────
insert into common.facts (scope, key, value, status, checked_at, source_url, note) values
  ('eu', 'eu.etias_launch',
     '{"text":"late 2026"}'::jsonb,
     'provisional', now(),
     'https://travel-europe.europa.eu/etias_en',
     'ETIAS expected last quarter 2026; date has slipped repeatedly — keep human-tier, no regex check (official page is JS-rendered).'),

  ('eu', 'eu.etias_validity',
     '{"text":"about three years"}'::jsonb,
     'provisional', now(),
     'https://travel-europe.europa.eu/etias_en',
     'ETIAS authorization validity (3 years or until passport expiry).'),

  ('eu', 'eu.cash_declaration',
     '"€10,000"'::jsonb,
     'verified', now(),
     'https://taxation-customs.ec.europa.eu/customs/prohibitions-restrictions/eu-cash-controls_en',
     'EU cash-declaration threshold (Reg. 2018/1672). Verified against the official EC customs page 2026-07-12. Check-config candidate — see proposal file.'),

  ('eu', 'eu.passport_validity_min',
     '{"text":"three months"}'::jsonb,
     'provisional', now(),
     null,
     'Schengen Borders Code: passport valid ≥3 months beyond planned departure. facts.json carried no source_url — add one at first console review.'),

  ('eu', 'eu.passport_issue_age',
     '{"text":"ten years"}'::jsonb,
     'provisional', now(),
     null,
     'Schengen Borders Code: passport issued within previous 10 years. facts.json carried no source_url — add one at first console review.'),

  ('eu', 'eu.ees_status',
     '{"text":"now fully in effect"}'::jsonb,
     'verified', now(),
     'https://home-affairs.ec.europa.eu/policies/schengen/smart-borders/entry-exit-system_en',
     'EES fully operational since 10 April 2026 (progressive rollout from 12 Oct 2025). Verified against the official EC page 2026-07-12. Categorical → human-tier; terminal state, low churn.')

on conflict (scope, key) do update set
  value      = excluded.value,
  status     = excluded.status,
  checked_at = excluded.checked_at,
  source_url = excluded.source_url,
  note       = excluded.note;
