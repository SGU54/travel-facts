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
