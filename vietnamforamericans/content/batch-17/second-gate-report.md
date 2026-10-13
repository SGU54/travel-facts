# Batch 17 — second gate (ChatGPT, 2026-10-12)

All five dry ground, no Task B. Task A: FAIL, **nine actionable, all fixed in one round.**
Dry-ground check: PASS.

## A customs fact applied in the wrong direction

The worst finding, and a new shape:

> *"On the way out, Vietnam's own allowances apply to what you are carrying, and goods beyond
> **a total customs value of 10,000,000 dong per entry** must be declared."*

`customs.goods_value` is an **entry** duty-free allowance. I quoted the number correctly, kept the
words "per entry" inside the span, and then wrote a sentence applying it to **departure**. Every
customs fact in the layer concerns entry; nothing establishes a Vietnamese exit declaration
threshold for ordinary goods. The whole sentence was removed.

The span was right. The direction was wrong. That is the third distinct way this project has
shipped a correct fact inside a false statement — after the paraphrase (batch 14) and the gloss
(batch 15/16). **The check is not "does the span match the fact" but "is the claim the sentence
makes the claim the fact supports".**

## Dietary guidance — the consequential class on this batch

*"These places are **entirely plant-based** — no fish sauce, no meat stock"* against, later in the
same article, *"com chay cooking is **largely** vegan"*. A contradiction, and the categorical half
is the dangerous one: someone with a religious or medical requirement would act on it. Rewritten
to describe what these kitchens cook without, and to say explicitly that egg and dairy should be
confirmed at the individual place rather than assumed from the category.

Also *"Near any significant pagoda, **there will be** vegetarian food close by. That is a reliable
rule"* → a search heuristic, not a guarantee of availability.

## The rest

- **Frozen price in words, again**: *"a few thousand dong each"*. The excerpt guard catches
  excerpts; this was in the body. Removed.
- **Outcome guarantees on the tours article**: *"you stop being nervous about street food"* and
  *"changes how you eat for two weeks"*.
- **Business norms stated as observations**: "five or six" stops, "two to four hours", "three to
  five dishes", "four to six people", "a dozen or more" che. Converted to questions to ask or to
  unquantified description.
- **An unsupported ratio**: *"a street food tour gives you more of the eating... in half the time"*,
  calculated against a class duration the article never states.

## The excerpt-to-body table

The gate produced one on request, and it earned its place: two excerpts overstated their bodies.
*"Yes, on the first evening, and no later than that"* where the body argues early rather than late,
and *"what a good one does that you cannot do alone"* where the body says "cannot easily get on
your own". *"Most classes rush it"* asserted a prevalence the body never establishes. Keep asking
for this table.
