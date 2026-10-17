# content.py — the decisions. The analytical heart of "Vietnam, End to End."
# ─────────────────────────────────────────────────────────────────────────────
# Every decision must land in model.md's bottom-right cell: NON-OBVIOUS to a
# diligent amateur AND HIGH-STAKES. Naive models are MINED from the corpus's own
# "most people / the mistake / widely reported" sentences, never invented.
#
# The organising fact this book turns on:
#   Vietnam runs three climates at once down one 1,650 km line, and the
#   direction you travel it is locked by the international ticket and the
#   e-visa form — both bought before anyone looks at a weather table.
#
# Tokens, substituted at build time (build3.py):
#   {EST} {OFF} {SUR} {VOL}   provenance marks
#   {C:claim-id}              a bound evidence claim (evidence.json display.book)
# cols is a LIST and every row has exactly len(cols) cells — asserted in build3.
# ─────────────────────────────────────────────────────────────────────────────

DECISIONS = [

# ── 01 ───────────────────────────────────────────────────────────────────────
{
 "n": "01", "cat": "Days",
 "plate2": "A23", "plate2_after": 1,
 "plate2_cap": "One road, one valley, the better part of a morning. Distance in the north is counted in hours rather than miles, and this is what a thin line on the map is actually asking of the calendar.",
 "q": "How many days do you really have, and how many regions do they buy?",
 "cols": ["Days of leave", "What the ground will hold"],
 "fig": "days",
 "plate": "A03",
 "plate_cap": "The planning table, before the subtraction. Every pin on this map is a half-day of transfer that is not yet on the calendar, and the honest number is the one left after they are.",
 "lede": (
   "A fortnight off work is not a fortnight in Vietnam. The crossing from the East Coast "
   "runs twenty-two to twenty-six hours each way, the arrival day is lost to a body twelve "
   "hours out of step, and every change of region costs half a day in transfers. By the time "
   "those are subtracted, the itinerary most people draft (three regions, two excursions, a "
   "beach) belongs to a trip about a week longer than the one they booked."
 ),
 "table_title": "The subtraction · counted from the day you leave home",
 "rows": [
   ("10 days of leave {EST}", "2 regions, 1 internal flight, no overnight excursion"),
   ("13 days of leave {EST}", "3 regions, tightly: one excursion in the north"),
   ("17 days of leave {EST}", "3 regions with slack, Huế as a stop, one excursion"),
   ("24 days of leave {EST}", "3 regions plus what a fortnight cuts: Sapa and the delta"),
 ],
 "verdict": (
   "<strong>Count the days on the ground first, then pick adjacent regions, never the two "
   "ends.</strong> Seven days on the ground is two regions done well or three done badly; "
   "ten is the first length at which all three fit; fourteen is the length the country is "
   "built for. North plus centre, or centre plus south — the north-and-south pairing skips "
   "the middle, which is where Huế and Hội An are, and it is the combination people most "
   "often regret. Write the plan out and count the half-days lost to movement: if more "
   "than a quarter of the trip is transfers, remove a region rather than compress the stays."
 ),
 "reasoning": """<p>The arithmetic is unforgiving because none of its terms is optional. {C:timezone} The
westbound flight adds to that offset, so a Monday evening departure lands on Wednesday
morning; the day between went into the crossing and does not come back until the return.
Two weeks of leave is twelve days of Vietnam, and the first of those twelve is written off
before it starts.</p>

<p>Within what remains, the unit that matters is the move. Each region is about an hour's
flight from the next, which sounds like nothing and is in fact a hotel checkout, a transfer,
a domestic terminal, the flight, and a transfer at the far end — most of a day gone, with
one easy thing possible at the other end of it. Three regions in ten days is two of those
days. Add an overnight excursion in the north, which claims two days of its own, and the
centre has shrunk to a single night before anyone has argued about it. {EST}</p>""",
 "for": [
   "then take three → thirteen days of leave or more, one northern excursion, Huế as a day",
   "then take the ends → a returning visitor who has already done the centre",
   "then stretch to Cambodia → three weeks, not two: Angkor needs three days plus a day at each end",
 ],
 "against": [
   "then take two → ten days of leave; the third region is the one you will remember as airports",
   "then take two → travelling with children, where fewer places and longer stays is the whole adjustment",
   "then subtract one → the list already has Sapa and the delta on it and the leave is under three weeks",
 ],
 "note": (
   "{EST} The day-count is the first of four decisions that settle the shape of the trip; "
   "the month, the direction and the anchor region follow in Decision 02. Make them in that "
   "order, because each closes options for the next."
 ),
 "claims": ["timezone"],
},

# ── 02 ── THE FREE HOOK ──────────────────────────────────────────────────────
{
 "n": "02", "cat": "Season",
 "plate2": "A24", "plate2_after": 1,
 "plate2_cap": "The north under its winter grey: cloud sitting on the ridge and none of it burning off. It is not rain and it does not spoil a trip, but it is the version of the country the photographs never show.",
 "q": "Which month, and which end do you start from?",
 "cols": ["Month", "What the line is doing"],
 "fig": "season",
 "hook": True,
 "plate": "A18",
 "plate_cap": "The bay in October: clear water, clear air, the version the brochure shows. The same week, the central coast is in its storm season. The two facts sit in different articles, and the ticket is usually bought before either is read.",
 "lede": (
   "Ask when to visit Vietnam and the internet answers with a month, which only works if "
   "the trip stays in one region. It will not. The classic first trip runs the length of a "
   "country that is running three climates at once, so the month you choose decides which "
   "end is in season, which end carries the risk, and therefore which direction the trip "
   "should run. Most people settle the direction first, by buying the flight, and consult "
   "the weather afterwards."
 ),
 "table_title": "The year, by end of the country · from the site's own weather grid",
 "rows": [
   ("March – April {EST}", "all three regions workable at once; the least compromised window"),
   ("October – November {EST}", "the north at its best; the central coast in typhoon season"),
   ("December – February {EST}", "south dry and bright; Hanoi and Sapa cold, grey, drizzling"),
   ("June – August {EST}", "the centre's beach season; the north hot and wettest; south in afternoon rain"),
   ("September {EST}", "the terrace harvest in the north; storms begin on the central coast"),
 ],
 "verdict": (
   "<strong>Let the month choose the direction, and put the slack where the storm is.</strong> "
   "If the dates are yours, take March or April and the direction barely matters. If they "
   "are not, build around the region your month favours and run the line so that the "
   "weather-sensitive end comes first, while you still have days to move. An autumn trip "
   "meets the central coast's storm season whichever way it runs, so the answer there is "
   "not a direction but a spare half-day kept in the centre and refundable rooms near the "
   "river. The one hard constraint is the airline map: {C:nonstop} A West Coast traveller "
   "who wants the nonstop is starting in the south whether they intended to or not."
 ),
 "reasoning": """<p>The reason this is a decision and not a lookup is that the regions do not share a
calendar. The north has four seasons including a winter that surprises everyone who packed
for Southeast Asia in the abstract; the centre is driest from February to August and then
spends September to November under the storms that flood Hội An's riverside streets in most
years; the south is warm all year and divides into dry and wet rather than hot and cold. {EST}
October is the clearest month on Hạ Long Bay and one of the worst on the Hải Vân Pass, in
the same week.</p>

<p>Direction then follows from three things that are usually settled before anyone asks
the question. The only US nonstop lands in Saigon, so a traveller who needs it starts
south. Open-jaw tickets into one end and out of the other cost little more than a return
and remove the backtrack entirely. And jet lag argues for landing somewhere that absorbs a
slow first day — Hanoi's Old Quarter does; Saigon in the heat does not. When those three
cancel out, start in the harder city with fresh energy and finish in the one with the most
flights home.</p>""",
 "for": [
   "then go south-first → the San Francisco nonstop is what makes the fare work",
   "then go south-first → December to February, when the south is dry and the north is cold; end in Hanoi's mist, do not start in it",
   "then go north-first → September to November, taking the bay and Sapa while they are clear and keeping slack for the centre",
 ],
 "against": [
   "then forget direction → March or April, when every region is workable and the order is a tiebreaker",
   "then forget direction → the trip is the centre only; fly in and out of Đà Nẵng and there is no line to run",
   "then move the dates → the plan is beach-led and the only month available is September or October",
 ],
 "note": (
   "{OFF} {C:tet-2027} Whatever the weather is doing, the lunar new year overrides it as a "
   "planning factor; it moves every year and is Decision 10. Fares and the exact flight "
   "schedule are on the Field Sheet."
 ),
 "claims": ["nonstop", "tet-2027"],
},

# ── 03 ───────────────────────────────────────────────────────────────────────
{
 "n": "03", "cat": "Entry",
 "q": "What does the e-visa form commit you to?",
 "cols": ["Field on the form", "What it locks"],
 "fig": "visa",
 "plate": "A04",
 "plate_cap": "The stamp sometimes grants less time than the visa does. Photograph it at the counter; a careful traveller's most common overstay is a discrepancy nobody checked.",
 "lede": (
   "The e-visa looks like paperwork and behaves like the first route decision of the trip. "
   "Four fields on the form (how long, how many entries, which gate in, which gate out) "
   "are each binding, and none of them can be changed from inside the country. People fill "
   "it in weeks before they have settled whether Cambodia is a loop or an exit, and then "
   "discover at a river border that the form has already decided."
 ),
 "table_title": "The four fields · what each one forecloses",
 "rows": [
   ("Duration {OFF}", "granted as requested, up to 90 days; no extension exists for an e-visa"),
   ("Entries {OFF}", "single is spent the moment you leave; a loop needs multiple or a second visa"),
   ("Port of entry {OFF}", "binding: a visa naming Hanoi will not get you through Saigon"),
   ("Port of exit {OFF}", "binding: a river or land exit on an airport visa fails at the post"),
   ("The print {OFF}", "a paper copy travels with the passport; the official instruction says so"),
 ],
 "verdict": (
   "<strong>Settle the shape of the trip, then apply — never the other way round.</strong> "
   "Decide first whether Cambodia or Laos is an exit, a loop, or absent; whether you land "
   "north or south; and how many days the ground will hold with a buffer at both ends. Only "
   "then fill in the form, on the official site, asking for the duration you need "
   "rather than the three weeks you first guessed. {C:visa-fee} {C:visa-processing} Apply "
   "several weeks out and do not hold non-refundable flights against the lower figure."
 ),
 "reasoning": """<p>{C:visa-90} The premise most people arrive with is that a visa can be adjusted later, because in
most countries it can. {C:visa-noext} The Immigration Department allows in-person extensions
for other categories (sponsored business visas, work-linked visas, residence cards), and the electronic tourist visa is not among them. Agencies advertising an e-visa extension are
selling an exit and re-entry, or a different visa through a sponsor, under a name the
government says does not exist.</p>

<p>The gate rules are two rules wearing one coat, and both must be satisfied. {C:visa-gates}
Flying in is therefore never the problem. The second rule is the binding one. {C:visa-port}
Overland and on the river is where both bite, because only some land crossings accept an
e-visa at all, and the one you intend to use has to be the one you named. The Châu Đốc
boat to Phnom Penh, the Mộc Bài bus, a return through either — each is a line on the form,
filled in before the route existed. {OFF}</p>

<p>The river exit has a second form behind it, and it is Cambodia's. {C:cambodia-evisa} The
boat still runs and the post still stamps; the document it stamps has to have come from a
consulate or the arrival counter rather than the Cambodian website, and that is settled in
the same week as the Vietnamese form, not on the jetty at Châu Đốc.</p>""",
 "for": [
   "then take multiple entry → Vietnam, then Cambodia, then Vietnam again, usually because of a return flight that cannot be changed",
   "then name a land gate → the Mekong boat or the Mộc Bài bus is the exit, and the visa must say so; the river exit also needs a Cambodian visa that is not the Cambodian e-visa",
   "then skip the visa → Phú Quốc only, thirty days or fewer, arriving and leaving the island directly and never clearing the mainland",
 ],
 "against": [
   "then keep it single → one entry, one exit, both by air, which is most first trips",
   "then ask for more days → the plan is loose and the multiple-entry premium is the cheapest flexibility in the trip",
   "then do it earlier → the dates fall near Tết, when the working-day clock stops for a week",
 ],
 "note": (
   "{OFF} {C:declaration} It is separate from the visa, free, and on Vietnam's own account "
   "shortens the queue. Do it. Fees, processing time and the gate count are on the Field "
   "Sheet with their check date."
 ),
 "claims": ["visa-90", "visa-fee", "visa-processing", "visa-noext", "visa-gates", "visa-port", "declaration", "cambodia-evisa"],
 "compare": {
   "traveller": "one US adult, one e-visa application on the official portal",
   "alternatives": ["single entry", "multiple entry"],
   "unit": "USD per application, government fee only",
   "excludes": "agent markups, bank transfer charges",
 },
},

# ── 04 ───────────────────────────────────────────────────────────────────────
{
 "n": "04", "cat": "Road",
 "q": "Ride it yourself, ride pillion, or hire the driver?",
 "cols": ["The way you cover a road", "What you are carrying"],
 "fig": "road",
 "plate": "A05",
 "plate_cap": "The Hải Vân hairpins, pillion. Riding behind someone who reads this road removes the licence problem; it does not remove the road, which is the hazard the State Department writes about at greatest length.",
 "lede": (
   "Renting a motorbike is the trip a great many Americans picture, and it is the one "
   "decision in Vietnam where what is easy and what is legal sit furthest apart. The shop "
   "will hand you the keys against a passport photocopy and ask nothing. That absence of a "
   "check is not permission; it only means the consequences arrive later, usually in a "
   "hospital, when an insurer reads the policy."
 ),
 "table_title": "Six ways to cover the same road · a first-time visitor",
 "rows": [
   ("Rent and ride yourself {OFF}", "illegal without a Vietnamese licence; the insurer may refuse the bill"),
   ("Pillion with an easy-rider {OFF}", "the only lawful two-wheel form for a visitor; a helmet for you as well as the rider"),
   ("Car with a driver {EST}", "the regional legs; costs about what bare rental costs at home"),
   ("Grab bike or car {EST}", "the city hops, a dollar or two, fare fixed in the app"),
   ("Train {EST}", "the coast between Huế and Đà Nẵng, and the overnight legs"),
   ("Fly {EST}", "anything over roughly five hundred miles"),
 ],
 "verdict": (
   "<strong>Do not rent. Everything the bike was for is reachable without it.</strong> "
   "{C:licence} {C:insurance} A bad crash on a Vietnamese road can mean an evacuation bill "
   "in six figures, and riding unlicensed means finding out whether the policy pays at the "
   "worst possible moment. Ride pillion on the one mountain route you came for, take the "
   "train over the pass, hire a car for the regional legs, and use a Grab bike for the "
   "city traffic, which puts you on two wheels in the river with a local at the handlebars "
   "for the price of a coffee."
 ),
 "reasoning": """<p>The naive model is not stupid; it is the one most riders hold, because the roads are
full of visitors on rented scooters and most of them come home. The point is the asymmetry.
Road traffic, not crime, is what puts foreign visitors in hospital here, and the State
Department puts it plainly rather than in a lawyer's hedge: a US licence and an
International Driving Permit from AAA do not work, and converting a licence needs residency
papers a two-week visitor cannot hold. {OFF} Buying the IDP before you fly is money spent on
a document that changes nothing at a Vietnamese roadside.</p>

<p>What the alternatives give up is smaller than it looks. The Hà Giang loop is mostly done
pillion in any case, and the passenger is the one who gets to look at the scenery. A car with
a driver waits while you wander and carries the bags between hotels. The Hải Vân Pass is
better from the railway below it than from the road, and the view is the only reason to be
on the road at all. {EST} The one thing self-drive buys is the lane too narrow for a car —
and {C:zero-alcohol}</p>

<p>The law the shop ignores is Vietnam's own, not only Washington's reading of it. {C:no-licence-act}
Two further rules travel with the pillion seat and the handlebars alike: {C:helmets} And {C:red-light}
Two of the guidebooks still in print say a right turn on red is tolerated outside Hanoi; the
2024 statute says otherwise, and the cameras in both cities read the statute.</p>""",
 "for": [
   "then ride anyway, knowingly → the quiet lanes around Hội An or the flat roads of Ninh Bình, with your own helmet, photographs of every scratch, a photocopy as deposit and no beer at lunch",
   "then rent a bicycle → An Bàng, Tra Quế and the paddies are flat and a few kilometres apart",
 ],
 "against": [
   "then hire the driver → the leg is Huế to Hội An over the pass with luggage, or anything in the delta",
   "then take the easy-rider → Hà Giang or the pass is the reason you came; the road is the day, not the transfer",
   "then take a Grab → it is a city, it is hot, and the distance is more than a mile",
 ],
 "note": (
   "{OFF} Enforcement is tightening rather than relaxing — cameras and higher fines in both "
   "big cities — and the drink-driving limit is zero, not a threshold. A bia hơi evening and a "
   "scooter home is an offence, not a judgement call."
 ),
 "claims": ["licence", "insurance", "zero-alcohol", "no-licence-act", "helmets", "red-light"],
},

# ── 05 ───────────────────────────────────────────────────────────────────────
{
 "n": "05", "cat": "Legs",
 "plate2": "A29", "plate2_after": 1,
 "plate2_cap": "A Vietnam Railways carriage, which is the whole argument in one object: slower than the flight, and the only leg of the trip where the travelling is the thing you remember rather than the thing you endure.",
 "q": "Fly, train, or sleep through it — leg by leg?",
 "cols": ["The leg", "The call"],
 "fig": "legs",
 "plate": "A06",
 "plate_cap": "A four-berth soft sleeper, which is the compartment most visitors want and the version of an overnight that converts hours into sleep you would have paid a hotel for anyway.",
 "lede": (
   "The romantic answer is the train the length of the country, and almost nobody rides it "
   "end to end because there is no reason to: the Reunification line takes a day and a half "
   "to cover what a flight covers in two hours. The practical answer is not one mode but a "
   "rule of distance, with one leg that breaks it on purpose and one leg where the usual "
   "fallback does not exist."
 ),
 "table_title": "Five legs most first trips contain · door to door",
 "rows": [
   ("Hanoi → Saigon, ~1,140 km {EST}", "fly; the train is 32–36 hours, the bus more"),
   ("Hanoi → Đà Nẵng, ~600 km {EST}", "fly, early in the day; 15–17 hours by rail"),
   ("Huế → Đà Nẵng, ~100 km {EST}", "train, sea side; the one leg never worth flying"),
   ("Hanoi → Sapa, ~320 km road {EST}", "day van 5–6 h, or the overnight train; no flight to fall back on"),
   ("Saigon → Cần Thơ, ~170 km {EST}", "road, 3–4 h; there is no useful railway"),
 ],
 "verdict": (
   "<strong>Fly above five hundred miles, never below a hundred and fifty, and take the "
   "train on the coast.</strong> Between those lines it is a toss-up decided by departure "
   "times and whether you would rather sleep through a journey or see it. {C:hue-dn-rail} "
   "It costs very little and replaces a transfer you were making anyway, which makes it "
   "the best-value hour in the country. Book the internal flights early in the day: the "
   "low-cost carriers accumulate delay as the schedule runs, and the leg that connects to "
   "a cruise check-in or an international departure is the one that cannot slip."
 ),
 "reasoning": """<p>The distance rule holds because the airports eat the short hops. Add two transfers,
check-in and security to a one-hour flight and a leg like Huế to Nha Trang is four hours
door to door against a train that leaves from the middle of town. At the other end the
arithmetic inverts: {C:han-sgn-rail} The same journey is a little over two hours in the air,
and the fare gap between the cheapest and dearest carrier on a route is often smaller than
the baggage fee that separates them. {EST}</p>

<p>The overnight legs are a genuine planning tool and a safety decision at once. A sleeper
saves a hotel night and moves a long journey out of daylight; the train does that with a
flat berth and a door, the bus with a berth built to a shorter frame and an operator you
cannot verify from the seat. Reviews describe legroom, not maintenance. The position is that the bus goes places the railway does not, and that where both exist the train is the
one you can assess. {EST} Sapa is the exception that needs slack: every route there is
overland, so a return booked for the day of an international flight has no fallback at all.</p>""",
 "for": [
   "then take the bus → Đà Lạt, Mũi Né, Phong Nha, Cát Bà and the delta towns, where the railway does not go; daytime where possible",
   "then take the overnight train → Hanoi to Huế or to Lào Cai for Sapa, when daylight hours matter more than the fare",
   "then fly short → Côn Đảo, Phú Quốc from the north, Điện Biên: there is no practical alternative",
 ],
 "against": [
   "then do not fly → Huế to Đà Nẵng, ever; and Hội An has no airport or station, so every version of that leg goes through Đà Nẵng by road",
   "then do not take the sleeper bus → with children of any age, or on mountain roads at night if the train exists",
   "then leave a spare day → any thin-schedule route, where a cancelled flight means the next day's, not the afternoon's",
 ],
 "note": (
   "{VOL} Fares and timetables move with the holiday calendar; they live on the Field "
   "Sheet. The three domestic airports each need three hours between an international "
   "arrival and a domestic departure — you clear immigration, collect bags, and change "
   "terminals."
 ),
 "claims": ["hue-dn-rail", "han-sgn-rail"],
},

# ── 06 ───────────────────────────────────────────────────────────────────────
{
 "n": "06", "cat": "North",
 "plate2": "A25", "plate2_after": 2,
 "plate2_cap": "The terraces in their short green-and-gold fortnight. Sapa’s case rests almost entirely on this, and it is the narrowest window anywhere in the northern leg.",
 "q": "The bay, Ninh Bình, or Sapa — which one does the northern leg carry?",
 "cols": ["Excursion from Hanoi", "What it costs the leg"],
 "fig": "north",
 "plate": "A07",
 "plate_cap": "Trang An from above: the same limestone as the bay, on rivers instead of sea, two hours from Hanoi. For a northern leg of four or five days it returns more per day than anything else on this map.",
 "lede": (
   "Hanoi sits at the hub of three excursions that every first-timer wants and almost no "
   "northern leg can hold. A one-night cruise does not occupy one night; the transfer out "
   "takes most of a day and the return most of a morning, so it claims two. Sapa is five to "
   "six hours each way by road, which makes a day there two travel days for one in the "
   "valley. Ninh Bình is two hours. The question is not which is best. It is what the leg "
   "has room for once the first choice has taken its share."
 ),
 "table_title": "Three spokes, in days · a four-to-five-day northern leg",
 "rows": [
   ("Ninh Bình, day trip {EST}", "1 day; the same karst on rivers, two hours each way"),
   ("Hạ Long or Lan Hạ, one night {EST}", "~2 days; the dawn and dusk the day boats miss"),
   ("Hạ Long, day trip {EST}", "1 day, mostly coach; the version most often called thin"),
   ("Sapa, two nights {EST}", "3–4 days with the road; the valley, not the town"),
   ("Hà Giang loop {EST}", "5+ days; replaces Sapa and wants more than it"),
 ],
 "verdict": (
   "<strong>On a short northern leg take Ninh Bình; on a standard one, the overnight bay; "
   "take Sapa only when the mountains are the reason you came.</strong> Ninh Bình returns a "
   "full day of extraordinary landscape for two hours of travel. The bay is worth the "
   "overnight and not worth the day trip, and it is worth asking for Lan Hạ by name, where "
   "the same limestone carries a fraction of the boats. Sapa is five hours of mountain road "
   "in each direction with no flight behind it, and if the trek is the point it earns that; "
   "if it is on the list because it was on a list, it is the addition most people regret. With "
   "two days and no more, read the forecast before you read the brochures: calm and clear, the "
   "boat; cloud, wind or a warning, the rowboat — and sleep in Ninh Bình rather than come back."
 ),
 "reasoning": """<p>The reason the day trip to the bay disappoints is structural rather than bad luck. It is
a long road transfer each way for a few hours on the busiest water, alongside the other day
boats, with a shopping stop on the way; what it cannot deliver is the late afternoon after
the day boats have gone and the early morning before they return, which is what the
photographs are made of. {EST} An overnight buys those two windows, kayaking from the back
of the boat, and an anchorage. Cancellations are decided by the port authority, not the operator, so a cruise never goes on the night before an international flight.</p>

<p>The two-day case is the common one and it has an asymmetry the brochures do not print.
{C:bay-suspension} Ninh Bình's rowboats go out in rain, and a wet day there is a worse day
rather than a lost one. {C:halong-road} So the two places are substitutes and not merely
alternatives: the same transfer, the same limestone, one of them at the mercy of a forecast and
the other not. A cancelled sailing on the morning of departure turns into a Ninh Bình day from
the same hotel if the fallback was already in your head; it turns into a day in Hanoi if it was
not.</p>

<p>Sapa's cost is the road, and the road has no substitute. There is no airport, the
railway stops an hour short at Lào Cai, and the expressway van is the fastest version at
five to six hours. Budget four days for a two-day trek and you are close to what the leg
really costs. {EST} The decision underneath is whether the mountains or the water are the
anchor of the north; the leg rarely holds both without the centre paying for it.</p>""",
 "for": [
   "then take Sapa → mountains and trekking are the reason for the trip; go in September–October or March–May and sleep in the valley, not the town",
   "then take both → three weeks, when Ninh Bình and Sapa stop being a fork",
   "then take Cát Bà instead → independent travellers who would rather sleep on land and take day boats into Lan Hạ",
 ],
 "against": [
   "then skip the bay → it is winter and the mist that photographs well makes the karsts invisible in person; Ninh Bình is the better bet",
   "then take the rowboat → the two-day forecast shows cloud, wind or a storm warning; the port authority grounds the fleet at once and a two-day window has nowhere to move to",
   "then skip Sapa → the leg is four days or fewer; two of them on a mountain road is the wrong trade",
   "then skip the day trip → if the bay matters, do the overnight; if the day is all there is, Ninh Bình gives comparable scenery for half the travel",
 ],
 "note": (
   "{EST} Ask any operator which bay the itinerary covers — Hạ Long, Bái Tử Long or "
   "Lan Hạ — how many cabins the boat has, and what happens when the port authority cancels. "
   "The answers, not the price, separate the tiers."
 ),
 "claims": ["bay-suspension", "halong-road"],
},

# ── 07 ───────────────────────────────────────────────────────────────────────
{
 "n": "07", "cat": "Centre",
 "plate2": "A26", "plate2_after": 2,
 "plate2_cap": "Hội An after the lights go on, which is the hour the town is sold on — and also the hour the day visitors are still in it. The case for sleeping here rather than at the beach is about the hours either side of this one.",
 "q": "Hội An, An Bàng, or Đà Nẵng — and how many nights does the tailor need?",
 "cols": ["Base", "What it costs each day"],
 "fig": "centre",
 "plate": "A08",
 "plate_cap": "Hội An before seven. The same streets at noon are the tourist trap the reviews describe; the base you choose decides whether you are inside the town at the hours when it is this.",
 "lede": (
   "Three places inside an hour of each other produce three different trips, and they are "
   "sold under one label. The Ancient Town is walkable to everything and busiest through "
   "the middle of the day; An Bàng is ten minutes away by bicycle and a different pace "
   "entirely; Đà Nẵng is a city with an airport, forty-five minutes south of neither. The "
   "distances look trivial on a map. They are the entire decision."
 ),
 "table_title": "The three bases · the round trip into the Ancient Town",
 "rows": [
   ("Hội An, in or beside the old town {EST}", "a walk; the quiet hours are yours"),
   ("An Bàng beach {EST}", "20–30 min by bicycle there and back, less by Grab"),
   ("Đà Nẵng {EST}", "~1.5 hours on the road per visit; a base for Đà Nẵng, not Hội An"),
   ("The split, two nights each {EST}", "one transfer; the town early and late, an airport at the end"),
 ],
 "verdict": (
   "<strong>Two nights with the old town as the point: sleep in it. Three or four with "
   "beach time: An Bàng, and ride in. A week, a family, or a flight at either end: Đà Nẵng, "
   "or the split.</strong> Hội An is described as magical and as a tourist trap, and those "
   "are the same streets before seven and at noon; a base inside the town is the only one "
   "that puts you there at the right hours without a plan. The season overrules all of "
   "it: from September to November the beach is the part of the proposition that fails "
   "first, and the streets nearest the river flood in some years."
 ),
 "reasoning": """<p>The tailor sets a floor under the number of nights, and it is the detail most often
discovered too late. A well-made garment needs two fittings, which in practice means
ordering on the first morning and allowing two full days, three for a suit that is meant
to fit. A one-night stop in Hội An is not the trip to have clothes made on, however
persuasive the overnight turnaround sounds. {EST}</p>

<p>Đà Nẵng is a legitimate choice for what it is — a working coastal city with a long
beach, the Chăm sculpture museum, the Sơn Trà peninsula and an airport minutes from the
centre — and a poor substitute for what it is not. Treating Hội An as a day trip from it
costs about an hour and a half on the road every time, which on a two-night stay is a
third of the daylight. {EST} Mỹ Sơn, an hour west of Hội An, belongs to the same leg and
rewards an arrival at opening more than any site in the country; a car that sets the hour
is the thing worth paying for there.</p>""",
 "for": [
   "then take Đà Nẵng → a late arrival or early departure by air, a family wanting more than a beach, or a stay of a week",
   "then take An Bàng → three nights or more, the sea is in season, and dinner in town is a bicycle ride you are happy to make in the dark",
   "then take the split → four nights, and you want the town's quiet hours and an airport hotel on the last night",
 ],
 "against": [
   "then take the town → two nights, the Ancient Town is why you came, or clothes are being made",
   "then abandon the beach base → September to November, when the sea is rough and the sky is grey",
   "then check the river → any Hội An room between September and November; ask how far from the water it sits",
 ],
 "note": (
   "{EST} Entry to the Ancient Town is by a ticket covering a set number of heritage houses; "
   "how many, and how long it stays valid, are reported differently by different visitors — "
   "ask at the booth. The lantern night on the fourteenth of the lunar month is worth "
   "planning the two nights around."
 ),
 "claims": [],
},

# ── 08 ───────────────────────────────────────────────────────────────────────
{
 "n": "08", "cat": "South",
 "plate2": "A27", "plate2_after": 2,
 "plate2_cap": "A flooded cajuput forest in An Giang, at the Cambodian end of the delta and well off the coach circuit. The last block of days in the south turns on whether you want this or the ninety-minute boat with the coconut-candy stop.",
 "q": "What can the last block of days absorb?",
 "cols": ["Ending", "Days it takes"],
 "fig": "south",
 "plate": "A09",
 "plate_cap": "Cái Răng at first light. By mid-morning the big boats have left, and the coach circuits sold in Saigon leave the city at the hour this is ending, so no day trip has ever been here while it was running.",
 "lede": (
   "Almost everyone visiting Saigon is offered the Mekong day trip, and a great many take "
   "it and come back unimpressed, because the thing they were sold happens at dawn four "
   "hours away. The ending of a trip is a fixed block of days before a flight, and the "
   "delta, Phú Quốc, Côn Đảo and a slower city are competing for it at very different "
   "prices in days. The question is not which appeals. It is which the block can hold."
 ),
 "table_title": "What each ending costs · days out of the final block",
 "rows": [
   ("Extra days in Saigon {EST}", "only themselves; Chợ Lớn, District 4, Củ Chi, the rooftops at dusk"),
   ("Mekong, Cần Thơ overnight {EST}", "2 days; the only version that is at Cái Răng while it runs"),
   ("Mekong, coach day trip {EST}", "1 day; staged stops on the near fringe, widely called the weakest day"),
   ("Phú Quốc {EST}", "a flight each way and 3–4 nights to be worth the flight"),
   ("Côn Đảo {EST}", "4–5 days; a thin schedule and a three-night minimum"),
 ],
 "verdict": (
   "<strong>Two weeks or more: the Cần Thơ overnight. One week: skip the delta entirely "
   "rather than spend a day on the coach circuit.</strong> Cái Răng is a working wholesale "
   "market that is winding down by eight in the morning, and the only way to be on the "
   "water at five is to have slept in Cần Thơ; a private boat for two costs little and sets "
   "the hour. If the trip should end on sand, Phú Quốc has the flights and the beach and "
   "wants three nights; Côn Đảo is the quiet one and costs four or five days that a first "
   "fortnight does not have. An extra day in the city costs nothing to absorb, which makes "
   "it the default when the block is short."
 ),
 "reasoning": """<p>The coach circuit is not a scaled-down delta; it is a different product. It goes to Mỹ
Tho or Bến Tre, two hours out, for a boat, a horse cart, a coconut-candy workshop and a short
sampan through a palm canal, and it is reasonable value sold honestly as a day out of the
city. Sold as the Mekong Delta it disappoints, and the floating market some itineraries
include is a much smaller operation near the city, not Cái Răng. {EST}</p>

<p>The endings also have a direction. A delta night sits naturally on the way to Cambodia
by river, Cần Thơ to Châu Đốc to the boat up to Phnom Penh, which turns the end of one trip
into the start of another — provided the e-visa named a river exit (Decision 03). Phú Quốc
and Côn Đảo are flights, and the thin schedule on the island routes means a cancelled
departure costs the next day rather than the afternoon; neither belongs on the last night
before an international connection. {EST}</p>""",
 "for": [
   "then take Phú Quốc → November to March, when the island is dry and the central coast has just finished its storms",
   "then take Côn Đảo → the war and the colonial prison are a specific interest, and the four days exist",
   "then take the river out → three weeks, Cambodia is next, and the visa was filled in for the crossing",
 ],
 "against": [
   "then stay in the city → the block is two days or fewer; the museums, Chợ Lớn and a street-food evening fill them better than a coach",
   "then stay in the city → the flight home is early, and the last night belongs near the airport, not two hours from it",
   "then take a Vĩnh Long homestay → a quiet canal night matters more than the market; closer, quieter, and not at Cái Răng",
 ],
 "note": (
   "{EST} Boats to Cái Răng are booked the evening before at the Ninh Kiều quay or through "
   "the hotel; agree the departure time, the hours on the water, and whether it continues to "
   "Phong Điền. The Chợ Lớn afternoon in Saigon is the thing most short visits skip and most "
   "visitors who did it mention."
 ),
 "claims": [],
},

# ── 09 ───────────────────────────────────────────────────────────────────────
{
 "n": "09", "cat": "Beach",
 "plate2": "A31", "plate2_after": 1,
 "plate2_cap": "Phú Quốc from the west coast at the end of the day. Which month you come decides whether the evening looks like this or like a grey chop, and that is the beach decision in one frame.",
 "q": "Which beach — and does the month leave you a choice?",
 "cols": ["Coast", "Its calm months"],
 "fig": "beach",
 "plate": "A10",
 "plate_cap": "Phú Quốc in its dry season, which runs opposite to the central coast's. The question is never which beach is best; it is which beach is dry when you are there.",
 "lede": (
   "Vietnam's two beach destinations are opposite kinds of place with opposite weather, "
   "and the month settles the question more often than any preference does. Phú Quốc is dry "
   "roughly from November to April and rough from May; Nha Trang is dry from January to "
   "August and wettest in October and November. Picking the wrong one for the month is how "
   "people end up on a grey beach wondering what the fuss was."
 ),
 "table_title": "Five coasts · from the site's own seasonal grid",
 "rows": [
   ("Phú Quốc {EST}", "November – April; the best sand, the most building"),
   ("Nha Trang {EST}", "January – August; a city with a beach, on the railway"),
   ("An Bàng and Đà Nẵng {EST}", "February – August; the beach afternoon inside a trip about something else"),
   ("Côn Đảo {EST}", "March – September; empty, a prison island, four days of transport"),
   ("Mũi Né {EST}", "wind November – April, swimming May – October; never both"),
 ],
 "verdict": (
   "<strong>November or December, Phú Quốc. May to August, Nha Trang. January to April, "
   "either, so decide on character. September and October, no coast is reliable, and the "
   "real question is whether a beach belongs in that itinerary at all.</strong> A first "
   "north-to-south fortnight needs no detour: An Bàng for the afternoons, and Nha Trang if "
   "the route and the month allow. A trip that should end on sand is a flight to Phú Quốc. "
   "Both places disappoint the people who booked the brochure — the unspoilt island that is "
   "now a resort coast, the beach town that is a high-rise city — and that is an expectation "
   "problem the month table prevents."
 ),
 "reasoning": """<p>The character difference is the second decision, and it only opens in the months when
both are dry. Phú Quốc is an island with resorts strung along its coast and a small town in
the middle: you use the property's beach and take taxis to anything else, and the south has
a theme park, a cable car and a built-up resort town that is nothing like the photographs.
Nha Trang is a city of several hundred thousand with a six-kilometre municipal beach along
its front, cheaper, busier, with a large package-tourism layer and a real place to eat
behind it. {EST}</p>

<p>Access decides the rest. Nha Trang is on the railway and the highway, so it drops into a
north-to-south route without a detour; Phú Quốc is a flight and a dedicated leg, which is
why it works as an ending rather than a stop. The island also carries the country's only
visa exemption for Americans — thirty days or fewer, arriving and leaving the island
directly, which helps only if the island is the whole trip. {OFF}</p>""",
 "for": [
   "then take Phú Quốc → the beach is the point, it is November to April, and three nights are available",
   "then take Nha Trang → a beach day inside a longer overland route, in summer, when the central coast is hot and humid",
   "then take Côn Đảo → remoteness and the prison history, with four days and a tolerance for cancelled ferries",
 ],
 "against": [
   "then drop the beach → September or October, when the answer is a city or the north instead",
   "then use An Bàng → the trip already passes Hội An and the only beach you need is an afternoon",
   "then check the building → any Phú Quốc property: recent reviews mentioning construction next door are worth more than the brochure",
 ],
 "note": (
   "{EST} Flags and local advice, not how the water looks, decide whether to swim; rip "
   "currents are a real hazard on the open coast in the windy months, and lifeguards are a "
   "given only on the municipal beaches at Đà Nẵng and Nha Trang."
 ),
 "claims": [],
},

# ── 10 ───────────────────────────────────────────────────────────────────────
{
 "n": "10", "cat": "Calendar",
 "plate2": "A30", "plate2_after": 1,
 "plate2_cap": "Trấn Quốc on the West Lake causeway. Around Tết the pagodas fill while much of the ordinary city shuts, which is the shape of the holiday in one frame: not an empty country so much as a differently occupied one.",
 "q": "Your dates touch Tết. Go through it, or around it?",
 "cols": ["What Tết does", "Which way it pushes"],
 "fig": "tet",
 "plate": "A11",
 "plate_cap": "Peach blossom and kumquat trees in the week before. The spectacle of Tết is in the days leading up to it; on the day itself the streets empty, because the whole country has gone indoors to eat with its family.",
 "lede": (
   "Tết is not a festival a visitor attends; it is the entire country travelling home. "
   "Articles treat it as a week to avoid, which misses the mechanism. It does not make one "
   "week inconvenient. It pushes the transport bookings months earlier than you would "
   "otherwise make them, inverts the usual price relationship between the cities and the "
   "coast, empties the ATMs in small towns, and raises the cost of any plan that leans on "
   "a single mid-trip flight — because that is the link most likely to fail."
 ),
 "table_title": "The four things Tết does to a plan",
 "rows": [
   ("Seats on popular routes {EST}", "book out well ahead and fares rise; on the wanted days the seat may not exist"),
   ("Family-run food, tailors, small operators {EST}", "close for several days, sometimes a week"),
   ("City hotels versus the coast {EST}", "cities can get cheaper as business stops; resorts fill with domestic holidaymakers"),
   ("Banks and small-town ATMs {EST}", "close, run empty, and go unrefilled for days"),
 ],
 "verdict": (
   "<strong>Go around it unless you have a reason to be there, and if you go through it, "
   "fix the transport the day the dates are known.</strong> {C:tet-2027} The disruption "
   "runs about a week either side of the official days, because people travel home before "
   "and back after. A trip that must overlap it should base in a larger city or a resort "
   "area rather than a small town, carry more cash than seems sensible, withdrawn in a city "
   "before the holiday starts, and expect its favourite-looking kitchen to be shuttered. "
   "What it gets in return is the stillest Hanoi you will ever see, temples full and alive, "
   "and the flower markets in the week before, which are a genuine sight."
 ),
 "reasoning": """<p>The date moves with the lunar calendar, usually landing between late January and
mid-February, and it is widely misreported in travel articles written well ahead. The
official holiday is the smaller number; the practical window is wider, and one national
carrier treats a span running into the third week of February as its return-surge period
on routes from Saigon to the north. {OFF} A plan that depends on a Hanoi–Đà Nẵng flight in
that week has put its weakest link exactly where the pressure is.</p>

<p>Two other dates do a smaller version of the same thing and are fixed on the solar
calendar: Reunification Day and Labour Day on 30 April and 1 May, which fill the beaches
and hill towns for a long weekend whose exact shape is announced each year, and National
Day in early September. {C:natday-2027} If the only difference between two possible weeks
is that one contains a national holiday, that is a real reason to pick the other. {OFF}</p>""",
 "for": [
   "then go through it → a Vietnamese connection, an invitation into a home, or a taste for a capital at its quietest",
   "then go through it → a package or a resort stay, which feels the closures far less than independent travel",
   "then use the inversion → a city hotel can be the bargain of the trip in that week; the coast is the opposite",
 ],
 "against": [
   "then move the dates → the plan is independent, food-led, and runs through small towns",
   "then move the dates → the trip has one internal flight on which the whole sequence depends",
   "then move the dates → the e-visa is still to be applied for and the working-day clock stops for the holiday",
 ],
 "note": (
   "{VOL} The dates for your own year, and the government's announced span, are on the Field "
   "Sheet and must be checked there; a Tết date printed in a book is the kind of fact that "
   "goes wrong quietly. Learn <em>chúc mừng năm mới</em>; it is received warmly."
 ),
 "claims": ["tet-2027", "natday-2027"],
},

# ── 11 ───────────────────────────────────────────────────────────────────────
{
 "n": "11", "cat": "Money",
 "plate2": "A28", "plate2_after": 2,
 "plate2_cap": "A market morning, where the card does not reach. The stalls, the xe ôm and the small kitchens are a cash economy, so the number worth planning is what a machine will give you in a day, not what sits in the account.",
 "q": "How much cash, and where does the card quietly stop?",
 "cols": ["Where you are", "What works"],
 "fig": "cash",
 "plate": "A12",
 "plate_cap": "The 500,000 and the 20,000 are both blue-ish polymer and differ by a factor of twenty-five. Learn those two notes before you land; dim light at the end of a long day is where the expensive mistake happens.",
 "lede": (
   "Vietnam is one of the cheapest countries an American can fly to, so the money "
   "decision gets made last — after the flights, after the route, after the bookings that "
   "assumed they could pay. Cards work in four cities and stop; the QR code everyone around "
   "you is scanning is tied to a domestic bank account; the ATM charges a flat fee and caps "
   "the withdrawal. How much you carry and where you can refill draw the boundary "
   "of how far off the main line you can comfortably go."
 ),
 "table_title": "The reach of a foreign card · and what is cash",
 "rows": [
   ("Hotels, chains, malls, mid-to-upper restaurants in Hanoi, Saigon, Đà Nẵng, Hội An {EST}", "card"),
   ("Street food, markets, independent cafés, Grab paid in person, tickets bought locally {EST}", "cash"),
   ("Nearly everything outside the four cities {EST}", "cash"),
   ("VietQR, which every Vietnamese person is using {EST}", "not for a visitor"),
   ("The Sapa valley, the delta, a Tết week in a small town {EST}", "cash, carried in from a city"),
 ],
 "verdict": (
   "<strong>Withdraw the maximum the machine and your bank allow, as rarely as you can "
   "stand, and carry into the countryside what the countryside cannot dispense.</strong> "
   "The ATM fee is flat and the cap is low, so the cost per dollar is set entirely by how "
   "much you take at once: five small withdrawals are five fees. Your own bank's foreign "
   "charge stacks on top and is often the larger half, which is the part within your "
   "control before you fly. Decline the machine's offer to bill in dollars — dynamic "
   "currency conversion is a worse rate every time — change nothing at the airport beyond "
   "the ride to the hotel, and keep a small reserve of clean dollars for emergencies rather "
   "than for spending."
 ),
 "reasoning": """<p>No fee figure is printed here, and that is deliberate: no bank's own foreign-card tariff
could be verified against a primary source, and every number in circulation traces to a
travel blog. The structure is what is true and what lasts — a flat charge, a per-withdrawal
cap, and a US-side fee on top — and the rule follows from the structure without needing the
number. {EST}</p>

<p>Tipping is the other half of the cash question and it is mostly a matter of unlearning.
It is not customary, leaving nothing is normal, and the places it is anticipated are a short
list: private guides and drivers hired by the day, spa therapists, porters, and the pooled
envelope on an overnight cruise. The scams that exist are price-ambiguity rather than theft
— a service begun before a number is named — and one habit prevents nearly all of them:
agree the figure, in đồng, before anything starts. {EST} Crossing a border is the one
place the cash itself is regulated: {C:cash-declare}</p>

<p>The đồng is not a courtesy to the country; it is the law. {C:dong-only} A price quoted in
dollars is therefore the seller's convenience rather than a rate you are bound to, and
settling it in đồng is both the cheaper and the regular course.</p>""",
 "for": [
   "then carry more → the far north, the delta backroads, or any dates inside the Tết window; refill in the last city",
   "then rely on the card → a trip that stays in the four cities and sleeps in chain hotels",
   "then change at a gold shop → it is legal, ordinary, and usually a better rate than the bank; never with someone who approaches you",
 ],
 "against": [
   "then carry less → you are leaving the country into Cambodia, where small dollar notes are useful and đồng is not",
   "then stop tipping → an ordinary phở shop, a market, a cab; rounding up is the gesture, a percentage is a misunderstanding",
   "then count twice → any stack of similar notes, in both directions; it is the zeros, not dishonesty",
 ],
 "note": (
   "{OFF} Every visitor's overnight address is registered with the police; the hotel does it "
   "from your passport at check-in; that is why they ask for it. In a homestay the host is "
   "responsible, and it is worth confirming when you book. {C:host-reg}"
 ),
 "claims": ["cash-declare", "dong-only", "host-reg"],
},
]
