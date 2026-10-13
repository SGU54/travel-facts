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
  onboarding a live site. Triggers: new travel site, launch/scaffold/resume
  [project], build/check facts, reconcile, write batch N, clean/link/publish, import
  batch, fleet console, facts checker, check config, link-rot agent, onboard [site],
  common schema migration, swamp list, guide handoffs, backfill guide name,
  opportunity gate, should we write this, reject rules, search volume, winnable
  SERP, article predictions — or any
  project name + lifecycle verb. Read state.json FIRST for site work; open only the
  relevant stage reference (6-fleet-ops.md for fleet ops).
---

# Travel Empire — one skill, five stages

Everything runs through one pipeline with one source of truth for progress. A **project =
destination + audience** (e.g. `romeforamericans`). Same country, different audience =
different project (visa, money framing, flight origins all change).

```
STAGE 1  ARCHITECTURE  empty correct site (minimalist template look) + approved categories & article list
STAGE 1c OPPORTUNITY   the pre-writing gate: every article-list row gets REJECT /
                       INVESTIGATE / PRODUCE / STRUCTURAL, with a written reason and a
                       filed prediction. Volume is the target, winnability the filter —
                       never the reverse. (1c-opportunity-gate.md)
STAGE 2  FACTS         facts.json built, cross-checked (manual AI panel), reconciled
STAGE 3  WRITING       batches of 5 articles from facts.json, second-gate checked
STAGE 4  PUBLISHING    clean -> images -> import (draft) -> links -> affiliates -> publish
         (3 and 4 repeat per batch until the article list is done)
STAGE 5  DESIGN        restyle the BUILT site into a distinct identity (after infra is real),
                       then ship the standard UX/SEO feature set (5-features.md) + go-live checklist
STAGE 5c CONVERSION    the guide's own selling surfaces — SEVEN, intent-gated: /guide
                       sales page, end band, inline marker, sticky aside, category
                       band, trip-tool callout, home band — ONLY on a site whose guide
                       has a checkout link; fail-closed everywhere else. 5c MOUNTS;
                       the marketing skill writes the hooks/copy + the placement map.
                       (5c-conversion.md)
         LIVE          set NEXT_PUBLIC_SITE_URL, deploy real DNS, submit sitemap to GSC → stage: "live"
STAGE 6  FLEET OPS     empire-wide layer ABOVE any one site: the console, the facts checker,
                       the agents. A new site is ONBOARDED into it, not built by it. (6-fleet-ops.md)
```

**Design comes LAST, not first.** The site is built on the neutral **minimalist template look**
and only restyled once the real architecture, components, and content exist. This is deliberate
and reverses the old order: designing up front produced mockups the build then ignored, shipping
the template default anyway. Styling the *actual rendered site* — real components, real content,
real responsive behavior — is the only way the design that's approved is the design that ships.

## The guide is the center — the swamp doctrine

Search traffic no longer pays for article volume (AI answer boxes absorb informational
queries). The fleet's revenue engine is the **paid guide** (the dossier); the site is the
proof layer and the funnel toward it. Every content decision serves this. The doctrine:

**Articles reveal the destination's real swamps; the guide charts the crossing.**

- A **swamp** is genuinely difficult terrain a first-timer will cross anyway — a real,
  high-stakes, *connected* decision (Greece: which boat the day before the flight; Rome:
  where to sleep given the walkability thesis). Real means an experienced traveler would
  nod. A manufactured swamp is a lie about the landscape and is the fastest way to burn
  the trust the guide's price depends on.
- The article **fully answers its own question first** — nothing the reader came for is
  ever withheld (a withheld answer is a paywall and reads as one). THEN it turns: reveals
  that this question sits inside a bigger, connected decision, and hands off to the guide
  as the place the connections are already worked out. The guide sells the *map of the
  swampland*, never the single answer.
- **Three intensities, matched to the page:** full turn (high-intent decision pages on a
  real swamp) · light seed (one sentence on broad top-of-funnel pages) · **dry ground
  stays dry** (no swamp → no handoff beyond at most a nav-level mention; never dig a bog
  in a meadow).
