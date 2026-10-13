# -*- coding: utf-8 -*-
"""content.py — Thailand, Covered. The cover and the eight decisions.

Every claim below traces to a named corpus article. Sources are recorded in
`src` so the second-pass check can follow them; nothing here was supplied from
outside the reporting. Where a sentence is quoted, it is quoted because the reporting
said it better than a paraphrase would.

The ledger obeys the 2026-09-18 contract in b-decide.md:
  · `cols` is a LIST, and the builder REJECTS a row whose length differs
  · the unit lives in the header
  · no column is invented to complete a shape — Decision 01 has no defensible
    price column, so it does not have one
"""

BOOK = "Thailand, Covered."
PRESS = "Thailand for Americans · a decision manual"

COVER_PROMISE = (
    "Four of its islands have no airstrip, clinics instead of hospitals, and "
    "three separately-booked legs to reach them. It is the same four every time. "
    "This book works the trip out from there."
)

# The provenance key. Every mark used in the book is defined here and printed on
# the key page in the front matter — a glyph that appears on page 3 and is
# explained nowhere is a decoration, not a citation.
MARKS = {
    "est": "<span class='mk'>●</span>",   # derived from the reporting, not stated in it
    "off": "<span class='mk'>◇</span>",   # a published figure, reported as published
    "sur": "<span class='mk'>▲</span>",   # consistent across every article surveyed
    "vol": "<span class='mk'>◆</span>",   # moves — re-check before you travel
}

MARK_KEY = [
    ("est", "Derived. The reporting supplies the parts; the conclusion is this book's, and is arguable."),
    ("off", "A reported figure, passed on as reported — a fare band, a flight time, an airport rule. Traceable in the source ledger."),
    ("sur", "Stated consistently across the reporting behind this book. Repetition by one desk is consistency, not corroboration."),
    ("vol", "Moves. Season, demand or a timetable changes it. The Field Sheet says where to re-check."),
]

# The key page. A glyph that appears on page 3 and is explained nowhere is a
# decoration, not a citation — so the marks above are printed with their meanings
# before the first decision uses them.
HOWTO = {
 "eyebrow": "Thailand for Americans · how to read this",
 "title": "Eight decisions, in the order they get made",
 "standfirst": (
   "This is not a guidebook and it does not describe Thailand. It takes the "
   "eight choices that are hard to reverse once you are there, and works each "
   "one out to a call you can disagree with."
 ),
 "blocks": [
   ("Every decision answers before it argues",
    "Each one opens with the call and the exception to it, in that order. The "
    "argument, the comparison and the reversal follow. If you read nothing else "
    "on a page, read the box at the top — it is the whole answer, and the rest "
    "is there so you can overrule it on purpose."),
   ("Every comparison names its unit",
    "The table on each decision compares like with like on one stated measure, "
    "and the row that changes the choice is named in words rather than marked "
    "in colour. Where the reporting does not support a column — a price, a "
    "ranking — the column is absent rather than estimated."),
   ("Where the quotations come from",
    "This book is built from 97 articles published on thailandforamericans.com "
    "— the same desk, not an outside authority. Sentences in quotation marks are "
    "verbatim from those articles, and the ledger at "
    "<strong>thailandforamericans.com/sources</strong> lists every one, so any "
    "{off} or {sur} claim can be traced to the page it came from. Where a claim "
    "rests on something other than that reporting, the source is named in the "
    "line itself."),
   ("What this book will not do",
    "It names no hotel, no restaurant, no stall, no elephant venue and no "
    "insurer. It does not rank the islands, because the reporting behind it "
    "describes them and does not score them. Anything that moves faster than a "
    "printed page is marked as such and sent to the Field Sheet at the back."),
 ],
}

