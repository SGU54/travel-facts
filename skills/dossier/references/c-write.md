# Stage C — The prose

> **Follow `references/writing-code.md` for HOW prose sits on the page** — provenance-mark
> density (one per paragraph, never mid-sentence — the first cold build hit 28 marks on one
> page and became unreadable), the fixed page anatomy, and the header hierarchy. This file is
> the voice and content; that file is the typographic code.

# Stage C (voice) —  Write

## Register

Economist/Monocle, not travel blog. Calm, confident, no fluff, no enthusiasm, no emoji.
The reader is an intelligent adult spending thousands on a trip. **Show the reasoning; let
them disagree.**

The test an outside reviewer applied to Rome and it passed: *"Most Rome guides answer 'where
should I eat?' This answers 'how should I think?'"*

## The chapter set that works

```
OPENING          the contract: "so you can disagree with us and still come out ahead"
HOW TO READ      the marks + the two documents + "using this on the trip"
CONTENTS         a TOC. A $39 product without one is a PDF, not a publication.
THE GROUND       the ORGANISING FACT — the one thing that reorganises the trip.
                 Rome's is scale; a country's is sequencing. See a2-shape.md.
                 + the transit-reality page (why the obvious tool doesn't help)
BEFORE YOU FLY   the checklist, every line with a deadline
DAY ZERO         the arrival day — the most anxious hours, and nobody writes it
TIMING           the rhythm of the week (closures, strikes, the seasonal trap)
THE SET PIECES   the destination's 2-3 unavoidable operations, each with its order-of-ops
EATING           the rule that outlives any list of names
MONEY            where it actually leaks
THE DECISIONS    13 × 1pp — the heart
THE HORIZONS     the booking calendar (stable horizons; prices live on the Sheet)
WHERE TO STAY    6 assessments on identical criteria + a decision tree
THE PLAN         the days, as operations not itineraries
THE FOURTH DAY   day trips, verdict up front
FAILURE MODES    20, organised BY CONSEQUENCE — the thing a website of articles can't do
KIT              the wallet card (print it, carry it)
BACK MATTER      "What this won't tell you" — the brand
CLOSING          about the destination, never about your methodology
FIELD SHEET      the dated annex
```

## Prose craft

- **Drop cap** opens a chapter. Never a verdict, never mid-page.
- **Standfirst** is the argument in one sentence, italic, above a hairline rule.
- **Pull quote** must not repeat body text on the same page (Rome shipped that bug).
- **Three wonder paragraphs, no more.** Rome's: the Pantheon threshold, the first espresso
  standing at the bar, the bridge at dusk. Anticipation is part of what's being sold — but
  four is a travel blog.

## The words that expose the machine

Count them. Rome's first draft: *actually* 20×, *whole* 13×, *structural* 10×, *honest* 10×,
*genuinely* 9×. **"Honest" was the worst** — the book kept *saying* it was honest instead of
being it.

```python
import re
full = ' '.join(p.extract_text() for p in PdfReader(pdf).pages).lower()
for w in ['actually','whole','structural','genuinely','honest','exactly','simply','precisely']:
    print(f"{len(re.findall(r'\\b'+w+r'\\b', full)):3}×  {w}")
```

Target ≤ 5 each in a 14k-word book. Every fix is a **judged rewrite**, not a deletion.

## The Field Sheet

- Only **real verified values** under "Verified at press time · <month>".
- Everything unverified becomes **"Confirm in your travel week ◆ — where to look"** with the
  official source named. Never a blank cell, never "— verify".
- **Never promise a page count.** Rome promised six pages and shipped two — for a product
  whose premise is honesty, that discredits every other claim in the book.
- State the survey method once, plainly, and mark it `▲ SURVEYED`.

### Locating a value is not supplying it

The split exists so the durable reasoning is not held hostage to a price. It does
**not** license moving the decisive input out of both documents. All three books
did exactly that:

- Greece p3 promises the Sheet "tells you what it costs this Tuesday". Decision 03
  recommends when a fast-ferry premium is worthwhile, prints **no fare
  difference and no value-of-time threshold**, and p42 sends the buyer to "the
  operators' own sites" without naming an operator.
- Rome p14 says the current pass figures are on the Sheet; p47 says "confirm
  before buying". There is no room-rate comparison, though p12 says rates by area
  and season live there.
- Turkey p33 says bank tariffs are on the Sheet; p51 supplies "the bank's own
  tariff page" and no bank. Its four fee layers never become a worked total.

**Rules:**
1. **Every decision-changing variable gets its own Sheet row**, with a source
   locator, a check date, and *which decision it can reverse*.
2. **A dated worked example belongs in the Book**, beside the reusable
   calculation. A number the reader can redo is durable even when the number is
   not; forbidding arithmetic was never the point of forbidding prices.
3. **Validate every Book→Sheet promise.** If the Book says "it's on the Sheet",
   the row exists or the build fails.
4. **The Sheet carries an explicit issue date.** "Raised 2026" inside one row is
   not a date for the document.
5. **Check at COMMITMENT, not only in travel week.** A booking made six months
   out cannot be repaired by a Tuesday price.
6. **If no defensible value exists, bound the recommendation and say what remains
   undecided.** Do not advertise a missing input as delivered.

### The carry object has a physical size or it is not one

Rome p44 says "The whole book, compressed to what fits in a pocket. Print it;
carry it." The card is the **full 6.79in body width**, with answer text already at
~7.9pt. Scaled to a 3.25in pocket width that type becomes **~3.8pt**. Turkey p47
labels a full-column list "The card to print, or photograph, and carry" and gives
no boundary, cut size or fold at all. A short list of words is not a format.

Specify a **pocket reference**: two adjacent **3.25in × 4.5in panels**, 6.5in
total, inside the existing 6.79in body. Cut around the pair, fold between them;
folded it is 3.25in × 4.5in. Print the final size next to the instruction, and say
**print at 100%**. Type **≥12px/15px**. Build it as one unfragmented fixed-layout
table, two 3.25in cells, `box-sizing:border-box`, 12px inner padding, an outer cut
rule and a dashed centre fold rule. **Reject overflow — never `overflow:hidden`.**
If the content will not fit at the minimum size, cut words or add a second,
separately labelled card. Do not call it wallet-sized unless a wallet format has
actually been tested.


## The refusals page — reframed by the model

"What this book won't tell you" is NOT the book's identity — it is a CONSEQUENCE of the
model in `references/model.md`. The book sells reality (the connections, the real model behind the naive one). One
person's dinner recommendation is not reality — it is a data point that rots in a season and
that the reader can get free anywhere. So the refusal is not "we're too pure to name a
restaurant"; it is **"we refuse to fake reality, and a single restaurant pick is fake
certainty."**

Frame every refusal as protecting the buyer from false confidence:
- not "we won't name restaurants" → "a named restaurant is a guess with a byline; what
  outlasts it is the RULE for spotting the right one, which we do give you."
- not "we won't list hotels" → "a hotel pick is stale in a season; the DECISION of which
  area, and why, is what we make — and it doesn't expire."

The refusals page should leave the reader MORE confident they bought the durable thing, not
feeling something was withheld. It is the model stated as a boundary.