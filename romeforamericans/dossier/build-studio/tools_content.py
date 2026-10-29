# -*- coding: utf-8 -*-
"""The hand-written half of the "Before you book" spread.

The checklist is GENERATED from each book's own verdicts (calls.json), so it can
never drift from the chapters. What cannot be generated is the part that turns an
argument into an action: the question you say out loud, and a trip with its
assumptions on the page. Those are written here, one entry per book, and every
one of them restates a call the book already makes rather than introducing a new
claim — the books name no businesses, and neither do these.
"""

# ── questions: (counterparty, [question, …]) ────────────────────────────────────
# ── trips: (title, assumptions, [(day-or-leg, what happens), …], why) ───────────

GREECE = dict(
    intro="Nine calls, in the order they bind. The page number is where each is argued.",
    qheading="What to ask, before you pay",
    qintro="Say these in these words. Every one of them settles something this book "
           "spends pages on, and none of them requires a name we refuse to print.",
    questions=[
        ("A ferry operator, or the aggregator", [
            "Is this sailing high-speed or conventional?",
            "If the meltemi cancels it, do I get a refund or a re-route — and which do you default to?",
            "Is there a later sailing the same day on any operator, or is this the last one?",
        ]),
        ("A hotel, before you book the room", [
            "How far is the port, and can I walk it with a suitcase?",
            "What is the difference in price between a caldera view and the room behind it?",
            "Is there a transfer, what does it cost, and where exactly does it meet me?",
        ]),
        ("A sunset cruise, if you take one", [
            "If the wind cancels, is it a refund or a credit for another evening?",
            "What time does it return to the harbour, and how do I get back up?",
        ]),
    ],
    tripheading="Two weeks that follow the calls",
    tripintro="Both are built from the nine calls and nothing else. The assumptions are "
              "stated because they are what makes the shape right; change one and the shape changes.",
    trips=[
        ("Ten nights, first visit, two islands",
         "Assumes: late May or late September; an open-jaw ticket is available; you want "
         "one famous island and one that is not; you are willing to pay for one flight.",
         [("Nights 1–2", "Athens. The buffer that protects the whole trip, and the Acropolis on a slot booked from home."),
          ("Nights 3–6", "Naxos or Paros. Four nights, one island — the book's ratio, not a tour's."),
          ("Nights 7–9", "Santorini, arriving by ferry while the light is still good."),
          ("Night 10", "Back to Athens — fly the long leg rather than sail it — and sleep near the airport."),
          ],
         "The last crossing is the one that can cost you the plane, so it is a flight, and the night "
         "before the flight is on the mainland. That is decision 01 and decision 07 doing their work."),
        ("Seven nights, one island, fewest moves",
         "Assumes: you would rather be somewhere properly than somewhere twice; peak season; "
         "a round-trip ticket into Athens.",
         [("Nights 1–2", "Athens, arrival buffer and the ancient core on foot."),
          ("Nights 3–6", "One island reachable by a short, frequent, conventional ferry."),
          ("Night 7", "Athens again, deliberately — the buffer at the other end."),
          ],
         "Two moves in a week instead of six. Decision 02 says this returns more than the island "
         "count suggests, and decision 06 says the moves are where the money goes."),
    ],
)

