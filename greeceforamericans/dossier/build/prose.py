# -*- coding: utf-8 -*-
"""prose.py — the opening, the essays, the surrounding chapters, the Field Sheet.

Voice: Economist/Monocle — calm, declarative, no enthusiasm. The synthesis is the
author's (unmarked); the corpus's hard facts carry a mark, once each, at sentence end.
Every chapter is a FLOW section with an endmark; figures sit inside the prose.
"""

# ---------- OPENING (the contract) ----------
OPENING = dict(
   id="open", eyebrow="GREECE FOR AMERICANS · MELTEMI PRESS",
   q="A book you can disagree with and still come out ahead.",
   standfirst="This is not a list of the best islands. It is the reasoning behind a first trip, so the calls are yours, made with the meter in view.",
   body=[
     ("p","<span class='dropcap'>M</span>ost Greece guides answer a question you can answer yourself in an afternoon of open tabs: where should I go, where should I eat, what should I see. The tabs are free and they are endless, and six weeks before a trip they are the problem, not the solution. What no single article does, because each is written alone, is hold the whole trip in mind at once and tell you how the pieces constrain each other. That connection is what this book is for."),
     ("p","So this is a decision manual, not a guidebook. Its unit is the call rather than the attraction: the order of the islands, the number of nights, the boat for the leg, the room to book and the one to skip. Each call is argued in the open, with the facts it rests on and the reasoning laid beside them, so that where your trip differs from the assumed one — a honeymoon, a family, two weeks not one — you can re-run the logic yourself and land somewhere we didn't send you. A book you must obey is worth less than one you can argue with."),
     ("p","One promise and one refusal frame everything that follows. The promise: every hard fact here traces to something greeceforamericans.com published, and carries a mark telling you how solid it is. The refusal: no live prices, no named hotels, no restaurant lists — the things that rot in a season and that you can get, free and current, anywhere. What this book sells is the part that doesn't expire: the shape of the trip, and the calls that shape forces."),
   ],
)

# ---------- HOW TO READ ----------
HOWTO = dict(
   id="howto", eyebrow="HOW TO READ THIS",
   q="The marks, the two documents, and using this on the trip.",
   standfirst="Two things carry the book's honesty: a mark on every sourced fact, and a hard line between what lasts and what changes.",
   body=[
     ("p","<span class='dropcap'>E</span>very factual claim in this book carries a provenance mark — a small signal of how much weight it can bear. They are seasoning, not decoration: most sentences here are reasoning, which is the author's and unmarked. Only the hard facts underneath the reasoning are marked, once each. The four you will see:"),
     ("marks", None),
     ("p","Where that reporting comes from: this book is built from the eighty articles published on greeceforamericans.com &mdash; the same desk, not an outside authority. Sentences in quotation marks are verbatim from those pages, and the figures the book passes on were reported there first. Every one of those articles is listed at <b>greeceforamericans.com/sources</b>, with the date it went up and, where someone has re-read it against its sources, the date that happened &mdash; so any marked claim here can be traced to the page it came from. Where a claim rests on something else &mdash; a port authority's published schedule, a government advisory &mdash; the line names that source itself."),
     ("p","The second structural choice is the two-document split. This <em>Book</em> holds what ages slowly — the geography, the sequencing logic, the decisions. It never prints a live price, because a price in a book is a lie within a season. The dated figures — this year's fares, schedules, opening hours — live in the <em>Field Sheet</em>, a short companion you check in your travel week. When the Book and the Sheet disagree, the Sheet is right; it was updated more recently. The Book tells you <em>which</em> ferry decision to make and why; the Sheet tells you what it costs this Tuesday."),
     ("p","On the trip itself: read the decisions before you book, not after you land — most of them are choices you make from home, weeks out. Carry the Field Sheet, not the Book. And treat the failure-modes chapter as a pre-flight checklist rather than bedtime reading; it is organised by consequence, so you can scan for the mistakes that cost the most."),
   ],
)

