# Book and Field Sheet

The book explains choices and their reasoning. The Field Sheet provides the dated
values, rules, links, and checks needed to act on them. Both are release artifacts.

## What the Sheet must contain

Print the complete check date (YYYY-MM-DD or unambiguous written equivalent), edition,
destination, and intended user. For each relevant item, show the amount/rule, unit,
eligibility, validity, key exception, and a clickable authoritative source.

Examples of scope to make explicit: adult/child, zone, one-way/return, per person/per
vehicle, night/day/journey, tax component, included airport access, activation period,
required identification, and a tariff's effective dates. Include only the fields that
matter to this decision; avoid a huge generic checklist.

“Check current,” “higher tier,” and a domain without the relevant booking page are not
complete entries when an actionable value or exact rule can be verified. If primary
information cannot be obtained, state the limitation and a specific safe action; do not
claim the comparison is complete or invent a number to fill the cell.

Show at least one worked calculation when a price comparison drives a prominent choice.
Use the same quantities and boundaries as the book. A tax increase may change the budget;
knowing about it does not itself save that tax.

## Shared content

Both outputs compile from evidence.json. Bind the canonical rule into all repeated
locations, including cards and SVG labels. The book can use a longer explanation and
the Sheet a compact display string, but the exception and scope must survive.

A rule change can reverse the recommendation. Update dependent text, diagrams, itinerary
notes, summaries, and calculations. Do not state that only numbers change, or that the
Sheet automatically overrides contradictory book text. One release must agree with itself.

## Handoff and maintenance

Link the book to the actual delivered companion or a verified public update location.
Where local companion links are unsuitable for the delivery platform, identify its exact
filename and give a tested public update link if one exists. Do not invent an endpoint,
write a dummy URL into the final product, or promise emailed updates without that service.

Choose recheck intervals according to volatility and consequences, and verify before a
new publication. Record who/what process is responsible; a printed “quarterly” label is
not an automated update. A metadata creation date is not the visible fact-check date.

## Build and validation

New builds use two templates and two explicit release.json entries. Avoid combining and
splitting them when independent templates are simpler. Each is inspected and audited:
evidence coverage, canonical text, PDF text preservation, readability, date, and links.
Allow two or more pages when one page would hide conditions or shrink useful text.

For an existing combined HTML, the optional fssplit.py can extract the Field Sheet.
Read its command help, verify the actual section ID and retained wrapper CSS, then use
the split files as the final render sources. Update the book's contents and cross-links;
a removed section must not retain a page number of zero or an obsolete destination.
Splitting is not an exemption from the two-document audit.
