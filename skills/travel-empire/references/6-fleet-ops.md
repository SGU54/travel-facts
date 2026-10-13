# Stage 6 — Fleet ops (the console, the checker, the agents)

The empire-wide operations layer that sits ABOVE any single site. Built after the
first sites were live (passes 4–5). Where stages 1–5 BIRTH a site, stage 6
MAINTAINS the whole fleet from one place. A new site doesn't "do" stage 6 — it gets
ONBOARDED into the fleet-ops that already exists.

Read this when: standing up / editing the fleet portal, working on the facts
checker or its `check` configs, building or running an agent (link-rot etc.),
or onboarding a new site into the console.

Repo: **fleet_ops** (separate from site repos and from travel-facts). Canonical
package + manifest: `fleet-empire-pass4-5.zip` / `PACKAGE.md` / `AGENT-LAYER.md`.

## The shared `common` schema (source of truth after a fact is born)

One Supabase project; each site in its own Postgres schema; a shared `common`
schema holds everything fleet-wide. Migrations are numbered, idempotent, applied
in Studio in order:

| Migration | Adds |
|-----------|------|
| SETUP_common / 0002 | `facts` (scope,key,value,status,checked_at,source_url,note,check,check_failures,last_check_ok), `fact_revisions`, the `check` config column |
| 0003 | `facts.proposed_value` — the checker's structured proposal when it flags |
| 0004 | `sites.admin_url` |
| 0005 | `audit_log` — every console write attributed |
| 0006 | `check_runs`, `sites.engine_version`, `sites.vercel_project_id`, `fleet_meta` |
| 0007 | `link_clicks` (site-side /go/ logging) |
| 0008 | `link_findings`, `link_runs` (agent #1) |
| 0009 | `subscribers` (+ unique (site_key,email), touch trigger) — the lead-magnet capture table LEAD_MAGNET_SETUP.md always referenced; versioned since 2026-08 |

**HARD-WON: grant sequences AFTER every migration that adds a table.** A table's
identity sequence is not granted to `service_role` by the table grant alone;
inserts then fail SILENTLY (checker/agents print a non-fatal `! insert failed`
that scrolls past). After running any migration that creates a table, run:
`grant usage, select on all sequences in schema common to service_role;`
and if the API can't see a new table: `notify pgrst, 'reload schema';`

## Facts: the `check` config (official-source verification is LIVE)

The "deferred official-source verification" that 2-facts.md describes as parked is
BUILT. A fact with a structured `check` config is auto-maintained by the weekly
checker; a fact without one ages until a human re-verifies it (that's fine —
prose/categorical facts legitimately stay human-tier).

`check` config shape (jsonb on `common.facts`):
```json
{ "kind": "regex", "select": "fee will be EUR (\\d+)", "field": null, "bound_ratio": 3 }
```
- `select` — regex with ONE capture group, run against a STATIC official page
  (JS-only pages like the live ETIAS site are unreachable — pick a server-rendered
  gov/EC page that states the value in plain text).
- `field` — `null` for a scalar value; the key name for an object value
  (`{"amount":20}` → `"field": "amount"`).
- `bound_ratio` — auto-correct within ×N; beyond it, FLAG for human review.

Only facts with a machine-extractable number on a static source are good
candidates. Fixed numerics with official pages (visa fees, day-counts, Schengen
90/180) are ideal; categorical prose and multi-value judgments stay human-tier.

## The checker (`scripts/check-facts.mjs`, weekly GitHub Action)

Per fact with a `check` config: fetch source → extract → compare.
- match → refresh checked_at/last_check_ok, clear proposal.
- drift WITHIN bound → auto-update value (logged to fact_revisions).
- drift BEYOND bound, or categorical change → status `needs_review`, value KEPT,
  **`proposed_value` = the full next value** (so the console's one-click Accept is
  mechanical, never a note re-parse).
- source dead 3 consecutive runs → escalate needs_review.
- writes one `check_runs` row per run (dry runs included — a broken cron must be
  visible).

Node **22** in the workflow (recent supabase-js refuses to construct on Node 20 —
no native WebSocket). A flagged fact stops substituting into articles (readers see
the written fallback) until resolved.

## The fleet console (portal, its own Vercel project off fleet_ops)

The FortiManager of the fleet — one screen over every site. Next.js 14, Supabase
Auth + email allowlist, service-role SERVER-SIDE only. **All Supabase reads use
`cache: 'no-store'`** (Next 14 caches GET fetches → stale ops data otherwise).
Pages: Sites (+per-site drill: publish/unpublish, dry-run bulk publish),
Review queue (accept-proposal / keep-current), Source health, Freshness, History,
Fact edit, Links (agent findings), Affiliates, Ops (checker runs + audit trail +
agent dead-man switch). Every mutating action writes an `audit_log` row; a failed
audit write ABORTS the action (an unattributable write is worse than none).

Tier-3 integrations are feature-flagged (missing cred → "not configured", never a
crash): Vercel deploy status, GSC 28-day clicks per domain (service-account JWT;
the property must be a **Domain property** `sc-domain:` and the Search Console API
enabled in the GCP project), GitHub workflow dispatch ("Run checker now").

## The agent layer (pass 5) — detect → PROPOSE → human approves → audit

Agents are scheduled detectors that write PROPOSALS into `common` tables, reviewed
in the console, fully audited. **Agents NEVER edit content or values directly** —
same human gate as the checker; the certified human signature is the value.
Agent code is changed by a human through git, NEVER by an agent (no self-modifying
automation). Roster ranked for the current scale in `AGENT-LAYER.md`.

**Agent #1 link-rot** (`scripts/link-check.mjs`, ~€0/run, deterministic — no LLM):
scans published articles per site, classifies href links (internal / external /
affiliate `/go/` where a 3xx redirect IS success), checks each unique URL once,
upserts `link_findings`, and **auto-resolves a finding when its URL passes OR
disappears from the article** (both are "fixed"; the resolver keys on
site|article|url, not just live-and-passing). One `link_runs` row per run.
NOTE: extracts `href` only — broken images (`src`) are agent #5's job, not #1's.

Later agents (freshness auditor, fact-scout, coverage-gap) are LLM-based and
DESIGNED but gated: no agent #N+1 is built until agent #N passes its live
validation checklist. This is the validate-before-scale gate applied to the agent
layer itself.

## Onboarding a NEW site into the fleet (the stage-6 step for a new site)

**TIMING: steps 1–2 are a DEPLOY prerequisite, not a go-live step** —
`common.subscribers` and `common.link_clicks` both FK to
`common.sites(site_key)`, and both writes are fail-soft: an unregistered
site's signups and clicks are silently dropped from the first deploy. Run the
insert + grants when the site first deploys; do the rest at go-live.

When a site reaches "live", complete the registration so the console lights up
its row. This is a SIX-step procedure across three surfaces (Supabase SQL,
Supabase settings, Google Search Console) — the SQL alone is NOT enough, and
skipping steps 4–6
leaves the console row erroring on the Deploy and GSC columns. (Learned the hard
way onboarding romeforamericans, 2026-07: the SQL ran but the row showed
`v2 → pass-2` engine drift, `api error` on deploy, and `err` on GSC — all three
were steps below that the bare insert doesn't cover.)

### Step 1 — Supabase SQL Editor: register the row (idempotent)
```sql
insert into common.sites (site_key, domain, admin_url, destination_scope,
  engine_version, vercel_project_id)
values ('<schema>', '<domain>', '<ADMIN_VERCEL_URL>', '<scope>',
  '<engine>', '<SITE_VERCEL_PROJECT_ID>')
on conflict (site_key) do update set
  domain            = excluded.domain,
  admin_url         = excluded.admin_url,
  destination_scope = excluded.destination_scope,
  engine_version    = excluded.engine_version,
  vercel_project_id = excluded.vercel_project_id;
```
Use `do update` (not `do nothing`) so a re-run corrects a bad earlier value
instead of silently keeping it.

### Step 2 — same editor: the two always-run lines
```sql
grant usage, select on all sequences in schema common to service_role;
notify pgrst, 'reload schema';
```

### Step 3 — `engine_version` must match the fleet baseline
The console compares each site's `engine_version` to `common.fleet_meta`
(key `engine_version`). If they differ it renders an engine-DRIFT warning
(`<site value> → <baseline>`). The value is a MANUAL marker with no operational
effect — sites shown in the console are simply the not-yet-migrated ones — so its
only job is to NOT flash a false warning. **Stamp the same string the live sites
use** (currently `pass-2`), unless you are deliberately bumping the whole fleet to
a new engine generation, in which case update `fleet_meta` AND every site row
together, never one site alone.

### Step 4 — Supabase → Settings → API → Exposed schemas (UI, not SQL)
Add the site's own schema (`<schema>`) to the allow-list, alongside `common`.
Without this, the site's server reads its own schema fine via the service role,
but anything reading Rome through the Data API fails.

### Step 5 — the Vercel project id must be the SITE project, not admin
Sites deploy as TWO Vercel projects: `apps/site` (public) and `apps/admin` (CMS).
`vercel_project_id` in the row must be the **`apps/site`** project's id (Vercel →
that project → Settings → General → Project ID, `prj_…`) — that is the deployment
the console's health check watches. `admin_url` is the **`apps/admin`** project's
production URL (a convenience jump-link only). Do not cross them: an admin id in
`vercel_project_id` makes the console watch the wrong deploy. A placeholder or
wrong id → the Deploy column reads `api error`.

### Step 6 — share the GSC property with the fleet service account
In Google Search Console → the site's **Domain property** → Settings → Users and
permissions → add the fleet service-account email (the `client_email` inside
`GOOGLE_SERVICE_ACCOUNT_JSON`) as a user. Until then the GSC column reads `err`
(the console reads clicks via `sc-domain:` and can't see an unshared property).
A freshly re-platformed site legitimately shows `0` clicks for a while — that is
a real number, not an error.

### Step 7 (Tier-4) — /go/ click logging
The `/go/[role]/[item]` route must call the click-logging insert into
`common.link_clicks` before redirecting (canonical drop-in:
`site-snippets/go-click-logging.ts`). v5.2+ sites wire this via the db package
(`logGoClick()` — fire-and-forget, fail-open, attribution BY `site_key`).
**SERVICE ROLE IS LOAD-BEARING here**: `link_clicks` ships RLS-on with no
policies and anon has no INSERT grant (by design — the public anon key must
not be able to forge rows). `logGoClick` therefore builds its own
service-role writer; pointing it at the anon `commonClient()` silently kills
ALL click logging fleet-wide (real bug, found 2026-08 — zero rows ever
landed). Never "simplify" it back onto the read client. The portal only READS
`link_clicks`.

### Verify
Reload the console. The row should read: engine = baseline (no `→`), Deploy =
`ready · <age>`, GSC = a number. Then click a `/go/` link on the live site and
confirm `select count(*) from common.link_clicks where site_key = '<schema>';`
increments.

The console, checker, and every agent then cover the new site automatically —
marginal fleet-ops cost per added site is ~zero. That property is the whole point
of the layer, and the precondition the strategy gate names before scaling series.
