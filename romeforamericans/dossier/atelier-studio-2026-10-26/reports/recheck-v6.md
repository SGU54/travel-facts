# Ruth Calloway re-reads Rome, Solved. (2026-10-26): build-studio r5, 86 pages + Field Sheet (1 p)

Against: recheck-v5 (2026-10-26: 1 blocker, 9 majors, 23 minors).
Evidence: I re-ran `critic.py` today (`_studio/r5/critic/`: book.txt, companion-field-sheet.txt, critic-sheet.md, desk-numbers.md). I looked at the rendered pages `_affiche/p26.png` (Fig. 5), `p35.png` (D06 poster), `p36.png`, `p37.png` (Fig. 7), `p48.png` (Fig. 9), `p65.png` (Pantheon) and `p79.png` (wallet card). I also read `_studio/writer/notes.md` (v5 section), `figure-edits.json`, `figfix.py` and `_studio/marta/pictures.json`. I fetched the official taxi tariff PDF myself (below).
Quotes in « » are copied from book.txt or the Sheet text.

A note on page numbers: the `_affiche/pNN.png` file numbers match the printed folios. Fig. 5 is on p26, the D06 poster on p35, Fig. 7 on p37 and Fig. 9 on p48, not on p25/p34/p36/p47 as the brief listed them.

**Verdict: SHIP AFTER FIXES (owner-only)**

The studio's work is done. The taxi blocker is closed: I checked the wording line by line against the deliberation's own perimeter, and no page or Sheet row contradicts it. The three figures (Fig. 5, Fig. 7 and Fig. 9) now draw what their text says. The Pantheon reads « booking optional » everywhere. The misstated D09 join is gone.

Two majors remain, and only the owner can close them: the listing's page count (M15) and p4's statement of what the book sells (M17). The new filings are all minors: wording that the 30-day rewrite left uneven.

**Counts now:** 0 blockers · 2 majors (both owner) · 23 minors.

What happened to the v5 filings:
- **Blocker:** 1 of 1 closed (N1).
- **Majors:** 6 of 9 closed (M1, M3, M18, N2, N3, N4). M14 is closed on the owner's attestation and leaves one minor behind (m30). M15 and M17 stay open for the owner.
- **Minors:** 5 of 23 closed (m10, n1, n3, n4, n7). The other 18 stay open.

New filings: 0 blockers, 0 majors, 5 minors (m30 from M14, plus n9–n12).

## Taxi zone: checked against Delib. G.C. 157 (21 May 2026)

Source: https://www.comune.roma.it/web-resources/cms/documents/TariffarioTaxi_giugno2026.pdf (curl + pdftotext, 2026-10-26). Its header reads « DELIBERAZIONE DELLA GIUNTA CAPITOLINA N. 157 del 21 Maggio 2026 ».

What the tariff says:
- **The fixed fare:** « Dall'Aeroporto di Fiumicino all'interno Mura Aureliane e viceversa € 55,00 ».
- **The meter minimum:** « CORSA MINIMA AEROPORTO DI FIUMICINO … € 35,00 ».
- **The meter maximum:** « TARIFFA MASSIMA … all'interno del G.R.A. … non potranno superare l'importo di € 80,00 ».
- **The zone's boundary** (« Area within the following clockwise boundary »): « … Via Gregorio VII, Piazza Pio XI, Via Anastasio II, Via Cipro, Via Frà Albenzio, Piazza S. Maria delle Grazie, Via Vittor Pisani …, Piazzale degli Eroi, Via Andrea Doria, Largo Trionfale, Viale delle Milizie, Piazza delle Cinque Giornate, Ponte Matteotti, Lungotevere A. da Brescia … Piazzale Flaminio ». The boundary also runs along Piazza dei Cinquecento and Via Marsala (Termini), and along the Mura Portuensi and Gianicolensi (Trastevere).

Every mention in the book and on the Sheet agrees with it:

