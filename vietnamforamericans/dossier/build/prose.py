# prose.py — the opening, the essays, the back matter.
# Register: Economist/Monocle. Calm, no enthusiasm, no fluff. Show the reasoning
# and let the reader disagree. Three wonder paragraphs in the whole book, no more.
# Tokens {EST} {OFF} {SUR} {VOL} {C:id} are substituted by build3.py.
# ─────────────────────────────────────────────────────────────────────────────

OPENING = {
 "kind": "The contract",
 "title": "What this book is for",
 "standfirst": "A first trip to Vietnam is not hard. It is long, and the decisions that "
               "shape it are made in the wrong order.",
 "body": """
<p class="lede">Vietnam is among the easier countries an American can travel in. The State
Department places it at its lowest advisory level, the food is excellent at every price, the
internal flights are cheap and frequent, and the people are warmer to American visitors than
most first-timers expect. Almost nothing about the trip is difficult. What it is, instead, is
long — a thousand miles from the first city to the last, running three climates at once —
and the length turns a dozen small decisions into one sequence, where each choice quietly
closes options for the next.</p>

<p>This book exists because that sequence is where the days go. The month you can travel
decides which end of the country is in season. The international ticket decides which end
you land at, and it is usually bought first. The e-visa form, filled in weeks earlier, has
already fixed how long you can stay and which gate you may leave through. The overnight
cruise you booked because it was on every list has claimed two days of a northern leg that
had four. None of that is difficult. It is simply not answerable one article at a time,
which is exactly how it is usually answered.</p>

<h2>What we do and do not claim</h2>

<p>Every call in here is argued in the open, with the arithmetic on the page, so that you can
disagree with us and still come out ahead. That is the contract. Where we say fly, we show
the hours that say fly; where the call is close, we say it is close. A recommendation you
cannot audit is worth nothing to someone spending four thousand dollars, and the number of
places where a confident voice is repeating a decade-old blog post is high in Vietnam —
the rail pass that no longer exists, the visa exemption that was never for Americans, the overnight train to Sapa that the expressway overtook. {EST}</p>

<p>We do not tell you which hotel to book or which restaurant to eat at. Those are the two
things every guide leads with and the two that age fastest. The back of this book says
plainly what it refuses to do, and why.</p>
""",
}

HOWTOREAD = {
 "kind": "How to read it",
 "title": "Marks, and the two documents",
 "standfirst": "Every load-bearing claim carries a mark that tells you what kind of claim "
               "it is, and which of the two documents it belongs in.",
 "body": """
<p class="lede">Travel writing rarely distinguishes between a rule written into a decree, a
fact that has been true for forty years, and a price that was checked once in spring. This
book marks the difference on the claims a decision turns on, because the three age at
completely different rates and you are entitled to know which one you are being handed.</p>

<div class="ledger">
  <div class="lcap">The four marks</div>
  <table>
    <tr><th>Mark</th><th>Means</th></tr>
    <tr><td>{EST} <b>ESTABLISHED</b> — structural, true for years</td><td>the book</td></tr>
    <tr><td>{OFF} <b>OFFICIAL</b> — a published rule, a government advisory</td><td>the book</td></tr>
    <tr><td>{SUR} <b>SURVEYED</b> — our own dated observation, with its method</td><td>the book, dated</td></tr>
    <tr><td>{VOL} <b>VOLATILE</b> — a price, a timetable, a date that moves</td><td>the Field Sheet</td></tr>
  </table>
</div>

<p>A mark is a classification, not a citation: it says what kind of claim you are reading.
Reasoning carries no mark, because reasoning is ours and is what you are paying for; what it rests on is marked
once, at the end of the sentence that states it.</p>

<h2>Where the reporting comes from</h2>

<p>This book is built from a hundred articles published on vietnamforamericans.com — the
same desk, not an outside authority. It works from what they establish and makes the
connections no single article was in a position to make. Every one is listed at <b>vietnamforamericans.com/sources</b>, with the date it went
up. Where a claim rests on something else (the State Department, the Immigration
Department's FAQ, the customs decree) the Field Sheet prints the address.</p>

<h2>Why there are two documents</h2>

<p>The book is built to stay true for about two years and contains no live prices, because
a price printed in a book is a lie with a long shelf life. Every volatile figure (the visa
fee, the processing window, next year's Tết dates, the fares) lives in the <b>Field
Sheet</b>, a short dated companion reissued every quarter. When the two disagree, the Sheet
is right and the book is old. Read the book once before you book anything; carry the Sheet
on the trip.</p>
""",
}

