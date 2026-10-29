# -*- coding: utf-8 -*-
"""content2.py — the essays and chapters around the decisions. Voice: Economist/Monocle.
Answers 'how should I think', not 'where should I eat'. The organising fact is the spine.
"""
from content import EST, OFF, SUR, VOL

OPENING = {
 "title":"Rome, Solved.",
 "sub":"A decision manual for a first Roman trip \u2014 the calls the free web scatters, joined.",
 "body":[
   ("Six weeks before a trip to Rome you are not short of facts. You have forty browser tabs, a dozen contradictory "
    "\u201cbest of\u201d lists, and a Reddit thread for every question you can think to ask. What you are short of is the thing "
    "no single tab gives you: a competent voice that holds the whole picture at once and says here is what actually "
    "matters, here is the call, and here is how you\u2019ll know if you disagree and are still right."),
   ("That is the whole of what this book is. It is not a guidebook \u2014 it will not walk you through every church or rank "
    "the gelato. It is a manual of decisions: the fifteen or so choices that decide whether a first Roman trip feels "
    "effortless or exhausting, each one resolved with its reasoning shown, so you can follow the call or overrule it on "
    "purpose. The facts underneath are free and everywhere. The connections between them \u2014 which is where nearly every "
    "expensive mistake actually hides \u2014 are what we\u2019ve done for you."),
   ("Everything here traces to a single organising fact, and the book is really that fact worked out to its "
    "consequences. We\u2019ll state it plainly in a moment, defend it, and then let it decide where you sleep, whether you "
    "buy a transit pass, how you sequence the two biggest sights, and where you eat. The promise is not that you\u2019ll "
    "agree with every verdict. It\u2019s that you\u2019ll never be guessing \u2014 and that when you close the last tab, the trip is "
    "already decided."),
   ("A word on what you\u2019re holding, so the shape makes sense. Each decision is posed as a real question a first-timer "
    "asks, answered with the reasoning laid bare \u2014 the cross-article synthesis, the losable verdict, the case for "
    "overruling us. The chapters between them give the ground the decisions stand on: the one fact, the rhythm of the "
    "week, the texture of the quarters you\u2019ll walk. And a short companion sheet carries the figures that change, so "
    "this book can hold only what lasts. Read it once, cover to cover, in an evening. Then carry the wallet card and "
    "the Field Sheet, and let the forty tabs stay closed."),
 ],
}

HOWTO = {
 "title":"How to read this book",
 "sub":"Two documents, four marks, and one way to carry it on the trip.",
 "body":[
   ("This is a book of judgement, so it separates two kinds of statement carefully. When we assert a hard fact \u2014 a "
    "fare, a rule, a distance \u2014 we mark it, so you can see it is sourced and how solidly. When we reason across those "
    "facts to reach a call, we don\u2019t mark it, because that synthesis is ours and you are free to argue with it. Most "
    "paragraphs carry no mark at all. A mark means \u201cthis specific claim is checkable\u201d; its absence means \u201cthis is our "
    "read.\u201d"),
   ("The marks are four. "+EST+" ESTABLISHED is structural \u2014 true for years, unlikely to move. "+OFF+" OFFICIAL is a "
    "regulated fare, a published rule, a government advisory. "+SUR+" SURVEYED is our own dated observation, with the "
    "month attached. And "+VOL+" VOLATILE is a live figure \u2014 a price, an opening hour, a booking window \u2014 which is "
    "why you will rarely see it in these pages: volatile numbers belong in the second document."),
   ("Because a book that prints today\u2019s prices is wrong by spring, this product is two documents by design. The Book "
    "\u2014 what you are reading \u2014 holds the analysis that ages slowly: the decisions, the reasoning, the geography, the "
    "rules that outlive any list. The Field Sheet is a dated, single-page companion carrying only the volatile figures "
    "\u2014 the current fares, the booking windows, the exchange reference \u2014 refreshed on its own schedule. When the two "
    "ever disagree, the Field Sheet is the newer truth and wins. Read the Book once before you go; carry the Field "
    "Sheet in the trip week."),
   ("One more habit will serve you. Where a decision hands you a verdict, it also hands you the case for overruling it \u2014 "
    "a short \u201cchoose this instead if\u2026\u201d beside each call. That is not hedging; it is the point. A manual that only "
    "worked for the average traveller would fail the specific one, and you are specific: you may burn out on your feet, "
    "or travel with children, or care more about one long dinner than three museums. Read the verdict as the default "
    "and the exceptions as the fitting \u2014 the book is built to be argued with, and it tells you exactly where your own "
    "circumstances should win."),
 ],
}

