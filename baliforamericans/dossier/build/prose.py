# prose.py — the opening, the essays, the back matter.
# Register: Economist/Monocle. Calm, no enthusiasm, no fluff. Show the reasoning
# and let the reader disagree. Three wonder paragraphs in the whole book, no more.
# Tokens {EST} {OFF} {SUR} {VOL} {C:id} are substituted by build3.py.
# ─────────────────────────────────────────────────────────────────────────────

OPENING = {
 "kind": "The contract",
 "title": "What this book is for",
 "standfirst": "A first trip to Bali is not hard. It is far, and the decisions that shape it "
               "are made in the wrong order, by people who have read everything.",
 "body": """
<p class="lede">Bali is among the easiest places an American can travel to, and among the most
written about. The visa is bought on a website, the food is good at every price, a car and its
driver can be had for the day, and the people are warmer to visitors than the volume of visitors
would lead you to expect. Almost nothing about the trip is difficult. What it is, instead, is far
(two flights and a hub each way, the body sixteen hours out of step, a calendar day lost to the
date line) and small in a way that misleads: an island eighty-nine miles wide whose distances
are counted in hours, where the base you choose decides what the trip contains and the sea
decides whether the one boat runs.</p>

<p>This book exists because that is where the days go. The number of nights decides how many
bases there can be. The hour the long flight lands decides where the first bed should be. The
month decides which coast the surf is on and how rough the strait is. The last night decides how
long the only drive with a deadline will take. The island leg, placed where the picture says it
should go, puts the one weather-dependent link against the flight home. None of that is
difficult. It is simply not answerable one article at a time, which is exactly how it is usually
answered.</p>

<h2>What we do and do not claim</h2>

<p>Every call in here is argued in the open, with the arithmetic on the page, so that you can
disagree with us and still come out ahead. That is the contract. Where we say inland first, we
show the three pins that say so; where the call is close, we say it is close. A recommendation
you cannot audit is worth nothing to someone spending four thousand dollars, and the number of
places where a confident voice is repeating a decade-old blog post is high in Bali: the Nyepi
date from last year, the scooter that "everyone rides", the ATM fee nobody can source, the dry
season that is supposed to mean a calm sea. {EST}</p>

<p>We do not tell you which villa to book or which warung to eat at. Those are the two things
every guide leads with and the two that age fastest. We print no drive time, because the site
this book is built from refuses to, and it is right: the number would be wrong at the hour you
read it. The back of this book says plainly what it refuses to do, and why.</p>
""",
}

HOWTOREAD = {
 "kind": "How to read it",
 "title": "Marks, and the two documents",
 "standfirst": "Every load-bearing claim carries a mark that tells you what kind of claim "
               "it is, and which of the two documents it belongs in.",
 "body": """
<p class="lede">Travel writing rarely distinguishes between a rule written into a governor's
circular, a fact that has been true for forty years, and a fee that was checked once in
October. This book marks the difference on the claims a decision turns on, because the three
age at completely different rates and you are entitled to know which one you are being
handed.</p>

<div class="ledger">
  <div class="lcap">The four marks</div>
  <table>
    <tr><th>Mark</th><th>Means</th></tr>
    <tr><td>{EST} <b>ESTABLISHED</b> — structural, true for years</td><td>the book</td></tr>
    <tr><td>{OFF} <b>OFFICIAL</b> — a published rule, a government advisory</td><td>the book</td></tr>
    <tr><td>{SUR} <b>SURVEYED</b> — our own dated observation, with its method</td><td>the book, dated</td></tr>
    <tr><td>{VOL} <b>VOLATILE</b> — a fee, a timetable, a date that moves</td><td>the Field Sheet</td></tr>
  </table>
</div>

<p>A mark is a classification, not a citation: it says what kind of claim you are reading.
Reasoning carries no mark, because reasoning is ours and is what you are paying for; what it
rests on is marked once, at the end of the sentence that states it. The one surveyed claim in
this book is the set of road distances, measured by the site on the road network in October
2026 and printed as miles; nothing in it was measured in minutes.</p>

<h2>Where the reporting comes from</h2>

<p>This book is built from seventy-seven articles published on baliforamericans.com, the same
desk, not an outside authority. It works from what they establish and makes the connections no
single article was in a position to make. Every one is listed at
<b>baliforamericans.com/sources</b>, with the date it went up. Where a claim rests on something
else (the State Department, the immigration directorate, the customs service, the CDC, the
governor's circular, the holiday decree) the Field Sheet prints the address.</p>

<h2>Why there are two documents</h2>

<p>The book is built to stay true for about two years and contains no live fee or price,
because a figure printed in a book is a lie with a long shelf life. Every volatile figure (the
visa and levy amounts, the overstay fine, next year's Nyepi, the holiday cluster, the crossing
times, the tax rates) lives in the <b>Field Sheet</b>, a short dated companion reissued every
quarter. When the two disagree, the Sheet is right and the book is old. Read the book once
before you book anything; carry the Sheet on the trip.</p>
""",
}

