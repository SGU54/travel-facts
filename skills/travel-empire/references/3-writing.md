# Stage 3 — Writing (batches of 5)

Turn facts.json into finished drafts, five at a time, in the project's audience voice — then
run the second gate before anything enters publishing.

## Required inputs (load ALL three, every batch)

1. `article-list.json` — which 5 articles this batch covers (title, slug, category_slug).
2. `facts.json` — the only permitted source of facts and recommendation pools.
3. `corrections.json` — **mandatory.** Every recorded correction overrides facts.json and
   any AI output (hard rule 8). If a correction touches this batch's topics, it wins. New
   corrections discovered during this batch get appended and pushed with state.

## Batching

Exactly **5 articles per batch**; a 60-article site = 12 batches; one batch fully written →
second-gated → published before the next begins. Order batches by buying-intent tier from
the article list (money pages first) when the user wants revenue early; size never changes.

## Article shape

- **Length: 1000–1200 words by default.** Sanctioned exceptions when the topic genuinely
  demands it: list-type articles (packing, phrases) may run 800–1000; multi-day itineraries
  may run 1200–1600. Never pad or amputate to hit the band — that destroys the quality the
  rest of the pipeline protects. Outside these ranges, flag it to the user instead.
- **Audience voice.** Flight origins from the audience's hubs, money in their currency terms,
  comparisons to home, the concerns this audience actually has. Locale/units come from
  facts.json `_meta.locale` — data, not vibes.
- **Structure:** intro that answers the query fast; H2 sections with H3 sub-blocks (no wall
  of sibling H2s); price/summary folded into headings where natural; scannable; mobile-first;
  practical specifics over fluff.
- **Answer-first chunks (hard rule 16).** Every H2 opens with a **self-contained answer of
  40–80 words**: subject restated (never open on "it", "this", "that", "these", "as
  mentioned above", "here's why" — a pronoun with no antecedent is what makes a chunk
  unliftable), the entity named, the number given inside its fact-span. Then the nuance and
  the H3s, written for the human as before. This is the first 40–80 words under each H2,
  not a format for the article. Mechanically gated in `validate-batch.mjs`.
- **Carry ONE piece of the vein, never three (the pre-join guard).** On a site whose
  `article-list.json` has a `vein` block, the article's `piece` tag names which brick of
  the paid guide this article supplies. Cover it fully; naming three pieces in one article
  hands over the connection the guide is sold for — free, and in the most extractable form
  possible. Fixing a pre-join is never withholding: keep every fact the reader came for,
  cut the JOINING sentence ("and because X, Y also means Z"). Doctrine, contract, gates:
  `references/3b-vein-and-citability.md`.
- **Facts locked to facts.json.** `serve_live` values are NEVER frozen into prose — write
  "check the current rate" or a live-served range, never a hard number.
- **Fact-spans (pass 2): statable volatiles get SPANS, not dodges.** For facts.json entries
  with status `verify_recommended` (or YMYL `verified` values worth keeping fresh — fees,
  visa day-counts, policy figures), STATE the number in prose wrapped in a fact-span instead
  of avoiding it:
  `Americans get <span class="fact" data-fact="entry.visa_free_days">visa-free 60 days</span>.`
  The inner text is the honest current value AND the fail-closed fallback; the site's render
  path keeps it fresh from the shared fact DB (`common.facts`). Rules: one fact per span;
  wrap the VALUE only, not the sentence; key = dotted `domain.name` (e.g. `money.atm_fee`,
  `entry.fee_arrival`); real characters, never entities. The "wrong in a year?" test decides
  what gets a span — everything stable stays plain prose; true `serve_live` values (exchange
  rates) still use the live converter, unstored. Each spanned fact MUST also be emitted to
  the seed SQL (below) or the span just shows its fallback forever.
- **A drift-prone value NEVER goes in a heading, `title`, or `excerpt`.** None of those can
  carry a span, so the value freezes there while the spanned copy below it keeps updating —
  and the page ends up contradicting itself. Put the value in prose (spanned) and keep the
  heading value-free: `## Your passport: how much validity you need`, never
  `## Your passport: the 150-day rule`. Same for the article `title` and `excerpt`, which the
  resolver never touches at all. This is not hypothetical: Turkey shipped an H2 reading "the
  150-day rule" whose body argued the figure was *stricter* than the correct six months —
  the wrong number in the heading is what made it read as a considered editorial claim
  instead of a number someone could fix, and it survived every review because headings look
  like structure, not data. Trip lengths in itinerary titles ("7 Days in Turkey") are fine:
  a 7-day itinerary stays 7 days. The test is the same "wrong in a year?" one.