DECISIONS = [

# ─────────────────────────────────────────────────────────────── 01 · RIDE ──
{
 "n": "01", "cat": "Ride",
 "nav": "01 · What you may drive",
 "q": "What may you actually drive, and what are you insured on?",
 "src": ["renting-a-car-in-thailand", "grab-and-taxi-coverage-thailand",
         "getting-around-thai-islands-without-a-scooter",
         "thailand-road-conditions-by-region",
         "what-travel-insurance-actually-covers-thailand",
         "thailand-island-distances-and-transport"],

 "scope": "You intend to move around an island under your own steam.",

 "open_call": (
   "<strong>Rent the scooter only if your home licence carries a motorcycle "
   "endorsement.</strong> Not because the shop will ask, and it usually will not, "
   "but because the endorsement is the condition your travel policy attaches to "
   "its motorbike exclusion. Without it you are riding uninsured on the islands "
   "that have a clinic rather than a hospital."
 ),
 "open_exception": (
   "The exception that matters: on Phuket, Samui and Ao Nang the alternative "
   "exists — Grab runs, and songthaews run to a pattern. On Koh Tao, Koh Phangan, "
   "Koh Lanta and Koh Chang it does not, and the ride you decline has to be "
   "replaced with a fixed-rate taxi you arrange each time."
 ),

 "lede": (
   "Every account of Thailand treats the scooter as a question of nerve. It is "
   "not. It is a question of entitlement, and the answer was settled before the "
   "trip, in a licence office at home."
 ),
 "body": [
   ("Driving a car in Thailand requires a valid home driving licence plus an "
    "International Driving Permit issued under the 1949 Geneva Convention. In the "
    "United States, AAA and AATA are the only authorised issuers, at around $20, "
    "same-day in person. {off} That much is widely repeated and correct."),
   ("What is almost never said beside it: <strong>the permit translates the "
    "entitlement you already hold; it does not add one.</strong> A car needs the "
    "ordinary licence an American already has. A motorbike needs a motorcycle "
    "endorsement on that licence, which most Americans do not have and which an "
    "International Driving Permit does not confer. {est}"),
   ("That would be a paperwork footnote if the insurance side did not close on "
    "it. Motorbike riding is commonly excluded from travel policies or requires a "
    "rider, and the motorbike exclusion carries a further condition attached: a "
    "valid motorcycle licence. {est} The two facts are written in different "
    "documents, by different industries, and they meet on an island road."),
   ("There are two costs here and conflating them is what leads people astray. "
    "Police checkpoints are common in tourist areas, and riding without the right "
    "permit or without a helmet typically means a fine of a few hundred baht, "
    "commonly in the region of 400 to 500. {off} Travellers who have been stopped "
    "once reasonably conclude the whole issue is overblown. The fine is not the "
    "risk. Where the exclusion applies, the insurer can deny the claim in full. "
    "Not reduce it: deny it. A serious motorbike injury requiring surgery runs "
    "into the tens of thousands of dollars at a Thai private hospital, and "
    "evacuation is the line item on top of that."),
   ("It is worth being exact about the rental counter, because the transaction "
    "feels like approval and carries none. Vendors rarely check licence details "
    "with any care, and plenty will hand over a bike against a passport photocopy "
    "and a cash deposit. <strong>The vendor not checking is not permission.</strong> "
    "It is simply the reason most people discover the problem after a crash "
    "rather than before one. Two practical corollaries: the helmet is legally "
    "required for rider and passenger and is frequently a condition of the "
    "coverage itself, and the deposit is a photocopy or cash. Never the passport "
    "itself, which in someone else's drawer becomes a bargaining chip in any "
    "dispute about damage. {off}"),
   ("The road is the third fact. Street lighting is poor to absent outside "
    "Bangkok and the main urban areas — island roads, mountain roads and rural "
    "stretches are largely unlit after dark, and most island roads have no "
    "footpaths at all. {sur} This is the most consistent finding across every "
    "region surveyed, and it applies equally to a car, a scooter and someone "
    "walking home from dinner."),
 ],

 "plate": {"slot": "A02", "after": 3, "caption":
   "No footpath, no lighting column, and the carriageway runs straight into the "
   "verge. This is the most consistent single finding in the reporting, and it "
   "applies equally to a car, a scooter and a walk back from dinner."},
 "table_title": "What each option requires, and what it excludes · one island week",
 # No price column. Fares are reported ranges that differ by island, and a
 # ledger that certifies a comparison nobody made is the Rome p12 failure.
 "cols": ["Option", "What it requires of you", "Where it exists"],
 "rows": [
   ("Car",
    "Home licence + IDP (1949 Geneva). No endorsement needed.",
    "Everywhere with road; impractical on Koh Tao"),
   ("Scooter",
    "A <strong>motorcycle endorsement</strong> on the home licence — the IDP does not add it",
    "Everywhere, and rented without the check"),
   ("Grab",
    "Nothing. Fixed price, no negotiation, no language barrier.",
    "Bangkok, Chiang Mai, Phuket, Samui, Ao Nang"),
   ("Songthaew / fixed taxi",
    "Nothing, but a fare agreed each time",
    "All seven; the only option on the four"),
 ],
 "decisive_row": 1,

 "call": (
   "<strong>Count the endorsement before you count the fare.</strong> A day of "
   "songthaew hops is friction; a day of riding without the entitlement your "
   "policy names is a different category of exposure, and it is at its worst "
   "precisely where the scooter is most tempting: the small islands, where the "
   "alternative is thinnest, the road is unlit and the clinic cannot treat what "
   "the road produces."
 ),
 "for": [
   "your licence carries the endorsement → ride, and ride in daylight",
   "you are on Phuket, Samui or Ao Nang → decline it; Grab covers the day",
   "you are staying inside one walkable strip → you need none of this",
 ],
 "against": [
   "no endorsement, and the island has no Grab → budget fixed-rate taxis as a "
   "line item, not as a fallback",
   "you rent anyway → ride as though a motorbike claim would be refused, because "
   "outside your policy's licence condition it may be; decide that deliberately "
   "rather than at the counter",
   "you are still undecided → note that the reporting settles it for you: \"the "
   "travelers who get caught are almost never the ones who planned to ride\"",
 ],
 "note": (
   "{vol} Car rates run roughly 700–1,500 baht a day by class, and island taxi "
   "fares are reported ranges rather than tariffs — both move with season and "
   "demand. The Field Sheet carries what to re-check and where. What does not "
   "move is the entitlement rule."
 ),
},

# ─────────────────────────────────────────────────────────── 02 · SEQUENCE ──
{
 "n": "02", "cat": "Sequence",
 "nav": "02 · How many islands fit",
 "q": "How many islands actually fit, and in what order?",
 "src": ["how-many-days-in-thailand", "island-hopping-thailand",
         "bangkok-to-islands-transport", "7-day-thailand-itinerary",
         "10-day-thailand-itinerary", "2-weeks-in-thailand-itinerary",
         "getting-to-the-southern-islands-by-air", "bangkok-vs-islands-vs-north"],

 "scope": "You are choosing how many places to sleep in.",

 "open_call": (
   "<strong>Two places in a week, three in a fortnight, and one coast whichever "
   "it is.</strong> Not because more is unpleasant, but because a transfer costs "
   "half a day or more at each end and a coast change costs a return to the "
   "mainland. Those are days taken out of the middle of a trip that is "
   "already short at both ends."
 ),
 "open_exception": (
   "The exception is not an island, it is a category. An un-serviced island is "
   "not one transfer: it is <strong>three legs each way</strong>, each with its "
   "own timetable and most often booked separately from the others. Added to a "
   "seven-night trip it does not cost half a day; it costs the whole recovery "
   "margin."
 ),

 "lede": (
   "The reporting is unanimous on the shape of the mistake: \"each island transfer "
   "eats half a day or more,\" and the checklist trip is the one that loses. The "
   "question is not how many islands you can reach. It is how many nights "
   "survive the reaching."
 ),
 "body": [
   ("The subtraction starts before Thailand does. There are no nonstop flights "
    "from the United States, you arrive eleven or twelve hours out of sync with "
    "the East Coast, and the first day is an arrival-and-recovery day, so the "
    "realistic time on the ground is a day or two less than the trip length. {sur} "
    "A seven-night trip is a five- or six-night trip, and it is the middle that "
    "the transfers then come out of."),
   ("Then each move takes its own cut. Bangkok to Phuket or Krabi is about an "
    "hour and twenty-five minutes in the air and roughly half a day door to door "
    "once airport travel at both ends and the thirty-to-sixty-minute run from the "
    "island airport are counted. {off} That is why the one-week shape the reporting "
    "names is three nights in the city and four on one southern island. Not a "
    "compromise, the honest arithmetic."),
   ("The coast is a boundary rather than a preference. The Andaman side runs "
    "roughly November to April and the Gulf mid-year, and \"crossing between the "
    "two coasts mid-trip means returning to the mainland and a long transfer.\" "
    "{sur} A plan with one island on each coast has bought a backtrack in order "
    "to visit two places, one of which is in its wet season."),
   ("And the four change the unit of measurement entirely. A journey to Koh Tao "
    "is \"a flight, a road transfer, and a crossing — three legs, each with its "
    "own timetable, most often booked separately from one another.\" {off} Three "
    "legs out, three back, inside a week, from eleven time zones away."),
 ],

 "fig": "legs",
 "plate": {"slot": "A03", "after": 1, "caption":
   "The fare is the smallest part of the cost. The half-day at each end is the "
   "rest of it, and a second island buys two more of them."},
 "table_title": "What each shape of a seven-night trip leaves you · one coast",
 "cols": ["Shape", "Moves after landing", "What the reporting reports each move costs",
          "What is left"],
 "colw": ["label", "mid", "", ""],
 "rows": [
   ("Bangkok only",
    "none",
    "—",
    "seven nights, all of them urban"),
   ("Bangkok + one serviced island<br>(Phuket, Krabi, Samui)",
    "one flight, one road transfer",
    "about half a day each way, door to door {off}",
    "the reporting's own shape: three in the city, four on a beach"),
   ("Bangkok + one un-serviced island<br>(Tao, Phangan, Lanta, Chang)",
    "three legs each way, separately booked",
    "flight, road transfer, boat — each on its own timetable {off}",
    "four beach nights only if nothing slips {est}"),
   ("Two islands, same coast",
    "two transfers plus the arrival",
    "\"each island transfer eats half a day or more\" {sur}",
    "realistic in a week — and nothing else fits beside it"),
   ("Two islands, opposite coasts",
    "back to the mainland in between",
    "\"a long transfer\" that \"wastes precious days\" {sur}",
    "refused: one of the two is in its wet season"),
 ],
 "decisive_row": 2,

 "call": (
   "<strong>Count moves, not islands.</strong> Every plan in the table reaches "
   "the sea; they differ in how much of the week is spent getting there and how "
   "much margin is left when a crossing is suspended. On a first trip the second "
   "island is the most expensive thing on the itinerary, and it is the item "
   "nobody prices."
 ),
 "for": [
   "seven nights → one base, and day-boats for the rest; \"not every island "
   "needs an overnight\"",
   "ten nights → the reporting's three-and-three-and-three: Bangkok, the north, the "
   "islands",
   "fourteen → three islands on one coast, or two with rest days built in",
 ],
 "against": [
   "you are taking a dive course → the course is the trip. One base, no hopping, "
   "and Koh Tao is the place for it",
   "you are on the Gulf in October–December, or the Andaman in September–October "
   "→ put the buffer day back before you add a second island",
 ],
 "note": (
   "{vol} Crossing times and the domestic schedule both thin outside high season, "
   "and the reduced season overlaps the wetter months when boats are also more "
   "likely to be disrupted. The number of legs to each island does not move."
 ),
},

# ─────────────────────────────────────────────────────────────── 03 · BASE ──
{
 "n": "03", "cat": "Base",
 "nav": "03 · Which island",
 "q": "Which island — and which side of the line?",
 "src": ["thailand-island-distances-and-transport", "which-thai-island-is-right-for-you",
         "medical-care-in-thailand-for-visitors", "medical-evacuation-from-thai-islands",
         "getting-to-the-southern-islands-by-air", "when-ferries-cancel-thailand",
         "krabi-vs-phuket", "grab-and-taxi-coverage-thailand"],

 "scope": "The trip includes an island at all.",

 "open_call": (
   "<strong>Decide which side of the line your trip can afford to be on, then "
   "choose freely inside it.</strong> The line is not size, price or beauty. It "
   "is whether the island has an airstrip and a hospital, or a clinic and a boat."
 ),
 "open_exception": (
   "The reporting supplies both counterexamples itself, and they are worth holding. "
   "Koh Tao has hyperbaric chambers where larger islands may not. \"The "
   "facilities follow the diving, not the population.\" And Samui's airport is "
   "privately operated by Bangkok Airways, so the island with the best air access "
   "has the fewest alternatives when that access fails."
 ),

 "lede": (
   "Four separately observed measures — air access, medical capability, how "
   "many booked legs a journey takes, and what moves you around once you are "
   "there — draw the same line through the same seven "
   "places. That is why this is a threshold and not a theme."
 ),
 "body": [
   ("The reporting reaches it from three directions and notices. From the air side: "
    "\"These are the same four islands that have clinics rather than hospitals, "
    "and Koh Tao and Koh Phangan are among the crossings most frequently "
    "suspended in rough weather.\" From the medical side: \"The place where a "
    "transfer is most likely to be needed is the place where it is slowest to "
    "arrange.\" {sur}"),
   ("On the ground the difference is structural rather than a matter of degree. "
    "Koh Samui and Phuket have full private hospitals capable of handling serious "
    "cases without a transfer. Koh Phangan, Koh Tao, Koh Lanta and Koh Chang have "
    "clinics: they handle ordinary problems and stabilise serious ones. \"On Samui "
    "a serious injury is treated where it happens. On Koh Tao it is stabilised and "
    "moved.\" {off}"),
   ("The daily-movement picture is a separate measurement again, and it does not "
    "follow size. \"A large island with a concentrated centre can involve less "
    "daily movement than a small island with scattered bays.\" Koh Tao is under "
    "eight kilometres long and asks more of you than its size suggests; Ao Nang "
    "is on the mainland and asks almost nothing. {off}"),
   ("One consequence of the movement picture deserves stating here rather than "
    "in Decision 01, because it is settled at this moment and not at that one. "
    "Whether you will end up riding anything is decided by where you sleep. "
    "Islands and towns whose beaches, viewpoints and restaurants are spread out "
    "are the ones where nearly everyone rents something, whatever they intended "
    "when they booked; places with a walkable centre, or cheap and frequent "
    "songthaews, are the ones where a scooter never comes up. {est} By the time "
    "the question is live, the licence endorsement is no longer obtainable."),
   ("So the figure below is not a ranking, and this book will not produce one. "
    "The reporting describes these places; it does not score them. What the table "
    "does is put the four axes in one place, so a trip can be matched to the side "
    "of the line it is equipped to be on."),
 ],

 "fig": "line",
 "plate": {"slot": "A04", "after": 1, "caption":
   "Nothing in this frame is a runway, and nothing in it is a hospital. That is "
   "the whole of Decision 03: the island is chosen from the left-hand columns of "
   "FIG. 1, not from the photograph."},
 "table_title": "FIG. 1 · Seven places, as the reporting reports them",
 "cols": ["Place", "Airstrip", "Medical on the island", "Grab",
          "Getting around it, as reported"],
 "colw": ["narrow", "mid", "mid", "tiny", ""],
 "rows": [
   ("Phuket", "HKT · its own, international", "full private hospital", "yes",
    "48–50 km; songthaew town↔beach, 15–50฿, about 6am–6pm {vol}"),
   ("Koh Samui", "USM · its own <em>(Bangkok Airways only)</em>", "full private hospital", "yes",
    "51 km ring road; songthaew round the ring, 30–150฿, no timetable {vol}"),
   ("Ao Nang / Krabi", "KBV · on the mainland", "mainland hospitals", "yes",
    "not an island; walkable strip, songthaew to Krabi Town every 10–20 min, 50–60฿ {vol}"),
   ("Koh Lanta", "none", "clinic", "no",
    "25–30 km, long and narrow; songthaew to Saladan, 50–100฿ {vol}"),
   ("Koh Phangan", "none", "clinic · hyperbaric chamber", "no",
    "16–18 km, separate bays; road transport reported 50–500฿ {vol}"),
   ("Koh Tao", "none", "clinic · hyperbaric chamber", "no",
    "7.5 km; fixed taxi 300–500฿ for one or two, about 100฿ per extra person {vol}"),
   ("Koh Chang", "none", "clinic", "no",
    "west-coast road; shared trucks, 50–200฿, clustering around ferry arrivals {vol}"),
 ],

 "call": (
   "<strong>The island is not chosen from a photograph; it is chosen from the "
   "left-hand columns.</strong> Airstrip and medical tier are fixed, knowable "
   "while the itinerary is being built, and unknowable at the moment they become "
   "relevant. Everything in the right-hand column can be arranged on arrival."
 ),
 "for": [
   "first trip, seven nights, no diving → the serviced side: Phuket, Krabi and "
   "Ao Nang, or Samui",
   "you want the four → go, but go for longer, and read Decision 05 before you "
   "book the policy",
   "you are travelling with someone whose health you would worry about → the "
   "line is the entire decision",
 ],
 "against": [
   "you are taking a dive course → Koh Tao has the chamber on the island; the "
   "general rule inverts for the specific emergency diving produces",
   "you never leave one walkable strip → Ao Nang is on the mainland and needs "
   "none of this",
 ],
 "note": (
   "{vol} Fares move, and the operating hours of the shared-truck networks on Koh "
   "Tao, Koh Phangan and Koh Lanta \"are not reliably documented anywhere\" — the "
   "honest answer is daylight, with an evening cutoff that varies. The airstrip "
   "and medical columns do not move."
 ),
},

# ──────────────────────────────────────────────────────────── 04 · TRANSIT ──
{
 "n": "04", "cat": "Transit",
 "nav": "04 · Who owns the failure",
 "q": "How do the legs connect, and who owns the failure?",
 "src": ["bangkok-airport-transfer-bkk-dmk", "thailand-domestic-flight-baggage-and-changes",
         "domestic-flights-vs-overnight-train-thailand", "when-ferries-cancel-thailand",
         "getting-to-the-southern-islands-by-air", "trains-in-thailand-guide"],

 "scope": "Any trip with a domestic leg, which is nearly every trip.",

 "open_call": (
   "<strong>Put the domestic leg on the same ticket as the long-haul, or accept "
   "in advance that you own every failure on it.</strong> Separate bookings are "
   "separate contracts: the onward carrier owes you nothing for a connection "
   "missed because the inbound ticket failed, and the bag is not through-checked. "
   "Plan as though the replacement ticket is yours to buy."
 ),
 "open_exception": (
   "When the two ends genuinely cannot go on one ticket, put the <em>slack</em> "
   "there instead. An overnight in Bangkok rather than a same-day connection; the "
   "earlier crossing rather than the later one, because \"if a day's sailings are "
   "going to be cancelled, the later ones are likelier to go first.\""
 ),

 "lede": (
   "Most travellers assume an invisible safety net spans the legs of one trip, "
   "because the legs feel like one trip. It does not exist, and the place it most "
   "often fails is a fifty-kilometre gap in the middle of Bangkok."
 ),
 "body": [
   ("Bangkok has two airports about fifty kilometres apart, and travellers "
    "routinely book an international arrival at one and a domestic departure from "
    "the other without noticing. Suvarnabhumi takes full-service and most "
    "international carriers; Don Mueang takes primarily low-cost carriers and a "
    "large share of the domestic network. \"They are separate airports roughly 50 "
    "km apart by road, not two terminals of the same place.\" {off}"),
   ("None of the connection happens airside. You clear immigration, reclaim "
    "checked baggage, exit to landside, cross fifty kilometres of Bangkok, and "
    "check in again from scratch: \"a complete re-entry into the system, not a "
    "transfer within one.\" The road leg runs forty-five to sixty minutes "
    "off-peak and ninety minutes to two and a half hours in traffic, and the hour "
    "is set by when your inbound lands rather than by anything you choose. {off}"),
   ("For a connection between the two airports, <strong>no official minimum "
    "connection time is published at all.</strong> That absence is itself the "
    "fact: the figures circulating in guides and forums cite no airport or "
    "airline standard. What exists instead is the arithmetic above. {off} The "
    "free inter-airport shuttle is real but narrow. It runs for transferring "
    "passengers who can show an onward boarding pass and a passport, and the "
    "airport authority states that non-connecting passengers are not eligible, so "
    "a night in the city between two flights pays its own way in both directions."),
   ("The same structure decides the small things. Bags are through-checked to "
    "the final destination on a single ticket and between codeshare partners, and "
    "not across separate bookings, which is the mechanical reason each step has "
    "to be repeated. And a carry-on-only low-cost fare and a transpacific "
    "suitcase are not compatible; the add-on bought at the airport costs more "
    "than the same add-on bought at booking. {off}"),
 ],

 "fig": "gap",
 "fig_at": "close",
 "plate": {"slot": "A05", "after": 1, "caption":
   "Baggage Claim 4 at Suvarnabhumi, with Udon Thani and Chiang Mai on the board "
   "— the second of the five steps. Between two separately booked tickets it "
   "happens in full, and then again at the far end of fifty kilometres of road."},
 "table_title": "Four ways to join the legs, and who rebooks you when one fails",
 "cols": ["How the legs are booked", "Your bags", "Who rebooks you",
          "What it costs when it fails"],
 "colw": ["label", "mid", "", ""],
 "rows": [
   ("One ticket, or codeshare partners on one itinerary",
    "through-checked to the final destination",
    "the airline that sold it",
    "a rebooking"),
   ("A separate domestic ticket, same airport",
    "reclaim, and check in again",
    "nobody — neither carrier has an obligation to the other's passenger",
    "the domestic ticket is forfeit; buy a new one"),
   ("A separate domestic ticket, the <em>other</em> Bangkok airport",
    "reclaim, cross 50 km, check in from scratch",
    "nobody — and no published minimum connection time to argue from",
    "45–60 min off-peak; 90 min to 2½ hours in traffic {off}"),
   ("A combined bus-and-boat or flight-and-boat ticket",
    "—",
    "depends on who sold it; when only the boat fails, the onward portion is often not covered",
    "read the terms at purchase, not at the pier"),
 ],
 "decisive_row": 2,

 "call": (
   "<strong>The question is never which leg is fastest. It is which leg, if it "
   "fails, you have to buy twice.</strong> Ask it once, at booking, while both "
   "tickets are still hypothetical. It is the only moment at which the answer "
   "is still free to change."
 ),
 "for": [
   "one ticket end to end → a same-day connection is a reasonable plan",
   "separate tickets → overnight in Bangkok and fly south fresh the next morning",
   "the boat leg is carrying something that matters → book it direct with the "
   "operator, one fewer party between you and the rebooking",
 ],
 "against": [
   "you are coming back from an un-serviced island on departure day → come back "
   "the day before. A delayed domestic flight that causes a missed international "
   "departure is the traveller's problem, not the carrier's",
   "you are set on the sleeper → book the berth weeks ahead, and from Krung Thep "
   "Aphiwat Central Terminal. Hua Lamphong, named in most older guides, is no "
   "longer the long-distance terminus",
 ],
 "note": (
   "{off} The sleeper runs about 12½–13 hours to Chiang Mai and 11–13 toward "
   "Surat Thani, arriving early and removing a hotel night. {vol} Domestic "
   "schedules thin outside high season, and last departure times from the "
   "southern airports are not reliably documented — \"anyone quoting a confident "
   "last-flight time is working from a schedule that may have changed.\""
 ),
},

# ───────────────────────────────────────────────────────────── 05 · INSURE ──
{
 "n": "05", "cat": "Insure",
 "nav": "05 · What a policy answers",
 "q": "What are you exposed to, and what does a policy actually answer?",
 "src": ["what-travel-insurance-actually-covers-thailand",
         "medical-evacuation-from-thai-islands", "medical-care-in-thailand-for-visitors",
         "travel-insurance-thailand", "thailand-travel-health-guide"],

 "scope": "You are going to an island with clinic-level care.",

 "open_call": (
   "<strong>Buy the policy for the evacuation line rather than the medical "
   "line.</strong> In an emergency, get treated first: nothing on this page is a "
   "reason to delay care. Whenever circumstances allow — and for anything that is "
   "not an emergency they usually do — <strong>call the assistance line before "
   "the billing is arranged</strong>. That call is what decides whether the "
   "hospital bills your insurer or bills you."
 ),
 "open_exception": (
   "The distinction the industry blurs and the reporting does not: \"evacuation and "
   "repatriation are separate benefits.\" A policy with evacuation and no "
   "repatriation \"will get someone from Koh Tao to a Bangkok hospital\" — and "
   "stop there."
 ),

 "lede": (
   "A travel policy is four or five separate coverages sold as one product, and "
   "the gap between what it covers and what a traveller assumes it covers \"usually "
   "sits in the definitions rather than in the fine print.\""
 ),
 "body": [
   ("Start with the mechanic, because it decides more than any coverage limit. "
    "Thai private hospitals commonly require payment, or a guarantee of payment, "
    "before treating a foreign patient. Direct billing happens when the insurer "
    "issues a guarantee of payment to that specific hospital: a document, "
    "arranged through the assistance line, not something the hospital produces on "
    "request. {off}"),
   ("The consequence is blunt: \"calling after treatment turns a potential "
    "direct-billing case into a reimbursement case.\" Under reimbursement someone "
    "needs the funds available at the moment of the emergency, potentially a "
    "large sum, on a card, in a country far from home. The difference is not "
    "administrative."),
   ("The scale is what makes it a decision rather than a formality. Medical "
    "evacuation from a Thai island runs into the tens of thousands of US dollars, "
    "with a dedicated air ambulance at the higher end and a commercial flight "
    "with a medical escort at the lower. {off} And American domestic health "
    "insurance generally provides little or no coverage abroad and almost never "
    "covers evacuation at all."),
   ("One practical detail the reporting insists on and no policy schedule mentions. "
    "The insurer's assistance line coordinates the evacuation. Not the patient, "
    "not the treating clinic, not a family member calling from home. So the "
    "number that matters is the one printed on the policy, and \"it is worth "
    "having it somewhere other than an email inbox on a phone that may be in a "
    "bag on a boat.\""),
 ],

 "plate": {"slot": "A06", "after": 2, "caption":
   "Where the street looks like this, the clinic is a first response and the "
   "hospital is somewhere else. What the policy is really buying is the journey "
   "between them."},
 "table_title": "What each coverage answers, and the Thai scenario it answers it in",
 "cols": ["The coverage", "What it actually pays for", "The scenario on this trip",
          "What it is mistaken for"],
 "rows": [
   ("Emergency medical",
    "sudden, unexpected illness or injury during the trip",
    "a clinic visit on Koh Lanta; a hospital stay on Samui",
    "routine or planned care, and follow-up once home — neither is covered"),
   ("Evacuation",
    "the move to the nearest facility capable of treating you",
    "Koh Tao to Samui, Phuket or Bangkok — tens of thousands of dollars {off}",
    "the flight home, which is a different benefit entirely"),
   ("Repatriation",
    "the return to your home country",
    "the flight home after the Bangkok hospital",
    "evacuation, which stops in Bangkok"),
   ("Trip interruption",
    "problems met once the trip has already started",
    "a suspended crossing that eats a separately booked flight",
    "cancellation — which is the one that gets advertised"),
   ("Direct billing vs reimbursement",
    "not a coverage but a mechanic: a guarantee of payment issued to the hospital",
    "whether you hand over a card during the emergency, or a deductible",
    "an administrative detail"),
 ],
 "decisive_row": 4,

 "call": (
   "<strong>Two questions to the insurer, before buying: do you direct-bill in "
   "Thailand, and does this policy include repatriation as well as "
   "evacuation?</strong> Neither answer usually appears in the schedule, and both "
   "of them change what happens on the worst day of the trip."
 ),
 "for": [
   "you are diving, riding or climbing → buy the rider, or the exclusion applies "
   "to the exact activity you came for",
   "you are going to the four → evacuation <em>and</em> repatriation, both named "
   "in the schedule",
   "you have a pre-existing condition → the waiver, and the stability period it "
   "requires beforehand",
 ],
 "against": [
   "you are in Bangkok the whole time → the medical-geography argument weakens; "
   "the interruption argument does not",
   "your card offers \"travel insurance\" → check whether it covers evacuation at "
   "all before treating it as an answer",
 ],
 "note": (
   "{sur} Policy wordings differ, and the reporting documents categories rather than "
   "contracts. No insurer is named in this book and none is recommended. {off} "
   "The nationwide medical emergency number is 1669; the Tourist Police line, "
   "1155, is English-speaking and is often the more practical first call when the "
   "language barrier is itself the obstacle."
 ),
},

# ─────────────────────────────────────────────────────────────── 06 · CITY ──
{
 "n": "06", "cat": "City",
 "nav": "06 · Bangkok, by line",
 "q": "Bangkok: where do you sleep, and how do you cross it?",
 "src": ["where-to-stay-in-bangkok", "getting-around-bangkok",
         "bangkok-first-timer-guide", "3-days-in-bangkok-itinerary",
         "budget-hotels-hostels-bangkok", "tuktuks-taxis-thailand"],

 "scope": "You are spending nights in Bangkok rather than transiting through it.",

 "open_call": (
   "<strong>Choose the station first and the neighbourhood second.</strong> "
   "\"Staying near a BTS or MRT station is the best transport decision you can "
   "make in Bangkok.\" An otherwise lovely hotel a sweaty twenty-minute walk "
   "from one \"will quietly cost you hours over a few days.\""
 ),
 "open_exception": (
   "The exception is the Old Town, and it is a real one. The Grand Palace, Wat "
   "Pho and Wat Arun are precisely the sights the trains do not directly serve. "
   "They are served by the river instead, which is also a line, also cheap, and "
   "also immune to the traffic."
 ),

 "lede": (
   "Bangkok is this book's spine inverted. It is the place where every system "
   "works, which is exactly why arriving here tells you nothing about the rest of "
   "the trip, and why here, uniquely, the decision is measured in minutes rather "
   "than in exposure."
 ),
 "body": [
   ("That makes one instrument sufficient for the whole comparison: which line "
    "the district sits on, and how far you walk to reach it. The BTS Skytrain and "
    "the MRT metro are \"clean, fast, cheap, air-conditioned,\" and, crucially, "
    "they fly over or under the traffic.\" {sur} Every district below is compared on "
    "that and nothing else, because everything else about them is preference."),
   ("The river counts as a line. The Chao Phraya Express and the cross-river "
    "ferries are \"the smart way to reach the historic temple area, which the "
    "trains don't directly serve,\" connecting from the BTS at Saphan Taksin. "
    "Orange-flag commuter boats are the cheapest and most frequent; the blue-flag "
    "tourist boat costs more and stops at the main riverside sights. {off}"),
   ("One more line runs where the trains do not, and it is worth naming as a "
    "line rather than as a boat trip. The canal boats on Khlong Saen Saep are "
    "\"a fast, local way to cut across the city center, if a bit chaotic,\" and "
    "motorbike taxis, the riders in coloured vests, exist for exactly the short "
    "hop that a jam makes impossible. {off} Neither is a sightseeing choice; both "
    "are the answer to a specific ten minutes."),
   ("The buses are the honest omission: very cheap, and \"slow, hot, and hard "
    "to navigate without local knowledge.\" Most visitors skip them. {sur} One "
    "caution on the stored-value cards, because it is the commonest wrong "
    "assumption about this city: <strong>there is no single card for both "
    "networks.</strong> The BTS takes one and the MRT another, so a day using "
    "both means carrying two or buying singles at the gate. {off}"),
   ("The road is the failure mode, and it is predictable. The city gridlocks "
    "roughly 7–9am and 4–7pm, and \"if you must cross town by road at peak time, "
    "allow far more time than the distance suggests.\" Tuk-tuks are not cheaper "
    "than a metered taxi or a Grab, they require hard negotiation, and some "
    "drivers run detours to a showroom that pays them a commission. A novelty "
    "rather than transport. {sur}"),
 ],

 "plate": {"slot": "A07", "after": 0, "caption":
   "The viaduct is the argument for the district: it goes over the traffic rather "
   "than through it. Choose the station first and the neighbourhood second."},
 "table_title": "Four districts, measured on one instrument: access to a line",
 "cols": ["District", "On which line", "What it is for", "What it costs you"],
 "colw": ["label", "mid", "", ""],
 "rows": [
   ("Sukhumvit · Asok, Thonglor",
    "BTS — and at Asok the BTS and MRT cross",
    "the first-timer's path of least resistance; the largest concentration of hotels, at every price",
    "\"a little old Thailand atmosphere\" traded for genuine convenience"),
   ("Silom / Sathorn",
    "BTS and MRT both",
    "business by day, dining and rooftops by night; the gateway to Patpong's night markets",
    "nothing in transit terms — and less tourist density than central Sukhumvit"),
   ("Riverside / Old Town · Rattanakosin",
    "the river, not the trains",
    "the Grand Palace, Wat Pho and Wat Arun, a walk or a ferry away",
    "a slower commute to everything modern"),
   ("Khao San / Banglamphu",
    "neither — taxi, Grab, or a river boat",
    "cheap beds, energy, and the historic core nearby",
    "no metro access at all"),
 ],
 "decisive_row": 2,

 "call": (
   "<strong>If you want the lowest-friction first choice, book near Asok and stop "
   "deciding.</strong> If temples and the river matter more than malls and "
   "nightlife, take the Old Town and accept the commute deliberately. It is a "
   "real cost, paid for a real thing, which is the only kind of trade this book "
   "endorses."
 ),
 "for": [
   "first trip, no strong preference → Sukhumvit at Asok",
   "you came for the temples and the river → Riverside or the Old Town",
   "you are counting baht → Khao San, with the Grab fares back across town "
   "budgeted rather than discovered",
 ],
 "against": [
   "you land late and exhausted → whatever the district, a pre-booked car or a "
   "Grab is worth the few extra dollars to skip the taxi queue",
   "your days start at 8am or end at 5pm on the far side of town → the line "
   "matters more than the room does",
 ],
 "note": (
   "{vol} November to February is the cool, dry peak: book those months well "
   "ahead and expect higher rates. {off} Train and boat fares are low across "
   "the board. The airport side of this is Decision 04."
 ),
},

# ──────────────────────────────────────────────────────────── 07 · CULTURE ──
{
 "n": "07", "cat": "Culture",
 "nav": "07 · The door and the elephant",
 "q": "The temple door, and the elephant question",
 "src": ["what-to-wear-thai-temples", "thai-etiquette-for-americans",
         "elephant-tourism-ethics-thailand", "ethical-elephant-sanctuary-thailand",
         "best-temples-in-thailand", "what-to-pack-for-thailand"],

 "scope": "You will enter a temple, and you are considering an animal attraction.",

 "open_call": (
   "<strong>Carry a scarf or a sarong, and use riding as the first filter on an "
   "elephant venue.</strong> One instantly covers shoulders or wraps as a skirt; "
   "the other ends the search early: if a venue offers rides, stop there. Passing "
   "that test is necessary, not sufficient — the table names what else to read."
 ),
 "open_exception": (
   "On the dress code there is no exception, which is the point. Shoulders and "
   "knees covered applies to men and women alike, it is actively checked at the "
   "entrance of the major sites, and visitors who do not meet it are turned away."
 ),

 "lede": (
   "Two culture questions on a Thailand trip have an actual answer rather than a "
   "range of opinions. Both are decided before you arrive at the door, and both "
   "are cheap to get right."
 ),
 "body": [
   ("The temple rule is simple and enforced: cover the shoulders and cover the "
    "knees. \"At the most visited sites, staff actively check visitors at the "
    "entrance and will turn away anyone who doesn't meet the code.\" {off} Shoes "
    "come off before entering temple buildings, not just the grounds, along "
    "with hats and sunglasses; socks are usually fine. The shoes-off custom "
    "extends to guesthouses, homes, some shops and certain restaurants: \"if you "
    "see a pile of shoes at the entrance, that's your cue to add yours to it.\""),
   ("Two additions for women. Clothing should not be see-through or very tight, "
    "and, the one that catches visitors out, a woman should never touch a monk "
    "or hand anything directly to one. Place the item down for him to pick up, or "
    "pass it via a man. {off} Major sites including the Grand Palace often lend "
    "or rent cover-ups, but not everywhere does, and it can mean a queue or a "
    "deposit."),
   ("The elephant question is a decision rather than a sentiment, because the "
    "reporting supplies a single test that anyone can apply. \"Whether a place "
    "offers elephant rides is the single most reliable test of its ethics… A venue "
    "that has chosen not to offer rides has usually rethought its entire "
    "relationship with the animals; one that still does, whatever it calls itself, "
    "has not.\" {sur} Use it before looking at anything else."),
   ("The complication is real and worth stating rather than smoothing away. "
    "Logging was largely banned in 1989, leaving thousands of captive elephants "
    "and their mahouts without work, and tourism became the alternative "
    "livelihood. Captive elephants cannot simply be released. There is not "
    "enough protected habitat, and many have known only human care. \"The goal is "
    "supporting genuinely welfare-focused operations, not demanding an impossible "
    "purity.\""),
 ],

 "plate": {"slot": "A08", "after": 0, "caption":
   "At the busiest sites this door is staffed, and visitors with bare shoulders or "
   "knees are turned away. A scarf in the day bag settles it before you arrive."},
 "table_title": "Reading a venue on what it does, not on what it calls itself",
 "cols": ["What is advertised", "What it requires of the animal", "Read it as"],
 "rows": [
   ("Riding, with or without a seat",
    "a training process built on coercion and restraint; heavy seats can damage the spine over time",
    "disqualifying — no further research needed"),
   ("Painting, instruments, circus tricks",
    "the same coercive training, in unnatural and stressful conditions",
    "disqualifying"),
   ("Chains, small enclosures, bullhooks",
    "control through fear and pain",
    "disqualifying"),
   ("Roaming in herds, observation, sometimes feeding or bathing",
    "nothing that requires breaking it; the best are moving toward hands-off",
    "the model worth funding"),
   ("The word “sanctuary”",
    "nothing whatsoever",
    "\"the word alone guarantees nothing\" — check whether it still advertises riding"),
 ],
 "decisive_row": 4,

 "call": (
   "<strong>Apply the riding test first. If a venue passes it, read the table "
   "above for the rest.</strong> "
   "It is a filter you can run yourself on any operator, in about thirty seconds, "
   "without trusting a review or a certification, which is exactly why this book "
   "carries it instead of a list of venues that will be out of date before you go."
 ),
 "for": [
   "temples are on the itinerary → the scarf lives in the day bag, not the suitcase",
   "you want to see elephants → the Chiang Mai area is the best-known hub; a "
   "visit is typically a full day including transport, and the good ones cap "
   "numbers, so book ahead",
   "you are packing for heat and the dress code at once → loose long trousers or "
   "maxi skirts in cotton or linen solve both",
 ],
 "against": [
   "a venue's own page emphasises how much you will touch or ride the elephants "
   "rather than how they are cared for → that is the answer",
   "you are heading for a rooftop bar or an upscale venue → smart casual is "
   "enforced there too: no shorts, vests or flip-flops",
 ],
 "note": (
   "{sur} No venue is named in this book. The reporting's test is a filter you apply "
   "yourself, which is the only kind of recommendation that survives the year "
   "between writing and travelling."
 ),
},

# ──────────────────────────────────────────────────────────────── 08 · EAT ──
{
 "n": "08", "cat": "Eat",
 "nav": "08 · Eating well",
 "q": "Ordering well, without a reservation system you can use",
 "src": ["thai-street-food-guide", "thai-food-what-to-order", "how-spicy-is-thai-food",
         "best-markets-bangkok", "thai-cooking-class-guide"],

 "scope": "Every trip.",

 "open_call": (
   "<strong>Eat where the queue is, and order at the heat you can actually "
   "take.</strong> A stall busy with locals means fast turnover, and fast turnover "
   "is simultaneously the quality test and the safety test. The queue is the "
   "first inspection; the rest of this page is the second."
 ),
 "open_exception": (
   "The caveat on heat, stated by the reporting rather than softened: \"even 'a "
   "little spicy' by Thai standards can be hot for many Westerners,\" and some "
   "vendors will make a dish milder for an obvious tourist than for a local. The "
   "phrase is a starting point, not a guarantee."
 ),

 "lede": (
   "Street food in Thailand is not merely the cheap option. \"Vendors often specialize "
   "in a single dish perfected over years or generations, and locals eat from "
   "stalls daily.\" It is frequently the best food in the country, sold from a "
   "cart."
 ),
 "body": [
   ("The ordering mechanics take a minute to learn and work everywhere. Point at "
    "what you want, or at what someone else is eating; hold up fingers for "
    "quantity; carry three words — <em>mai phet</em> (not spicy), <em>phet nit "
    "noi</em> (a little spicy), <em>aroi</em> (delicious, and always "
    "appreciated). Have small notes ready, because stalls do not take cards. {off}"),
   ("The safety habits and the quality habits are the same habits, which is what "
    "makes the rule easy to keep. Choose busy stalls with high turnover; eat what "
    "is cooked fresh and hot in front of you; be cautious with raw items, "
    "pre-cut fruit that has been sitting out, and uncooked shellfish; drink "
    "bottled water, though ice in established places is generally fine. Give the "
    "stomach a day or two to adjust. {sur}"),
   ("Dietary needs are workable with the right word rather than the right "
    "sentence. Fish sauce and shrimp paste are common hidden ingredients, so "
    "<em>jay</em> signals strict vegetarian or vegan — look for the yellow-and-red "
    "symbol — and <em>mang-sa-wirat</em> signals vegetarian. For an allergy, carry "
    "a translation card and accept that cross-contamination at a busy stall "
    "cannot be controlled. {off}"),
   ("And the food changes as the trip moves, which is an argument for eating "
    "regionally rather than searching for the same dish twice. Khao soi and sai "
    "ua in the north; som tum, laab and gai yang in Isan; bolder curries and "
    "seafood in the south; and in Bangkok, Yaowarat in Chinatown."),
 ],

 "plate": {"slot": "A09", "after": 1, "caption":
   "The queue is the inspection. Busy means fast turnover, and fast turnover is "
   "the first inspection you can make from the pavement."},
 "table_title": "Where to eat what, and what each place is reliably good at",
 "cols": ["Where", "Reliably good at", "How you order", "What to watch"],
 "rows": [
   ("A street stall",
    "one dish, done for years — noodles, grilled skewers, one-plate rice",
    "point; fingers for quantity; small notes",
    "turnover. A stall busy with locals is the first quality and safety filter"),
   ("A market",
    "breadth — sweets, fruit and shakes, the region's specialities in one place",
    "the same, plus a willingness to try something you cannot name",
    "pre-cut fruit that has been sitting out"),
   ("A simple local restaurant",
    "a menu, a seat, and the same food",
    "pictures or English on the tourist streets",
    "milder by default for an obvious tourist — say the phrase anyway"),
   ("A street-food tour, early",
    "learning what is what, and stalls you would never find alone",
    "booked ahead",
    "worth it on day one; much less so on day six"),
 ],
 "decisive_row": 0,

 "call": (
   "<strong>Follow the crowd, start at <em>mai phet</em>, and work up.</strong> "
   "Most people's tolerance grows over a trip — what is punishing on day one is "
   "often pleasant by the end of a fortnight. And if a dish catches you out, "
   "reach for rice rather than water: water spreads the chili oil around."
 ),
 "for": [
   "travelling with children, or a low tolerance → rice, fried rice, pad thai, "
   "satay, spring rolls, grilled meats, omelettes and fruit are all naturally mild",
   "you want the heat → say <em>phet nit noi</em> and climb from there",
   "you want to learn the map fast → a guided street-food tour in the first days, "
   "not the last",
 ],
 "against": [
   "an allergy → a translation card, and the honest acceptance that a busy stall "
   "cannot control cross-contamination",
   "strict vegetarian → <em>jay</em>, not \"no meat\". Fish sauce and shrimp "
   "paste are the hidden ingredients",
 ],
 "note": (
   "{sur} No restaurant and no stall is named in this book. A named stall is the "
   "fastest thing in any guide to go out of date, and the reporting's own test — "
   "follow the crowd — outlives every one of them."
 ),
},
]


