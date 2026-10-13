---
name: dossier
description: Create, revise, and audit paid travel decision guides and their dated Field Sheets from a destination publisher's content, with primary-source verification, useful comparisons, consistent recommendations, and inspected PDF output. Use for premium destination manuals, foramericans guides, revised editions, and guide-plus-cheat-sheet production.
---

# Dossier

Build a guide readers can act on and trust. Deliver a useful, well edited book and
a current, independently usable Field Sheet. Quality means accurate decisions,
clear limits, readable pages, and consistent advice across every component.
A long PDF, a polished cover, or a green script alone does not establish quality.

## Start with the actual task

Read available project state and supplied material. Preserve the user's audience,
brand, title, scope, and authorized choices. For an existing edition, first compare
the prior review with the new files; keep a defect-to-fix record with page references.
Do not restart naming or ask for assets already supplied. Make reversible production
choices and continue; ask only when a missing answer materially changes the product.
Read [inputs](references/0-inputs.md).

Choose the route:
- **New guide:** research → decisions → manuscript → design → render → review.
- **Revision:** reproduce defects → update canonical evidence/content → rebuild every
  affected component → check regressions → review.
- **Audit only:** inspect supplied files, distinguish confirmed defects from unknowns,
  and report findings. Do not require a new production manifest to review an old PDF.

Use a build directory separate from this skill and preserve the user's originals.
Keep a small `state.json` with inputs, scope, current stage, evidence gaps, output
paths, and remaining issues. Reuse work that is still valid.

## The quality order

1. **Truth and scope.** A recommendation cannot outrun its evidence.
2. **Usable decisions.** Explain what to do, for whom, when, and what changes the choice.
3. **Consistency.** Book, diagrams, itineraries, summaries, and Field Sheet agree.
4. **Reading and navigation.** The reader can find and use the answer.
5. **Visual finish.** Typography, spacing, imagery, and page rhythm support the content.

Never repair layout by deleting a caveat, hiding overflow, shrinking essential type,
or shortening a correct answer until it becomes misleading. Recompose the page.

## 1. Research and product structure

Read [model](references/model.md), [mining](references/a-mine.md), and
[shape](references/a2-shape.md). The site's corpus supplies topics, voice, and useful
connections. It is not the sole authority for current prices, admission rules,
transport validity, laws, safety, or accessibility. Verify consequential facts against
the responsible operator, venue, regulator, or other suitable primary evidence.

Maintain `evidence.json` using [the evidence contract](references/evidence-contract.md).
Register the claims that change spending, access, timing, safety, or the recommendation;
do not turn every ordinary sentence into a database entry.

- Keep authority separate from volatility. An official rule can change tomorrow.
- Record the exact source, supporting passage/locator, scope, and actual check date.
- Resolve conflicting official pages; when unresolved, narrow the claim and give a
  safe, explicit verification action. Never silently choose the convenient version.
- Do not invent an observation, survey, testimonial, source, price, or date checked.
- Treat lack of inventory, unreleased dates, closure, and late arrival as different cases.
- Estimate only with named assumptions and suitable precision. Do not disguise a
  walking-speed calculation as an observed route or an accessible route.
- No guaranteed two-year accuracy or promised update service without an actual process.

The synthetic `assets/evidence-example.json` illustrates structure only. Its sources,
prices, and decisions must never become destination facts.

## 2. Make the decisions useful

Read [decisions](references/b-decide.md). For each question, identify a traveler,
feasible alternatives, a default, its assumptions, and genuine exceptions that name a
different action. Compare the same units and boundaries; show the arithmetic when
a number drives the recommendation. Distinguish per person from per party, travel
time from the complete excursion, and arrival days from full usable days.

Familiar advice can earn its place by preventing a common error or saving research.
Do not manufacture hidden traps, high stakes, scores, or exclusivity to justify a price.
Do not set page/word/image quotas from the number of source articles.

Test the assembled trip for at least the principal reader and a materially different
case (for example a short stay or reduced mobility). Check that exceptions, summaries,
and fallback routes still work when the original plan fails.

## 3. Write and bind the content

Read [writing](references/c-write.md) and [writing code](references/writing-code.md).
Use calm, concrete prose, clear headings, specific recommendations, honest uncertainty,
and short worked examples. Keep the useful reasoning; remove repeated promises and
repeated explanations. A recap should help the reader act, not repeat a chapter.

Use reader-facing citations or compact source notes that lead to an actual source.
A glyph is optional navigation, never a substitute for a citation or a confidence score.

