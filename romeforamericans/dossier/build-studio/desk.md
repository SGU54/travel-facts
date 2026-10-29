
## 2026-10-26 — Rome by the studio of three (owner: "maintenant refaisons rome"), in `build-studio/`

- Brunner (`studio.py` from Barcelona, + Rome labels; `brunner_set.us_house` extended: St. Peter's, "with", AD 126, judgment/math/…): 394 → 95 faults, 0 blockers. Fixed on the way: the shipped edition's "Failure modes, p. ○" (now a link numbered at render); a figure label read back as a stray line ("wrong carbonara."); Title Case transcribed from capitals ("Costs You The Trip, Or A Whole Day"); a poster foot that repeated its thesis or a paragraph (fidelity TWICE → 0).
- Marta (`marta_pics.py` from her ledger): 33 frames out (incl. the p5 Forum panorama, the twice loser), the Forum moves to Decision 04's closing with the ½ in the sky, OSTIA above the arcades, the rooftops and St. Peter's whole on the 340 column with the caption beside; closings without a true picture typographic (decisions: verdict on ink; essays: their name on red).
- Writer (`rome_writer.py` ← `_studio/writer/`): Ruth's 3 blockers and 8 majors answered in 41 sourced edits; the Field Sheet rebuilt (27 rows, as of October 2026, label → value, on one sheet); B3: what closes (Vatican Sundays and holidays, Ostia and Borghese Mondays, Colosseum winter hours) and what a strike means; plans say "never a Sunday", "Ostia (closed Mondays)".
- Joins: "What the free guides never connect" on each decision's closing page (9; 21 article URLs; weak: D07, D05, D09).
- Gates: rhythm gate reads `_fullsheet.json` (as Barcelona). 86 pages, six gates green, fidelity 0 twice.
- Waiting: Marta's Unsplash refill; then Ruth's recheck.
- Unsplash refill: Marta chose 7 of 24 slots; 6 printed (the Pantheon fountain's dated inscription p8, Line A at Barberini p15 with its ceiling ad cropped away, Bernini's Pluto and Proserpina under the 3 p38, the Momo stair p69, Orvieto's portal p72; Spanish Steps dropped: its closing carried 116 characters, so it has no page; the sampietrini margin had no margin). Tool rules added: a mark wholly outside the printed window is cropped away (`mark_box`); "illegible" lettering is not legible text in a corner.
- Ruth recheck v5 → v6: N1 taxi zone (Delib. G.C. 157: the Vatican, Borgo and Prati up to Viale delle Milizie inside the €55 zone), N3 Pantheon booking optional (caption, Fig. 7, poster), M1 Fig. 5 €31–41, M3 Fig. 7 redrawn in days (Colosseum 30, Arena ≈7, Pantheon none), M18 Fig. 9 Pompeii 12 h, N4 D09 join dropped (`figfix.py`). Verdict v6: SHIP AFTER FIXES, owner-only (M15 listing says 64 pages; M17 p4 statement).
- Final: 86 pages, six gates green, fidelity 0 twice, Field Sheet one sheet, Brunner 87 (0 blockers), Marta 0 KILL; shipped PDF shrunk to 4.8 MB (`shrink-pdf.py dossier.pdf out 1600 82`). Package `../atelier-studio-2026-10-26/`. Not published.
- Owner: "page 4 et 7 sont un peu vides" → `margins.py`: p4's closing field (it carried only the last paragraph) goes, the paragraph joins the prose, the margin carries two of the chapter's sentences; p7's margin carries the key to the four marks and where the sources are. 85→86 pages after the Sources page.
- Owner pasted a ChatGPT audit (`_studio/external/chatgpt-audit-2026-10-26.md`); Ruth triaged it (`_studio/ruth/chatgpt-triage.md`): X1 Tap & Go (each traveler their own card, same one all day, €8.50 cap for 24 h from the first tap) and X2 sources (a "Sources, checked October 2026" page, 29 entries, two columns, one page) accepted as majors; X3–X8 minors (coperto law cited inline, US passport rule labelled, €5 per passenger beyond four, St. Peter's booking described once, the wallet card points to the Sheet, walk-times from/to stated). Rejected: softening the coperto ban (L.R. Lazio 22/2019 art. 75 c.4 re-read on the Region's PDF) and editorial "variants" already present. All answered (57 writer edits).
- Final: 86 pages, six gates green, fidelity 0 twice, Field Sheet one sheet, Brunner 90 (0 blockers), Marta 0 KILL; shipped PDF 4.9 MB. Owner items: p4 statement (M17), listing page count (M15), the site's own Termini article says 20–25 min where the book measures 28′ (n8).

## 2026-10-28 — Hannah's rights pass and Ruth's M17 (studio cards 35 and 38, approved by the owner)

- **Hannah:** the 11 printed frames now each carry author, original page, licence and date read (`_studio/marta/pictures.json`, `_studio/marta/credits.json`).
  - Found by perceptual hash on the volume's batch folders and re-read on their pages: rooftops = Pexels 32114353 (Ensar), St. Peter's Square = Pexels 12044711 (SlimMars 13), Ostia = Pexels 36577336 (Soo Chul Park). The five Unsplash frames re-found on unsplash.com and confirmed (not Unsplash+): Leonardo Evaristo, Marco Chilese, tommao wang, Nicolas Hoizey, Sterling Lanier.
  - Three inherited frames had no recoverable source and were replaced, same subject and 3:2: the Forum from the Palatine → Pexels 36635790 (Ludovic Delot; the ½ still sits in clear sky right of the Vittoriano, p30); the Pantheon interior → Pexels 35128649 (Oswald; the dome and its oculus, as the caption says, p64); the Portico of Octavia → Wikimedia Commons, Jorge Franganillo, CC BY 2.0 (p61).
  - Credits: a "Photographs" paragraph on the Sources page (p86), the full URL only for the CC BY frame; the book stays 86 pages.
- **Ruth M17 (writer edit `M17`):** p4 now says what the book sells beyond the free site ("…the site this book comes from gives them away. What it never does is make the links. This book is the decision manual that joins the free guides into calls you can act on, and the Field Sheet keeps the figures that move current.").
- Gates: six release gates green (`_studio/release-2026-10-28.txt`); fidelity 0 printed twice (the 28 "lost" are the Field Sheet rows lifted out by fssplit); 11 of 11 printed frames licensed.
- Shipped: `../atelier-release-2026-10-28/` (locked, 4.8 MB); bucket `guides/Rome/rome-solved.pdf` replaced and read back identical; Etsy listing 4601367120 file replaced; site previews (p16, p58, p76) unchanged. Field Sheet unchanged.

## 2026-10-28 (evening): Ruth's 23 open minors (owner: "vas y avec les remarques")

- Already closed earlier today: m30 (Hannah's rights pass, 11 of 11 frames sourced) and n8 (the site's Termini articles now say 30–35 min). n9, n11 and n12 were already answered in `figfix.py`.
- Answered now in `figfix.py` (block "Ruth recheck v6, the 18 open minors"), plus `compose-affiche.py` for the card:
  - m2: the cover says "within a kilometer and a half of its center".
  - m3: nine choices and nine calls, on p4 and p81.
  - m6: Fig. 1 prints "Termini".
  - m7: Fig. 2/4 say "no line crosses it", and the captions name Line C at the Colosseum.
  - m8: the Fig. 10 caption: Termini, twice as far as the core.
  - m9: "half a day somewhere real than a whole day reaching somewhere famous".
  - m14: the tier reads "Costs you a meal, a fine, or marks you as a tourist".
  - m16: 8:30 a.m. and 8:30 p.m. in Figs 6, 8 and 13.
  - m17: the ZTL is defined (a limited-traffic zone whose cameras fine unauthorized cars, rentals included).
  - m23: Borghese: every ticket booked; the official site says leftover last-minute tickets are never sold on free Sundays.
  - n10: on the poster, the third sight is the Underground (tier, foot and card agree). The tier no longer says "A day or two … pantheon": the v5 fix missed the lower case. The axis reads 30 DAYS AHEAD → THE DAY YOU VISIT. The peak Standard is booked "the day the 30-day sale opens".
  - n6: p37 and p48 promise only what the Sheet holds.
  - n2: the cut card carries all 12 rows, whole (7.2/8.6 px, short labels).
- n5: the strike bands now cite ATAC (`sources.json`; ATAC notice: guaranteed until 8:29 and 17:00–19:59).
- m27: the site hooks say three sights, not four (romeforamericans `58ef10a`).
- `figfix` text rules now see through the typesetter's no-break spaces (m9 and m14 were hiding behind them).
- Left open, by design:
  - m1: the first call is on p16; moving it would mean restructuring the book.
  - m13: the reprised figures in the operations section (Figs 2/4, 6/12, 8/13).
  - m26: phone reading; the owner set the phone editions aside.
- Gates: 86 pages, page fills identical to the 28/10 morning render, six release gates green (`_studio/release-2026-10-28b.txt`).
- Shipped:
  - `../atelier-release-2026-10-28b/` (locked, 4.8 MB);
  - bucket `guides/Rome/rome-solved.pdf` replaced and read back identical;
  - Etsy 4601367120 file replaced;
  - site preview p58 re-cut (romeforamericans `53d03ab`).
- The Field Sheet is unchanged (same text) and was not re-uploaded.
