# Stage G — AUDIT: is the book clean, or clumsy?

## Run ONE command — but it is THIS one.

```bash
python3 scripts/audit-release.py <build-dir> [--paper RRGGBB]
```

> **This section used to say "Run ONE command. Ship on green." and point at
> `audit-book.py`.** That was false in two ways, and both shipped books.
> `audit-book.py` never invoked `audit-furniture.py`, `audit-layout.py` or
> `audit-ai-smell.py`, so the one documented command ran one gate of four while
> SKILL.md claimed four were required. And "ship on green" overstates what any
> of this measures: these are production checks on a well-formed artefact. They
> cannot read whether a comparison is sound. **Green means releasable, not
> right.** The editorial sign-off (comparison contract, assembled trip, working
> reversals — `b-decide.md`) is a separate, human gate and no script replaces it.

`audit-release.py` runs all four, prints a verdict per gate, and **fails closed**:
a gate whose inputs are missing is `BLOCKED`, not a pass. Deliberate omissions go
through `--skip <gate>` so they appear in the record instead of vanishing.
(`audit-depth.py` used to go quiet when it could not find a corpus — a missing
input that read as an absent problem.)

`audit-book.py` remains the per-artefact PDF check and is still worth running
alone while iterating. It reads the RENDERED
PDF (once chapters flow, the DOM no longer maps to pages — the print engine makes them, so
only the PDF is ground truth). It checks:

| check | fails when | fix |
|---|---|---|
| page-shape | median fill < 66%, or > 30% of pages half-empty | FLOW the chapters (layout.md) |
| consistency | body fill swings more than 62 points | flow evens it; a slab next to a stub is the tell |
| no orphan stubs | a chapter TAIL dribbles onto a near-empty page | one flow per run of chapters, not a patchwork |
| rhythm | a text-only run longer than 6 pages | budget visuals into the dry stretch (b-decide.md) |
| cover | page 1 < 6% non-paper — a bare title | argue the thesis (cover.md) |
| depth | < 0.40 pp/article, or < 11% output/corpus length ratio | mine deeper (a-mine.md), don't pad |

> **On "corpus used":** the number is `100 × words_in_pdf / words_in_corpus`. It is
> a LENGTH RATIO, not coverage — it does not match claims, passages or articles.
> Repeating a sentence raises it; splitting one source article into two changes
> the target without adding evidence. Treat it as a prompt for a second mining
> pass, never as proof the corpus was mined. Pair it with the coverage record
> (`a-mine.md`): decisions covered, omitted, and unsupported.

Green = the book is well-filled, evenly shaped, visually paced, fronted by a cover that
argues something, AND deep enough to have used its corpus. That is "clean". Ship it.

The depth row is the one a cold build failed: it is possible to build a perfectly clean
SHORT book that skimmed its corpus. audit-book.py now refuses it. (Depth only runs if
`corpus.json` is in the build dir — always ship the corpus with the build.)

Red = "clumsy", with the specific rows to fix. Do NOT ship a clumsy book by overriding the
gate; fix the cause. Every red row maps to a reference file that says how.

## The one hard case the gate surfaces: the patchwork stub

A book that mixes flowed chapters with fixed pages will strand a chapter's tail on a
near-empty page at the seam (Greece: a 63-word Operations tail on its own page). The gate
flags it as an orphan stub. The real fix is architectural, not a patch: **make the body one
continuous flow** and mark chapter starts with `break-before: page` only where a fresh page
genuinely helps the reader. A patchwork of flow + fixed will always stub at the joins — the
gate is telling you the seams are the problem.

## Reading the individual gates

The bundled gate is the verdict; the individual scripts give detail when a row is red:
`audit-page-shape.py <pdf>` (per-page fill), `audit-rhythm.py <html>` (the visual map as a
P/f/. string). Use them to locate a failure, then fix at the stage the table points to.

---

## MERGED 2026-10-08 — three families, one entry point

`scripts/audit-release.py` was replaced by the rewrite's version and then had the
historic orchestration grafted back in. It now reports:

- the evidence/binding gates (new)
- content integrity, final HTML vs final PDF (new)
- `legacy_gates()` → `audit-release-legacy.py`, the six gates this file already describes
- `audit-source-defects.py` → truncated cells, repeated `<thead>` rows, a word split
  across a page turn

Read `references/evidence-contract.md`, `references/content-integrity.md` and
`references/quality-standard.md` for the three new families.

**A gate that cannot run is BLOCKED, never a pass.** `audit-content.py` needs Node
Playwright and will block here; that is the correct behaviour and must not be read as
a clean sheet.

**Do not retire the legacy gates.** They are the only ones that currently run end to
end on the seven existing books, none of which has an `evidence.json` yet.
