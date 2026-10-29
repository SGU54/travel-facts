# Writer's answers to Ruth Calloway, critic-v4 (2026-10-25). Written 2026-10-26

Files: `rome-edits.json` (41 edits, each `old` checked to occur exactly once across every string field of every block in rome-book.json, then applied in sequence without a miss), `fieldsheet.json` (27 rows, 6 groups, dated), `closures.json` (B3, two paragraphs).

**How to apply.** Each edit names `chapter_id`, `block` and `field`. Most are `text`. Some are ledger cells such as `rows[0].vals[0]`, a caption `cap`, a call `rest` or `forks.items[n].text`. Line blocks (`t: line`) also carry `runs`. Whoever applies an edit must rebuild `runs` from the new `text`. Eight line edits change length by −8 to +13 characters (M2, M4 ×2, M8 ×2, M16, B3 ×2), so **Brunner must check the reflow**.

**Source reachability on 2026-10-26.** These sites refused connections from WebFetch, curl and the owner's Chrome: colosseo.it, cultura.gov.it and its subdomains (Pantheon, Ostia, Borghese), and scioperi.mit.gov.it. For those values I used the official wording that WebSearch returned from those pages, and every row says so. A source showing "read by Ruth" is her 2026-10-25 reading.

## Blockers

- **B1: closed.** Every deferral now finds a dated value on the Sheet (see `deferrals`), or it left the book:
  - **Room rates (p19) left the book.** No official or primary source publishes them, so D01's note now says we print none.
  - **p31, p34 and p49** were reworded to name only what the Sheet answers. The passage tour and "Circumvesuviana conditions" were dropped because I could not source them.
  - **Pompeii hours stay "check current"**: pompeiisites.org returned 404, and only third-party hours were found.
  - **Owner:** the Sheet's update path (romeforamericans.com/guide/sheet, "enter the email you bought the Book with"). Ruth asks whether an Etsy purchase counts. That is a product question I have not answered.
- **B2: closed for the writer.**
  - The Sheet is dated October 2026, every row reads label → value, and the taxi reads "set 2024, reissued May 2026", which matches the edited p27 note.
  - The wrong "raised 2026" and "Full Experience ~weeks" values are gone.
  - **Brunner** still has to set the Sheet on one page.
- **B3: closed**, subject to the paragraphs being inserted (`closures.json`).
  - The new paragraphs cover the Vatican Sunday closure and church holidays, Ostia's and the Borghese's Monday closure, and the Colosseum's winter hours.
  - They also cover strikes: where they are announced, Rome's guaranteed bands, Trenitalia's list for the airport train, and what a strike means in practice.
  - The plans on p68 and p86 now say "never a Sunday" and "Ostia (closed Mondays)".
  - Room came from about 80 words cut from Walking the quarters and the removed queue figure.

## Majors filed to the writer

- **M1: closed for the text.**
  - Everything is now in one unit, a party of two: about €31–41 door to door by train plus the hop, against €55 for the taxi. This covers the text, the Fig. 5 caption and the ledger.
  - The four-person overrule was corrected, because the official four-for-€40 group fare makes it roughly a tie.
  - **Brunner** must redraw Fig. 5's bars.
  - **Open:** the p24 poster ("€55") belongs to Marta.
- **M2: closed.** Centro Storico, Monti, Trastevere and Termini are inside the Walls. Prati and the Vatican are outside, where the meter runs (at least €35, at most €80). The book now says how to spot an official taxi, and p87 agrees.
- **M4: closed.** Standard tickets go on sale 30 days ahead (colosseo.it, via search excerpt). From April through October, book when your dates are firm; in winter, a few days ahead is enough. The "season" part is our read and is unmarked.
- **M3 (Fig. 7):** belongs to Brunner. The text and ledger now give 30 days (standard and underground) and about 7 days (arena).
- **M5: closed.** Tickets carry each visitor's name, and each of you shows photo ID at the gate (p29).
- **M6: closed.** The dress code is quoted from basilicasanpietro.va.
- **M7: closed for the writer.**
  - "Entire" is dropped.
  - The paragraph replaces its padding sentence with: passport valid three months past your Schengen exit, the EES (live since 10 Apr 2026), ETIAS not yet required, a phone/eSIM, and 112.
  - **Owner:** should the book name an eSIM seller or link /go/esim (the Airalo affiliate)? I wrote none. Disclosure rules apply if you do.
- **M8: closed.** One action everywhere: ask before you sit; if the coperto is on the bill, ask for it to come off; if they refuse, pay it and don't return. Pages 40, 41, 80 and 87 agree, and "not a scam" / "not a trick" are gone.
  - **Correction to Ruth's table:** L.R. Lazio 21/2006 was repealed by L.R. 22/2019, art. 107. The ban now stands in L.R. 22/2019, art. 75, c. 4, which is in force: "è vietato applicare costi aggiuntivi per il coperto".
- **M16: closed.** The three filed claims (p33, p38, p56) lose their ● and their unsourced numbers. The sibling "go weeks in advance ●" on p38 and the failure-mode line also changed.
  - **Not changed:** ledger option cells such as "Vatican Museums — timed, sells out weeks ahead ●" still carry ●. They are a design choice (every row is marked) and are flagged here for Brunner.

## WRONG / STALE claims