# ─── the essays ─────────────────────────────────────────────────────────────
# Material the reporting supports strongly but which is NOT a decision: it is not
# hard to reverse, or it is not a choice at all. Stage A2 refused each of these
# as a decision and promised them here rather than dropping them, because the
# reporting is real and the previous book padded a decision out of one of them.

ESSAYS_FRONT = [
{
 "id": "e1", "nav": "Before the eight · the calendar",
 "position": "Essay",
 "eyebrow": "Before the eight · the calendar",
 "q": "There is no best time. There are three, and they disagree.",
 "scope": "Thailand's two coasts have opposite wet seasons, and the north keeps a "
          "third season of its own that no beach calendar mentions.",
 "src": ["best-time-to-visit-thailand", "thailand-weather-by-season",
         "island-hopping-thailand", "chiang-mai-first-timer-guide",
         "7-days-northern-thailand", "when-ferries-cancel-thailand"],
 "fig": "calendar",
 "lede": (
   "Every account of Thailand opens with a best time to go. There are three of "
   "them, they are each correct, and they govern different parts of the same "
   "country — which is why a trip can be planned entirely sensibly and still "
   "land in the wrong month."
 ),
 "body": [
   ("The national answer is three seasons. Cool and dry from roughly November to "
    "February — the peak, and the most reliable weather, which is also why it is "
    "the busiest and the priciest. Hot from March to May, genuinely punishing "
    "inland, with Songkran in mid-April. Rainy from June to October. {off}"),
   ("That last one is worth not flinching from. The rain \"typically comes in "
    "intense bursts, often in the afternoon, leaving plenty of dry hours around "
    "them — so a rainy-season trip is far from a washout,\" and the reporting notes "
    "that seasoned travellers actively prefer it for the value and the quiet."),
   ("The coastal answer overrides the national one, because the two coasts run "
    "opposite calendars. The Andaman side — Phuket, Krabi, Phi Phi, Koh Lanta — "
    "is best roughly November to April, with peak monsoon around September and "
    "October. The Gulf side — Samui, Phangan, Koh Tao — is often best mid-year, "
    "with its wettest stretch around October to December. {off} So there is "
    "almost always a coast with good beach weather; the trick is being on it."),
   ("The northern answer contradicts both, and it is the one Americans are least "
    "often told. The north is at its best November to February — and then, "
    "\"roughly February to April, agricultural fires cause poor air quality "
    "across the north.\" {sur} Nine separate articles in the reporting behind "
    "this book say so independently, which is as close to unanimous as this "
    "reporting gets about anything."),
   ("Put the three calendars on one axis and a popular window turns awkward. A "
    "November or December trip that wants Chiang Mai and the Gulf islands has "
    "chosen the north's best month and the Gulf's wettest stretch at the same "
    "time. Neither half is a mistake on its own. This is the shape of trap the "
    "whole book keeps finding, and the reporting states it best about ferries: "
    "\"The travelers who get caught are rarely the ones who picked the wrong "
    "ferry. They are the ones whose island, month and departure arrangements "
    "were each individually reasonable.\""),
 ],
 "plate": {"slot": "A01", "after": 1, "caption":
   "Mid-afternoon in the wet season. The rain arrives like this, in bursts, and "
   "the dry hours sit on either side of it. The street does not stop."},
 "note": (
   "{vol} December and January coincide with the Western winter holidays: "
   "availability tightens and prices climb the closer you book. {off} Songkran "
   "falls in mid-April. Nothing in this figure is a forecast — it is what the "
   "reporting says about a normal year."
 ),
},
]

