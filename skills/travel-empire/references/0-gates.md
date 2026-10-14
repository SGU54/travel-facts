# Stage 0 — The gate contract (read before trusting any PASS)

Every check in this fleet has, at some point, printed PASS while measuring nothing. The
list is long and all of it is real: a 0-word manuscript passed two book gates; a cover
check called one brand's paper "ink"; a rhythm check read `F I G .` as no figures; the
facts checker runs weekly and reports `match 2` on a table of 231; `audit-fleet.mjs`
prints "rien à signaler" for a site whose fonts never load. The common shape: **a gate
keyed to a name it did not find, or a verdict printed without its denominator.**

## The contract

A gate:

1. **Prints its denominator before its verdict.** `checked 143 of 143 URLs`, `scanned 90
   of 90 published articles`, `9 of 9 sites`, `fonts loaded 3 of 3 declared`. A gate whose
   count is 0, or is not printed, has not run.
2. **Says BLOCKED when it cannot run.** Missing input, missing dependency, unreachable
   host, unknown class name → `BLOCKED <why>`, exit 1. Never a skip that reads as a pass
   (`audit-depth` used to go quiet with no corpus; `validate-batch` skips the vein gates
   without `--list` — both now say so on the first line).
3. **Names what it keyed on.** If it selects `section.dec` or `span.fact` or
   `/go/guide/`, it prints how many it found. Zero matches on a populated site is a FAIL
   of the gate, not of the site.
4. **Fails closed and exits non-zero**, so it can sit in a cron and a red run is red.
5. **Compares across sites when it can.** Most defects here were found because one site
   differed (Rome: 0 body images, 0 FAQ, 2 swamp tags, fonts dropped; Morocco: 34 images
   without width; Japan: a third-party script). A per-site number is a fact; the same
   number across nine sites is a diagnosis.

A ★ decision is the only other thing a step may be: a question with the candidates
rendered and a recommended default.

## The fleet gates (what runs, what it proves, what it keys on)

Scripts live in `_fleet-audit-2026-10-14/scripts/` until adopted into `fleet_ops/scripts/`.

| gate | proves | keys on | denominator |
|---|---|---|---|
| `fleet-gate.mjs` HOST / CANON / ALIAS / SITEMAP / ROBOTS | canonical www, 308 apex, `X-Robots-Tag: noindex` on `<slug>-site.vercel.app`, sitemap article count == DB published, `/go/` disallowed | HTTP + `<loc>` + PostgREST count | 9 of 9 sites, N locs |
| `fleet-gate.mjs` FONTS | the compiled CSS's first rule is the fonts `@import` OR a `<link href*=fonts.googleapis>` exists | `/_next/static/css/*.css` bytes | css length |
| `render-check.mjs` | what Chromium sees: `document.fonts` loaded, computed h1 face, console errors, failed requests, broken images, surfaces present, fact-span `display` | real browser | 3 pages × 9 sites |
| `fleet-gate.mjs` GUIDE / STRIPE | live ⇒ 200 + 2 CTAs + DB price; dark ⇒ 404; `/go/guide/sales-page` → the payment link + `client_reference_id`; Stripe amount == `guide_price`; webhook enabled | `site_settings` + HTTP + Stripe API | 7 of 7 live guides |
| `fleet-gate.mjs` REGISTRY / SUBSCRIBE / CLICKLOG / FACTS / STATE | `common.sites` row + prj id + engine; subscribe route alive (422) and, with `--write-probe`, `stored:true`; null-UA rows in 7 d == 0; every fact-span resolves; state.stage matches reality | PostgREST + HTTP | per site |
| `onboard-check.mjs` | the 7 onboarding steps, emitting the one SQL file for the FAILs | PostgREST, `vercel env ls`, `.vercel/project.json` | 7 of 7 steps |
| `corpus-check.py` | words, h2, images, images without width, IMAGE_SLOT/`{{` leftovers, guide-span glosses, fact-spans + unresolved, aff slots, FAQ/map/converter blocks, "Checked <Mon>" literals, external links, raw vendor URLs | regexes over DB `content` | 9 sites × N published |
| `state-reconcile.mjs` | proposes true state.json from DB + live + registry | PostgREST | 9 of 9 |
| `funnel.py` | link_clicks (bot-classified) + Stripe sessions + GSC exports | three APIs | rows / sessions / pages |
| `validate-batch.mjs` (existing) | word envelope, link cap, disclosure, frozen rates, alt, slugs, feature blocks, fact-span provenance, answer-first, pre-join, guide-span | the batch JSON (+ `--list`, `--facts`) | **add**: prints `N articles, M fact-spans, K guide-spans, J H2s` on line 1 |
| `skeleton-check.mjs` (existing) | template neutrality; FAILS on any font `@import` | repo files | **add**: `scanned N files` |
| `check-facts.mjs` (existing) | facts with a `check` config vs their official source | `common.facts.check` | **fix**: headline = `checked X of N (Y unchecked)`; WARN when X/N < 0.1 |
| `audit-fleet.mjs` (existing) | static repo rules (tokens, enhancer, surfaces, cost, M1/M3/M4, state) | repo files | **fix**: site list from `common.sites`, not a constant |
| dossier `audit-release.py` (existing) | evidence, content integrity, the six legacy gates, source defects | build dir | BLOCKED on every shipped book today — see dossier D-6 |

## Where the skills live (and why that is a gate too)

`~/.claude/skills/{travel-empire,dossier,marketing}` are symlinks into
`/Volumes/Untitled/travel-facts/skills/` — the exFAT volume whose git corruption is
documented twice in these same skills. When the drive is absent the symlinks dangle and
`find` returns 0 files; AppleDouble `._*` files sit inside the trees. **Proposal:** move the
three skills to local disk (`~/.claude/skills/` as real directories, tracked in the
`travel-facts` git repo under `skills/`), leave the volume for images only, and make the
`synced/` bucket read-only mirrors. Gate: `test -d ~/.claude/skills/travel-empire/scripts`
with no symlink, `find … -name '._*' | wc -l == 0`.

## Writing a new gate (the template)

```
#!/usr/bin/env node
// <name>.mjs — proves <one sentence>. READ-ONLY. Exit 1 on FAIL/BLOCKED.
let n = 0, fails = 0;
for (const site of SITES) { … n++; if (!ok) fails++; console.log(`${ok?'PASS':'FAIL'} ${site} ${check} ${whatISaw}`); }
console.log(`checked ${n} of ${SITES.length} sites`);   // the denominator, always
process.exit(fails ? 1 : 0);
```
If the gate selects by a class/id/file name, print `found K <selector>` and FAIL when K is 0
on a site that should have them.
