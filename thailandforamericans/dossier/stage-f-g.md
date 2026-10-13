# Stages F and G — the plates, the render, and the five gates

**`Thailand-Covered-2026.09.pdf` — 45 pages, US Letter, 4.2 MB, self-contained.**
All five release gates pass. The old edition was 23 pages and failed all three
depth signals.

```
PASS  furniture   41→45 sheets, every one painted to trim, furnished, body in column
PASS  book        no orphan stubs · longest text-only run 5pp · 2.2 marks/page · cover 96.7%
PASS  layout      8 chapters, 8 decisions, roles: divider/figure/ledger/opener/verdict
PASS  ai-smell    7,063 words of prose · em-dash 4.2/1k · rhythm CV 0.62
PASS  depth       0.46 pp/article · 121 w/article · 14.1% of corpus used
```

## The plates

Ten, chosen by the user from a published contact-sheet artifact (two candidates
per slot, each carrying the argument it had to prove). First plate at p4 of 45 —
inside the opening 12%. Five in each half. Never more than three pages without one.

**Three picks did not survive the caption-truth check, and that check is the
reason to do it at all:**

| slot | what it turned out to be | what replaced it |
|---|---|---|
| A10 | the banknote reads **BANK NEGARA MALAYSIA** — Malaysian ringgit | the other candidate on the same sheet: a Bangkok stall priced by hand in Thai |
| A05 | the departure board reads **"Welcome to Changi Airport Terminal 1"** — Singapore, in a chapter about the gap between Bangkok's two airports | Baggage Claim 4 at Suvarnabhumi, Udon Thani and Chiang Mai on the board — literally the second of the chapter's five steps |
| A08 (at the contact-sheet stage) | a shoe rack that is plainly **Japanese** | the slot became *the door itself*, and the brief was rewritten to say so |

**A defect in my own contact sheet, worth recording:** the picker showed Pexels
`fit=crop` thumbnails, so five natively-portrait frames appeared as 3:2. The user
picked on crops, not frames. Every crop was then re-derived and looked at.
**On A06 the edge-energy scan chose foliage and power lines over the village
street the slot exists to show** — blind trust in the scan would have shipped it.
Centre crop used there, energy crop on the other five.

## What the gates caught that reasoning had not

1. **`audit-layout.py` reported "0 decisions" and passed nothing.** It matches the
   skill's documented role vocabulary — `dec chap decision`, `.opener`, `.ledger`,
   `.verdict`, `.partdiv` — and this builder had invented `.decision-open` and
   `.call`. The gate checked the most important thing by checking nothing at all.
   The book now uses the contract names. *Same defect class as everything else on
   this project: a thing configured, nothing reading it, no error anywhere.*
2. **Tail-feeding moved three plates to the ends of their chapters.** That is right
   for a decorative plate and wrong for an anchored one — A05's caption says "the
   second of the five steps". `FEED_PLATES = False`, with the reason written down.
3. **The decisive-row marker overflowed its column** as an inline `nowrap` span and
   printed across the neighbouring cell. Now a block.
4. **em-dash 13.8/1k.** A real tic, not a false positive: 35 rewritten, down to
   4.2/1k. Direct corpus quotations kept their own punctuation.
5. **My own em-dash pass broke a sentence** — "rather than the medical line Then
   call" — which a rendered-page read caught. A scan for lowercase-word-into-capital
   across the whole manuscript found that one and no others.

## Depth: how the last 400 words were found

The first full build came in at 118 w/article against a 120 floor. The fix was
**the second mining pass, not padding**: `is-thailand-safe-for-tourists` and
`common-scams-thailand` (1,699w) had never been written, and they carry the book's
sharpest single fact — *road traffic accidents, especially motorbikes, are the
leading cause of injury and death for tourists*, while the scams "involve no
violence". The risk people prepare for is not the risk. That became the essay
**"The risk is not the one you packed for"**, and it points straight back at
Decision 01.