ESSAYS_BACK = [
{
 "id": "e2", "nav": "Money · the arithmetic of cash",
 "position": "Essay",
 "eyebrow": "Money · the arithmetic of cash",
 "q": "The fee that does not shrink",
 "scope": "Thai ATMs generally charge foreign cards a flat local withdrawal fee — flat, not "
          "a percentage — so it is the number of withdrawals that costs you, "
          "never the amount.",
 "src": ["atm-fees-thailand-real-cost", "money-in-thailand-guide",
         "thailand-on-a-budget", "thailand-trip-cost"],
 "lede": (
   "For years the answer was one number: 220 baht, at every Thai bank, on every "
   "foreign card. \"That figure is still quoted in most guides, and it is no "
   "longer reliably what you will see on the screen.\""
 ),
 "body": [
   ("Two things about that fee are structural and will outlast any number. It "
    "is <strong>flat</strong>, so it is the count of withdrawals that costs you "
    "and never the amount. And it is now set <strong>by card network</strong>, "
    "so the same machine charges differently depending on which card goes in — "
    "with the supermarket-chain ATMs cheaper than the banks. The current "
    "schedule is on the Field Sheet, because it is precisely the kind of "
    "figure that will be wrong before this book is. {vol}"),
   ("The consequence is easy to miss. If you are carrying both a Visa and a "
    "Mastercard, <strong>which one you reach for changes the cost of every "
    "withdrawal for the whole trip</strong>, and nothing about the machine tells "
    "you in advance. The fee is displayed on screen before you confirm, so the "
    "habit worth building is simply reading that screen instead of clicking "
    "through it."),
   ("Because the largest charge is flat, taking out 2,000 baht and taking out "
    "20,000 baht incur exactly the same fee. It is the cadence that costs, and "
    "the spread across a realistic trip is wider than almost anyone assumes."),
   ("Three other charges sit underneath. Your home bank's foreign transaction "
    "fee, typically nothing to 3%, which scales with the amount and so pushes "
    "gently the other way. The network's exchange margin, built into the rate "
    "rather than itemised, which is why even careful people miss it. And dynamic "
    "currency conversion — the avoidable one. {off}"),
   ("At some point the machine offers to charge you in dollars rather than baht. "
    "Accepting hands the conversion to the ATM operator \"at a rate typically "
    "3–7% worse than the interbank rate your card network would have used. On a "
    "large withdrawal that single tap costs more than the flat fee did.\" "
    "<strong>The rule has no exceptions: always choose baht.</strong> The screen "
    "is designed to make accepting look like the safe, familiar option."),
   ("There is a ceiling and there is a counterweight. A single withdrawal is "
    "capped, and the cap differs by bank, so there is a floor under how few "
    "withdrawals a trip can involve — the figures are on the Field Sheet. {vol} "
    "And "
    "cash you are carrying is cash that can be lost or stolen, and a hotel safe "
    "is not always available or trustworthy. The arithmetic pushes toward large "
    "infrequent withdrawals; sense pushes back. Land in the middle on purpose "
    "rather than by drifting."),
   ("What sets the cash floor is not the budget but the shape of the spending. "
    "Thailand is still largely cash-based for everyday life: street food, "
    "markets, small vendors, tuk-tuks, songthaews and most rural businesses want "
    "notes. Cards are comfortable at hotels, malls, and chain and upscale "
    "restaurants, and unreliable outside them. The local QR system, PromptPay, "
    "is everywhere among Thais and generally needs a Thai bank account, so it is "
    "not an option for a visitor. {off} A trip weighted toward the first list "
    "needs materially more cash in hand than one weighted toward the second, and "
    "that, rather than the fee, is what should set how often you visit a machine."),
   ("Carrying dollars is the other route and it is worth costing properly. "
    "Exchanging cash at a dedicated booth can beat repeated withdrawals for "
    "larger sums once the flat fee is counted, and airport counters are "
    "consistently worse than city booths. So the airport is the place to change "
    "the minimum you need to get into town, not the trip's cash. {off} Two "
    "small mechanics travel with it: bring crisp, undamaged bills, because torn "
    "or marked notes are sometimes refused, and keep a mix of denominations. "
    "Breaking a 1,000-baht note at a food stall is its own small problem."),
   ("Which is why this sits in a book about routing rather than a book about "
    "budgets. \"Withdrawal cadence is not really a money decision. It is a "
    "routing decision.\" People make twenty small withdrawals \"not because they "
    "miscounted the fee, but because their itinerary never let them plan further "
    "ahead than the next two days.\" Decision 03 is what determines whether "
    "there is a bank ATM within reach at all."),
 ],
 "plate": {"slot": "A10", "after": 6, "caption":
   "Priced by hand, paid in cash. Stalls, markets and songthaews are what set how "
   "often you stand at a machine, not the size of your budget."},
 "table_title": "The same cash, the same bank, the same fortnight · 60,000 baht at the Visa rate",
 "cols": ["Withdrawal pattern", "Withdrawals", "Flat fees paid"],
 "colw": ["label", "narrow", ""],
 "rows": [
   ("3,000 baht as needed", "20", "5,000 baht"),
   ("6,000 baht at a time", "10", "2,500 baht"),
   ("20,000 baht at a time", "3", "750 baht"),
 ],
 "decisive_label": "the drift, priced",
 "decisive_row": 0,
 "note": (
   "{vol} Every figure in the table moves — the network fee most of all. The "
   "structure does not: a flat fee makes frequency the cost. {off} A few US "
   "accounts reimburse foreign ATM fees outright, which removes the calculation "
   "entirely; Charles Schwab's checking account and Fidelity's cash management "
   "account are the two the reporting names."
 ),
},
{
 "id": "e3", "nav": "Entry · the deadline you are given",
 "position": "Essay",
 "eyebrow": "Entry · the deadline you are given",
 "q": "The fine is capped. The ban is not.",
 "scope": "Thailand's overstay rules price the act rather than the wallet, and "
          "the date that governs is the one an officer writes on your stamp.",
 "src": ["thailand-entry-refusal-and-overstay", "thailand-entry-requirements-americans",
         "do-americans-need-visa-thailand", "thailand-digital-arrival-card-tdac",
         "thailand-visa-extension-process"],
 "lede": (
   "This is not a decision and it is not presented as one. It is a set of "
   "deadlines handed to you at a desk, and the only choice inside it, how close "
   "to the stamped date to plan, has a one-word answer."
 ),
 "body": [
   ("The fine is 500 baht per day, capped at 20,000. The cap is reached at 40 "
    "days and the fine stops accumulating there. It is paid at the immigration "
    "counter on departure; officers calculate the days, collect, issue a receipt "
    "and then stamp you out. {off}"),
   ("One mercy is rarely mentioned. For an overstay of a few hours caused by a "
    "flight delay or a schedule change, the fine is usually waived if you "
    "explain the situation at departure. The Royal Thai Embassy states this "
    "directly. \"A missed connection that pushes you past midnight is not the "
    "scenario the penalty structure is aimed at.\" Read that next to Decision 04, "
    "which is about exactly which missed connections are yours to own."),
   ("The ban is the part that scales, and the table opposite is the whole shape "
    "of it: the money flat-lines at 40 days while the consequence keeps climbing "
    "for years. Being caught rather than presenting yourself carries "
    "substantially harsher consequences: detention at an immigration facility "
    "before deportation, and a longer ban, while <strong>the cash fine is "
    "identical either way</strong>. {off}"),
   ("As this edition goes to press the number itself has just moved, which is "
    "the best possible illustration of why it is not a decision. The 60-day "
    "exemption introduced in 2024 was rolled back on <strong>15 September "
    "2026</strong>: most nationalities including Americans now receive "
    "<strong>30 days</strong> on arrival, extendable once by up to 30 more at a "
    "Thai immigration office inside the country, for roughly 60 days maximum per "
    "entry. {vol} A second new clause limits visa-exempt entries by <em>land "
    "border</em> to two per calendar year; arrivals by air and sea are not "
    "limited, so it does not touch a normal fly-in holiday."),
   ("What that change did <em>not</em> touch is everything else on this page. "
    "The fine, the cap, the ban ladder, the arrival card, the onward-ticket "
    "requirement and the funds rule all stand exactly as written. {sur} That is "
    "the shape of this whole category: one volatile number wrapped in a "
    "structure that does not move, which is why the number belongs on the Field "
    "Sheet and the structure belongs in the book."),
   ("And the date that governs is still the \"admitted until\" date on the entry stamp. "
    "Not the exemption length in the abstract, not what an airline or a booking "
    "site said, not a calculation from the arrival date. Officers write it by "
    "hand or stamp it, and it is worth reading before you leave the desk."),
   ("Two requirements are enforced in places travellers do not expect. Proof of "
    "onward or return travel is usually enforced by the airline at check-in "
    "rather than by Thai immigration on arrival — \"the requirement is most "
    "likely to bite thousands of miles before Thailand,\" at your own departure "
    "airport, with no Thai official involved. And a funds requirement exists in "
    "the regulations, commonly cited as 20,000 baht per person or 40,000 per "
    "family, that is not routinely checked: the honest description is \"a rule "
    "that exists and is enforced inconsistently.\" {off}"),
   ("Finally, the arrival card. The Thailand Digital Arrival Card replaced the "
    "paper TM6 in May 2025. It is mandatory for foreign nationals, free, and "
    "filed online before arrival at the official immigration site. The filing "
    "window has changed since introduction, so the current timing is worth "
    "taking from the official site rather than from any guide, including this "
    "one. {vol}"),
 ],
 "table_title": "Where the money stops and the consequence keeps going · voluntary departure",
 "cols": ["Length of overstay", "The fine", "The re-entry ban"],
 "colw": ["label", "mid", ""],
 "rows": [
   ("1–40 days", "500 baht a day, to a 20,000 cap", "none"),
   ("41–90 days", "20,000 baht — the cap is already reached", "none"),
   ("More than 90 days", "20,000 baht", "up to 1 year"),
   ("More than 1 year", "20,000 baht", "up to 3 years"),
   ("More than 3 years", "20,000 baht", "up to 5 years"),
   ("More than 5 years", "20,000 baht", "up to 10 years"),
 ],
 "decisive_label": "the ban begins here",
 "decisive_row": 2,
 "note": (
   "{vol} Thai policy here has tightened repeatedly, and back-to-back "
   "visa-exempt entries attract additional scrutiny — admission on an exemption "
   "is at the officer's discretion rather than automatic. Every figure on this "
   "page is one to confirm against the official source before you fly; the Field "
   "Sheet says where."
 ),
},
{
 "id": "e4", "nav": "Refused · the north",
 "position": "Essay",
 "eyebrow": "Refused · the north",
 "q": "The north is a different trip, and this book hands it back",
 "scope": "Around 5,000 words of the reporting behind this book are about Chiang "
          "Mai and the mountains. None of it produced a decision, and the honest "
          "thing is to say why rather than to manufacture one.",
 "src": ["chiang-mai-first-timer-guide", "7-days-northern-thailand",
         "chiang-mai-vs-chiang-rai", "pai-thailand-guide",
         "best-things-to-do-chiang-mai", "where-to-stay-in-chiang-mai"],
 "lede": (
   "A decision, in this book, is a choice that is hard to reverse once you are "
   "there and that fails together with other choices. The north is neither, and "
   "padding it into a ninth chapter is precisely what the previous edition did "
   "with entry requirements."
 ),
 "body": [
   ("What the reporting does support is a clear and unglamorous shape. Three to "
    "four days for a first visit: the Old City temples, the mountain temple Doi "
    "Suthep, a cooking class, and a full day at an observation-only elephant "
    "sanctuary. An hour and a quarter from Bangkok by air, or the sleeper "
    "overnight. Songthaews run fixed routes for a small flat fare, Grab works, "
    "and the old city is walkable. {off}"),
   ("None of that is hard to reverse. You can decide the whole of it from a seat "
    "on the plane, and nothing else in the trip breaks if you change your mind. "
    "Its one genuine constraint is seasonal, and it is not in this chapter. The "
    "burning season belongs to the calendar, and the calendar is at the front of "
    "the book where it can govern the decisions that follow it."),
   ("One caution the reporting does supply belongs with Decision 01 rather than "
    "here. The mountain roads out to Chiang Rai and Pai are long and winding, "
    "and most travellers book an organised tour or a private driver rather than "
    "self-driving. The Pai road \"has over 700 curves and can induce motion "
    "sickness.\" {off}"),
   ("And if the north <em>is</em> the trip rather than an addition to it, the "
    "reporting supplies its own seven-day shape: two days in Bangkok, three in "
    "Chiang Mai, one for a side trip (Chiang Rai at about three hours each way, "
    "Pai, or Doi Inthanon) and a flight back to Bangkok for the departure. That "
    "is a coherent week and it is a different book from this one."),
 ],
 "note": (
   "{sur} Cool season aside, every northern source in the reporting agrees on the "
   "same three-to-four-day shape, which is why there was nothing left to decide."
 ),
},
]


