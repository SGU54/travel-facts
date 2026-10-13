# Optional advanced compositor

The legacy render-paged.py and render-paged-fit.py scripts contain measured layout passes
for older dossier templates. They are optional tools for those builds; the default
render-guide.mjs uses straightforward pagination and post-render checks.

Read the selected script before adapting it. Its measurements and CSS selectors may depend
on a particular page size, section classes, figure conventions, or old browser behavior.
Do not assume a historical engine limitation remains true without reproducing it.

## Safe refinement order

First correct the source structure, repeated table headings, heading/body grouping,
figure-caption grouping, and page breaks. Then adjust nonessential spacing locally.
Resize or crop a photograph only when the subject remains useful. Redesign a crowded
diagram before reducing its essential labels below the final printed size target.

A page-flow engine may split a paragraph or section into fragments. The first fragment
may retain the original ID while later ones use a shared data reference. A script that
only inspects the first fragment can silently skip continuation-page defects.
Measure the actual rendered fragments and group them carefully.

## Text is not a layout lever

Never delete nodes, move partial words, hide text outside a crop, or remove qualifications
to make a page fit. Automatic hyphenation and split-word repairs need special scrutiny.
Prefer a manual/no-automatic-hyphenation setting when page seams become unreliable.

Every pass must have an observable before/after condition and be reversible. A loop
must have a finite limit; if it cannot improve the layout while preserving content,
report the issue and change the source composition. Do not keep feeding unrelated photos
into chapter tails or let a “fit” pass shrink all figures without checking their labels.

## Required output checks

Assert pagination completed, assets decoded, and DOM/PDF page counts agree where the
engine exposes the count. Then run audit-content on the exact final source and PDF,
for the book and the Sheet, followed by audit-release.

A correct count does not prove that the last paragraph survived. Inspect page boundaries,
figure labels, and any block touched by a layout pass. Added navigation or PDF
postprocessing is another final-artifact change and invalidates a previous review hash.