GROUND = {
 "kind": "The ground",
 "title": "One line, three climates",
 "standfirst": "The single fact that reorganises a first trip to Vietnam, and the reason "
               "the usual question has no answer.",
 "fig": "line",
 "plate": "A01",
 "plate_cap": "The north in its cool season: mist in the valleys, the terraces bare water. Three hundred miles south the same week, the central coast is drying out; six hundred miles south, Saigon is in high season. Three countries, one line.",
 "plate_after": 6,
 "body": """
<p class="lede">Ask when to visit Vietnam and you will be given a month. The answer is
honest for somebody and useless for you, because the question has no answer. The country
runs about a thousand miles from the Chinese border to the Gulf of Thailand along a single
north–south spine, and at any given moment it is running three different climates. A month
that is perfect in one third is the worst of the year in another. {EST}</p>

<p>The north (Hanoi, the bay, Ninh Bình, Sapa) has four real seasons, including a winter
that arrives as a persistent grey drizzle in the fifties and sixties Fahrenheit and catches
out everyone who packed for Southeast Asia in the abstract. The centre (Huế, Đà Nẵng, Hội An) is driest from February to August and then spends September to November under the
storms that flood Hội An's riverside streets in most years. The south (Saigon, the delta, the islands) is warm all year and divides into dry and wet rather than hot and cold, the wet
arriving as a heavy afternoon hour rather than a washed-out day. {EST}</p>

<p>Put the three side by side and the shape of the problem is visible at once. No month is
green at both ends. March and April compromise least, so they are busy. October is
the north's best month and the centre's worst, in the same week. December is bright in the
south and cold in the north. Whatever month you have, one third of the line is in its
difficult season, and the trip will cross it.</p>

<h2>Why that decides the direction</h2>

<p>The classic first trip runs the length of the line in one direction — Hanoi to Saigon or
the reverse — with an internal flight or two and the Huế–Đà Nẵng coast by train. Direction
feels like the first creative decision, and it is mostly not a decision at all: it is the
residue of three things settled elsewhere. {C:nonstop} So a West Coast traveller who wants
the nonstop starts in the south whether they intended to or not. Open-jaw tickets, into one
end and out of the other, are widely available and cost little more than a return, so the
backtrack is never necessary. And the month has an opinion: the weather-sensitive end should
come first, while there are still days to move. {EST}</p>

<p>By the time anyone asks themselves which way to go, the airline map and the calendar have
usually answered it. The useful move is to notice that earlier, and to treat the international
booking as the moment the route is chosen rather than a separate errand done in a lunch hour.</p>

<h2>What else the line decides</h2>

<p>Once the country is a line rather than a map, most of the remaining decisions get easier,
and several of them stop being decisions at all. The long legs sort themselves by distance:
fly the thousand-kilometre hops, take the train on the one stretch of coast where the train
is the point, and never fly the hundred kilometres between Huế and Đà Nẵng. The excursions off the line (the bay, Sapa, the delta, the islands) each cost a known number of days, and
the days come out of somewhere. And the e-visa, which names the gate you will enter and the
gate you will leave by, has to be filled in for the line you will travel,
because it cannot be corrected once you are on it. {OFF}</p>

<p>Everything that follows is that single fact, worked out. Eleven decisions, each with the
arithmetic on the page; the operations a first trip runs; and the failures, sorted by what
they cost. The country is better than any plan you can make of it. The plan's job is to
leave you free for that.</p>
""",
}