# ---- THE GROUND: the organising fact, defended ----
GROUND = {
 "title":"The ground: a city you can walk across",
 "sub":"One fact reorganises the whole trip \u2014 the historic core is about a kilometre and a half across.",
 "body":[
   ("Here is the fact the rest of this book is built on. Rome\u2019s historic centre \u2014 the connected core that holds "
    "almost every sight a first-timer comes for \u2014 is far smaller than it looks on a map. The Pantheon, the Trevi "
    "Fountain, Piazza Navona, the Spanish Steps, Campo de\u2019 Fiori, the Forum and the Colosseum all sit inside a "
    f"pedestrian district you can cross on foot in well under an hour. {EST} From its centre near Piazza Venezia, the "
    "farthest of those sights \u2014 the Colosseum, the Spanish Steps, the edge of Trastevere \u2014 are about twenty minutes\u2019 "
    "walk. The dense heart of it, the Pantheon and the piazzas, is closer to ten."),
   ("Two structural facts make walking not merely possible but the only sensible way around. The metro deliberately "
    "skirts the historic centre \u2014 you cannot tunnel freely under two millennia of ruins \u2014 so the core has no line "
    f"beneath it, and cars are restricted or unwelcome in the tangle of pedestrian lanes. {EST} On foot is genuinely the "
    "fastest way through the centre, and it is also the richest: walk from the Pantheon to the Trevi and you pass "
    "fountains, churches with Caravaggios hung in the gloom, artisan workshops and tiny piazzas you\u2019d never have "
    "planned to see. In Rome the walking is not the overhead between sights. It is the sightseeing."),
   ("Internalise that one measurement and the daunting city becomes a small one, and half the trip\u2019s decisions answer "
    "themselves. You sleep in the core because the core is walkable (Decision 01). You skip the transit pass because you "
    "won\u2019t ride enough to justify it (Decision 02). You take the fixed-fare taxi from the airport because it delivers "
    "you into that walkable heart (Decision 03). You eat two streets off the monuments because the core is small enough "
    "that two streets is a different city (Decision 08). Every one of those calls is the same kilometre-and-a-half fact, "
    "pointed at a different question. The one real exception \u2014 the Vatican, across the river, a genuine ride or a long "
    "walk away \u2014 is exactly why it gets its own half-day rather than sharing the ancient core\u2019s (Decision 04)."),
   ("It\u2019s worth meeting the obvious objection head-on, because it\u2019s a fair one: isn\u2019t Rome an enormous city? It is \u2014 "
    "a sprawling modern metropolis of nearly three million people, with suburbs and ring roads and a second airport. But "
    "the Rome a first-timer comes to see is not that city; it\u2019s the compact historic core the tourist map actually "
    "covers, and that core is the kilometre and a half we\u2019ve measured. The confusion between the two \u2014 planning for "
    "the metropolis when you\u2019ll only ever touch the core \u2014 is precisely what produces the Termini base, the transit "
    "pass and the metro-map anxiety this book spends its pages undoing. Rome the metropolis is large. Rome the trip is "
    "small, and you walk it. Hold those two apart and the rest of the book follows."),
 ],
 "fig":"cover_ring",
 "figcap":"The classic-sights core drawn to real walk-times: a 1.5\u2009km ring from Piazza Venezia contains everything a first-timer comes for, with the Colosseum and Spanish Steps on its rim at \u224820 minutes. Termini and the Vatican sit outside it \u2014 which is the whole argument.",
}

# ---- the transit-reality companion page ----
TRANSIT_REALITY = {
 "title":"Why the obvious tool doesn\u2019t help",
 "sub":"The metro is free to read at every station \u2014 and it can\u2019t take you where you\u2019re going.",
 "body":[
   ("A first instinct in any big European city is to master its metro, and Rome punishes that instinct gently. The "
    "network is real and useful for a few specific journeys \u2014 out to the Vatican, in from a far-flung station, across "
    "to a day-trip railhead \u2014 but its two main lines, A and B, cross at Termini and then run to the city\u2019s edges, and "
    f"the historic heart sits in the gap between them. {EST} There is no line under the Pantheon because there cannot be "
    "one. The single most photographed square kilometre of the city is, to the metro, a hole."),
   ("This is why we don\u2019t reprint a metro map, though it\u2019s free at every station: for the first-timer\u2019s core trip it "
    "would mislead more than it helps, implying the network reaches sights it structurally cannot. The honest picture is "
    "the negative space \u2014 the walkable centre the lines curve around. For the handful of rides you will take, tap a "
    "contactless card and let the daily cap handle the fare (Decision 02); for everything inside the core, the fastest "
    "route is your feet."),
   ("The rides that are genuinely worth taking are few and specific, and worth naming so you know the network isn\u2019t "
    "useless \u2014 only misapplied. Line A carries you out to the Vatican (the Ottaviano stop) when you don\u2019t fancy the "
    "long walk across the river, and back in from the airport train at Termini; Line B drops you at the Colosseo stop "
    "beside the ancient core, and runs to the Ostiense and Piramide interchanges for the day-trip lines out to Ostia. "
    "Buses and trams fill the gaps the metro leaves \u2014 the tram to Trastevere, buses across the centre \u2014 but for a "
    "first-timer sleeping in the core, the honest tally is a Vatican hop, an airport connection and a day-trip line. "
    "Everything else is the walk you came to take. Carry the network as a tool for the three journeys that leave the "
    "core, not as the way you\u2019ll get around inside it."),
 ],
 "fig":"transit_reality",
 "figcap":"The two metro lines cross at Termini and run to the edges; the historic heart sits in the gap. The useful mental model of Rome\u2019s transit is the hole in the middle \u2014 not the lines around it.",
}