# ─── back matter ────────────────────────────────────────────────────────────
REFUSALS = {
 "id": "ref", "nav": "What this book refused", "position": "Back matter",
 "eyebrow": "Back matter · the refusals",
 "q": "What this book refused, and why",
 "scope": "Ninety-seven articles and 83,533 words of reporting stand behind "
          "these pages. A good deal of it did not become one, and a book that "
          "cannot say what it left out is asking to be trusted on faith.",
 "lede": (
   "Every refusal below was decided before a word of the chapter was written, "
   "which is the only point at which such a decision is honest. Afterwards it "
   "becomes a justification."
 ),
 "body": [
   ("The pattern is consistent. Material was refused when it was <em>not a "
    "choice</em>: a deadline handed to you, a season you cannot move. Or when "
    "the reporting behind it would not carry the weight a chapter puts on it. "
    "Nothing was refused for being inconvenient to the argument."),
   ("Three of these refusals became essays rather than disappearing, because the "
    "reporting is good and the reader still needs it. The difference is that an "
    "essay does not pretend to a verdict. Two of them, prices and anything "
    "with a filing window, went to the Field Sheet on the next page, which is "
    "where a fact with a shelf-life belongs."),
 ],
 "table_title": "Refused, and the reason on the record",
 "cols": ["What was refused", "Words behind it", "Why"],
 "colw": ["label", "narrow", ""],
 "rows": [
   ("Entry requirements as a decision", "4,164",
    "Below the depth floor, and the rules have a shelf-life. The previous "
    "edition shipped this as a decision and padded it. Here it is an essay, and "
    "its volatile half is on the Field Sheet. Vindicated four days before this "
    "edition went to press, when the exemption was cut from 60 days to 30."),
   ("A ranked list of islands", "—",
    "The reporting describes these places; it does not score them. A ranking would "
    "have been invented and then defended."),
   ("The north as a decision", "5,016",
    "A chapter, not a decision: nothing in it is hard to reverse and nothing "
    "fails together with anything else. Handed back as an essay."),
   ("Current prices", "3,928",
    "Thin, and volatile by definition. Field Sheet."),
   ("A season calendar as a decision", "1,644",
    "Say what the seasons do and stop. It is FIG. 5 and the essay in front of "
    "the eight, where it can govern them."),
   ("A price column on Decision 01", "—",
    "Fares are reported ranges that differ by island. A ledger that certifies a "
    "comparison nobody made is a failure these manuals have shipped before."),
   ("Hotels, restaurants, stalls, venues, insurers", "—",
    "Named nowhere, in any of these manuals. A name is the fastest thing "
    "in a guide to go out of date."),
   ("A bibliography", "—",
    "The reporting behind this book is this site's own, and it is all online. "
    "A printed list of 97 URLs would age worse than the book; the ledger at "
    "thailandforamericans.com/sources is maintained instead."),
 ],
 "note": (
   "{sur} Two gaps belong to the reporting itself and this book repeats them "
   "rather than filling them: the island shared-truck timetables, and the last "
   "departures from the southern airports. Both would have been easy to invent. "
   "{off} Every article behind this book is listed at "
   "<strong>thailandforamericans.com/sources</strong>, with the date each was "
   "last checked — so any quotation or reported figure here can be read back to "
   "the page it came from. Claims that rest on anything else name their source "
   "in the line itself."
 ),
}

