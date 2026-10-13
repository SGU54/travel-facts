# Layout roles

Read before drafting and rendering. Use references/layout-architect.md for page design
and references/writing-code.md for typography. Assign visual roles so a reader can find
an answer, compare options and understand an exception without decoding a wall of prose.

## Use roles that match the content

| Role | Purpose | Suggested treatment |
|---|---|---|
| opener | Start a section and orient the reader | Clear title, optional number, restrained rule |
| ledger | Compare actual alternatives on stated criteria | Readable table with headers, units and a scope caption |
| verdict | State a recommendation and its main condition | Clearly emphasized answer, kept with its context |
| forks | Show default conditions and alternative actions | Distinct labels and parallel, readable blocks |
| figure | Explain a geographic, quantitative or procedural relationship | Appropriate size, descriptive caption and source note |
| reasoning | Explain why the answer follows | Comfortable body measure and paragraph spacing |
| reference | Supply figures, procedures or sources for later use | Scannable list or table with working references |
| divider | Separate genuinely distinct parts when useful | Part title and orientation, without filler pages |

Keep existing class names when compatible with the renderer, but let the meaning decide
which roles a section needs. A checklist does not need a fabricated verdict or table.
No fixed anchor, image or page-density quota establishes readability. Avoid making every
section visually identical when its content serves a different purpose.

## Tables and conditions

Use explicit column headers whose count matches every row. Keep scope, units and
uncertainty close enough to the table to be read with its values. Align text for scanning;
allow wrapping and repeat headers correctly when a table spans pages. Do not hide
overflow, truncate decisive text or reduce type below a comfortable use size to make a
table fit.

Label conditions by their actual role:

- **This suits you if** states the conditions supporting the printed recommendation.
- **Choose another option if** states a changed condition and the alternative action.
- A separate scope note identifies readers for whom the decision does not apply.

Do not use two labels that both mean an exception, or label an alternative as the condition
under which the default holds. If legacy for / against fields are retained, map them
explicitly to these meanings. Apply references/b-decide.md before styling the boxes.

## Classification and rendering

Prefer explicit section IDs and structured block roles. If a legacy manuscript requires
classification, support its actual markers and inspect the rendered mapping; do not
classify every table as a scored decision or every bold paragraph as a verdict. Preserve
semantic headings, lists and tables in HTML.

Associate figures, captions and evidence references with exact IDs, never loose substring
matches on chapter titles. Draw repeated facts and rules from the canonical evidence
record described in references/evidence-contract.md. A caption, carry card or diagram
must not silently drop a condition carried by the main text.

Keep an opener with enough following content to introduce the section. Avoid keeping an
entire long section unbreakable. Use overflow: visible for content unless a deliberately
cropped decorative asset requires otherwise; never use clipping to conceal layout failure.

Make recommendations findable through hierarchy and spacing, without letting a decorative
panel overpower the qualifications that make the advice correct. Use sensible font sizes,
line lengths and contrast for both print and any phone edition.

## Navigation and position

Generate contents links, bookmarks, page references and running labels from the final
section structure. Use decision counts only when they match the actual numbered set.
Check pages where a new chapter begins: a running head must identify the visible chapter,
not inherit the previous one. In a paged renderer using named strings, validate whether
string(..., last) gives the correct result for the chosen opener layout.

## Review

Run applicable layout diagnostics, then inspect representative pages and all flagged or
changed pages. Check visual hierarchy, figure placement, tables, fragments across page
breaks, links and the physical size of any carry reference. Inspect shared instructions
at their actual point of use as well as in the main chapter.

Use counts and density signals to find places worth looking at. Do not add decorative
content, filler prose or artificial roles to satisfy a numerical diagnostic. Fix unreadable
or misleading results even if every script passes. Record a tool's limits rather than
claiming that structural validation proves accuracy, visual quality or purchase value.
