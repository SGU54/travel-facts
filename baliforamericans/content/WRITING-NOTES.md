# Writing notes for baliforamericans batches (learned on batch 1's second gate, 2026-10-13)

Batch 1 needed four review rounds. Every failure was one of these, so write to avoid them from the first draft:

1. **No absolutes the article later qualifies.** "Every foreign tourist pays" fails when the next section lists exemptions. Write "foreign tourists pay, with a short list of exemptions".
2. **No claims about how people or institutions behave** unless facts.json carries them: what rental shops do, what police look for, what insurers decide, what customs officers ask, how often checks happen, what "usually" happens. State the rule; leave the behavior out.
3. **Do not stretch a sourced sentence past its scope.** The State Department line about cars and motorcycles says nothing about pedestrians.
4. **No invented durations or quantities** ("five minutes", "takes weeks", "a ten-minute call").
5. **Label advice as advice** ("our advice is practical, not official") and keep it separate from the documented requirement.
6. **Opening paragraph under each H2 is 40-80 words** and names its subject; check after every edit, cuts push it under 40.
7. **One canonical wording per fact key** across the whole site: the DB value replaces the span text at render (see ../fact-spans.json).
8. The review model's trust score moves about 7 points between runs on identical text. Fix what it names, re-run once, and judge the named reasons, not the number alone.

Pipeline per batch (all in this folder): write src/*.html + meta.json -> build.py -> make-gate.py NN -> review in ChatGPT -> fix ->
image-queries.json -> source-images.py NN -> contact-sheet.py NN (+ crops at full size) -> picks.json -> place-images.py NN ->
upload-batch.mjs -> finalize.py NN -> validate-batch.mjs -> articles-batch.mjs update -> seed facts -> publish -> links.

## Vein audit at 20 articles (2026-10-13, dossier/audit-synthesis.py, 4 themes each)
entry-stack 2.4 · scooter liability chain 2.1 · health chain 2.9 · holiday calendar 3.8 · money leak 3.9.
All thin (2-4), none a vein yet; the paperwork theses are the most pre-joined (2-3 articles already carry all four parts).
The geography theses (base split x drive times x boat days x flight home; season x coast) could not be measured: no
articles exist. Working rule until the re-run at 40: every area / transport / itinerary article carries ONE of
{base choice, drive time, boat-day placement, season-by-coast} in depth and only names the others in a sentence.
Do not write an article that works out base + drive times + boat day + departure day together: that is the guide.
No `vein` block written to article-list.json yet (a signal at 20, not a verdict). Re-run at 40.

## Vein audit re-run at 41 published articles (2026-10-13, 4 themes each)
health chain 4.8 (medication / vaccines-dengue / hospital-deposit / insurance; only 1 article joins all four) -> the one thesis above 4.
base x drive time x boat x last night 3.3 · season x coast x base x calendar 3.3 (both thin-but-real, and the 32 remaining
articles are the ones that feed them) · liability chain 2.3 · money leak 2.3 · entry stack 1.9 (dead: already joined in 3 articles).
Rule for the remaining area / itinerary / stay articles is unchanged and now measured: ONE geography piece per article.
The itinerary articles are the danger: they must give a day order, and must NOT also work out base choice + boat-day placement +
last-night location in one place. No `vein` block is written to article-list.json: choosing the thesis is the dossier build's call.