BEFORE_FLY = {
 "title":"Before you fly",
 "sub":"The short list of things with a deadline \u2014 everything else can wait for Rome.",
 "intro":("Most of Rome rewards improvisation; a small number of things punish it. This is the entire pre-departure list "
   "that matters, each line with the deadline that makes it urgent. If it isn\u2019t here, it can wait until you land. The "
   "list is deliberately short, and its shortness is the point: the anxiety of trip-planning comes from treating every "
   "choice as equally urgent, when in truth only a handful have a clock on them. Get these few right, weeks or days "
   "ahead as noted, and everything else \u2014 what to see, where to eat, how to spend an afternoon \u2014 is better decided "
   "on the ground, in the city, than in a spreadsheet at home."),
 "items":[
   ("Weeks ahead", "Book the sights that sell out: Vatican Museums, Borghese Gallery, and \u2014 if you want the arena "
    "floor \u2014 the Colosseum Full Experience. These are the ones that punish a late booking (Decision 06)."),
   ("Weeks ahead", "If Pompeii is your day trip, reserve the high-speed train both ways \u2014 the late-afternoon returns "
    "fill up, and being stranded after a twelve-hour day is the failure mode (Decision 09)."),
   ("A week ahead", "Tell your bank you\u2019re travelling so your card isn\u2019t frozen, and confirm it\u2019s a no-foreign-"
    "transaction-fee card if you have one (Decision 07)."),
   ("A day or two ahead", "Reserve the standard Colosseum combined ticket and the Pantheon\u2019s timed entry \u2014 to skip "
    "the ticket line, not because they\u2019ll sell out (Decision 06)."),
   ("Before you pack", "Real walking shoes, broken in. Rome\u2019s sampietrini cobblestones are hard on feet and footwear, "
    "and this is a city you cross on foot \u2014 no fresh sneakers, no heels, no flimsy sandals."+EST),
   ("Book nothing for", "St Peter\u2019s Basilica \u2014 it\u2019s free, and its only queue is security, which no booking touches. "
    "Go early instead (Decision 05)."),
 ],
}

DAY_ZERO = {
 "title":"Day zero: the arrival",
 "sub":"The most anxious hours of the trip, and the ones nobody writes down.",
 "body":[
   ("The trip begins the moment the wheels touch at Fiumicino, jet-lagged and hauling luggage \u2014 not the ideal state "
    "for decoding fixed fares and train platforms, which is exactly why the airport transfer is the first place a little "
    "settled judgement pays off. Take the fixed-fare official taxi to a central hotel if you\u2019re two-to-four people with "
    "suitcases; take the Leonardo Express if you\u2019re light or sleeping near Termini (Decision 03). Either way, walk "
    f"past anyone who approaches you offering a ride and go to the marked official rank. {EST}"),
   ("Then do almost nothing. The single best first-day plan in Rome is to drop the bags, walk out the door of your "
    "central hotel, and let the walkable core do the work \u2014 no tickets, no schedule, no sight you\u2019ve committed to. "
    "Within a few blocks of a Centro Storico or Monti base you will pass a two-thousand-year-old temple, a Bernini "
    "fountain and a good espresso bar without trying, which is the whole argument for sleeping there. The Pantheon is "
    "free to enter and needs only a timed slot; the piazzas cost nothing at all. Save the booked, ticketed, sequenced "
    "sights for tomorrow, when you\u2019ve slept."),
   ("There is a real wonder in this first aimless evening, and it is part of what you paid for. The light goes gold on "
    "the travertine, the day-trippers thin out, and a city that read as a logistical problem on your laptop becomes, "
    "abruptly, the reason you came. Let day zero be that. The decisions in this book exist precisely so the rest of the "
    "trip needs no anxious improvising \u2014 which frees the first night to be spent, not planned."),
   ("Two practical notes keep day zero from souring. First, aim your arrival transfer at your hotel\u2019s neighbourhood, "
    "not at a landmark \u2014 give the driver the street address, and if you\u2019re on the Leonardo Express, know your onward "
    "hop from Termini before you land rather than working it out on the platform with bags. Second, if you arrive too "
    "early to check in, most central hotels will hold your luggage \u2014 drop the bags, don\u2019t drag them \u2014 and the "
    "walkable core means you\u2019re never more than a few minutes from a first espresso and a place to sit while the room "
    "is readied. The single thing that reliably ruins a first day is trying to sightsee seriously on no sleep; the "
    "single thing that saves it is permission to do almost nothing well. Take the permission."),
 ],
}

TIMING = {
 "title":"The rhythm of the week",
 "sub":"What closes, what strikes, and the one \u201cfree\u201d day that costs the most.",
 "body":[
   ("Rome\u2019s week has a texture worth knowing before it surprises you. Many kitchens and smaller sights keep their own "
    "rhythms \u2014 the Jewish Ghetto\u2019s kosher restaurants and the Boccione bakery close for Shabbat and Jewish holidays, "
    f"with shortened Friday hours {EST} \u2014 and the city\u2019s free state-museum Sunday, first of each month, is the single "
    f"busiest sightseeing day there is, with two-to-three-hour queues by mid-morning. {EST} Treat \u201cfree\u201d as \u201ccrowded\u201d "
    "and plan around it (Decision 06)."),
   ("Season is the larger rhythm, and for a first trip it\u2019s a mild decision rather than a fraught one. Late April into "
    f"early June, and September into October, are the ideal windows \u2014 warm, lively, and beautiful \u2014 at the cost of "
    f"peak crowds and higher prices. {EST} July and August are hot and busy; the ancient sites, unshaded, are genuinely "
    "punishing on stone at midday, which turns the early or late Colosseum slot from a nicety into self-defence. Winter "
    "is quiet, cool and cheap, with short queues and a city returned to Romans. None of this reshapes the trip the way "
    "the walk-time fact does; it adjusts the edges."),
   ("The daily rhythm matters more than the season, because it decides when the same sight is a pleasure or a scrum. "
    "The ancient core rewards the early start twice over \u2014 cool stone and thin crowds before the tour buses arrive \u2014 "
    "and the Vatican Museums reward it a third time, since a booked early slot walks in past a line that will run for "
    "hours by late morning. Midday, counter-intuitively, is when to eat and rest rather than sightsee: the sun is "
    "hardest on the unshaded ruins and the sights are at their fullest. Romans themselves shift the day late \u2014 dinner "
    "rarely before eight, the pre-dinner aperitivo bridging the gold-lit hours between \u2014 and a first-timer who moves "
    "with that rhythm rather than against it sees more and queues less. The single scheduling instinct worth keeping is "
    "to front-load the day and leave the afternoon soft."),
 ],
}

