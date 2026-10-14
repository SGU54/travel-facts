# Stage 3b — Feeding the vein, and writing for citation

Two doctrines that live together because they pull in opposite directions and the
resolution is a single rule. Read this WITH `3-writing.md` before drafting any batch on a
site that has a measured vein (or intends to build a dossier at all).

- **Feeding** — does this article carry material the paid guide will later CONNECT?
  (`3-writing.md` wires the *conversion* — swamp + handoff. It does not wire the *supply*.)
- **Citability** — can an AI answer engine lift a self-contained, attributable chunk out of
  this article?

**The rule that reconciles them:**

> **Make the FACTS citable. Never the THESIS.**

A perfectly citable chunk gives one fact with its date and its source. A chunk that joins
the closed currency AND the commission AND the haggling anchor is the guide's product,
given away in a form built for copying. Both failures are silent: the first costs traffic,
the second costs the thing the site is monetised on.

---

## 1. The vein — plan the corpus from what was MEASURED, not from the taxonomy

`architecture/article-plan.md` derives the list from the destination's shape (country → per
city; city → per neighbourhood; + the Plan-your-trip set). That heuristic produces the
articles a traveller searches, and it stays. But it is blind to the only question the paid
guide depends on: **does this corpus have something to connect?**

The instrument already exists — `dossier/scripts/audit-synthesis.py` — and it is normally
run far too late, at the dossier's Stage A, after 80 articles are written. Japan is the
case: 84 articles, then the discovery that the one strong vein was already pre-joined
inside a single article. Barcelona is the counter-case: the money-trap web scored HEADROOM
15.3 with **zero** articles joining it — a whole book's spine, sitting there unbuilt.

**Run the audit EARLY — as soon as ~20 articles exist — and re-run it at 40.** At 20 the
number is a signal, not a verdict; the RANKING of candidate theses is what's reliable, and
the ranking is what decides the next forty articles.

How to run it (name the real parts; auto-detection lies):

```bash
python3 ~/.claude/skills/dossier/scripts/audit-synthesis.py corpus.json \
  "theme1 regex" "theme2 regex" "theme3 regex" "theme4 regex"
```

Reading the result:

| HEADROOM | Meaning | Action |
|---|---|---|
| < 2 | the corpus already pre-joins it | **dead thesis** — do not plan articles into it |
| 2–4 | thin but real | usable if nothing better scores |
| > 4 | scattered, rarely joined | **the vein** — plan depth articles into it |

**Compare theses at an EQUAL number of themes.** Adding a fifth theme mechanically inflates
HEADROOM (it becomes less likely any single article holds them all). A 5-theme score is not
comparable to a 4-theme score, and quoting one as an improvement is self-deception.

**A too-generic theme lies WEAK.** "Distances / hours / train / itinerary" scored 1.5 on
Morocco not because the vein was mined out but because those words appear everywhere. If a
thesis scores WEAK, first ask whether the regexes name the destination's SPECIFIC parts
before concluding the vein is dead.

### The vein contract (article-list.json, schema_version 5)

The measured result is DATA, not chat memory — it must survive into the batches that
consume it. Top-level block, written when the audit is first run, amended when re-run:

```jsonc
{
  "schema_version": 5,
  "vein": {
    "thesis": "In <destination>, no price is a price — and you arrive unable to prepare.",
    "measured": { "headroom": 5.9, "corpus_at_audit": 20, "date": "2026-08-09" },
    "max_pieces_per_article": 2,
    "pieces": [
      { "id": "closed-currency", "name": "the currency you can't buy in advance",
        "match": "closed currency|before you arrive|can't get it|export limit" },
      { "id": "commission",      "name": "who pays the guide",
        "match": "commission|faux guide|unofficial guide|showroom" },
      { "id": "anchor-price",    "name": "the opening price",
        "match": "haggl|bargain|opening price|markup" },
      { "id": "cash-cost",       "name": "what cash actually costs",
        "match": "atm|withdraw|dcc|cash machine|tipping|gratuity" }
    ]
  },
  "articles": [
    { "title": "…", "slug": "…", "category_slug": "…",
      "swamp": "money", "handoff": "turn",     // conversion layer (3-writing.md)
      "piece": "commission" }                  // supply layer (THIS file) — or "none"
  ]
}
```

`swamp` and `piece` are different axes and both are needed. `swamp` decides which DOOR to
the guide the page shows; `piece` decides which BRICK of the guide the page supplies. An
article can be dry ground (`swamp: "none"`) and still carry a piece; the reverse is common
too. Absent `vein` block = v4 behaviour, unchanged — never retrofit a live site's list
uninvited.

### The planning rule

**Each depth article carries ONE piece, fully. No article carries three.** The corpus is a
set of well-lit rooms; the guide is the floor plan. Plan the next batches so every piece
gets its own dedicated article (that's where the guide's word count comes from), and so no
article ends up standing in three rooms at once.

Two supporting numbers, both learned the hard way:

- **~1 000 words per article is the floor for a viable dossier.** At 1 072 (Barcelona,
  Morocco) the extraction yields ~0.5 dossier page per article and the depth gate passes.
  At 654 (Japan) it does not — and *adding thin articles moves the dossier further away*,
  because the gate is per-article (≥0.40 pp, ≥120 words each). Volume never fixes thinness.
- **New articles are born with their fact-spans.** Retrofitting spans onto a written corpus
  means touching the same articles twice; that, not the writing, is the real waste.

---

## 2. The pre-join guard — the failure that costs the product