FIELD_SHEET = {
 "id": "fs", "nav": "The Field Sheet", "position": "Back matter",
 "eyebrow": "Back matter · cut this out",
 "q": "The Field Sheet",
 "scope": "Everything in this book that moves, on two cards that fit a passport "
          "wallet. Cut along the rule. Nothing on these cards is an argument.",
 "cards": [
   {"title": "Confirm before you fly",
    "sub": "Each of these was true when this went to press and each can change.",
    "items": [
      ("The arrival card", "TDAC is mandatory and free. The <em>filing window</em> "
       "has changed before — take it from the official immigration site, not a guide."),
      ("Your admitted-until date", "<strong>30 days</strong> on arrival since "
       "15 Sep 2026, extendable once by 30 at an immigration office (~1,900฿). "
       "But read the stamp: the date written there governs, not the rule you "
       "read before you flew."),
      ("Last departures, southern airports", "Not reliably published. Check the "
       "timetable for your date before planning a same-day connection."),
      ("The ATM fee, by network", "Visa ≈250฿ · Mastercard up to 350฿ · some banks "
       "still 220฿ · AEON (in Big C and Lotus's) ≈150฿. Single-withdrawal cap "
       "≈20,000–30,000฿ by bank. Read the screen before you confirm. "
       "<strong>Always choose baht.</strong>"),
      ("Your policy, two questions", "Do you direct-bill in Thailand? Does this "
       "include repatriation as well as evacuation?"),
      ("Your licence", "A motorbike needs a motorcycle endorsement. The IDP "
       "translates it; it cannot add it."),
      ("The season for your coast", "Andaman wettest Sep–Oct · Gulf wettest "
       "Oct–Dec · the north's burning season Feb–Apr."),
    ]},
   {"title": "If something goes wrong",
    "sub": "In this order. The first call is the one that changes the outcome.",
    "items": [
      ("Your insurer's assistance line", "<span class='fill'>&nbsp;</span><br>"
       "Write it here. <strong>Emergency → get care first.</strong> Otherwise "
       "call before the billing is arranged, while a guarantee of payment may "
       "still be possible."),
      ("1669", "Nationwide medical emergency."),
      ("1155", "Tourist Police. English-speaking, and often the more practical "
       "first call when the language is the obstacle."),
      ("A boat is cancelled", "Take the earlier crossing next time; prefer the "
       "larger ferry in marginal weather. A separately booked flight is not "
       "protected — that ticket is forfeit."),
      ("You are past your stamped date", "Present yourself at the counter rather "
       "than being found. <strong>On voluntary departure</strong>, under 90 days "
       "is a fine and no ban; being caught is harsher. A few hours caused "
       "by a delayed flight is usually waived if you explain it."),
      ("The ATM offers you dollars", "Decline. Always choose baht."),
    ]},
 ],
 "note": (
   "{vol} Every value on the left-hand card moves. The right-hand card does not "
   "— it is a sequence, not a set of figures. {off} Emergency numbers are as "
   "published by the Thai authorities."
 ),
}


