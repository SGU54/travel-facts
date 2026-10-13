# -*- coding: utf-8 -*-
"""content.py — THE DECISIONS. The analytical heart (model.md).

Each decision clears the bottom-right cell: NON-OBVIOUS to a diligent amateur AND
HIGH-STAKES. Every hard fact traces to the corpus and carries a provenance mark;
the synthesis (the connective reasoning) is the author's and is unmarked. The
decisions are written as arguments, not filled into a template — they FLOW.

Provenance marks used in-book (VOLATILE stays on the Field Sheet):
  est = STRUCTURAL (geography, physics — doesn't change)
  stb = STABLE (the ordering / the rule holds; any figure lives on the Sheet)
  off = OFFICIAL (a published rule or advisory)
  sur = SURVEYED (our own dated observation)
"""

# Each decision: (id, number, eyebrow, question, standfirst, body_blocks, verdict, ledger, fig)
# body_blocks is a list of ("p", html) / ("h2", txt) / ("aside", (title, html)) / ("pull", txt)
# ledger is None or (header_cols, [(k, cells...)])
# fig is None or a (maps_fn_key, caption, fig_after) — placed inside the prose

def mk(**kw): return kw

DECISIONS = [

mk(id="d01", num="01",
   eyebrow="I · THE ONE THAT DECIDES THE OTHERS",
   q="In what order do you take the islands?",
   standfirst="The islands are not a set to collect. They are a route with one deadline, and only one direction survives a cancelled boat.",
   body=[
     ("p","<span class='dropcap'>E</span>very other decision in this book is downstream of this one, and almost no first-timer makes it deliberately. The instinct is to choose islands the way you choose a playlist — the famous ones, in any order, as many as the days allow. That instinct is what the ferry network quietly punishes. A Greek island trip is a sequence of water crossings ending in a fixed transatlantic flight home, and the sequence has a grain. Cut against it and a single windy afternoon takes not a beach day but the plane."),
     ("p","The mechanism is specific. The summer <span class='sc'>meltemi</span> wind disrupts or cancels Cyclades crossings, and it does so most reliably to the fast catamarans — the very boats a rushed itinerary leans on to make a tight connection. <span class=\"mk est\">● STRUCTURAL</span> A conventional ferry in moderate wind sails; the high-speed catamaran in the same wind stays in port. So the danger is not \"a ferry might cancel\" in the abstract. It is that your <em>last</em> crossing, the one with your flight behind it, is the one most exposed, if you let the itinerary put a fast-boat leg there."),
     ("fig","route"),
     ("p","This is why the order has a right answer and a wrong one. End your island run on the node with the most and earliest links back to Athens, and bank a night in Athens before the flight. Then a cancellation on your final hop costs you a hotel night you can absorb, not a plane you cannot rebook. End instead on the island that is farthest, thinnest-connected, or reachable only by the cancellable fast boat — Santorini is all three on its worst days — and you have placed the single most fragile leg of the trip against its single most expensive deadline."),
     ("fig","meltemi"),
     ("p","The corollary reorganises the whole map. Islands that sit close together with frequent connections — Paros and Naxos are twenty kilometres apart <span class=\"mk est\">● STRUCTURAL</span> — are the reliable middle of a trip; the famous-but-far ones belong early, when a lost day is only a lost day. The reader who internalises nothing else from this book should internalise the shape: <em>famous-and-far first, close-and-frequent in the middle, near-Athens last.</em>"),
   ],
   verdict=("The order is the insurance",
            "Sequence so your final crossing is short, frequent, and conventional — then a buffer night in Athens. Put the fast-catamaran legs and the far islands early, where the meltemi can only cost you a day. The flight home should sit behind a hop that sails in wind, not one that cancels in it."),
   ledger=("The last-leg test", "LAST ISLAND", "RISK ON THE FINAL HOP", [
       ("Athens (buffer night)", "None — you are already at the airport", "safe"),
       ("Paros / Naxos", "Frequent, short, conventional ferries", "low"),
       ("Mykonos", "Well-connected, but fast-boat dependent", "medium"),
       ("Santorini", "Far, fast-catamaran leg, meltemi-exposed", "high"),
   ]),
),

mk(id="d02", num="02",
   eyebrow="I · THE PACING TRAP",
   q="How many islands, and how many nights each?",
   standfirst="The most common first-timer mistake, in the words of our own reporting, is trying to see too many. The arithmetic of why is unforgiving.",
   body=[
     ("p","<span class='dropcap'>T</span>he honest ceiling is lower than anyone wants to hear: no more than two or three islands in ten days, and at least three nights on each. <span class=\"mk stb\">◆ STABLE</span> This is not a counsel of laziness. It is what the ferry timetable does to a day. A crossing is rarely just its sailing time. Add the pre-departure buffer the port demands, the transfer to and from each harbour, the check-out and check-in, and a \"quick hop\" between islands eats a half-day at each end. Two hops in a week and you have spent a full day of a seven-day trip standing in ferry queues."),
     ("fig","pace"),
     ("p","The visible cost is time; the hidden cost is that the islands blur. Three nights is the floor at which an island becomes a place rather than a photo stop — one full day to see the headline sight, one to do nothing in particular, which is the day people actually remember. Below three nights you are commuting, not travelling. The four-island itinerary that looks efficient on paper delivers four airports' worth of logistics and no island at all."),
     ("aside",("THE HALF-DAY RULE","Treat every island change as costing a half-day at each end — the buffer, the transfer, the two hotel desks. Budget it as lost time before you count nights, and the ceiling of two–three islands stops feeling arbitrary.")),
     ("p","There is a second base pattern worth naming, because it dissolves the problem entirely: give one island all your nights. A single-base trip — Naxos or Paros as a hub, day-trips by fast boat to its neighbours — buys the variety of hopping without the tax of moving hotels, and it removes the cancelled-connection risk from the middle of your trip. For a first visit, it is frequently the better trip and almost never the one people plan."),
   ],
   verdict=("Fewer islands, more nights",
            "Two or three islands in ten days; three nights minimum on each. When in doubt, drop an island rather than a night. A single-base trip with day-hops is the underrated option — all the variety, none of the moving-day tax, and no fragile connection in the middle of your week."),
   ledger=("What a week actually holds", "PLAN", "WHAT YOU GET", [
       ("2 islands, 3–4 nights each", "Two real places; time to rest", "good"),
       ("3 islands, ~3 nights each", "Workable; the pace is brisk", "ok"),
       ("4+ islands in a week", "Four transit days; no island", "bad"),
       ("1 base + day-hops", "Variety without moving hotels", "good"),
   ]),
),

mk(id="d03", num="03",
   eyebrow="II · THE MONEY LEAK NOBODY FLAGS",
   q="Fast ferry or slow, and when does the premium buy nothing?",
   standfirst="The fast boat costs more, cancels more, and on the routes that matter saves less than the fare implies. The slow boat is sometimes the sophisticated choice.",
   body=[
     ("p","<span class='dropcap'>T</span>he fast ferry is sold as the obvious upgrade and priced accordingly, and for most legs the premium is real time saved. But two facts the booking sites do not connect turn the default on its head. First, the fast catamaran is the boat the meltemi cancels; the conventional ferry in the same wind sails. <span class=\"mk est\">● STRUCTURAL</span> You are paying more for the vessel more likely to strand you. Second, the time saved is smaller than the fare gap suggests on exactly the routes a first-timer takes most."),
     ("p","Take the headline crossing. Piraeus to Santorini is roughly five hours by high-speed boat and eight by conventional. <span class=\"mk stb\">◆ STABLE</span> Three hours is worth paying for on the way out, when the day is ahead of you. On a short trip our own reporting is blunter still: fly that leg — forty-five minutes against five-to-eight hours by sea, a saved day for the price of a domestic ticket. So the fast <em>ferry</em>'s sweet spot is narrower than it looks: it is the middle-distance hop where flying isn't offered and the slow boat would cost a half-day, not the long haul (fly it) and not the short hop (the slow boat is barely slower)."),
     ("fig","flyferry"),
     ("p","The rule that falls out: match the boat to the leg, not the brand to the trip. Book the conventional ferry for your <em>return</em> legs and your weather-exposed legs — you trade an hour or two for a boat that actually sails. Spend the fast-boat premium only on an outbound middle-distance hop where the hours saved are hours of daylight you'll use. And on the long crossings to Santorini or Crete, stop arguing about ferries and check the flight."),
   ],
   verdict=("Buy speed only where it buys daylight",
            "Fast boat: outbound middle-distance hops only. Return and weather-exposed legs: the conventional ferry, which sails when the catamaran cancels. Long crossings (Santorini, Crete): fly — the saved day beats any ferry. The premium fast fare on a windy return leg is the worst ticket in Greek travel."),
   ledger=("The right boat for the leg", "LEG", "THE CALL", [
       ("Long crossing (Santorini/Crete)", "Fly — 45–60 min vs 5–9 h", "fly"),
       ("Mid-hop, good weather, outbound", "Fast ferry earns its premium", "fast"),
       ("Return leg / windy day", "Conventional ferry — it sails", "slow"),
       ("Short hop (Paros–Naxos)", "Any boat; slow is barely slower", "slow"),
   ]),
),

mk(id="d04", num="04",
   eyebrow="III · WHICH ISLANDS ARE WORTH YOUR WEEK",
   q="Santorini and Mykonos, or the islands that cost less and crowd less?",
   standfirst="The two famous names are famous for reasons that don't survive contact with July. The enthusiasm in our own reporting points somewhere quieter.",
   body=[
     ("p","<span class='dropcap'>T</span>he default first-timer pairing is Santorini and Mykonos, and it is defensible — once. Santorini's caldera is genuinely singular; Mykonos's beaches and night are real. But our own reporting is unusually candid about the cost of both. Santorini is \"famous for one thing — that sunset — but there's far more than standing in a crowd in Oia at 8pm,\" and the walk back from that sunset is \"a slow shuffle in a huge crowd.\" <span class=\"mk sur\">▲ SURVEYED 06/25</span> The famous islands deliver their postcard and, in peak season, a stadium to view it from."),
     ("p","Set against them, our own reporting reserves its warmest, least-hedged language for the islands most Americans have never heard of. Naxos: \"for first-timers who want an authentic, relaxed, beautiful island without the crowds or the cost, hard to beat,\" with \"the Cyclades' best beaches.\" Paros: \"stylish but unpretentious, beautiful but relaxed, and far better value than its famous neighbours,\" and the better ferry hub besides. <span class=\"mk stb\">◆ STABLE</span> When a body of reporting is measured about the famous places and effusive about the quiet ones, that asymmetry is data."),
     ("fig","santstay"),
     ("p","This is not an argument to skip Santorini. It is an argument about proportion and pairing. Give Santorini the shoulder-season visit and the early-or-late timing that its crowds require, and pair it not with a second expensive headline but with Naxos or Paros — the working, beautiful, affordable island that will be the part of the trip you didn't expect to love. The trip that reads best on this reporting is one famous island, handled well, plus one quiet one, given room."),
   ],
   verdict=("One headline, one hidden",
            "Pair a single famous island — Santorini, shoulder season, timed against the crowd — with Naxos or Paros, not with a second marquee name. The quiet island is cheaper, less crowded, and, by our own account, the one people come home talking about. Two headliners is the expensive way to be disappointed twice."),
   ledger=("Worth-it, by what you want", "IF YOU WANT…", "THE ISLAND", [
       ("The singular view (once)", "Santorini — shoulder season, timed", "yes"),
       ("Beaches + value + calm", "Naxos — best beaches, least fuss", "yes"),
       ("Style + a hub for hopping", "Paros — relaxed, well-connected", "yes"),
       ("Beaches + nightlife", "Mykonos — real, but pricey & windy", "ok"),
   ]),
),

mk(id="d05", num="05",
   eyebrow="III · THE ISLAND THAT ISN'T A HOP",
   q="Where does Crete fit, and why not in an island-hopping week?",
   standfirst="Crete is not a Cyclade with more sand. It is a region the size of a small country, and squeezing it into a hopping itinerary wastes it twice.",
   body=[
     ("p","<span class='dropcap'>C</span>rete breaks the mental model most first-timers arrive with, and our own reporting is emphatic about it: \"for first-timers used to thinking of Greek islands as small and hoppable, Crete asks for a different mindset.\" It is the largest Greek island by far, roughly 160 miles end to end, with a two-hour drive between its two main cities alone. <span class=\"mk est\">● STRUCTURAL</span> It is reached by a one-hour flight from Athens or a nine-hour overnight ferry — the distances alone tell you this is not a stop between beaches."),
     ("fig","crete"),
     ("p","The error is to append Crete to a Cyclades itinerary as \"one more island,\" giving it two or three nights. That buys you the airport and the transfer and almost none of the island. Our reporting's floor is four or five nights \"to justify the journey, ideally a week,\" with the island worked as one or two regional bases and day-trips out — not raced across. Its scale is a feature: it absorbs summer crowds better than a small island, and it holds mountains, gorges, and beaches a Cyclade simply doesn't have room for."),
     ("aside",("THE RULE","Crete is its own trip. Combine it with Athens and one Cyclade at most, or give it a standalone week. Pairing it with three hopping islands means you've booked two different kinds of holiday and done neither.")),
     ("p","So the decision is really a fork in what kind of trip you are taking. If you want the classic island-hopping week, leave Crete for another visit — it will still be there, and it rewards the trip built around it. If Crete is the draw, build the week around <em>it</em>: base in the west or centre, or split a week between two bases to cut the driving, and treat Athens as the bookend, not a co-star."),
   ],
   verdict=("Crete is a trip, not a stop",
            "Don't append Crete to a hopping itinerary. Either leave it for a visit of its own — a week, one or two regional bases — or make it the whole trip and bookend it with Athens. Two or three nights on Crete is the journey's cost with none of its reward."),
   ledger=("Fitting Crete", "YOUR TRIP", "WHERE CRETE GOES", [
       ("Classic Cyclades week", "Skip it this time — it deserves its own", "later"),
       ("Crete is the draw", "Whole week, 1–2 bases, Athens bookend", "yes"),
       ("Two weeks total", "One week Crete + one week Cyclades", "yes"),
       ("\"One more island\" (3 nts)", "The worst use of Crete", "no"),
   ]),
),

mk(id="d06", num="06",
   eyebrow="IV · WHEN AMERICANS OVERPAY WITHOUT NOTICING",
   q="Where does the money actually leak on a Greek island week?",
   standfirst="Not on the obvious lines. The leaks are structural — the caldera premium, the fast-fare-plus-cancellation, the currency prompt only Americans see.",
   body=[
     ("p","<span class='dropcap'>T</span>he Greek islands are not, by European standards, an extractive destination — this is not a place engineered to separate tourists from cash at every turn. The leaks are fewer and more specific than the anxiety suggests, which is exactly why they go unnoticed. The largest is not a scam but a preference sold back to you at a markup: on Santorini, the price is the view, not the island. <span class=\"mk stb\">◆ STABLE</span> A caldera-rim room in Oia or Imerovigli commands a premium that an inland village or a beach town a short drive away simply doesn't — for the same island, the same food, the same light everywhere but the balcony."),
     ("p","The second leak is the one this book has already named from the other side: the fast-ferry premium paid on a leg where it saves little and cancels much. Money and breakage are the same leak here — you pay more for the boat that strands you, then pay again to rebook. And the third is specifically American, and invisible to everyone else: the card reader that asks whether you'd like to be charged in dollars instead of euros. Always decline; \"dynamic currency conversion\" bakes in a worse rate than your card's own. <span class=\"mk off\">◇ OFFICIAL</span> The prompt is designed to be answered wrong by exactly the traveller this book is written for."),
     ("pull","Tipping is minimal — rounding up is plenty. The instinct to tip twenty percent is money left on every table."),
     ("p","The rest is small and self-correcting once seen: the airport-adjacent restaurant, the sea-view table with the sea-view markup, the transfer not pre-booked. None of these is large. Named together, they are the difference between a trip that feels expensive and one that doesn't, and not one of them requires giving anything up, only knowing where the meter is before you stand next to it."),
   ],
   verdict=("Know where the meter is",
            "The real leaks: the caldera-view premium (sleep inland or beach, visit the rim), the fast-fare-on-a-windy-leg double cost, and the dollars-or-euros prompt (always choose euros). Tip by rounding up, not by American percentages. None of it costs you the trip, but unwatched, it's the reason the week feels dear."),
   ledger=("The four leaks", "THE LEAK", "THE PLUG", [
       ("Caldera-view room", "Sleep inland/beach; visit the rim by day", "plug"),
       ("Fast fare on a windy return", "Conventional ferry — cheaper, sails", "plug"),
       ("\"Charge in USD?\" prompt", "Always choose euros — decline DCC", "plug"),
       ("20% tipping instinct", "Round up; that is the local norm", "plug"),
   ]),
),

mk(id="d07", num="07",
   eyebrow="III · THE HUB QUIRK THAT DECIDES YOUR HOPS",
   q="Ferry or domestic flight, and the island-to-island trap?",
   standfirst="The fly-or-ferry question has a clean answer by distance. But one quirk of the route map turns the obvious island-to-island flight into a mistake.",
   body=[
     ("p","<span class='dropcap'>T</span>he first-order rule is straightforward and worth stating plainly: for the short Cycladic hops, take the ferry — it is frequent, scenic, part of the experience, and faster door-to-door once you count airport time. For the long hauls — Athens to Crete above all — take the flight, because a one-hour flight beats a ferry of eight or nine hours. <span class=\"mk stb\">◆ STABLE</span> Match the mode to the distance and you get the best of both: the ferry where it shines, the plane where it counts. So far, so obvious."),
     ("p","The non-obvious part, the fact that costs people a wasted day, is the hub. Most Greek domestic flights route through Athens. <span class=\"mk stb\">◆ STABLE</span> There are few direct island-to-island connections, so flying from, say, Santorini to Mykonos is usually neither practical nor direct: you would fly Santorini&thinsp;→&thinsp;Athens&thinsp;→&thinsp;Mykonos, which takes longer and costs more than the ferry that goes straight across. The traveller who assumes \"I'll just fly between the islands to save time\" has assumed a route map that doesn't exist. Between two Cyclades, the boat is not the budget option — it is the fast one."),
     ("aside",("THE ONE EXCEPTION WORTH KNOWING","The seasonal island airports — Santorini and Mykonos especially — can feel crowded and chaotic at peak times, with tight security and limited facilities. Even when a flight makes sense (a long leg), arrive with real time to spare; the airport is not where you want your buffer to evaporate.")),
     ("p","So the decision resolves to a hybrid, and to one warning. Fly the long legs to and from Athens; ferry the short hops between neighbouring islands; and never plan an island-to-island <em>flight</em> as a time-saver, because it almost always routes the long way through the capital. The scenic ferry isn't the compromise here. On the hops that make up most of a Cyclades trip, it is simply the right tool, and the flight is the trap."),
   ],
   verdict=("Fly the long legs, ferry the hops",
            "Flights earn their place only on the long hauls to and from Athens (Crete above all). Between neighbouring Cyclades, the ferry is faster door-to-door and far more scenic, and the island-to-island flight you were tempted by routes the long way through Athens. Hybrid by distance; never fly a short hop."),
   ledger=("Mode by leg", "THE LEG", "THE MODE", [
       ("Athens ↔ Crete", "Fly — 1 h beats a 9 h overnight", "fly"),
       ("Athens ↔ Santorini (short trip)", "Fly — saves a day", "fly"),
       ("Neighbouring Cyclades hop", "Ferry — faster door-to-door, scenic", "ferry"),
       ("Island ↔ island by air", "Trap — routes through Athens", "no"),
   ]),
),

mk(id="d08", num="08",
   eyebrow="IV · THE MAINLAND YOU'D SKIP",
   q="How long in Athens, and is it worth the days?",
   standfirst="First-timers treat Athens as an airport with ruins attached and rush to the islands. Two or three days is the on-ramp that makes the rest of the trip work.",
   body=[
     ("p","<span class='dropcap'>T</span>he temptation is to minimise Athens — land, glimpse the Acropolis, flee to the islands the same day. It is a mistake on two counts. First, as the sequencing chapter showed, a same-day island connection off a transatlantic flight is how you lose a day to a missed boat; Athens is the buffer that protects the whole trip. Second, the city earns its keep: two or three days is the perfect on-ramp to Greece. <span class=\"mk stb\">◆ STABLE</span> The historic core is compact and walkable, with the Acropolis, the Agora, and the Acropolis Museum all within minutes of a central base."),
     ("p","The non-obvious operational calls are about the Acropolis, and they save both money and misery. Go at opening or in the late afternoon — timing is everything, and the midday combination of heat and crowds on unforgiving marble is the worst of both. <span class=\"mk sur\">▲ SURVEYED 06/25</span> And buy the combination ticket, which covers several ancient sites and is excellent value, but buy it at a <em>quieter</em> site than the Acropolis, because it lets you skip the Acropolis's own ticket line entirely. That single move, a combo ticket purchased at a lesser site, converts the longest queue in Athens into a walk-through."),
     ("fig","athens"),
     ("p","A third day, if you have it, is best spent on a day trip rather than on more city — the sunset temple at Cape Sounion, or the ancient oracle at Delphi — which breaks up the sightseeing and adds real variety and contrast to the trip's opening. <span class=\"mk stb\">◆ STABLE</span> For a base, the old quarter around the Acropolis is the most charming and walkable district and the easiest for first-timers. The through-line: Athens is not the part of the trip to compress. It is the on-ramp that makes the islands land right, and two or three deliberate days there is the setting the rest of the book assumes."),
   ],
   verdict=("Give Athens two or three days",
            "Not a same-day transit — the on-ramp. Base in the walkable old quarter; do the Acropolis at opening or late afternoon, never midday; and buy the combination ticket at a quieter site to skip the Acropolis line. A third day buys a day trip (Sounion or Delphi), not more city. Athens is the buffer that protects the whole trip."),
   ledger=("The Athens on-ramp", "IF YOU HAVE…", "THE MOVE", [
       ("2 days", "Acropolis + museum + old quarter, timed early", "core"),
       ("3 days", "Add a day trip — Sounion sunset or Delphi", "add"),
       ("The Acropolis line", "Combo ticket bought at a quieter site", "skip"),
       ("A same-day island dash", "Don't — take the buffer night here", "no"),
   ]),
),

mk(id="d09", num="09",
   eyebrow="IV · THE SIGNATURE EVENING, DONE RIGHT",
   q="The Oia sunset — how not to waste the one you came for?",
   standfirst="The most photographed sunset in Greece is also the most mobbed. The evening you pictured and the evening most people get are not the same, and the gap is entirely avoidable.",
   body=[
     ("p","<span class='dropcap'>T</span>he Oia sunset is the signature Santorini experience and it is genuinely beautiful — as the sun drops behind the caldera, the white village glows gold. <span class=\"mk sur\">▲ SURVEYED 06/25</span> It is also genuinely mobbed: the crowds gather along every wall and rooftop, and the walk back out afterward is a slow shuffle in a huge crowd. The default experience — arrive at eight, join the scrum, inch home in the dark — is the one that leaves people quietly deflated by the thing they most looked forward to. The fix is a plan, and our own reporting supplies three."),
     ("p","First, if you want the classic Oia vantage, treat it as an operation: arrive well before sunset — at least an hour, more in peak season — claim a spot, and be patient. The crowd is the price of that exact view, and the only way to pay it in comfort is to pre-empt it. Second, and better for many, find a quieter caldera-edge perch elsewhere: the sunset is visible from all along the rim, and a spot in Imerovigli or Firostefani, or a quiet wall away from Oia's main drag, trades the postcard framing for room to breathe and a walk home you don't have to queue for."),
     ("p","The third option removes the crowd entirely by changing your position: a sunset catamaran cruise watches the caldera glow from the water below, dinner and drinks included — a memorable and genuinely romantic alternative, and one to book ahead in season, since these fill. <span class=\"mk stb\">◆ STABLE</span> Whichever you choose, the broader rule holds for all the big-ticket Santorini sights: see them early or late to dodge the cruise-ship crowds that pour into Oia and Fira at midday. The island rewards the traveller who is counter-cyclical to the day-trippers, and punishes the one who arrives when they do."),
     ("fig","sunset"),
   ],
   verdict=("Have a sunset plan, not a sunset hope",
            "Three good moves, one bad one. Good: arrive an hour-plus early for the classic Oia spot; or take a quieter rim perch away from the main drag; or watch from a catamaran cruise below (book ahead). Bad: arriving at eight to join the mob and shuffle home. And see every big Santorini sight early or late — never midday, when the cruise ships land."),
   ledger=("Watching the sunset", "YOUR MOVE", "WHAT YOU GET", [
       ("Oia, 1 h+ early", "The postcard, earned with patience", "ok"),
       ("Quiet rim perch (Imerovigli)", "The same sun, room to breathe", "good"),
       ("Catamaran cruise (booked)", "The caldera from below, no crowd", "good"),
       ("Oia at 8pm, no plan", "The scrum and the shuffle home", "bad"),
   ]),
),

]