GROUND = {
 "kind": "The ground",
 "title": "Short miles, long days",
 "standfirst": "The single fact that reorganises a first trip to Bali, and the reason the usual "
               "question has no answer.",
 "fig": "island", "fig_after": 1,
 "plate2": "A37", "plate2_after": 3,
 "plate2_cap": "Rice terraces on a hillside in the centre of the island, the kind of place that is a morning from Ubud and a full day from the coast. Which of the two it is for you was decided when you chose where to sleep, which is why the base is the decision that contains the others.",
 "plate": "A01", "plate_after": 5,
 "plate_cap": "Mount Agung at sunrise over the east of the island. The whole of Bali is in frame at this scale, which is the problem: a map that fits on a page suggests a place that fits in a day, and the island's hours do not scale with its miles.",
 "body": """
<p class="lede">Ask how long it takes to get from the airport to Ubud and you will be given a
number. The number is honest for the person who measured it and wrong for you, because the
question has no answer. The distance is about twenty-two road miles, which an American reads as
half an hour. The time depends on the hour, the day, the rain, and whether a village has closed
its road for a ceremony, and it can be several times what the mileage suggests. The site this
book is built from measured every distance on the island and refused to print a single drive
time. That refusal is the ground the book stands on. {SUR}</p>

<p>Bali is about eighty-nine miles from east to west and fifty from north to south, with the
airport on a narrow neck of land in the south. From there it is about four road miles to Kuta,
seven to Seminyak, eight to Nusa Dua, eleven to Sanur, twelve to Canggu and thirteen to
Uluwatu; twenty-two to Ubud in the hills; thirty-five to Sidemen and the Gili port at Padang
Bai; about fifty to Munduk in the mountains and sixty to Amed and Lovina on the far coasts. In
miles, nothing is far. In hours, the island divides into three: a south where a short hop is an
app ride, a centre that is a morning away, and a far side that is a day's travel and belongs to a
stay rather than an outing. {EST}</p>

<p>The roads make it so. In the south they run through continuous built-up areas, narrow, shared
with cars, trucks and a great many motorbikes that pass on either side; into the hills they are
narrow and winding; everywhere a procession can close one for a period on no timetable a visitor
can consult, and in the wet months heavy rain slows everything. The site's rule replaces the
clock: a day holds three or four stops in one direction, chosen so the route never doubles back
through the busy south, with the drive home counted as part of the day. A live map, set to the
actual hour on the actual day, the night before, is the instrument; your driver's estimate is the
second opinion, and the longer of the two is the one to believe.</p>

<h2>Why that decides the base</h2>

<p>Once distance is counted in hours, the base stops being a hotel choice and becomes the
decision that contains all the others. The beach areas and the cultural centre are about twenty
miles apart and a slow drive, so a single base means a long day trip to whichever one you did
not choose; one such day is fine and three of them is a commute. The quiet regions are far
enough that a day trip is impractical, so they are a stay or nothing, and a stay is three nights.
The question to ask of every base is not what it is near but what it is far from, and the honest
answer to that question is what turns a list of places into a sequence of nights. {EST}</p>

<p>Three fixed points then decide the order of those nights, and none of them is on the map.
The hour the long flight lands, after two flights and a hub and a calendar day lost to the date
line, decides how far the first bed can sensibly be from the terminal and what the first two
mornings are good for. The sea under the one boat crossing, which answers to the harbour master
and the swell and is roughest in the dry months, decides where in the trip the island nights can
safely sit. The drive to the airport on the last morning, the only journey on the island with a
penalty for being late, decides where the last night must be. Everything else about the itinerary
is negotiable. These three are not.</p>

<h2>What else the hours decide</h2>

<p>Once the island is a set of hours rather than a map, most of the remaining decisions get
easier, and several of them stop being decisions at all. The scooter that looked like the only
way to reach dinner turns out to be a symptom of a villa in the wrong place. The four famous
temples sort themselves by the base each is a short outing from, and few trips need all four.
The volcano climb belongs to an Ubud morning, because the car comes in the middle of the night
and comes earlier the further south you sleep. The entry stack, which fixes the trip's outer edge
at thirty counted days and names the ticket out you must already hold, has to be done in an order
that starts with the passport, months before any of this. {OFF}</p>

<p>Everything that follows is that single fact, worked out. Eleven decisions, each with the
arithmetic on the page; the operations a first trip runs; and the failures, sorted by what they
cost. The island is better than any plan you can make of it. The plan's job is to leave you free
for that.</p>
""",
}