# The vein the first pass left in the ground. `is-thailand-safe-for-tourists` and
# `common-scams-thailand` say the same thing from two directions: the risk people
# prepare for is not the risk the reporting records. It points straight back at
# Decision 01, which is why it belongs in front of the closing essays.
ESSAY_RISK = {
 "id": "e5", "nav": "Risk · what actually goes wrong",
 "position": "Essay",
 "eyebrow": "Risk · what actually goes wrong",
 "q": "The risk is not the one you packed for",
 "scope": "Visitors arrive braced for crime and unbraced for traffic. The "
          "reporting puts it the other way round, and it is not close.",
 "src": ["is-thailand-safe-for-tourists", "common-scams-thailand",
         "thailand-road-conditions-by-region", "scuba-diving-snorkeling-thailand",
         "thailand-travel-health-guide"],
 "lede": (
   "Visitors arrive braced for crime and unbraced for traffic. On the numbers "
   "that exist, it is the other way round, and it is not close — which makes "
   "this the one page in the book that argues with what the reader already "
   "believes."
 ),
 "body": [
   ("Start with what is rare. Violent crime against tourists is relatively "
    "uncommon, most of the country sits at the lowest US advisory level, and the "
    "scams, of which there are many and which are well catalogued, are "
    "explicitly \"about separating you from your money through deception,\" not "
    "about force. {off} They are predictable enough to be listed, which is the "
    "opposite of dangerous."),
   ("Now the part that is not rare, and here the figures come from outside this "
    "desk. <strong>Traffic crashes are the most common cause of non-natural "
    "death for American travellers abroad</strong>, on the US State "
    "Department's own count — ahead of homicide, terrorism and natural "
    "disaster. Among destinations, Thailand sits at the top for fatal road "
    "crashes per visit, and the State Department's Thailand page names the "
    "vehicle: multiple US citizens die each year in crashes involving two- and "
    "three-wheeled vehicles. Roughly three-quarters of Thai road deaths are "
    "motorbike riders and passengers."),
   ("So it is not a risk among risks, and it is produced by the single most "
    "casually-made decision on the whole trip: renting a scooter at a counter, "
    "with no licence check, on an island with no streetlights."),
   ("Read that beside Decision 01 and Decision 05 and the three facts close into "
    "one. The reporting's own summary of the road risk names the remedy in the same "
    "breath as the licence: \"wear a helmet, have a motorcycle license (also an "
    "insurance requirement), and go slowly,\" or simply avoid scooters. Three "
    "separate industries, licensing, insurance and whoever paints the road, "
    "arrive at the same sentence."),
   ("The scams deserve their catalogue, but they fall to habits rather than "
    "vigilance. Assume the Grand Palace is open and walk to the official "
    "entrance. \"Temple closed today\" is the oldest one there is, and it ends "
    "at a jewellery shop. Insist on the meter or use Grab. <strong>Photograph a rented scooter "
    "or jet-ski before you take it</strong>, and never leave a passport as a "
    "deposit. Use only the official site for the arrival card; paid look-alikes "
    "exist for a document that is free. {off}"),
   ("Two more that are neither crime nor traffic, and both are avoidable by "
    "knowing them. Bootleg spirits cut with methanol occasionally cause serious "
    "harm. Sealed, reputable brands only. And riptides affect some beaches, "
    "where the flags and the local answer are the whole of the advice. {sur}"),
 ],
 "table_title": "What visitors prepare for, against what the reporting records",
 "cols": ["The worry", "What the reporting actually says"],
 "colw": ["mid", ""],
 "rows": [
   ("Violent crime",
    "Relatively rare against tourists. Most of the country sits at the lowest US advisory level. {off}"),
   ("Scams",
    "Common, catalogued and non-violent: \"about separating you from your money through deception.\" Beaten by habits, not by vigilance."),
   ("Road traffic",
    "<strong>The most common cause of non-natural death for American travellers abroad</strong>, and Thailand leads on fatal crashes per visit. Motorbikes are about three-quarters of Thai road deaths. This is Decision 01 — the decision people spend the least time on."),
   ("The deep south",
    "Yala, Pattani, Narathiwat and parts of Songkhla carry higher warnings and sit well off the standard route. Bangkok, Chiang Mai and the popular islands are not affected. {off}"),
   ("Bootleg alcohol",
    "Methanol-tainted spirits occasionally cause serious harm. Sealed, reputable brands only."),
   ("Riptides",
    "Real on some beaches. Heed the flags and ask locally. The reporting offers no list, and neither does this book."),
 ],
 "decisive_row": 2,
 "decisive_label": "the one that is measured",
 "note": (
   "{off} Tourist Police, English-speaking: 1155. General emergencies: 191. "
   "Medical: 1669. {vol} The road-risk figures on this page are the State "
   "Department's and are dated; advisories and counts change, and its current "
   "Thailand page is the source, not this one. One diving note that belongs "
   "here rather than in a chapter: policies commonly exclude diving or require a "
   "rider, and there is a recommended window between a last dive and a flight, "
   "which is an itinerary constraint, not a diving one."
 ),
}

