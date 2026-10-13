# Diagnose actual render failures

Start from the failing command, exact source paths, and its error output. Keep the previous
good build and change one cause at a time. Never claim a patch applied without checking
the target changed and inspecting the newly generated output.

## Missing runtime or assets

The Node renderer needs Playwright plus a compatible installed Chromium. A Node package
alone does not include a usable browser. If launch fails, report the missing dependency;
install through the environment's supported process when allowed. Do not report a
successful render or silently deliver an old PDF.

Use the bundled assets/paged.polyfill.js.gz. Do not overwrite it with an unverified download
or an HTTP error page. Source styles should be inline for local Paged.js builds. Keep
font/image dependencies as real local files, confirm decoding, and list them in the build
asset manifest. Wait for readiness promises, not an arbitrary sleep.

## Lost or unexpected pages

Check pagination completion and errors, dimensions, named pages, oversize unsplittable
blocks, and whether the final chapter exists in the PDF. Source and output must be the
explicit files in release.json; a PDF found by a directory glob may be the companion sheet.

Do not assume a short file means a rendering failure: it may be the wrong input. Do not
assume the expected page count means success: some text may still be clipped or missing.

## Page seams

Borders/padding may repeat on fragmented elements; use source grouping and restrained
separators, then inspect continuation pages. Headings need body lines beneath them.
Long tables should split intentionally with repeated headers. Avoid nested “keep together”
wrappers that make a group taller than a page.

For a word split across pages, first reproduce it with a small fixture. Disable the
responsible typography/compositor feature or recompose the paragraph. Preserve the full
word in source; audit the final output. Do not patch a PDF text layer over a visible defect.

## Figure and navigation errors

Measure real SVG label bounds after transforms; guessed character widths cannot certify
containment. Keep unique IDs and generated figure numbering. Test link destinations and
bookmarks in the final PDF. A removed Sheet section must not leave a contents row with
folio zero or a bookmark pointing to another chapter.

Every changed input requires recompilation/rendering of affected outputs and a fresh
review. Legacy diagnostic heuristics never authorize skipping a required check.