- **FS taxi "raised 2026" (WRONG):** fixed on the Sheet.
- **FS Full Experience (WRONG):** fixed on the Sheet.
- **Pantheon "needs a timed slot" (WRONG in part, m28):** all six booking lines now match "Prenotazione Facoltativa".
- **Ostia leg (STALE, m29):** now about 26 minutes, every 20 minutes Monday to Saturday, on the Metromare timetable in force from 27 July 2026.
- **FL1 €8 (STALE):** kept on the Sheet as "≈ €8" with the 2024 tariff date. No newer Trenitalia tariff was found.

## Not the writer's (untouched)

- M9–M14 belong to Marta.
- M15 and M17 belong to the owner. M17 asks what the book sells beyond the site's own seven calls; that is the owner's call, so p4 is unchanged.
- M18 belongs to Brunner.
- Minors are out of scope, except m28 and m29 (WRONG/STALE). m9 and m15 were closed in passing.
- British spellings in the existing text (m18) are Brunner's. All new text is in US spelling.

## Recheck v5 (2026-10-26): writer items

- **N1 (blocker): answered.** The tariff's "Mura Aureliane" zone (Delib. G.C. 157, 21 May 2026) runs along Via Cipro, Piazzale degli Eroi, Via Andrea Doria and Viale delle Milizie. That puts the Vatican, Borgo and Prati up to Viale delle Milizie inside the €55 zone.
  - **p27:** the M2 edit's `new` was replaced, not stacked.
  - **p86:** the edit's `new` was also replaced. The line grows by 17 characters, so Brunner must check the reflow.
  - **Field Sheet:** the two taxi rows were rewritten. The €35–80 meter now applies only beyond that line.
  - No edit or row now says Prati or the Vatican is outside the zone.
- **N2: answered with what the official source says.**
  - ADR says fares are "set by the competent municipality", that the town's symbol is on the front doors, and that Fiumicino town taxis wait in front of T1 and T3.
  - No official Comune di Fiumicino tariff was found. The €80 figure appears only in the press, so the book and Sheet say "fares their town sets" and the Sheet says "check current".
- **N4: recommend dropping the D09 join.** The live articles already make the call and give the 12-hour figure. joins.json carries `recommend: drop`, plus an accurate text in case the owner keeps the block.
- **N3, M1, M3, M18 (printed figure and poster text):** see `figure-edits.json` (21 items). Pompeii keeps 12 hours: p47 now says 2½ hours each way plus 6–7 hours at the site, and the Fig. 9 bar must end at 12.
  - The p47 ledger's Ostia line (~30–35 min) was missed in v4; it is fixed now.
- **Minors fixed in passing:**
  - n1: the taxi gap is stated (≈ €14–24 more for two; about a tie for four).
  - n3: "or scams" is gone.
  - n4: the timetable takes ◆; the EES line now reads "began 12 Oct 2025, fully in force 10 Apr 2026"; the taxi estimate takes ◆.
  - n7: the FL1 row shows its tariff date.
- **Not done:**
  - n5 (no ATAC page could be read; the band still rests on Cotral's page).
  - n6 (the Vatican and Borghese windows are still not official).

## ChatGPT-audit triage (X1–X8), 2026-10-26

- **X1 (major): closed for the text.**
  - p23 now says each traveler taps their own card or phone, uses the same one every time, and is capped at the Roma 24-hour price for 24 hours from the first tap.
  - The p23 call and p10 now say "24-hour cap".
  - Wallet card: "Your own card each, same one all day. No pass." (+8 characters; Brunner to check the fit).
  - The Sheet row cites ATAC's Tap & Go pages. These are bot-walled and were read via search.
  - No BIT count is printed: ATAC's Italian and English FAQs disagree.
- **X2 (major): done.**
  - `sources.json` lists 29 entries in six groups, each with body, title, canonical URL and checked date. Bot-walled or unreachable pages are flagged.
  - The p8 caption sentence, which belongs to Marta, is in `figure-edits.json`. It claims only ◇ and ◆ claims, because ● marks are "established" and carry no source.
  - The Sheet's note now points to the Sources page.
- **X3:** p41 names "Regional Law 22/2019, art. 75(4)" plus the table form "l.r. 22/2019, art. 75". The wallet card reads "Banned: l.r. Lazio 22/2019, art. 75." Both changes amend my own M8 edits.
- **X4:** p51 (amending my M7 edit) and the Sheet now give the US rule: 3 months past your Schengen exit, 6 recommended, 2 blank pages, 90 days in any 180.
- **X5:** p25 (amending my M1 edit) and the Sheet add "+ €5 per passenger beyond four" (tariff text). "Bags included" stays.
- **X6:** p33 and p36 now give one description: optional paid booking, a timed slot with a digital audioguide and a dedicated route in, security still mandatory, wait not guaranteed (basilicasanpietro.va, via search).
- **X7:** the wallet-card Sheet line is in `figure-edits.json` for Brunner.
- **X8:**
  - p17 now names start and end points. Termini → Piazza Venezia is 28 minutes and Termini → Pantheon 35, so they read as two trips. Centro Storico or Monti → Piazza Venezia is 13.
  - The D01 ledger head now reads "WALK TO PIAZZA VENEZIA".
  - The p16 poster foot (Marta's) is in `figure-edits.json`.
  - m2: p9 says "straight-line radius" and p17 says radius.
  - **Still open:** n8 (the site's own Termini article says 20–25 minutes). That article is the owner's.