- **Model-panel consensus is NOT a source for a YMYL entry rule.** Where facts.json carries a
  reconciled panel value for a visa, passport, vaccination or advisory fact, verify it against
  the OFFICIAL source (travel.state.gov and the relevant US embassy page for a US audience)
  before it reaches prose. Turkey's panel ruled "150 days" over the generic six-month default
  and explained why — confidently, in writing, and wrong. Generic web search does not settle
  these either: the same query returned visa-free and a $57 e-visa, 150 days and six months.
  Fetch the official page.
- **Emit the fact seed SQL (same batch, same moment).** For every fact spanned this batch,
  append an idempotent upsert block to `travel-facts/<project>/<site>-facts.sql` (create on first
  use; append-only, never rewrite prior blocks). One row per fact:
  `(scope=site schema, key, value jsonb, status, checked_at=now(), source_url)` with
  `on conflict (scope, key) do update`. STATUS IS A DIRECT MAP of facts.json's own flag —
  `verify_recommended → 'provisional'`, `verified → 'verified'` — never self-promote AI
  research to verified. source_url comes straight from facts.json (never invented). Full
  contract + examples: the template's `docs/fact-emission.md`. The DB is the source of truth
  after seeding — this file only BIRTHS facts; the fleet checker + console maintain them
  thereafter (Stage 6, `references/6-fleet-ops.md`). A spanned fact with a machine-extractable
  official source is a candidate for a `check` config so the checker auto-verifies it.
- **Guide handoffs — write the article's swamp assignment (this is the conversion layer).**
  Load the article's `swamp` + `handoff` tags from `article-list.json` before drafting.
  The doctrine (SKILL.md "The guide is the center"): the article reveals a real swamp; the
  paid guide charts the crossing. Three intensities, fixed by the tag:
  - `turn` (high-intent decision pages): the article answers its own question FULLY and
    honestly first — withholding the answer is an auto-fail — then a short closing section
    makes the **turn**: reveal that this decision is one node in a bigger connected decision
    (name the real stake: what actually goes wrong), then hand off to the guide as where
    the connections are worked out. The turn emerges from the article's own expertise
    ("notice what happened across all of this…"), never from a warning label. No fear
    words, no false urgency: the register is knowledgeable friend, not marketer.
  - `seed` (broad top-of-funnel pages): ONE sentence, planted where the topic naturally
    touches the swamp. No dramatics, no dedicated section.
  - `none` (dry ground): no handoff. Never manufacture a swamp — a puddle sold as a bog
    is the aggression failure and burns sitewide trust.
  Every handoff names the guide through the **guide-span** (hard rule 15):
  `<span class="guide" data-guide="name">the complete Greece trip guide</span>` — neutral
  gloss inner text, standalone-noun phrasing, sentence must survive the later name swap.
  The handoff points at the guide's *system* (the sequencing chart, the connected map),
  never "the answer is inside." One guide-span per `turn` article (at most two if a seed
  higher up is natural), one per `seed` article, zero on `none`.

- **Scope note for handoffs:** the swamp named in a turn MUST be the article's assigned
  swamp from the list — don't freelance a different one mid-batch. If drafting reveals the
  assignment is wrong (the article actually sits on a different swamp, or on dry ground),
  STOP and update `article-list.json` first, then write. The list is the contract the
  dossier build will later reconcile against.

- **Recommendations from the pools:** lead with `core`, use `optional` as extras.
- **Image slots (SCAFFOLDING ONLY — they must not survive to import):** mark each in-body
  image as `<!-- IMAGE_SLOT_n: what it shows -->` in the draft and record its intended alt
  text. These comments render as NOTHING (bodies render via `dangerouslySetInnerHTML`), so
  Stage 4 (step 3.5) MUST rewrite every slot into a real `<figure><img loading="lazy">` tag
  with a delivery URL carrying `width=1200`. The hero is `featured_image` (template-rendered,
  never in the body).
  Never hardcode image URLs at this stage. If a live build ever shows missing in-body images,
  the cause is almost always a slot comment that was never converted — grep the imported HTML
  for a literal `IMAGE_SLOT`.
- **Feature blocks:** most articles should carry a FAQ block; itinerary/area articles a
  map; money articles live-price spans and one converter. Conventions + rules (coordinates
  are facts, etc.): `references/5-features.md`.