# Part dividers. The book has a real three-part shape and, until now, no contents
# of any kind — a 40-page manual with no way in. Each divider carries what its
# part holds, so it does a job rather than filling a sheet.
PARTS = [
 {"id": "p1", "nav": "Part one · the eight decisions", "position": "Part one",
  "eyebrow": "Part one",
  "title": "The eight decisions",
  "blurb": "Each is a choice that is hard to reverse once you are there, and that "
           "fails together with the others. They are in the order they get made.",
  "items": [
    ("01 · Ride", "What may you actually drive, and what are you insured on?"),
    ("02 · Sequence", "How many islands actually fit, and in what order?"),
    ("03 · Base", "Which island — and which side of the line?"),
    ("04 · Transit", "How do the legs connect, and who owns the failure?"),
    ("05 · Insure", "What are you exposed to, and what does a policy answer?"),
    ("06 · City", "Bangkok: where do you sleep, and how do you cross it?"),
    ("07 · Culture", "The temple door, and the elephant question"),
    ("08 · Eat", "Ordering well, without a reservation system you can use"),
  ]},
 {"id": "p2", "nav": "Part two · after the eight", "position": "Part two",
  "eyebrow": "Part two",
  "title": "After the eight",
  "blurb": "Material the reporting supports strongly, but which is not a decision — "
           "because it is not a choice, or because it is trivially reversible. "
           "None of it carries a verdict.",
  "items": [
    ("Risk", "What actually goes wrong, and what does not"),
    ("Money", "The fee that does not shrink"),
    ("Entry", "The fine is capped. The ban is not."),
    ("The north", "A different trip, handed back"),
    ("Refused", "What this book left out, and the reason on the record"),
    ("The Field Sheet", "Everything that moves, on two cards to cut out"),
  ]},
]


# The cover device: the same seven places and the same four measurements as
# FIG. 3, with no axis labels — cover.md permits one device and nothing below
# 24px, and a legend would need 11px type. The cover shows a pattern that breaks;
# the interior names what broke. (name, [airstrip, hospital, one leg, Grab],
# rule-after-this-row)
COVER_DEVICE = [
    ("Phuket",        [2, 2, 2, 2], False),
    ("Koh Samui",     [2, 2, 2, 2], False),
    ("Ao Nang",       [1, 1, 1, 2], True),
    ("Koh Lanta",     [0, 0, 0, 0], False),
    ("Koh Phangan",   [0, 0, 0, 0], False),
    ("Koh Tao",       [0, 0, 0, 0], False),
    ("Koh Chang",     [0, 0, 0, 0], False),
]
