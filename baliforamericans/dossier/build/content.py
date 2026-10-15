# content.py — the decisions. The analytical heart of "Bali, in Its Own Time."
# ─────────────────────────────────────────────────────────────────────────────
# Every decision must land in model.md's bottom-right cell: NON-OBVIOUS to a
# diligent amateur AND HIGH-STAKES. Naive models are MINED from the corpus's own
# "most visitors / the classic mistake / looks like" sentences, never invented.
#
# The organising fact this book turns on:
#   Bali is eighty-nine miles wide and its distances are counted in hours, not
#   miles. Three fixed points — the hour the long flight lands, the sea under
#   the one boat, and the drive to the airport on the last morning — decide
#   where the nights go and in what order. The corpus prints no drive time,
#   because none would be true; neither does this book.
#
# Tokens, substituted at build time (build3.py):
#   {EST} {OFF} {SUR} {VOL}   provenance marks
#   {C:claim-id}              a bound evidence claim (evidence.json display.book)
# cols is a LIST and every row has exactly len(cols) cells — asserted in build3.
# ─────────────────────────────────────────────────────────────────────────────

DECISIONS = [

# ── 01 ───────────────────────────────────────────────────────────────────────
{
 "n": "01", "cat": "Nights",
 "q": "How many nights do you really have, and how many bases do they buy?",
 "cols": ["Nights on the island", "What they hold"],
 "fig": "nights",
 "plate": "A03",
 "plate_cap": "The planner, before the subtraction. The page looks like fourteen days; the trip inside it is twelve nights, two of them slow, one of them half spent leaving, and the arithmetic is the whole of this decision.",
 "plate2": "A25", "plate2_after": 2,
 "plate2_cap": "Rice and coconut palms in the last light, an ordinary roadside somewhere in the centre. A base is wherever you come back to at this hour, and the question of how many you can afford is a question of nights, not of places.",
 "lede": (
   "A week off work is not a week in Bali. There is no nonstop from the United States, so the "
   "journey is two flights and a hub each way; the calendar jumps a day going out; the body "
   "arrives twelve to sixteen hours out of step and spends two days catching up. By the time "
   "those are subtracted, the itinerary most people draft (Ubud, a beach, the north, an island) "
   "belongs to a trip about a week longer than the one on the vacation request."
 ),
 "table_title": "The subtraction · nights on the island, counted from the local arrival date",
 "rows": [
   ("5 nights {EST}", "about three good days; one base; worth it only from inside Asia"),
   ("7 nights {EST}", "about five good days; two bases, Ubud and one coast; no north, east or island"),
   ("10 nights {EST}", "about eight good days; three bases, one of them an island or the east; one spare day"),
   ("14 nights {EST}", "about twelve good days; four bases of three to four nights, moving one way round"),
 ],
 "verdict": (
   "<strong>Count nights on the island, divide by three, and that is your ceiling on bases.</strong> "
   "Seven nights is Ubud and one beach base and nothing else; ten is the first length at which "
   "a third stop fits without rushing the first two; fourteen is the length the island is built "
   "for, and the first at which the far side (Munduk, Amed, Sidemen) stops costing more days "
   "than it gives. A fifth base in two weeks is a trip spent in cars. If the leave is a week, "
   "take the narrow trip on purpose or wait until you can take longer: a rushed week at the far "
   "end of a journey this long is the version people regret."
 ),
 "reasoning": """<p>The arithmetic is unforgiving because none of its terms is optional. {C:timezone} Day and
night are close to reversed, and the CDC's guidance is to allow at least two days before anything
important; on a vacation the important things are the ones you paid for and cannot move. The
flight west crosses the date line, so a Friday evening departure can land on Sunday, and the
hotel night you paid for on Saturday is one you never slept in. The return gives the day back,
and takes a day at home before work. {C:nonstop}</p>

<p>Within what remains, the unit that matters is the move. A hotel change costs about half a day
of packing, a drive and a check-in, and the site's working minimum is three nights in a place,
which gives two full days there; a base of two nights gives one, which is rarely enough to
justify the change. That rule is where the ceiling comes from: nights divided by three is the
upper limit on bases, and it is an upper limit, not a target. {EST}</p>

<p>The island's geography does the rest. The beach areas and the cultural centre are about twenty
road miles apart and the drive between them is slow, so a single base means a long day trip to
reach whichever one you did not choose. One such day is manageable. Three of them is a commute,
and the reason most trips of a week or more split the stay. The quiet regions are further again:
Munduk is about fifty-one road miles from the airport, Amed about sixty-one, and neither works as
a day trip from anywhere a first visit stays. They are a stay or nothing, and a stay is three
nights. {EST}</p>

<p>So each length has a shape, and the shape is not negotiable by enthusiasm. Five nights is one
base and the beach, and most Americans should not fly this far for it. Seven is Ubud and one coast,
with one hotel change and no slack if a day goes to rain or a stomach. Ten adds a third region
(the Nusa islands are the closest, since the boats leave from Sanur) and one spare day, which is
the length the site recommends for a first trip from the United States, and roughly what two
weeks off work becomes once the travel days are counted. Fourteen adds a fourth base and opens
the highlands and the east. Beyond that, the trip is long enough to need a visa extension
decision, which is Decision 04's problem.</p>

<p>The honest move is to write the nights down before writing any places, and to accept what
the number refuses. A traveller who lists Ubud, Seminyak, Uluwatu, the Gilis and Munduk against
nine nights has not planned a trip; they have planned five arrivals.</p>""",
 "for": [
   "then take five nights → you are already in Asia, in the time zone, and the flight is short",
   "then take four bases in fourteen → you want the north or the east, and will move one way round the island, never doubling back through the south",
   "then stay put whatever the length → small children, limited mobility, or a honeymoon that came to rest",
 ],
 "against": [
   "then take two bases, not three → ten nights with a boat in them; the island leg needs slack on both sides, and the slack comes out of a base",
   "then take one base → seven nights with a late-night arrival and an early departure; the second base would be two nights, which is one day",
   "then subtract a base → the list already has the Gilis on it; that side trip costs two travel days on its own and belongs on a fortnight or a return visit",
 ],
 "note": (
   "{EST} The night count is the first of three decisions that settle the shape of the trip; the "
   "order of the bases follows in Decision 02 and the month in Decision 03. Make them in that "
   "order, because each closes options for the next."
 ),
 "claims": ["timezone", "nonstop"],
},

# ── 02 ── THE FREE HOOK ──────────────────────────────────────────────────────
{
 "n": "02", "cat": "Order",
 "q": "Which base first, which last, and where does the boat go?",
 "cols": ["The pinned point", "What it fixes"],
 "fig": "order",
 "hook": True,
 "plate": "A26",
 "plate_cap": "Balangan, on the Bukit, in the late afternoon. The south coast is where a trip should end, not begin: close to the airport, with nothing left to catch, and the body clock finally on the island's time. Spent on arrival, the same beach is slept through.",
 "plate2": "A04", "plate2_after": 1,
 "plate2_cap": "Village compounds beside the paddies outside Ubud. This is where the first mornings belong: a traveller from the United States wakes at five whether they want to or not, and the terraces at that hour are the best use a jet-lagged body will ever be put to.",
 "lede": (
   "Ask where to stay in Bali and every answer is a list of places. The list is the easy half. "
   "The order the places come in is decided by three things the trip cannot move: the hour the "
   "long flight lands, the sea under the one boat crossing, and the drive to the airport on the "
   "last morning. Most people settle the order by booking the beach first, because the beach is "
   "the picture, and only later discover that each of the three pins has landed in the worst "
   "place it could."
 ),
 "table_title": "The three pins · each one is set before the itinerary exists",
 "rows": [
   ("The arrival hour {EST}", "a body twelve to sixteen hours out of step wakes at dawn for two days; the first base should be the one that rewards a five o'clock start"),
   ("The sea {EST}", "the boat answers to the harbour master and the swell, has no fallback, and is roughest in the dry season; it must sit where a lost day costs a beach day"),
   ("The airport run {EST}", "the one drive with a penalty for being late; the last night decides whether it is four miles or sixty-one"),
   ("The visa clock {OFF}", "thirty days, counted from the stamp, not rounded; the order does not change it, but a late extension does"),
 ],
 "verdict": (
   "<strong>Inland first, the island in the middle, the airport's coast last.</strong> Open in "
   "Ubud or its villages, where the dawn waking of jet lag is spent among terraces and temples "
   "that are at their best at that hour and at their worst at eleven. Put the boat, if there is "
   "one, in the middle third, so the return crossing has at least one full day of slack behind "
   "it, two in July, August or the wet months. Finish on the south coast, seven to eleven road "
   "miles from the terminal, with no boat and no long drive between the last full day and the "
   "flight. The same ten nights in the reverse order spend the dawn hours asleep on a beach, "
   "put the only weather-dependent link against the flight home, and end twenty-two miles "
   "inland on the morning of a hard deadline. {C:crossing}"
 ),
 "reasoning": """<p>The reason this is a decision and not a preference is that the three pins are not
symmetrical. Jet lag from the United States is about as strong as jet lag gets, and it has one
useful property: it wakes you early. The site's day-plans use it deliberately, opening in Ubud
so that the first mornings fall among rice terraces and spring temples before the coaches
arrive, and so that the thing you most want to see is not scheduled for a version of yourself
that is not fully present. Spend those mornings on a west-facing beach and they are spent
asleep, because the beach's hour is sunset and the body's is five a.m. {EST}</p>

<p>The sea is the second pin and the least forgiving. Every island in a Bali trip is reached by
small fast boat across open water, and the harbour master's office for the Sanur route issues a
sailing approval for each departure and has told operators not to sail in poor weather. No
cancellation rate exists, so none is printed; what the site does print is the margin: at least
one full day between the boat back and an international flight, two in July and August or the
wet season. The trap is that the dry season is not the calm season. {C:strait} A boat landing at
Sanur at midday with a flight that evening looks comfortable on paper and assumes the morning
sailing ran. From the Nusa islands, if it did not, the only way back is still by sea.</p>

<p>The third pin is the only drive on the island with a deadline. The airport sits on a neck of
land in the south, four road miles from Kuta, seven from Seminyak, eleven from Sanur,
twenty-two from Ubud and sixty-one from Amed, and every one of those passes through the
busiest roads on the island. The site prints no drive times because none would be true at the
hour you read it; what it does say is that the leaving time is an output of where the last night
is, not a separate choice. A last night on the coast makes departure day short and dull. A last
night in the hills, or on an island, makes it long and tense. {EST}</p>

<p>Put the three together and the order writes itself, which is why the site's own week,
ten-day and fortnight routes all run the same way: Ubud, then the island or the far side, then
the coast. The exception the site allows is a late-night arrival, where a drive inland in the
dark after twenty-four hours of travel argues for a first night on the coast instead, close to
the terminal, and a move inland after breakfast. That is a one-night adjustment, not a reversal
of the order.</p>

<p>Everything else about the itinerary is negotiable. These three are not, and a booking made
in the wrong order cannot be corrected by anything bought later.</p>""",
 "for": [
   "then coast first → the flight lands late at night; take the shortest drive to a bed and move inland in the morning",
   "then no island at all → seven nights, or a traveller uneasy in small boats; East Bali gives the quiet without the sea",
   "then the island nearer the end → a Gili leg done by air via Lombok, flown back two days before the international flight; the strait is out of it",
 ],
 "against": [
   "then reverse it → a surf trip in the dry season where the west coast is the whole point and Ubud is a day trip; even then, sleep the last night near the airport",
   "then skip Ubud → a resort honeymoon in Nusa Dua that came to rest; the dawn hours are spent at the pool, knowingly",
   "then keep the boat out of it → a wet-season week; the crossing costs more of a short trip than it gives",
 ],
 "note": (
   "{EST} This is the organising fact of the book, given away whole: the order is the residue of "
   "three pins, and the pins are set by the ticket, the sea and the airport before anyone lists "
   "a hotel. Decision 06 prices the island leg; Decision 09 settles the arrival hour."
 ),
 "claims": ["crossing", "strait"],
},

# ── 03 ───────────────────────────────────────────────────────────────────────
{
 "n": "03", "cat": "Month",
 "q": "Which month, and which coast does it point to?",
 "cols": ["Month", "What the four calendars are doing"],
 "fig": "season",
 "plate": "A05",
 "plate_cap": "A beach from above in the shoulder months, with room on the sand. The rainfall normals say May, June and September; the school calendar at home says July. The two calendars disagree, and the disagreement is the whole decision.",
 "plate2": "A35", "plate2_after": 2,
 "plate2_cap": "Wet-season rain on leaves. It is warm, it is green, and in the south it arrives in bursts rather than days; what it costs is the outings that need a clear sky or a calm sea, which is why a short trip pays more for the dry months than a long one does.",
 "lede": (
   "Ask when to visit Bali and the internet answers with a month, which only works if a trip has "
   "one calendar. It has four. The rain follows one, the crowds follow a second, the surf moves "
   "from one coast to the other with the wind, and the sea under the boats is roughest in the "
   "very months the rain is lightest. Most people choose July because it is dry, and arrive in "
   "the island's fullest, roughest and most expensive weeks."
 ),
 "table_title": "The year, by what each month is doing · from the site's own normals and coast rules",
 "rows": [
   ("May – June {EST}", "rain under four inches and falling; west-coast surf begins; before American schools let out; the least compromised window"),
   ("July – August {EST}", "driest, at about an inch; the northern summer peak; the largest swells and the roughest strait"),
   ("September – October {EST}", "about two and a half inches; after the peak; October is the edge where the rains can return early"),
   ("November – March {EST}", "five to fourteen inches a month, warmest and greenest; east-coast surf; Nyepi and the March cluster; late December full"),
   ("April {EST}", "about four inches after March's nine; shoulder with a wet-season backup plan"),
 ],
 "verdict": (
   "<strong>Take May, June or September if the dates are yours; if they are not, let the month "
   "choose the coast and the length.</strong> The rainfall normals and the crowd calendar point "
   "at the same eight weeks of July and August, and the sea under the boats is at its worst in "
   "exactly those weeks, so the dry peak buys sun at the price of company and a rougher strait. "
   "A surfer's base follows the wind: west and the Bukit in the dry season, Sanur and the east "
   "in the wet. A wet-season trip is a fine trip on a fortnight and a poor one on a week built "
   "around beaches, boats and a sunrise climb, because a short trip has no days to give to the "
   "weather. And any March trip is checked against Nyepi before the ticket is bought. {C:rain}"
 ),
 "reasoning": """<p>The reason this is a decision and not a lookup is that the four calendars are measured on
different things and do not line up. Temperature is not one of them: the Denpasar station's
normals hold between about seventy-nine and eighty-three degrees in every month, so the only
thing the season changes is rain, and it changes that a great deal. The normals come from one
station at sea level by the airport; they say nothing about Ubud, the mountains or the north,
and nothing about how many days it rains or for how long, so the site prints the totals and
refuses to describe a typical day. {EST}</p>

<p>The crowd follows the school year, not the sky. July and August are the driest months and
the northern summer vacation, so weather and calendars point at the same eight weeks; late
December is wet and full at once. The site has no official visitor or price statistics by
month and gives none, which is itself the finding: the shoulder windows of May, June and
September are drier than most people assume and emptier than July, and the gain is space, not
a number. {EST}</p>

<p>The surf is the third calendar, and it is the one that moves the base. The wind reverses
between seasons: the dry-season trades blow offshore on the west-facing coast and hold the
waves up at Canggu and the Bukit; the wet-season north-westerlies do the same on the east, at
Keramas, Sanur and Nusa Dua, and crumble the famous west-coast breaks. A surfer's January base
and July base are on opposite sides of the island, and the drive between them takes time in
the island's traffic. {C:surf-coast}</p>

<p>The fourth calendar is the one first-timers never consult. Rain and swell are separate
things, and the travel-guide sources the site relies on describe the sea between Bali and
Lombok as roughest in July and August, when the swells are strongest; the fast-boat accident at
Sanur in which two passengers died happened in August. A dry-season trip is not a calm-sea
trip, and a July itinerary with an island leg needs the larger buffer, not the smaller one.</p>

<p>Finally the island's own dates, which move every year. In 2027 Nyepi falls on Monday 8
March inside a national holiday cluster that runs without a working day from the sixth to the
fifteenth, and Galungan decorates the roads on 13 January and 11 August. None of these is a
reason not to go; each is a reason to check the decree before the flights, which is Decision
08's subject.</p>""",
 "for": [
   "then take July → a surf trip to the west coast where the largest swells are the point, with the island leg done by air or not at all",
   "then take the wet season → a fortnight, a traveller who values green and quiet over guaranteed sun, and a base with plenty under cover",
   "then take late December → the dates are fixed by the holidays at home; book early and accept the company",
 ],
 "against": [
   "then take October, not September → school-free travellers who can wait; it is drier than May and after the peak, at the price of the wet edge",
   "then take April → a long trip with slack in the second half, where a wet-season backup plan costs nothing if the sun comes",
   "then take any month but March → a week, with a boat in it; the March cluster and Nyepi take a seventh of it before the weather does",
 ],
 "note": (
   "{EST} The month fixes which coast the surf is on and how much slack the island leg needs; it "
   "feeds Decision 02's order and Decision 06's buffer. The rainfall normals are the book's; "
   "the year you travel will differ from them, and the meteorological agency's seasonal "
   "forecast is the thing to read in your travel month."
 ),
 "claims": ["rain", "surf-coast"],
},

# ── 04 ───────────────────────────────────────────────────────────────────────
{
 "n": "04", "cat": "Paperwork",
 "q": "What does the entry stack commit you to, and in what order?",
 "cols": ["The step", "What it fixes, and when it can be done"],
 "fig": "stack",
 "plate": "A34",
 "plate_cap": "A US passport with the boarding pass tucked in it, at the gate. Every later form is filled against this document's number, which is why the renewal comes before the visa and not after: a visa issued against the old passport is a visa for a passport you no longer carry.",
 "plate2": "A24", "plate2_after": 3,
 "plate2_cap": "An airport at dusk, the waiting part. The arrival card cannot be filed before the last three days, which for a journey that crosses the date line means the evening before you leave home or the layover airport, whichever falls inside the window.",
 "lede": (
   "The visa question looks like one form and turns out to be a stack: a passport test, a visa, "
   "a provincial levy, an arrival card and a customs declaration, run by different offices on "
   "different websites with different deadlines. Each is easy. What goes wrong is the sequence, "
   "because one step has to be settled months ahead and one cannot be done until the last three "
   "days, and because several of them silently fix the outer edge of the trip."
 ),
 "table_title": "The stack, in the order it must be done · official fees live on the Field Sheet",
 "rows": [
   ("Passport {OFF}", "six months beyond the landing date, two blank visa pages; endorsement pages do not count; renew before buying anything"),
   ("Visa, the e-VOA {OFF}", "same visa and price as the airport counter; thirty days, extendable once; apply after the flights and the final passport; valid for entry ninety days"),
   ("Levy {OFF}", "a provincial charge on a separate site, by card, once per trip; a voucher per person; it can be asked for at a temple gate"),
   ("Arrival card {OFF}", "free; immigration, customs and health in one; opens only in the last seventy-two hours; a QR code per traveller, including infants"),
   ("Customs {OFF}", "medicine declared and shown in the red channel; one litre of alcohol per adult; the excess is destroyed, not taxed"),
 ],
 "verdict": (
   "<strong>Settle the passport first, then the shape of the trip, then the stack, in that "
   "order.</strong> {C:passport-6m} If it fails that test the trip has a renewal in front of "
   "it, and the visa must be bought against the new number, not the old. Buy the e-VOA on the "
   "official site once the flights and the passport are final: it is the same visa as the "
   "airport counter at the same price, and it removes a queue from the worst hour of the "
   "journey. Pay the levy from home on the province's own site. Leave the arrival card for the "
   "last two days, counted from the local date you land, and screenshot the code. Declare the "
   "medicine. And read the stamp before walking away from the desk, because thirty days is "
   "counted, not rounded. {C:visa-required}"
 ),
 "reasoning": """<p>The stack is five systems because it is three governments' worth of rules. The visa is
national immigration law, the same for Bali as for Jakarta; the levy is a Bali provincial charge
that has nothing to do with the right to enter; the arrival card is a national declaration to
immigration, customs and health at once; and the customs allowances are a third office again.
Paying for one does not cover the others, and many first-time visitors pay for the visa and
assume they are done. {C:levy}</p>

<p>The ordering problem starts with the passport, because it is the only item nothing else can
fix. The visa does not cure a short passport; the levy and the arrival card are filled against
the passport number; and a passport renewed after the e-VOA was bought leaves a visa issued for
a document you no longer carry. The site's four-step check — find the expiry, add six months to
the arrival date, count the empty visa pages leaving out the endorsement pages, confirm it is a
full-validity passport — belongs before the flight purchase, for every traveller in the group,
because a child's passport is issued for a shorter period and can be closer to the line than it
feels. An emergency passport does not work with the visa on arrival at all. {OFF}</p>

<p>The visa fixes the outer edge of the trip in two ways most people notice late. It is thirty
days, which is shorter than most calendar months, so a trip planned as "a month" can run past it
by a day or two, and an expired visa is an overstay whatever the intention. {C:overstay} And
immigration expects an outbound ticket from Indonesia, which a one-way into Bali does not
satisfy and a domestic hop to Lombok does not either; the ticket out of the country is the one
to carry. A stay past thirty days means an extension, which since May 2025 includes a
photograph and an interview at an immigration office, and an office is shut on the holiday
clusters. {C:visa-ext}</p>

<p>The arrival card is the step that cannot be done early. {C:arrival-card} For an American the
window is measured from the local date of landing, which is a day later than the date of
departure, so the practical slot is the evening before leaving home or the layover airport. The
card carries the customs declaration, and medicine is one of the items that sends a passenger
to the red channel; declaring it is the expected behaviour and the inspection is short when the
prescription is in your hand. Alcohol bought at the hub counts toward the one-litre allowance,
and the two-for-one at the departure airport is a bad deal for a solo traveller, because the
excess is destroyed on the spot. {C:customs}</p>

<p>Three small government payments on three websites is also three sets of lookalike sites.
The official addresses end in the government's own domains; a page that quotes more than the
official amount is a third party's page, and the State Department's Indonesia page is the
safest place to start from for all of them.</p>""",
 "for": [
   "then buy the visa at the airport → a trip booked at short notice, an application that failed, or unease about a card on an unfamiliar site; it is the same visa, after a longer queue",
   "then plan the extension in → a stay past thirty days known in advance; set the office visit about two weeks before day thirty, in a base near an immigration office",
   "then get the IDP as well → any chance of renting a car; it is issued at home, and the decision to rent gets made on the spot",
 ],
 "against": [
   "then leave before day thirty rather than extend → a route that passes through another country anyway; each re-entry is a new visa, a new card and the same passport rules",
   "then carry the levy voucher on paper → a day of temple visits far from signal; the stated penalty is refusal at an attraction, not at the airport",
   "then do the card at the hub → a routing with a long daytime layover inside the window; a flat battery at Denpasar is the case the printout is for",
 ],
 "note": (
   "{VOL} The visa fee, the extension fee, the overstay fine, the levy and the customs figures "
   "are set in rupiah or by regulation and move; the Field Sheet carries each with the address "
   "it was read from and the date. The rule that does not move is the order."
 ),
 "claims": ["passport-6m", "visa-required", "levy", "overstay", "visa-ext", "arrival-card", "customs"],
},

# ── 05 ───────────────────────────────────────────────────────────────────────
{
 "n": "05", "cat": "The road",
 "q": "Ride it yourself, ride pillion, or hire the driver?",
 "cols": ["Way to cover a road", "The call, for a first trip"],
 "fig": "road",
 "plate": "A07",
 "plate_cap": "A road in Bali at an ordinary hour: cars, trucks and a great many motorbikes passing on either side. The State Department describes exactly this, and a visitor on a rented scooter with no local riding experience is the most exposed person in the picture.",
 "plate2": "A33", "plate2_after": 2,
 "plate2_cap": "Scooters lined up for rent. Being handed the keys says nothing about whether you may legally ride; the shop checks the deposit, not the licence class, and the gap between the two is what a police stop or a crash will cost.",
 "lede": (
   "The scooter is the cheapest way around Bali and the one every first-timer is handed within "
   "an hour of arriving, which is why the question is usually asked as 'is it safe'. It is the "
   "wrong question. The right one is a chain: the licence class you hold at home decides whether "
   "you are legal, being legal decides what a roadside stop costs, and both bear on what your "
   "insurer says after a crash. Every link was fixed before you left the United States."
 ),
 "table_title": "Five ways to cover a road · scored on the chain, not on price",
 "rows": [
   ("Rent a scooter {OFF}", "legal only with a motorcycle endorsement translated by an IDP; otherwise unlicensed, and the insurer may read the policy after the crash"),
   ("Pillion on a Grab or Gojek bike {EST}", "through the traffic without the handlebars or the liability; a helmet is required for the passenger too"),
   ("App car or Blue Bird taxi {OFF}", "the fare shown before you confirm; a city service, patchy outside the built-up south"),
   ("Car with a driver, by the day {EST}", "the default for any full day out, any luggage, any child, any journey after dark or in rain"),
   ("Self-drive rental car {OFF}", "legal with the IDP and a car licence; the larger vehicle is often presumed responsible in a collision"),
 ],
 "verdict": (
   "<strong>Do not rent a scooter on a car-only licence. A driver for the days out, an app for "
   "the short hops, and your own two feet where the base allows it.</strong> {C:licence} A "
   "permit translates the licence you hold; it cannot add a class. If your US licence carries no "
   "motorcycle endorsement the site's reading of the statute is that you are unlicensed on a "
   "scooter, and the question to put to your insurer in writing is whether you are covered riding "
   "one with the licence and permit you actually hold. The honest answer for most Americans is "
   "that the scooter is not a transport decision at all. It is a base decision: a villa so far from "
   "dinner that only a scooter reaches it is a villa in the wrong place."
 ),
 "reasoning": """<p>The licence is the first link, and it is the one the rental shop will never check. A
rental agreement is not a licence check; being handed a scooter is not evidence that you may
ride it. Indonesia's traffic law requires a licence matching the type of vehicle driven and
treats motorcycles as their own class, separate from cars. An American with a motorcycle
endorsement at home and an International Driving Permit that reflects it holds what the law
describes. An American with a car licence does not, and no official page the site could find
says otherwise. {C:licence-fine} Those are statutory maxima, not a roadside price list, and the
State Department's advice if fined is to ask for an official receipt; it notes that travellers
occasionally report requests for unofficial payments. {OFF}</p>

<p>The second link is physical, and the island's roads make it. Bali is where the State
Department's description of Indonesian traffic is met every day: narrow roads through continuous
built-up areas, shared with cars, trucks and large numbers of motorcycles that weave between
vehicles and pass on either side. A car puts a steel body between you and the same traffic. The
site's advice is blunt about experience: if you have never ridden a motorbike at home, Bali is a
poor place to learn, and left-hand driving, heat and jet lag make it worse. {EST}</p>

<p>The third link shows up only when something goes wrong, and it is the expensive one. A
travel policy may make cover for a motorbike accident depend on the rider being licensed for
that vehicle; it may attach conditions about helmets, engine size, riding as a passenger and
alcohol. The site cannot tell you what your policy says and neither can this book. What it can
say is what the bill looks like without it: {C:medical-pay} An unlicensed rider's position after
a crash is weaker still, because {C:presumed}</p>

<p>The middle options are better than the argument usually allows. Both apps offer a ride on the
back of a motorbike, which gets you through traffic without your holding the handlebars or the
liability, and a passenger in a hired car needs no licence of any kind: the requirement falls on
the person driving. For a full day out, anything with luggage, any group with children and any
journey after dark or in rain, a car with a driver is the site's answer, with the price, the
hours, the stops and whether the car is a registered tourist vehicle agreed in writing the day
before. For short hops in the south, the apps show the fare before you confirm. {EST}</p>

<p>Which leaves the base. The scooter looks attractive when the villa is far from everything,
and a remote base makes it tempting in exactly the proportion that a central one makes it
unnecessary. That is why this decision sits beside Decision 02 and not beside the packing list:
a traveller who chooses a walkable base has already made it.</p>""",
 "for": [
   "then rent → a licensed, experienced rider making short local trips from a base, in daylight, sober, helmet fastened, scooter photographed from every side, passport never left as the deposit",
   "then self-drive a car → an IDP in hand and a reason, such as a family with its own car seat; book through an established company, as the 2025 circular requires",
   "then ride pillion on an app bike → a solo traveller in the south with a short hop and no luggage; the helmet is the law, and the fare is on the screen",
 ],
 "against": [
   "then even the driver is the wrong answer → Nusa Lembongan, where cars are not allowed without village permission; walk, cycle, or hire a ride, and apply the same licence law to the island's motorbikes",
   "then no app either → the Bukit at sunset, a remote waterfall, a temple at dusk: arrange the ride back before you set out, because the app may match a ride out and not one home",
   "then not today → the first two days, in rain, or after a drink; jet lag affects concentration, wet roads are harder, and the circular prohibits riding under the influence",
 ],
 "note": (
   "{VOL} The traffic-law maxima and the State Department's wording are on the Field Sheet with "
   "their addresses. The site's reading that a car-only licence does not cover a scooter is an "
   "interpretation of the statute, stated as such; no official page contradicts it, and none "
   "confirms it."
 ),
 "claims": ["licence", "licence-fine", "medical-pay", "presumed"],
},

# ── 06 ───────────────────────────────────────────────────────────────────────
{
 "n": "06", "cat": "The island leg",
 "q": "A day trip, island nights, the Gilis, or none — and where in the trip?",
 "cols": ["Island leg", "What it costs in days, and what the sea can take from it"],
 "fig": "boat",
 "tailfig": "buffer",
 "plate": "A08",
 "plate_cap": "Boats at anchor with the mountains behind. The crossing is the one link in a Bali trip that depends on the sea, and the board that matters is not the timetable but the harbour master's sailing approval, issued each morning for each boat.",
 "plate2": "A27", "plate2_after": 2,
 "plate2_cap": "Kelingking on Nusa Penida, the island's famous cliff. A day trip sees it from the top at the hour everyone else does; a night on the island sees it early or late, and the path down is a clifftop descent of about four hundred metres that the day-trip schedule has no time for.",
 "lede": (
   "Every Bali itinerary of ten nights or more grows an island leg, and most of them put it at "
   "the end, because the beach is where a trip is supposed to finish. The leg is reached by small "
   "fast boat across open water, it has no fallback except a flight from Lombok, and the sea "
   "that decides whether it runs is roughest in the months the rain is lightest. Where it sits in "
   "the trip is therefore worth more than which island it is."
 ),
 "table_title": "Four island legs · the days they take and the exposure they carry",
 "rows": [
   ("Nusa Penida day trip from Sanur {EST}", "one day and two crossings; covers one side of the island in the day-trip crowd; needs a base on Sanur's side"),
   ("Nusa Lembongan, two or three nights {EST}", "two crossings, days apart; a car-free island with Penida ten minutes away by local boat; a wet landing"),
   ("Nusa Penida nights {EST}", "the cliffs early and late and both sides on separate days; rough roads, simpler services, luggage across on the boat"),
   ("The Gilis, by boat or via Lombok {EST}", "two travel days whatever the route; the open strait or a flight plus a drive; earns its place on a fortnight or a return visit"),
 ],
 "verdict": (
   "<strong>On ten nights, three on Nusa Lembongan with a day on Penida, placed in the middle "
   "third with the boat back at least one full day before the flight. On a week, a Penida day "
   "trip mid-trip or nothing. The Gilis on a fortnight or a return visit.</strong> {C:crossing} "
   "Lembongan is the easier first island stay and the natural base for a Penida day, and the "
   "whole leg hangs on the morning boat from Sanur, so it favours a trip that passes through "
   "Sanur's side anyway. The buffer is the site's own margin: one full day between the return "
   "crossing and an international flight, two in July, August or the wet months. A boat landing "
   "at midday before an evening flight is not a buffer; it is a bet that the morning sailing "
   "ran. {C:strait}"
 ),
 "reasoning": """<p>The arithmetic starts with what each leg costs in days. A Penida day trip is one day and
two crossings, and the site is firm about what it covers: one side of the island, west or east,
and not both, because the roads are rough and the viewpoints are far apart. Island nights cost
the crossings plus the transfer days around them, which on Lembongan is a morning boat out and
a morning boat back with two full days between; a single night is spent mostly on boats and
transfers. The Gilis cost two travel days in either direction whatever the route, because the
short part of the journey is the crossing and the long part is getting to a port or an airport
and from the far end to a bed. On a seven-night trip that leaves five days for everything else;
on fourteen it leaves twelve. {EST}</p>

<p>Then the exposure. The Sanur route crosses the Badung Strait and comes under the harbour
master's office, which issues a sailing approval for each departure and has told operators not
to send boats out in poor weather, pointing them at the meteorological agency's wave forecasts.
The state news agency reported waves above two and a half metres as the line at which boats on
the route are at risk, and reported the capsizing at the harbour entrance in August 2025 in
which two passengers died. A cancelled boat is the system working. The site invents no
cancellation rate; what it says is that sea conditions do not always clear overnight, which is
why it does not count an afternoon as a buffer. {OFF}</p>

<p>The placement follows from the two together. An island leg in the middle third of the trip
turns a cancelled return crossing into an extra beach day with days of slack behind it. The same
leg at the end turns every swell into a threat to the flight home, and from the Nusa islands the
only way back is by sea. The Gilis have one more option, which is to cross to Lombok, drive the
better part of two hours and fly; some travellers take the boat out, when a delay costs beach
time, and fly back, when it would cost more. A domestic flight is a separate ticket with its own
baggage rules, and the site's advice is never to put one on the same day as the flight to the
United States. {C:domestic-bags}</p>

<p>Which island is the smaller question. Lembongan is about eight square kilometres, nearly free
of cars, built for visitors and ten minutes from Penida by local boat; Penida is thirty times
the size, wilder, with rough roads and simpler services. The site's view is Lembongan for a
first island stay, with Penida as a day from there, and that the Gilis, flatter and sandier and
further, belong on a longer trip. Two spots carry specific warnings: rip currents at Dream
Beach, and fatal falls at Devil's Tear, where the barriers are there for a reason. {EST}</p>

<p>The manta trip off Penida belongs to the same arithmetic. It is a small boat on the exposed
side of the island, it is moved or cancelled when conditions are poor, and no operator controls
a wild animal; it wants a spare day after it and suits confident swimmers who do not get
seasick. Everyone else gets a better morning at the calmer snorkelling stops the same boats
make, which many people find the better part anyway.</p>""",
 "for": [
   "then nights on Penida → ten nights or more and photographs without the day-trip crowd are the point; both sides on separate days, and a car with a local driver on the rough roads",
   "then the Gilis → a fortnight or more, with the leg in the middle; fly via Lombok in July, August or the wet season, or if small fast boats are not for you",
   "then the day trip after all → a week, a base on Sanur's side, a morning boat and a return that lands well before dark, with nothing fixed that evening",
 ],
 "against": [
   "then no island → a wet-season week, a traveller uneasy in small boats, or limited mobility; the wet landing and the rough paths are real, and Sidemen or Amed give the quiet without the sea",
   "then the island nearer the end → a Gili leg flown back from Lombok two days before the international flight; the strait is out of the chain, the domestic flight is not",
   "then Lembongan as the beach base itself → a ten-night trip that would otherwise end in the south anyway; return to Sanur with two nights left, and spend them there without a transfer",
 ],
 "note": (
   "{VOL} Crossing times, ports and the wave forecast are on the Field Sheet with their sources; "
   "none is a timetable. The buffer is the site's own margin, not an official rule, and it is the "
   "part of this decision that survives any change in the operators."
 ),
 "claims": ["crossing", "strait", "domestic-bags"],
},

# ── 07 ───────────────────────────────────────────────────────────────────────
{
 "n": "07", "cat": "The day",
 "q": "How many stops does a day hold, and from which base?",
 "cols": ["The outing", "The base it is a short outing from, and what it costs from the others"],
 "fig": "spokes",
 "plate": "A09",
 "plate_cap": "The view a day out mostly consists of: a rural road through the windscreen, somebody else driving. The site prints no drive times because none would be true at the hour you read it; what it prints is the rule that a day holds three or four stops in one direction.",
 "plate2": "A28", "plate2_after": 2,
 "plate2_cap": "Tanah Lot at sunset, which is when everyone comes. Seven road miles up the coast from Canggu and the closest of the four famous temples to the west-coast resorts; the site's advice is the morning, when the light is on the temple and the approach is not a queue.",
 "lede": (
   "Bali is small by American standards and every sight looks like a short drive from every "
   "other. In miles that is true: the airport is twenty-two from Ubud, Ubud is twenty-seven from "
   "the volcano, the four famous temples are in four corners of an island eighty-nine miles wide. "
   "In hours it is not, and the site refuses to print a single drive time because the number "
   "would be wrong for most of the people reading it. The day is planned from a rule, not a clock."
 ),
 "table_title": "The outings, by the base they belong to · road miles are the site's own",
 "rows": [
   ("Tegallalang and the spring temples {EST}", "six miles north of Ubud; a morning from Ubud, a full day from the coast"),
   ("Kintamani and the Batur sunrise climb {EST}", "twenty-seven miles from Ubud, forty-five from Seminyak; the pickup comes well before dawn, and earlier the further south you sleep"),
   ("Uluwatu temple at sunset {EST}", "seventeen miles from Seminyak, thirteen from the airport; the one temple that fits a beach holiday; arrange the ride back first"),
   ("Tanah Lot {EST}", "seven miles from Canggu; go in the morning"),
   ("Besakih and Lempuyang {EST}", "twenty-seven and forty-five miles from Ubud; nine from Amed; a day's driving for a single photograph from the south"),
   ("The Munduk waterfalls and the north {EST}", "fifty-one to sixty-two miles from the airport; a stay in the highlands, not a day trip from Seminyak"),
 ],
 "verdict": (
   "<strong>Three or four stops, in one direction, chosen so the route never doubles back "
   "through the busy south, with the drive home counted as part of the day.</strong> That is "
   "the site's rule and it replaces the clock. Group the sights by the base they are a short "
   "outing from: the terraces, the spring temples and the volcano from Ubud; Uluwatu from the "
   "Bukit or Seminyak; Tanah Lot from Canggu; Besakih from Ubud or Sidemen; Lempuyang only from "
   "Amed. Leave early, so the return drive falls before the late afternoon, when beachgoers, "
   "commuters and sunset-seekers are all moving at once. And check a live map for the actual "
   "hour and the actual day, the night before, then believe the longer of its answer and your "
   "driver's. {C:distances}"
 ),
 "reasoning": """<p>The reason the day is a decision is that the site's distances are stable and the hours are
not, and a first-timer reads the one as the other. The airport is four road miles from Kuta,
seven from Seminyak, twelve from Canggu, eleven from Sanur and thirteen from Uluwatu, and a
newcomer reads those as ten-minute drives. The roads in the south run through continuous
built-up areas and are shared with motorcycles that pass on either side; the routes into the
hills are narrow and winding; a procession or a temple ceremony can close a road for a period
on no timetable a visitor can consult; and heavy rain slows everything, so a drive in January
wants more margin than the same drive in July. None of that is bad luck. It is structural, and
the site's method is to check a live map set to the hour you will actually travel, and to ask
someone who makes the journey every week. {EST}</p>

<p>The day therefore holds fewer stops than the map suggests, and the stops have to lie in one
direction. A base in the far south puts the central highlands at the end of a long drive;
Uluwatu to Ubud is about thirty-four miles through the busiest roads on the island, and a
traveller who wants several days in the hills does better to move base than to commute. The
same arithmetic sorts the four famous temples: Uluwatu and Tanah Lot are easy from the south,
though not together in one sunset; Besakih and Lempuyang belong to Ubud and the east. Few trips
need all four, and Lempuyang, in the site's view, is worth the journey for travellers already
staying around Amed or Sidemen and hard to justify from the south for one photograph that is
taken by numbered turn, with a mirror held under the phone, after a wait that can run to
hours. {EST}</p>

<p>The volcano is the day that most depends on the base. Travel guides put the Batur climb at
about two hours from Toya Bungkah with a required local guide, and the sunrise schedule means
being collected from the hotel in the middle of the night; the further south you sleep, the
earlier the car comes, and the site's advice is not to attempt it from the far south at all.
From Ubud the drive is shorter by a wide margin, and a trip of a week can fit it on the second
or third Ubud morning, never the first, with the rest of that day kept free. Cloud decides the
view, and the caldera rim at Penelokan gives it without the night walk. {C:batur}</p>

<p>Waterfalls follow the same logic with stairs added. Almost every one sits at the bottom of a
valley, so the day is a walk down, time at the water and a climb back in humid air, and the
site's rule is two or three in one direction, paired with a terrace or a temple rather than a
fourth fall. The Ubud group is the easy set; the dramatic ones are in the north and belong to a
stay in Munduk, not a day from the coast. Swimming after heavy rain is the thing to skip, since a
river can rise quickly and the CDC's advice on floodwater applies. {EST}</p>

<p>The driver is the instrument. A car and its driver for the day, with the price, the hours,
fuel, parking, the list of stops and the pickup time in a message you can both refer to, is how
the site's day-plans are run, and the local knowledge of which order to do the stops in is the
thing you are paying for. A driver you have used before is also the right person for the
airport run, which is the one day with a deadline.</p>""",
 "for": [
   "then five stops → a transfer day between bases, where the stops lie along the road anyway and the day's end is a check-in, not a dinner reservation",
   "then one stop → the Batur climb, the manta boat, a Penida day; each is a whole day with the rest of it kept free",
   "then do it from the south → Uluwatu at sunset from the Bukit, Tanah Lot from Canggu; the rest of the island waits for the Ubud nights",
 ],
 "against": [
   "then no driver → central Ubud for a day on foot around the three main streets; the market, the palace and the Monkey Forest are a walk",
   "then not that day → a procession on the road is part of life on the island and a reason to keep slack before anything with a fixed start; it is not a reason to push through",
   "then not from here at all → the north and the far east from a one-week coast base; the drive takes a large share of the time, and the site's answer is a longer trip",
 ],
 "note": (
   "{EST} Entrance fees, hours and guide arrangements change and the site lists none; carry "
   "small rupiah notes and ask the driver the day before. The miles in this decision are the "
   "site's measured road distances; the hours are yours to check on the day."
 ),
 "claims": ["distances", "batur"],
},

# ── 08 ───────────────────────────────────────────────────────────────────────
{
 "n": "08", "cat": "Calendar",
 "q": "Your dates touch March. Through Nyepi, or around it?",
 "cols": ["Date in 2027", "What it does to a trip"],
 "fig": "march",
 "plate": "A10",
 "plate_cap": "An ogoh-ogoh, the demon effigy paraded on the eve of Nyepi before the island falls silent. The night before is the loudest of the year and the day itself the quietest; a traveller has to be inside their accommodation for the second, with a flight that cannot touch either side of it.",
 "plate2": "A29", "plate2_after": 2,
 "plate2_cap": "A temple festival in progress. Galungan and the village ceremonies decorate the island and can close a road for an hour; they do not close it. Nyepi is the one day of the Balinese year that does, and it is on a different calendar from all of them.",
 "lede": (
   "Nyepi looks like a single date to avoid or to seek out, and the blogs treat it as a curiosity: "
   "a day of silence, lights off, a quiet hotel. For a traveller from the United States it is "
   "a different object. The airport halts regular flights for twenty-four hours, mobile data is "
   "switched off, the date moves every year, and in 2027 it falls inside a national holiday "
   "cluster that runs nine days without a working day. The flight that crosses the date line "
   "is the one most exposed to it."
 ),
 "table_title": "March 2027 and the other moving dates · from the official decrees",
 "rows": [
   ("Monday 8 March · Nyepi {OFF}", "regular flights stop from six to six; mobile data and broadcasts off; residents and visitors stay inside their accommodation"),
   ("Wednesday 10 – Thursday 11 March · Eid al-Fitr {OFF}", "a national holiday, with collective leave on the 9th, 12th and 15th: no working day from Saturday the 6th to Monday the 15th"),
   ("13 January and 11 August · Galungan {EST}", "penjor along the roads, families at the temples; not a national holiday, no documented restriction on visitors"),
   ("The other long weekends {OFF}", "Chinese New Year, Good Friday, Eid al-Adha, Vesak, Independence Day: days off for the country, which is a holiday destination for Indonesians too"),
 ],
 "verdict": (
   "<strong>Around it, unless you are coming for it; and if you are, land a full day before, "
   "not the evening before, and sleep that night somewhere you would be content to spend "
   "twenty-four hours.</strong> {C:nyepi-2027} A day lost that way is a seventh of a one-week "
   "trip, and the 2027 cluster means the week around it is a holiday for the whole country, "
   "with rooms and transport booked earlier and side trips treated with more care. Work out the "
   "arrival date in Bali time, since the calendar date you leave home is not the date you land, "
   "and check it against the decree, not a blog: Nyepi fell on 19 March in 2026 and on 8 March "
   "in 2027. Download the maps and tickets the day before; plan any ride for the edges of the "
   "window; and confirm your own flight with the airline, since the 2027 airport hours were not "
   "announced when the site wrote this. {C:holidays-2027}"
 ),
 "reasoning": """<p>The reason Nyepi is a decision rather than a note is that it is the only day on the
Indonesian calendar that comes with island-wide restrictions on visitors, and the restrictions
land on exactly the systems a long-haul traveller depends on. Under a circular from the
communications ministry, mobile data and broadcast television and radio are switched off for
twenty-four hours from six in the morning, with hospitals and vital services exempt and
fixed-line connections not covered; the operators text customers beforehand. For Nyepi 2026 the
airport's general manager announced that all regular commercial flights would halt for the same
twenty-four hours, and the annual joint appeal from Bali's religious and provincial authorities
asks residents and tourists alike not to travel or leave their accommodation. Ride apps need
data, so the edges of the window are the only hours a car can be booked. {OFF}</p>

<p>The six-to-six window is what makes an American itinerary the exposed one. The closure
reaches into the nights on both sides, so a flight due to land late the evening before, or to
leave early the morning after, sits close to the edge. The journey from the United States
crosses the date line and takes more than a day, so a connection that slips by a few hours can
turn a safe arrival into one on the wrong side of the closure, with the visa clock and the
onward-ticket rule unaffected by the reason. That is the site's argument for a full day of
margin on the way in, and for sleeping the Nyepi night in a place chosen for it, with meals and
water arranged, since nobody goes out for either. {EST}</p>

<p>The 2027 cluster changes the arithmetic around it. The national holidays are fixed each year
by a joint decree of three ministers, published the year before; the 2027 list was signed in
September 2026, and it puts Eid al-Fitr two days after Nyepi with collective leave on the days
between and after, so that the holidays and weekends run without a working day from Saturday 6
to Monday 15 March. The site has no official source for which shops or attractions close on
which holiday and states none; what the calendar itself settles is that government offices are
shut, which matters to anyone whose first thirty days end near the cluster and who needs the
immigration office for an extension. {C:galungan-2027}</p>

<p>Galungan is the opposite case and the one people confuse with it. It follows the 210-day
Pawukon calendar, so it comes twice in most years and in a different month each time; it is not
a national holiday, the site found no restriction on visitors attached to it, and what changes
is that Balinese families are at home or at the temple, so a particular driver or guide may not
be working. The sensible version of the day is a morning in a village looking at the penjor, a
light itinerary, and bookings confirmed a few days before. A procession on the road has the
right of way; wait for it.</p>

<p>The rule the site gives is short. Look up that year's Nyepi first, because it is the only
date that can stop an arrival or a departure. Then look at the national list for long weekends,
and at the Galungan dates if you would like to see the festival. The decree is the source; the
blog that gives last year's date is how a trip lands on the wrong side of the window.</p>""",
 "for": [
   "then go through it → a day with no traffic and no aircraft is rare anywhere, and some travellers plan for it on purpose; arrive a full day before, book early, and choose the hotel for the night it is",
   "then plan around the cluster, not just the day → a stay whose first thirty days end in March; start the extension earlier, because the office is shut for most of that week",
   "then choose a Galungan week → the penjor are up, the restriction does not exist, and the only cost is a driver who may be with his family",
 ],
 "against": [
   "then move the dates → a one-week trip; the closure takes a seventh of it, and the holiday cluster around it takes some of the rest in rooms and traffic",
   "then at least move the flights → the dates are fixed by work but the arrival and departure are not; shift both a full day clear of the window and confirm with the airline",
   "then keep the boat out of that week → an island leg against a national holiday cluster on both sides of the closure; the margin the sea needs is the margin the calendar has already spent",
 ],
 "note": (
   "{VOL} The 2027 dates are from the official holiday decree and the Hindu holiday letter; "
   "2028's will be published in 2027. The Field Sheet carries the dates with their sources, and "
   "the airport's Nyepi hours are a row marked confirm with the airline, because no 2027 "
   "announcement existed at this edition."
 ),
 "claims": ["nyepi-2027", "holidays-2027", "galungan-2027"],
},

# ── 09 ───────────────────────────────────────────────────────────────────────
{
 "n": "09", "cat": "The flight",
 "q": "Which hub, one ticket or two, and what hour do you land?",
 "cols": ["Routing", "What it decides"],
 "fig": "hubs",
 "plate": "A11",
 "plate_cap": "A hub terminal, mid-journey. There is no nonstop from the United States, so this room is part of every Bali trip; the question the site puts to it is whether the connection would still work if the first flight landed an hour late, and whether both flights are on one booking.",
 "plate2": "A32", "plate2_after": 2,
 "plate2_cap": "An island and a calm sea from the window on the final leg. The short flight is the easy half of the journey; what it decides is the local hour you land, and that hour decides how far the first bed should be from the terminal.",
 "lede": (
   "The flight looks like a price comparison and is three decisions wearing one fare. The hub "
   "decides how long the final leg is and how many flights a day could rescue a missed one. The "
   "ticket decides who owns the problem when the first flight is late. And the arrival hour, "
   "which nobody compares, decides whether the first night is spent four miles from the "
   "terminal or twenty-two miles inland in the dark after twenty-four hours of travel."
 ),
 "table_title": "The routing, by what each choice fixes · from the site's October 2026 schedule snapshot",
 "rows": [
   ("Through Singapore {EST}", "the shortest final leg, about three and a half hours; the longest first flight"),
   ("Through Hong Kong, Taipei, Tokyo or Seoul {EST}", "the Pacific line from the West Coast; five to eight hours in"),
   ("Through Dubai, Doha or Istanbul {EST}", "ten to thirteen hours in; from the East Coast, about as short as flying west"),
   ("One ticket {EST}", "the airline owns a missed connection and the bag"),
   ("Two tickets {EST}", "sometimes cheaper; you own the delay and the bag; the safe form is a night at the hub"),
 ],
 "verdict": (
   "<strong>One ticket, through the hub with the shortest final leg your home airport allows, "
   "on a connection that would survive an hour's delay, landing at an hour you have already "
   "matched to the first night's distance.</strong> {C:nonstop} For a first trip the site's "
   "advice is the through ticket; two bookings move the risk of a missed flight and a stranded "
   "bag from the airline to you, and the only safe way to use them is an overnight at the hub, "
   "which costs a hotel night and requires that you can enter that country. Then read the "
   "arrival time in Bali's clock: a daytime landing can go anywhere; a dusk landing goes to "
   "the south coast; a late-night landing goes to the shortest drive there is, and moves on "
   "after breakfast. {C:timezone}"
 ),
 "reasoning": """<p>The hub is a real choice because the site's schedule snapshot for Bali's airport lists
dozens of international routes and no American city among them, so every itinerary has a
connection and the question is only where. From the West Coast the East Asian hubs sit on the
straight line to Indonesia; from the East Coast and the Midwest, both directions are possible.
The Department of Transportation's tests for any connection apply to an Asian hub as much as a
domestic one: prefer the least congested connecting airport, consider its weather, and ask what
happens if the first flight is delayed. The site gives no minimum connection time in minutes
because none is official for each hub; its rule is a connection that would still work if the
first flight landed an hour late, and anything tighter is a risk you are choosing. {C:hubs}</p>

<p>The ticket decides who owns that risk. {C:bags-dot} With two separate bookings the question
of what happens when the first flight is late has two airlines to answer it, and the site could
find no official source on how any airline treats a passenger stranded by another's delay, so
it will not describe one; the advice is to ask the second airline before buying, and to assume
the bag will not be transferred, which means collecting it at the hub, entering that country,
and checking in again as a new passenger. The Montreal Convention lets a passenger claim delay
expenses afterwards, with receipts. It is not a seat on the next flight. {OFF}</p>

<p>The return is the same exposure in reverse, and the more expensive one, because the short
flight out of Bali has to arrive in time for the long flight home and a missed long-haul seat is
the dearer thing to replace. A split ticket wants at least as much room on the way back as on
the way out, which is one more reason the site's day-plans end on the coast near the terminal
and keep boats and domestic flights out of the last day. {EST}</p>

<p>The arrival hour is the decision nobody compares, and the site is explicit that it matters
most. Bali is eight hours ahead of UTC with no clock change, so a journey that leaves on a
Friday evening can land on a Sunday, and the hotel night in between is paid for and never slept
in. The CDC's advice after landing is to follow the destination's schedule and get daylight,
which a daytime arrival allows and a midnight one does not. The site's own routes assume a
morning or midday arrival and open in Ubud; its one allowed reversal is for a late-night
landing, where the first night goes to the shortest drive from the terminal and the move inland
waits for the morning. {EST}</p>

<p>Two further items ride on the flight booking and are missed if it is treated as an errand.
The visa application asks for the departure date and a booked return flight, and immigration
can ask for the outbound ticket on arrival, so a one-way into Bali needs its second booking
before the first is useful. And the layover country has entry rules of its own: a transit that
stays inside the terminal is one thing, a bag collected at the hub is an entry, and an entry
stamp uses part of a page that Indonesia's two-blank-page rule was counting on.</p>""",
 "for": [
   "then two tickets → an experienced traveller who has priced the saving against a night at the hub and can enter that country; leave many hours, confirm the cabin allowance of the second airline, and carry the second booking's confirmation",
   "then a stopover on purpose → a fortnight or more, where a night in the hub is a small share of the holiday and puts part of the jet-lag adjustment somewhere worth seeing",
   "then fly east → an East Coast or Midwest departure where the Gulf routing is as short and the connection is looser",
 ],
 "against": [
   "then not Singapore after all → the long first flight is the problem for you; Tokyo or Seoul split the journey, at the price of a longer second leg",
   "then not an evening landing → a solo traveller or a family who would rather pay for a daytime arrival than negotiate a dark terminal and a transfer at midnight",
   "then no layover city at all → a one-week trip; a night at the hub is a seventh of it, and most travellers push through",
 ],
 "note": (
   "{VOL} The hub list and the second-leg hours are a schedule snapshot dated October 2026 and "
   "are on the Field Sheet as such; routes change by season. The ticket rule and the arrival "
   "rule do not."
 ),
 "claims": ["nonstop", "timezone", "hubs", "bags-dot"],
},

# ── 10 ───────────────────────────────────────────────────────────────────────
{
 "n": "10", "cat": "Health",
 "q": "What breaks the chain: the medicine bag, the deposit, or the policy?",
 "cols": ["The link", "What the site could establish, and what it refuses to"],
 "fig": "chain",
 "plate": "A12",
 "plate_cap": "A clinic corridor. The State Department's description of care in Indonesia is measured and the billing is not: a deposit before treatment, mostly in cash, with the insurer reimbursing afterwards from a folder of documents. The question is settled before you need the corridor.",
 "plate2": "A30", "plate2_after": 2,
 "plate2_cap": "Macaques at the Sacred Monkey Forest in Ubud, where the animals live close to visitors. The CDC says rabies-infected dogs are commonly found in Indonesia and its instruction after any bite or scratch is to seek care immediately; whether to be vaccinated beforehand is a decision for the clinic at home.",
 "lede": (
   "Each piece of the health question is manageable on its own: a stomach bug is fluids, a "
   "mosquito is repellent, a scratch is a clinic, a pill is a prescription. What a traveller "
   "needs is how they connect when something goes wrong, because the connections are where the "
   "money is. The pill that was legal at the pharmacy is a narcotic at the border; the clinic "
   "wants a deposit before it looks at you; the policy reads its scooter clause after the crash."
 ),
 "table_title": "The chain, link by link · what each one costs if it fails",
 "rows": [
   ("The medicine bag {OFF}", "ninety days of prescribed medicine; sixty of psychotropics; the narcotic class not at all, prescription or not"),
   ("The border {OFF}", "medicine is a red-channel item, declared and shown with the prescription; no list exists to look yours up"),
   ("The clinic {OFF}", "a deposit before treatment, mostly cash; an ambulance can take forty-five minutes, so a taxi is the ambulance"),
   ("The policy {OFF}", "US plans, Medicare and Medicaid pay nothing abroad; the scooter and evacuation clauses decide whether it helps"),
   ("The animal {OFF}", "rabies is common in the island's dogs; any bite or scratch is washed and seen the same day"),
 ],
 "verdict": (
   "<strong>Settle the chain at home, in this order: the medicine's class, the policy's two "
   "clauses, the clinic's address, and then the habits.</strong> {C:meds} {C:adhd} So the work "
   "is yours: find which class your own prescription falls in, ask your doctor what you would "
   "switch to, carry everything in its original packaging with the prescription and a letter "
   "by generic name, and leave every cannabis and CBD product behind. Read the scooter clause "
   "and the evacuation clause of any policy before paying, because {C:evacuation} Ask your "
   "accommodation on the first day which clinic it would send a guest to and how you would get "
   "there at night. Then the habits: sealed water, food served hot, repellent by day as well as "
   "dusk, no touching any animal, and spirits only from a sealed, labelled bottle."
 ),
 "reasoning": """<p>The first link is the one most likely to catch an American, because it is decided by
class and not by legality at home. Indonesia's food and drug agency writes its guidance by class
of drug: ordinary prescription medicine for up to ninety days' use with a prescription,
psychotropic medicine for sixty, and narcotic-class medicine and precursors not at all, with or
without a prescription. The uncomfortable part is that customs publishes no list of prohibited
medicines and the agency names classes, not products, so no article can tell you drug by drug.
{C:cbd} A gummy for sleep or a cartridge in a jacket pocket is the case that catches people, and
it is a criminal matter, not a customs one. {OFF}</p>

<p>The clinic is the second link, and the State Department's description is the one to plan
from: routine care in the major cities, adequate care harder to find in rural areas, most
foreigners with the means leaving the country for anything beyond basic procedures, and a bill
that starts before the treatment. {C:medical-pay} The site quotes no price for a consultation,
a night or a deposit, because it has no official source and the figures online vary widely;
what it says is to know how you would raise a deposit at short notice, which cards you carry,
and what your daily withdrawal limit is. {C:ambulance}</p>

<p>The policy is the third link and the one that is read too late. Insurance in Indonesia is
usually a way of getting money back, not a card that makes a bill disappear, so the claim is
built from the medical report, the itemised bill, proof of payment and, after an accident, a
police report. Two clauses decide whether it helps at all. The scooter clause may make cover
depend on the rider being licensed for that vehicle, which for a car-only licence is Decision
05's problem. The evacuation clause matters because the State Department says an injured
traveller will likely need to reach a major city and patients pay all transfer costs; what
triggers it, who decides, and where it would take you differ from one policy to the next, and a
policy bought for cancellation alone may contain very little medical cover. {OFF}</p>

<p>The animal link is the one with a decision in front of the flight. The CDC frames the
pre-travel rabies vaccine as two questions, whether your activities raise the chance of contact
and whether you could reach prompt treatment, and says vaccines are typically available after an
exposure; the vaccine does not remove the need for treatment, it simplifies it. Whatever was
decided at home, the rule on the island is fixed: wash the wound with soap and running water and
go to a clinic the same day, whether or not the animal looked healthy. Monkeys at the temples
are the common case, and the forest's rule is no food in hand and bags closed. {C:rabies}</p>

<p>The habits close the chain rather than start it. Travellers' diarrhoea is the commonest thing
that goes wrong and is mostly fluids; the site prints no percentage of visitors who get it,
because none is official. The mosquito question in Bali is dengue and Zika, not malaria:
{C:malaria} Dengue's mosquitoes bite by day, there is no vaccine available in the United States,
and the warning signs come in the two days after the fever breaks, which is the wrong moment to
stop watching. The drink question is methanol and spiking, and the State Department's three
rules cost nothing: watch it poured, accept none from strangers, leave none unattended. {OFF}</p>""",
 "for": [
   "then get the rabies vaccine → remote parts of the island, small children who reach for animals, or a long stay; it is a series of shots and a question for your insurer as well as your doctor",
   "then switch the prescription → a stimulant or a strong painkiller; the alternative is agreed with your doctor at home, since a banned drug cannot be replaced on the island",
   "then buy the policy for the evacuation alone → a trip with diving, a volcano climb or an island leg; check the activity list and the altitude and depth limits by name",
 ],
 "against": [
   "then skip the clinic visit → a scratch that did not break the skin, washed anyway; anything that did is seen the same day, and children and older travellers sooner",
   "then not the pre-travel vaccine → a short stay in the resort south with no animal contact planned; the post-exposure route is the one the CDC says is typically available",
   "then the antibiotics stay in the bag → a mild stomach bug; the CDC reserves them for severe cases, and the decision belongs to your own doctor before the trip, not a pharmacy counter abroad",
 ],
 "note": (
   "{VOL} The advisory level, the CDC's Zika notice, the emergency numbers and the consular "
   "agency's number are on the Field Sheet with their addresses; notices change, so read the "
   "date on the one you open. The medicine classes are the agency's; the drug-by-drug answer is "
   "the reader's to get, and the site says so."
 ),
 "claims": ["meds", "adhd", "evacuation", "cbd", "medical-pay", "ambulance", "rabies", "malaria"],
},

# ── 11 ───────────────────────────────────────────────────────────────────────
{
 "n": "11", "cat": "Money",
 "q": "Which card, how much cash, and where do the small percentages land?",
 "cols": ["Where money leaks", "What it is, and whether it is yours to remove"],
 "fig": "bill",
 "plate": "A13",
 "plate_cap": "Hundred-thousand-rupiah notes. The arithmetic is in the zeros: a ten-thousand and a hundred-thousand note differ by one digit and a factor of ten, and the site's advice is to count them before handing anything over and to be the last person to touch the stack.",
 "plate2": "A31", "plate2_after": 2,
 "plate2_cap": "A QR icon on a phone screen. The codes at every counter in Bali belong to the national payment standard, and the island's rules tell visitors to use them; the cross-border scheme that lets a foreigner scan one connects six Asian countries and not the United States.",
 "lede": (
   "Bali is cheap, which is why nobody looks at the money carefully. The site refuses to print "
   "a daily budget and quotes almost no price, and what it finds instead is a structure: no "
   "single item is large, and six small percentages land on the same dollar. Two of them are "
   "decided at home, by which card you carry and what your bank charges. The rest are decided "
   "by reading the foot of the menu before ordering."
 ),
 "table_title": "The stack on one dollar · structure only; the figures that move are on the Field Sheet",
 "rows": [
   ("Your card's foreign transaction fee {EST}", "set by your own bank and the one cost removable before you leave: carry a card that does not charge it"),
   ("The terminal's offer to bill in dollars {EST}", "dynamic conversion at the terminal's rate; choose rupiah and let your own bank convert"),
   ("Local tax on food, drink and rooms {OFF}", "ten percent in Badung and Gianyar, which cover the resort south and Ubud; often not on the menu price"),
   ("The service charge {OFF}", "a hotel's own rate, distributed to the staff by regulation; where it appears, a tip is a personal extra and not a correction"),
   ("The entertainment tax {OFF}", "bars, nightclubs and spas were set at forty percent from January 2024 and the rate was contested; read how the venue states its prices"),
   ("The changer and the machine {EST}", "a licensed changer shows a number and the central bank's logo; no official figure exists for ATM fees or caps, so the site prints none"),
 ],
 "verdict": (
   "<strong>Two cards on different networks, one of them without a foreign fee; rupiah cash "
   "counted by the zeros for everything small; and no plan that depends on a QR code.</strong> "
   "{C:qris} So the official payments go on the card from home, the large items go on the card "
   "on the island, and the small ones go in cash withdrawn at a bank branch or changed at a "
   "counter that shows its licence. {C:changer} When the terminal offers dollars, decline. Read "
   "the foot of the menu for the line that says whether tax and service are included, and "
   "compare two rooms on the total, since the margin between them can be that line alone. Tip "
   "in rupiah, in the hand of the person you mean to thank, and only where no service charge "
   "has already done part of the job."
 ),
 "reasoning": """<p>The structure starts with what an American cannot use. The QR codes at every counter
belong to the national standard run under the central bank, and the island's 2025 rules tell
visitors to pay with them and to transact in rupiah. The cross-border version that lets a
foreigner scan one with a home banking app connects a short list of Asian countries, and the
United States appears nowhere on the central bank's page; a phone camera reads the code and
moves no money. The site could not settle from an official source whether a short-stay
American can open and fund a local wallet, so it refuses to build a trip on a workaround. That
leaves cards and cash as the two working methods, which is the whole of the decision. {OFF}</p>

<p>The two percentages decided at home are the easy ones. A foreign transaction fee is set by
your own bank, applies to every purchase in rupiah including the visa and the levy paid from
your kitchen table, and is removed by carrying a card that does not charge it. Dynamic
currency conversion is the terminal's offer to bill you in dollars at its own rate, and the
site's advice is the same every time: choose rupiah. Neither is a Bali fee; both are choices
made before the plane leaves. {EST}</p>

<p>The percentages on the bill are regulations, and they explain why the menu price is rarely
the price. {C:tax} A service charge is a different thing from the tax: under an Indonesian
labour regulation it must be distributed to the staff, half shared equally and the rest by
seniority and performance, and the regulation sets no rate, so the figure is the business's own.
A price quoted "plus plus" carries both. The site's practical rule is to look for the line at
the foot of the menu, to ask if it is not there, and to compare rooms and villas on the final
figure for your dates. The entertainment category is the outlier, set at forty percent by the
two regencies' 2023 regulations from January 2024 and publicly contested since; the site cannot
tell you how any venue is classified, only to read how it states its prices. {OFF}</p>

<p>Cash is where the counting happens. Prices are written in thousands and millions and
sometimes with the thousands dropped, so a hundred and fifty is a hundred and fifty thousand,
and the notes are a factor of ten apart on one digit. The State Department says ATMs accept
US-issued cards and may charge a conversion or transaction fee, advises machines in secure
locations such as major bank branches, and the site has no official source for operator fees or
withdrawal limits and quotes none; the half you can check before you fly is your own bank's
schedule. At the changer, agree the amount first, count the notes yourself in front of the
cashier, and do not let anyone recount them after you have. {C:cash-declare}</p>

<p>Tipping is where the structure becomes manners. Where a service charge is on a hotel bill,
part of what you paid already reaches the staff and an extra is a personal thank-you; where
none appears, nothing has gone to them beyond wages. A driver who spent the day with you, a
guide on a climb, a therapist, a porter: cash in rupiah, in the hand. The agreed price for
anything without a posted one is the whole price, and a tip on top is a gift, which is why the
site's advice is to agree the number before the day starts rather than negotiate it at the end.
Foreign coins are the least useful thing to leave anyone.</p>""",
 "for": [
   "then carry more cash → the far side of the island, the Nusa islands and the Gilis, where card acceptance is not something to count on and the ATM may be a boat away",
   "then take the card to the counter anyway → the official sites: the visa takes Visa, Mastercard and JCB; the levy adds American Express; both charge in rupiah",
   "then pay the villa by card through a platform → any deposit to a private host; a bank transfer to a stranger is the money the site says is hardest to recover",
 ],
 "against": [
   "then not the ATM at the airport for the whole trip → enough for the first day's transport and a meal, then a bank branch; the site's advice is secure machines and a check for tampering",
   "then no tip at all → a bill that already carries a service charge at a hotel restaurant; the staff share in it by regulation",
   "then not in dollars → a seller who quotes a price in US dollars; the island's rules require rupiah, and the rate they apply on the day is theirs",
 ],
 "note": (
   "{VOL} The tax rates, the entertainment rate and its status, the cash-declaration threshold "
   "and the customs allowances are on the Field Sheet with their sources. The exchange rate is "
   "not printed anywhere in this book: check it the week you travel and make one rule of thumb "
   "for what a hundred thousand rupiah is worth."
 ),
 "claims": ["qris", "changer", "tax", "cash-declare"],
},

]