- **Titles/excerpts — real characters, not HTML entities.** Author apostrophes/quotes as
  real characters (`'`, not `&#39;` / `&apos;`). Entities authored into the title render
  literally ("Barcelona&#39;s") wherever the field is shown as text. Belt-and-braces: the
  template's render path decodes entities (lib/decode.ts `decodeEntities`, applied in
  ArticleCard, the article h1 + metadata, and FeaturedGrid) — because stored data may
  already contain entities, the decode helper is the robust fix; clean authoring alone is
  fragile.
- **Affiliate slots — place them BY INTENT as you write (this is the monetization).**
  When a passage recommends something bookable, drop an affiliate SLOT inline. The slot
  names a ROLE, never a URL or vendor — the vendor + this site's ID + the link are
  resolved at render through `/go/`, and a slot renders as a link ONLY once a credential
  is configured (else it degrades to plain prose — fail-closed). So place slots
  generously; they light up as approvals land, fleet-wide, with zero article edits.

  Syntax (the `class="aff"` + `data-aff="role"` is the contract the render layer reads):
  ```
  where to <span class="aff" data-aff="hotels">stay in Trastevere</span>
  <span class="aff" data-aff="flights">flights from the US</span>
  <span class="aff" data-aff="tours" data-item="colosseum">skip-the-line Colosseum tickets</span>
  <span class="aff" data-aff="insurance">travel insurance</span>
  <span class="aff" data-aff="rail">train tickets</span>
  ```
  Roles are the KEYS of the site's `affiliates` config (hotels/tours/flights/rail/
  insurance/…) — use those exact strings, they must match the policy table's roles.
  Rules:
  - The inner text is REAL, complete prose that reads fine even if the slot never links
    (it's the fallback). Write "book your **Colosseum tickets**", not "click **here**".
  - Generic by default: a BARE slot (`data-aff="hotels"`, no `data-item`) searches the
    site's DESTINATION — a hotels slot → "hotels in Rome" with your id. We do NOT
    recommend specific properties in free articles (that's the paid guide's job).
  - `data-item` is the per-article AREA OVERRIDE: `data-item="trastevere"` narrows the
    same generic search to a neighborhood. Use it when a neighborhood is more relevant
    than the whole city — still a search, never a specific property.
  - Place where a real reader is ready to act: where-to-stay articles → a hotel slot in
    the lodging recommendation; itineraries → a ticket/guide slot on the sight; arrival
    articles → nothing bookable, no slot. One or two well-placed slots beat ten.
  - NEVER write a raw vendor URL or a bare `/go/` link — always the slot span. Disclosure
    ships from the template (Stage 4 concern), not the prose.

## Scope discipline (ranking/list articles drift HARD — recurring bug)

"Best of" / ranking / comparison articles naturally pull toward famous places that are OUT
of scope. Real cases: a "most romantic islands" and "best beaches" list drifting to islands
not in facts.json; a "best ruins" list. Two rules:

- **Constrain every ranking/list/comparison to in-scope destinations from facts.json.** If a
  place isn't in facts.json's pools, it isn't a candidate — no matter how famous. Sites have a
  defined scope (e.g. "Athens + 5 classic islands"); honor it. Mainland *sites* you visit FROM
  an in-scope base (a day-trip ruin) are fine; out-of-scope *destinations* recommended as a
  place to go are not.
- **Out-of-scope substring checks MUST be word-bounded** (`\bios\b`, not `ios`). Unbounded
  matches fire on innocent substrings ("ios" inside "Agios"/"Prokopios"), producing false
  flags. Validate scope with word boundaries, then eyeball the real hits.

## Don't appropriate the regional to the destination country

A destination often shares its food, crafts, and rituals with a wider region, and writing
about them as if the destination *invented* or *exclusively owns* them is both factually
wrong and a form of erasure of the neighbours who share the tradition. This bit a Morocco
build: couscous, tagine, mint tea, the hammam, argan, sfenj are Maghrebi / North African (some
wider still), not Moroccan inventions. The distinction is origin-vs-variant:

- **OK — describing the local variant or practice.** "Moroccan hospitality", "Moroccan
  salads", "Moroccan sweets", "Moroccan cuisine", "the Moroccan tagine" (= the Moroccan version
  of the dish), "make a tagine". These claim a local rendering, not authorship.
- **NOT OK — attributing origin or exclusivity to the destination.** "a quintessentially
  Moroccan experience" (of the hammam), "sfenj (Moroccan doughnuts)", "Morocco's own
  couscous", "uniquely Moroccan", "invented/originated in Morocco". Rewrite to the true scope
  ("North African", "Maghrebi", "traditional across the region") or drop the origin qualifier.