- Handoffs point at the guide via the **guide-span** (hard rule 15) — articles are written
  before the guide exists or is named; the dossier build names it and the name is
  backfilled through the admin. Articles need the swamps and the pointer, never the PDF.

**Conversion is only half of it — the articles must also SUPPLY the guide.** The swamp
layer makes an article POINT at the guide; nothing in it makes the article CONTAIN the
material the guide will later connect. That gap is what cost Japan its dossier (84 articles
written against a hypothesis, one usable vein, already pre-joined in a single article). The
fix is to run the dossier's synthesis audit EARLY — around 20 articles — plan the next
batches into the vein it measures, and enforce the one rule that keeps the product
sellable: **an article carries one piece of the vein, never three.** Doctrine, contract and
gates: `references/3b-vein-and-citability.md`.

Where it lives in the pipeline: Stage 1 drafts the **swamp list** and tags the article
list (contracts below) → Stage 3 writes the handoffs and the second gate scores them
(Pull × Trust, `3-writing.md`) → the dossier skill mines the corpus, proposes the guide's
NAME, the user confirms, and the confirmed name is backfilled into every guide-span via
the admin's batch update. Awareness flows forward only; the build order never changes.

During Stage 5, also ship the **standard site-wide feature set** (reading time, TOC, breadcrumbs,
JSON-LD suite, RSS, 404, skip-link, trust/best-time/cost strips, itinerary picker) — see
`references/5-features.md`. These are no-API/no-cost and are what make the site feel designed and
useful rather than a bare article list. Then run the **go-live checklist** in `4-publishing.md §9`.

## State first, always

Every project has `state.json` in the facts repo:
`https://raw.githubusercontent.com/SGU54/travel-facts/main/<project>/state.json`

**Before doing ANYTHING on a project — new chat or turn 400 of an old one — fetch and read
state.json.** It answers: which stage, which batch, what the batch's sub-status is, which
slugs are published. Never trust the chat scroll; trust state. After every step boundary,
output the updated state.json for the user to push (assistant has no repo access — the user
is the transport for all repo writes). Template: `assets/state-template.json`.

If state.json doesn't exist, the project is new → Stage 1.

## Built through Claude Code — what that changes

The whole pipeline now runs here, in a terminal with the repos and the volume mounted.
Three consequences worth stating, because each one was learned the expensive way:

**Look at the pictures.** Image filenames are stock slugs and say nothing. Whether you
are picking for an article or for the book, build a contact sheet and READ it — PIL does
it; there is no ImageMagick on this machine. For candidates the user must choose between,
publish the sheet as an **Artifact** (Stage 4 §3): a visual picker, two candidates a
slot, not a list of links.

**Check what already exists before sourcing anything.**
`<site>/content/batch-*/images/` accumulates every photograph ever downloaded for that
project, with `batch-NN-images.md` naming each batch's topics. One project's paid PDF
shipped with six plates while 168 usable landscape frames sat unused in that folder.

**A script that reports PASS has not necessarily checked anything.** Every gate in this
empire keys off exact class names, ids and file names. Point one at a site that uses
other names and it measures nothing and says fine. Read the *count* in a gate's header —
"23 chapters, 7 decisions" — before you trust its verdict. This is the single most
common way a check has lied here.

## The stage files (read only the one you need)