# ---------- THE GROUND (organising fact essay) ----------
GROUND = dict(
   id="ground", eyebrow="II · THE GROUND",
   q="Greece is a network with one deadline.",
   standfirst="The single fact that reorganises a first trip: you are not visiting islands, you are routing across water toward a plane that will not wait.",
   body=[
     ("p","<span class='dropcap'>H</span>ere is the mental model to arrive with, because it is not the one most first-timers bring. A Greek island trip is not a collection of destinations you assemble like a shopping list. It is a route through a transport network — ferries, a few domestic flights, one immovable transatlantic departure — and the network has properties that decide your trip whether or not you attend to them. Distance, frequency, and weather are not trivia here. They are the terrain."),
     ("p","Our own reporting names the central mistake without hedging: \"the single most common first-timer mistake is trying to see too many islands.\" <span class=\"mk stb\">◆ STABLE</span> But that is the symptom. The cause is treating a network as a list — assuming that because two islands are both \"in Greece,\" moving between them is cheap, when in fact each move costs a half-day of logistics and exposes you to a boat that might not sail. The list-thinker plans five islands and gets five airports. The network-thinker plans two or three and gets Greece."),
     ("fig","arrival"),
     ("p","Three network facts do most of the work, and every decision in this book is one of them applied. <em>Distance</em>: the Cyclades are close to each other but not to Athens or to Crete — Paros and Naxos are twenty kilometres apart while Santorini is well over two hundred from Piraeus. <span class=\"mk est\">● STRUCTURAL</span> <em>Frequency</em>: islands in the same group connect often and reliably; the far ones connect less. <em>Weather</em>: the summer meltemi wind cancels the fast boats that a rushed plan depends on, and it cancels them most cruelly on your last, most expensive leg."),
     ("p","Hold those three and the rest of the book is corollary. The order of the islands (put the fragile legs early); the number (the network taxes every move); the boat (match it to the leg and the weather); even where the money leaks (distance and weather are what you overpay to fight) — all of it falls out of one idea. You are routing, not collecting. Plan the trip as a route and the network works for you. Plan it as a list and it works against you, quietly, until the afternoon it takes your flight."),
   ],
)

# ---------- BEFORE YOU FLY ----------
BEFORE = dict(
   id="before", eyebrow="III · BEFORE YOU FLY",
   q="What to settle from home — every line with a deadline.",
   standfirst="The trip is mostly won or lost weeks out, at a keyboard. These are the things that cannot be fixed once you land.",
   body=[
     ("p","<span class='dropcap'>T</span>he entry rules for Americans are, for now, simple, but two of them wreck trips when ignored, and both are avoidable from home. First, the passport. Americans visit Greece and the wider Schengen Area visa-free for up to ninety days in any one-hundred-eighty-day period. <span class=\"mk off\">◇ OFFICIAL</span> But check both your passport's dates, issue and expiry, well before booking, because renewals take time and an expired-too-soon passport is the most common avoidable entry problem there is. This is a ten-minute check that saves a cancelled trip."),
     ("p","Second, the newer machinery. The EU's Entry/Exit System (EES) is replacing the old passport stamp with a biometric process — on entry, officials record your facial image and fingerprints along with your passport details. <span class=\"mk off\">◇ OFFICIAL</span> There is no fee and no advance action; just arrive with your biometric U.S. passport and allow extra patience at control on your first entry while your data registers. You may also have heard of ETIAS, a quick online pre-authorization. It is not in force, and the EU has not announced a launch date; you do not need one for this trip. If it launches before your trip, apply only through the official EU site — unofficial sites already charge inflated fees for it."),
     ("aside",("THE 90/180 TRAP","The ninety-day limit is Schengen-wide, not per country. Time in France, Italy, or anywhere else in the zone counts toward the same ninety days. For a two-week Greek trip this never binds, but if Greece is one leg of a longer European tour, count the whole zone, not just Greece.")),
     ("p","Beyond entry, the deadlines that matter are all about scarcity in peak season. Book the fixed points first — your Athens nights, your one or two island stays, the domestic flight if you're flying a long leg — because these sell out in July and August while the hops between them can wait. Pre-book harbour transfers on the islands where the port is far from the towns. And settle the ferry sequence itself before you book anything else, because the order decides everything downstream, and it is far easier to arrange from home than to repair from a hotel lobby with a cancelled boat behind you."),
   ],
)

