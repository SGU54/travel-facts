# Layout decisions and their limits

The quality standard and page-spec.md govern the finished artifact. This reference helps
choose consistent composition; it does not override truth, scope, or readability.

## Whole-document decisions

Choose the actual reading format, a comfortable body size, a useful column width, a small
type/spacing hierarchy, the brand palette, and navigation. Use a single system across the
book and a compatible, independently usable Sheet. A phone edition is a separately
composed layout, not a shrunken print PDF.

Keep page margins for reading and furniture. A background may be white or tinted.
Check continuation pages for the same intended treatment as openers. A full-bleed cover
must not force ordinary text onto the trim edge.

## Page-level decisions

Give the answer a clear hierarchy. Explanations, notes, exceptions, data labels, and
decorative furniture have different jobs. Essential qualifications need enough size
and contrast to be read; a subordinate role does not justify 5–6pt type.

Tables need comparable units, explicit headings, and widths proportionate to the amount
of information. A single sentence under a number can be clearer than a dense multi-column
table. Figures should remove a reading burden; they need not meet a density quota.

A chapter end can breathe. Distinguish an intentional tail from an accidental orphan
fragment. Useful whitespace is acceptable. Repetition, redundant headings, decorative
boxes, and irrelevant photographs are not remedies for an empty region.

## Optional measured refinements

A local adjustment to spacing, a photograph's crop, or a break rule may improve a seam.
Measure its impact and compare before/after at final size. Keep meaningful sequence and
image-caption relationships. Do not globally compress the book or widen every paragraph
because one chapter has a tail.

If a paginator pass changes DOM fragments, text integrity becomes a required postcondition.
A lost word must block release even when all pages look full. The safe fallback is to
remove the offending pass and recompose the source, not patch the final PDF.

## Review record

Use release.json and review.json for the actual files. Record pages inspected and concrete
findings, unresolved issues, and the result of applying different traveler scenarios.
Do not fill a review by inferring that the code “should” have produced a good page.