MOROCCO = dict(
    intro="Eight decisions, in the order you meet them. The page number is where each is worked.",
    qheading="What to ask, and who to ask it of",
    qintro="Morocco rewards the question asked before the transaction starts. Each of these "
           "closes one of the four leaks the money chapter names.",
    questions=[
        ("A riad, when you book — and again the week before", [
            "What is the total price of the airport transfer, in dirham, agreed now?",
            "Where exactly does the driver meet me, and what happens if my flight is late?",
            "Will someone walk me from the car to the door? (In a medina the car cannot reach it.)",
            "Is breakfast included, and is there anything else added at checkout?",
        ]),
        ("A guide, before you set off", [
            "Are you licensed, and may I see the badge?",
            "Am I paying you directly, and is the price for the whole morning?",
            "Are we going to any shops today?",
        ]),
        ("A driver, for the desert or an intercity leg", [
            "Is the price for the vehicle or per person, and does it include fuel and the driver's nights?",
            "How many hours is the drive, honestly, and where do we stop?",
        ]),
        ("A card terminal, every single time", [
            "Charge it in dirham, please — not dollars.",
        ]),
    ],
    tripheading="Two trips the book would actually endorse",
    tripintro="Both run on the Marrakech–desert–Fez line the sequence chapter argues for. "
              "The assumptions are on the page because they decide the shape.",
    trips=[
        ("Seven days, one way, with the desert",
         "Assumes: an open-jaw ticket into Marrakech and out of Fez; you want the dunes rather "
         "than the nearer sand; spring or autumn.",
         [("Days 1–2", "Marrakech. Jemaa el-Fnaa from a rooftop first, then from within."),
          ("Days 3–5", "Merzouga by private driver — three days, two nights, because the extra night is the point."),
          ("Days 6–7", "Fez. A licensed guide on the first morning, paid by you, which turns the maze into a city."),
          ],
         "One direction, no backtracking, and the only long drive bought as content rather than transit. "
         "That is decision 03, decision 04 and decision 05 agreeing with each other."),
        ("Five days, no desert, two cities",
         "Assumes: you would rather see two cities properly than add nine hours of road; "
         "the train is running; you are flying in and out of the same airport.",
         [("Days 1–2", "Marrakech, with the set pieces taken in the order the places chapter gives."),
          ("Day 3", "Al Boraq to Fez — the dependable spine, booked days ahead, not months."),
          ("Days 4–5", "Fez, and the hammam on the second evening rather than the first."),
          ],
         "The desert is not a side trip you slot in; refusing it is a decision, and this is what "
         "refusing it buys you."),
    ],
)

TURKEY = dict(
    intro="Seven decisions, in the order they bind. The page number is where each is reasoned.",
    qheading="What to ask, before the money moves",
    qintro="Each of these gets you a figure the published record does not carry. That is the "
           "whole reason to ask out loud rather than look it up.",
    questions=[
        ("Your insurer, before you buy the policy", [
            "Is this cover primary, or secondary to my card and my health plan?",
            "Do you direct-bill hospitals in Turkey, or do I pay and claim?",
            "Is a balloon flight excluded, and is a hired scooter or car excluded?",
        ]),
        ("Your card issuer, before you fly", [
            "What do you charge on a foreign ATM withdrawal — a flat fee, a percentage, or both?",
            "Which number do I call from abroad if you freeze the card, and does it take collect calls?",
            "Have you a travel notice on file, and does it expire?",
        ]),
        ("A rental desk, at the counter and in writing", [
            "What is the minimum age, the minimum licence-holding period, and the deposit?",
            "Does the card have to be in the driver's name, and does it have to be a credit card?",
        ]),
        ("A seller, before any object presented as old", [
            "Is this an antiquity, and can you give me an invoice that says what it is and how old?",
        ]),
    ],
    tripheading="Two shapes, with the risk priced in",
    tripintro="Neither is an itinerary of places. Both are shapes that put the fragile legs where "
              "a failure costs a day rather than the flight home.",
    trips=[
        ("Twelve days, Istanbul and two regions, flying internally",
         "Assumes: you want Cappadocia and the coast; you are willing to pay a little more for "
         "one ticket; a balloon morning matters to you.",
         [("Legs 1–2", "Istanbul, then the internal leg on the SAME ticket as the international one."),
          ("Middle", "Cappadocia, with the balloon on the FIRST available morning, not the last."),
          ("Last leg", "Coast, then the overland move immediately before the international return."),
          ],
         "The balloon goes early because weather cancels it and you want a second morning in hand. "
         "The overland leg sits where the schedule has most slack. Decisions I, III and VII."),
        ("Eight days, Istanbul only, no hire car",
         "Assumes: one city, properly; no driving, so no licence threshold binds; "
         "you would rather go deep than move.",
         [("Days 1–2", "Arrival, and the money arrangements made before anything else."),
          ("Days 3–6", "The set pieces on the order-of-operations the book gives, not the list order."),
          ("Days 7–8", "The Asian side, and whatever you decided you wanted more of."),
          ],
         "Removing the car removes decision III entirely, and removing the internal flight removes "
         "decision I. A short trip is shorter because of what it refuses."),
    ],
)