BEFOREYOUFLY = {
 "kind": "Before you fly",
 "title": "The things with deadlines",
 "standfirst": "Most of the preparation is optional. These are not, and each has a date "
               "attached — some of them earlier than the flight.",
 "body": """
<p class="lede">Vietnam asks more of an American traveller in advance than Japan or Western
Europe do, and the items with the longest horizons are the ones that look most like details.
{C:visa-required} That single fact puts a government working-day clock in front of
everything else, and the clock stops for a week at Tết.</p>

<div class="ledger">
  <div class="lcap">What has a deadline · counted back from departure</div>
  <table>
    <tr><th>Task</th><th>When</th></tr>
    <tr><td>Settle the route shape — the gates in and out, the days — then apply for the e-visa on the official site {OFF}</td><td>several weeks out</td></tr>
    <tr><td>Travel clinic: Hepatitis A, Hepatitis B and typhoid are recommended, and some need spaced doses {OFF}</td><td>6–8 weeks out</td></tr>
    <tr><td>International tickets, open-jaw; they lock the direction {EST}</td><td>2–4 months out, much earlier near Tết</td></tr>
    <tr><td>Internal flights — the useful departure times go first {EST}</td><td>once the tickets are fixed</td></tr>
    <tr><td>The bay cruise, a Sapa homestay in the autumn peak, a Hội An room near Tết {EST}</td><td>weeks out</td></tr>
    <tr><td>Passport: six months beyond arrival, two blank pages {OFF}</td><td>check it today</td></tr>
    <tr><td>The pre-arrival declaration, free, online {OFF}</td><td>no earlier than 3 days before</td></tr>
    <tr><td>Grab installed, card added; an eSIM if the phone takes one {EST}</td><td>the week before</td></tr>
  </table>
</div>

<p>The visa deserves the first slot because it is the only item that can refuse you. {C:visa-processing}
The counter-evidence is real — Vietnam's own embassy in India publishes a far wider range —
so the lower figure is a floor, not a promise, and non-refundable flights should not be
bought against it. When the document arrives, read every field against the passport
character by character; a mismatched passport number or date of birth can mean being refused
on arrival, with an expensive airport sponsorship as the only remedy. Then print it. {OFF}</p>

<h2>The passport, specifically</h2>

<p>{C:passport-6m} The State Department's own page is internally inconsistent on the page
count, saying one blank page per stamp in one section and at least two in another, so treat
two as the working minimum. One trap worth knowing if things go wrong mid-trip: Vietnam may
not accept the twelve-page US emergency passport for e-visa entry, so a passport replaced at
an embassy elsewhere in the region may not get you in. {OFF}</p>

<h2>The clinic</h2>

<p>{C:vaccines} Hepatitis A and typhoid are both food-and-water borne, which is the relevant
route in a country where the best eating is done at street stalls. Most visitors do not need
antimalarials, which contradicts the blanket advice given about Southeast Asia: {C:malaria}
Sapa, Hà Giang and the central highlands are not covered by that list, and a trip built
around trekking changes the calculation — a question for a clinic with the actual route in
front of it, not for this page. Dengue is the mosquito risk with no vaccine; it is urban,
seasonal, and bites by day, so repellent is not a jungle concern.</p>

<h2>If you are Vietnamese American</h2>

<p>The largest group of Americans travelling to Vietnam with a reason beyond tourism has a
paperwork layer the tourist pages do not describe, and most of it surfaces at departure rather
than arrival, which is the wrong place to learn it.</p>

<div class="ledger wrap">
  <div class="lcap">What a family of Vietnamese origin travels on</div>
  <table>
    <tr><th>Who</th><th>What the trip runs on</th></tr>
    <tr><td>A dual-national adult {OFF}</td><td>one passport for entry, every domestic flight and exit; chosen before booking</td></tr>
    <tr><td>A US-citizen child of Vietnamese parentage {OFF}</td><td>ask the Vietnamese consulate first: a Vietnamese passport or exit visa may be needed to leave</td></tr>
    <tr><td>A Vietnamese minor without both parents {OFF}</td><td>the absent parent's notarised consent, or proof of sole custody</td></tr>
    <tr><td>An overseas Vietnamese who will go back more than once {OFF}</td><td>the five-year visa-exemption paper instead of an e-visa per trip</td></tr>
    <tr><td>Everyone else on a US passport {EST}</td><td>the e-visa — Decision 03</td></tr>
  </table>
</div>

<p>The first rule is about documents, not nationality: {C:same-passport} A family that enters on
Vietnamese passports and tries to leave on American ones, or the reverse, has created the
problem at the booking stage. Decide which passport the trip runs on before a single flight is
bought, and use it for every domestic sector too, because the airlines check. {OFF}</p>

<p>The children are where families are caught. {C:child-exit} {C:minor-consent} A grandparent
taking a grandchild to the village, or one parent travelling alone with the children, carries
the other parent's notarised consent or proof of sole custody; the question of what a
particular child needs in order to leave goes to the Vietnamese consulate before booking, not
to the US Embassy, which cannot answer it. For families who will go back more than once there
is a standing alternative to the e-visa: {C:exemption-paper} It replaces a ninety-day visa
bought trip by trip with something closer to a permission, and it is applied for at a
Vietnamese consulate in the United States. {OFF}</p>

<h2>What does not need doing</h2>

<p>You do not need an International Driving Permit, which Vietnam does not recognise. You do
not need cash in advance beyond a modest reserve of clean dollars for emergencies; the
airport exchange counter is the worst rate of the trip. You do not need day tours, cooking
classes, drivers or food walks booked from abroad — they are arranged in the country a day or
two ahead, usually more cheaply and with better information about the weather. And you do
not need a packing list for one climate: a trip that touches Hanoi or Sapa between November
and March wants real layers, a shell, and shoes that come off easily at temple thresholds. {EST}</p>
""",
}

