# Stage 6 — Fleet ops (the console, the checker, the agents, the weekly gate)

The empire-wide operations layer ABOVE any single site. Where stages 1–5 BIRTH a site,
stage 6 MAINTAINS the whole fleet from one place. A new site doesn't "do" stage 6 — it
gets ONBOARDED into it, by a script that proves each step.

Repo: **fleet_ops** (separate from site repos and from travel-facts). Workflows:
`.github/workflows/check-facts.yml` (Mondays 06:17 UTC), `link-check.yml` (Thursdays
06:00 UTC), and — proposed — `fleet-gate.yml` (Mondays, after check-facts).

## The shared `common` schema (source of truth after a fact is born)

One Supabase project; each site in its own Postgres schema; a shared `common` schema holds
everything fleet-wide. Tables today: `affiliate_policy, affiliate_programs,
affiliate_site_credentials, audit_log, check_runs, fact_revisions, facts, fleet_meta,
guide_entitlements, link_clicks, link_findings, link_runs, sites, subscribers`.

| Migration | Adds |
|-----------|------|
| SETUP_common / 0002 | `facts` (scope,key,value,status,checked_at,source_url,note,check,check_failures,last_check_ok), `fact_revisions` |
| 0003 | `facts.proposed_value` |
| 0004 | `sites.admin_url` |
| 0005 | `audit_log` |
| 0006 | `check_runs`, `sites.engine_version`, `sites.vercel_project_id`, `fleet_meta` |
| 0007 | `link_clicks` |
| 0008 | `link_findings`, `link_runs` |
| 0009 | `subscribers` |
| (v5.7) | `guide_entitlements` — the purchase record the Stripe webhook writes |
| **0010 (proposed)** | `facts.review_after date, facts.source_kind text, facts.support text` — the provenance fields `validate-facts.mjs` already requires on facts.json but the DB drops at birth; `link_clicks.ua_unknown boolean` for the 5,031 rows logged before UA capture |

**HARD-WON: grant sequences AFTER every migration that adds a table**, then
`notify pgrst, 'reload schema';`. `onboard-check.mjs` emits both lines in its SQL.

## Facts: the `check` config (official-source verification)

A fact with a structured `check` config is auto-maintained by the weekly checker; a fact
without one ages until a human re-verifies it. **As of 2026-10-14, 2 of 231 facts have a
check config.** The checker is therefore green while maintaining under 1 % of the layer.
Two rules follow:

- the checker's headline is `checked X of N facts (Y unchecked, Z dead sources)` — the
  unchecked count is the number that matters, and `X/N < 0.1` is a WARN row in the console;
- every Stage-3 seed of a fact with a numeric value on a static official page ships WITH its
  `check` config (`{kind:"regex", select:"…(\\d+)…", field:null, bound_ratio:3}`). A seed
  without one is a `provisional` fact that nobody will ever re-check.

## The checker (`scripts/check-facts.mjs`, weekly GitHub Action)

Per fact with a `check` config: fetch source → extract → compare. match → refresh; drift
within bound → auto-update (logged); beyond bound → `needs_review` + `proposed_value`;
source dead 3× → escalate. One `check_runs` row per run, dry runs included. Node 22.

## The fleet console (portal, its own Vercel project off fleet_ops)

One screen over every site. Supabase Auth + email allowlist, service role SERVER-SIDE only,
`cache: 'no-store'` on every read. Pages: Sites, Review queue, Source health, Freshness,
History, Fact edit, Links, Affiliates, Ops. Every mutating action writes `audit_log`.
Tier-3 integrations are feature-flagged: Vercel deploy status (`VERCEL_TOKEN`), GSC 28-day
clicks (`GOOGLE_SERVICE_ACCOUNT_JSON`, `webmasters.readonly`, Domain properties only),
GitHub workflow dispatch.

**Proposed rows (from the 2026-10 audit):** `/guide` visitors (Vercel Analytics API) and
Stripe sessions per site per week — the funnel in one line, so "has anyone reached
checkout" is a glance, not an API session.

## The agent layer — detect → PROPOSE → human approves → audit

Agents never edit content or values directly. Agent #1 link-rot (`scripts/link-check.mjs`)
is live: 7 sites, 653 articles, ~340 URLs/run, 2 open findings. **Its site list must come
from `common.sites`** — it still reads 7 sites while 9 are live (same defect as
`audit-fleet.mjs`).

## Onboarding a NEW site into the fleet — a script, not a procedure

The old seven-step prose (Studio SQL ×2, Supabase UI, Vercel UI, GSC UI, code) is now:

```
node scripts/onboard-check.mjs <schema> <slug> <domain> --sql-out onboard-<schema>.sql
```

It verifies, read-only, with a PASS/FAIL per step and `checked N of 7`:

1. `common.sites` row exists with the right domain (else **subscribers and clicks are being
   silently dropped from the first deploy** — the FK is fail-soft);
2. sequences granted / API reloaded (proven by the subscribe probe);
3. `engine_version` == `fleet_meta.engine_version`;
4. the schema is exposed to the Data API (a PostgREST read through `Accept-Profile: <schema>`);
5. `vercel_project_id` == the `apps/site` project in `.vercel/project.json`;
6. GSC Domain property shared with the service account (today: proven only by the portal
   column; API check is A-5 in AUTOMATION-MAP);
7. `/api/subscribe` alive (422 on a bad email) and the five site env vars present on the
   Vercel project (`vercel env ls production`).

For every FAIL it prints the remedy; the SQL remedies are written as ONE idempotent file to
paste into the Studio editor once (REST cannot run GRANT/DDL and there is no psql on this
machine — adding `SUPABASE_DB_URL` to `.env.local` lets the script apply it itself).
**Run it before the first production deploy, and again at go-live.**

Timing rule (unchanged, now enforced): steps 1–2 are a DEPLOY prerequisite, not a go-live
step. The `new-site` bootstrap prints this command at the end of its run.

### Verify
`onboard-check.mjs` green, then `fleet-gate.mjs --sites <schema>` green, then the console
row reads engine = baseline, Deploy = ready, GSC = a number.

## The weekly fleet gate (proposed workflow `fleet-gate.yml`)

```
node scripts/fleet-gate.mjs --json gate.json --stripe        # 14 checks × N sites; exit 1 = red
python3 scripts/corpus-check.py articles/ facts.json         # the cross-site table
node scripts/render-check.mjs                                # real-browser truth (playwright in runner)
node scripts/state-reconcile.mjs --apply                     # state.json is data
python3 scripts/funnel.py --days 7                           # the funnel line
```
Secrets: SUPABASE_URL + service key (present), STRIPE_SECRET_KEY (use a restricted read-only
key), VERCEL_TOKEN. A red run posts the FAIL lines; a green run posts the denominators.