# ---- WHERE TO STAY: the assessments (feeds Decision 01, on identical criteria) ----
STAY = {
 "title":"Where to stay, assessed",
 "sub":"Five bases on the same three criteria \u2014 walk to the core, character, price.",
 "intro":("Decision 01 gives the call; this is the evidence behind it. Five bases first-timers actually weigh, each judged "
   "on the same three axes, with the walk-time to the core centre measured on foot. The rule beneath every line is the "
   "same: on a short first trip, minutes-to-the-core is worth more than square-metres-of-room."),
 "hoods":[
   ("Centro Storico", "13\u2032 to core", "The postcard Rome, and the default for a first trip that can afford it. Step "
    "out near the Pantheon or Navona and you rarely need transport; it\u2019s the most atmospheric and most convenient base "
    "for the classic sights. The trade is price and small, sometimes noisy rooms. You are paying purely for location, "
    "and on three or four days it is usually worth it."),
   ("Monti", "13\u2032 to core", "The value pick that gives up almost nothing. Tucked between the Colosseum and Termini, "
    "Monti is a genuinely local quarter of wine bars and narrow lanes, central enough to walk to the Forum, with more "
    "personality and better prices than the tourist core. Lively in the evenings \u2014 ask about the room\u2019s position if "
    "you sleep light. For most first-timers weighing cost against location, this is the sharpest answer."),
   ("Trastevere", "20\u2032 to core", "The base for travellers who rank evenings and food above proximity to the ruins. "
    "The cobbled, ivy-draped quarter across the Tiber is the Rome people fall for, and the standout for a classic "
    "dinner. The cost is a bridge between you and most mornings\u2019 sights \u2014 twenty minutes on foot to the centre \u2014 "
    "which is the right price only if atmosphere is what you\u2019re optimising."),
   ("Prati", "38\u2032 to core", "Calm, elegant and orderly, by the Vatican \u2014 the choice for a quieter, more residential "
    "base with good shopping and dining, if you don\u2019t mind sitting west of the historic core. It is the farthest of "
    "these from the walkable heart, so it suits a Vatican-focused trip or a traveller who wants evenings away from the "
    "crowds more than mornings inside them."),
   ("Near Termini", "28\u2032 to core", "The cheapest and best-connected base, and the one this book steers you away from "
    "for a first trip. Rome\u2019s densest, most affordable hotels and unbeatable transport \u2014 both metro lines, the airport "
    "train, onward rail \u2014 but the area is functional, not charming, and gritty in spots. It earns its place only for a "
    "trip built around serial rail day-trips, where the station on the doorstep outweighs the walk into the centre."),
 ],
 "fig":"hood_locators",
 "figcap":"The five bases as walk-time rings to the core centre: Centro Storico and Monti at 13 minutes, Trastevere at 20, Termini at 28, Prati at 38. The cheapest and \u201cbest-connected\u201d base is the farthest from what you actually walk to.",
 "tree_cap":"Where to sleep, as a decision: the only question that matters is whether you\u2019re here to walk. Everything else follows from it.",
}

# ---- THE PLAN: days as operations ----
PLAN = {
 "title":"The plan, as operations",
 "sub":"Not an itinerary of sights \u2014 the order-of-operations that keeps the days from colliding.",
 "body":[
   ("A first Roman trip has two unavoidable heavy half-days \u2014 the ancient core, and the Vatican \u2014 and the single most "
    "important scheduling rule is that they never share a day (Decision 04). Everything else arranges itself around that "
    "constraint. If you slept in the core, the ancient cluster is your doorstep morning and the Vatican is the cross-"
    "river expedition; the sequence writes itself."),
   ("A clean three-day shape: the first day is the walkable core on foot \u2014 Pantheon, piazzas, Trevi, Campo \u2014 with "
    "nothing booked, easing off the flight (Day Zero). The second is the ancient half-day, Forum first at opening, "
    "Colosseum on a midday slot, and a Roman dinner two streets off the monuments (Decisions 04, 08). The third is the "
    "Vatican \u2014 Museums on a booked early slot, St Peter\u2019s by timing not ticket, and an afternoon in Trastevere across "
    "the river (Decision 05). A fourth day, if you have it, is Ostia rather than Pompeii (Decision 09)."),
   ("The rule beneath the shape is to under-schedule on purpose. Three-to-four hours on ancient stone is genuinely "
    "tiring; the single largest museum in Rome is a morning in itself; and the walk home through the lit core at night "
    "is the part you\u2019ll remember. Leave the gaps. A first Roman trip fails far more often from cramming than from "
    "missing a sight \u2014 and the sight you skip is always there for the next visit the city has just talked you into."),
   ("If you have only two days, the shape compresses without breaking, because the two-half-days rule still holds. Day "
    "one becomes the ancient core in the morning \u2014 Forum at opening, Colosseum on a midday slot \u2014 and the walkable "
    "centre in the afternoon and evening, Pantheon and piazzas on foot. Day two is the Vatican on a booked early slot, "
    "St Peter\u2019s by timing, and Trastevere across the river for the last dinner. Everything that doesn\u2019t fit \u2014 the "
    "Borghese, a day trip, the dome climb \u2014 is what makes you come back, and the city is very good at making you come "
    "back. What you do not do, on two days or five, is fold the ancient core and the Vatican into one day to \u201csave\u201d "
    "the other for something else. That trade always costs more than it saves, because the thing it costs is the "
    "attention that made either sight worth seeing."),
 ],
 "fig":"ancient_flow",
 "figcap":"The ancient half-day, two valid orders. Forum-first buys cool, empty ruins early and saves the Colosseum\u2019s interior shade for midday; Colosseum-first beats the tour buses. Either way it is a half-day \u2014 and it never shares a day with the Vatican.",
}

