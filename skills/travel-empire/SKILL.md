---
name: travel-empire
description: >
  The ONE skill for the travel-site empire — empty domain to published monetized
  articles, plus the fleet-ops layer above all sites. A project = destination +
  audience (e.g. romeforamericans). Covers: standing up a NEW site (scaffold,
  Supabase/R2/Vercel, admin); facts.json build + cross-check; writing article
  batches; clean/image/import/link/publish; design/restyle; go-live. AND Stage 6
  fleet ops — the fleet console/portal, the facts checker + check configs, the
  needs_review queue, the agent layer, the shared common schema + migrations,
  onboarding a live site, the weekly fleet gate. Triggers: new travel site,
  launch/scaffold/resume [project], build/check facts, reconcile, write batch N,
  clean/link/publish, import batch, fleet console, facts checker, check config,
  link-rot agent, onboard [site], fleet gate, common schema migration, swamp list,
  guide handoffs, backfill guide name, opportunity gate, should we write this,
  reject rules, search volume, winnable SERP, article predictions — or any project
  name + lifecycle verb. Read state.json FIRST for site work; open only the relevant
  stage reference (6-fleet-ops.md for fleet ops; 0-gates.md before trusting any PASS).
---

# Travel Empire — one skill, five stages, one gate contract

Everything runs through one pipeline with one source of truth for progress. A **project =
destination + audience** (e.g. `romeforamericans`). Same country, different audience =
different project (visa, money framing, flight origins all change).

```
STAGE 1  ARCHITECTURE  empty correct site (minimalist template look) + approved categories & article list
STAGE 1c OPPORTUNITY   the pre-writing gate: every article-list row gets REJECT /
                       INVESTIGATE / PRODUCE / STRUCTURAL, with a written reason and a
                       filed prediction. Volume is the target, winnability the filter —
                       never the reverse. (1c-opportunity-gate.md)
STAGE 2  FACTS         facts.json built, cross-checked, reconciled — with provenance
STAGE 3  WRITING       batches of 5 articles from facts.json, second-gate checked
STAGE 4  PUBLISHING    clean -> images -> import (draft) -> links -> affiliates -> publish
         (3 and 4 repeat per batch until the article list is done)
STAGE 5  DESIGN        restyle the BUILT site into a distinct identity (after infra is real),
                       then ship the standard UX/SEO feature set (5-features.md) + go-live gate
STAGE 5c CONVERSION    the guide's own selling surfaces — SEVEN, intent-gated — ONLY on a site
                       whose guide has a checkout link; fail-closed everywhere else. 5c MOUNTS;
                       the marketing skill writes the hooks/copy + the placement map. (5c-conversion.md)
         LIVE          NEXT_PUBLIC_SITE_URL, real DNS, sitemap in GSC, fleet-gate green → stage: "live"
STAGE 6  FLEET OPS     empire-wide layer ABOVE any one site: the console, the checker, the agents,
                       the weekly fleet gate. A new site is ONBOARDED into it, not built by it. (6-fleet-ops.md)
```

**Design comes LAST, not first.** The site is built on the neutral **minimalist template look**
and only restyled once the real architecture, components, and content exist. Styling the
*actual rendered site* is the only way the design that's approved is the design that ships.

## What runs this pipeline (read this once — it changed)

The pipeline runs **in Claude Code, on this Mac, with the repos checked out, the facts repo
on local disk, Supabase/Stripe/Vercel credentials in `apps/admin/.env.local` and
`special/`, Playwright in `barcelonaforamericans/node_modules`, PIL available, no
ImageMagick.** Consequences, each of which retires a sentence that used to say "the user
does this":

- **Repo writes are the session's.** state.json, article-list.json, facts.json, seeds: the
  session edits, commits and pushes `travel-facts/<project>/` itself. "Output state.json
  for the user to push" is dead text.
- **Exports come from the DB, not from an upload.** `articles-batch.mjs export` or one
  PostgREST call with `Accept-Profile: <schema>`. Never ask for a corpus file.
- **The browser is a tool, not a person.** Vercel, GSC, Stripe, Namecheap, CJ are logged in
  in Chrome. A dashboard check is a session action.
- **Scripts run here.** `python3 …/dossier/scripts/x.py`, `node scripts/y.mjs` — paths are
  this machine's (`~/.claude/skills/<skill>/scripts/`), never `/mnt/skills` or `/opt/pw-browsers`.
