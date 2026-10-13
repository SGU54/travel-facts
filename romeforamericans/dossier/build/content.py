# content.py — THE DECISIONS. Every ledger column labelled; every claim marked; every
# verdict losable. All ledes open differently — checked as a set.
E='<span class="mk est">●</span>'; O='<span class="mk off">◇</span>'
S='<span class="mk sur">▲ 07/26</span>'; V='<span class="mk vol">◆</span>'

DECISIONS=[
 dict(n="01",cat="Base",q="Where should you sleep?",cols="MIN TO THE PANTHEON",
  lede="Every evening around six the same migration crosses the city: visitors who saved "
       "thirty dollars a night beside the station, riding back into the centre for dinner, "
       "then out again at midnight. They pay the difference back in transit, in waiting, in "
       "evenings cut short — the one currency this trip runs on.",
  table_title="Six bases, one yardstick · walk to the Pantheon, computed from coordinates",
  rows=[
   (f"Centro Storico — postcards out the door; small rooms, night noise {E}","0′"),
   (f"Monti — central and characterful for less; the Forum a stroll away {E}","14′"),
   (f"Trastevere — the city's best evenings, with a bridge to cross each morning {E}","20′"),
   (f"Prati · Borgo — calm streets, the Vatican at your door, early nights {E}","20′"),
   (f"Testaccio — where Rome itself eats; light on sights {E}","30′"),
   (f"Termini · Esquilino — every train, most beds, least romance {S}","34′"),
  ],
  verdict="<b>The call</b>Pay for the centre. On a first visit the base is the trip: inside "
       "the ring, 'getting around' dissolves into the sightseeing, and the evening belongs "
       "to you. If the budget refuses, Monti keeps you central for less; choose Trastevere "
       "only when evenings outrank mornings, because you will cross that bridge twice a day. "
       "The station saves money and spends the holiday.",
  fo=["your budget carries a small central room → take it over a large distant one",
      "evenings, food and wandering are the point → Trastevere earns its bridge"],
  ag=["you land past midnight and leave at dawn → Termini's convenience is real",
      "a week or longer with kitchen ambitions → an apartment changes the arithmetic (Decision 02)"],
  note=f"{V} Room rates are the one number this book never prints — shop your dates; "
       "shoulder months move them most (Decision 03)."),

 dict(n="02",cat="Time",q="How many days does Rome need?",cols="DAYS",
  lede="Ask a Rome regular how long a first visit needs and the answer rarely varies: three "
       "days. Two cover the pillars — the ancient core and the Vatican. The third is where "
       "the city stops being a checklist and starts being the place people come back for.",
  table_title="What each day buys · first visit",
  rows=[
   (f"Triage — the icons at a march; no museum gets its due {E}","1"),
   (f"The two pillars — ancient Rome and the Vatican, each given a morning {E}","2"),
   (f"The city breathes — Borghese, the neighborhoods, the long lunch {E}","3"),
   (f"Depth or distance — a day trip without amputating Rome (Decision 14) {E}","4"),
   (f"Rhythm — big days alternating with gentle ones; downtime becomes real {E}","5–7"),
  ],
  verdict="<b>The call</b>Three days, and defend the third against your own itinerary. The "
       "fourth is the first optional day, and it buys more than any other single addition: "
       "either the Borghese at leisure plus a neighborhood afternoon, or one clean escape "
       "by rail. Past five, alternate heavy and light days or the monuments blur into one "
       "long stone corridor.",
  fo=["this is likely your one visit → four days, day trip included",
      "art is the reason you fly → the third day exists for the Borghese"],
  ag=["a 48-hour stopover → run days one and two only, and skip every pass (Decision 07)"],
  note=f"{V} Timed-entry supply, not stamina, caps a short trip — booking horizons on the "
       "Horizons page; live windows on the Field Sheet §2."),

 dict(n="03",cat="Season",q="When should you go?",cols="HEAT · CROWD · PRICE",
  lede="August 15 empties the city of Romans. Ferragosto sends the trattoria owner to the "
       "coast, shutters the family shops, and leaves the monuments standing in white heat "
       "for whoever remains. The calendar decides more of this trip than most people allow.",
  table_title="The year, in three pressures · darker months cost more of each",
  rows=[
   (f"Late April – May — the postcard season; everyone knows it {E}","MILD·FULL·HIGH"),
   (f"September – October — spring's equal, with warmer seas and softer light {E}","MILD·FULL·HIGH"),
   (f"June – August — survival mode: dawn starts, siesta, evening returns {E}","HOT·PEAK·HIGH"),
   (f"November – March — the quiet bargain; short days, some rain {E}","COOL·THIN·LOW"),
   (f"Easter week & the holidays — beautiful, mobbed, priced accordingly {S}","MILD·PEAK·PEAK"),
  ],
  verdict="<b>The call</b>Aim for the two windows — late April into May, or September into "
       "October — and accept that the pleasant months are the crowded ones; that trade is "
       "honest. If cost rules, winter is underrated: thin lines, low fares, the city to "
       "yourself by five. Never default into July or August; go then only on purpose, with "
       "the summer protocol (Timing chapter) already booked in.",
  fo=["flexibility exists → October is the connoisseur's pick",
      "budget leads → January and February, and pack for rain"],
  ag=["school holidays bind you → book the timed entries the day flights are bought (Decision 04)"],
  note=f"{V} Ferragosto closures, Easter dates and event surges move yearly — calendar "
       "notes, Field Sheet §3."),

 dict(n="04",cat="Booking",q="What must be booked before you fly?",cols="HORIZON",
  lede="At the Borghese Gallery the queue is short for the worst reason: there isn't one. "
       "No reservation, no entry — however far you flew, however empty the building looks. "
       "Rome's front doors have quietly become appointment-only, and the appointments sell "
       "out in a strict order.",
  table_title="The sell-out order · book from the top down",
  rows=[
   (f"Borghese Gallery — mandatory reservation, no walk-ins, small capacity {E}","WEEKS "),
   (f"Colosseum · Full Experience — guided slots only, smallest allocation {S}","WEEKS "),
   (f"Vatican Museums — timed entry; season sets the horizon {S}","DAYS–WEEKS "),
   (f"Colosseum · standard — the combined ticket; releases move {S}","DAYS "),
   (f"Pantheon — recently ticketed and timed; short horizon, real queue {O}","DAYS "),
   (f"Papal Audience — free, ticketed, Wednesdays; order ahead {O}","WEEKS "),
  ],
  verdict="<b>The call</b>Book four things the day the flights are bought: Borghese, "
       "Colosseum, Vatican, Pantheon — in that order, matched to days one, two and three "
       "(The Plan). Everything else in Rome can be decided over breakfast. A tour can "
       "substitute for a slot you missed; buying one at the door cannot.",
  fo=["your dates are fixed → there is no reason to wait a single day",
      "the Full Experience tempts you → it books first or not at all (Decision 08)"],
  ag=["you refuse fixed hours → travel in deep winter and carry the risk knowingly"],
  note=f"{V} Release windows and official sellers drift — current horizons and links, "
       "Field Sheet §2. One seller is official; the rest resell it {S}."),

 dict(n="05",cat="Arrival",q="Fiumicino to the centre — rail, flat fare, or the cheap seat?",
  cols="PLATFORM-TO-PLATFORM",
  lede="You clear customs into a corridor of murmured offers — 'taxi, taxi' — and the "
       "trip's first decision arrives before the jet lag lifts. The men soliciting are the "
       "one option with no fixed price; everything else about this choice is pleasantly "
       "mechanical.",
  table_title="Four ways in · times as published; fares live on the Sheet",
  rows=[
   (f"Leonardo Express — non-stop to Termini, every quarter-hour or so {S}","32′"),
   (f"FL1 regional — cheaper, but it skips Termini: Trastevere, Ostiense, Tiburtina {E}","≈30′"),
   (f"Taxi, fixed fare — flat to inside the walls, bags included; traffic decides {O}","45–60′"),
   (f"Shuttle bus — the cheapest seat, in the same traffic as the taxi {S}","45–60′+"),
  ],
  verdict="<b>The call</b>Default to the Leonardo Express: immune to traffic, indifferent "
       "to jet lag, and the fastest thing on the board. The flat-fare taxi wins for three "
       "or more people, a midnight landing, or luggage you regret — split, it competes; "
       "solo, it is a multiple of the train. Staying Trastevere or Testaccio, the FL1 "
       "delivers you closer than Termini ever will.",
  fo=["party of 3–4 → the flat fare divides into good value",
      "base in Trastevere → FL1 to your own station, then feet"],
  ag=["solo with one bag → the train, every time",
      "anyone soliciting in arrivals → the answer is no; the rank outside is regulated "+O],
  note=f"{V} All fares — train, flat taxi, bus — Field Sheet §1, verified at press time. "
       "Ciampino has its own flat fare and no rail; same logic, smaller numbers."),

 dict(n="06",cat="Transit",q="Do you need transit tickets at all?",cols="RIDES, TYPICAL DAY",
  lede="The most common transit mistake in Rome is a purchase, not a wrong turn. The city "
       "sells day passes, carnets and cards to visitors whose feet were already covering "
       "the distance — the metro cannot reach the places they came for.",
  table_title="Where rides really occur · walk-first base assumed (Decision 01)",
  rows=[
   (f"Inside the ring — the sights are a stroll apart; wheels lose to feet {E}","0"),
   (f"The Vatican leg — one hop if the bridge walk holds no charm that day {E}","0–1"),
   (f"Late return from Trastevere or Testaccio — tram or bus after dinner {S}","0–1"),
   (f"Airport legs — separate tickets either way (Decision 05) {E}","—"),
   (f"Day-trip rail — national trains, never city tickets (Decision 14) {E}","—"),
  ],
  verdict="<b>The call</b>Buy nothing in advance. Tap a contactless card at the gate for "
       "the odd ride and let the system's daily cap protect you — the pass math never "
       "starts. Two rules keep it clean: a paper ticket must be validated or it is a fine "
       "in waiting, and the 64 and 40 buses trade speed for the city's densest pickpocket "
       "traffic (Decision 13).",
  fo=["mobility is limited or the heat is on → ride freely; the cap still protects you"],
  ag=["you tallied real rides and the pass still wins → you are the Decision 07 case; run it"],
  note=f"{V} Single-fare price, validity minutes and the fine — Field Sheet §1. The tap "
       "system's daily cap: confirm it covers your card type before relying on it."),

 dict(n="07",cat="Passes",q="Roma Pass, Omnia, or neither?",cols="BREAKS EVEN WHEN",
  lede="Somewhere over the Atlantic a pass gets bought because it sounds comprehensive. "
       "The brochure arithmetic assumes a visitor who rides constantly and queues for "
       "attractions daily; the walk-first reader of this book is neither.",
  table_title="The pass shelf, against your itinerary — not the brochure's",
  rows=[
   (f"Roma Pass 48 h — transport + one covered sight {O}","1 SIGHT + HEAVY RIDING"),
   (f"Roma Pass 72 h — transport + two covered sights {O}","2 SIGHTS + HEAVY RIDING"),
   (f"Omnia 72 h — the above + Vatican entry + a bus tour, at a premium {O}","YOU WANTED THE BUS TOUR"),
   (f"Neither — pay per entry, tap per ride {E}","YOU WALK — THIS BOOK"),
  ],
  verdict="<b>The call</b>Neither, for the trip this book plans. The Vatican sits outside "
       "the Roma Pass entirely — a separate state, a separate ticket — and the walking "
       "thesis starves the transport half of its value. The 72-hour pass earns its keep "
       "only when the Colosseum plus two more covered sites and daily riding all appear "
       "on your list; the Omnia mostly sells a bus tour wrapped in confidence.",
  fo=["Castel Sant'Angelo and the Capitoline were coming anyway, by bus → run the 72 h math"],
  ag=["the Vatican is your centrepiece → no pass touches it; book direct (Decision 09)",
      "it 'sounds simpler' → simplicity is the product being sold, not delivered"],
  note=f"{V} Pass prices and the covered-attraction list shift — current figures, Field "
       "Sheet §2. Do the subtraction there in ink; it takes one minute."),

 dict(n="08",cat="Colosseum",q="Standard ticket, or the Full Experience?",cols="CONSTRAINT",
  lede="At the booking screen a fork appears: the ticket, or the ticket with two more rooms "
       "and a fixed hour attached. The upgrade is not a better view of the same thing — it "
       "is the arena deck under your feet and the machinery rooms below it.",
  table_title="Three tickets, one building · see the section drawing, Set Pieces",
  rows=[
   (f"Standard — the tiers, looking down; Forum and Palatine on the same admission {O}","FLEXIBLE · 24 H"),
   (f"Arena floor — the combatant's eye-line, up into the stands {E}","GUIDED SLOT"),
   (f"Underground — the hypogeum: cells, lift shafts, the backstage of the games {E}","GUIDED · SELLS FIRST"),
  ],
  verdict="<b>The call</b>First visit, three days, many claims on your hours: the standard "
       "ticket is the right one, and it is already a great visit. Buy the Full Experience "
       "when the building itself is why you flew and you can commit weeks ahead to a fixed "
       "guided hour — as theatre machinery and engineering, the underground rewards exactly "
       "that visitor and bores the box-ticker.",
  fo=["you plan weeks out and love the backstage → the hypogeum is the best ticket in Rome"],
  ag=["flexibility matters more than depth → standard, early slot, and keep your morning",
      "a man with a laminated badge offers to help → he is the markup (Decision 04)"],
  note=f"{V} Tier names, prices and the release window move — Field Sheet §2. The 24-hour "
       "combined validity held at press time {O}."),

 dict(n="09",cat="Vatican",q="The early slot or the late one?",cols="CROWD PRESSURE",
  lede="There are two quiet hours in the Vatican Museums each day, and they sit eight hours "
       "apart. Between them moves a tide of tour groups that no ticket class outruns — "
       "timing, not spending, is the lever.",
  table_title="One day at the Museums · pressure by hour, as observed",
  rows=[
   (f"Opening slot, T−25 for security — the Sistine before the murmur {S}","LOW"),
   (f"Late afternoon — the groups drain out; extended evenings when offered {S}","LOW"),
   (f"Mid-morning to lunch — the tide at full height {S}","PEAK"),
   (f"Wednesday morning — the Papal Audience fills the square; Museums run, basilica waits {O}","SQUARE FULL"),
  ],
  verdict="<b>The call</b>Book the first slot of the day and arrive twenty-five minutes "
       "early — security screens everyone and no ticket skips it. The late-afternoon slot "
       "is the underrated equal for anyone allergic to alarms. Walk the route with intent "
       "to the Raphael Rooms and take the Sistine at the end, where it belongs; the "
       "basilica afterward through its own line, dressed to code.",
  fo=["you would rather sleep → the last two hours are the same museum, calmer"],
  ag=["Wednesday is your only day → see the Audience or skip the basilica till afternoon",
      "a dome climb tempts → 551 steps; the lift erases only 230 of them "+E],
  note=f"{V} Hours, extended evenings and the free last Sunday (mobbed) — Field Sheet §2. "
       "Dress code is a rule, not a suggestion {O}."),

 dict(n="10",cat="Eating",q="How do you avoid eating badly in a city this good at food?",
  cols="READS AS",
  lede="A host in a doorway, a photograph of carbonara laminated against the weather: "
       "Rome's weakest kitchens advertise hardest, and they do it within sight of the "
       "monuments. The fix is not a list of restaurants — lists die by spring. It is a "
       "filter you carry.",
  table_title="The filter · signals you can read from the pavement",
  rows=[
   (f"Host outside, photo menu, five languages laminated {S}","TRAP"),
   (f"'Tourist menu' boards; a menu spanning all of Italy {S}","TRAP"),
   (f"Cream in the carbonara — the canon broken in public {E}","FRAUD"),
   (f"Front-row tables on the famous square — the view is on the bill {S}","RENT"),
   (f"Posted prices, a coperto on the bill, a room with Romans in it {S}","GO"),
   (f"Ninety seconds' walk off the piazza — a different city, a different bill {S}","GO"),
  ],
  verdict="<b>The call</b>Trust the filter over any list, including one of ours. Walk the "
       "ninety seconds, order the Roman canon — cacio e pepe, carbonara, amatriciana, "
       "gricia — done plainly, and book the good rooms a day ahead like the locals do. "
       "Dinner starts at eight; an empty room at seven is not a find, it is a warning "
       "reading you back.",
  fo=["one splurge is planned → Rome's fine dining earns it; book well ahead"],
  ag=["hunger hits at six → that is what aperitivo is for (Decision 11)"],
  note=f"{E} The canon and the coperto are stable. {V} Named rooms are not — which is why "
       "the back-matter page refuses to print them."),

 dict(n="11",cat="Evening",q="Is aperitivo dinner, or a prelude to it?",cols="WHEN",
  lede="At seven, hunger arrives on American time; Roman kitchens will not wake for another "
       "hour. Into that gap the city long ago installed its most civilised invention — a "
       "drink built to open the appetite, with just enough food to hold the line.",
  table_title="The Roman evening, in order",
  rows=[
   (f"Aperitivo — spritz or wine, olives and bites, the light going gold {E}","6–8 PM"),
   (f"Rooftop hour — the same ritual with the skyline attached {S}","GOLDEN HOUR"),
   (f"Dinner — kitchens wake at half seven; rooms fill from eight {E}","8 PM →"),
   (f"The passeggiata, gelato in hand — dessert is a walk {E}","AFTER"),
  ],
  verdict="<b>The call</b>Prelude. Rome's kitchens are too good to trade for a buffet of "
       "crostini, however generous the spread. Use the hour as the bridge it was designed "
       "to be — piazza table or rooftop, one spritz, watch the stone change colour — then "
       "walk into dinner at eight like you were raised to it. Skipping dinner for a big "
       "aperitivo spread is legal, common, and a small self-robbery.",
  fo=["a heavy lunch happened → let one evening be spritz, gelato and the bridge home"],
  ag=["you booked the trattoria for 7:00 → move it; you will dine alone with the staff "+S],
  note=f"{V} Rooftop terraces open and close with seasons and renovations — Field Sheet §3 "
       "for the checking habit, not the names."),

 dict(n="12",cat="Money",q="Cards, cash, and the question that costs you money?",cols="THE MOVE",
  lede="The card reader tilts toward you with a courtesy: pay in dollars, or in euros? One "
       "answer is a small quiet tax collected thousands of times a day from people who "
       "chose the familiar word. It is the only test in Rome you can fail politely.",
  table_title="Where the money leaks, and the counter-move",
  rows=[
   (f"The dollars-or-euros prompt, at every terminal and ATM {E}","ALWAYS EUROS"),
   (f"Foreign-transaction fees on the wrong card {E}","NO-FEE CARD"),
   (f"Standalone ATMs and their exchange 'offers' {S}","BANK-ATTACHED ATMS"),
   (f"The coperto and the small bar — card-cool territory {S}","CARRY SMALL NOTES"),
   (f"Tipping on American reflex {E}","ROUND UP, €1–2"),
  ],
  verdict="<b>The call</b>Euros, every single time the machine asks — the 'conversion' is a "
       "worse rate wearing a convenience costume. Bring one no-fee card, pull cash from "
       "bank-attached machines, and keep small notes for the coperto and the espresso "
       "counter. Then un-learn the tip: service is not waiting for twenty percent, and "
       "rounding up is the local ceiling, not the floor.",
  fo=["the machine offers dollars 'for your convenience' → that word is the price tag"],
  ag=["a server seems hurt by €2 → they are not; the theatre is for tourists "+S],
  note=f"{V} What a day costs — the question everyone asks — depends on your Decision 01 "
       "and 10 choices; the levers, not the totals, are stable. Exchange-rate reality: "
       "Field Sheet §1."),

 dict(n="13",cat="Risk",q="How worried should you be?",cols="POSTURE",
  lede="Bus 64 rolls out of Termini toward St Peter's with a cargo of sightseers and, most "
       "days, somebody quietly working the crowd. That sentence is close to the entire "
       "criminal risk profile of a Roman holiday — and it is manageable with your elbows.",
  table_title="The risk ledger · read once, then relax",
  rows=[
   (f"Violent crime against visitors — rare; comparable to or below peer cities {E}","GO"),
   (f"U.S. advisory — Level 2, 'exercise increased caution' {O}","STANDARD EUROPE"),
   (f"Pickpockets — the 64/40 buses, Termini, Metro A, the sight crowds {S}","BAG DISCIPLINE"),
   (f"Scam theatre — petitions, friendship bracelets, 'gold' rings {S}","WALK ON"),
   (f"Fines — unvalidated tickets; sitting on the Spanish Steps {O}","KNOW THE TWO RULES"),
  ],
  verdict="<b>The call</b>Go, and spend your worry on bookings instead. The city's danger "
       "is opportunistic, not violent: it wants an open bag on a crowded bus, a paused "
       "tourist accepting a bracelet, a wallet in a back pocket at the Trevi. Zip the bag "
       "to the front in the five hotspots, refuse street offers without slowing, and the "
       "risk falls to statistical noise.",
  fo=["you were anxious enough to read this twice → that attention is the entire fix"],
  ag=["a stranger's kindness requires your hand, phone or signature → it is a script "+S],
  note=f"{V} The advisory level and any event-driven notes — Field Sheet §1. The full "
       "consequence-ordered list lives in Failure Modes."),

 dict(n="14",cat="The Fourth Day",q="Should day four leave Rome — and for where?",
  cols="RAIL, ONE WAY",
  lede="On the fourth morning the city loosens its grip and the departure boards at Termini "
       "start making offers: hill towns an hour out, the buried port down the old road, "
       "Naples flashing past at speed. Say yes to one — the wrong one costs a day of Rome.",
  table_title="The escapes, priced in minutes · centre to centre",
  rows=[
   (f"Ostia Antica — Pompeii's thrill, closer, quieter; the substitution play {S}","30–35′"),
   (f"Orvieto — a hilltop, a funicular, one staggering cathedral {E}","≈60′"),
   (f"Tivoli — Hadrian's Villa and the Villa d'Este in one green day {E}","≈60′"),
   (f"Castelli Romani — wine towns in the hills; lunch is the sight {E}","30–40′"),
   (f"Pompeii — high-speed to Naples, then the slow local line {E}","70′+35–40′"),
   (f"Florence — possible at speed, and not advisable {S}","≈90′"),
  ],
  verdict="<b>The call</b>With four days, leave once. Default to Ostia Antica or Orvieto — "
       "maximum reward per minute, home for aperitivo. Choose Pompeii only if ruins are "
       "the reason for the trip; it is the longest day on this table and worth it on those "
       "terms alone. Florence in a day is a two-way rehearsal for the visit it deserves — "
       "give it nights of its own, or give it nothing.",
  fo=["ancient stone is your love language → Pompeii, earliest train, booked seats",
      "heat is punishing → Tivoli's gardens and water were built for exactly this"],
  ag=["only three days exist → stay; Rome does not forgive amputation (Decision 02)"],
  note=f"{V} High-speed fares float like airfares — book ahead on the operator apps; "
       "regional lines are fixed-price walk-ups. Details, Field Sheet §2."),
]

def decision_page(d):
    rows="".join(f'<tr><td>{a}</td><td class="num">{b}</td></tr>' for a,b in d["rows"])
    fo="".join(f"<li>{x}</li>" for x in d["fo"]); ag="".join(f"<li>{x}</li>" for x in d["ag"])
    return f"""
<div class="dhead"><span class="dn">{d['n']}</span>
<span class="dmeta"><span class="dk">DECISION {d['n']} / 14</span><span class="dcat">{d['cat']}</span></span></div>
<div class="dq">{d['q']}</div>
<p class="b">{d['lede']}</p>
<div class="led-h"><span>{d['table_title']}</span><span class="cols">{d['cols']}</span></div>
<table class="led">{rows}</table>
<div class="verdict"><b>{'THE CALL'}</b>{d['verdict'].replace('<b>The call</b>','')}</div>
<div class="fa"><div><h4>Then it's yes</h4><ul>{fo}</ul></div>
<div><h4>Then it's no</h4><ul>{ag}</ul></div></div>
<div class="note">{d['note']}</div>"""
