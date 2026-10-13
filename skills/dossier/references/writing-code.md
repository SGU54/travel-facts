# THE WRITING CODE — how prose is set on the page

Read this before Stage C. The first build that ignored it put a provenance mark after every
sentence — up to 28 on one page, 11.6 per page on average — and the prose became unreadable
confetti. A dossier can have a beautiful cover and a strong thesis and still read like a
machine filled in a template. This is the code that stops that.

## Provenance marks: the 1-in-4 rule, and never mid-sentence

Marks (● ESTABLISHED / ◇ OFFICIAL / ▲ SURVEYED / ◆ VOLATILE) exist to tell the reader *this
specific claim is sourced, and how solid it is.* They are a SEASONING, not a garnish on
every bite. Marking every sentence is the same as marking nothing — the reader stops seeing
them, and the page turns to noise.

**The rules, hard:**

1. **At most ONE mark per paragraph**, and only on the paragraph's single load-bearing
   claim — the number, the date, the fact a decision turns on. Not on every sentence that
   happens to be true.
2. **A mark goes at the END of the sentence it certifies, never mid-sentence.** Never break
   a clause with a mark. `...arrive 30–60 minutes before departure. ◆ VOLATILE` — not
   `...arrive 30–60 minutes ◆ VOLATILE before departure`.
3. **Most paragraphs carry NO mark.** Analysis, reasoning, and connective prose are the
   author's synthesis — they aren't "sourced claims" and don't get marked. Only the hard
   facts underneath them do.
4. **Rough budget: one mark per ~4 sentences, and no page over ~6 marks.** If a page has
   more, you are marking prose that isn't a factual claim. Cut the marks, not the prose.
5. **The Field Sheet is where volatile figures live** — so ◆ VOLATILE should be RARE in the
   book body (it points the reader to the Field Sheet). A book body full of ◆ means volatile
   data is in the wrong document.

The test: read any paragraph aloud. If a mark interrupts the sentence or you hit more than
one, it's wrong. Marks should be nearly invisible until the reader wants to check a fact.

## The anatomy of a page — what goes where, in order

Every content page follows the same skeleton so the book reads as one designed object, not a
pile of blocks. Top to bottom:

```
  [running head]     — the chapter/part name ONLY. Set by the page furniture, never typed
                       into the body. It repeats; it is not content.
  H1 / H2            — the heading. One per section. Never orphaned at a page foot
                       (break-after:avoid — see layout.md).
  standfirst         — one italic sentence stating what this section decides. Optional on
                       sub-sections, required on chapter opens.
  body               — prose. Justified, drop-cap on the first paragraph of a chapter only.
  figure / table     — the arguing visual, UNDER the paragraph that introduces it.
  verdict            — the boxed call, where the section is a decision. Never split.
  [folio]            — page number + short title. Set by furniture, never typed into body.
```

**The running head and folio are FURNITURE, not text.** They are emitted once by the page
template and repeat automatically. NEVER write the chapter name or site name into the body
prose — that is what produced "GREECE, IN ORDER — DOSSIER" colliding with the last line. If
you see the running head or folio text inside a paragraph, the furniture and the content are
fighting; fix the template, don't type around it.

## Section headers: a fixed hierarchy, used consistently

- **Part divider** (I · THE GROUND) — the eyebrow line above a chapter H1. All caps, mono,
  muted. One per chapter.
- **H1** — the chapter/decision question. Display face. One per section.
- **H2** — a sub-section within a chapter (THE ACROPOLIS / THE PORT). Small caps or mono
  label, NOT the display face — H2 must be visibly subordinate to H1.
- **Never skip a level** (no H2 without an H1 above it) and never use a heading as emphasis
  mid-paragraph. A heading starts a section; it is not a bold phrase.

## Voice, briefly (the rest is in c-write.md)

Economist/Monocle register: calm, declarative, no hedging, no fluff. The synthesis is the
author's; state it plainly without marking it. The facts are the corpus's; mark the
load-bearing ones, once each, at the end of their sentence. That division — unmarked
synthesis, sparingly-marked fact — is what makes the page read like judgment rather than a
sourced database.