- **The volume `/Volumes/Untitled` is exFAT.** Images live there; git never runs there. The
  three big skills are symlinked from it today (see 0-gates.md "where the skills live").

## The gate contract (the rule that replaces a hundred "verify that…" sentences)

**Every step in this skill is one of exactly two things:**

1. **A gate** — a command with a machine-readable PASS/FAIL that prints its denominator
   (`checked 143 of 143`, `scanned 90 of 90 published`, `9 of 9 sites`). A gate that cannot
   run prints `BLOCKED`, never PASS. A gate with no count is not a gate; it is a wish.
2. **A ★ decision** — a question to the user, with the candidates rendered and a
   recommended default, phrased so "yes" is a complete answer.

Nothing in between. "Verify the deploy", "spot-check YMYL facts", "confirm fonts load",
"make sure the sitemap is right" are all gates now (`0-gates.md` lists them with the script
that runs each). The user's involvement is the ★ list and nothing else. Read
`references/0-gates.md` before trusting any PASS printed by anything in this fleet —
several gates key off exact class/file names and measure nothing when pointed at a site
that uses other names (a 0-word manuscript once passed two gates).

**The ★ decisions, in pipeline order** (the complete list — if a step wants the user and is
not here, it is a gate that has not been written yet):

| ★ | stage | question | default |
|---|---|---|---|
| 1 | 1 | approve the destination-shaped categories | the derivation |
| 2 | 1/1c | approve the article list (arrives pre-scored; REJECT rows removed) + the swamp hypothesis | PRODUCE + STRUCTURAL rows |
| 3 | 2 | rule on ≤5 fact disputes that have no official source | the value with primary support, else null |
| 4 | 3/4 | read each batch for voice (5-item judgment gate) | publish |
| 5 | 4 | pick images from the contact sheet | the first candidate per slot |
| 6 | 5 | pick one of 2–3 design directions | the one whose thesis names the place most specifically |
| 7 | 5/5c | choose the three featured articles | top three by impressions with a hero image |
| 8 | dossier A2/A3 | is this thesis right; approve the name + hooks | the mined spine; the first name |
| 9 | 5c | the price | $24 country / $19 city (fleet convention) |

## The guide is the center — the swamp doctrine

Search traffic no longer pays for article volume (AI answer boxes absorb informational
queries). The fleet's revenue engine is the **paid guide** (the dossier); the site is the
proof layer and the funnel toward it. Every content decision serves this. The doctrine:

**Articles reveal the destination's real swamps; the guide charts the crossing.**

- A **swamp** is genuinely difficult terrain a first-timer will cross anyway — a real,
  high-stakes, *connected* decision. Real means an experienced traveler would nod. A
  manufactured swamp is a lie about the landscape and burns the trust the price depends on.
- The article **fully answers its own question first** — nothing the reader came for is
  ever withheld. THEN it turns: reveals that this question sits inside a bigger, connected
  decision, and hands off to the guide as the place the connections are already worked out.
- **Three intensities:** full turn · light seed · **dry ground stays dry**.
- Handoffs point at the guide via the **guide-span** (hard rule 15); the dossier build names
  the guide and the name is backfilled through the admin.

**Conversion is only half of it — the articles must also SUPPLY the guide.** Run the
dossier's synthesis audit EARLY (~20 articles), plan the next batches into the vein it
measures, and enforce: **an article carries one piece of the vein, never three.**
`references/3b-vein-and-citability.md`.

**And the swamp tags must reach the DB.** The tag in `article-list.json` is what Stage 4
carries into `articles.swamp`; the surfaces read the DB. A site whose list has swamps but
whose DB has two tagged rows (Rome, 2026-10) has a conversion layer that renders on two
pages. Gate: `fleet-gate` SWAMP — `swamp_tagged / published ≥ 0.25` on any site with a live guide.

## State first, always — and state is data, not memory

`travel-facts/<project>/state.json` is the source of truth for progress. **Before doing
ANYTHING on a project, read it.** After every step boundary, the session updates and
commits it. Template: `assets/state-template.json`. Required fields now include
`site_url`, `launched` (first `published_at`), `published_count`, `guide.{live,price}`.