`scooter-rental-thailand-what-it-costs-you` (1,366w, the largest article in its
category) was also under-mined: the two-costs distinction — a 400–500 baht
checkpoint fine against a claim denied *in full* — went into Decision 01, and its
"whether you will ride is decided by where you sleep" insight into Decision 03.

Two part dividers were added at the same time. They are not filler: the book had
**no contents of any kind** before them, and each divider lists what its part holds.

## Still open

- The live "See inside" previews on thailandforamericans.com still show the old
  23-page edition. They need re-cutting from this PDF.
- Greece, Rome and Turkey have not been regenerated against the corrected skill.
- `audit-layout.py` reports "0 figures" although the book has five drawn ones; it
  counts `<img>`, not `<svg>`. Harmless here, wrong in general.

---

# Revision pass — the reader's five remarks (2026-09-19)

**`Thailand-Covered-2026.09.pdf` — 45 pages, 4.4 MB. All five gates still pass;
depth went UP (124 w/article, 14.4% of corpus) because two of the fixes were
writing rather than styling.**

### 1. The cover was type only

It named the thesis and proved nothing. It now carries **the device**: the same
seven places and the same four measurements as FIG. 3, drawn as filled / half /
empty marks, with an accent rule where the marks stop. No axis labels — `cover.md`
allows one device and nothing below 24px, and a legend would need 11px type. The
cover shows a pattern that breaks; the interior names what broke.

### 2. "Isthmus Press"

An invented imprint (after the Isthmus of Kra). Convention for these manuals, not
a requirement. **Open question for the user: keep, replace with "Thailand for
Americans", or drop.**

### 3. FRONT MATTER / ESSAY / BACK MATTER in the foot band

Correct objection: they told the reader nothing the page did not already say.
Removed. The foot-left now carries `DECISION 04 OF 08` on decisions and nothing
elsewhere. The folio became **`n / 45`**, which answers "how far through am I"
rather than just "which sheet is this" — and restores the ink the furniture gate
needs in that band (a bare "3" was too thin to register, and two pages failed).

### 4. The type started large and shrank

It did: `.lede` was 17px against a 15px body, which reads as the text shrinking
rather than as emphasis. **One body size now, 16px/24px throughout**, the opening
paragraph leading by position and weight instead. Forks 12→13px, captions 12→12.5px.

### 5. A dead band down the right, text pinned left

The prose was set to a 520px measure inside a 652px column. A narrow measure earns
its keep only when something lives in the band beside it, and nothing did — so
every page had two right edges. **One measure now, the full column**, for prose,
opener, verdict, standfirst, captions and dividers alike. Type up to 16px so the
longer line still reads.

### Two more gate blind spots, found while re-passing

- **`audit-layout.py` could not see a photographic plate as an anchor.** It looked
  for `FIG. n`, `THE CALL`, `PART x`, `DECISION n` and nothing else, so a page
  carrying a full-width plate and its caption read as bare prose. Both its figure
  patterns are now letterspace-tolerant (`P L . A`, `F I G . 1`) — the same trap
  `audit-book.py`'s FIGLABEL already handled, never ported across.
- **The feather pass only measured `section.dec`.** Essays never got the
  compositor's card, which is why the orphan pages that appeared after the
  furniture change were all essays. Now measures `.essay` too, and `.tight` /
  `.loose` apply to any section.

### What the orphan fixes actually were

Not spacing. Two of them were **redundant prose** (a note repeating PL. J's
caption two pages earlier) and one was **an under-written essay**: the money vein
holds 4,017 words and only the ATM article had been mined. Writing out the cash-vs-cards
and dollars-vs-withdrawals material filled the page honestly and took
words/article from 121 to 124.

---

# Second revision — the imprint, and FIG. 3

**`Thailand-Covered-2026.09.pdf` — 45 pages, 4.5 MB. Five gates still green.**

### The imprint

"Isthmus Press" is gone. The cover and the key page now read **"Thailand for
Americans · a decision manual"**. The cover foot, which used to repeat "Thailand
for Americans" under it, became `thailandforamericans.com · edition 2026.09`.
Two prose references to "this press" became "these manuals".

### FIG. 3 was losing its first two columns