BEFOREYOUFLY = {
 "kind": "Before you fly",
 "title": "The things with deadlines",
 "plate": "A36", "plate_after": 4,
 "plate_cap": "A tour boat on clear water. The trips that look as though they need booking from home are the ones that do not: the boat, the driver, the volcano and the snorkelling are arranged on the island a day or two ahead, with the forecast in hand.",
 "standfirst": "Most of the preparation is optional. These are not, and each has a date "
               "attached — one of them months before the flight, one of them seventy-two "
               "hours before you land.",
 "body": """
<p class="lede">Bali asks less of an American traveller in advance than most of Asia does, and
the few items with deadlines are the ones that look most like details. {C:passport-6m} That
single test puts a State Department renewal clock in front of everything else, because no visa
cures a short passport and every later form is filled against the passport's number.</p>

<div class="ledger wrap">
  <div class="lcap">What has a deadline · counted back from departure</div>
  <table>
    <tr><th>Task</th><th>When</th></tr>
    <tr><td>Passport: six months beyond the landing date, two blank visa pages, every traveller including children {OFF}</td><td>check it today; renew before buying anything</td></tr>
    <tr><td>Travel clinic: hepatitis A, hepatitis B and typhoid are recommended, and some need spaced doses; the rabies question for remote travel or small children {OFF}</td><td>6–8 weeks out</td></tr>
    <tr><td>International tickets, one booking, the final leg and the arrival hour chosen on purpose {EST}</td><td>2–4 months out; earlier for July, August, Christmas and the March cluster</td></tr>
    <tr><td>The medicine's class, checked with your doctor; the alternative agreed; a letter by generic name {OFF}</td><td>weeks out, before anything is packed</td></tr>
    <tr><td>The e-VOA on the official site, after the flights and the final passport; the levy on the province's site {OFF}</td><td>once the flights are fixed; both valid well ahead</td></tr>
    <tr><td>The policy's scooter and evacuation clauses read; the assistance number saved and shared {OFF}</td><td>before paying for it</td></tr>
    <tr><td>Phone unlocked; a travel eSIM installed; the ride app set up while your US number still receives texts {EST}</td><td>the week before</td></tr>
    <tr><td>The arrival card, free, online {OFF}</td><td>within 72 hours of the local arrival date, no earlier</td></tr>
  </table>
</div>

<p>The passport deserves the first slot because it is the only item that can refuse you with
no remedy at the border. The US Consular Agency in Bali is blunt that immigration will not let
you in otherwise, and adds the detail many travellers miss: the endorsement pages at the back do
not count as blank pages, so the count is of visa pages with nothing on them. A passport replaced
after the e-VOA was bought leaves a visa issued for a number you no longer carry; renew first and
buy the visa second. An emergency passport does not work with the visa on arrival at all. {OFF}</p>

<h2>The clinic</h2>

<p>{C:vaccines} Hepatitis A and typhoid are both food-and-water borne, which is the relevant
route here: {C:water} A great deal of good eating is done at small places, and the habits
are the same at every price. The CDC adds that the typhoid vaccine is not fully protective, so the food and
water habits still matter. No one needs antimalarials for a normal Bali trip, which contradicts
the blanket advice given about Southeast Asia: {C:malaria} Dengue has no vaccine available in
the United States and its mosquitoes bite by day, so repellent is a breakfast-terrace concern,
not a jungle one. The CDC's Zika notice for Bali is the item anyone pregnant or planning a
pregnancy reads before booking. The rabies decision is the one with a series of shots in front
of the flight: for remote parts of the island, small children who reach for animals, or a long
stay, it is a conversation with the clinic; for everyone, the rule after a bite or scratch is a
wash and a doctor the same day. {OFF}</p>

<h2>The medicine bag</h2>

<p>This is the deadline that does not look like one. Indonesia sorts medicine by class, allows
ninety days of ordinary prescriptions with the prescription and sixty of psychotropics, and bans
the narcotic class outright with or without a prescription; the State Department names ADHD
medicines among the ones that are illegal and notes that customs publishes no list to look yours
up. The work is therefore yours, weeks out: find your drug's class, agree an alternative with
your doctor if it is a stimulant or a strong painkiller, pack everything in its original
packaging with a prescription per item, and go through every pocket and toiletry bag for
cannabis and CBD products, which are illegal in every form however they were bought at home. {OFF}</p>

<h2>What does not need doing</h2>

<p>You do not need to register your phone with customs: a tourist roaming on a US SIM or using a
local SIM bought at an operator's outlet is outside the rule, and the site reads a foreign travel
eSIM as the roaming case. You do not need an International Driving Permit unless there is a
chance you will rent a car, and if there is, you need it from home, because it is issued in the
United States and a rental is the kind of decision that gets made on the spot; it adds no
motorcycle class to a car licence. You do not need drivers, day tours, cooking classes or the
volcano climb booked from abroad; they are arranged on the island a day or two ahead, with the
weather in hand. You do not need a packing list for one climate if the trip stays in the south,
and you do need a sweater for Munduk or a Batur summit, a sarong and a light cover for every
temple gate, and a refillable bottle, because the island's rules ban single-use plastics and the
State Department's advice is sealed water. {EST}</p>
""",
}

