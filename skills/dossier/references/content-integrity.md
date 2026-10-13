# Preserve content through rendering

## Contract and commands

Compare each final PDF with the exact pre-pagination HTML used for that document.
Audit the Book and Field Sheet separately; also audit a phone edition if shipped.

```bash
python3 scripts/audit-content.py BUILD/_book.html BUILD/dossier.pdf --critical-json BUILD/book-critical.json --json
python3 scripts/audit-content.py BUILD/_sheet.html BUILD/fieldsheet.pdf --critical-json BUILD/sheet-critical.json --json
```

Use explicit paths from `release.json`; never choose the first PDF or HTML returned
by a directory glob. Do not compare the Book with the combined Book + Sheet source.
Do not use a paginated DOM snapshot as the source: it can already contain a loss.

Interpret the exit code:

- `0 / PASS`: the inspected text agrees within the documented normalization.
- `1 / FAIL`: words, numbers, symbols, or critical snippets differ.
- `2 / BLOCKED` or `INCONCLUSIVE`: an input, parser, dependency, or source visibility
  assumption prevents a reliable result. It is not a pass and must block release.

Inspect the JSON's missing/unexpected token counts, source examples, PDF page
examples, critical results, normalizations, and excluded furniture. Repair the
source or compositor, render again, and rerun the audit. Never lower thresholds,
remove critical snippets, or edit extracted PDF text to obtain green output.

## Critical snippets

Use a non-empty JSON list. Each entry has a unique `id`, a non-empty `text`, and a
positive integer `min_occurrences` (default `1`):

```json
[
  {
    "id": "airport-ticket-exception",
    "text": "The urban single ticket excludes the airport metro",
    "min_occurrences": 1
  },
  {
    "id": "booking-comparison-seam",
    "text": "compared when booking",
    "min_occurrences": 1
  }
]
```

Check the minimum in both source and PDF. A snippet absent from the source is a
failure too. Declare the actual approved wording of operational rules, prices,
dates, eligibility conditions, negations, and exception clauses. A snippet does
not prove those statements true; evidence review and contradiction checks remain
separate gates. A larger minimum does not localize occurrences: use distinct,
context-bearing snippets for different tables/cards instead of assuming that a
global count proves the right version is present in each location.

## What is normalized

Use a strict token multiset comparison with no percentage-loss allowance. One
missing word is enough to fail. Preserve letters, accents, digits, currency and
percentage signs, and the guide's provenance glyphs. Normalize Unicode NFKC,
ligatures, case, typographic apostrophes, and soft hyphens.

Join a line-end hyphen only when both printed fragments exist and concatenate
to a word in the source. Reattach a floated drop cap only when the actual glyph
is present, its geometry places it beside the first line, and the concatenation
is a source word. Rejoin tracked lettering only from the actual printed letters.
Never infer or restore absent characters: `ared` must not become `compared`.

Exclude scripts, styles, metadata, templates, explicitly hidden elements, and
running furniture from the expected source. Inspect print computed styles with
source JavaScript disabled. Include SVG text; do not pretend that this reads
labels baked into raster images. Use `data-content-audit="furniture"` only for
genuine running heads/folios, not as an escape hatch for substantive content.

On the PDF side, recognize running furniture only at page edges, preserve cover
content, and report each exclusion. Resolve named running strings from their
`string-set: name content(text)` source selectors. For a generated TOC folio,
require a local source anchor, its named PDF destination, and its label plus the
correct page number printed in the matching link rectangle. Add only that
verified folio to the expected tokens; never ignore all extra numbers. Custom
page-counter resets and unresolved references require review. Recognize repeated
table headers near page tops. Ambiguous extraction or generated body content requires review rather than
a forgiving similarity score. A scan or PDF with no extractable text cannot pass.

The primary source reader requires Node, Playwright, and Chromium. PyMuPDF reads
the PDF. If Chromium cannot run, the restricted lxml fallback can validate simple
stylesheet-free HTML; it reports `INCONCLUSIVE` for unevaluated stylesheets. Do
not use that fallback to certify a designed guide whose print CSS was not read.

## Render without editorial mutation

Prefer the explicit renderer:

```bash
node scripts/render-guide.mjs BUILD
```

It reads `release.json` with `documents: [{id, html, pdf, critical_json}]`. Paths
are relative to `BUILD`; `critical_json` defaults to `<id>-critical.json`. Supply
all font/image/style assets locally. `DOSSIER_CHROMIUM_EXECUTABLE` may select an
already installed compatible Chromium. The renderer loads the bundled
`assets/paged.polyfill.js.gz`, waits for fonts and images, rejects page/asset errors,
and checks DOM/PDF page counts. Request outlines and tagged output from supported
Playwright versions; inspect the result without claiming PDF/UA conformance.
It performs no prose rewrites, table shortening,
or paragraph-specific editorial repairs. It replaces a final output only after
the source/PDF text audit passes; a failed draft remains `.unverified.pdf` with
its audit report. Run the full release audit afterward.

Read legacy renderer scripts before using them. Their figure fitting, feathering,
and pagination measurements can move content but do not themselves prove its
preservation. The reviewed legacy scripts ended with a page-count assertion;
that cannot detect losing four letters while keeping the same number of pages.
A page-count check cannot establish text preservation. Do not attribute a lost
fragment to a specific compositor pass unless reproduced from the original source.

## Verification and limits

Run `python3 scripts/test-content.py`. The deterministic tests read a small HTML
fixture, generate genuine selectable PDFs, and exercise an intact `com- / pared`
page seam and a broken `ared` seam, accents, ligatures, soft hyphens, a floated
drop cap, a table, price loss, changed negation, empty input, invalid PDF, and the
critical-snippet contract. A separate end-to-end Paged.js test runs when Chromium
is available; if unavailable it explicitly reports `SKIP`, not successful render
validation. Do not describe the ReportLab fixtures as a tested Paged.js build.

A multiset can miss words moved between sentences. Case and most punctuation are
intentionally normalized. Critical snippets improve local sequence checks but do
not prove semantic agreement, fact accuracy, accessibility, reading order, glyph
visibility, or that text outside the page crop is visible. Continue to render and
inspect pages and run geometry, factual, operational, and editorial gates. Never
replace those reviews with this check.
