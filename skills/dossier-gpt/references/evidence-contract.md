# Evidence contract — version 1

Read this at Stage B, update it while writing, and audit it before release.

## Contents

- [Scope and limits](#scope-and-limits)
- [Build the register](#build-the-register)
- [Required structure](#required-structure)
- [Dates and uncertainty](#dates-and-uncertainty)
- [Decisions and arithmetic](#decisions-and-arithmetic)
- [Field Sheet and final text](#field-sheet-and-final-text)
- [Run the check](#run-the-check)

## Scope and limits

Maintain `BUILD_DIR/evidence.json` for the **small set of claims that determine an
action, a cost, an admission, a deadline, or a consequential comparison**. Do not
register every descriptive sentence. Include dependencies: a price used in a
comparison is consequential even when it appears only in a table or diagram.

This register records the editor's evidence. Its audit checks references, dates,
declared conflicts, arithmetic and required content. It does **not** browse URLs,
verify that a source says what is claimed, find undeclared contradictions, assess
whether an exception is sensible, or prove that the inventory is complete. Those
remain explicit editorial checks. Passing this audit is not release approval.

Use `assets/evidence-example.json` to understand the shape. It is a **SYNTHETIC
fixture** with an invalid example domain and fictional currency, not researched
content. Its formal checks can pass without its sources being real; that is also a
demonstration of the audit's limit. Replace its entire contents for a real project.

## Build the register

1. Start from the mined corpus and identify the source passage for each decisive
   claim. Reopen the underlying authority for current prices, taxes, legal rules
   and admission. A published article is a lead, not independent verification.
2. Record the exact source URL and the heading, table, paragraph or PDF page that
   supports the claim. Record when you actually checked it. Do not manufacture a
   checked date from a publication date or search snippet.
3. Separate **authority** from **volatility**. An official fare is both official
   and changeable; a confident tone does not make an access instruction stable.
4. State the scope: place, audience, ticket/category, dates and exclusions that
   change the answer. Record incompatible official statements as a conflict.
5. Attach decisions, changed conditions, alternative actions and calculations.
   Keep assumptions visible; do not turn an inference into a quote from a source.
6. Supply canonical text for each component that publishes the claim. Regenerate
   every occurrence, including summaries, charts, wallet cards and contingencies.

## Required structure

Use UTF-8 JSON, `schema_version: 1`, stable IDs beginning with a letter, and
`release_date` in `YYYY-MM-DD` form. Duplicate keys or IDs are errors. The top-level
fields are `schema_version`, `project`, `release_date`, `sources`, `claims`,
`decisions`, `calculations`, `field_sheet`, and `conflicts`. Empty `calculations`
and `conflicts` arrays are legitimate; omitting either is not.

### Sources

Each source has `id`, `kind`, `locator`, `scope`, `checked_at`, and either `url`
or an `artifact` for a retained observation. URLs must be HTTP(S), without embedded
credentials. Observation artifacts must be files inside the build directory; do
not point at transient files outside it.

| `kind` | What it supports |
|---|---|
| `primary` | The responsible authority's own rule, price, original data or official publication. Verify this designation yourself. |
| `secondary` | Reporting or analysis; identify the underlying authority where one exists. |
| `corpus` | The site's published passage that originated the claim; alone it cannot verify a current regulated price or access rule. |
| `observation` | Retained measurements or field observations; also record method and sample on the claim. |
| `publisher_policy` | The guide publisher's own refund, update or delivery policy. It cannot establish destination facts or regulations. |

A museum's own ticket page can be primary for its tickets. The guide publisher's
page can verify its own delivery promise. A domain suffix does not prove authority;
the audit accepts a declaration, while the editor must inspect its legitimacy.

### Claims

Each claim requires these fields:

| Field | Meaning |
|---|---|
| `id`, `text`, `scope` | Stable identifier, exact factual or analytical proposition, and where it applies. |
| `authority` | `official`, `reported`, `observed`, `inference`, or `judgment`. |
| `volatility` | `stable` or `changeable`, independent of authority. |
| `topic` | `fare`, `tax`, `legal`, `admission`, `schedule`, `geography`, `publisher_policy`, or `other`. Use `fare`/`tax` for actual monetary rates; use `admission` for ticket-validity rules. |
| `status` | `verified`, `qualified`, or `unresolved`. Here verified means the editor checked the stated proposition, not that software proved it. |
| `sources` | Nonempty array of source IDs. Critical fares, taxes, legal and admission claims require a primary source. |
| `as_of`, `recheck_by` | Date the editor checked this claim, and latest date to check it again. |
| `critical` | Explicit boolean. Claims used by decisions, calculations or the Field Sheet must be `true`. |
| `display` | Object containing `book` and/or `sheet`, each a nonempty canonical **string**. A snippet can repeat throughout its component. |

Add `valid_from` and/or `valid_until` when the published claim has known validity
bounds. Add `value: {"amount": "3.25", "unit": "EUR/journey"}` for a numerical
input or output; an actual value is mandatory for critical fares and taxes. Store
amounts as finite decimal strings, never floats, formulas or `"check current"`.

For `inference` or `judgment`, add a nonempty `assumptions` array. For `observed`,
add `survey: {method, sample, observed_from, observed_until}` and an observation
source. Describe the actual method and sample in text. Reading several articles is
synthesis, not a field survey. An external survey may instead be a reported claim
with the original study as its source; explain its limitations in the prose.

For a calculated headline, add `calculation_id` and `value`, with
`authority: "inference"`. The checker ties that claim's amount and units to the
calculation; final text then uses the same claim binding as any other snippet.

## Dates and uncertainty

All dates use the declared release date, so audits remain reproducible. Source
`checked_at`, claim `as_of`, survey dates, Sheet `checked_at` and conflict
`resolved_at` cannot be later than release. A claim cannot precede the checks of
its cited sources; the Sheet check cannot precede the checks of its listed claims.

Critical claims must apply on release, must not have passed `valid_until` or
`recheck_by`, and must have been checked within these maximum intervals:

- **Changeable: 90 days.** Use days or weeks where the access or booking risk
  requires it. Quarterly maintenance is a ceiling, not evidence that nothing
  changes between updates.
- **Stable: 730 days.** This is a review ceiling, not a promise of two-year truth.

The same ceiling applies to cited source checks and the distance between `as_of`
and `recheck_by`. Old publication dates are acceptable; old unreviewed evidence
cannot become fresh merely by assigning a far-future deadline. Validity end dates
are inclusive. Future announced changes should be worded as announcements and
scoped accordingly, not entered as a current rule that has already taken effect.

`unresolved` blocks publication. To use `qualified`, provide a short
`qualification` string and retain it verbatim in **every** canonical snippet for
that claim. Keep an honest usable instruction and any necessary value; a caveat
must not hide an unknown price. Recheck, withdraw the assertion, or use a clearly
scoped prudent alternative when the facts do not support the original action.

Each declared conflict has `id`, `claim_ids`, at least two `source_ids`, and
`status: "resolved" | "unresolved"`. A resolved conflict also needs `resolution`
and `resolved_at`. Resolution can mean removing a claim or publishing an explicit
safe qualification; it need not mean pretending to know which conflicting page
matches the real world. The editor must confirm that the revised action no longer
depends on the disputed assertion. Do not delete a conflict merely to pass.

## Decisions and arithmetic

Each decision has `id`, `question`, `when`, `action`, `claim_ids`, and at least one
`exceptions` entry with `condition`, alternative `action`, and `claim_ids`. A rule
with no meaningful alternative belongs in a checklist, not in this decision list.
The audit rejects verbatim repetitions of the default as an exception; assessing
whether the changed fact genuinely reverses the advice remains an editorial read.

Declare each numerical comparison as `comparison: {basis, options}`, with at
least two `{label, calculation_id}` options. The `basis` identifies the same
traveller, time span, geography, coverage, inclusions and exclusions for both
options. Do not call budgeting a compulsory cost a saving. Qualitative judgments
do not need invented numbers or a `comparison` block.

Each calculation has `id`, `operation: "sum" | "difference"`, `inputs`, and
`result: {amount, unit}`. Each input is
`{claim_id, quantity: {amount, unit}}`. Multiply the claim value by the scenario
quantity, then add terms, or subtract the second term from the first. `difference`
requires exactly two inputs. Inputs must refer to source-value claims, not other
calculations; keep the arithmetic transparent rather than nesting expressions.

Use explicit dimensions: `EUR/person/night × person*night` gives `EUR`.
`EUR/person` and `EUR/vehicle` cannot be added, nor can euros and dollars or minutes
and hours. Convert deliberately in a documented input first. Unit `1` is
dimensionless. Identifiers are case-sensitive; use the same vocabulary throughout.
Different routes, door-to-door boundaries or party sizes are also substantive
incompatibilities even when the unit strings agree; the editor must inspect them.

The check uses `Decimal` and no `eval`. Results must match exactly. If rounding is
needed, declare `round_to: "0.01"` (a positive power of ten); the rule is
`ROUND_HALF_UP`. Do not round inputs silently. All calculation inputs must be
included in the relevant decision's `claim_ids`.

## Field Sheet and final text

`field_sheet` requires `checked_at` and nonempty `claim_ids`. Include every
critical changeable claim, including access conditions and entry-system status,
not just prices. Each listed claim needs a `display.sheet` snippet. Numerical
changeable claims must show their declared amount there in plain decimal notation
(dot or comma, no thousands grouping). Provide applicability, units and caveats in
the snippet. A source link supplements the figure; it does not replace it.

Use `display.book` for the durable reasoning and `display.sheet` for current
values and conditions. Generate snippets from the register and keep the claim ID
through the final-content binding used by the release workflow. Do not assume a
new footer or appendix corrects a contradictory chart, summary or carry card.
When values change the recommended action, update the Book's call too.

The register check does not inspect HTML or PDFs. The release workflow must check
that the final Book and Sheet contain the registered snippets and that unbound
high-impact repetitions were reviewed. Do not treat a manifest alone as proof
that the delivered artifacts match it.

## Run the check

```bash
python3 scripts/audit-evidence.py BUILD_DIR
python3 scripts/audit-evidence.py BUILD_DIR --json
python3 -B scripts/test-evidence.py
```

The CLI returns **0 / PASS** for successful registry checks, **1 / FAIL** for
validation failures, and **2 / BLOCKED** for absent, unreadable, malformed or
unsupported-version input. JSON output contains `gate`, `status`, `errors`,
`checked` counts, and an explicit limit statement when the registry was evaluated.
Use the exit status, not a substring search for PASS. Correct the evidence and
content that failed; never weaken a gate to obtain a release label.