DAYZERO = {
 "kind": "Day zero",
 "title": "The first six hours",
 "standfirst": "Nobody writes the arrival day, which is the one where a plan is most easily "
               "lost: two flights, a hub, a date line, and a body sixteen hours out of step.",
 "fig": "arrival",
 "plate": "A02",
 "plate_cap": "The last leg, at dusk. The short flight into Bali is the easy half of the journey; what it decides is the local hour you land, and the hour decides whether the first bed is four miles from the terminal or twenty-two miles inland in the dark.",
 "plate_after": 3,
 "body": """
<p class="lede">The arrival day is written off before it starts, and the useful thing is to
write it off on purpose. {C:timezone} The flight west crosses the date line, so a Friday evening
departure can land on a Sunday; the hotel night in between is paid for and never slept in, and
the body arrives wanting to sleep through the Balinese afternoon and wake in the small hours.
Fatigue from the journey passes after a night; the jet lag takes two days. Plan nothing for the
arrival day beyond reaching a room.</p>

<p>What stands between the gate and the room is four things in order, and a traveller who did
the paperwork from home has little left to do at any of them. The visa comes first: an e-VOA
goes to immigration with the passport and the record; a visa bought at the counter means a
payment line before the immigration line, with a card ready and cash as the backup, because no
official list says what the counter accepts on a given day. Immigration checks the passport, the
visa and the arrival card's QR code, which lives as a screenshot because airport Wi-Fi is a poor
thing to depend on at that moment. Read the stamp before walking away, because the thirty days
are counted from it. {OFF}</p>

<p>Customs is the last official step and the arrival card already carries the declaration. The
allowance is one litre of alcohol per adult, with the excess destroyed rather than taxed, and a
bottle bought at the hub counts toward it. Medicine is a red-channel item, which is where
declared things are looked at and not an accusation; the prescriptions ride in the hand luggage
for exactly this minute. Nothing about a personal phone needs the registration desk. {OFF}</p>

<h2>Money and signal</h2>

<p>The two things most travellers want before leaving the terminal are rupiah and data. The
State Department says the ATMs accept US cards and may charge, and advises machines in secure
locations and a check for tampering; the site's advice is enough rupiah at the airport for the
first day's transport, a meal and small purchases, and the rest later at a bank branch, counted
by the zeros. A travel eSIM set up at home works when the plane lands; a local SIM has to be
bought and registered at an operator's counter first; and the ride app you set up while your US
number still received texts is the one that will work in the hall. {EST}</p>

<h2>Getting out</h2>

<p>Transport from the airport comes in three forms, and the one the site recommends for a first
arrival after a journey of this length is the one booked before you flew: a car arranged with
the hotel or a driver, the name and the meeting point in writing. It costs more than an app ride
and removes every decision from the moment you are least able to make one. The second is Grab,
which runs pickups from its own lounge at the international terminal, booked in the app; the
third is the official taxi counter with a working meter. The person who approaches you in the
hall with a price is the case the State Department's advice to avoid unlicensed taxis at airports
was written about; walk past. {OFF}</p>

<h2>How far to go</h2>

<p>The distance between the terminal and the first bed is a choice made when you booked, and it
interacts with the hour. A daytime landing can go anywhere, including the twenty-two miles to
Ubud, because the day is already written off and the dawn waking of the next two will be spent
among the terraces. A dusk landing goes to the south coast, four to eleven miles away, with Ubud
waiting for the morning. A landing late at night goes to the shortest drive there is, Kuta,
Jimbaran or Sanur, and moves on after breakfast. The CDC's advice after landing is daylight and
the local schedule, and it is easy to follow here: spend the first mornings outside, eat at
Balinese hours from the first meal, keep naps to twenty minutes, and do not ride or drive anything
on the first two days, because jet lag affects concentration and the roads ask for all of it. {EST}</p>
""",
}