JAPAN = dict(
    intro="Nine decisions, in the order they get made. The page number is where each is worked.",
    qheading="What to ask, and what to say",
    qintro="Two of these are questions and two are sentences to say out loud. All four settle "
           "something this book spends a chapter on.",
    questions=[
        ("A ryokan, before you book the night", [
            "Is the rate per person or per room, and does it include dinner and breakfast?",
            "Do you accept guests with visible tattoos in the shared bath, and can a private bath be arranged?",
            "What time is dinner, and what is the last check-in?",
        ]),
        ("A hotel, when the station matters more than the room", [
            "Which station are you closest to, how many minutes on foot, and which line is it on?",
        ]),
        ("At a counter with no English menu", [
            "“Osusume wa nan desu ka?” — what do you recommend? Then order that.",
        ]),
        ("At a card terminal, anywhere", [
            "Charge it in yen, please — decline the dollar conversion.",
        ]),
    ],
    tripheading="Two trips, with the pass arithmetic done",
    tripintro="The rail-pass question is settled differently in each, and that is the point: "
              "the answer follows the route, never the other way round.",
    trips=[
        ("Nine nights, Tokyo and Kyoto, no rail pass",
         "Assumes: an open-jaw ticket in via Haneda and out via Kansai; late November; "
         "you would rather do less well than more badly.",
         [("Nights 1–4", "Tokyo, on the Yamanote loop. One anchor a day, loose afternoon."),
          ("Night 5", "One long leg to Kyoto — the only one of the trip."),
          ("Nights 6–8", "Kyoto, on a bus corridor, two major temples a day and something unlike them between."),
          ("Night 9", "An onsen town, one night, then out through Kansai."),
          ],
         "One long leg against a pass that needs about four. Buying the pass here costs money and "
         "then bends the route to justify itself. Decision 02."),
        ("Fourteen nights, three bases, pass worth checking",
         "Assumes: you have been before, or you have the appetite; you will take two day trips; "
         "you fly in and out of Tokyo.",
         [("Nights 1–5", "Tokyo, with one committed day trip — ten days or more is where a day trip earns its place."),
          ("Nights 6–10", "Kyoto, with one day trip, and the famous temple at opening."),
          ("Nights 11–13", "A third base reached by a long leg, not a day trip."),
          ("Night 14", "Back to Tokyo for the flight — the second long leg."),
          ],
         "Now count: two long legs plus the return. Divide the pass price by a Tokyo–Kyoto fare and "
         "see whether you reach four inside one seven-day window. Often you still do not."),
    ],
)

THAILAND = dict(
    intro="Eight decisions, in the order they get made. The page number is where each is worked.",
    qheading="What to ask, before you are standing there",
    qintro="Each of these is the question that stops a decision being made for you at a counter, "
           "a desk, or a dive shop.",
    questions=[
        ("Your insurer, before you buy", [
            "Do you direct-bill hospitals in Thailand, or do I pay and claim it back?",
            "Does this cover evacuation from an island to the mainland, and to what limit?",
            "Is riding a motorbike covered, and does that require a motorcycle endorsement on my licence?",
        ]),
        ("A hotel, when the island has no road network", [
            "How do I get from the pier to you, is it arranged, and what does it cost?",
            "Is the last boat of the day before or after my flight lands?",
        ]),
        ("A transfer or boat operator", [
            "If the flight is late, does the boat wait, or do I buy the next one myself?",
            "Is this one ticket end to end, or three tickets that happen to be sold together?",
        ]),
        ("A card terminal, every time", [
            "Charge it in baht, please — decline the dollar conversion.",
        ]),
    ],
    tripheading="Two trips, counted in moves",
    tripintro="Both are counted the way decision 02 counts: by moves, not by islands. "
              "The assumptions decide which one is right for you.",
    trips=[
        ("Ten nights, Bangkok and one serviced island",
         "Assumes: first trip; cool dry season; you want a beach but not a project; "
         "you would rather not ride anything.",
         [("Nights 1–3", "Bangkok, near Asok, and stop deciding — the rail line matters more than the room."),
          ("Nights 4–9", "One serviced island: one flight, one road transfer, about half a day door to door."),
          ("Night 10", "Back to Bangkok the day BEFORE the flight, not the morning of."),
          ],
         "Two moves. The buffer night exists because decision 04 says the leg that fails is the one "
         "you have to buy twice."),
        ("Fourteen nights, Bangkok and an un-serviced island",
         "Assumes: you have time to spend on transit; you accept three legs each way; "
         "you have checked the licence question before you touch a scooter.",
         [("Nights 1–3", "Bangkok."),
          ("Nights 4–11", "The quieter island — flight, road transfer, boat, each on its own timetable."),
          ("Nights 12–14", "Back with two clear days in hand, not one."),
          ],
         "Three legs each way, separately booked, is four beach nights only if nothing slips. "
         "Decision 02 and decision 04 are the same decision seen from two ends."),
    ],
)

