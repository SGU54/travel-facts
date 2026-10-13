# One release contract

Run `scripts/audit-release.py BUILD_DIR`. Both the book and the Field Sheet are
required. A failed, missing, skipped, inconclusive, or outdated check is not a pass.
The command never substitutes for actually reading the sources and viewing the output.

## Build manifest

`release.json` uses explicit files; no alphabetical PDF discovery:

```json
{
  "schema_version": 1,
  "title": "Destination decisions",
  "edition": "2026.10",
  "release_date": "2026-10-08",
  "purpose": "publication",
  "evidence": "evidence.json",
  "review": "review.json",
  "assets": ["img/A01.jpg", "fonts/body.woff2"],
  "documents": [
    {
      "id": "book",
      "template": "book-template.html",
      "html": "book.html",
      "pdf": "dossier.pdf",
      "critical_json": "book-critical.json",
      "page_size_pt": [612, 792]
    },
    {
      "id": "sheet",
      "template": "sheet-template.html",
      "html": "sheet.html",
      "pdf": "fieldsheet.pdf",
      "critical_json": "sheet-critical.json",
      "page_size_pt": [612, 792]
    }
  ]
}
```

Use the real title, edition, and check date; the dates above are illustrative.
All paths are relative to BUILD_DIR, distinct, and inside it. Remove unused sample asset
paths; list the actual local assets including fonts and CSS. A phone edition can add
id `phone`, using the book's canonical display text but its own layout and PDF.
`page_size_pt` is optional; omit it only when varying page sizes are intentional.

Use purpose `proof` only for clearly labeled synthetic development fixtures.
A proof can pass the checks but is never declared ready for publication. Reserved example
source URLs are rejected for a publication. Neither mode verifies the network automatically.

## Canonical compilation

`evidence.json` follows evidence-contract.md. Use these literal template tokens:

| Token | Resolves to |
|---|---|
| `{{claim:claim-id}}` | That claim's canonical display for book/sheet |
| `{{source-url:source-id}}` | Escaped URL for a source link |
| `{{source-label:source-id}}` | Source's optional label, or its ID |
| `{{title}}` | Manifest title |
| `{{edition}}` | Manifest edition |
| `{{release-date}}` | Manifest full release date |

Tokens are escaped as text/attribute values, not evaluated as code. Canonical snippets
are plain text. Reuse the same claim token in repeated rules, cards, and SVG labels.
Different book/sheet display strings must retain the same scope and exception.

```bash
python3 SKILL_DIR/scripts/compile-guide.py BUILD_DIR
```

This writes compiled HTML, each critical-snippet JSON file, and bindings.json with
input hashes and occurrence counts. All critical snippets declared for a component must
be bound in its template. Unknown tokens and stale generated output block release.
`--check` verifies without rewriting. Corrections belong in templates/evidence, not
generated HTML. List dependency files in assets so their changes invalidate the record.

## Checks and their limits

| Check | What it establishes |
|---|---|
| evidence | Declared support, primary-source requirements, dates, units/calculations, conflicts, Sheet coverage |
| bindings | Compiled text and critical occurrences still match current templates/evidence/assets |
| PDF per output | Readable file/text layer, title, text bounds, declared size, source links, internal destinations/bookmarks |
| content per output | Expected text and required snippets survived final rendering |
| review | Actual reviewer, all pages inspected, scenarios and checks complete, exact current hashes, no unresolved major issues |

Small text is reported for visual review because the script cannot know whether a
particular span is essential content or furniture. PDFs still need a human/model visual
read. An evidence register does not prove the listed website really supports its claim;
the reviewer must open and compare it. Semantic contradictions in unregistered paraphrases
can also require a real reading.

## Review the actual artifact

```bash
python3 SKILL_DIR/scripts/audit-release.py BUILD_DIR --prepare-review
```

The command creates a **pending** review.json and returns BLOCKED until inspection is
complete. It does not overwrite an existing review. Retain prior observations when
updating an edition, then refresh hashes and checks only after inspecting changed files.

The record includes reviewer, actual review date, hashes of release/evidence/bindings,
and per-document PDF/HTML hashes plus page count. Complete:

- `pages_viewed`: the one-based pages actually inspected, each once.
- `checks`: facts, decisions, consistency, visual, navigation; each `pass` only after
  its work has been done.
- `notes`: concrete observations, including any small-type warnings resolved by inspection.
- `scenarios`: at least two distinct entries `{id, result:"pass", details}` for the
  main reader and a materially different profile or failed-plan case.
- `open_issues`: empty, or explicitly accepted minor issues with an explanation.
  Critical/major issues block publication.

Rasterize all pages; inspect both the sequence and readable detail of each page.
Read every relevant source, execute the comparisons, apply exceptions, and walk the
assembled itinerary. Test core external destinations when network access permits;
a failed fetch is not by itself proof of a broken website. State unverifiable destinations
as unresolved rather than inventing an HTTP outcome. Check local PDF navigation too.

Then rerun audit-release. Any later source/asset/PDF edit invalidates the corresponding
review. Hash matching records which files were reviewed; it cannot establish that a
reviewer actually looked at them. Never fabricate the attestation.

## Legacy diagnostics

The older audit-book/layout/furniture/rhythm/marks/AI-smell/depth/synthesis scripts can
help diagnose a legacy template. They are not the release contract and their style,
page-fill, corpus-ratio, or image-count assumptions must not force extra pages, smaller
type, unsupported conclusions, or irrelevant pictures. A modern build need not satisfy
a historical brand's paper-color or furniture geometry.