FAILURE_MODES = {
 "kind": "Failure modes",
 "title": "What goes wrong, by what it costs",
 "plate": "A39", "plate_after": 3,
 "plate_cap": "Boats in the channel off Nusa Lembongan, under the bridge that carries walkers and motorbikes across to Ceningan. Most of what goes wrong on an island leg went wrong weeks earlier, when the nights were placed; a cancelled boat here is an extra afternoon or a missed flight, depending only on the order.",
 "standfirst": "Organised by consequence rather than by topic — which is the one thing a "
               "website of separate articles cannot do.",
 "body": """
<p class="lede">These are the failures that recur, sorted by what they take from you. A website
answers them one at a time, in whichever article each happens to belong to. Seeing them ranked by
cost tells you where to spend a limited supply of planning attention, and in Bali the ranking is
unusual: the expensive failures are about days, paperwork and a chain of small clauses, not
about money.</p>

<h2>Costs you the trip, or a hospital</h2>

<div class="ledger wrap">
  <div class="lcap">The ones that are not recoverable on the day</div>
  <table>
    <tr><th>What happens</th><th>Where it is answered</th></tr>
    <tr><td>A passport with five months left, or two "blank" endorsement pages {OFF}</td><td>Decision 04 — refused at the desk; renew first, buy the visa second</td></tr>
    <tr><td>A rented scooter on a car-only licence, then a crash {OFF}</td><td>Decision 05 — unlicensed under the traffic law; the insurer may read the policy afterwards</td></tr>
    <tr><td>An ADHD prescription or a CBD gummy in the bag {OFF}</td><td>Decision 10 — the narcotic class is banned with or without a prescription; a criminal matter, not a customs one</td></tr>
    <tr><td>The island boat back on the morning of the flight home; the harbour master holds the boats {EST}</td><td>Decision 06 — the leg goes in the middle; a full day's buffer, two in July and August</td></tr>
    <tr><td>A connection that slips and lands on the wrong side of the Nyepi window {OFF}</td><td>Decision 08 — a full day clear of the date, in Bali's calendar, not yours</td></tr>
    <tr><td>A hangover far worse than the drinks, or blurred vision, the afternoon after an unlabelled spirit {OFF}</td><td>The risk chapter — methanol; a hospital, and say the word</td></tr>
  </table>
</div>

<h2>Costs you days</h2>

<div class="ledger wrap">
  <div class="lcap">The expensive ones</div>
  <table>
    <tr><th>What happens</th><th>Where it is answered</th></tr>
    <tr><td>Four regions planned into seven nights; each becomes an arrival {EST}</td><td>Decision 01 — nights divided by three is the ceiling on bases</td></tr>
    <tr><td>The beach booked first; the dawn hours of jet lag slept through {EST}</td><td>Decision 02 — inland first, the coast last</td></tr>
    <tr><td>A villa chosen for its photographs, far from everything; every meal a ride {EST}</td><td>Where to stay — the question is what the base is far from</td></tr>
    <tr><td>Six stops in a day from the far south, three of them in the highlands {EST}</td><td>Decision 07 — three or four, in one direction, from the base they belong to</td></tr>
    <tr><td>The Gilis added to a week {EST}</td><td>Decision 06 — two travel days whatever the route; a fortnight or a return visit</td></tr>
    <tr><td>The Batur climb on the first Ubud morning, or from Seminyak {EST}</td><td>Decision 07 — the second or third morning, from Ubud, with the day after kept free</td></tr>
    <tr><td>A July trip with the island leg and a small buffer, because July is dry {EST}</td><td>Decision 03 — the dry season is not the calm season</td></tr>
    <tr><td>A stay planned as "a month" on a thirty-day visa {OFF}</td><td>Decision 04 — counted, not rounded; the extension about two weeks before day thirty</td></tr>
  </table>
</div>

<h2>Costs you money</h2>

<div class="ledger wrap">
  <div class="lcap">The avoidable ones</div>
  <table>
    <tr><th>What happens</th><th>Where it is answered</th></tr>
    <tr><td>The visa or the levy bought on a lookalike site at a higher price {OFF}</td><td>Decision 04 — the government's own domains, reached by typing the address</td></tr>
    <tr><td>Two separate tickets, the first flight late, the second airline unmoved {EST}</td><td>Decision 09 — one booking, or a night at the hub</td></tr>
    <tr><td>Two duty-free bottles, one of them destroyed at the belt {OFF}</td><td>Decision 04 — one litre per adult, and the hub purchase counts</td></tr>
    <tr><td>A card with a foreign fee, the dollar option accepted at every terminal {EST}</td><td>Decision 11 — the one cost removable at home; always rupiah</td></tr>
    <tr><td>A daybed booked without asking whether the minimum spend is per person, or before tax {EST}</td><td>The set pieces — four questions to the reservations desk</td></tr>
    <tr><td>A villa deposit sent by bank transfer to a stranger {EST}</td><td>Where to stay — a card, through a platform</td></tr>
  </table>
</div>

<h2>Costs you the thing you came for</h2>

<p>The quietest failure has no line item. It is arriving on an island you will probably visit
once with a plan assembled from forty open tabs, and spending ten days executing it: every
viewpoint at the hour the day-trip boats arrive, every sunset from the spot everyone else chose,
every day starting with a car. The complaint people have about a Bali trip is rarely that it
missed a temple. It is that nothing was enjoyed, because everything was present. The book is
mostly arithmetic because the arithmetic is what buys back the attention.</p>
""",
}

