---
name: dossier
description: >
  Build a paid PDF decision-manual for one destination+audience project (e.g. "Rome,
  Solved." for romeforamericans) from that site's article corpus. It sells the
  CONNECTIONS the free corpus doesn't make: non-obvious, high-stakes synthesis
  scattered across dozens of free articles and joined in none (read
  references/model.md FIRST). Two deliverables: the BOOK (stable ~2yr analysis) + the
  FIELD SHEET (dated volatile figures, quarterly). Covers the model and
  synthesis-viability check, corpus mining, the decision framework and its quality
  bar, provenance marks, essays, vector maps from real coordinates, the cover, the
  image brief, the render, flow layout, and the gates — plus naming the guide (Stage
  A3: propose from the mined spine, user confirms, name + hooks backfill the site via
  the admin). Triggers: build the dossier / guide / paid PDF for [project], name the
  guide, write decisions, draw the maps, dossier image brief, render the dossier,
  dossier audit. Read state.json FIRST.
---

# Dossier — the paid PDF for one project

One project (destination + audience) → one sellable PDF, built **from that site's own
corpus**. Not a guidebook: a **decision manual**. The reader is anxious six weeks before
a trip, and the product resolves decisions with visible arithmetic.

> **READ `references/model.md` FIRST — before Stage 0.** It is the one idea the whole
> skill serves: you are selling the CONNECTIONS the free corpus doesn't make, not the
> facts. Every decision must be non-obvious to a diligent amateur AND high-stakes. The
> first cold build passed every structural gate and was forgettable because it skipped
> this. A clean book that no one would pay for is the failure this skill exists to prevent.

> Forged on Rome, Solved. — 57pp, 14k words, 21 figures, 13 decisions. Every rule here
> was paid for by a real bug in that build. Do not re-learn them.

```
STAGE 0  INPUTS    corpus export + project name + brand tokens (see references/0-inputs.md)
STAGE A  MINE      corpus → what can this support? + SYNTHESIS CHECK: are the key
                   facts scattered (sellable) or pre-connected (weak)? audit-synthesis.py
STAGE A2 SHAPE     the organising fact + the shape (city? country? region?) — Rome's
                   walk-time thesis does NOT transfer. references/a2-shape.md
STAGE A3 NAME      propose the guide's NAME from the mined spine → USER CONFIRMS →
                   the confirmed name is a DELIVERABLE (it backfills the site's
                   guide-spans through the admin batch update). See "The name is a
                   deliverable" below.
STAGE B  DECIDE    the decisions, the provenance marks, the two-document split
STAGE C  WRITE     essays + decisions + failure modes + Field Sheet. OBEY THE
                   PAGE SPECIMEN (references/page-spec.md — exact zones + CSS) and
                   FOLLOW
                   references/writing-code.md: marks are seasoning (1/paragraph,
                   never mid-sentence), and the page has a fixed anatomy.
STAGE D  DRAW      vector figures from REAL coordinates (never stock, never platform tiles)
STAGE E  IMAGE     MINE THE SITE'S OWN LIBRARY FIRST (content/batch-*/images — one
                   project had 168 usable frames sitting unused while its book
                   shipped with six). Contact-sheet them and LOOK; the filenames
                   are stock slugs. Only then emit a brief for what is missing.
                   Head bands are furniture and unnumbered; plate letters are
                   stamped after assembly, in reading order. references/e-image.md
STAGE F  RENDER    TWO DOCUMENTS: the Book and the Field Sheet.
                     python3 render-both.py <build-dir>
                   splits at RENDER time (never in the source) and paginates each.
                   references/fieldsheet-split.md.
                   Then the COMPOSITOR passes finish the pages — fit, feather,
                   tail-feed, snug, fill, widow. They are measured, never
                   hand-listed, and the ORDER matters: references/compositor.md.
                   READ references/build-traps.md FIRST — every render failure mode
                   below is already diagnosed there (CORS on the stylesheet, the
                   96-byte polyfill, borders cloned onto fragments, stranded openers).
                   ⚠ Any tool that navigates or re-sets the PDF must read the
                   document that was PAGINATED (_book.html), not dossier3.html.
STAGE G  AUDIT     ONE entry point, and it fails closed:
                     audit-release.py <build-dir> [--paper <hex>]
                   It runs all SIX gates (furniture · book · layout · ai-smell ·
                   claims · depth) and reports each. --paper is now sniffed from
                   the build's own stylesheet; the old default was one project's
                   cream and failed every sheet of a book printed on anything else. A gate whose inputs are missing
                   is BLOCKED, not a pass. g-audit.md used to say "Run ONE
                   command. Ship on green." and point at audit-book.py — which
                   invoked none of the other three.
                   ⚠ GREEN MEANS RELEASABLE, NOT RIGHT. These are production
                   checks on a well-formed artefact. No script reads whether a
                   comparison is sound; the editorial sign-off (b-decide.md's
                   comparison contract, the assembled trip, the working
                   reversals) is a separate human gate.
                   Quality bar (model.md) is taught, not gated. Design authority:
                   references/layout-architect.md; the mechanism: references/roles.md.
                   ⚠ No gate catches fragmentation artifacts — rasterise a few spreads
                   and LOOK at them before you ship.
```

**Read `references/` only for the stage you're in.** Each one is short and has the code.

---

## The non-negotiables

**1. The corpus is the STARTING source, not the authority.** Every claim traces to an
article the site published — no invented facts, no half-remembered prices, no "typically
around €X". But the corpus is **not** the authority for current prices, admission rules,
transport validity, opening hours, laws, safety or accessibility. Verify those against the
operator, venue or regulator, and record the check in `evidence.json`
([the evidence contract](references/evidence-contract.md)).

*Changed 2026-10-08.* This rule used to read "the corpus is the only source", and an
outside reader took the Barcelona book apart on exactly that: a free Park Güell route
through a ticketed zone, an airport-ticket rule that ignored the passes which do cover
it, a booking window the official calendar cannot honour. Every one of them was faithful
to the corpus. None was true.

**1b. A recommendation cannot outrun its evidence.** Where official sources contradict
each other, say so, narrow the claim, and give the reader a verification action — never
silently pick the convenient version. An estimate names its assumptions. A mark is
navigation, never a citation and never a confidence score: see
[quality standard](references/quality-standard.md).

**2. Every claim carries a provenance mark.**

| mark | means | lives |
|---|---|---|
| `● ESTABLISHED` | structural, true for years | the Book |
| `◇ OFFICIAL` | regulated fare, published rule, gov advisory | the Book |
| `▲ SURVEYED mm/yy` | our own dated observation | the Book, dated |
| `◆ VOLATILE` | price, hours, release window | **the Field Sheet only** |

**A mark is a classification, not a source address.** It says what KIND of claim
this is; it does not let the reader check it. `▲ SURVEYED` is currently attached
to work with no stated sample or method (Greece p41 marks "reading the corpus and
cross-checking it" as a survey; Rome p12's distances are "ours, measured on foot"
with nothing locating the measurements). And the taxonomy mixes two axes:
`◇ OFFICIAL` describes AUTHORITY while `◆ VOLATILE` describes SHELF-LIFE — an
official rule can also be volatile, and Turkey p16's official inflation figure
plainly is. The three books also disagree about which shape means what.

So, in addition to the mark:

- Every consequential claim carries a **claim ID** linked to the article passage
  it came from and, where one exists, the underlying source.
- **Source type and recheck status are separate fields.** A claim can be
  `OFFICIAL` *and* due for recheck.
- **`▲ SURVEYED` requires a described observation method.** Reading the corpus is
  not a survey. If there is no method, it is synthesis.
- **Generate the legend and the glyphs from one definition** so three books
  cannot drift apart on what `◆` means.
- Synthesis stays unmarked, but **names its assumptions**.

**The old lint rule said "no mark = opinion = cut."** That misdescribes what is
being sold: the reasoning IS informed judgement, and cutting everything unmarked
would cut the product. The rule is now: *no traceable support = no consequential
claim.* Judgement is welcome; unsupported certainty is not.

**3. The two-document split by shelf-life.** The Book ages slowly and never carries a live
price. The Field Sheet is dated, quarterly, emailed. When they disagree, the Sheet wins.
**Never promise a page count you don't ship** — describe the Sheet by what it *carries*.

**4. What the dossier refuses to do**, and says so on its own back-matter page: name hotels
(we haven't slept in them), name restaurants (wrong by spring — the *rule* outlives the list),
print current prices (they belong on the Sheet), republish anyone's ratings (legally and
editorially radioactive). That page IS the brand. Never let a reviewer talk you out of it.

**5. Photographs are the user's to choose — and every one is LANDSCAPE.** Never generate
them, never pull from an API, never ship a placeholder in a paid product. A 2:3 phone shot
needs 7in of height to fill the column and renders as a stamp; `validate-images.py` gates
this before the build, and the build itself refuses portraits. Aim for **one plate per six
pages, spread across both halves** — `audit-rhythm.py` fails a text-only run over 6 pages. After the text and figures are done, emit the
image brief **in the chat**, alphanumerically (A01, A02…), and stop. The user downloads in
that order and hands the files back. See `references/e-image.md`.

**6. Legal.** No platform API data (Booking/TripAdvisor/Google all prohibit resale in a PDF).
No per-hotel scores. No logos. No negative claims about named businesses. Own artwork only.
Coordinates and geography are public facts — drawing your own map from them is fine.

---

## The name is a deliverable (Stage A3)

The site's articles are written BEFORE this build exists. They hand off to the guide
through **guide-spans** — `<span class="guide" data-guide="name">neutral gloss</span>` —
whose inner text is a placeholder gloss ("the complete Greece trip guide") until this
build names the real product. Naming therefore belongs HERE, after the cold-mine, so the
name reflects the corpus's actual spine and not a planning-stage guess (the Rome and
Greece rebuilds both overturned the assumed spine — a name minted before the mine would
have baked the wrong thesis in).