| Stage | When | Read |
|-------|------|------|
| 1 Architecture | new site; schema/config/admin/deploy work | `references/1-architecture.md` |
| 1c Opportunity gate | article list drafted, nothing written yet; "which of these should we actually write", volume/SERP/winnability, reject rules, predictions | `references/1c-opportunity-gate.md` |
| 2 Facts | state.stage = facts; "build/check the facts" | `references/2-facts.md` |
| 3 Writing | state.stage = writing; "write batch N" | `references/3-writing.md` |
| 3b Vein + citability | any site with (or planning) a dossier: what the articles must SUPPLY it, and how to write chunks an AI answer engine can lift | `references/3b-vein-and-citability.md` |
| 4 Publishing | state.stage = publishing; "clean/import/link/publish" | `references/4-publishing.md` |
| 5 Design | state.stage = design; site built + content live; "now make it look good" | `references/architecture/design-step.md` |
| 5b Features | during Stage 5; ship standard UX/SEO feature set | `references/5-features.md` |
| 5c Conversion | guide has a checkout link; "build the guide surfaces / sales page / ad sidebar" | `references/5c-conversion.md` |
| Live | design approved; "set it live / launch / submit to GSC" | `references/4-publishing.md §9 (go-live checklist)` |
| Affiliates | during stage 4's affiliate step (often deferred to just after launch) | `references/affiliates.md` |
| Feature blocks | writing maps/FAQ/live-money/TikTok into articles | `references/5-features.md` |
| 6 Fleet ops | the console / facts checker / `check` configs / agents; onboarding a live site into the fleet | `references/6-fleet-ops.md` |

## The contracts (data does the remembering, not prose)

One folder per project in the facts repo. Each file carries `schema_version`; scripts check
it before running.

- `article-list.json` — approved titles + slugs + category_slugs, plus OPTIONAL per-article
  `role` + `links` (the link plan — drives Start Here + internal links; see article-plan.md).
  **Schema_version 4 adds the swamp layer:** a top-level `swamps` array (the destination's
  hypothesis-grade terrain map, drafted in Stage 1 — 5–10 entries of
  `{id, name, one_liner}`) and per-article `swamp` (an id from that array, or `"none"`) +
  `handoff` (`"turn" | "seed" | "none"`). The swamp list is a HYPOTHESIS — the dossier's
  cold-mine may re-rank it at guide-build; that produces a small retrofit worklist, never a
  rewrite. Written by Stage 1, read by 2–4 and by the dossier skill. **A v3 list without
  the swamp layer (pre-doctrine sites: Thailand, Greece, Rome, …) is VALID — never
  retrofit a live site's list or articles uninvited; retrofit is its own user-requested
  task.**
  **Schema_version 5 adds the vein layer:** a top-level `vein` object (the MEASURED thesis —
  `thesis`, `measured{headroom,corpus_at_audit,date}`, `max_pieces_per_article`, and the
  `pieces[]` with their match regexes) and per-article `piece` (a piece id, or `"none"`).
  `swamp` and `piece` are different axes: swamp = which door to the guide this page shows;
  piece = which brick of the guide this page supplies. Written when the synthesis audit is
  first run (~20 articles), amended when re-run. Contract + gates:
  `references/3b-vein-and-citability.md`.
- `facts.json` — the ONLY facts file in the repo: cross-checked, reconciled (Stage 2). Drafts
  and raw AI returns NEVER go to the repo.
- `corrections.json` — accumulated local fixes that override AI output. Stage 3 MUST load it
  alongside facts.json. Template: `assets/corrections-template.json`.
- `travel-facts/<project>/<site>-facts.sql` — append-only seed of every fact the site's batches
  spanned (written by Stage 3, run by the user at publish). Seeds only — the shared fact DB
  (`common.facts`) is the source of truth after birth; the checker + fleet console maintain it
  thereafter (Stage 6, `references/6-fleet-ops.md`). Facts given a structured `check` config are
  auto-verified against official sources; the rest age until human review in the console.
- `state.json` — progress, as above.

## Hard rules (each lives here and ONLY here — stage files link back)

1. **Facts come from facts.json; recommendations from its pools.** Never invent facts,
   hotels, attractions, or prices. Never freeze `serve_live` values (rates, prices) into prose.
2. **FACTS and RECOMMENDATIONS reconcile oppositely.** AI agreement on a fact is a signal,
   not proof; disagreement is a red flag to resolve. Agreement on a recommendation is
   confidence; disagreement is more options. Never blur them.