BACKMATTER = {
 "kind": "Back matter",
 "title": "What this book will not tell you",
 "standfirst": "The refusals are the product. They are what keeps the rest of it true.",
 "body": """
<p class="lede">Five things this book deliberately does not do. Each is a thing most guides lead
with, and each is a thing we would have to get wrong in order to include.</p>

<ul class="refuse">
<li><b>It does not name hotels or villas.</b> We have not slept in them. An assessment of a room
we have not been in is a repackaged booking-site listing with a confident voice on top, and you
can read those for free. What the book does instead is tell you which part of the island to sleep
in and in what order, which is the decision that survives a change of ownership, and the four
questions to put to any listing before paying.</li>

<li><b>It does not name restaurants, beach clubs or boat operators.</b> A list is wrong within a
season: the cook moves, the club changes its minimum, the operator changes its boat. The rules
that generated the list are still right in five years (food cooked to order and served hot, a
minimum spend asked per person or per bed before or after tax, a named boat with a life jacket
per seat) so the book gives you the rules.</li>

<li><b>It does not print a drive time.</b> The site measured every road distance on the island
and refused to print a single duration, because the number would be wrong at the hour you read
it. The book inherits that refusal. Miles are stable and are printed; hours are checked on a live
map at your hour, the night before.</li>

<li><b>It does not print current fees or prices.</b> Fees belong in the Field Sheet, which is
dated and re-issued. Where a number is structural (the visa fee set in rupiah, the levy, the
customs allowances, the tax rate) the Sheet carries it with the date it was read. The book
carries no exchange rate and no daily budget, because the site has no official source for one and
will not invent it.</li>

<li><b>It does not republish anyone's ratings.</b> Aggregate scores from the booking platforms
are contractually and editorially radioactive, and reprinting them would add nothing you cannot
see for yourself.</li>
</ul>

<div class="ledger wrap">
  <div class="lcap">Where the refused figures live instead</div>
  <table>
    <tr><th>Refused in the book</th><th>Where it is answered</th></tr>
    <tr><td>Hotels, villas, restaurants, clubs, boats {EST}</td><td>the rule that generated the list, in the chapters; the four questions, in where to stay</td></tr>
    <tr><td>Drive times {EST}</td><td>road miles in Decision 07 and the ground; a live map at your hour, the night before</td></tr>
    <tr><td>Fees, prices, dates, rates {VOL}</td><td>the Field Sheet, dated, reissued quarterly, with the address each was read from</td></tr>
    <tr><td>Ratings and rankings {EST}</td><td>nowhere; the island is better than any ranking of it</td></tr>
  </table>
</div>

<p>There is a sixth refusal that shaped this edition. Where no primary source could be found for
a figure that every blog prints — the ATM fee and cap, the percentage of visitors who get sick,
how often the boats are cancelled, which businesses close on which holiday — we wrote the
structure and left the figure out, rather than copy a number whose origin nobody could name. A
chapter assembled to fill a page is detectable, and it devalues the chapters that were earned.</p>
""",
}

