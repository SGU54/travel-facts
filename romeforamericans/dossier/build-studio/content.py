# -*- coding: utf-8 -*-
"""content.py — THE DECISIONS. The analytical heart. Each is a cross-article synthesis
that no single free article makes, with a losable verdict and named stake.
Marks: <span class='mk est'>\u25cf</span> ESTABLISHED / off \u25c7 OFFICIAL / sur \u25b2 SURVEYED / vol \u25c6 VOLATILE.
Density rule (writing-code.md): \u22641 mark per paragraph, at sentence end, most paragraphs none.
"""

EST = "<span class='mk est'>\u25cf</span>"
OFF = "<span class='mk off'>\u25c7</span>"
SUR = "<span class='mk sur'>\u25b2</span>"
VOL = "<span class='mk vol'>\u25c6</span>"

DECISIONS = [
{
 "n":"01","cat":"Base","fig":"core_map",
 "q":"Where should you actually sleep?",
 "stand":"The most consequential booking you make \u2014 and the instinct that ruins it is treating a metro address as an upgrade.",
 "lede":(f"Rome\u2019s historic core is roughly a kilometre and a half across, and its outer edges \u2014 the Colosseum, "
   f"Trastevere, the Spanish Steps \u2014 sit about twenty minutes\u2019 walk from the centre. {EST} The classic sights a "
   "first-timer comes for are not scattered across a metropolis; they are one connected pedestrian district you cross on "
   "foot in well under an hour. That single fact should decide where you sleep \u2014 and it quietly overturns the booking "
   "logic most Americans arrive with."),
 "body":[
   ("The instinct is reasonable and wrong. You are told, correctly, that the streets around Termini station hold Rome\u2019s "
    "densest concentration of hotels, at the city\u2019s best prices, with both metro lines and the airport train on the "
    f"doorstep. {EST} So you book there to save money and \u201cstay near the transport.\u201d The flaw is that the transport "
    "you are buying access to cannot reach the sights you came for. Rome\u2019s metro deliberately skirts the historic centre "
    f"\u2014 you cannot tunnel freely under two thousand years of ruins \u2014 so the heart of the city has no line under it at "
    f"all. {EST} A Termini base puts you next to the one tool that doesn\u2019t serve the place you\u2019re going."),
   ("Do the walk instead of the maths. From a hotel by Termini, the Pantheon is a thirty-five-minute walk and Piazza "
    "Navona closer to forty; from Centro Storico or Monti, the centre of the core is about thirteen. The €30 you saved on "
    "the room buys you an hour of daily commuting \u2014 by metro to a station that still leaves you a walk short, or on foot "
    "across the least interesting part of the centre. You did not save money. You spent it in the currency the trip is "
    "actually short of, which is unhurried time inside the walls."),
   ("This is why the neighbourhood, not the hotel, is the decision. A merely adequate room in the core beats a beautiful "
    "one outside it, because on a three-day first trip the walk home at midnight \u2014 past a floodlit fountain, through a "
    "lane of wine bars \u2014 is not travel overhead. It is the thing you came for. The base decides how much of that you get."),
 ],
 "cols":"WALK TO CORE \u00b7 CHARACTER \u00b7 PRICE",
 "table_title":"The bases, scored \u00b7 first-time American, 3 nights",
 "rows":[
   ("Centro Storico \u2014 postcard Rome, walk to all "+EST, "13\u2032", "highest"),
   ("Monti \u2014 local feel, steps from the Forum "+EST, "13\u2032", "mid"),
   ("Trastevere \u2014 charm and dinners, a bridge over "+EST, "20\u2032", "mid"),
   ("Prati \u2014 calm, elegant, Vatican-side "+EST, "38\u2032", "mid"),
   ("Near Termini \u2014 cheapest, best transport, gritty "+EST, "28\u2032", "lowest"),
 ],
 "verdict":("<strong>Sleep inside the core; treat a metro address as a downgrade, not a discount.</strong> For a first "
   "trip of three or four days, book Centro Storico if the budget allows and Monti if it doesn\u2019t \u2014 both put the "
   "centre thirteen minutes\u2019 walk away. Choose Trastevere only if evenings matter more than mornings, and accept the "
   "bridge. Termini is a fine place to change trains and a poor place to wake up."),
 "for":["you want the classic sights, and you\u2019re here three or four days \u2192 Centro Storico or Monti",
        "evenings and atmosphere outrank proximity to the ruins \u2192 Trastevere, bridge and all"],
 "against":["you\u2019re here to do serial day-trips by rail and barely see Rome \u2192 Termini earns its place",
            "you specifically want a large full-service hotel \u2192 the core has few; Prati or Termini have them"],
 "note":(f"The €-figures move; the walk-times don\u2019t. {VOL} Room rates by area and season live on the Field Sheet. "
   "The distances above are ours, measured on foot. "+SUR+" SURVEYED 07/26."),
 "xref":"the transit maths that follows from this \u2192 Decision 02",
},
{
 "n":"02","cat":"Transit","fig":"transit_reality",
 "q":"Do you need transit tickets at all?",
 "stand":"The Roma Pass sells itself on a commute you already decided not to make.",
 "lede":(f"Rome\u2019s two tourist passes \u2014 the Roma Pass and the pricier, Vatican-inclusive Omnia Card \u2014 promise to "
   f"save you money and time, and the marketing makes them sound like obvious buys. {EST} The honest answer is that they "
   "pay off for a specific traveller with a specific itinerary and waste money for everyone else. What almost no one tells "
   "you is that Decision 01 has already answered this one."),
 "body":[
   ("The passes bundle two things: unlimited public transport for the period, and free or discounted entry to a handful of "
    f"attractions. {EST} The standard advice \u2014 sound as far as it goes \u2014 is to \u201crun the math\u201d: total the entry "
    "prices you\u2019d pay anyway, add your transport, and compare to the pass. But that math is always computed in a vacuum, "
    "as if your transport spend were an unknown. It isn\u2019t. If you took Decision 01 and slept in the core, you will walk "
    "to nearly everything, and your real transport bill for three days is close to zero."),
   ("Collapse the transport line and the pass\u2019s case collapses with it. Strip out the rides you won\u2019t take, and a "
    "pass has to justify itself on attraction savings alone \u2014 a much narrower margin, and one the first Sunday of the "
    f"month can erase entirely, when state museums including the Colosseum admit everyone free. {OFF} For the walk-"
    "everywhere first-timer, the pass is selling a convenience \u2014 grab-any-bus, skip-the-ticket-line \u2014 priced for a "
    "traveller who is criss-crossing the city by metro. You are not that traveller by design."),
   ("So do the thing that makes the question disappear: tap a contactless card. Tapping a card or phone on the reader "
    "charges the single fare and automatically caps your spending at the day-pass price once you\u2019ve ridden enough \u2014 no "
    f"kiosk, no paper, no validation, and no way to overpay. {EST} It is strictly better than buying single paper tickets, "
    f"and it removes the one genuinely expensive mistake here: an unvalidated paper ticket is treated as no ticket, and "
    f"inspectors issue on-the-spot fines of €100 or more without sympathy. {OFF} The tap is its own validation."),
 ],
 "cols":"WHO \u00b7 THE HONEST VERDICT",
 "table_title":"The pass, decided by how you sleep and walk",
 "rows":[
   ("Central base, mostly on foot (Decision 01) "+EST, "skip it \u2014 tap a card, let the cap work"),
   ("Doing the Vatican + Colosseum blitz, riding daily "+EST, "Omnia can pay \u2014 but only at 72h"),
   ("Transport-heavy, 2+ covered sights, no Vatican "+EST, "Roma Pass math may work \u2014 check it"),
   ("Two-day trip "+EST, "Omnia is 72h-only \u2014 you can\u2019t use the value"),
 ],
 "verdict":("<strong>If you slept in the core, skip the pass and tap a contactless card.</strong> The daily fare cap means "
   "you never overpay and never do arithmetic at a machine. Reach for the Roma Pass only if you\u2019re genuinely transport-"
   "heavy and hitting two or more of its sights; reach for the Omnia only for a three-day Colosseum-and-Vatican blitz. "
   "Buying either \u201cto be safe\u201d is the easiest way to overpay in Rome."),
 "for":["you\u2019re criss-crossing by metro daily and hitting 2+ covered sights \u2192 do the Roma Pass math",
        "classic 3-day blitz, both Colosseum and Vatican, using the bus tour \u2192 Omnia can just about pay"],
 "against":["you\u2019re central and walking (the whole premise of this book) \u2192 tap a card, skip the pass",
            "you\u2019re here two days \u2192 the Omnia\u2019s 72-hour floor rules it out on its own"],
 "note":(f"Pass prices and the fare cap shift periodically. {VOL} Current figures are on the Field Sheet; the logic above "
   "doesn\u2019t change with them."),
 "xref":"why your base already decided this \u2192 Decision 01",
},
{
 "n":"03","cat":"Arrival","fig":"airport_strip",
 "q":"Train, or the fixed-fare taxi from the airport?",
 "stand":"The cheap option is only cheap for a hotel you were told not to book.",
 "lede":(f"Nearly every transatlantic flight lands at Fiumicino, and the first decision of the trip \u2014 made jet-lagged, "
   "hauling luggage \u2014 is how to reach the city. The received wisdom is that the Leonardo Express train is the smart, "
   f"cheap choice and the taxi is the lazy splurge. {EST} At face value it\u2019s true: the train is about €14, the fixed "
   f"airport taxi €55. {OFF} But that comparison quietly assumes something Decision 01 told you not to do."),
 "body":[
   ("The Leonardo Express runs non-stop to Termini in about thirty-two minutes, roughly every fifteen minutes through the "
    f"day. {OFF} It is fast, frequent and traffic-proof \u2014 and it deposits you at Termini, which, as Decision 01 "
    "established, is exactly where you are not sleeping. From there you still need a metro hop or a taxi or a fifteen-to-"
    "twenty-five-minute walk with your bags to a central hotel. The train\u2019s €14 is only the first leg of your actual "
    "journey door-to-door."),
   ("Re-price it honestly and the gap narrows to almost nothing. Train plus an onward taxi and the luggage-drag lands "
    "around €25\u201330 to a central base; the fixed taxi is €55 flat, up to four people, door to door, no matter the "
    f"traffic or hour. {OFF} For a couple with suitcases after an overnight flight, €25 of difference to be delivered to "
    "the door \u2014 rather than decoded across a station and a second connection while exhausted \u2014 is not obviously the "
    "wrong spend. The train wins outright only if you\u2019re near Termini or a metro stop, the very address the book steers "
    "you away from."),
   ("Whichever you pick, the rules are the same and worth stating, because the real money is lost here, not saved. Use "
    "only the official white taxis from the marked rank, and confirm it\u2019s the posted fixed airport fare before you load "
    f"the bags \u2014 anyone who approaches you inside the terminal offering a ride is the classic unmetered overcharge. {EST} "
    f"There is also a cheaper regional train, the FL1 at about €8, but it does not go to Termini; it serves Trastevere, "
    f"Ostiense and Tiburtina, so it\u2019s a genuine bargain only if you\u2019re sleeping near one of those. {OFF}"),
 ],
 "cols":"OPTION \u00b7 DOOR-TO-DOOR, CENTRAL BASE",
 "table_title":"Fiumicino to a central hotel \u00b7 party of two, luggage",
 "rows":[
   ("Leonardo Express + onward taxi/walk "+OFF, "\u2248 €25\u201330, two legs"),
   ("Fixed-fare official taxi, door to door "+OFF, "€55 flat, up to 4"),
   ("FL1 regional train (only if near its stops) "+OFF, "\u2248 €8, one leg"),
   ("Shuttle bus to Termini "+EST, "cheapest, ~50\u201360 min, traffic"),
 ],
 "verdict":("<strong>Central base, first night, real luggage: take the fixed-fare taxi and don\u2019t feel fleeced.</strong> "
   "The €55 buys door-to-door delivery on the trip\u2019s most fragile day, and split two-to-four ways it\u2019s competitive with "
   "the train once you count the onward hop. Take the Leonardo Express if you\u2019re near Termini, travelling light, or "
   "solo \u2014 then it\u2019s the clear winner. The FL1 is for the handful sleeping by its stations."),
 "for":["couple or family with suitcases, central hotel, jet-lagged \u2192 the fixed-fare taxi",
        "solo or light traveller, or sleeping near Termini/a metro line \u2192 the Leonardo Express"],
 "against":["you\u2019re four people to the door \u2192 €55 split beats four train-plus-onward fares",
            "you\u2019re staying near Trastevere or Ostiense \u2192 the €8 FL1 is the quiet bargain"],
 "note":(f"The taxi fixed fare rose to €55 in 2026 and is set by the airport authority; the train fare is regulated too. "
   f"{VOL} Confirm both on the Field Sheet before you fly."),
 "xref":"why Termini isn\u2019t your base \u2192 Decision 01",
},
{
 "n":"04","cat":"Ancient Rome","fig":"ancient_flow",
 "q":"How do you fit the ancient core into a day?",
 "stand":"One 24-hour ticket doesn\u2019t just save money \u2014 it forbids you a second great sight that afternoon.",
 "lede":(f"The Colosseum, the Roman Forum and the Palatine Hill share a single combined ticket, valid for twenty-four hours "
   f"across all three. {OFF} First-timers meet this at the checkout page as confusion \u2014 three sights, one cart, which "
   "line? \u2014 and resolve it as a money question. It is really a scheduling question, and getting it wrong is how a great "
   "day becomes a forced march."),
 "body":[
   ("Treat the three as one continuous half-day, because geographically that\u2019s what they are: the Forum and Palatine are "
    f"a single archaeological park and the Colosseum is a two-minute walk from its edge. {EST} A thorough visit to all "
    f"three, done properly, is three to four hours on unshaded ancient stone. {EST} That figure is the whole planning "
    "constraint, and it\u2019s the one the ticket page never shows you. The combined ticket isn\u2019t a discount to celebrate; "
    "it\u2019s a time-budget to respect."),
   ("Which is why the classic first-timer error is not a money mistake at all: it is pairing this entire cluster with "
    f"another major sight the same day \u2014 the Vatican, especially. {EST} Do that and you have stacked three-to-four hours "
    "of walking in the sun on top of the single largest museum complex in Rome, on opposite sides of the river. The day "
    "that was meant to be the reason you came turns into an exhausted trudge by four in the afternoon. Give the ancient "
    "cluster its own half-day. The Vatican gets a different one."),
   ("And here your base quietly sets the sequence. Sleep in Monti or Centro Storico and the ancient core is on your "
    "doorstep, so it\u2019s the natural morning and the Vatican is the cross-town expedition; the two unavoidable half-days "
    "fall into an obvious order. The only real choice left inside the ancient morning is which end to start: the Forum at "
    "opening, when it\u2019s cool and nearly empty and its lack of shade doesn\u2019t matter yet, then the Colosseum on a midday "
    "slot for its interior shade \u2014 or the Colosseum first to beat the tour buses, accepting the Forum in the midday heat."),
 ],
 "cols":"ORDER \u00b7 WHAT IT BUYS",
 "table_title":"The ancient half-day, two ways \u00b7 one 24-hour ticket",
 "rows":[
   ("Forum + Palatine first, at opening "+EST, "cool, empty; shade saved for the arena"),
   ("Colosseum first, earliest slot "+EST, "beats the buses; Forum hot at midday"),
   ("The cluster + the Vatican, same day "+EST, "a death march \u2014 don\u2019t"),
   ("Standard tier (not arena floor / underground) "+EST, "right for a first visit; see Decision 06"),
 ],
 "verdict":("<strong>Give the ancient core its own half-day, and start with the Forum at opening.</strong> Enter the "
   "Forum and Palatine when they\u2019re cool and empty, break for lunch, take a midday Colosseum slot for the interior "
   "shade, and do not \u2014 whatever the ticket page tempts you toward \u2014 bolt the Vatican onto the same afternoon. Book "
   "the Standard combined ticket; the arena-floor upgrade is a separate decision with a separate deadline."),
 "for":["you burn out on your feet, or you\u2019re travelling with kids \u2192 Forum-first, split across two mornings if needed",
        "photographs and beating crowds matter most \u2192 Colosseum first slot, then the Forum"],
 "against":["you genuinely have only one morning in Rome \u2192 Colosseum + Forum, treat the Palatine as optional",
            "you\u2019re certain you want the arena floor \u2192 that\u2019s the Full Experience, and it changes the booking horizon"],
 "note":(f"Ticket labels and tier rules shift periodically; confirm the current combined-ticket terms on the official park "
   f"site when you book. {VOL} Timed-slot availability is on the Field Sheet."),
 "xref":"how far ahead to book each tier \u2192 Decision 06 \u00b7 the Vatican\u2019s own day \u2192 Decision 05",
},
{
 "n":"05","cat":"Vatican","fig":None,
 "q":"What does \u201cskip the line\u201d actually skip at the Vatican?",
 "stand":"There are two different queues here, and the expensive ticket only touches one of them.",
 "lede":(f"\u201cSkip the line\u201d is the most-marketed and least-understood phrase in Rome, and nowhere does it mislead more "
   "money out of Americans than at the Vatican. The reason is that a major sight has two entirely different lines, and "
   "they are not the same thing \u2014 a distinction no single listing you\u2019ll buy from bothers to draw."),
 "body":[
   ("There is the ticket line \u2014 waiting to buy admission \u2014 and the security line, the metal-detector screening everyone "
    f"passes through. {EST} A pre-booked timed ticket skips the ticket line. That\u2019s the whole of what it does. At the "
    "Vatican Museums this is genuinely valuable, because they\u2019re timed and capacity-limited and slots sell out weeks "
    f"ahead in peak season {EST} \u2014 so the official timed ticket, with its small booking fee, is the difference between "
    "walking in and a long wait. But the pricey third-party \u201cskip the line\u201d tickets are, overwhelmingly, that same "
    "timed entry with a reseller\u2019s markup wrapped around it, sometimes bundled with a tour you may not want."),
   ("St Peter\u2019s Basilica is where the confusion costs the most, because the basilica is free \u2014 there is no ticket to "
    f"skip. {EST} Its wait is purely the security screening, and no admission product in existence bypasses that. The one "
    "genuine shortcut is a guided tour that enters St Peter\u2019s through the internal passage from the Sistine Chapel, "
    "skipping the square\u2019s security line \u2014 or simply arriving at opening or in the late afternoon when the screening "
    "queue is shortest. Paying anyone for \u201centry\u201d to a free church is paying for nothing."),
   ("The Borghese Gallery makes the point from the opposite direction. It runs on mandatory timed reservations with a "
    f"hard cap and no walk-ins, so everyone inside already holds a booked slot {EST} \u2014 there is no general line for a "
    "\u201cskip\u201d product to skip. Its only real deadline is booking before it sells out. Put the three together and the rule "
    "is plain: book the official timed ticket where one exists, recognise that St Peter\u2019s wait is security you can only "
    "out-schedule, and treat any premium \u201cskip the line\u201d upsell as a tour or a markup \u2014 never magic."),
   ("The genuine fork, then, is not skip-the-line versus wait \u2014 it\u2019s guided versus self-guided, and that\u2019s a taste "
    "decision worth making on purpose. A good guided tour of the Vatican Museums buys you two real things: the "
    "passage-entry to St Peter\u2019s that skips the square\u2019s security line, and a narrative thread through a collection "
    "vast enough to be numbing without one. What it costs is money and the freedom to linger. A confident self-guider "
    "with a downloaded audio guide gets the same official timed entry for a fraction of the price and sets their own "
    "pace, at the cost of doing the interpretive work themselves. Neither is wrong. The error is paying tour prices "
    "under the impression you\u2019re buying a shortcut, when what you\u2019re actually buying \u2014 or not \u2014 is a guide."),
 ],
 "cols":"SIGHT \u00b7 WHAT THE REAL WAIT IS",
 "table_title":"The two lines, sight by sight",
 "rows":[
   ("Vatican Museums \u2014 timed, sells out weeks ahead "+EST, "ticket line: book official, skip it"),
   ("St Peter\u2019s Basilica \u2014 free entry "+EST, "security only: passage-tour or go early"),
   ("Borghese \u2014 mandatory slot, no walk-ins "+EST, "no line to skip; just book ahead"),
   ("Third-party \u201cskip the line\u201d premium "+EST, "usually the timed ticket + a markup"),
 ],
 "verdict":("<strong>Book the official timed ticket for the Museums; for St Peter\u2019s, buy nothing and go early.</strong> "
   "The Museums\u2019 official slot is the real value and skips the only line a ticket can. St Peter\u2019s is free and its wait "
   "is security \u2014 beaten by the museum-passage tour or by opening/late-afternoon timing, not by a purchase. The "
   "Borghese\u2019s mandatory reservation is your \u201cskip the line\u201d already. Pay a premium only for a guide you actually want."),
 "for":["you\u2019d retain more of the Sistine Chapel and St Peter\u2019s with a guide \u2192 a passage-tour earns its price",
        "the official Vatican site is sold out for your dates \u2192 a reputable reseller\u2019s backup slot is legitimate"],
 "against":["you\u2019re a confident self-guider with an audio app \u2192 the official timed ticket does the line-skipping for far less",
            "you\u2019re about to pay for \u201centry\u201d to St Peter\u2019s \u2192 stop; it\u2019s free, and only security stands between you and the door"],
 "note":(f"Booking fees, opening hours and the passage-tour availability change; confirm on the Field Sheet. {VOL} "
   "The two-line distinction itself does not."),
 "xref":"why this is its own half-day, not the Colosseum\u2019s \u2192 Decision 04 \u00b7 the horizon to book it \u2192 Decision 06",
},
{
 "n":"06","cat":"Booking","fig":"booking_calendar",
 "q":"What must you book in advance \u2014 and how far?",
 "stand":"The single highest-impact hour of planning, and it lives in four articles that never share a calendar.",
 "lede":(f"The biggest mistake Americans make in Rome is the plainest: showing up at the Colosseum, the Vatican or the "
   f"Borghese expecting to buy a ticket at the door. {EST} Each of those sights tells you, in its own place, that it needs "
   "booking ahead. What no single source does is put the deadlines on one calendar \u2014 so a first-timer books the easy "
   "thing early and discovers the hard thing sold out."),
 "body":[
   ("Sort the sights by how early they vanish, because the horizon is different for each. The Colosseum\u2019s Full "
    f"Experience \u2014 the arena floor and the underground \u2014 is guided-only and sells out weeks ahead. {EST} The Vatican "
    f"Museums are timed and capacity-capped and go weeks in advance in peak season. {EST} The Borghese Gallery is the "
    f"strictest of all: a mandatory timed slot with a hard cap and no walk-ins whatsoever. {EST} These three are the ones "
    "that punish a late booking with the word \u201csold out\u201d against the sight you flew for."),
   ("Below them sit the sights that reward booking but rarely deny it. The standard Colosseum combined ticket runs on "
    f"timed entry you should still reserve, especially in high season; the Pantheon is now timed-entry too. {OFF} These "
    "you book to skip the ticket line, not because they\u2019ll be gone \u2014 a day or two ahead is usually enough. And one sight "
    "needs nothing at all in advance: St Peter\u2019s is free, and its only queue is security, which no booking touches (see "
    "Decision 05)."),
   ("One trap belongs on this calendar because it looks like the opposite of one. The first Sunday of each month brings "
    f"free state-museum entry \u2014 the Colosseum, Forum and Palatine included \u2014 which sounds like a gift and is, in "
    f"practice, the single busiest day of the month, with queues that stretch two to three hours by mid-morning. {EST} "
    "Unless saving the modest entry fee genuinely matters to you, a normal paid day with a booked slot is the better "
    "experience. Free is not the same as cheap once you price the hours."),
 ],
 "cols":"SIGHT \u00b7 HOW FAR AHEAD",
 "table_title":"The one booking calendar \u00b7 earliest-to-vanish, down",
 "rows":[
   ("Colosseum Full Experience (arena/underground) "+EST, "~weeks \u2014 guided-only, sells out"),
   ("Vatican Museums "+EST, "~weeks in peak \u2014 sells out"),
   ("Borghese Gallery "+EST, "book on sale \u2014 mandatory, no walk-ins"),
   ("Colosseum Standard / Pantheon "+OFF, "a day or two \u2014 to skip the ticket line"),
   ("St Peter\u2019s Basilica "+EST, "nothing \u2014 free; only security, go early"),
 ],
 "verdict":("<strong>Book the three that sell out the moment your dates are firm; leave the rest to the trip week.</strong> "
   "The Vatican Museums, the Borghese, and \u2014 if you want it \u2014 the Colosseum\u2019s arena floor are the ones that vanish; "
   "reserve them first, weeks out. The standard Colosseum and the Pantheon need only a day or two. Book nothing for St "
   "Peter\u2019s, and steer clear of the first Sunday unless the free entry truly matters more than the morning."),
 "for":["you want the arena floor or underground \u2192 this is the booking that must happen first, weeks ahead",
        "your dates are still soft \u2192 lock the Vatican and Borghese the instant they firm up; those don\u2019t wait"],
 "against":["you only want the standard sights \u2192 a day or two ahead is genuinely enough; don\u2019t over-plan",
            "your trip overlaps a first Sunday \u2192 either arrive before opening for a booked free slot, or skip the date"],
 "note":(f"Which sights are timed, and how fast each sells out, shifts by season and by policy. {VOL} The live booking "
   "windows are the Field Sheet\u2019s core; the ordering above is stable."),
 "xref":"the Vatican\u2019s two lines \u2192 Decision 05 \u00b7 the ancient tiers \u2192 Decision 04",
},
{
 "n":"07","cat":"Money","fig":None,
 "q":"Cards or cash \u2014 and the one prompt that quietly overcharges you?",
 "stand":"An American-specific tax you pay by reflex, at a card reader, every time you answer wrong.",
 "lede":(f"Money in Rome trips up American visitors in three predictable ways: they tip too much out of habit, they get "
   f"quietly overcharged by choosing dollars at the card machine, and they\u2019re unsure whether to carry cash at all. {EST} "
   "Italy is card-friendly, tipping is light, and a little cash smooths the edges \u2014 but two of those three mistakes are "
   "specifically American, and the standard Rome advice names them again and again without ever handing you the single "
   "card you need at the counter."),
 "body":[
   ("The costliest is a single word, answered by instinct. When a card reader or ATM asks whether to charge in dollars or "
    f"euros, many Americans choose dollars because it feels familiar \u2014 and pay a worse exchange rate every time, "
    f"sometimes several percent. {EST} This is dynamic currency conversion, and it is the single most common way "
    "Americans overpay in Rome. Always choose euros. Pair that with a card that carries no foreign-transaction fee \u2014 "
    "another ~3% saved on every purchase \u2014 and draw cash only from bank ATMs, never the standalone Euronet-type machines "
    "in tourist areas or the airport exchange desks, which exist to give you a worse rate."),
   ("The second American reflex costs less per instance but fires at every meal. Tipping in Italy is light and not "
    f"obligatory: staff earn a full, regular wage, not a tip-dependent one, so there is no fifteen-to-twenty-percent "
    f"expectation. {EST} Rounding up, or leaving a euro or two per person for good service, is generous and plenty; locals "
    "often leave little beyond the coins. The American 20% doesn\u2019t read as courtesy here \u2014 it reads as a tourist who "
    "hasn\u2019t learned the rules, and it can double the cost of an otherwise light bill over a week."),
   ("Two things on the receipt look like tips or scams and are neither. The coperto is a small per-person cover charge "
    f"for the table, stated on the menu \u2014 not a gratuity and not a trick. {EST} A servizio, when present, is a service "
    "charge already included, which means no further tip is needed. Carry a modest amount of cash \u2014 a day or two\u2019s "
    "small spending \u2014 for the family trattorias that prefer it, for tips (best left in coins, since the card machines "
    "rarely prompt for one), and for the church light-boxes that illuminate a Caravaggio for a euro. You will not need much."),
   ("The balance to strike is cards for almost everything, a little cash for the edges. Italy has become genuinely "
    "card-friendly \u2014 tap to pay works nearly everywhere, and for most purchases a no-foreign-fee card in euros is both "
    "the cheapest and the simplest instrument. Cash earns its place in the specific gaps: the small neighbourhood "
    "trattoria that still prefers it, the market stall, the tip you want to leave in coins, the €1 to light a chapel. "
    "What you do not want is a fat envelope of euros bought at a poor rate before you flew, or drawn from a tourist-area "
    "machine that skims you twice \u2014 once on the fee, once on the conversion you should always decline. Draw small "
    "amounts from a bank ATM as you need them, keep the day\u2019s cash on you and the rest in the room, and let the card "
    "do the heavy lifting. The pickpocket\u2019s best day is the day you carry a week\u2019s spending at once."),
 ],
 "cols":"AT THE COUNTER \u00b7 THE MOVE",
 "table_title":"The American wallet card for Rome",
 "rows":[
   ("Reader asks dollars or euros? "+EST, "Euros. Always. (Decline DCC.)"),
   ("Tipping a €60 dinner? "+EST, "Round up / a couple of euros \u2014 not €12"),
   ("Coperto on the bill? "+EST, "Normal cover charge \u2014 not a tip, not a scam"),
   ("Need euros? "+EST, "Bank ATM, decline conversion \u2014 not an exchange desk"),
 ],
 "verdict":("<strong>Choose euros at every machine, tip like a local, and carry a little cash.</strong> The dollars-or-euros "
   "prompt is the one recurring overcharge you control completely \u2014 always euros, always a no-fee card if you have one, "
   "always a bank ATM. Tip by rounding up, not by American percentage; the coperto isn\u2019t a tip. Keep a day or two\u2019s "
   "cash for small trattorias and tips, and no more \u2014 large sums are only pickpocket bait."),
 "for":["you have a no-foreign-fee card \u2192 use it everywhere, tap to pay, and always in euros",
        "you like the reassurance of arrival cash \u2192 a small amount is fine; top up from bank ATMs in the city"],
 "against":["you\u2019re tempted to pre-buy euros at your home bank \u2192 the rate is usually poor; wait and use an ATM here",
            "you feel rude leaving \u201conly\u201d a euro or two \u2192 you\u2019re tipping exactly as a Roman does; the reflex is the error"],
 "note":(f"Exchange spreads and any no-fee card you use are yours to check before flying; the euro-not-dollars rule is "
   f"permanent. {VOL} The current USD\u2013EUR reference sits on the Field Sheet."),
 "xref":"the scams this overlaps with \u2192 Failure modes, p.\u2009\u25cb",
},
{
 "n":"08","cat":"Eating","fig":"eating_rule",
 "q":"How do you avoid eating badly in a city this good at food?",
 "stand":"The trap isn\u2019t bad luck \u2014 it\u2019s a direct function of the walk-time thesis, and ninety seconds cures it.",
 "lede":(f"Rome has spectacular food and, especially around the big sights, plenty of mediocre, overpriced restaurants "
   f"engineered to catch tourists who don\u2019t know better. {EST} Every guide hands you a filter of red and green flags. "
   "What none of them connects is why the traps cluster exactly where they do \u2014 and once you see that, the filter "
   "collapses into a single move you can make with your feet."),
 "body":[
   ("The tells themselves are reliable and worth carrying. Walk away from a host outside actively waving you in; from big "
    "laminated menus with glossy photos of every dish; from menus in five languages with flags; from a \u201cmenu turistico\u201d; "
    f"from an encyclopaedic menu doing pizza and pasta and seafood and steak all at once. {EST} Look instead for a short, "
    "seasonal, often handwritten menu, mostly in Italian, focused on Roman classics \u2014 cacio e pepe, carbonara, "
    f"amatriciana, gricia \u2014 and a room with locals in it after 8:30 p.m., when Romans actually eat. {EST} That is the "
    "whole filter, and it works."),
   ("But notice the single strongest red flag, because it explains all the others: proximity to a major sight. Prime real "
    f"estate facing the Trevi, the Pantheon, Piazza Navona or the Colosseum pays for itself with location, not cooking \u2014 "
    f"the closer to a top sight, the higher the trap risk. {EST} That is not a coincidence you memorise; it is the walk-"
    "time thesis of this whole book, seen from the dinner table. Because the historic core is small and dense, sight-"
    "facing frontage is the most valuable and most touristed ground in the city, and the restaurants on it are priced for "
    "a captive one-time audience that will never return."),
   ("Which means the cure is the same kilometre-and-a-half fact that decides everything else here. You do not need a "
    "restaurant list \u2014 lists rot within a season, and the listicle that named a dozen favourites is free anyway. You need "
    "to walk ninety seconds off the sight. The core is small enough that two or three streets back from any monument is a "
    "different city with a different bill: quieter frontage, cheaper rent, and a kitchen that survives on Romans coming "
    "back. The rule outlives every list, because it\u2019s built from the geography, not from names."),
 ],
 "cols":"SIGNAL \u00b7 READ",
 "table_title":"The filter, and the one move behind it",
 "rows":[
   ("Photo-menu, flags, tout at the door "+EST, "walk away \u2014 priced for one-time tourists"),
   ("On the famous piazza itself "+EST, "the strongest trap signal there is"),
   ("Short Italian menu, Roman classics "+EST, "the green flag \u2014 a kitchen that specialises"),
   ("Locals in the room after 8:30 p.m. "+EST, "the one review you can trust"),
 ],
 "verdict":("<strong>Don\u2019t collect restaurant names; walk ninety seconds off the sight.</strong> The trap density is "
   "highest exactly where the frontage is most valuable \u2014 facing the monuments \u2014 so the reliable move is to leave that "
   "frontage. Two or three streets back, look for a short Italian menu of Roman classics and a room that fills with "
   "locals after 8:30. That rule finds you a good meal almost anywhere in the core, and it never goes out of date."),
 "for":["you want one durable skill instead of a list to chase \u2192 the ninety-second rule is the whole of it",
        "you\u2019re near a major sight at dinnertime \u2192 that\u2019s the cue to walk, not to sit down where you are"],
 "against":["you\u2019ve booked a specific well-reviewed place \u2192 fine \u2014 the rule is for the other five nights you didn\u2019t plan",
            "it\u2019s lunch and you\u2019re mid-sightseeing \u2192 a market or a standing counter beats any sit-down by the monument"],
 "note":(f"We name no restaurants on purpose \u2014 see \u201cWhat this book won\u2019t tell you.\u201d A named place is a guess with a "
   "byline; the rule is what lasts."),
 "xref":"why the core is small enough for this to work \u2192 Decision 01",
},
{
 "n":"09","cat":"Day trips","fig":"daytrip_asymmetry",
 "q":"If you have a fourth day, where does it go?",
 "stand":"The famous name is the wrong default: Ostia beats Pompeii for a short trip by eleven hours.",
 "lede":(f"A fourth or fifth day in Rome buys a day trip, and the reflex is Pompeii \u2014 the Roman city stopped mid-life by "
   f"Vesuvius, one of the most affecting places in Italy. {EST} It is genuinely extraordinary and, for a first-timer on a "
   "tight trip, usually the wrong call \u2014 because almost no one weighs it against the ancient Roman city sitting half an "
   "hour from the centre, which no single article ever places beside it."),
 "body":[
   ("Price Pompeii honestly as a day and the cost is time, not money. From Rome it is a full twelve hours door to door: a "
    "seventy-minute high-speed train to Naples, a transfer to the basic Circumvesuviana commuter line for another thirty-"
    f"five to forty minutes, several hours at the vast site, and the whole journey again in reverse \u2014 roughly two hours "
    f"each way. {EST} It is a rewarding day and a demanding one, and every guide that describes it says the same thing: "
    f"don\u2019t try to pair it with anything else. {EST} It consumes the day whole."),
   ("Now set Ostia Antica beside it, which nothing you read for Rome does. Ostia was Rome\u2019s own port \u2014 a full ancient "
    "city of paved streets, apartment blocks, baths, temples and astonishing floor mosaics \u2014 abandoned and silted up "
    f"rather than buried, and remarkably preserved for it. {EST} It is reached in about thirty to thirty-five minutes from "
    f"the centre on a regular metro ticket: no high-speed booking, no transfer, no two-hour haul, and far fewer crowds. {EST} "
    "It gives you the texture of everyday Roman urban life \u2014 the thing the great monuments can\u2019t \u2014 for a fraction of "
    "the day."),
   ("So the honest comparison, which is the value the free articles leave on the table, is this: Pompeii is the greater "
    "site and the far greater cost; Ostia is \u201cRome\u2019s Pompeii\u201d at a tenth of the day. If your fourth day is your only "
    "spare day, Ostia lets you have the ancient-port experience and still keep an evening in Rome \u2014 whereas Pompeii is "
    "the whole day and then some. Choose Pompeii only if you actively want that specific, singular place and have a full "
    "day to give it. As a default for a short trip, the famous name is the trap; the nearer ruin is the smarter day."),
 ],
 "cols":"TRIP \u00b7 THE DAY IT COSTS",
 "table_title":"The ancient-port choice \u00b7 one spare day",
 "rows":[
   ("Ostia Antica \u2014 metro, ~30\u201335 min each way "+EST, "half a day; keep the evening in Rome"),
   ("Pompeii \u2014 train + Circumvesuviana, ~2h each way "+EST, "~12h door-to-door; the whole day"),
   ("Which is the greater site "+EST, "Pompeii \u2014 but at the full day\u2019s price"),
   ("Which fits a first-timer\u2019s spare day "+EST, "Ostia \u2014 the smarter default"),
 ],
 "verdict":("<strong>For a single spare day, take Ostia Antica; save Pompeii for a trip that can spare a whole day to "
   "it.</strong> Ostia delivers the ancient-port experience \u2014 real streets, real mosaics, everyday Roman life \u2014 half "
   "an hour out on a metro ticket, and leaves you an evening in Rome. Pompeii is the greater site and demands twelve "
   "hours and an early start; it rewards the trip that has the day to give, not the one squeezing in a fourth."),
 "for":["you want maximum ancient Rome with an evening still in the city \u2192 Ostia Antica, and it\u2019s cheap",
        "you specifically came for Pompeii and have a clear full day \u2192 take it, start by 8, pair it with nothing"],
 "against":["you\u2019re deciding between other day-trips entirely \u2192 Florence and Naples are their own calls; this one is ancient-port vs ancient-port",
            "you\u2019ve got five-plus days \u2192 you may fit both a full Pompeii day and a half-day Ostia; the tension is only on a tight trip"],
 "note":(f"Train times, Circumvesuviana conditions and site hours change; the Field Sheet carries the live figures. {VOL} "
   "The two-hours-versus-thirty-minutes asymmetry does not."),
 "xref":"why the ancient core itself is a half-day, not a day-trip \u2192 Decision 04",
},
]
