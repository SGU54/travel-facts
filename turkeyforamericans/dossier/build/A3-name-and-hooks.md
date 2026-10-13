# Stage A3 — the name, the thesis, the hooks

Emitted after the cold mine, per the skill: the name reflects the corpus's actual
spine, not a planning-stage guess.

---

## Stage A2 — the shape

Category dominance across 102 articles: `getting-around` 13, then six named
regions (Istanbul 8, Cappadocia 7, Aegean 7, Mediterranean 6, Central Anatolia 3,
Eastern 3), with `itineraries` and `plan-your-trip` as categories of their own.

No single dominant hub, movement as its own subject → **country shape.** Rome's
scale thesis does not transfer; neither does a sprawl city's transit graph.

## The organising fact

Every dossier turns on one fact that reorganises the reader's mental model. This
one is not distance, not sequencing, and not season.

> **In Turkey, the number you need does not exist.**

Not hard to find. Not buried. **Not published anywhere**, in each of the five
decisions this book resolves:

| decision | the number a traveler looks for | what is actually there |
|---|---|---|
| Medical exposure | what a hospital visit costs | no published self-pay tariff for a foreigner — pricing sits in a Ministry framework |
| The internal moves | the minimum connection time at Istanbul | **neither Istanbul airport publishes one**, for any connection type |
| The licence chain | what you need to rent a car | nothing statutory — it is each company's contract |
| Taking things home | how old is too old to export | **no age threshold in the statute** — protection is a judgement |
| The cost of cash | what an ATM charges | no national figure; one major bank publishes, others do not |

Measured across the five reconciled fact panels: **28 of 129 facts came back
unpublished from both models**, and each swamp's *central* number is one of them.
That is a pattern, not a coincidence.

### The mistake the book exists to prevent

A first-timer looks for the number, finds something that *looks* like one, and
treats it as authoritative. The hundred-year rule. The ninety-minute connection.
"You need an IDP." A hospital price from a forum post.

Every one of those fills a vacuum where the real answer is a judgement — and
every one of them is repeated confidently by sources that never checked whether a
published figure exists. **The free corpus can only report components. Where the
number is absent, the decision has to be reasoned, and that is what is being
sold.**

---

## Name — three proposals

Following the shipped pattern (destination + promise of resolution), never a
single swamp's ranking in the title.

### 1. Turkey, Worked Out.  ← recommended

Two senses at once, both exact. *Worked out* as in figured out, and *worked out*
as in calculated. This is a book of visible arithmetic — fee stacks, connection
components, four disagreeing thresholds — performed precisely because the tables
don't exist. Plain English an American reader hears immediately, and it sits
naturally beside *Rome, Solved.* and *Thailand, Covered.*

### 2. Turkey, Reckoned.

*Reckon* carries both meanings the book needs — to calculate, and to judge — which
is the whole method. Slightly more literary; a shade archaic for some readers.

### 3. Turkey, Decided.

Cleanest match to the fleet rhythm and the clearest promise. Weakest on
distinctiveness: it could title any decision manual, and says nothing about why
this one had to be reasoned rather than looked up.

---

## Thesis line

> Turkey's highest-stakes decisions all share a property nobody mentions: the
> number you would look up does not exist. This book does the reasoning the
> lookup can't.

## Hooks — one per swamp

Raw. Accurate first, punchy second — the marketing skill strengthens these before
they ship. Keyed to the swamp ids in `article-list.json`.

**S-insure**
> A Turkish hospital will treat you before it bills you — and no published tariff
> anywhere tells you what the bill will be.

**S-transit**
> Neither Istanbul airport publishes a minimum connection time. Every figure you
> have seen was invented by someone.

**S-licence**
> Four parties decide whether you may drive in Turkey, they require four
> different things, and only three of them can be looked up.

**S-customs**
> The hundred-year rule everyone repeats is not in Turkish law — and the statute
> it isn't in carries five to twelve years.

**S-money2**
> One Turkish bank publishes its foreign-card ATM charge. It is a percentage, and
> it runs to twenty-five.

**S-calendar** — no hook. The mine demoted it (Gate A: zero cross-swamp joins, no
option structure). Its surfaces fall back to the thesis, which is the fail-open
behaviour the config expects.

---

## What happens with the confirmed name

1. It fills `SITE_CONFIG.guide.name`, with the thesis and hooks alongside it.
2. The admin **batch update** writes it into every `span.guide` inner text,
   replacing the gloss `complete Turkey trip guide` in one pass.
3. This build supplies the string. It does not perform the backfill.

### A gap worth knowing before the conversion layer goes live

There are **30 guide-spans, all in the 30 new articles.** The 72 originally
published articles carry **none** — they were written before the guide layer
existed, so nothing in them hands off to the product.

That is not a blocker for naming, and the Stage 5c surfaces (home band, category
band, article aside, end band) work independently of spans. But it means the
in-prose handoff currently reaches only the batch-16-to-21 drafts. If the paid
guide is going to sell from the whole corpus, a later pass should seed spans into
the highest-intent published articles — the ones the wet-map already marks as
swamp-adjacent — rather than leaving 72 articles with no route to it.

**Confirm a name and I'll emit the batch-update payload with it.**