| where | wording | verdict |
|---|---|---|
| p27 | « The €55 covers the zone the tariff calls the Aurelian Walls: the walled city (Centro Storico, Monti, Trastevere, Termini) plus the Vatican, Borgo and Prati up to Viale delle Milizie. ◇ Beyond that line the meter runs (at least €35, at most €80 from the airport) » | Correct. See n11 for a nit. |
| p27 join | « "Taxis in Rome" fixes €55 for up to four inside the Walls » | Quotes the article, and "the Walls" is the tariff's own name for the zone. No conflict. |
| p86 | « It covers the Walls plus the Vatican and Prati up to Viale delle Milizie, and it is published. » | Correct. |
| FS | « Roma Capitale taxi, Fiumicino → the "Aurelian Walls" zone · €55 fixed … the walled city plus the Vatican, Borgo and Prati up to Viale delle Milizie (set 2024, reissued May 2026) ◇ » | Correct. |
| FS | « Taxi beyond that zone (e.g. north of Viale delle Milizie) · meter: at least €35, at most €80 ◇ » | Correct. The €80 cap applies to rides inside the G.R.A. ring road (n11). |
| p24/p25/p26 posters, ledgers and Fig. 5 | « €55 FLAT, UP TO 4 » | No zone claim. |

A grep finds no « outside the Walls », « not Prati » or « not … the Vatican » anywhere in the book or on the Sheet.

## v5 filings: status