# ---------- DAY ZERO ----------
DAYZERO = dict(
   id="dayzero", eyebrow="IV · DAY ZERO",
   q="The arrival day — the most anxious hours, and nobody writes them.",
   standfirst="You land jet-lagged into a hub you must transit, with a decision already waiting. Here is how the first day actually goes.",
   body=[
     ("p","<span class='dropcap'>M</span>ost first trips begin at Athens airport, because that is where the transatlantic flights land and where the onward journey to the islands begins — you pass through whether you planned to or not. <span class=\"mk est\">● STRUCTURAL</span> The anxious question of the first hours is not \"what do I see\" but \"how do I get from this airport to my first island without wasting the day I just crossed an ocean to reach.\" The answer depends on a fork you should have decided weeks ago, but which becomes real the moment you clear customs."),
     ("p","If your first island is a near Cyclade reached by ferry, the route runs through the port of Piraeus — roughly twenty to thirty minutes from central Athens by Metro, and the launch point for most island trips. <span class=\"mk stb\">◆ STABLE</span> The mistake here is trying to make a same-day ferry connection off a long-haul flight: a delayed plane, a missed Metro, a sold-out sailing, and you are stranded at the port overnight. Unless your flight lands early and your buffer is generous, give Athens the first night. You will see the Acropolis, sleep off the jet lag, and catch a rested morning ferry."),
     ("p","If your first island is far — Santorini, Crete — the same logic points to flying that leg, but the same caution applies to the timing. A forty-five-minute domestic flight to Santorini is the right tool, but a tight same-day connection off an international arrival is how a delay costs you the onward seat. The pattern that survives contact with jet lag and airport chaos is the same in both cases: land, take the first night in Athens, and start the islands on a fresh day with the whole morning ahead. Day Zero is not a day you travel far. It is the day you land safely and reset."),
   ],
)

# ---------- TIMING ----------
TIMING = dict(
   id="timing", eyebrow="V · TIMING",
   q="When to go, and the season most people get wrong.",
   standfirst="Peak season delivers the postcard and the crowd and the wind, all at once. The shoulder months quietly outperform on every axis that matters.",
   body=[
     ("p","<span class='dropcap'>T</span>he instinct is to go in July or August, because that is summer and summer is when you take a beach holiday. It is also when the famous sights are most crowded, prices are highest, and the meltemi wind is strongest — the exact months it most disrupts the fast ferries. <span class=\"mk stb\">◆ STABLE</span> Peak season stacks every disadvantage of a Greek trip into the same weeks and charges the most for the privilege. It is not wrong, but it is the setting on which every problem this book addresses is at its worst."),
     ("fig","season"),
     ("p","The shoulder months — May, June, September, October — are where the trip quietly improves on nearly every axis. The crowds thin noticeably while the weather stays warm and the sea stays swimmable; the sunsets stay gorgeous while the stadium-crowd feeling recedes; the wind is milder, so the ferries are more reliable and the exposed beaches more usable. <span class=\"mk sur\">▲ SURVEYED 06/25</span> For a honeymoon or any trip where the point is the place rather than the party, the shoulder season delivers the magic with far less of what spoils it, and at lower prices besides."),
     ("p","The one caution the shoulder season carries is at its edges: the further you push toward winter, the more that seasonal businesses on the smaller islands close, and schedules thin. Late October and beyond, some island infrastructure winds down. But within the shoulder proper, roughly May through early October, you are trading almost nothing for cooler crowds, calmer water, and a more forgiving ferry network. If your dates are flexible at all, this is the choice that buys the most in the whole trip, and it costs less, not more."),
   ],
)

