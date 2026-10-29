# Desk — Rome, Solved. (Affiche, Season II) — 2026-10-25

Owner: "applique marta II et brunner sur rome". The whole book recomposed in Marta Serra's hand
(`build-v2/compose-affiche.py` + `marta2.py` ← `models/m9-marta-II`, render `render-affiche.py`).
Rome's sign is the sampietrino (cover field, the 13′ core, the 90″ piazza).

**Brunner's standing fixes** (shared module `atelier/scripts/brunner_set.py`, the same as Barcelona's):
real quotes, glued paragraph ends (190), hyphenation limits. New on Rome: 15 compounds the shipped PDF
broke at line ends ("first- timer", "out- schedule") rejoined; Brunner's proof now catches that pattern.

**Brunner → Marta, and her answers**
- p20/p25 · empty pages: the ledger and the forks in one margin float outgrew the sheet and pushed the
  whole text over. *Marta:* the stack keeps the margin; the forks run under the prose in two columns.
- decision text pages · holes beside the short margin. *Marta:* the margin ends with the ledger; the prose
  runs on (`data-air` on the aside). Long decisions without a figure (d05, d07) take Brunner's tail2.
- p75 · hole beside the day-trips lede. *Marta:* the chapter's second photograph fills that margin.
- p2 · the contents' bullets read as a stopped column → Brunner's proof fixed (a label column is not text).
- The wallet card: *Marta:* the card is the page — the closing photograph removed.

**Engine (found and fixed):** every decision poster split onto a blank sheet — its bottom-anchored foot
let Paged.js pour the paragraph onto a new page; feet now anchored from the top. The 90″ poster used ○ ●
(not in Archivo → Type3 Lucida): drawn as shapes. Figure labels' stroked halo embedded as Type3: replaced
by paper chips drawn after pagination. Bare provenance marks wrapped in the Symbols face.

**Result:** 93 pages (Édition: 70), six release gates green, Brunner 0 faults, 17 named TrueType faces,
no Type3. Sale file: `Rome-Solved-affiche-II-locked.pdf`, 9.7 MB (images 1300px). Desk empty → the Eye.

## 2026-10-25, second pass — the owner's eye on the photographs

**Owner:** p4 and p7 cropped into bands (the horse's head cut); p12, p16, p68 add nothing; pages 4–12 leave an empty strip on the right (p10).

**Marta:**
- No photograph is cropped any more. A secondary photograph keeps its own proportions: a portrait stands whole in the 264px margin, a landscape is a 290px plate with its caption beside it.
- Essays: the right margin now carries the chapter's photographs, whole, then *The calls this chapter decides*: the decisions the text sends the reader to (01·02·03·04·08 for The ground). This fills the strip on p4–p12.
- Left out: the lane (p12), the train (p16), Navona (p68). Also left out, from the same family: d01's second cobbled lane, the uncaptioned hotel room, the day-trips vineyard (replaced in the margin by the Decision 09 cross-reference).

**Brunner:**
- The margin only holds what stands beside the text. In an essay with a figure, anything taller than the prose before that figure would push the figure onto a page alone, so it is left out instead (Castel Sant'Angelo in The plan; the photographs of Failure modes and What this book won't tell you).
- No photograph is ever set alone on a page.

**Result:** 87 pp (93 before). Six gates green; Brunner 0 faults; no Type3; 29 bookmarks. Sale file 7.85 MB locked (`build-v2/shrink-pdf.py src out 1300 70`, then `lock-pdf.py`).