Because state rots when it is maintained by hand (5 of 9 projects read `stage: writing,
batch: 1` while live with shipped books, 2026-10-14), it is also **reconciled
mechanically**: `fleet-gate` STATE fails when `stage=="live"` disagrees with
`www 200 && published>0`, and `state-reconcile.mjs --apply` rewrites the file from the DB,
the live site and `common.sites`. If state.json doesn't exist, the project is new → Stage 1.

## Built through Claude Code — three things learned the expensive way

**Look at the pictures.** Filenames are stock slugs. Contact-sheet with PIL and READ it.
Candidates for the user go in an Artifact picker, two per slot.

**Check what already exists before sourcing anything.** `<site>/content/batch-*/images/`
holds every photograph ever downloaded for the project.

**A script that reports PASS has not necessarily checked anything.** Read the *count* in a
gate's header before you trust its verdict. This is the single most common way a check has
lied here, and it is why `0-gates.md` exists.

## The stage files (read only the one you need)

| Stage | When | Read |
|-------|------|------|
| 0 Gates | before trusting any PASS; before writing any new check | `references/0-gates.md` |
| 1 Architecture | new site; schema/config/admin/deploy work | `references/1-architecture.md` |
| 1c Opportunity gate | article list drafted, nothing written yet | `references/1c-opportunity-gate.md` |
| 2 Facts | state.stage = facts | `references/2-facts.md` |
| 3 Writing | state.stage = writing | `references/3-writing.md` |
| 3b Vein + citability | any site with (or planning) a dossier | `references/3b-vein-and-citability.md` |
| 4 Publishing | state.stage = publishing | `references/4-publishing.md` |
| 5 Design | site built + content live | `references/architecture/design-step.md` |
| 5b Features | during Stage 5 | `references/5-features.md` |
| 5c Conversion | guide has a checkout link | `references/5c-conversion.md` |
| Live | design approved | `references/4-publishing.md §9` — now `fleet-gate --sites <s>` green |
| Affiliates | stage 4's affiliate step | `references/affiliates.md` |
| 6 Fleet ops | console / checker / agents / onboarding / the weekly gate | `references/6-fleet-ops.md` |

## The contracts (data does the remembering, not prose)

One folder per project in the facts repo. Each file carries `schema_version`; scripts check it.

- `article-list.json` — approved titles + slugs + category_slugs, plus OPTIONAL `role` + `links`.
  **v4** adds the swamp layer (`swamps[]`, per-article `swamp` + `handoff`). **v5** adds the
  vein layer. A v3 list without the swamp layer is VALID — never retrofit a live site's list
  uninvited; a retrofit is a ★ request (and, when granted, is a SQL + list change together —
  the DB and the list must agree, gate SWAMP).
- `facts.json` — the ONLY facts file in the repo: cross-checked, reconciled (Stage 2), with
  provenance (`source_url, source_kind, checked_at, review_after, scope, support`).
  **Known gap (2026-10):** `common.facts` has no `review_after` / `source_kind` / `support`
  columns, so provenance is validated on the file and dropped at birth. Until migration
  0010 adds them, `review_after` lives in `note` as `review_after=YYYY-MM-DD`.
- `corrections.json` — accumulated local fixes that override AI output. Stage 3 MUST load it.
- `travel-facts/<project>/<site>-facts.sql` — append-only seed of every spanned fact.
  Seeds only — `common.facts` is the source of truth after birth; the checker + console
  maintain it (Stage 6). The seed is applied by `validate-batch.mjs --seed` (PostgREST
  upsert with the service key), not by pasting into Studio.
- `state.json` — progress, as above.

## Hard rules (each lives here and ONLY here — stage files link back)

1. **Facts come from facts.json; recommendations from its pools.** Never invent facts,
   hotels, attractions, or prices. Never freeze `serve_live` values into prose.
2. **FACTS and RECOMMENDATIONS reconcile oppositely.** Agreement on a fact is a signal, not
   proof; disagreement is a red flag. Agreement on a recommendation is confidence;
   disagreement is more options.
3. **Mutate HTML only through a DOM** (cheerio/DOMParser). Never `String.replace()` on raw HTML.
4. **Every Supabase client is schema-pinned — never bare `createClient`, never inline keys on
   the command line.** Apps pin from `SITE.dbSchema`; scripts pin from `SUPABASE_DB_SCHEMA` in
   `.env` and refuse to run without it. The `common` read client is anon; **writes to `common`
   use a service-role client** — anon writes are RLS-blocked and fail silently.