The step, right after Stage A2:

1. From the mined spine and organising fact, **propose 2–3 names** following the shipped
   pattern — *destination + promise of resolution* ("Rome, Solved." / "Greece, in
   Order."), never a single swamp's ranking baked into a title.
2. **The user confirms one.** The name is not final until confirmed.
3. Emit the confirmed name as a **deliverable of the build** (alongside the PDF): the
   admin's **Guide panel → "Name backfill"** (`POST /api/guide-name-backfill`) writes it
   into every `span.guide` inner text across the site's corpus in one pass — a cheerio DOM
   operation, dry-run by default, article status untouched, idempotent. The dossier build
   does not perform the backfill — the admin does; this build just supplies the confirmed
   string.
4. **With the name, emit the THESIS line and the per-swamp HOOK lines** (one sentence
   per swamp, written from the shipped decisions — this build knows the real spine, so
   it writes the doors into it). These are RAW hooks — accurate first, punchy second.
   The `marketing` skill (its references/hooks.md three-part test: name the wrong
   move → concrete-image stake → open loop) strengthens them before they ship to the
   site's guide config; don't polish here, don't ship flat ones there. The user confirms the set. These three fill
   `SITE_CONFIG.guide` (name / thesis / hooks) for the site's Stage 5c conversion
   surfaces (travel-empire `references/5c-conversion.md`). Hooks are keyed by the
   swamp ids from the site's `article-list.json`; a swamp the mine demoted simply
   gets no hook (the surfaces fall back to the thesis — fail-open, never broken).

Two corpus-reading rules that come with this: when MINING (Stage A), **strip every
`span.guide` element AND the sentence containing it before the cue tally** — that is the
machine-detectable rule; "handoff prose" in general is not detectable and must not be
guessed at. The rest of a turn section is normal corpus prose and tallies normally. These
spans are the site pointing at this product, not destination signal, and counting them
inflates whatever swamps the article
list guessed. And the site's `article-list.json` `swamps` array is a **hypothesis to
reconcile, not an input to obey**: the cold-mine wins, as it did on Rome and Greece. Where
the mine demotes or surfaces swamps relative to that list, say so in the chat — it's a
small retrofit worklist for the site's articles (a seed to add, a turn to soften), handled
by the travel-empire skill, not by this build.

---

## Quick reference — what goes where

| you're doing | read |
|---|---|
| **starting fresh — what do I need?** | **`references/0-inputs.md`** |
| corpus check, is this destination viable | `references/a-mine.md` |
| **what shape is this destination — city? country?** | **`references/a2-shape.md`** |
| choosing the decisions, writing them | `references/b-decide.md` |
| essays, failure modes, the Field Sheet | `references/c-write.md` |
| maps, illustrations, the cover device | `references/d-draw.md` |
| the image brief + wiring photos in | `references/e-image.md` |
| emit the brief | `scripts/emit-image-brief.py <slots.json>` |
| **validate the photos the user sent** | **`scripts/validate-images.py img/ [--fix]`** |
| **check the book's visual rhythm** | **`scripts/audit-rhythm.py dossier3.html`** |
| **check the pages hold a shape** | **`scripts/audit-page-shape.py dossier3.html`** |
| **design the cover (D.5)** | **`references/cover.md` — argue the thesis, don't template** |
| **lay out the pages (F.5)** | **`references/layout.md` — FLOW chapters, don't hand-place** |
| **THE final gate — clean or clumsy?** | **`scripts/audit-book.py <build-dir>` — runs everything (incl. depth), one verdict** |
| **is the book deep enough?** | **`scripts/audit-depth.py <build-dir>` — yield model, enforced** |
| **THE MODEL — why anyone buys it** | **`references/model.md` — READ FIRST; pay for the connections** |
| **THE LAYOUT ARCHITECT — the design authority** | **`references/layout-architect.md` — the page as a designer sees it: sheet contract, baseline & scale, composition judgment, feathering. Read before Stage C and Stage F.** |
| **THE ROLES — the layout intelligence layer** | **`references/roles.md` — every block gets a ROLE with a fixed visual weight (opener · ledger · verdict · forks · figure · reasoning · reference). Without it a book passes every gate and still reads as a wall of text. Read before Stage C and Stage F.** |
| **THE RENDER TRAPS — already paid for** | **`references/build-traps.md` — CORS on the stylesheet, the 96-byte polyfill, borders cloned onto fragments, stranded openers, feathering that silently does nothing. Read at Stage F BEFORE debugging.** |
| **THE PAGE SPECIMEN — exact geometry** | **`references/page-spec.md` + assets/page-specimen.png — head/body/foot zones in px, the paged page model** |
| **every sheet furnished & painted?** | **`scripts/audit-furniture.py <pdf>` — the gate that catches the continuation-page bug** |
| **HOW prose sits on the page** | **`references/writing-code.md` — mark density, page anatomy, header hierarchy** |
| **do furniture & body collide?** | **`scripts/audit-geometry.py <pdf>` — dead-zone check (in audit-book)** |
| **prose not over-marked?** | **`scripts/audit-marks.py <pdf>` — confetti check (folded into audit-book)** |
| **is there synthesis to sell? (Stage A)** | **`scripts/audit-synthesis.py corpus.json "theme" ...` — scattered vs pre-joined** |
| **THE COMPOSITOR — the passes that finish a page** | **`references/compositor.md` — fit · feather · tail-feed · snug · fill · widow, in that order. Furniture before argument; 85% floor. What Chromium and Paged.js actually do.** |
| **TWO DOCUMENTS — the Field Sheet is its own PDF** | **`references/fieldsheet-split.md` + `scripts/render-both.py`** |
| **split the sheet out / inspect the split** | **`scripts/fssplit.py <build-dir>`** |
| **the sixth gate — does the book contradict itself?** | **`scripts/audit-claims.py <build-dir>` — mark key, declared counts, figure labels, ornaments, contents vs outline** |
| **bookmarks + clickable links** | **`scripts/add-nav.py <build-dir> [--pdf F] [--html F]`** |
| **the phone edition** | **`scripts/render-phone.py <build-dir>` — 4.5×8in, narrower measure** |
| **the manuscript the ai-smell gate reads** | **`scripts/emit-manuscript.py <build-dir>`** |
| **too many em-dashes** | **`scripts/dash-pass.py <build-dir> [--apply]` — converts by JOB, not position** |
| build + render + the gates | `references/f-render.md` |
| the refinement loops before ship | `references/g-audit.md` |
| the design system (structure, scale) | `assets/design-system.md` |
| where a project's colours come from | `references/brand-tokens.md` |

---

## The build, in one screen

```
build/
  content.py     decisions (the analytical heart)
  content2.py    terrain, neighborhoods, days, failure modes
  content3.py    the destination's set pieces, day trips, eating, money
  content4.py    pre-departure, PHOTOS dict
  content5.py    first day, rhythm, churches, wallet, calendar
  prose.py       OPENING + the essays (drop caps, standfirsts, pull quotes)
  design2.py     THE CSS LIVES HERE — not in build3.py (see the bug log)
  maps.py        every vector figure, drawn from real lat/lon
  illus.py       drawn illustrations (scope its palette — see bug log)
  covers.py      the cover device
  build3.py      execs the above → dossier3.html
  img/           user-supplied photos, resized
```

Render: `python3 render-paged.py` (copy from `scripts/`, with `assets/paged.polyfill.js`)
— Paged.js paginates the flow into real page divs, the feathering pass finishes the
chapter tails, then Playwright prints. Fonts and photos by FILE URL, never base64.

---

## The release contract (merged 2026-10-08)

`scripts/audit-release.py` is the one entry point. It now runs **three families** and
fails closed on all of them:

```bash
python3 SKILL_DIR/scripts/audit-release.py BUILD_DIR --prepare-review
# look at the actual pages, then complete review.json
python3 SKILL_DIR/scripts/audit-release.py BUILD_DIR
```

| family | what it can see | what it cannot |
|---|---|---|
| evidence + bindings (`audit-evidence`, `compile-guide`) | a claim with no source, a stale binding, a rule repeated out of sync | whether the source is right |
| content integrity (`audit-content`) | text lost between final HTML and final PDF | a defect identical in both |
| the six legacy gates + `audit-source-defects` | furniture, depth, marks, self-consistency; truncated cells, repeated headers, a word split across a page turn | any claim about the world |

**Why all three.** The legacy orchestrator was nearly dropped in this merge. Its own
header documents what happens then — "two competing release contracts, and the shorter
one won because it was the one written down as a command". A `legacy_gates()` call keeps
them in the contract, and a missing legacy script is BLOCKED, never a quiet pass.

**`audit-source-defects.py` exists because content integrity structurally cannot help.**
It compares final HTML against final PDF; the two truncated cells shipped in Barcelona
were identical in both. Source damage has to be caught in the source.

### What this merge deliberately did NOT take

- **The Node renderer is not the default.** `render-guide.mjs` is installed and optional.
  `render-paged.py` carries seven books and a dozen diagnosed Paged.js traps, and Node
  Playwright is not installed on this machine while the Python one is.
- **`references/` was kept.** The rewrite compressed nearly every file — e-image −281
  lines, layout-architect −234, compositor −140, build-traps −64 — and what it dropped
  was operational: the polyfill-at-root hang, `document.fonts.ready` resolving before
  `<body>`, the asset library with Barcelona's 276 unused photographs, the U+2011
  page-turn detector. Doctrine improved; scar tissue did not.
- **`agents/openai.yaml` was not installed.** It is an OpenAI product manifest
  (`products: chatgpt, codex, api, atlas`), not a skill artifact.

### Dependencies the new gates need

`audit-content.py` wants **Node** Playwright (its fallback wants `lxml`); neither is
installed here, and it BLOCKS rather than passing. `audit-evidence` and the compiler need
`evidence.json` + `release.json`, which no existing book has — building those for the
seven is real work, not a flag.

---

## THE BUG LOG — every one of these actually happened

### 2026-10-01 — the seven-book pass: two documents, the compositor, and gates that measured nothing

**A gate keyed to a class name checks NOTHING on a book that uses other names, and says
PASS.** One project wrote its chapters as bare `<section id="x">`; every fleet tool keys
off `section.dec`. `emit-manuscript.py` produced a **0-word manuscript**, two gates
measured nothing, and the renderer's feather pass had nothing to measure — which is why
that book paginated flat with no compositor ever firing. Teaching the book the fleet's
nouns once beat forking five tools. *Read a gate's header count before trusting its
verdict.*

**Five more gate blind spots, each right about one book and wrong about the next:**
- `audit-furniture`'s default paper was one project's cream — every sheet of a book on
  any other stock failed as "unpainted". `audit-release.py` now sniffs `--paper` from the
  build's stylesheet.
- `audit-claims` matched mark glyphs as literal characters; a book writing `&#9679;`
  reported "cannot check" — which reads like a pass.
- `audit-layout`'s opener aliases missed `kicker`/`standfirst`, so seven decisions read
  as openerless. Its stranded-opener check was a **text search** that flagged
  continuation pages carrying 400 words because another chapter *mentioned* them; it now
  resolves from the PDF's named destinations. Two follow-ons: **page 1 is the cover**,
  and a title chapter nothing links to has **no destination at all** — so the guard needs
  to sit on both branches.
- `audit-ai-smell` flagged "landscape" literally; in a travel book that is a mountain.
  Only the figurative pattern counts.
- `audit-book`'s rhythm check read `FIG./PL.` caption TEXT. Head bands are deliberately
  unnumbered, so a book with a photograph on 93 % of its pages reported a 7-page
  text-only desert. Ask the page whether it draws an image XObject.

**`add-nav` wrote ZERO bookmarks and reported success** on a contents written as a
`<nav>` of bare `<a>` — the row matcher wanted `<tr>` or `<li>`. Four row idioms exist.

**THE CLASS OF BUG: tools reading the source instead of the print.** Once the Field Sheet
became its own document, `add-nav` and `render-phone` were still reading `dossier3.html`
— so the outline looked for a chapter the file no longer had, and the phone edition kept
one the print book had lost. Both silent. See references/fieldsheet-split.md.

**The compositor levers are now written down** (references/compositor.md), including the
ones that cost whole renders: `break-after:avoid` works and `break-before:avoid` is
dropped; `break-after:avoid` on a head band pushes the whole opener off; nested
`break-inside:avoid` moves a block that fits; `break-inside:avoid` on a **table** is
all-or-nothing and conservative; Paged.js keeps a section's `id` only on its **first
fragment** (this one defeated four separate passes, each of which ran, found nothing and
reported success); an automatic hyphen **is** a DOM character (U+2011) but only after the
split; Chromium has no `hyphenate-limit-last`.

**Express a ratio as WIDTH, not height** — it scales the height identically and needs no
measurement, which is the trap above avoided entirely.

**Furniture must be invisible to the movable-block passes, in BOTH lists.** A new band
class added to only the block scan was still collected by the shrink rewriter, which set
`width:auto` **inline** — beating the stylesheet — and a full-column band rendered as a
narrow portrait stamp.

**A head image must MEAN something.** A chapter captioned *"a kilometre and a half, end
to end… it is walkable"* carried a plate of carbonara and passed every gate. Gates count
images; they cannot see subject.

**The site's own image library is usually already there.** One book shipped with 6 plates
across 35 pages (17 % of pages, against a fleet band of 45–74 %) while
`content/batch-*/images/` held 168 usable landscape frames. Contact-sheet and LOOK — the
filenames are stock slugs.

**My own prose fix broke a book.** Rewording "at the back" 20 characters longer pushed a
reading key onto a sheet of its own; the `book` gate caught it. Keep a replacement no
longer than the original.

### 2026-09-18 — the external review pass (three shipped books, read against the skill)

Greece, Rome and Turkey were reviewed together by an outside model, and the
checkable claims were then verified independently. Three books from one skill is
a natural experiment: **a fault in all three is the skill's fault.**

| # | what shipped | why it got through |
|---|---|---|
| R1 | `audit-book.py` invoked none of the other three gates, while `g-audit.md` said "Run ONE command. Ship on green." | two release contracts; the shorter one was the one written as a command |
| R2 | The rhythm check reported a **43-page text-only run on a 43-page book full of figures** — Greece letterspaces its labels, extraction yields `F I G .`, and `\bFIG\.\s` matched nothing | a broken detector and a true failure look identical from the outside |
| R3 | The cover check called Rome's own `#F6EEDB` paper "ink" (`b>220`) and scored its cover **97.1% non-paper** — blank stock would have passed | a per-brand value was hardcoded as a constant |
| R4 | R2 and R3 **masked each other in opposite directions**: Greece failed for a reason that did not exist, Rome passed for a reason that was not true | nobody re-read a gate that agreed with them |
| R5 | Rome p12 printed **three headers over two-cell rows** — "WALK TO CORE" above character descriptions, walk minutes under "PRICE", and no price anywhere on the page | `cols` was a free STRING with no tie to row arity |
| R6 | "Ostia beats Pompeii by **eleven hours**" — a whole excursion minus a travel leg | no rule required both sides of a comparison to share boundaries |
| R7 | `design-system.md` specified **7.5px captions** in the same file that corrects reviewers with "8px is the floor for print" | the doctrine contradicted itself on one page |
| R8 | Greece p35's figure printed `THE NIGHT THAT SAVES THE FLIGH` | rule 1 said "no label outside the canvas"; a character-count estimate cannot certify containment |
| R9 | All three books ship with **zero PDF bookmarks**, and Greece's contents page prints **zeros for every folio** | `f-render.md` already required checking folios; nothing ran it |
| R10 | Rome's "wallet card" is **6.79in wide** — a pocket is 3.25in, which would put its type at ~3.8pt | "print it, carry it" was a promise with no physical specification |

**The pattern:** ten of these are the same shape — *something was declared, and
nothing checked that it was true.* A header string that never met its cells, a
gate that never ran, a floor contradicted in its own file, a promise with no
spec. That is what the audit now has to catch, and what a human still has to read
for.

Read this before touching the build. Each cost real time on Rome.

**1. The CSS lives in `design2.py`.** Edits to `build3.py`'s style block do nothing. Symptom:
"my fix didn't apply." Half the Rome cover bugs were this.

**2. `python3 build3.py` printing "pages: 57" does NOT mean it wrote the file.** A rename left
it writing to `guide3.html` while renders read `dossier3.html` — two hours of "verified" work
went to a file nobody rendered. **Always check the output file's mtime after a build.**

**3. Never `2>/dev/null` the build.** It hides `NameError` and you render stale HTML.

**4. String-replace edits fail silently.** `s.replace(old,new)` with a non-matching `old`
returns the string unchanged and reports success. **Always `assert old in s`** before replacing,
or patch by line index.

**5. A rule you "tuned" may not exist.** `.map.band svg{height:...}` was edited three times
across two sessions; it was never in the stylesheet. Map SVGs sized purely by viewBox aspect.
**`grep` for the selector before tuning it.**

**6. `.map figcaption` fell back to browser default 16px** — *larger than 13.4px body text* —
because a FIG-numbering edit replaced the combined `.map figcaption,.photo figcaption` rule
with `.photo` alone. Symptom: captions look wrong on some pages, fine on others.

**7. `.map` had no margin rule at all**, so map captions welded to the paragraph below them
(0px) while photo captions got 22px. Same symptom: "some pages are OK, some aren't."

**8. Figure too small = the artwork's viewBox, not the CSS.** Rome's day-trip maps were
660×120 and rendered 119px against a reference figure's 293px. Fix the viewBox.

**9. Rebuilding a function by index slice deletes its neighbours.** Rebuilding `MAP_HOOD`
silently removed four `GFX_*` functions and `DAYTRIP_GEO`. **After any slice-rebuild, assert
every public function still loads.**

**10. `illus.py` redefining `C={...}` clobbers `maps.py`'s palette** → `KeyError: 'water'`.
Extend, don't replace.

**11. A collision detector that flags a label beside its own dot reports 36 phantom hits.**
Real collision = the dot's centre falls *inside* the glyph box. Write the strict version first.

**12. A blanket fix breaks what was already right.** "All inside-ring labels point inward"
flipped four correct labels to fix one. **Target the actual condition**, not the category.

**13. External design values don't transfer.** A reviewer's 23px pull quote (designed against
a one-sentence sample) rendered 209px tall against a 90-word verdict and blew the page. Their
A4 canvas and 0.38in margins were wrong for US Letter. **Measure their render, take the ideas,
re-derive the numbers against real content.**

**14. A CSS box that doesn't match the image's aspect silently eats the photograph.**
A 3:1 box with `object-fit:cover` showed 50% of every landscape and **22% of every
portrait** — 78% thrown away, invisibly. The box must follow the image, never the reverse.
`validate-images.py` gates the shape before the build.

**15. `display:flex` on a `<figure>` makes the caption a row sibling of the image.**
Rome v2 shipped captions stranded to the *right* of the picture in dead space. The
`figcaption` CSS was correct the whole time; flex overrode where it landed.

**16. `:has()` does not land in this headless Chromium.** Two separate attempts to style
a page by its contents silently did nothing. Set the class in the generator instead.

**17. Slot IDs and plate letters diverge, silently.** The brief says `A07`; the book prints
`PL. E`, because plates are lettered in page order. Three rounds were lost swapping the wrong
photographs. Letter plates by slot (`chr(64+int(slot[1:]))`), and make the user name their
files `A07.jpg` — not `E.jpg`.

**18. An upload can arrive as a 2-byte file.** GitHub happily served `A08.png` as a bare
`\r\n`. Check the byte count before `Image.open()` and say so plainly — don't diagnose it as
a format problem.

**19. "Stale" means half-empty pages — and it took two wrong diagnoses to find that.**
Greece read as basic. First guess: thin pages. Wrong — its prose is *denser* than Rome's
(1.2% vs 0.9% ink). Second guess: pages packed to the trim edge. Also wrong, and wrong
because **the instrument was broken**: scanning a rendered PDF for its lowest ink finds the
FOLIO and reports ~96% for every book. The truth, measured on the DOM with furniture
excluded: **Greece median fill 60%, 25/41 pages under 65%, range 18-92%. Rome: 71%, 5/49,
range 57-90.** Greece's pages are two-thirds empty and no two are the same shape. Measure
the DOM, not the render.

**20. A plate at the top of a page outranks the figure that carries the argument.** Greece
opened p6 on a photograph and buried its route graph beneath — the reader meets the
decoration before the argument. The *arguing* figure leads; a photo is not automatically it.

**21. A decision is an argument, not a page.** Giving each decision its own two `page()`
calls made every one 55-60% full — six blank pages, and it read as a thin book. FLOW the
chapter (one `.flow` div, break rules, visuals inside the prose) and the engine fills the
pages: Greece 41pp→34pp, median fill 60%→84%, same words. The page count was layout, never
corpus. See references/layout.md.

**22. A figure belongs UNDER the prose that introduces it, not on its own page.** Greece's
route graph sat alone above an unrelated photo while the essay that argued it was 59% full
one page back. Emit the visual inside the flow after its paragraph; it drops onto the same
page when it fits and pushes over only when it must. Never a `page(fig(...))` by itself.

**23. The cover is the highest-leverage page and the first one skimped.** Greece shipped a
1.4%-ink title-on-paper. A cover must ARGUE the thesis (references/cover.md), be computed
from real coordinates so it's unclonable, and get its own render pass — the standalone SVG
hid hard-teal streamlines, a serif-fallback font, and a missing full-bleed. Budget two
rounds, not zero.

**24. Don't hand-maintain a SPLIT set.** Tuning which decisions break where is a loop that
never converges — every fix moves the overflow. Flow the chapter, set the fragmentation
rules once, render, measure. If you're keeping a list of page breaks, you've reverted to
fixed pages.

**25. A clean book can still be a thin book — and the org gate can't tell.** A cold rebuild
of Greece passed audit-book.py green at 19pp: well-filled, paced, good cover. It had used 9%
of an 80-article corpus that supports ~40pp. Organization checks are blind to thinness. The
depth gate (audit-depth.py, now in audit-book.py) catches it: pp/article, words/article, and
% of corpus used, calibrated so the thin build fails and the two good builds pass. Discovered
by the first true cold build — the exact failure a cold test exists to surface.

**26. Always ship corpus.json in the build tarball.** The depth gate needs it; without it,
audit-book.py silently skips depth and a thin book passes. The cold build happened to include
it, which is the only reason we caught this.

**27. Every chapter starts a fresh page; never let a chapter tail orphan into the next.**
Flowed chapters need `break-before:page` on `.chap` (Rome shipped tables splitting mid-row
across pages because only `.page` had the break, not `.chap`). See layout.md.

**28. A figure must render exactly once — guard the emit.** Rome drew FIG.3/5/9/10 twice
because a figure was claimed by both a chapter `fig` key and a decision/plate/renderer. Track
emitted keys, skip repeats, and number by appearance order (a static map + chapter-order
placement gives out-of-sequence captions). layout.md has the guard.

**29. Chapter-break slack is where plates go.** Breaking each chapter to a fresh page leaves
half-empty tails; fill the emptiest ones with a plate rather than stacking images elsewhere,
and pull a figure back onto the previous page when it would otherwise open a new one.

**30. White furniture bands: Chromium CLIPS template backgrounds** (full-bleed div,
oversized paint, background attr — all clipped) and bare `@page` margins are unpainted.
Watch for a hidden `@page{margin:1.02in}` in the CSS — that was Rome's real white band.
The per-chapter in-body runhead this entry once recommended is ITSELF bug #33 — the whole
mechanism class is superseded by the paged page model (page-spec.md).

**31. A chapter ending >70% empty wants another plate.** The corpus supports one more figure
or photo; two-thirds of a blank page is the signal to add it. layout.md — but fix the double
margin first, since most "empty" space is really wasted margin.

**32. Verify by extracting, not by looking.** Pulling the PDF's text is what caught
"COLOSSEUM" clipped to "COL" and two labels rendering outside the canvas entirely.

**33. Per-chapter furniture margins chapter-START pages only.** The in-body runhead fix
(old #30) gave a correct 92px top + furniture on the first page of each chapter, and
continuation pages started 2-3px from the trim, unfurnished, edge to edge. Chromium also
does not repeat `position:fixed` across printed pages. Margins and furniture must be a
property of the PAGE — the paged page model (Paged.js slices the flow into real page divs;
page-spec.md) is the only mechanism in this Chromium that furnishes and paints every page.
`audit-furniture.py` exists to catch this class: it fails the old architecture on nearly
every page and must pass on every build.

**34. Base64 megabytes silently truncate the paginated book.** With data-URI fonts the
CSS parse stalls for minutes; with data-URI photos the paginator's measure loop STOPS THE
BOOK EARLY with no error — Rome came out 37 of 48 pages, at a different point each run.
Fonts and photos are referenced by file URL, and the renderer pre-decodes images before
pagination. A short book after a render = check this first.

**35. Two selectors setting one named string shadow each other.** `string-set: rh` on
both `.dnum` and `.rh-src` made continuation runheads show a STALE chapter (the paginator
keys captured strings per selector). One selector per string — every section emits one
invisible `.rh-src` span after its H1.

**36. Feathering replaced hand-placed tail fixes.** Chapter tails are finished by the
renderer's measured TIGHT/FEED/LOOSE pass (layout-architect.md §4), bounded at ±1 notch,
recomputed every build. Escalate a tighten that fails to clear its tail (a 2-line orphan
is worse than the 6-line one you started with), and never keep a hand list of which pages
get what — that is the split-set antipattern (#24) in new clothes.

**37. The audit instrument must match the architecture.** The stub gate's 40%-of-sheet
line was calibrated on the double-margin flow; under real 92/72px pages the same sheet
fraction holds far more column, and an endmark-closed verdict apparatus at 38% is a set
tail, not dribble. Recalibrated to a third of the sheet — the same instrument correction
as #19: when the layout model changes, re-derive what the gates measure before trusting
either a pass or a fail.

**38. A chapter's figure/length budget is an authoring decision, not a render-time
discovery.** Every chapter breaks to a fresh page (#27), which means its total height IS
its page cost, decided the moment the prose and figures for it are chosen — feathering
(§4) corrects a notch of error, it does not rescue a chapter nobody sized. Japan's
"Decide these first" annex shipped a table split across a page turn, the page before it
a third empty, because no one asked while writing it whether the table's own shape would
survive its own page. Hold a one-line brief per chapter BEFORE Stage C commits it: words
→ pages at this book's measured rate, figure count + size class, and the closing-image
question answered explicitly (yes with a named plate, or no on purpose). See
layout-architect.md §0.

**39. `break-inside:avoid` on a `<table>` is not reliable in this render, regardless of
free space.** Paged.js paginates through a CSS-multicol scratch layout, and Chromium's
own fragmentation of `<table>` elements inside `break-inside:avoid` + multicol is a
separate, documented limitation: a table can be pushed to the next page even when the
current one visibly has room, and no shrinking or padding change reaches it (confirmed
by instrumenting the polyfill's own overflow test — every failing decision fired on a
width comparison, never a height one). The fix is markup, not CSS: a `<div>` grid
(`display:grid`, same columns, `break-inside:avoid` per row) does not carry the bug.
Decide this at Stage C, for any instrument whose rows must stay together — not after it
ships broken. See layout-architect.md §0.

**40. Judge an image candidate in the band it prints as, not as a full frame.** The two
judgments can disagree — a photo that reads as the obvious pick uncropped can turn out to
repeat the table under it once seen in the real crop, while an unremarkable full-frame
photo can be the one that answers what the text doesn't. Build the first-pass contact
sheet pre-cropped to the slot's aspect, offering multiple crops of a tall/wide source as
separate candidates, not thumbnails of the untouched photo. e-image.md.
