# Render the explicit outputs

Use release.json to name source templates, compiled HTML, PDFs, and critical snippets.
Never choose “the first PDF in the directory.”

## Default sequence

```bash
python3 SKILL_DIR/scripts/compile-guide.py BUILD_DIR
node SKILL_DIR/scripts/render-guide.mjs BUILD_DIR
python3 SKILL_DIR/scripts/audit-release.py BUILD_DIR --prepare-review
# Review actual outputs and complete the pending review record.
python3 SKILL_DIR/scripts/audit-release.py BUILD_DIR
```

Use the runtime's Node/Python executables when provided. The renderer needs Node
Playwright and an installed compatible Chromium; Python gates need PyMuPDF and their
documented dependencies. Missing dependencies mean BLOCKED, never successful output.
Do not silently switch to printing raw unpaginated HTML or deliver a half-built PDF.

The renderer waits for the complete DOM, fonts, and image decoding; injects the bundled
Paged.js polyfill; waits for pagination completion; prints with CSS page size and
backgrounds; and checks output through audit-content. It does not rewrite prose.
Keep source CSS inline and image/font assets local for a reproducible build.

## What to inspect

Compare final HTML and PDF for lost words, changed numbers, incomplete captions,
missing rows, and repeated/omitted paragraphs. Extracted text helps locate a defect;
it does not replace viewing the pages. Use content-integrity.md to interpret uncertainty.

Render all pages to images. Check a sequence view, then every page at readable size.
Verify continuation headers, page numbers, breaks, tables, and figure labels. Assess
printed size, the cover thumbnail, and the Sheet's actual reading conditions.
Links/bookmarks are tested after any navigation postprocessing; that final PDF is hashed
in review.json. Any later edit invalidates the review.

## Optional advanced compositor

The historical Python renderers can help an established build with its own layout
contract. They need Python Playwright and pypdf. Read compositor.md before use.
Their page-count check alone is insufficient. If a pass loses text, revert the pass or
change source layout. Do not reconstruct missing letters in the final PDF.

Density, image rhythm, and punctuation measurements can guide a review. They are not
publication gates. The required release command is audit-release.py, for both outputs.

The bundled polyfill is stored losslessly as assets/paged.polyfill.js.gz; the default
renderer decompresses it automatically. For a legacy Python build, decompress it to
BUILD_DIR/paged.polyfill.js before running the older renderer.