CLOSING = {
 "plate": "A14",
 "plate_cap": "Sanur at first light, an outrigger on the sand before the day's boats go out. Nothing on an itinerary; the hour a jet-lagged American is awake for anyway, and the thing the arithmetic in this book is protecting.",
 "plate_after": 2,
 "kind": "Closing",
 "title": "The island, not the plan",
 "standfirst": "",
 "body": """
<p class="lede">There is a moment, usually on the second or third morning, when the planning
stops mattering. It tends to arrive somewhere ordinary: a lane behind the paddies at six, with
the offerings being set out on the doorsteps and nobody else about; an east-facing beach where
the sun comes up over the water and the fishing boats are already back; a village road with a
procession crossing it, and the car switched off to wait. Nothing about it is a sight. It is an
island going about its day, at an hour most visitors are still asleep.</p>

<p>That is the thing the arithmetic is protecting. Every decision in this book exists to
subtract a small anxiety from the fortnight (the boat that was not booked against the flight,
the licence that was never tested, the last night that was close to the terminal) so that more of
it is available for the parts that cannot be decided in advance: the warung with one dish and a
queue, the beach you walked down four hundred steps to and had to yourself, the afternoon the
rain came and you let it.</p>

<p>Work the sums out before you go. Then put the book down and stop optimising. The island keeps
its own time, and it rewards the loose afternoon more than almost anywhere.</p>
""",
}

ESSAYS = [OPENING, HOWTOREAD, GROUND, BEFOREYOUFLY, DAYZERO]
BACK    = [FAILURE_MODES, BACKMATTER, CLOSING]