DAYZERO = {
 "kind": "Day zero",
 "title": "The first six hours",
 "standfirst": "Nobody writes the arrival day, which is the one where a plan is most easily "
               "lost.",
 "fig": "arrival",
 "plate": "A02",
 "plate_cap": "The kerb at arrivals, mid-afternoon. At Saigon the Grab pickup is not here at all — it is upstairs on the departures level — and the first offer at this kerb is the one to walk past.",
 "plate_after": 4,
 "body": """
<p class="lede">You land after twenty-two to twenty-six hours in transit, a full twelve
hours out of step with your body in winter and eleven in summer, on a calendar day that is
not the one you left on. What happens next is decided almost entirely by three things chosen
months earlier: which airport, which direction, and what time the wheels touch. None of them
felt like an itinerary decision when the ticket was bought. All of them are.</p>

<p>The arrival day is a write-off, and the trips that go wrong are the ones that refuse to
admit it. A six a.m. domestic flight or a cruise transfer on the morning after landing is
how two days are lost instead of one. Plan a slow afternoon, daylight, Vietnamese meal times
from the first meal, a nap of no more than half an hour, and an early night. Hanoi's Old
Quarter absorbs a jet-lagged wander well; Saigon in the heat is harder going in that state,
which is a small argument for landing north that most people never weigh. {EST}</p>

<h2>At the counter</h2>

<p>Have the printed e-visa with the passport, the first night's address written down, and the
pre-arrival declaration filed within the three days before. Then the one check that is still
fixable at home and not at the desk: the gate named on the visa against the airport on the
ticket. {C:visa-port} Saigon's immigration hall is the busiest in the country and its peak
queues are long; the smaller international airports (Đà Nẵng, Cam Ranh, Phú Quốc) are quick and far less stressful, which is a reason to route through one of them if the trip
is regional rather than country-wide. {OFF}</p>

<h2>Into the city</h2>

<p>Grab is the simplest answer at all three main airports and the fare is fixed before you
accept, which removes the inflated-meter conversation that airports everywhere are famous
for. At Saigon the pickup is on the upper departures level rather than at arrivals, which
catches people out; follow the signs up and walk past whoever offers a car at the kerb. At
Hanoi the pickup is signposted a short walk from the hall, and the 86 express bus runs to
the Old Quarter for a fraction of the price in about an hour. Đà Nẵng is minutes from its
own centre and forty-five minutes to an hour from Hội An, and at that distance a car
arranged by the hotel is worth the small premium after a long flight. {EST}</p>

<p>Change only enough at the airport counter to reach the hotel — the rate is the worst of
the trip — and use the ATM in the arrivals hall for one large withdrawal rather than
several small ones. A SIM counter in the hall needs the passport for registration; airport
wifi is enough to call the first Grab if the connectivity can wait until town.</p>

<h2>If you are connecting onward</h2>

<p>An international arrival followed by a domestic flight means clearing immigration,
collecting the bags, and checking in again at a separate domestic terminal. Budget three
hours between the two at either Hanoi or Saigon, more around the holidays. The same
asymmetry runs in reverse at the end of the trip: {C:exit-control} The last night of the
trip belongs near the departure airport, not two hours away behind a mountain road or on a
boat whose sailing the port authority decides. {OFF}</p>
""",
}