Phuket and Koh Samui had no column heads on the printed page. Their dots were
correct; the labels were absent.

**They were in the markup and correct in the DOM.** Measured in the unpaginated
render, all seven labels were `visible`, right colour, right position. Rendered
standalone, the figure was perfect. So the loss happened during pagination — and
querying the paginated DOM found it:

```
{'Four unrelated measurement': 2}      ← two copies of the same <svg>
  copy 1: ['Phuket', 'Koh Samui']
  copy 2: ['Ao Nang / Krabi', 'Koh Lanta', 'Koh Phangan', 'Koh Tao', 'Koh Chang']
```

**Paged.js split the SVG across two pages.** `figure { break-inside: avoid }` did
not stop it, and neither did adding `break-inside`/`page-break-inside: avoid` to
the `<svg>` itself — Paged.js descends into SVG children and its avoid-handling
does not apply there. The first fragment sat on the previous sheet, off the
visible area, carrying the two shortest labels.

**The fix is structural, not CSS.** Every drawn figure now ships as
`<img src="data:image/svg+xml;base64,…">`. An image is an atomic replaced element
and cannot be split. Two consequences handled:

- **The font.** An image is an isolated document and cannot reach the page's
  webfont, so the figures would have set in a fallback grotesque. Archivo (a
  variable font on Google Fonts — one file covers 400 and 600) is downloaded to
  `build/fonts/` and embedded as a base64 `@font-face` inside each SVG.
- **The namespace.** Inline, the HTML parser implies the SVG namespace. Standalone
  it is strict XML and must declare `xmlns`, or the `<img>` silently fails to
  decode. First attempt rendered four broken images; the probe caught it by
  checking `complete && naturalWidth > 0` rather than counting tags.

Also fixed while there: the magenta divider ran 6px below the base rule and read
as a stray tick. It now stops on the rule.

**The lesson for the skill:** *inline SVG is not safe in a paginated book.* Wrap
every drawn figure as an atomic image with its font embedded, and verify with a
post-pagination probe that each figure appears exactly once and actually loaded.
Counting elements in the source proves nothing.

---

# Editorial review 2026.09 — all 15 items

**45 pages, 4.6 MB. Five gates green. Depth went UP: 130 w/article, 15.1% of corpus.**

| # | what changed |
|---|---|
| 1 | The book named "the corpus" as a source without ever saying what it is. It is **this site's own 97 articles** — the same desk, not an outside authority. Said plainly on the key page; the word "corpus" is now gone from the printed text entirely (0 occurrences), replaced by "the reporting". |
| 2 | Prose said the four measures were "air access, medical capability, booking structure and **weather exposure**"; FIG. 3 measures **ground transport**. Corrected, and "four unrelated measurements" → "four separately observed measures" — air access and booking structure are plainly related. |
| 3 | "you have chosen to carry the medical cost yourself" → "ride as though a motorbike claim would be refused, because outside your policy's licence condition it may be". |
| 4 | **Highest priority.** "call the assistance number before treatment, not after" now reads: *"In an emergency, get treated first: nothing on this page is a reason to delay care. Whenever circumstances allow … call the assistance line before the billing is arranged."* |
| 5 | "no rebooking, no compensation" → "the onward carrier owes you nothing for a connection missed because the inbound ticket failed … Plan as though the replacement ticket is yours to buy." |
| 6 | "your only filter" → "the first filter … Passing that test is necessary, not sufficient — the table names what else to read." |
| 7 | "breaks a young elephant's spirit" → "built on coercion and restraint" — the observable practice, not an inferred mental state. |
| 8 | "There is no second instrument to learn" → "The queue is the first inspection; the rest of this page is the second." |
| 9 | "not the cheap option" → "not **merely** the cheap option". |
| 10 | "single safest first choice" → "lowest-friction first choice". The chapter measures transit access, not safety. |
| 11 | "Every district below is **scored**" → "**compared**". |
| 12 | See below — the item that changed most. |
| 13 | Field Sheet: "Under 90 days is a fine and no ban" → "**On voluntary departure**, under 90 days is a fine and no ban; being caught is harsher." |
| 14 | The ATM fee schedule left the permanent body. The body keeps what is structural — the fee is **flat** (so frequency costs, not amount) and set **by network** — and the numbers live on the Field Sheet alone, where the method says they belong. |
| 15 | One stable ledger URL, `thailandforamericans.com/sources`, on the key page and in the back matter. A "bibliography" row was added to the refusals table explaining why there is no printed list of 97 URLs. |