5. **Imports land as DRAFT, idempotently.**
6. **Affiliates are a separate explicit phase** with mandatory disclosure, programs only from
   `SITE_CONFIG.affiliates`, THIS site's own IDs, and **exactly one mechanism: `/go/`**. No
   third-party link-rewriting scripts in the page (a Travelpayouts "drive" script shipped on
   one site for months; it is outside the contract and outside every gate).
7. **No sex-tourism content, ever.**
8. **Corrections are law.**
9. **Content stages never alter schema.** Schema belongs to Stage 1 (and migrations in Stage 6).
10. **Media host ≠ folder name — and each lives in exactly ONE place.** `SITE.media.host` is
    the fleet delivery domain; `SITE.media.folder` is the per-site path. **The R2 object key IS
    the public_id, WITHOUT an extension** (a key ending `.jpg` in `site_settings.guide_cover`
    is a defect even when Cloudflare tolerates it). Explicit `ContentType` on every upload.
    **Every in-body image URL carries `width=1200`** in sorted options (34 full-resolution
    originals, one of 3.7 MB, shipped on Morocco for months; gate: corpus-check `noW == 0`).
11. **No contact email unless the user asks for one.**
12. **No fake or non-functional UI.**
13. **Never present static data as live.**
14. **Fleet-ops changes facts/content only through the human gate.**
15. **The guide is referenced ONLY through a guide-span** — `<span class="guide"
    data-guide="name">neutral gloss</span>`; the admin's Name backfill rewrites the inner
    text; glosses must be byte-identical across a site (one capitalised variant breaks the
    backfill's idempotency — gate: corpus-check `gloss == 1`).
16. **Make the FACTS citable, never the THESIS.**
17. **Web fonts load from a `<link>` in `app/layout.tsx` built from `SITE.brand.fonts` —
    never a CSS `@import`.** PostCSS inlines `tokens.css` above any `@import`, the import
    stops being the first rule, the browser drops it silently, and the whole identity falls
    back to Georgia/Impact. Vietnam shipped that way and was found by an outside reader;
    Rome was still shipping that way on 2026-10-14. `skeleton-check` fails on a font
    `@import`; `fleet-gate FONTS` and `render-check fontsLoaded` prove the served result.
18. **Every `/go/` hit is classified at write time.** `logGoClick` stores the user agent
    (never null), sets `is_bot` from the UA *and* from "no referer", and `/go/guide/[src]`
    accepts only the surfaces 5c names (anything else logs as `unknown`). A click log that
    cannot tell crawlers from readers is not an instrument (6,565 rows, 5,031 unclassifiable,
    2026-10).

## Free-tier verification model (no paid AI APIs)

The division of labor: **scripts prepare, the session is the panel, scripts reconcile, the
user judges the ≤5 disputes that have no official source, scripts validate, the user reviews
voice.** The old "user pastes prompts into Gemini/DeepSeek" step is retired unless the user
re-enables it (★ decision 3's default is official-source verification, not a second model).

- `scripts/make-prompts.mjs` still emits the prompt files (for the optional external pass).
- `scripts/reconcile.mjs` diffs returned JSONs into `facts.candidates.json` + `disputes.md`;
  it never writes `facts.json`. A fact counts as agreed only when EVERY panel member
  supplied a matching value.
- `scripts/validate-facts.mjs` checks provenance on every span actually used.
- `scripts/validate-batch.mjs` runs every mechanical check and prints its denominators.

## Quality gate (the only human-judgment items — 5, capped)

- [ ] Audience voice consistent; comparisons/framing match this audience
- [ ] Geographic accuracy plausible
- [ ] Safety advice honest, not alarmist; matches facts.json
- [ ] Recommendations traceable to facts.json pools
- [ ] Affiliate placements feel natural

## Definition of done (a batch of 5)

`validate-batch.mjs` passes with counts; second gate run in-session and fixes applied;
imported as drafts; links resolved and injected; new facts seeded (`--seed`); Start Here set;
affiliates + disclosure in; human voice gate passed; published via bulk-publish;
**state.json advanced and committed by the session**; `fleet-gate --sites <s>` green.
First batch of a new site: sitemap submitted (A-5) and `onboard-check.mjs` green.