3. **Mutate HTML only through a DOM** (cheerio/DOMParser). Never `String.replace()` on raw
   HTML for cleaning, links, or images. (Read-only *inspection* may grep.)
4. **Every Supabase client is schema-pinned — never bare `createClient`, never
   inline keys on the command line.** Two mechanisms, same value: the APPS pin
   from config (`SITE.dbSchema`, set once in site.ts — deliberately NOT an env
   var, so a deploy can't be mis-pointed); the pipeline SCRIPTS pin from
   `SUPABASE_DB_SCHEMA` in `.env` (and refuse to run without it — no default
   schema, ever). The `common` read client is pinned to `common` (anon,
   read-only); **writes to `common` (link_clicks, subscribers) use a
   service-role client — anon writes are RLS-blocked BY DESIGN and fail
   silently if you forget** (real fleet-wide bug, 2026-08).
5. **Imports land as DRAFT, idempotently.** A human reviews against the quality gate before
   anything publishes.
6. **Affiliates are a separate explicit phase** with mandatory disclosure, programs only from
   `SITE_CONFIG.affiliates`, and THIS site's own IDs.
7. **No sex-tourism content, ever.**
8. **Corrections are law.** A recorded local correction overrides any AI output, forever,
   via corrections.json.
9. **Content stages never alter schema.** Schema belongs to Stage 1 exclusively.
10. **Media host ≠ folder name — and each lives in exactly ONE place.** The host is the
    delivery domain shared by the whole fleet (`img.sgfleetmedia.com`); the *folder* is the
    per-site path segment (e.g. `greeceforamericans`). They are NOT the same and must never be
    conflated — baking the folder in as the host yields URLs that silently 404 (real bug: body
    images dead while helper-built heroes worked). Every image URL is built through
    `mediaUrl()` in `packages/config/site.ts` (aliased as `cloudinaryUrl` for the ~17 existing
    call sites), never hand-assembled. The host is `SITE.media.host`, the folder is
    `SITE.media.folder` — keep them distinct.

    **The fact that decides everything else: the R2 object key IS the public_id, WITHOUT an
    extension.** Keeping the same key is what let the entire fleet change CDN without touching
    a single database row (`featured_image`, `hero_image`, `categories.featured_image`,
    `guide_cover` were all left alone). Two consequences: an explicit `ContentType` on upload
    is CRITICAL, because with no extension it is the only thing identifying an object as an
    image; and an R2 folder is never provisioned — it is born from its first object.

11. **No contact email unless the user asks for one.** `SITE_CONFIG.contact.email` ships
    EMPTY (`''`). Header and footer already guard on it (`{SITE.contact.email && …}`), so empty
    = nothing renders. Only populate it when the user explicitly requests a contact address.
    (Recurring waste: a placeholder email shipped in chrome, then had to be removed by hand on
    every site.)
12. **No fake or non-functional UI.** Every interactive affordance ships wired to real behavior
    or does not appear. Search → real `/search` route; chips → real `/search?q=` or article
    links; itinerary picker → client-side routing to REAL existing articles (verify each slug
    exists). Never a dead input, a placeholder button, or a `<span>` that looks clickable. (The
    empire runs NO paid APIs — "smart" features are deterministic client-side routing, not AI calls.)
13. **Never present static data as live.** A hardcoded rate/ticker/"updated" badge that looks
    current but is baked-in silently goes stale and misleads. Either compute it client-side
    (local time is genuinely live and free), label it clearly as indicative, or omit it. This
    extends `serve_live` discipline from prose into UI chrome.
14. **Fleet-ops changes facts/content only through the human gate.** The checker and every
    agent DETECT and PROPOSE (needs_review + structured `proposed_value`, or a findings queue);
    a human approves in the console; every write is audited (a failed audit ABORTS the write).
    No agent edits an article or a fact value directly, and no agent modifies agent code —
    code changes go through a human and git. This is the pass-4/5 embodiment of "AI proposes,
    human is the authority." Details: `references/6-fleet-ops.md`.
15. **The guide is referenced ONLY through a guide-span — never a hardcoded name, never a
    raw token.** Articles are written before the guide is built or named, so every handoff
    names it through the span contract:
    `<span class="guide" data-guide="name">the complete Greece trip guide</span>`
    The inner text is a NEUTRAL, human-readable gloss that reads fine forever (fail-closed,
    same principle as fact-spans and affiliate slots) — a live article before naming shows
    the gloss, never a `{{TOKEN}}`. After the dossier build names the guide and the user
    confirms, the admin **batch update** rewrites every `span.guide` inner text to the real
    name via the admin's **Guide panel → "Name backfill"**
    (`POST /api/guide-name-backfill`, cheerio over every `span.guide`,
    dry-run by default, status never touched — hard rule 3 applies). Two phrasing rules so the swap is always
    clean: the span is referenced as a **standalone noun** ("that's charted in <span>…"),
    never leaning on the name's internal grammar; and the surrounding sentence must read
    correctly with BOTH the gloss and any plausible real name. Never invent or freeze a
    guide name in prose — naming belongs to the dossier build (cold-mined, user-confirmed),
    exactly as `serve_live` values belong to the fact DB.

16. **Make the FACTS citable, never the THESIS.** Every H2 opens with a self-contained
    answer of 40–80 words — subject restated (never a bare "it/this/as mentioned"), entity
    named, number given inside its fact-span — so an answer engine can lift an attributable
    chunk. That chunk answers THE ARTICLE'S OWN QUESTION and nothing wider. A chunk that
    joins three pieces of the site's vein is the paid guide's product, formatted for
    copying and given away: the two rules are one rule, and the second half is the half
    that costs money. Free articles say *what*; the guide says *therefore*. Doctrine, vein
    contract and the mechanical gates (answer-first, pre-join, guide-span):
    `references/3b-vein-and-citability.md`.

## Free-tier verification model (no AI APIs)

The user has no API budget. The division of labor is fixed: **scripts prepare, the user
pastes, scripts reconcile, the user judges disputes, scripts validate, the user reviews
voice.** Concretely:

- `scripts/make-prompts.mjs` emits ready-to-paste prompt files per external model.
- **The current Claude session counts as one panel member** (`ai_source: "claude"`) — the
  user only carries prompts to 1–2 external models, not four.
- `scripts/reconcile.mjs` mechanically diffs the returned JSONs into `facts.candidates.json`
  + `disputes.md` — it never writes `facts.json` itself and never settles a fact unless
  EVERY panel member supplied a matching value (one source answering and another returning
  null is `unverified`, not agreement — 2026-10-11 fix, see SKILL-CHANGES.md). The human
  promotes reviewed candidates into `facts.json` by hand.
- The second gate (written articles) uses **one strong external model, one paste** containing
  all 5 articles + facts.json — not the full panel.
- `scripts/validate-batch.mjs` runs every mechanical quality check; the human checklist is
  judgment-only and capped at 5 items.

## Quality gate (human judgment items — the mechanical ones live in validate-batch.mjs)

- [ ] Audience voice consistent; comparisons/framing match this audience
- [ ] Geographic accuracy plausible (neighbourhoods, distances, locations real)
- [ ] Safety advice honest, not alarmist; matches facts.json
- [ ] Recommendations traceable to facts.json pools; nothing smells invented
- [ ] Affiliate placements feel natural, not forced

## Definition of done (a batch of 5)

validate-batch.mjs passes; second gate run and fixes applied; imported as drafts;
link map built (`pick-links.mjs`) and injected (`inject-links.mjs`, dry-run eyeballed then
`--apply`); new facts seeded (the batch's `travel-facts/<project>/<site>-facts.sql` block run) if any
were spanned; Start Here path set (`pick-start-here.mjs`); affiliates + disclosure in; human gate
passed; published via admin; **state.json advanced and pushed**. First batch of a new site:
sitemap submitted to Search Console.