ROME = dict(
    intro="Nine calls, in the order they bind. The page number is where each is argued.",
    qheading="What to ask, before you pay",
    qintro="Every one of these settles something this book spends a chapter on, and none "
           "of them needs the name of a business we refuse to print.",
    questions=[
        ("A hotel, before you book the room", [
            "Which quarter is this in, and how many minutes on foot to the Pantheon?",
            "Is there a lift, and which floor am I on?",
            "Can you hold luggage before check-in and after checkout?",
        ]),
        ("A taxi at Fiumicino, before the doors close", [
            "Is this the fixed fare to the centre?",
            "Does that cover the bags and all of us?",
        ]),
        ("A restaurant, before you sit down", [
            "Is there a coperto, and how much is it?",
            "Is this the same menu that is posted outside?",
        ]),
        ("A card terminal, every single time", [
            "Charge it in euros, please — not dollars.",
        ]),
    ],
    tripheading="Two trips that follow the calls",
    tripintro="Both are built from the nine calls and nothing else. The assumptions are "
              "printed because they are what makes the shape right.",
    trips=[
        ("Three days, first visit, central base",
         "Assumes: you sleep inside the core; you have booked the timed tickets the moment "
         "your dates were firm; late April or September.",
         [("Arrival", "Fixed-fare taxi to the core. Bags dropped, then nothing scheduled."),
          ("Day 1", "The ancient core its own half-day, Forum at opening. Walkable centre after."),
          ("Day 2", "Vatican Museums on the official timed ticket; St Peter's early and free."),
          ("Day 3", "The quarters on foot, and whatever you decided you wanted more of."),
          ],
         "No transit pass, because a core address makes the network almost unnecessary — "
         "decision 01 and decision 02 are the same decision seen twice."),
        ("Four days, with the spare one spent well",
         "Assumes: the three days above went to plan; you would rather have a whole day "
         "somewhere real than half a day somewhere famous.",
         [("Days 1–3", "As above."),
          ("Day 4", "Ostia Antica: an entire ancient port for half a day and a metro fare."),
          ("Evening", "Back in the core for dinner ninety seconds off the sight."),
          ],
         "Pompeii is extraordinary and costs the whole day plus the travel. Decision 09 is "
         "about what a spare day is actually worth, not about which ruin is better."),
    ],
)