FAILURE_MODES = {
 "kind": "Failure modes",
 "title": "What goes wrong, by what it costs",
 "standfirst": "Organised by consequence rather than by topic — which is the one thing a "
               "website of separate articles cannot do.",
 "body": """
<p class="lede">These are the failures that recur, sorted by what they take from you. A
website answers them one at a time, in whichever article each happens to belong to. Seeing
them ranked by cost tells you where to spend a limited supply of planning attention, and
in Vietnam the ranking is unusual: the expensive failures are mostly about days and
paperwork, not money.</p>

<h2>Costs you the trip, or a hospital</h2>

<div class="ledger wrap">
  <div class="lcap">The ones that are not recoverable on the day</div>
  <table>
    <tr><th>What happens</th><th>Where it is answered</th></tr>
    <tr><td>The e-visa names Hanoi; the flight lands in Saigon {OFF}</td><td>Decision 03 — refused at the gate; check the document against the ticket at home</td></tr>
    <tr><td>A name or passport number mistyped on the application {OFF}</td><td>Decision 03 — read every field character by character before you fly</td></tr>
    <tr><td>Riding a rented scooter without a Vietnamese licence, then an accident {OFF}</td><td>Decision 04 — illegal, and the insurer may refuse the medical bill</td></tr>
    <tr><td>A river exit to Cambodia on a visa issued for an airport {OFF}</td><td>Decision 03 — the exit port is binding; name the crossing before you apply</td></tr>
    <tr><td>Arriving with a substance that was legal at home still in the blood {OFF}</td><td>The risk chapter — blood tests happen; consular access is routinely delayed</td></tr>
    <tr><td>A cocktail from a bucket in a backpacker bar; blurred vision the next morning {OFF}</td><td>The risk chapter — methanol; a hospital, not a hangover</td></tr>
    <tr><td>A dual-national child enters on the Vietnamese passport and the family tries to leave on the American one {OFF}</td><td>Before you fly — one passport for the whole trip; the child may need a Vietnamese passport or exit visa</td></tr>
  </table>
</div>

<h2>Costs you days</h2>

<div class="ledger wrap">
  <div class="lcap">The expensive ones</div>
  <table>
    <tr><th>What happens</th><th>Where it is answered</th></tr>
    <tr><td>Three regions planned into ten days of leave; the centre becomes one night {EST}</td><td>Decision 01 — count the ground days first, subtract the moves</td></tr>
    <tr><td>Sapa added to a one-week trip: two travel days for one in the valley {EST}</td><td>Decision 06 — Ninh Bình gives the landscape for a fifth of the travel</td></tr>
    <tr><td>The bay cruise on the night before an international flight; the port authority cancels {EST}</td><td>Decision 06 — never on the last night; the call is not the operator's</td></tr>
    <tr><td>A Sapa return booked for the day of the flight home; no flight to fall back on {EST}</td><td>Decision 05 — every route there is overland; leave a night in Hanoi</td></tr>
    <tr><td>Autumn trip with the beach as the anchor; the central coast is in its storm season {EST}</td><td>Decision 02 — let the month choose the region, keep the slack in the centre</td></tr>
    <tr><td>A mid-trip internal flight in Tết week; the seat does not exist {EST}</td><td>Decision 10 — book the transport the day the dates are known, or move them</td></tr>
    <tr><td>Clothes ordered in Hội An on the last evening {EST}</td><td>Decision 07 — two fittings, two full days; order on the first morning</td></tr>
    <tr><td>The Mekong coach circuit, taken as "the delta" {EST}</td><td>Decision 08 — Cái Răng is at dawn in Cần Thơ, or not at all</td></tr>
    <tr><td>The bay cruise booked for the only two free days; the port authority grounds the fleet {OFF}</td><td>Decision 06 — read the forecast first; Ninh Bình from the same hotel the same morning</td></tr>
    <tr><td>Huế given the template's single night; the citadel or the tombs, not both {EST}</td><td>The middle — two nights for history, one with the train for everyone else</td></tr>
  </table>
</div>

<h2>Costs you money</h2>

<div class="ledger wrap">
  <div class="lcap">The avoidable ones</div>
  <table>
    <tr><th>What happens</th><th>Where it is answered</th></tr>
    <tr><td>Five small ATM withdrawals, each paying the same flat fee {EST}</td><td>Decision 11 — the maximum, rarely</td></tr>
    <tr><td>The machine offers to bill in dollars and you accept {EST}</td><td>Decision 11 — always đồng; dynamic conversion is a worse rate every time</td></tr>
    <tr><td>A 500,000 note handed over as a 20,000 {EST}</td><td>Decision 11 — learn the two blue notes before you land</td></tr>
    <tr><td>An e-visa bought through a lookalike site at several times the fee {OFF}</td><td>Decision 03 — evisa.gov.vn, and nothing else</td></tr>
    <tr><td>A cyclo quoted per person, a shoe repair begun unasked, a tailor paid in full up front {EST}</td><td>Decision 11 — the number, in đồng, before anything starts</td></tr>
    <tr><td>An International Driving Permit bought before flying {OFF}</td><td>Decision 04 — a document that changes nothing here</td></tr>
  </table>
</div>

<h2>Costs you the thing you came for</h2>

<p>The quietest failure has no line item. It is arriving in a country you will probably visit
once, with a plan assembled from forty open tabs, and spending the fortnight executing it:
every sight at the hour the coaches arrive, every meal researched from home, every day
starting with an alarm. The complaint people have about a Vietnam trip is rarely that it
missed a city. It is that nothing was enjoyed, because everything was present. The book is
mostly arithmetic because the arithmetic is what buys back the attention.</p>
""",
}