# ---- FAILURE MODES: 20, organised BY CONSEQUENCE ----
FAILURE_MODES = {
 "title":"Failure modes",
 "sub":"Twenty ways a first Roman trip goes wrong, grouped by what it costs you \u2014 the view a shelf of articles can\u2019t give.",
 "intro":("A website of separate articles can tell you each of these once; only a book can line them up by consequence, so "
   "you see which mistakes cost the trip, which cost a day, and which merely cost money. That ordering is itself the "
   "product \u2014 read down to where your own anxieties sit."),
 "groups":[
   ("Costs you the trip, or a whole day", [
     ("Showing up unbooked at the Vatican, Borghese or Colosseum arena floor", "the sell-out sights; the one you flew for, gone. Book weeks ahead (Decision 06)."),
     ("Pairing Pompeii with anything else", "it\u2019s twelve hours door-to-door; stacking a second thing turns a great day into a wreck (Decision 09)."),
     ("Stacking the ancient core and the Vatican on one day", "three-to-four hours on stone plus the largest museum in Rome \u2014 a death march by four (Decision 04)."),
     ("Missing the last high-speed train back from a day trip", "the late-afternoon returns fill; pre-book both legs, especially the return (Decision 09)."),
     ("Choosing the first-Sunday \u201cfree\u201d museum day blind", "the busiest day of the month, two-to-three-hour queues; \u201cfree\u201d is not \u201ccheap\u201d once you price the hours (Decision 06)."),
   ]),
   ("Costs you money", [
     ("Answering the card reader in dollars", "dynamic currency conversion skims several percent, every time. Always euros (Decision 07)."),
     ("Buying a Roma Pass or Omnia \u201cto be safe\u201d", "if you\u2019re central and walking, the transport math is near zero and the pass doesn\u2019t pay (Decision 02)."),
     ("Tipping American-style", "staff earn a full wage; 20% doubles a light bill and marks you as a tourist. Round up (Decision 07)."),
     ("Paying a reseller\u2019s \u201cskip the line\u201d premium", "it\u2019s usually the official timed ticket plus a markup; buy direct (Decision 05)."),
     ("Using a Euronet ATM or an exchange desk", "worse rates by design; draw from bank ATMs and decline conversion (Decision 07)."),
     ("Taking an unofficial taxi at the airport or Termini", "the unsolicited offer is the classic unmetered overcharge; use the marked rank and the fixed fare (Decision 03)."),
     ("Booking the Omnia for a two-day trip", "it\u2019s 72-hour only \u2014 you physically cannot use the value (Decision 02)."),
   ]),
   ("Costs you a good meal, or marks you as a tourist", [
     ("Eating on the famous piazza", "prime sight-facing frontage pays with location, not cooking; walk ninety seconds off (Decision 08)."),
     ("Trusting the photo-menu and the tout at the door", "the reliable red flags; good Roman kitchens don\u2019t hustle (Decision 08)."),
     ("An unvalidated paper transit ticket", "counts as no ticket; on-the-spot €100+ fine. Tap a card, or validate without fail (Decision 02)."),
     ("Ordering cappuccino after dinner, or asking for big menu changes", "quietly outs you and sometimes gets worse food; espresso after meals."+EST),
     ("Sitting on the Spanish Steps", "banned and enforced \u2014 you\u2019ll be moved on or fined. A small cost, easily skipped."+EST),
   ]),
   ("Costs you comfort, or a base you\u2019ll regret", [
     ("Booking near Termini to save €30", "you spend the saving commuting into the core you came to walk (Decision 01)."),
     ("Wearing new shoes on the sampietrini", "the cobbles are hard on feet and footwear; broken-in walking shoes are non-negotiable (Before you fly)."),
     ("Renting a car for Rome itself", "the centre is restricted, the ZTL fines tourists automatically, and you\u2019ll walk everywhere anyway. Don\u2019t."+EST),
   ]),
 ],
 "fig":"failure_grid",
 "figcap":"The failure modes plotted by cost against avoidability. The book\u2019s targets are the upper-right: the mistakes that are both expensive and entirely preventable with one decision made in advance.",
}

WALLET = {
 "title":"The wallet card",
 "sub":"The whole book, compressed to what fits in a pocket. Print it; carry it.",
 "rows":[
   ("Reader asks dollars or euros?", "Euros. Always."),
   ("Tipping a meal?", "Round up / a euro or two. Never 20%."),
   ("Coperto on the bill?", "Normal cover charge. Not a tip."),
   ("Cash?", "Bank ATM, decline conversion. Small amounts."),
   ("Airport to a central hotel?", "Fixed taxi if 2\u20134 w/ bags; train if light."),
   ("Transit?", "Tap a contactless card. Skip the pass."),
   ("Eating near a sight?", "Walk 90 seconds off it."),
   ("Ancient core + Vatican same day?", "No. Separate half-days."),
   ("Must-book, weeks ahead?", "Vatican, Borghese, arena floor."),
   ("St Peter\u2019s?", "Free. Go early. Book nothing."),
   ("Spare day?", "Ostia (\u00bd day), not Pompeii (whole day)."),
   ("Where to sleep?", "In the core. Centro Storico or Monti."),
 ],
}

