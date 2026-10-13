# Draw an accurate, useful figure

Choose a figure when spatial relationships, a sequence, a comparison, or a branching
rule is clearer visually. Use vector shapes/text for exact diagrams and charts.
A pretty picture is not evidence that a route or recommendation works.

## Data before geometry

Use the same evidence.json claims and calculated values as the prose and Sheet.
Label a diagrammatic map as diagrammatic. Give a scale only when the projection,
coordinates, and drawing support it. Source geographic coordinates and route facts.
Straight-line distance multiplied by a constant is an estimate, not a measured route.

For walking time, record origin/destination, actual route or estimation method, slope,
stairs, accessibility limits, and assumed pace where applicable. A shortcut can be
closed or ticketed. A short distance is not proof of step-free access.
Do not make the geography fit the thesis; change the recommendation when necessary.

For comparisons, keep alternatives, units, and time/cost boundaries identical to the
decision table. For timelines, include an explicit start/end and all dependencies.
Opening dates, sold-out inventory, and booking-release windows are different states.
For decision trees, include the same exception that changes the prose recommendation.

## Build for final size

Use a root SVG viewBox matched to the intended aspect. Avoid nested whole-figure
scaling. Essential labels normally print at least 9pt. If a figure shrinks from
652 units to 489 printed points, a 12-unit label becomes 9pt; transforms compound.

Wrap long labels into explicit lines, increase figure height, simplify redundant
decoration, or move source notes to the HTML caption. Do not hide overflow or make the
essential type progressively smaller. A tiny label remains tiny in a high-resolution PDF.

Place dots/markers before labels and reserve their occupied boxes. Candidate label
positions may use estimated text width, but acceptance uses the browser's actual glyph
bounds transformed into root coordinates. Check canvas containment and real collisions.
Then view the rendered PDF: bounds alone cannot assess hierarchy or reading order.

## Figure identity and explanation

Keep stable figure IDs for build references. Assign reader-facing numbers in appearance
order after assembling the book, and reuse the generated mapping in captions and links.
Do not let static numbering disagree with actual order. Avoid accidental duplicate emits.

A caption explains what is shown and the qualification needed to interpret it. Place the
figure with its discussion, keep its caption attached, and cite the source of decisive
data. Do not use a stock photo caption to claim observed wait times or crowd behavior.

## Acceptance

Inspect the full-size figure in the final PDF, including labels, legend, scale, units,
source note, contrast, and every branch's result. Compare it with its canonical rule
and the Sheet. Critical SVG text can contain the same claim tokens as HTML prose.
Text converted to outlines cannot be checked by text extraction; inspect it explicitly
and prefer real vector text for essential information.