| id | status | evidence (quoted) | what remains |
|---|---|---|---|
| N1 | **CLOSED** | See the taxi section above. p27, p86 and both Sheet rows draw the official perimeter, and nothing says Prati or the Vatican is outside the zone. | n11 (nit) |
| N2 | CLOSED | p27: « The €55 is Roma Capitale's fare, so look for Rome's emblem: Fiumicino's own town taxis also work the airport, on fares their town sets. ◇ » FS: « Fiumicino town taxis charge their own town's fares: check current (no official Fiumicino tariff found) ◇ ». ADR (adr.it/pax-fco-taxi, read via WebSearch 2026-10-26) says « Le tariffe sono stabilite dal Comune competente ». The €80 Fiumicino figure appears only in the press, so the book is right not to print it. | none |
| N3 | CLOSED | p65 caption: « Inside the Pantheon, under the coffered dome and its open oculus. It now charges admission; booking is optional, so buy at the door. » (the frame shows the interior and the oculus; checked on p65.png). Fig. 7: « Pantheon · no booking needed · buy at the door ». p35: « Pantheon: no booking » and « the Pantheon needs no booking ». p36, p51 and p53 agree. This matches « Prenotazione Facoltativa ». | none |
| N4 | CLOSED | The D09 « WHAT THE FREE GUIDES NEVER CONNECT » block has gone from p49. A grep finds no « point opposite » or « half-day does ». | none |
| M1 | CLOSED | Fig. 5 (p26.png): « Leonardo + hop (metro or taxi) », train €28 solid plus onward to €41, labelled « ≈€31–41 ». Near Termini: « ≈€28 ». This matches the caption, the p25 ledger (« ≈ €31–41 for two ») and the Sheet (« ≈ €31–41 »). | none |
| M3 | CLOSED | Fig. 7 (p37.png) is redrawn on a 0–30-day axis: Underground and Standard « on sale 30 days ahead », Arena « opens ≈ 7 days ahead », Pantheon « no booking needed », St Peter's « free · no ticket ». p35 has lost « SIX WEEKS OUT » and « A day or two — Colosseum standard, Pantheon ». The foot now reads « The standard Colosseum goes on sale 30 days out … the Pantheon needs no booking. » The fix criterion is met. | The uneven wording left behind is filed as n9 and n10 (minors). |
| M14 | CLOSED on owner attestation → m30 | pictures.json still records six inherited frames (p31, p37, p49, p59, p62, p65) without a source page. The owner states that the book's photographs came from Unsplash and Pexels under their free licences, with the pages not recorded. Both licences allow commercial use without attribution. | m30 |
| M15 | **OPEN-owner** | LISTING.md: « Rome, Solved. is a 64-page decision manual » and « 1 PDF (64 pages) ». The book is 86 pages. (« 20 failure modes » is right: 5 + 7 + 5 + 3 on p76.) | Owner: change both listing lines to 86 pages, or to whatever the final render counts. |
| M17 | **OPEN-owner** | p4 is unchanged: « The connections between them… are what we've done for you. » | Owner: state what the book sells beyond the free site, and have p4 say the same. The Barcelona answer transposes directly: "a decision manual that helps American tourists make the calls; it holds the links between the free guides; and the Field Sheet keeps the figures current." |
| M18 | CLOSED | Fig. 9 (p48.png): Pompeii « ≈ 2½ h » + « the ruins · 6–7 h » + « ≈ 2½ h », with the bar ending at 12 h, labelled « ≈ 12 h door to door ». p47: « a full twelve hours door to door … six to seven hours at the vast site … roughly two and a half hours each way ». The ledger says « ~2½h each way · ~12 HOURS ». The legs add up to 11–12 h. | n12 (Ostia leg wording) |
| m1 | OPEN | The first call is still on p16 of 86. | as v4 |
| m2 | OPEN | p1 « kilometer and a half across »; p17 « roughly a kilometer and a half across »; the p9 poster « a radius, not a total width ». | as v5 |
| m3 | OPEN | p4 « the fifteen or so choices »; p82 « fifteen calls ». The book has nine decisions. | as v5 |
| m6 | OPEN | Fig. 1 still has « Term ». | as v4 |
| m7 | OPEN | Fig. 2 « no line reaches it » (p14, p22). | as v4 |
| m8 | OPEN | p59 « The cheapest and "best-connected" base is the farthest… » | as v4 |
| m9 | OPEN | p85 « whole day somewhere real than half a day somewhere famous ». | as v4 |
| m10 | CLOSED | « SIX WEEKS OUT » is gone; p35 reads « THE DAY SALES OPEN ». | none |
| m13 | OPEN | critic-sheet §4b: Figs 2/4, 6/12 and 8/13 are still the same drawings. | as v4 |
| m14 | OPEN | p78 still files the transit fine and the Spanish Steps fine under « Costs you a good meal, or marks you as a tourist ». | as v4 |
| m16 | OPEN | Fig. 6 « 08:30 · at opening » against Figs 8/13 « locals after 20:30 ». | as v4 |
| m17 | OPEN | p78 « the ZTL fines tourists automatically » is never defined. | as v4 |
| m23 | OPEN | p36 « no walk-ins whatsoever »; p38 caption « no walk-ins, ever »; p33 « mandatory slot, no walk-ins ». | as v4 |
| m26 | OPEN | Phone reading not re-tested on the body; not touched. | as v4 |
| m27 | OPEN-owner | Not touched. | as v4 |
| n1 | CLOSED | p25: « Re-price it honestly and the gap narrows: for two, the taxi costs about €14–24 more; for four, it is about a tie. » | none |
| n2 | OPEN | p79.png: on the back of the cut card, « St. Peter's · Free. Go early. Book nothing » is clipped at the cut line, and « Spare day » and « Where to sleep » are still missing. | Brunner: fit all rows inside the cut line (smaller leading, or drop the duplicate « Reader asks » line). |
| n3 | CLOSED | p41: « Two things on the receipt look like tips and are not. » | none |
| n4 | CLOSED | p47 « Monday to Saturday, ◆ »; FS « ≈ €9–13 by taxi ◆ »; FS « EES: began 12 October 2025, fully in force since 10 April 2026 ». | none |
| n5 | OPEN | The strike band still rests on Cotral's page (writer: no ATAC page was readable). | as v5 |
| n6 | OPEN | p38 « The live booking windows are the Field Sheet's core »; p49 « the Field Sheet carries the current ones » (train times and site hours). The Sheet answers « window: check current » for the Vatican and Borghese, and « Circumvesuviana and Pompeii hours: check current ». | as v5 |
| n7 | CLOSED | FS: « ≈ €8 a person (tariff of October 2024, still the one published) ◆ ». | none |
| n8 | OPEN-owner | p19 « thirty-five-minute walk », against 20–25 min in the site's Termini article. | as v5 |