# ---- BACK MATTER: the refusals (the brand) ----
REFUSALS = {
 "title":"What this book won\u2019t tell you",
 "sub":"Four things we refuse to print \u2014 not from purity, but because faking certainty would cheat you.",
 "intro":("This book sells you reality: the real model behind the naive one, the connections the free web leaves scattered. "
   "A few things on offer everywhere else are not reality \u2014 they are false certainty that rots in a season \u2014 and "
   "printing them would quietly discredit everything else here. So we refuse them on purpose, and tell you why."),
 "items":[
   ("We won\u2019t name specific restaurants", "A named restaurant is a guess with a byline, wrong by spring and free "
    "anywhere. What outlasts it is the rule for spotting the right one \u2014 walk ninety seconds off the sight, look for a "
    "short Italian menu and locals after 8:30 \u2014 which we do give you (Decision 08). The rule works in a neighbourhood we\u2019ve never named."),
   ("We won\u2019t list hotels", "A hotel pick is stale in a season and we haven\u2019t slept in it. The decision that lasts is "
    "which area, and why \u2014 and that one we make, in full, on measured walk-times (Decision 01). Pick your own room inside the base we argue for."),
   ("We won\u2019t print current prices", "A price in a book is a lie with a publication date. Every live figure \u2014 fares, "
    "booking windows, the exchange reference \u2014 lives on the dated Field Sheet, so it can be right when you read it "
    "rather than right when we wrote it. When the two disagree, the Sheet wins."),
   ("We won\u2019t republish anyone\u2019s ratings", "Per-place scores are legally and editorially radioactive, and they "
    "encode a crowd\u2019s taste, not a method you can carry. We give you the method instead \u2014 the filters and the "
    "geography \u2014 so you can judge a room or a plate the city has never rated."),
 ],
}

CLOSING = {
 "title":"After the last tab",
 "sub":None,
 "body":[
   ("There is a moment, usually the second evening, when Rome stops being a problem to solve. You\u2019ve done the ancient "
    "morning and eaten well two streets off the Forum, and you\u2019re walking back through the lit core with nowhere you "
    "have to be. A fountain you didn\u2019t plan to see is running in an empty square. The city that lived in forty browser "
    "tabs is simply around you, and it is better than the tabs promised."),
   ("That evening is what all the deciding was for. The point of resolving the fifteen calls in advance \u2014 where to "
    "sleep, what to book, how to sequence, where to eat \u2014 was never the calls themselves. It was to buy back the "
    "attention those decisions would otherwise have eaten on the trip, and spend it here, on the thing you actually "
    "came for. Close the last tab. Rome is a kilometre and a half across, and now you know how to walk it."),
   ("What you carry out of this book is not a list of sights \u2014 the sights were never the hard part, and they\u2019re free "
    "to look up. What you carry is a way of seeing the city that makes it small: the knowledge that the core is "
    "walkable, that the metro is a distraction, that the traps cluster where the frontage is dear, that the famous "
    "day-trip is the wrong default, that the expensive \u201cskip the line\u201d skips a line you could beat with an alarm "
    "clock. Those aren\u2019t facts to memorise; they\u2019re a lens. Put it on, and Rome stops being forty tabs of "
    "contradictory advice and becomes what it is \u2014 a kilometre and a half of the most rewarding walking in the world, "
    "already yours to cross."),
 ],
}

# ---- FIELD SHEET (the dated annex; volatile figures only) ----
FIELD_SHEET = {
 "title":"The Field Sheet",
 "sub":"The volatile figures, dated. Everything that moves lives here, not in the Book.",
 "method":("Method: the figures below are the ones that change \u2014 fares, booking windows, an exchange reference. Verified "
   "values are marked as of their month; anything we could not verify at press time is listed as \u201cconfirm in your "
   "travel week,\u201d with the official source to check named. Never a blank cell. When the Sheet and the Book disagree, "
   "the Sheet is newer and wins."),
 "sections":[
   ("Getting in from Fiumicino", [
     ("Leonardo Express (non-stop to Termini)", "\u2248 €14 one-way, ~32 min, every ~15 min \u2014 confirm at trenitalia.com"),
     ("FL1 regional (Trastevere/Ostiense/Tiburtina, not Termini)", "\u2248 €8 \u2014 confirm at trenitalia.com"),
     ("Fixed-fare official taxi to inside the Aurelian Walls", "€55 flat, up to 4 (raised 2026) \u2014 posted at the rank"),
   ]),
   ("Passes & transit", [
     ("Single ticket (BIT, 100 min)", "confirm current fare \u2014 atac.roma.it"),
     ("Contactless daily fare cap", "auto-caps at the 24h pass price \u2014 confirm at atac.roma.it"),
     ("Roma Pass / Omnia Card price & inclusions", "confirm before buying \u2014 romapass.it / official Omnia site"),
     ("Unvalidated-ticket fine", "€100+ on the spot \u2014 validate paper, or tap a card"),
   ]),
   ("The sights that sell out", [
     ("Vatican Museums \u2014 booking window & fee", "sells out ~weeks in peak \u2014 tickets.museivaticani.va"),
     ("Borghese Gallery \u2014 mandatory timed slot", "book on sale \u2014 galleriaborghese.it"),
     ("Colosseum Standard & Full Experience", "Full Experience ~weeks, guided-only \u2014 colosseo.it"),
     ("Pantheon timed entry", "confirm current fee/slot \u2014 official Pantheon ticketing"),
     ("First-Sunday free-entry dates", "Domenica al Museo \u2014 confirm the month\u2019s date"),
   ]),
   ("Money", [
     ("USD\u2013EUR reference rate", "check in your travel week \u2014 a bank/FX source"),
     ("The rule that never moves", "at any reader, choose EUROS, never dollars"),
   ]),
 ],
}

