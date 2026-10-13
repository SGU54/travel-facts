# Stage A — Mine the corpus

**Ten minutes here saves a 38-page padded book.** Rome's v1 was 38pp with the decisions
padded to 0.6% ink because 58 of 96 articles were unused. The corpus check is what caught it.

## Is this destination viable at all?

```python
import json, re, collections
arts = json.load(open('<export>.json'))
def W(a): return len(re.sub('<[^>]+>',' ',a['content']).split())
by = collections.defaultdict(list)
for a in arts: by[a['category_slug']].append(a)
for c in sorted(by):
    print(f"{len(by[c]):3}  {sum(W(a) for a in by[c]):6,}w  {c}")
print("TOTAL:", sum(W(a) for a in arts), "words across", len(arts), "articles")
```

**The yield model** — measured across two real builds, and it is remarkably stable:

| | articles | words in | pages out | **pp/article** |
|---|---|---|---|---|
| Rome | 96 | 101k | 50 | **0.52** |
| Greece | 80 | ~85k | 41 | **0.51** |

**≈ 0.5 pages per article.** Use it to set expectations *before* you write a word:

```
expected_pages ≈ articles × 0.5
```

- **< 40 articles** → not yet. Write more first.
- **40–70** → 20–35pp. Fewer decisions, drop the day-trip chapter.
- **70–100** → 35–50pp — the full shape.
- **100+** → 50pp+, and now the constraint is editorial, not evidentiary.

**If the estimate disappoints, say so at Stage A — not at Stage G.** 80 articles buys ~41
pages. That is the honest number. The dishonest levers are padding and white space; the
honest ones are:

1. **More decisions.** Rome mined 13, then found 2 more STRONG veins on a second pass
   (7,562w and 4,166w) that it had walked past. **Do the second pass before writing.**
2. **A denser page.** Greece's essay pages run **2.1% ink** — the type is set for a book
   half its length. 13.4px/1.68 on a 6.8in measure is ~95 words of body per page; Rome's
   decision pages carry 300+. If the corpus is thin, the answer is more per page, not more pages.
3. **More figures.** A route graph, a section drawing, a comparison grid — each is a page
   that argues, drawn from facts already in the corpus. Greece shipped **7 figures for a
   book about a ferry network**. That is the vein it left unmined.

**What NOT to do:** stretch leading, inflate margins, add a photograph per chapter, or run
a chapter divider page. All four were tried on Rome's 38pp draft and all four read as padding.

## Which decisions can this destination support?

For each candidate decision, sum the words in the categories that feed it:

```
STRONG   > 9,000w   → a full decision with a real ledger
VIABLE   5,500-9k   → a decision, but check for substance not repetition
THIN     < 5,500w   → do NOT write it; it will pad
```

Rome's unmined STRONG veins found this way, late: the Colosseum tier fork (7,562w) and
aperitivo-vs-dinner (4,166w). Both became real decisions. Two THIN candidates were correctly
refused.

## The trap

**Ink coverage, not page count, is the quality signal.** Ask of every planned page: *what
does this resolve that a free blog post doesn't?* If the answer is "it lists things" — cut it.

## Output of this stage

- category inventory with word counts
- the decision shortlist, each tagged STRONG/VIABLE/THIN with its evidence
- an honest page-count estimate
- **the list of what this destination CANNOT support** — the refusals are as valuable as
  the plan, and they go on the back-matter page


## The yield model is now ENFORCED, not just advised

`scripts/audit-depth.py` (bundled into `audit-book.py`) checks three signals of
under-mining, calibrated on real builds:

| signal | floor | a thin build (cold Greece, 19pp) |
|---|---|---|
| pages / article | >= 0.40 | 0.24 |
| words / article | >= 120 | 90 |
| % of corpus words used | >= 11% | 8.8% |

A cold rebuild of Greece passed every *organization* check at 19 pages — clean, evenly
paced, good cover — while using 9% of an 80-article corpus that supports ~40 pages. The
audit that measures layout cannot see thinness; the depth gate can, and now fails that book
before it ships. If you come in thin, the fix is the second mining pass and deeper
decisions (250-350w of body each), NOT padding — padding fails the page-shape check.

## The synthesis viability check — is there anything to SELL here?

Before committing to a build, confirm the corpus actually has synthesis to sell (the whole
premise of `references/model.md`: the reader pays for connections the free articles don't
make). Once you've found the organising fact at A2, name its 2-5 component themes and run:

```bash
python3 scripts/audit-synthesis.py corpus.json \
  "theme1 regex" "theme2 regex" "theme3 regex" ...
```

It counts how scattered the themes are (raw material) versus how often a single article
already connects them (synthesis already free). **STRONG** = scattered and rarely pre-joined
→ the book's value exists. **WEAK** = the corpus already connects them in many articles →
the synthesis a buyer would pay for is largely free; find a deeper organising fact whose
parts aren't pre-joined, or accept this is a thin dossier.

> Greece, real themes (meltemi / ferry types / fixed return flight / sequencing): scattered
> across 19/21/13/9 articles, joined in only 2 → HEADROOM 4.2, STRONG. The connection is the
> product.

Do NOT let the script auto-pick themes — it can't, and guessing picks filler words and
returns a false WEAK. The themes are the organising fact's real parts, which is a judgment
you make at A2, not a tally.