## New filings

| id | p | severity | the book, verbatim | the reader's reaction | loses | to | closed when |
|---|---|---|---|---|---|---|---|
| m30 | 31, 37, 49, 59, 62, 65 | minor | pictures.json: six frames with « original source and licence unknown — to source » | — | Records: Unsplash and Pexels allow commercial use, but without a page URL a takedown claim can't be answered. | marta | pictures.json carries "Unsplash/Pexels, free licence (owner attestation 2026-10-26)" for the six frames, plus each page URL once it is found by reverse search. |
| n9 | 37 | minor | Fig. 7 caption: « sights ordered by how far ahead they vanish. The top three punish a late booking with "sold out." ». The drawn top three are Underground, Standard and Vatican, and the Arena is fifth. Vatican and Borghese are drawn as dashed bars running the full 30 days, with « window: check current ». | p36 says the three are the Arena, the Vatican and the Borghese, and that the Standard « rarely den[ies] » you. Which three do I lock first? | Trust; a small risk of booking the Borghese late. | brunner | The caption says what is drawn ("ordered by how early sales open"), or the order follows p36. The open-window bars stop short of a day value (a dot or an arrow, not a 30-day bar). |
| n10 | 35, 36, 51 | minor | p35 tier: « BOOK THE DAY SALES OPEN · VATICAN MUSEUMS · BORGHESE · UNDERGROUND »; big words: « Book them the moment your dates are firm »; foot: « the Vatican Museums, the Borghese, and … the arena floor »; axis: « THE DAY SALES OPEN … YOUR DATES ARE FIRM → » over a 42-day grid. p36: « From April through October, book it when your dates are firm » against the overrule « from April to October, book when the 30-day sale opens ». p51: « A DAY OR TWO AHEAD · In winter, reserve the standard Colosseum ticket » against p36 « in winter, a few days ahead ». | Is the third sight the Underground or the Arena? Do I book when my dates are firm, or when the sale opens? | Friction | marta, writer | One third sight on the poster (tier and foot agree with the wallet card). One rule for the Standard in peak season (« when the 30-day sale opens »). Winter reads « a few days ahead » on p51 too. The axis is labelled in days, not with a repeated phrase. |
| n11 | 27, FS | minor | « Beyond that line the meter runs (at least €35, at most €80 from the airport), so agree the fare before you load the bags » | You can't agree a fare on a meter. | Friction | writer | The line reads "the meter runs (minimum €35, capped at €80 anywhere inside the GRA ring road); check the meter is on before you load the bags". |
| n12 | 49, 71 | minor | p49 « The two-hours-versus-thirty-minutes asymmetry does not [change] »; p47 gives « ~2½h each way » and « about twenty-six minutes »; p71 « Ostia Antica ~30 MIN EACH WAY » | The numbers shift by a little each time. | Slight trust | writer | p49 says "two and a half hours against half an hour", and p71's ~30 min is explicitly door to station or matches p47. |

## What I would not change

- The taxi paragraph on p27. It now names the bases inside the zone as the tariff draws them, and for the first time it says which taxi charges the €55.
- The redrawn Fig. 7: days, not weeks, open bars where no official window exists, and a dot for "no booking". That is honest drawing.
- Fig. 9's legs, which add up to the total printed beside them.
- Dropping the D09 join instead of patching it.