# ---- THE SET PIECES: the unavoidable operations, each with its order-of-ops ----
SET_PIECES = {
 "title":"The set pieces",
 "sub":"Three operations every first trip runs \u2014 the Pantheon, the Vatican climb, the castle \u2014 done in the right order.",
 "body":[
   ("The Pantheon is the one that catches people twice \u2014 once with wonder, once with the ticket. Completed under "
    f"Hadrian around 126 AD and preserved because it was never abandoned but continuously used, it survives not as a "
    f"ruin but as a building: you walk in and stand under the same coffered dome the ancient Romans did, lit by the same "
    f"open oculus. {EST} What\u2019s changed recently is that it now charges admission and runs on timed entry, which blindsides "
    f"first-timers who remember it as the free marvel it long was. {OFF} Book the timed slot a day or two ahead (Decision 06); "
    "the visit itself rarely takes more than half an hour and lingers far longer than that."),
   ("There is a threshold moment here worth slowing down for, because anticipation is part of what you\u2019re buying. You "
    "step out of an ordinary Roman street, through the great bronze doors, and the space opens overhead into a perfect "
    "hemisphere with a hole of pure sky at its apex \u2014 rain falling straight through it onto the marble on a wet day, a "
    "shaft of hard sun tracking the floor on a bright one. Two thousand years of engineering resolve into a single "
    "quiet awe. Then you\u2019re back on the street with a gelato, and the city has done to you what it does."),
   ("The Vatican\u2019s two vertical set pieces reward knowing the logistics in advance. St Peter\u2019s dome is a genuine climb "
    f"\u2014 551 steps in total, with a lift that covers only the first stretch to the roof terrace and leaves the final "
    f"narrow, leaning spiral to your legs {EST} \u2014 governed by the basilica\u2019s dress code and security, so it pairs with, "
    "rather than interrupts, a St Peter\u2019s visit timed early (Decision 05). And Castel Sant\u2019Angelo, a short walk along "
    "the Tiber from St Peter\u2019s, is the natural afternoon companion to the Vatican morning: Hadrian\u2019s tomb turned "
    f"fortress, papal refuge, prison and now a museum crowned by one of the best rooftop views in Rome, linked to the "
    f"Vatican by the elevated corridor popes once fled along. {EST} Many visitors do the Vatican in the morning and the "
    "castle in the afternoon \u2014 which is exactly the half-day pairing the ancient core forbids with the Vatican, and "
    "invites here."),
 ],
 "fig":None,
}

# ---- EATING, deepened: the rule that outlives the list, plus what to order ----
EATING_ESSAY = {
 "title":"Eating: the rule that outlives the list",
 "sub":"Cucina povera, four pastas, and the coffee ritual that un-marks you as a tourist.",
 "body":[
   ("Roman food is not Italy\u2019s fanciest, and that is the point. This is cucina povera \u2014 \u201cpoor kitchen\u201d cooking built on "
    f"a handful of humble ingredients used brilliantly: pasta, cured pork cheek, sheep\u2019s cheese, black pepper, artichokes, "
    f"offal. {EST} The dishes are centuries old and Romans are fiercely protective of them, which is why the ninety-second "
    "rule of Decision 08 works so reliably: a kitchen two streets off the monument survives on locals who would notice a "
    "wrong carbonara, while the photo-menu on the piazza survives on tourists who won\u2019t return. Knowing what to order is "
    "the difference between tasting the actual city and eating a tourist-trap approximation of it."),
   ("Learn four pastas and you understand the cuisine. The Roman canon shares a common DNA \u2014 pecorino romano, guanciale "
    f"and black pepper \u2014 across cacio e pepe, carbonara, amatriciana and gricia. {EST} A real carbonara has no cream and no "
    "bacon; it\u2019s egg, pecorino, guanciale and pepper, and it is the dish Americans most often meet in a wrong version at "
    "home. Ordering these by name, in a room full of Romans, is both the better meal and the quiet signal that you\u2019ve "
    "done your reading."),
   ("Coffee and the pre-dinner hour are the two rituals that most quickly stop you reading as a tourist. Roman coffee is "
    f"a small strong espresso taken standing at a marble bar in thirty seconds for about a euro, often paid for first at "
    f"the register {EST} \u2014 no venti oat-milk latte on a park bench, and a cappuccino strictly before mid-morning. And "
    "aperitivo, roughly six to eight in the evening as the stone turns gold, is the civilised bridge into Rome\u2019s late "
    f"dinner: a spritz or a glass of wine with a few bites, as much social pause as drink. {EST} Both are cheap, both are "
    "pleasures, and both are the everyday texture the monuments can\u2019t give you."),
 ],
 "fig":"eating_rule",
 "figcap":"The ninety-second rule, drawn. Trap density falls off sharply within a short walk of any monument because the valuable, touristed frontage ends there \u2014 and the kitchens behind it survive on returning locals.",
}