- **Stay accurate without a geography detour.** Same discipline as any cross-border fact (e.g.
  argan also grows in western Algeria): correct the claim in a clause, don't turn the article
  into a lesson about the neighbour. The destination is still the subject.

This is a writing rule, not a fact-file rule — facts.json won't flag it, and an external
second-gate model called it a non-contradiction ("not in facts.json but no conflict"). It has
to be caught at authoring time.

## Second-gate findings are AUDITED, never auto-applied

External models mechanically match prose against facts.json — so when a facts.json field has
gone STALE (especially YMYL: visa fees, entry rules, launch dates), the model will flag your
web-verified-current figure as an "error" and tell you to revert to the stale one. Don't.
Audit each finding: confirm real catches, reject reversions to outdated facts, and when
facts.json is the thing that's stale, FIX facts.json (with a dated note) so the false flag
stops recurring. The gate catches real contradictions too — keep those — but it has no
knowledge of what's current, only of what the fact list says.



After the 5 are written: ONE strong external model, ONE paste containing all 5 articles plus
facts.json, asking only for **in-context errors** — a date that contradicts a later sentence,
a price stated two ways, a claim that reads wrong in a paragraph, a recommendation that
drifted from facts.json. (The full panel was for establishing facts; this gate hunts
contradictions, so one capable reader suffices — that's 1 round trip per batch, not 20.)
Apply fixes; record any durable lesson in `corrections.json`.

**Same paste, second rubric — score the batch's handoff articles on Pull × Trust.** Include
the batch's swamp assignments in the paste. **`turn` articles get both axes; `seed`
articles get Trust ONLY** — a seed is one sentence and has no turn, stake, or revealed
connection to score, so Pull structurally cannot apply to it (a seed failing "no turn
exists" would be the rubric misfiring, not the article). Score 0–100, WITH the failing
reason:

- **PULL — does the article make the reader SEE the swamp?** Sub-checks: a genuine turn
  exists (not a tacked-on CTA); a real stake is named (something that actually goes wrong);
  a *connection to other decisions* is revealed (not a restatement of the article); the
  handoff points at the guide's system, not "the answer's inside".
- **TRUST — is it honest and proportional?** Sub-checks: the reader's original question is
  fully answered BEFORE any handoff (withheld answer = automatic 0); the swamp is real (an
  expert would nod), not manufactured or inflated (a puddle sold as a bog); intensity
  matches the tag (a heavy turn on a `seed` page fails here); no fear-words or false
  urgency; guide mentioned once (twice max), not a drumbeat.

**The gate: `turn` passes on PULL ≥ 60 AND TRUST ≥ 80; `seed` passes on TRUST ≥ 80.**
Trust is a hard floor Pull can never buy
down — that single AND is what stops drift toward the hard sell (cranking urgency raises
Pull and tanks Trust). Too light fails Pull; too aggressive fails Trust; only the balanced
middle ships. Fix and re-check failed articles before import. Treat the scores as a
**craft-consistency gate, not a revenue oracle** — the model predicts persuasion, it does
not measure sales. Real conversion truth arrives later, per article, from guide sales data;
never mistake a passing score for proven revenue.

**Calibrate on first use — the thresholds are asserted, not proven.** Before trusting the
gate on a real batch, score four reference shapes and check the verdicts land right:
a proper turn (full answer, honest reveal, system handoff) → PASS both axes; the same
article with urgency cranked and the answer teased → high Pull, TRUST FAIL; the raw
article with no handoff at all → high Trust, PULL FAIL; a heavy turn bolted onto a broad
top-of-funnel page → proportionality TRUST FAIL. If the sleazy version clears Trust 80,
the threshold (or the rubric prompt) is wrong — fix the instrument before trusting a pass.

Mechanical checks that belong in `validate-batch.mjs`, not the paste: every `turn`/`seed`
article contains ≥1 `span.guide` with `data-guide="name"` and non-empty inner text; every
`none` article contains zero; no literal `{{` token anywhere; the span count per article
is ≤2. Plus the two 3b gates on the same run: **answer-first** (every H2 opens on a
self-contained 40–80-word block) and **pre-join** (no article names ≥3 vein pieces). All of
these need the list: `node scripts/validate-batch.mjs import-batch-NN.json --list article-list.json`.

## Handoff

Update `state.json` → `batch_status: "written"`, push, and hand the 5 articles to Stage 4.
If this batch spanned any facts, the appended `travel-facts/<project>/<site>-facts.sql` block goes
with them — the user runs it (service role) at publish time so the new spans resolve to live
values instead of sitting on their fallbacks.