# ---------- EATING ----------
EATING = dict(
   id="eating", eyebrow="VI · EATING",
   q="The rule that outlives any list of restaurant names.",
   standfirst="A named restaurant is a guess with a byline, wrong by next season. What lasts is the filter for finding the right one wherever you are.",
   body=[
     ("p","<span class='dropcap'>T</span>his book will not hand you a list of restaurants, and the refusal is a service, not a limitation. A specific restaurant recommendation is a data point that decays — under new management by spring, overrun once it's listed, or simply wrong for the village you're actually standing in. What doesn't decay is the rule for telling a good taverna from a tourist trap, and that rule is portable to every island and every year."),
     ("p","The filter is simple and it is consistent across our own reporting. Walk a few streets back from the harbour-front and the main square, where the rents are lower and the clientele is more local than transient. Read the menu for signals: fish sold by the kilo and vegetables that track the season suggest a kitchen buying fresh; a laminated menu in six languages with photographs suggests one buying tourists. Prefer the place full of Greek families at nine in the evening to the one with a host waving you in at seven. None of this is exotic knowledge — it is the same instinct you'd trust at home, applied somewhere the harbour-front is engineered to override it."),
     ("pull","A named restaurant is a guess with a byline. The rule for spotting the right one is the thing that travels."),
     ("p","On money and manners, two small corrections for American habits. Tipping is minimal here — rounding up is plenty, and the twenty-percent instinct is simply money left behind. <span class=\"mk stb\">◆ STABLE</span> And the sea-view table carries a sea-view markup; the same kitchen often serves the same dishes at a courtyard table a street inland for less. Eat where the food is, not where the view is, and save the view for the sunset you're not paying a cover charge to watch."),
   ],
)

# ---------- WHERE TO STAY ----------
STAY = dict(
   id="stay", eyebrow="VII · WHERE TO STAY",
   q="Which base, and why — the decision that doesn't expire.",
   standfirst="A hotel pick is stale in a season. The choice of which area, and what it buys or costs, outlives any specific room.",
   body=[
     ("p","<span class='dropcap'>W</span>e do not name hotels, for the same reason we don't name restaurants: the specific room rots, the reasoning lasts. What this book decides is the area — because on most islands the base you pick changes the trip more than the hotel does, and the area decision is one you can make from home with confidence that it will still be true when you arrive."),
     ("p","On Santorini the area decision is really the money decision, and it is the clearest case in Greece of paying for a view rather than a place. The caldera-rim villages — Oia, Imerovigli, Firostefani, Fira — carry a premium for the sunset-facing balcony; the inland villages and the beach towns return the same island, the same food, the same light everywhere but the room, for markedly less. <span class=\"mk stb\">◆ STABLE</span> If the caldera view from your own room is the point of the trip — a honeymoon, say — pay for it deliberately. If it isn't, sleep inland or at the beach and walk the rim at sunset like everyone else; the view is public."),
     ("p","On the quieter islands the calculus inverts: the towns are affordable enough that the base question becomes about character rather than cost. Naxos and Paros reward a base in or near the main town — walkable to dinner, well-connected to the beaches, close to the ferry hub for onward hops. The general rule across all of them: base yourself where the ferry leaves and the dinner is, not where the single famous beach is, because you'll want the beach once and the harbour and the tavernas every day. Proximity to the port also pays a specific dividend on your last island — it is what lets you make an early, low-stress connection toward the flight home."),
   ],
)