# ---- WALKING THE QUARTERS: the texture that makes the walk a pleasure ----
QUARTERS = {
 "title":"Walking the quarters",
 "sub":"What each district actually feels like on foot \u2014 the reward for a city you cross by walking.",
 "body":[
   ("The walk-everywhere thesis only holds up because the walking is a pleasure, and it\u2019s a pleasure because the core "
    "isn\u2019t one uniform tourist zone but a string of quarters with distinct characters, each a short stroll from the "
    "next. Knowing their textures turns a transfer between sights into the best part of the day. The Centro Storico is "
    "the dense magical heart \u2014 the square mile where the Pantheon, Piazza Navona and the Trevi sit within a few "
    f"minutes of each other, and where you genuinely don\u2019t need a plan: step out and stumble onto a two-thousand-year-"
    f"old temple, a Bernini fountain and the perfect espresso bar within a single block. {EST} This is the Rome most "
    "first-timers picture, and the argument for sleeping inside it."),
   ("Cross a few streets and the register changes completely. Monti, tucked between the Colosseum and Termini, is a "
    "village inside the city \u2014 cobbled lanes, vintage boutiques, wine bars and artisan workshops, a five-minute walk "
    f"from the Forum and once ancient Rome\u2019s roughest district, the Suburra where Caesar reportedly grew up. {EST} Campo "
    "de\u2019 Fiori shows Rome\u2019s split personality in a single square: a centuries-old open-air market of fruit and flowers "
    f"by morning, one of the city\u2019s liveliest social hubs by night, a brooding statue of a burned philosopher over it "
    f"all. {EST} And the Jewish Ghetto, tucked between the Tiber and Campo de\u2019 Fiori, layers two thousand years into a "
    "few compact streets \u2014 one of the oldest Jewish communities in the world, a grand synagogue, ancient ruins, and a "
    f"distinctive Roman-Jewish cuisine you can taste nowhere else. {EST} It\u2019s often overlooked, which is exactly the "
    "reason to go."),
   ("Two quarters reward a deliberate trip rather than a stumble. Trastevere, across the Tiber, is the Rome of postcards "
    "\u2014 a maze of cobbled lanes and ivy-draped fa\u00e7ades that\u2019s wonderful by day and genuinely magical after dark, when "
    "the lantern-lit lanes fill with a slow tide drifting from aperitivo to dinner to gelato; crossing the river as the "
    f"sun goes down is the one evening every first-timer should keep. {EST} And Testaccio, south of the centre and off "
    "the tourist trail, is where Romans actually eat \u2014 a working-class quarter built around the old slaughterhouse, "
    f"which made it the heartland of the four classic pastas and the bold \u201cfifth-quarter\u201d offal cooking, with a "
    f"brilliant food market and barely a tourist in sight. {EST} Neither is a sight to tick; both are the texture that "
    "the monuments, for all their grandeur, cannot give you \u2014 and both are a walk, or one short hop, from a central "
    "base."),
 ],
 "fig":None,
}

# ---- DAY TRIPS, THE FULL MENU: extends Decision 09's day-cost logic ----
DAYTRIPS_MENU = {
 "title":"Day trips, ranked by the day they cost",
 "sub":"Decision 09 settled Ostia versus Pompeii; here is the rest of the menu, on the same logic.",
 "intro":("The principle from Decision 09 generalises: a day trip is worth it when the reward per hour-on-the-train is high, "
   "and Italy makes that easy because the trains are fast, frequent, and drop you in the town centre \u2014 you almost never "
   "need a car. Once you\u2019ve done the core, the Vatican and the piazzas, here is the honest ranking of what a spare day "
   "buys, cheapest-in-time first."),
 "items":[
   ("Ostia Antica", "~30 min each way, metro ticket", "The best short trip, covered in full at Decision 09: an entire "
    "ancient port \u2014 streets, mosaics, everyday Roman life \u2014 for half a day and a metro fare. If you have one spare "
    "half-day, this is it."),
   ("Castelli Romani", "~40\u201360 min, regional train", "The Romans\u2019 own countryside escape \u2014 volcanic hills, two crater "
    "lakes, hill towns and the crisp Frascati wine poured all over the city. A relaxed day of wine and lake views for "
    "travellers who\u2019ve had their fill of monuments, and refreshingly untouristed."),
   ("Orvieto", "~1 hr, direct train", "A golden-stoned Umbrian hill town on a plug of volcanic rock, crowned by one of "
    "Italy\u2019s most spectacular Gothic cathedrals, with an underground world of caves and a namesake white wine. Compact, "
    "walkable and easy \u2014 the perfect low-effort antidote to a few intense days in the city."),
   ("Tivoli", "~1 hr, train or bus", "Two spectacular and utterly different villas in a day: Hadrian\u2019s vast ruined "
    "country estate and the Renaissance fountain-garden of Villa d\u2019Este. One of the best escapes near Rome \u2014 it just "
    "needs a little planning, since the two sites sit apart and each deserves real time."),
   ("Pompeii", "~2 hr each way, ~12 hr door-to-door", "The greater site at the greater cost, dissected at Decision 09. "
    "Extraordinary, and a whole demanding day; right for the trip that can spare one, wrong as a squeeze on a short "
    "visit."),
   ("Florence", "~1.5 hr each way, high-speed", "Possible, and rarely ideal. High-speed rail makes a day trip genuinely "
    "doable and tempting for travellers who won\u2019t otherwise reach Tuscany \u2014 but Florence rewards far more than a rushed "
    "day, and doing it from Rome means a great city seen at a sprint. Go if it\u2019s your only chance; otherwise save it for "
    "its own trip."),
 ],
 "close":("The pattern rewards reading. The nearer, lower-key places \u2014 Ostia, the Castelli, Orvieto, Tivoli \u2014 give a "
   "genuinely restful day and a real taste of Italy beyond the capital for a modest slice of time. The famous, farther "
   "names \u2014 Pompeii, Florence \u2014 are extraordinary and expensive in exactly the currency a short trip is short of. On a "
   "first visit of three or four days, the honest advice is to resist the famous day-trip and take a near one, or none "
   "at all: Rome itself is not close to exhausted in four days, and the countryside will still be there for the trip "
   "the city has already convinced you to take."),
 "fig":None,
}
