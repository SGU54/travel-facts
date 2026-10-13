# Batch 20 — second gate (ChatGPT, 2026-10-12). The final batch.

Two seeds + three dry ground. **Both seeds PASS at TRUST 85 on the first round**, all three checks
each, and the gate confirmed neither duplicates any of the eight handoffs already published on the
site. Task A: FAIL, five actionable plus several cross-checks, all fixed.

## The visa audit the brief asked for

I asked for a sentence-by-sentence scope check of the Cambodia article's visa section against
PARAPHRASE / GLOSS / DIRECTION, and it paid for itself twice:

**GLOSS, confirmed.** The article correctly said a Vietnam–Cambodia–Vietnam trip needs *"either a
valid multiple-entry visa covering the return, or a second visa approved before you come back"* —
and then, four paragraphs later, *"it is the version that needs **the multiple-entry visa**"*,
silently deleting the alternative it had just given. Fixed.

**Direction ambiguity in the example.** *"An e-visa naming Tan Son Nhat does not work at a land or
river border"* does not say which field it means. The rule covers entry and exit separately, so the
example now states both: the entry you make must match the entry port you named, the exit the exit.

**Subject blurring.** The no-extension span sat immediately after the port advice, which reads as
though it bars amending a port. It establishes a duration rule. Now in its own paragraph.

## The arithmetic again

*"The flights and the transfers eat a day at each end, Angkor itself wants three, and the week that
remains cannot hold Vietnam's three regions."* Fourteen minus two minus three is nine, not seven.
Now stated as nine, at the pace of the ten-day plan.

## The excerpt that contradicted its own article

*"The famous ones are for visitors and the good ones are not"* against the body's *"Both are worth
seeing"* and its description of Hoi An's market as both at once. Third batch running that an
excerpt was a finding; the excerpt guard in `check-batch.py` catches prices and counts but cannot
catch a thesis the body disowns. Asking the gate for the excerpt-to-body table is what catches that.

## Cross-checks against published articles — all clean except three wordings

- *"a day trip from Ho Chi Minh City **cannot work**"* was broader than the published claim, which
  is about the morning-departure coach circuits. Narrowed to that.
- Phu Quoc November–April and Nha Trang January–August called *"the opposite end of the year"*,
  when they overlap January to April. Corrected.
- Con Dao given as "four or five days" here against "three or four nights" in batch 19. Harmonised
  on nights.

**Frozen prices: none in any body or excerpt. Dry ground: PASS on all three.**