An article that joins three or more pieces of the vein **destroys the thing the guide
sells**, and it does so invisibly: the article is excellent, the reader is grateful, and
the HEADROOM the dossier depends on has just dropped.

This is the same failure `check-noconnect` catches at the sentence level (making the call
the book is supposed to make); the pre-join guard catches it at the article level (laying
out the map the book is supposed to draw).

**The gate measures JOINS, not mentions — and the distinction is the whole instrument.**
Counting pieces per ARTICLE over-fires: on Morocco's 20 published articles it flagged 4
pre-joins, and reading the passages showed **zero** real ones — the pieces were mentioned
in different sections, doing different jobs, never joined. (Keyword co-presence lying about
structure is now a ten-time-recorded pattern in this project; always read the sentences
before believing the count.) So:

- **mention** (piece regex fires anywhere in the article) → WARN above
  `max_pieces_per_article`. A signal to go look, nothing more.
- **join** (≥ `max + 1` pieces inside a **2-consecutive-sentence window**) → FAIL. That
  window is where a joining passage actually lives, and it is what the guide sells.

Both are mechanically checked by `validate-batch.mjs` against the `match` regexes, so
neither can rot into an intention.

**Fixing a pre-join is not deletion.** The article keeps every fact it needs to answer its
own question honestly (hard rule: nothing the reader came for is withheld — that stays
absolute). What comes out is the **joining sentence** — the "and because X, Y also means
Z" that does the guide's work. Cut the connective tissue, keep the flesh; then, if the
article is a `turn`, the handoff points at where those connections are worked out. The
article says *what*; the guide says *therefore*.

---

## 3. Citable chunks — answer-first, dated, attributable

What actually moves AI citation, verified rather than assumed (Aug 2026):

- **Being INDEXED beats being ranked.** ~87 % of ChatGPT citations correspond to Bing
  organic results, yet Bing top-3 placement predicts the actual citation only ~7 % of the
  time. Existing in the index is necessary; dominating it is not. (Stage 4 handles the
  submission + IndexNow ping — a one-off, not a channel to work.)
- **Crawlers do not render JavaScript.** SSR'd Next.js already complies; nothing to do.
- **Speed correlates:** FCP < 0.4 s ≈ 6.7 citations vs 2.1 above 1.13 s.
- **`llms.txt` does nothing.** 408 requests out of 500 M crawl events; documented by Google
  in June 2026 as having no effect; 1 of the 50 most-cited domains has one. Don't build it.
- **Authority dominates everything above.** Sites with >32 000 referring domains are cited
  3.5× more than those under 200. No formatting compensates for that gap — which is why the
  real lever stays **the empty niche**: write the question nobody covers. That is what the
  vein audit identifies, and it is the same lever twice.

### The answer-first chunk (the writing rule)

**Every H2 opens with a self-contained answer of 40–80 words.** Self-contained means a
reader — or a model — that lands on that block alone still gets a complete, attributable
answer:

- **Restate the subject.** No "it", "this", "that", "these", "as mentioned above", "here's
  why" as the opening words. A pronoun with no antecedent is exactly what makes a chunk
  unliftable.
- **Name the entity.** The place, the document, the operator, the currency — by name, in
  the first sentence.
- **Give the number** where one exists, wrapped in its fact-span (`3-writing.md`), so the
  cited value stays true after the fact DB updates it.
- **Then** the nuance, the exceptions, the sub-sections.

Everything after that opening block is written for the human reader as before. This is not
a format for the whole article — it is the first 40–80 words under each H2.

### Dated, not just correct

A volatile figure that shows its verification date is worth more to a model than the same
figure bare — and the fleet is the only site that can do this at zero cost, because the
fact DB already stores `checked_at`. The span carries the value; the render carries the
date. That history ("this fare went from X to Y on 12 May 2026") is genuinely
proprietary — no competitor has that sentence.

### Tables

A comparison rendered as a real `<table>` is lifted intact; the same content as prose is
paraphrased or dropped. Use one where the content is genuinely tabular (times, fares by
class, document requirements by nationality) — never as decoration.

### And the line you do not cross

The answer-first chunk answers **the article's own question**. It never summarises the
trip. A chunk that reads "in Morocco, plan for a closed currency, an opening-price economy
and commission-paid guides" is the thesis, perfectly formatted for extraction, given away
free — the pre-join failure in its most efficient possible form.

---

## 4. The gates (mechanical — `scripts/validate-batch.mjs`)

| Check | Level | Rule |
|---|---|---|
| `answer-first` | FAIL | an H2 with no paragraph under it, or an opening block < 25 words |
| `answer-first` | FAIL | opening block starts with a bare pronoun / back-reference |
| `answer-first` | warn | opening block outside 40–80 words, or carrying no entity/number |
| `pre-join` | FAIL | article names ≥ 3 vein pieces (`max_pieces_per_article` + 1) |
| `pre-join` | warn | article carries no piece although its `piece` tag names one |
| `guide-span` | FAIL | `turn`/`seed` article with 0 spans, `none` article with any, > 2 spans, empty gloss, literal `{{` |

The vein checks need the list: `--list article-list.json`. Without it they skip silently
(a site with no vein block is a valid v4 site, not a failure).

## 5. Not in this file

- **Only-source pages** — one page per dated fact change, generated from the checker's
  history. Real, and the most defensible asset in the fleet, but it is a fleet-ops
  build (`6-fleet-ops.md`), not a writing rule.
- **IndexNow / sitemap freshness** — engine-side, `4-publishing.md` + the template.