# ── fallbacks: what to do when the preferred move is not available ─────────────
# The review's phrasing: the books explain why well and finish how inconsistently.
# A plan with no fallback is finished only for the reader whose day goes right.
FALLBACKS = {
    'rome': ("When the plan does not survive the day", [
        ("Your Colosseum or Museums slot has gone",
         "Official timed tickets release on a fixed schedule and sell out; resellers do not "
         "create capacity, they resell it at a markup. Take the next available slot and move "
         "the day around it rather than paying twice for the same hour."),
        ("The queue at St Peter's is round the square",
         "It moves, and it is free. Go at opening or late in the afternoon; a paid ticket "
         "buys you nothing here, which is the whole point of decision 05."),
        ("The bill arrives larger than the menu implied",
         "It will be the coperto, and it is legal and posted. Ask before you sit, not after. "
         "A menu in six languages beside a sight is the thing decision 08 tells you to walk "
         "ninety seconds away from."),
        ("The driver says the fixed fare does not apply",
         "It applies between Fiumicino and the walled centre, and it is published. Agree it "
         "before the doors close; arguing at the destination is the position you do not want."),
    ]),
    'greece': ("When the plan does not survive the day", [
        ("The ferry is cancelled",
         "Take the refund only if there is a later sailing you can actually reach; otherwise take the "
         "re-route. Then move the buffer night forward rather than compressing the last island."),
        ("Your Acropolis slot is gone",
         "Slots are released sixty days out and sell through five to seven days ahead in summer. If none "
         "is left, take the Agora and the museum on the day you had planned, and the Acropolis on the "
         "first slot of your buffer morning."),
        ("The meltemi is up and you are on the wrong island",
         "Stop island-hopping. Fly the long leg to Athens if a seat exists, and treat the remaining "
         "nights as Athens nights — the buffer was always the point."),
        ("The caldera room is not what the photograph promised",
         "This is the one to accept rather than fix. The view is the product; a move mid-stay costs a "
         "day and rarely improves it."),
    ]),
    'morocco': ("When the plan does not survive the day", [
        ("Nobody is at the airport to meet you",
         "Do not take the first offer at the kerb. Call the riad from the arrivals hall — this is why the "
         "meeting point was agreed in writing — and wait inside."),
        ("The driver quotes a different price on arrival",
         "Pay the agreed figure and say so plainly. The agreement is the leverage; the argument at the "
         "end of a nine-hour drive is not."),
        ("The guide steers you into a shop",
         "Say you are not shopping today, and mean it. If it happens twice, the tour is over — you are "
         "paying him and can end it."),
        ("The train is full",
         "Second class on the next departure beats first class three hours later, and the coach is the "
         "honest fallback on any leg the train does not serve."),
    ]),
    'turkey': ("When the plan does not survive the day", [
        ("You miss the internal connection",
         "If it is on one ticket, the carrier owns it — go to the transfer desk, not the check-in queue. "
         "If it is on two, you own it, and the next seat you buy is the price of the saving."),
        ("The balloon is cancelled",
         "It is weather, not the operator. This is why it was booked for the first morning; take the "
         "second. If there is no second morning, take the refund rather than the standby."),
        ("Your card is frozen",
         "Use the voice channel you arranged before you left. A frozen card is not fixed by the terminal, "
         "the merchant, or a second attempt."),
        ("The rental desk refuses you",
         "It will be the age, the holding period or the card, and none of them is negotiable at a counter. "
         "The fallback is the intercity coach, which goes everywhere the car was going."),
    ]),
    'japan': ("When the plan does not survive the day", [
        ("The IC card will not load on your phone",
         "Buy a physical card at the station. It is the same card, it takes cash, and it takes ten minutes "
         "rather than an evening of troubleshooting."),
        ("The ryokan will not take you because of tattoos",
         "Ask for a private bath at booking, not on arrival. If the answer is no, the fallback is a "
         "different onsen town on the same night, not a different night."),
        ("You cannot get into anywhere to eat",
         "Go downstairs. A department-store food hall at seven in the evening is the reliable answer, and "
         "it is the one the eating chapter argues for anyway."),
        ("The temple day has stopped working",
         "Cut to two and put something that is not a temple between them. You are on day six; this is the "
         "expected failure, not a bad day."),
    ]),
    'thailand': ("When the plan does not survive the day", [
        ("Your flight lands after the last boat",
         "Sleep on the mainland and cross in the morning. A night in a pier town costs less than a "
         "chartered crossing and far less than a missed one."),
        ("A leg is late and the next is separately booked",
         "Nobody owns the gap but you. Buy the next departure rather than argue, and claim it later if "
         "your policy covers missed connection."),
        ("You are refused at a temple door",
         "It is the shoulders or the knees, and it is enforced at the entrance. The sarong in the day bag "
         "is the whole fix — buy one at the gate if you did not bring it."),
        ("The scooter is the only way to get around and you have no endorsement",
         "Then it is songthaews and walking for the week. Riding without the entitlement your policy names "
         "is the one failure on this list that is not about a day."),
    ]),
}

for _b, _f in FALLBACKS.items():
    locals()[_b.upper()]['fbheading'], locals()[_b.upper()]['fallbacks'] = _f


BOOKS = dict(rome=ROME, greece=GREECE, morocco=MOROCCO, turkey=TURKEY, japan=JAPAN, thailand=THAILAND)