## Item 12 — the review was right, and the fix went further than asked

The book claimed road crashes are "the leading cause of injury and death for
tourists in Thailand" and labelled that row THE ACTUAL NUMBER ONE.

The reporting states it verbatim three times — and **the reporting is this site's
own articles, which cite nothing for it.** Repeating a superlative is not
establishing one. That is exactly the circularity item 1 exposed, showing up as a
factual problem.

Replaced with what is attributable, and it is stronger:

- Traffic crashes are the **most common cause of non-natural death for American
  travellers abroad** — US State Department, ahead of homicide, terrorism and
  natural disaster.
- Among destinations Thailand **leads on fatal road crashes per visit**.
- The State Department's Thailand page names the vehicle: multiple US citizens
  die each year in crashes involving two- and three-wheeled vehicles.
- Roughly **three-quarters of Thai road deaths** are motorbike riders and passengers.

The decisive-row label went from "the actual number one" to "the one that is
measured". The note now says the road figures are the State Department's, are
dated, and that its current page is the source — not this one.

## The ledger exists

`thailandforamericans.com/sources` is live: 85 published articles in 27 sections,
generated from the articles table so it cannot drift from what is published. Each
row carries its publication date and, where `reviewed_at` is set, "Checked <date>".
Listed in the sitemap.

One trap on the first deploy, worth recording: the query selected `reviewed_at`,
which arrives with migration 0007. **PostgREST rejects the entire select when one
column is missing**, so the page rendered "Articles 0" — a traceability page
listing nothing. It now falls back to the columns that have always existed and
treats every check date as absent. Running 0007 only adds the Checked dates.

---

# Second review pass — six residuals

All six were leftovers from my own first pass, which is what a second read is for.

| # | what it was |
|---|---|
| 1 | p30 THE CALL still said "let it do the whole job", contradicting p28's "necessary, not sufficient". → "Apply the riding test first. If a venue passes it, read the table above for the rest." |
| 2 | **The Field Sheet still said "Call before treatment"** — the old wording surviving on the one page the reader carries. → "Emergency → get care first. Otherwise call before the billing is arranged…" |
| 3 | "Reporting the reporting supports strongly" — a duplication my corpus→reporting substitution produced. |
| 4 | p26 still said "scored", and the sentence carrying it was **factually wrong** — see below. |
| 5 | The street-food table still said "both the quality test and the safety test" after the prose had been qualified. → "the first quality and safety filter". |
| 6 | "Every ATM withdrawal on a foreign card carries a flat fee" → "Thai ATMs generally charge foreign cards a flat local withdrawal fee." |

## The one that was not a wording slip

I had written: *"A stored-value card for the BTS and MRT, bought at any station,
covers the network the districts below are scored on."*

**There is no such card.** The Rabbit Card runs the BTS (and the Pink and Yellow
lines); the MRT Blue Line takes its own card or tokens; there is no unified
ticket and no confirmed timeline for one. The source said "buy a stored-value
card or single-journey tickets at the stations" — I compressed two separate
networks into one card, and the reviewer was right to send it for external
checking.

It is now a fact the chapter was missing rather than a sentence it got wrong:
*"there is no single card for both networks. The BTS takes one and the MRT
another, so a day using both means carrying two or buying singles at the gate."*

## A pagination lesson from the same pass

Adding that paragraph pushed Decision 06 over a page and stranded its closing
note. The `.close` group — ledger/figure, note and end mark travelling together —
existed only on essays; decisions had the same defect and it had simply never
shown. Now both use it. The chapter was then tightened by a sentence, not by
shrinking type, and the book returned to 45 pages with all five gates green.