# ---------- THE PLAN ----------
PLAN = dict(
   id="plan", eyebrow="VIII · THE PLAN",
   q="The week, as operations — not an itinerary to obey.",
   standfirst="Not a day-by-day script but the load-bearing shape: where the fixed points go, and why the order is the one the network allows.",
   body=[
     ("p","<span class='dropcap'>A</span> classic first week resolves, on this reporting, to a shape rather than a schedule, and the shape is the same one every decision in this book has been building toward. Three nights in Athens to start: the on-ramp, the Acropolis, the jet-lag recovery, and the hub from which the islands depart. Then three to four nights on each of one or two islands, connected by the shortest reliable link the network offers, and a buffer night back near Athens before the flight home. <span class=\"mk stb\">◆ STABLE</span> That is the week. Everything else is which islands fill the slots."),
     ("fig","week"),
     ("p","The canonical version — Athens, then Santorini, connected by the forty-five-minute flight rather than a long ferry — works precisely because it respects the network. <span class=\"mk stb\">◆ STABLE</span> But note what the sequencing chapter demands you add to it: if Santorini is your island, it should not be your <em>last</em> stop before an international flight, because its links back are the far, fast-boat-dependent, weather-exposed kind. Fly out to Santorini early in the trip, or route back through Athens with a night's buffer. The pretty two-stop itinerary and the sequencing rule are not in tension; the rule just tells you which end of the trip each island belongs on."),
     ("aside",("THE OPERATIONS MINDSET","Plan the fixed points — Athens nights, island stays, the long-leg flight — and let the hops between them stay flexible. An itinerary scheduled to the hour breaks on the first cancelled ferry; a shape with slack in it bends and holds. The buffer night is not wasted time. It is the slack that keeps a bad-weather day from becoming a missed plane.")),
     ("p","For two weeks, the shape scales without breaking: add a second Cyclade or give Crete its own standalone week, but do not simply double the number of islands — that reintroduces the pacing trap at a larger scale. More time should buy more nights per island and more slack in the connections, not more airports. The trip that reads best is always the one with fewer moves and more room, whatever its length."),
   ],
)

# ---------- FAILURE MODES ----------
FAILURES = dict(
   id="failures", eyebrow="IX · FAILURE MODES",
   q="The mistakes, organised by what they cost.",
   standfirst="A website of articles can't do this: gather every way a first trip goes wrong and sort them by consequence, so you can guard the expensive ones first.",
   body=[
     ("p","<span class='dropcap'>T</span>his is the chapter no single article can write, because it requires holding the whole trip in view at once. Below are the recurring first-timer mistakes drawn from across our own reporting, sorted by what they cost rather than by topic — because a mistake that costs the trip deserves more of your attention than one that costs an afternoon. Read the first group before you book; the rest before you fly."),
     ("fig","failcost"),
     ("h2","COSTS THE TRIP (or a whole day)"),
     ("forlist_num", [
       "<b>Ending on Santorini before an international flight.</b> The far island, the fast-boat leg, the meltemi — every fragility stacked against the one deadline you can't rebook. End near Athens with a buffer night instead.",
       "<b>A tight same-day ferry off a long-haul arrival.</b> A delayed plane and a sold-out sailing strand you at the port. Give Athens the first night unless your buffer is generous.",
       "<b>No buffer night before the flight home.</b> One cancelled final crossing and you miss the plane. The buffer is the single cheapest insurance in the trip.",
       "<b>Booking the fast catamaran for a windy return leg.</b> It is the boat the meltemi cancels; the conventional ferry sails. You pay more to be stranded.",
       "<b>Passport too close to expiry.</b> The most common avoidable trip-wrecker. Check issue and expiry dates before you book.",
     ]),
     ("h2","COSTS REAL MONEY"),
     ("forlist_num", [
       "<b>A caldera-view room when the view isn't the point.</b> You're paying for a balcony, not an island. Sleep inland or beach; the rim is public at sunset.",
       "<b>Answering the \"charge in dollars?\" prompt with yes.</b> Dynamic currency conversion bakes in a worse rate. Always choose euros.",
       "<b>Tipping American percentages.</b> Rounding up is the norm; twenty percent is money left on every table.",
       "<b>Fast-ferry fares where flying is cheaper in time.</b> On the long crossings the flight saves a day; argue about ferries only on the mid-hops.",
       "<b>The sea-view table's markup.</b> Same kitchen, higher price for the view. Eat inland; watch the sunset for free.",
     ]),
     ("h2","COSTS THE EXPERIENCE"),
     ("forlist_num", [
       "<b>Too many islands.</b> Our own reporting's named top mistake. Four islands in a week is four airports and no island. Two or three, three nights each.",
       "<b>Peak season by default.</b> The crowds, the prices, and the wind all peak together. The shoulder months outperform on every axis if your dates flex.",
       "<b>Squeezing Crete into a hopping week.</b> It's a region, not a stop. Give it its own trip or leave it for next time.",
       "<b>The Oia sunset without a plan.</b> Arrive an hour early or watch the stadium-crowd shuffle. Better still, eat inland and skip the scrum.",
       "<b>Moving hotels every two nights.</b> The single-base trip with day-hops buys the same variety without the moving-day tax.",
     ]),
   ],
)