BACKMATTER = {
 "kind": "Back matter",
 "title": "What this book will not tell you",
 "standfirst": "The refusals are the product. They are what keeps the rest of it true.",
 "body": """
<p class="lede">Four things this book deliberately does not do. Each is a thing most guides
lead with, and each is a thing we would have to get wrong in order to include.</p>

<ul class="refuse">
<li><b>It does not name hotels.</b> We have not slept in them. An assessment of a room we have
not been in is a repackaged booking-site listing with a confident voice on top, and you can
read those for free. What the book does instead is tell you which part of a city to sleep in and why (the Old
Quarter against the French Quarter, the town against the beach), which is the decision that survives a change of ownership.</li>

<li><b>It does not name restaurants.</b> A list of restaurants is wrong within a season: the
cook moves, the queue finds it, the lease ends. The rule that generated the list is still
right in five years — one dish on the sign, a queue at the right hour, charcoal you can
smell — so the book gives you the rule. The eating chapter is that argument in full.</li>

<li><b>It does not print current prices.</b> Prices belong in the Field Sheet, which is dated
and re-issued. A price set in a book is a claim that stops being true quietly, and the reader
has no way to tell when it did. Where a number is structural — the visa fee set by decree,
the customs allowance in đồng — the Sheet carries it with the date it was read.</li>

<li><b>It does not republish anyone's ratings.</b> Aggregate scores from the booking
platforms are contractually and editorially radioactive, and reprinting them would add
nothing you cannot see for yourself.</li>
</ul>

<p>There is a fifth refusal that shaped this edition. Where no primary source could be found
for a number that every blog prints — the ATM fee, the per-withdrawal cap, the typical
sleeper-bus fare — we wrote the structure and left the figure out, rather than copy a number
whose origin nobody could name. A chapter assembled to fill a page is detectable, and it
devalues the chapters that were earned.</p>
""",
}

CLOSING = {
 "plate": "A14",
 "plate_cap": "First light, salt fields near the coast. Nothing on an itinerary; a country at work before the day's heat. It is the hour the book keeps sending you to, and the thing the arithmetic is protecting.",
 "plate_after": 2,
 "kind": "Closing",
 "title": "The country, not the plan",
 "standfirst": "",
 "body": """
<p class="lede">There is a moment, usually on the second or third morning, when the planning
stops mattering. It tends to arrive somewhere ordinary — a lake at six in the morning, full
of badminton and tai chi and old men doing slow exercises in their vests; a pavement at
seven, where a woman who has made one soup for thirty years hands you a bowl and a plastic
stool; a river before dawn, with a boat selling coffee alongside. Nothing about it is a
sight. It is a country working, at an hour most visitors are still asleep.</p>

<p>That is the thing the arithmetic is protecting. Every decision in this book exists to
subtract a small anxiety from the fortnight — the gate that matches, the leg that flies, the
night that was not spent on a coach — so that more of it is available for the parts that
cannot be decided in advance: the lane you turned down because the lanterns were lit, the
cafe you climbed to through what looked like somebody's hallway, the pass seen from a train
window with the sea on one side and the cloud lifting.</p>

<p>Work the sums out before you go. Then put the book down and stop optimising. The country
is better than any plan you can make of it, and it rewards the loose afternoon more than
almost anywhere.</p>
""",
}

ESSAYS = [OPENING, HOWTOREAD, GROUND, BEFOREYOUFLY, DAYZERO]
BACK    = [FAILURE_MODES, BACKMATTER, CLOSING]
