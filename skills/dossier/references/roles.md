# references/roles.md — the layout intelligence layer

**Read before Stage C (you write INTO these roles) and before Stage F (you render them).**
`layout-architect.md` is the judgment — how a designer thinks about a page.
This file is the **mechanism**: the fixed set of block roles, their visual weights,
and the gate that proves the reader can tell them apart.

## The failure this exists to prevent

A dossier can pass `audit-book` (pages full, no orphans, good rhythm) and still read
as a wall of undifferentiated text. The build gates measure **fill**; they do not
measure **legibility as structure**.

The symptom, in the user's words: *"the content feels disorganized — the skill lacks
a layout intelligence layer."* The cause, every time, is the same: markdown goes to
generic HTML, the paginator flows it, feathering tidies the tails, and **nothing ever
decides what a given block should LOOK like**. Everything comes out the same texture:
eyebrow, title, prose, table, figure, repeat.

The fix is not prettier CSS. It is a **classifier**: before rendering, every block is
assigned a ROLE, and each role has a fixed visual weight that never varies across the
book. The reader must be able to tell, **at a glance and without reading**, whether
they are looking at an argument, an instrument, or a verdict.

## The roles

| ROLE | WEIGHT | TEXTURE | WHAT IT IS |
|---|---|---|---|
| `opener` | heaviest | numbered title block, rule under | a chapter begins — an event, not a heading |
| `ledger` | heavy | tinted panel, ruled top | the scored table: an **instrument**, not an afterthought |
| `verdict` | heavy | barred panel, display type | THE CALL — what the reader paid for |
| `forks` | medium | symmetric two-up grid | for/against, visually parallel |
| `figure` | medium | breaks the column, numbered caption | the evidence anchor |
| `reasoning` | light | body measure | the argument |
| `reference` | dense | tabular grid | Field Sheet, sources register |
| `divider` | full page | part opener + its contents list | where you are in the book |

Two rules that are not negotiable:

1. **The verdict must outweigh the prose around it.** A decision manual whose verdicts
   look like body paragraphs has hidden the product. If `THE CALL` reads as just
   another label, the layer has failed.
2. **The ledger must look like an instrument.** It is the artifact that lets a reader
   disagree with you and still use the book. A plain bordered table reads as an
   appendix.

## Reference CSS (adapt the palette per site, keep the weights)

```css
/* opener — a chapter begins */
.opener{ break-inside:avoid; break-after:avoid; overflow:hidden; }
.opener .onum{ font-family:var(--display); font-size:58px; line-height:.78;
  color:var(--panel-edge); float:right; margin:-4px 0 0 16px; font-weight:600; }
.opener .okind{ font-family:var(--mono); font-size:8px; letter-spacing:.30em;
  text-transform:uppercase; color:var(--brass); margin:0 0 8px; }
.opener h1{ font-family:var(--display); font-size:31px; line-height:1.06; margin:0; }
.opener .orule{ height:2px; background:var(--brass); margin:13px 0 0; }

/* ledger — the instrument */
.ledger{ break-inside:avoid; break-before:avoid; background:var(--panel);
  border-top:2.5px solid var(--accent); }
.ledger .lcap{ font-family:var(--mono); font-size:8px; letter-spacing:.22em;
  text-transform:uppercase; color:var(--accent); padding:9px 14px 0; }
.ledger th{ font-family:var(--mono); font-size:8px; letter-spacing:.13em;
  text-transform:uppercase; color:var(--muted); text-align:left; }
.ledger td{ vertical-align:top; padding:9px 14px; line-height:1.46; }

/* verdict — the payoff */
.verdict{ break-inside:avoid; break-before:avoid; padding-left:15px;
  border-left:3px solid var(--brass); }
.verdict .vlab{ font-family:var(--mono); font-size:8.5px; letter-spacing:.24em;
  text-transform:uppercase; color:var(--brass); }
.verdict p{ font-family:var(--display); font-size:13.4px; line-height:1.52;
  text-align:left; }

/* forks — symmetric, labelled by MEANING not by keyword */
.forks{ display:flex; gap:18px; break-inside:avoid; break-before:avoid; }
.fork{ flex:1; border-top:1px solid var(--line); padding-top:8px; }
.fork.f b{ color:var(--accent); }   /* "When the other call is right" */
.fork.a b{ color:var(--brass); }    /* "When ours is wrong"           */
```

Label the forks by what they mean to the reader, not `for` / `against`. *"When the
other call is right"* and *"When ours is wrong"* tell them why the block exists.

## Position furniture

The reader should never wonder where they are. Emit a per-chapter position string and
print it in the footer: `DECISION 03 OF 08`. Use the same `string-set` mechanism as
the running head.

```html
<span class="rh-src">The chapter title</span>
<span class="pos-src">Decision 03 of 08</span>
```

```css
@bottom-left{ content:string(pos, last) }
```

`last` is the right choice, not `first` or `start`: with the opener pack (below),
most chapters open at the top of a page, and `last` names the chapter the page
belongs to. `start` reads the value from *before* the page and mislabels every page
that opens a chapter.

## The classifier

Assign roles from the manuscript's own shape, never from hand-tagging:

- a heading matching `^\d+ · [A-Z ]+ — .+` → `opener` with a decision number
- a block starting `|` inside a decision → `ledger` (caption from the `**cols:**` line)
- a block starting `**The call.**` → `verdict`
- blocks starting `**for**` / `**against**` → collect into one `forks` grid
- `**Bold heading**` followed by `- ` lines → sub-head + bullets, never one run-on
  paragraph
- everything else → `reasoning`

**Key figures to chapters, never by substring.** Matching a chapter title with `in`
put the food photo under a decision whose title merely contained the city's name.
Use exact keys or the chapter id.

## The gate

`scripts/audit-layout.py <build-dir>` — run it alongside `audit-book` at Stage G.

1. **role coverage** — every decision has an opener, a ledger and a verdict
2. **role distinction** — every role declares its own treatment
3. **texture run** — no run of pages with no structural anchor
4. **anchor density** — every spread carries at least one anchor
5. **stranded opener** — no chapter opens with almost none of its body (checked per
   chapter by its real `<h1>`, essays included, not just decisions)
6. **figure integrity** — no image used twice, no figure outside a chapter

A book that passes `audit-book` and fails this one is packed but unreadable as
structure. Both must be CLEAN.

## Honest limit

This layer does not catch **fragmentation artifacts** — see `build-traps.md`. Those
are visible on a rendered page and invisible to every gate we have. Rasterise a few
spreads and look at them before you ship. On this build the user found three real
defects in a row that all four gates had passed.