# ---------- BACK MATTER (the refusals — the brand) ----------
BACK = dict(
   id="back", eyebrow="X · WHAT THIS BOOK WON'T TELL YOU",
   q="The refusals are the product.",
   standfirst="Everything this book declines to do, it declines because doing it would sell you false confidence. The boundary is the brand.",
   body=[
     ("p","<span class='dropcap'>A</span> book is defined as much by what it refuses as by what it asserts, and this one refuses four things on purpose. Each refusal protects you from a specific kind of false certainty, and naming them is the most honest thing the book does."),
     ("p","<b>It won't name a hotel.</b> A specific hotel is stale within a season — new management, a slipped standard, a price that moved. What we make instead is the decision of which <em>area</em> to sleep in and why, and that decision doesn't expire. You leave with the durable thing, not a room number that might disappoint."),
     ("p","<b>It won't name a restaurant.</b> A named restaurant is a guess with a byline — overrun once listed, or simply wrong for the village you're in. The rule for spotting the right taverna anywhere, in any year, is what travels, and that is what we gave you."),
     ("p","<b>It won't print current prices.</b> A price in a book is a lie within a season. The live figures — fares, hours, schedules — live in the Field Sheet, dated and updated, where they belong. The Book carries only what doesn't move."),
     ("p","<b>It won't republish anyone's ratings.</b> Aggregated scores are someone else's data, legally radioactive to resell and editorially worthless once you can't see how they were made. We give you the reasoning to make your own call instead of laundering someone else's."),
     ("p","If any of that reads as withholding, invert it: what you were spared is four flavours of confident-but-wrong. What you keep is the part of the trip that stays true after the season turns."),
   ],
)

# ---------- CLOSING ----------
CLOSING = dict(
   id="closing", eyebrow="ENVOI",
   q="A last word — about the islands, not about us.",
   standfirst="",
   body=[
     ("p","<span class='dropcap'>T</span>here is a version of a first Greek trip that spends its whole energy fighting the network — racing between islands, chasing the famous sunset into a crowd, paying the premium for the boat that cancels — and comes home tired, having seen a great deal and rested in none of it. And there is another version, available for the price of a little planning from home, that works with the grain instead: fewer islands, more nights, the far ones early and the near ones last, a boat matched to its leg and a buffer against the wind."),
     ("p","The second trip is not the more expensive one or the more ambitious one. It is only the more deliberate one — the trip of someone who understood, before they booked, that they were routing across water toward a plane, and let that one fact put everything else in order. The islands reward it. The light on a whitewashed lane in the late afternoon, the ferry wake opening behind you toward the next harbour, a taverna table a street back from the water with the season's fish and no menu in English — these are what the network was in the way of, and what arrives once you stop fighting it. Greece, in order, is simply Greece with room to be enjoyed."),
   ],
)

CHAPTERS_BEFORE = [OPENING, HOWTO, GROUND, BEFORE, DAYZERO, TIMING]
CHAPTERS_AFTER  = [EATING, STAY, PLAN, FAILURES, BACK, CLOSING]
