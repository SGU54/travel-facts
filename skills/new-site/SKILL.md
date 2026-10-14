---
name: new-site
description: >
  Stand up a NEW travel-fleet site end to end from one command: generate a
  bootstrap script (clone the newest template zip, wire env, npm install, skeleton
  gate, working dirs, Vercel CLI login), write the kickoff prompt FROM the
  template with the four placeholders filled, run the pre-flight checks
  (registration, disk, donor env present), and launch it all in a new Terminal
  window that hands off to a fresh Claude session. Use when asked to start /
  scaffold / launch / bootstrap a new site. Covers only the standing-up; the
  content pipeline is the travel-empire skill, and the first thing the new
  session does after its first deploy is `onboard-check.mjs`.
---

# new-site — from a registered domain to a working session

One command produces three things: a **bootstrap script** on disk, a **kickoff prompt**
beside it (generated, not hand-copied), and a **new Terminal window** running the first
and handing off to a Claude session with the second.

It generates before it executes. The script is written out and can be read in full
before anything touches the filesystem, the network, or an account.

## Run it

```bash
~/.claude/skills/new-site/scripts/make-bootstrap.sh <slug> <schema> <domain> <destination> [--open]
```

| arg | meaning | example |
|---|---|---|
| `slug` | folder, repo and R2 media folder | `baliforamericans` |
| `schema` | Postgres schema **and** fact scope **and** `common.sites.site_key` | `bali` |
| `domain` | the already-registered domain | `baliforamericans.com` |
| `destination` | the place name used in the kickoff | `Bali` |
| `--open` | run it in a new Terminal window | |
| `--handoff-only` | site already on disk: skip scaffolding, emit just the Vercel login + Claude handoff | |

Without `--open` it prints the path and stops, so you can read it first.

## What the generator checks BEFORE writing anything (these used to be your job)

| check | what it does | on failure |
|---|---|---|
| registration | `dig +short NS <domain> @8.8.8.8` must answer | REFUSES: an unregistered domain gets you a site nobody can reach |
| disk | `df -k /` ≥ 2 GB free | REFUSES and prints the `.next` / `node_modules` dirs it would clear |
| donor env | the donor site's two `.env.local` files exist and carry the fleet keys | REFUSES, names the donor |
| template | picks the NEWEST `travel-template-v*.zip` in the template repo, prints which | — |
| kickoff | writes `travel-sites/<SCHEMA>-KICKOFF.md` from `assets/KICKOFF-template.md` with `<SLUG> <SCHEMA> <DOMAIN> <DESTINATION>` filled; never overwrites an existing one | — |

Each one prints what it saw (`checked 4 of 4 pre-flight`), so a refusal is specific.

## What the generated script does, and why in that order

1. **Template** — clones the template repo and unzips the newest versioned zip.
2. **Credentials** — copies `.env.local` from the donor, rewrites only
   `SUPABASE_DB_SCHEMA`, `MEDIA_FOLDER`, `NEXT_PUBLIC_SITE_URL`, `ADMIN_BASE_URL`;
   blanks `ADMIN_PASSWORD` / `ADMIN_SESSION_SECRET` for the session to generate.
3. **`npm install` at the repo root**, then **`skeleton-check --template`** (which now
   FAILS on any font `@import` — hard rule 17).
4. **Working directories.** TEXT in the git repo on local disk; IMAGES on
   `/Volumes/Untitled`. Never git on that volume.
5. **`vercel login`** before the session starts (skipped if already logged in).
6. **Hands off** to `claude` with the kickoff prompt — prompt FIRST, then `--add-dir`.
7. **Prints the two commands the session must run after its first deploy**:
   `onboard-check.mjs <schema> <slug> <domain> --sql-out …` and
   `fleet-gate.mjs --sites <schema>`.

## The one argument-ordering trap

```bash
claude "$(cat KICKOFF.md)" --add-dir /path/a /path/b     # correct
claude --add-dir /path/a /path/b "$(cat KICKOFF.md)"     # BROKEN — --add-dir swallows the prompt
```

## Refusals built in

- refuses if the site folder already exists (use `--handoff-only`);
- refuses `--open` with no kickoff file (it now writes one, so this only fires if the write failed);
- refuses on any pre-flight failure above;
- the generated script is `set -euo pipefail`.

## After the window opens

The session's first task (it is in the kickoff) is the admin: generate both secrets,
create the two Vercel projects from the same repo, verify on a preview that `/login` works
**and** the dashboard's category count matches `<schema>.categories`. Then, **before the
first production deploy**, `onboard-check.mjs` must be green — it is what proves the
`common.sites` row exists (else every subscriber e-mail is dropped with a 200), the alias
is `noindex`, the env is complete. Then Stage 1 of **travel-empire**. This skill stops at
the handoff.

## Four things that fail silently on a new site (all now gated)

- **An unregistered site drops every email it collects** — `onboard-check` step 1 / `fleet-gate SUBSCRIBE --write-probe`.
- **`<slug>-site.vercel.app` serves a full crawlable copy** unless `middleware.ts` is deployed — `fleet-gate ALIAS`.
- **`SUPABASE_SERVICE_ROLE_KEY` missing on the SITE project** — same symptom as the first, different cause (Vietnam, 24 h) — `onboard-check` step 7.
- **Vercel Web Analytics not enabled** — `<Analytics/>` renders, the dashboard shows "Demo Data" (Vietnam, Bali) — `fleet-gate ANALYTICS` (proposed) or the dashboard toggle.
- (still a hand step) **The GSC verification TXT value is visually truncated on screen** — read it from the DOM.