Create `release.json` and separate book/sheet HTML templates as described in
[release](references/g-audit.md). Insert shared rules with `{{claim:claim-id}}`
and source links with `{{source-url:source-id}}`; run:
```bash
python3 SKILL_DIR/scripts/compile-guide.py BUILD_DIR
```
The compiler resolves canonical text from `evidence.json` and records hashes in
`bindings.json`. Recompile after any evidence or template change. Do not patch the
generated HTML or PDF to correct a fact. Update the source and rebuild.

Every critical published rule must have a canonical snippet, and every place that
repeats it must use that same claim binding. Inspect paraphrases and diagrams for
semantic agreement; automatic matching cannot prove all prose agrees.

## 4. Build a Field Sheet that works by itself

Read [Field Sheet](references/fieldsheet-split.md). Give it a full visible check date,
edition, exact relevant values and units, eligibility/validity, the necessary exception,
and clickable primary sources. It must contain the facts needed to execute the book's
recommendations. “Check current” is not a substitute for an available current price.

An unavailable fact may be omitted with an explicit limitation and safe action; do not
sell an incomplete comparison as finished. Include the update location only after it
has been verified. Do not publish a broken handoff between the book and its companion.
More than one sheet page is acceptable when legibility or useful content requires it.

The two documents share one release date and evidence record. They must agree.
“The sheet wins if they disagree” is not an acceptable publication policy.

## 5. Design for the actual reader

Read [quality standard](references/quality-standard.md), [brand](references/brand-tokens.md),
and `assets/design-system.md`. Use the established identity where available.
US Letter is a default for an American audience, not a prohibition on other formats.
Start from `assets/print-base.css`; adapt the format deliberately.

Body text starts around 11–12 printed points. Essential table text, captions, and
diagram labels should normally be at least 9pt at final size; furniture may be smaller.
These are design targets, not a claim of universal accessibility. Review actual output.
Never rely on CSS pixel sizes before transforms or on a zoomed-in screenshot.

Read [drawing](references/d-draw.md), [imagery](references/e-image.md), and
[cover](references/cover.md) when applicable. Use exact vector diagrams for data.
Photographs need a verified subject, suitable crop, and documented permission/license.
A stock or generated picture cannot certify a crowd, queue, route, or field observation.
No mandatory photo quota. Choose an image because it helps, not to fill a page.

## 6. Render without losing content

Read [page specification](references/page-spec.md) and [rendering](references/f-render.md).
The default path is the bundled Paged.js build through `scripts/render-guide.mjs`.
It uses explicit outputs, waits for assets, checks page count, and avoids editorial
text manipulation during pagination. The older Python compositors remain optional;
their output must pass the same release checks.

Run the compiler, render, then compare the *exact final HTML and final PDF* for **every**
document. [Content integrity](references/content-integrity.md) defines what automatic
comparison catches and what needs inspection. A changed line break is acceptable;
missing letters, changed numbers, vanished paragraphs, and truncated labels are not.

Do not claim successful rendering when dependencies, images, fonts, or pagination fail.
Use [troubleshooting](references/build-traps.md) for actual failures.

## 7. Review and release

Use [release](references/g-audit.md) as the single publication contract.
```bash
python3 SKILL_DIR/scripts/audit-release.py BUILD_DIR --prepare-review
# Inspect the actual PDF pages, sources, decisions, and links; complete review.json.
python3 SKILL_DIR/scripts/audit-release.py BUILD_DIR
```

The command checks evidence, current compiled inputs, both documents, text preservation,
PDF structure, and a review record tied to the exact artifact hashes. Missing inputs,
unresolved major issues, or an outdated review block release. It never creates a passing
editorial review automatically.

Render all pages to images. Look at the complete page sequence and inspect each page
at readable size, especially continuations, tables, summaries, and the Field Sheet.
Check actual-size reading and a cover thumbnail. Test links/bookmarks in the final files.
A second reader should challenge assumptions and try the traveler scenarios when
available; do not require a user approval just to perform an internal review.

Legacy density, rhythm, “AI smell,” and corpus-length scripts are diagnostics only.
They neither certify usefulness nor override accuracy and readability. Do not pad
the book to satisfy them. [Layout](references/layout.md) and
[compositor](references/compositor.md) explain optional refinements.

Deliver the finished requested files with a clear account of what changed, what was
verified, and any material limits. A draft can be delivered as a draft when evidence is
missing; it must not be described as ready for sale. Publishing, emailing, or updating
external marketing is a separate action requiring the user's authorization.
