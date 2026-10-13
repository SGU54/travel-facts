# Article plan — the destination-shaped content list

Phase 3 of the build. After the design is chosen and the category structure is derived,
produce the **article list**: the concrete set of articles the site will contain. This is a
PLANNING artifact (titles + slugs + category), not the articles themselves — the `travel-content`
skill writes them, builds their facts, and publishes them in 5-article batches.

## What it is

A flat list, each row:
- **title** — the article's working title (final wording can flex in writing)
- **slug** — URL slug (kebab-case, language-appropriate, stable; the content skill keys on it)
- **category** — which subcategory (or main) it belongs to, by slug, from the approved structure

60–80 articles is the target band; size to the destination (a dense country supports more; a
small city fewer). Quality of coverage over raw count.

## How to derive it (destination-shaped)

The list flows from the category structure, which flowed from the destination shape. So the
article mix differs by destination type:

- **Country** — per major city/region: a first-timer guide, things-to-do, where-to-stay,
  getting-around, day-trips; plus country-level itineraries (X days), transport (rail passes,
  domestic flights), food, and the Plan-your-trip set (visa, money, when-to-go, connectivity,
  safety). The cities/regions multiply the per-place articles.
- **City** — per neighborhood: an area guide; plus the city's sights, day-trips out, where-to-stay
  by area, getting-around, food scene, and the Plan-your-trip set. Depth is in areas + excursions.
- **Region/route** — per stop/leg along the route, plus route-level logistics and itineraries.

## The second derivation: the MEASURED vein (from article ~20 onward)

The taxonomy above answers "what does a traveller search?". It cannot answer "does this
corpus have anything to CONNECT?" — and that second question is what the paid guide lives
on. So the list is derived twice:

- **The base** — the Plan-your-trip set and the per-place spine, from the taxonomy. Always
  needed; unchanged.
- **The depth articles** — planned into the vein the synthesis audit actually measured, not
  into whichever subjects look SEO-shaped.

Run `dossier/scripts/audit-synthesis.py` as soon as ~20 articles exist (and again at 40),
score 3–5 candidate theses at an EQUAL number of themes, and plan into the winner. A thesis
scoring under 2 is already pre-joined across the corpus — planning depth into it is wasted
work. Record the result in the list's `vein` block (schema_version 5) so the batches that
consume it are not depending on chat memory. Full method, contract and the pre-join gate:
`references/3b-vein-and-citability.md`.

Writing 80 articles first and measuring afterwards is the Japan failure, and it is
expensive: the audit costs an hour, the corpus costs months.

## The third derivation: the OPPORTUNITY gate (before anything is written)

The taxonomy answers "what does a traveller search?". The vein answers "what can this corpus
CONNECT?". Neither answers the question that decides whether the work pays:

> **can THIS domain win the SERP, and is the query big enough to be worth winning?**

Measured on the fleet's own data, the per-place spine this file prescribes — things-to-do,
where-to-stay, best-X, N-day itineraries — is where the losers come from: 43 such pages carry
10 800 impressions at a median position near 70 and produce approximately zero clicks.

So the list is derived a third time. Every row gets REJECT / INVESTIGATE / PRODUCE /
STRUCTURAL with a written reason, and a prediction filed before the batch is written.
Rules, thresholds, back-test and the prediction record: `references/1c-opportunity-gate.md`.

Two things that file will tell you and that contradict the taxonomy above, so they are worth
stating here too:

- **Volume is the target variable, winnability is the filter — never the reverse.** Chasing
  easy queries maximises hit rate and produces pages worth 6 impressions a month.
- **A row this file prescribes may still be REJECT.** Cover the traveller's need from an
  angle the gate accepts, or mark the row `structural: true` and accept it will not rank.

## The Plan-your-trip set (near-universal, audience-shaped)

Almost every destination needs these, framed for the specific audience:
visa/entry, money/costs, when-to-go, getting-there (flights/arrival), getting-around,
connectivity (eSIM/SIM/wifi), safety/health, etiquette/culture, what-to-pack.
For a country-for-a-specific-audience site, the visa/entry and getting-there articles are
audience-specific (e.g. "do <audience> need a visa for <country>") — these are exactly the
articles whose FACTS matter most, and that the content skill will verify hardest.

## Link plan — declare linking intent as you plan (OPTIONAL fields)

Linking is a PLANNING decision, not a publishing one: you already know at plan
time which article is the visa guide and which is the anchor city. Declare it
now and the publishing scripts consume it (plan-first; the resolver only fills
what you leave unsaid). Two OPTIONAL per-article fields — absent = fully
automatic behaviour, so this is backward-compatible:

```jsonc
{ "title": "...", "slug": "...", "category_slug": "...", "tier": 1,
  "role": "anchor",                                    // OPTIONAL, see below
  "links": [{ "phrase": "Thai Digital Arrival Card",   // OPTIONAL explicit links
              "slug": "thailand-digital-arrival-card-tdac" }] }
```

**`role`** — mark the article that fills a canonical first-timer SPINE slot.
Assign these as you build the list; they drive BOTH the homepage Start Here path
and the spine links. Exactly these six keys, at most one article per role (first
in the list wins), at most one role per article:

| role     | assign to the article that is…              |
|----------|---------------------------------------------|
| `entry`  | the visa / entry-requirements / arrival-card guide (the audience-specific one) |
| `season` | the "best time to visit / when to go" guide |
| `route`  | the flagship itinerary (the 7-day; if none, the shortest full-country itinerary) |
| `anchor` | the gateway-city first-timer guide (the city every trip starts in — e.g. Bangkok, Istanbul) |
| `money`  | the money / costs / budget guide            |
| `safety` | the "is it safe" / health-and-safety guide  |

Assign every role you have an article for (aim for all six; the Start Here
section needs ≥3 to show). Anything outside these six keys is ignored — don't
invent roles; the closed vocabulary keeps every site consistent.

**`links`** — explicit outbound anchors for relationships the resolver can't
infer (exotic domain phrases like "Blue Cruise", or deliberate cross-topic
intent). Each `slug` must be a real slug in this list; each `phrase` must
actually occur in that article's prose (else it's skipped at injection — nothing
to wrap); cap 3 per article. Use sparingly — the resolver handles the obvious
topic links (an article → its own subject) automatically. Reserve `links` for
the handful it would miss.

## Rules

- **Every article maps to an existing category** in the approved structure (FK contract — no
  orphans). If an article doesn't fit, the structure is wrong; fix the structure first.
- **Slugs are stable and unique** — the content skill upserts by slug; a changed slug later
  orphans the article. Decide them now.
- **No duplicate intent** — don't plan two articles that answer the same question; merge them.
- **Monetization-aware ordering (optional)** — the content skill writes in 5-article batches;
  it can prioritise high-intent articles (itineraries, where-to-stay, transport passes) first,
  since those carry the affiliate links. The plan can note priority, but order is the content
  skill's call.
- **Output the list to the facts repo** so it persists (survives a long chat / a resume) and
  the content phase can read it: `travel-facts/<project>/article-list.json` — an array of
  `{ title, slug, category_slug, tier?, role?, links? }` (role/links optional — see the link
  plan above). The assistant PRODUCES this file; the USER pushes it
  (the assistant has no repo access). Categories also persist (in the DB seed); the article LIST
  persists here, since the `articles` table only holds *written* articles, not the plan. The
  content phase fetches it by raw URL alongside `facts.json`.

## Hand-off

The approved article list + the seeded categories are the two things the content skill needs.
Facts are NOT built here — the content skill builds the facts file FROM this list, so the facts
are scoped to what the site will actually contain (comprehensive, no generic filler).
