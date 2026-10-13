# content.py — the decisions. The analytical heart of "Japan, Worked Out."
# ─────────────────────────────────────────────────────────────────────────────
# Every decision must land in model.md's bottom-right cell: NON-OBVIOUS to a
# diligent amateur AND HIGH-STAKES. Naive models are MINED from the corpus's own
# "most first-timers / the mistake / no longer" sentences, never invented.
#
# The organising fact this book turns on:
#   the trip almost every first-timer actually takes contains only TWO long train
#   journeys, and the national rail pass needs about FOUR to pay for itself.
#
# Marks: ● ESTABLISHED (structural) · ◇ OFFICIAL (published rule/fare)
#        ▲ SURVEYED mm/yy (our dated observation) · ◆ VOLATILE (Field Sheet only)
# Lint: no mark = opinion = cut.
# ─────────────────────────────────────────────────────────────────────────────

EST = "<span class='mk est'>●</span>"
OFF = "<span class='mk off'>◇</span>"
SUR = "<span class='mk sur'>▲</span>"
VOL = "<span class='mk vol'>◆</span>"

DECISIONS = [

# ── 01 ───────────────────────────────────────────────────────────────────────
{
 "n": "01", "cat": "Route",
 "q": "What does a day trip cost you?",
 "cols": "DAYS OUT · DAYS LEFT IN THE CITY",
 "fig": "days-ledger",
 "lede": (
   "Nobody plans a trip to Japan by deciding how many days <em>not</em> to spend in Tokyo. "
   "Yet that is the decision a day trip makes, and it is made by accretion — Hakone because "
   "of the Fuji view, Nara because of the deer, Nikko because it was on a list — until a "
   "five-day trip built around two cities has barely two days left standing in either of them."
 ),
 "table_title": "Where the days go · five-day Tokyo + Kyoto trip",
 "rows": [
   (f"5 days, no day trips {EST}", "4 full days in the two cities"),
   (f"5 days, one day trip {EST}", "3 full days in the two cities"),
   (f"5 days, three day trips {EST}", "barely 2 days in the two cities"),
   (f"10 days, two day trips {EST}", "6–7 full days in the two cities"),
 ],
 "verdict": (
   "<strong>Under a week, take none. At ten days, take two.</strong> A day trip is not an "
   "addition to the trip, it is a substitution: the Shinkansen to Hakone and back is three "
   "hours of daylight before you have looked at anything. The test is not whether the "
   "destination is worth seeing — they all are — but whether you would rather spend that day "
   "somewhere new or spend it getting better at the city you already chose. First-timers "
   "reliably answer that question wrong in the planning and right in hindsight."
 ),
 "reasoning": """<p>The substitution is easiest to see in hours rather than days. A day trip to Hakone or
Nikko is roughly two hours of travel each way once you count the walk to the station, the
transfer and the wait, which removes most of a working day before you have looked at anything.
What remains is an afternoon in a place you do not know, followed by the same journey back in
the dark. {EST}</p>

<p>Against that, the marginal day in a city you have already learned is worth more than it
sounds. By day three in Tokyo you know which exit of which station you want, you have found a
coffee place, and you can navigate an evening without a map. That fluency is precisely what a
day trip spends, and it is the reason returning travellers cut day trips first.</p>""",
 "for": [
   "then take it → ten days or more, and the second city already has its three full days",
   "then take it → the day trip <em>is</em> the thing you came for (Fuji, the deer, Miyajima)",
   "then take it → your base is Kyoto and the trip is Nara, which is forty minutes",
 ],
 "against": [
   "then skip it → five days or fewer, whatever the blogs stack into them",
   "then skip it → it is your first two days and you are still jet-lagged",
   "then skip it → you are moving hotels the next morning anyway",
 ],
 "note": (
   f"{EST} Nara from Kyoto is the one day trip that survives a short trip, "
   "because the round trip is under ninety minutes of travel and it runs on local lines you "
   "are already paying for."
 ),
},

# ── 02 ── THE FREE HOOK ──────────────────────────────────────────────────────
{
 "n": "02", "cat": "Rail",
 "q": "Does the national rail pass pay for itself?",
 "cols": "LONG LEGS · WHAT YOU PAY",
 "fig": "breakeven",
 "hook": True,
 "lede": (
   "For twenty years the Japan Rail Pass was the first thing an American bought and the "
   "advice was sound. In October 2023 the seven-day ordinary pass went from about ¥29,650 to "
   "¥50,000 — a rise of roughly seventy per cent in one step — and a great deal of the "
   "English-language internet has never been revised. The pass did not merely get more "
   "expensive. It stopped being the default answer."
 ),
 "table_title": "The break-even, in legs · seven-day ordinary pass",
 "rows": [
   (f"one long leg — Tokyo → Kyoto, then fly home {OFF}", "about ¥13,850"),
   (f"two long legs — the classic first trip {OFF}", "about ¥27,700"),
   (f"four long legs — what the pass needs {EST}", "about ¥55,400"),
   (f"the seven-day ordinary pass {OFF}", "¥50,000"),
 ],
 "verdict": (
   "<strong>Count your long journeys before you buy, not after.</strong> Divide the pass "
   "price by a Tokyo–Kyoto fare and it needs roughly four legs of that distance to break "
   "even — about two round trips inside seven days. The classic first trip makes two. The "
   "deeper cost is not the ¥50,000: it is that a pass already paid for quietly argues for "
   "more legs, and the route bends to justify the purchase instead of the purchase following "
   "the route."
 ),
 "reasoning": """<p>Two details sit on the credit side and are worth naming, because the arithmetic above
is deliberately unkind to the pass. It also covers local JR lines inside the cities and the
airport express from Narita, which is real value that is easy to forget when you are counting
only the long legs. {EST} And it converts every journey into a decision you no longer have to
make, which has a convenience worth something even when the money does not work.</p>

<p>The honest counter is that neither of those closes a ¥22,000 gap. If your route makes two
long journeys, you would need the incidental local travel to be worth more than most first
trips generate before the pass draws level, and the trips where it does draw level are
precisely the ones that were already going to reach four legs.</p>""",
 "for": [
   "then buy it → the route reaches Hiroshima or returns north through the mountains",
   "then buy it → four or more long legs inside a single seven-day window",
   "then buy it → you want unlimited spontaneity more than you want ¥20,000",
 ],
 "against": [
   "then skip it → Tokyo, Kyoto, home (the shape most first trips take)",
   "then skip it → your long legs are spread across twelve days, not seven",
   "then skip it → a regional pass covers the one area you move around in",
 ],
 "note": (
   f"{VOL} Field Sheet. Pass prices, the Tokyo–Kyoto fare, and the 1 October 2026 rise that "
   "hits overseas-agency purchases but not the official site. Re-run the division; the method "
   "outlives every number in it."
 ),
},

# ── 03 ───────────────────────────────────────────────────────────────────────
{
 "n": "03",
 "plate": "A03", "plate_cap": "The gate that refuses you. The reader panel is the thing your phone has to satisfy, and a US-issued Visa cannot — which is a four-minute problem at home and an afternoon here.", "cat": "Transit",
 "q": "Which card will load on an American phone?",
 "cols": "CARD · WILL IT LOAD",
 "lede": (
   "Japanese city transit offers three ways to pay and most visitors default to whichever one "
   "they read about first. That is a survivable mistake. The unsurvivable one is arriving with "
   "a phone that cannot top itself up, discovering it at a Shinjuku gate at nine in the "
   "morning, and losing the first afternoon to a problem that takes four minutes to solve on "
   "your own sofa."
 ),
 "table_title": "Topping up a mobile Suica in Apple Wallet · US-issued cards",
 "rows": [
   (f"US-issued Visa {SUR}", "refused — the common failure"),
   (f"US-issued Mastercard {SUR}", "works for Suica, not for Pasmo"),
   (f"US-issued American Express {SUR}", "works"),
   (f"cash, at any station machine {EST}", "always works"),
 ],
 "verdict": (
   "<strong>Create the card at home, load it with the card you intend to use, and watch the "
   "top-up complete before you fly.</strong> A US Visa is refused inside Apple Wallet while "
   "Mastercard and Amex go through, which is not documented anywhere official and produces a "
   "meaningless error rather than an explanation. If every card you own is Visa, the answer is "
   "not to keep retrying it at the gate: it is a physical card from a station machine, fed "
   "cash, which sidesteps the card networks entirely."
 ),
 "reasoning": """<p>The reason this fails so specifically is that the refusal happens inside Apple Wallet
rather than at the card network, so the error you see describes nothing useful and your bank
shows no declined transaction to investigate. {SUR} People conclude the card is broken, or that
their phone is, and try the same card repeatedly at a gate.</p>

<p>There is a second failure that looks identical and is not your card at all: a nightly
maintenance window during which top-ups fail for everyone, running until roughly four in the
morning Japan time. {SUR} A failure at two in the morning is a clock problem, not a payment
problem, and the fix is to wait rather than to start deleting and re-adding cards.</p>""",
 "for": [
   "then use the phone → you hold a Mastercard or Amex and set it up before departure",
   "then use the phone → Express Mode means you tap without unlocking, even on a flat battery",
 ],
 "against": [
   "then carry plastic → Visa-only, or an Android handset bought outside Japan",
   "then carry plastic → you would rather feed a machine ¥3,000 than debug a wallet",
 ],
 "note": (
   f"{VOL} Field Sheet. Which networks load, the nightly maintenance window that fails every "
   "card until about 04:00, and the physical-card deposit. The Visa behaviour rests on user "
   "reports, not an official statement — date it and re-check."
 ),
},

# ── 04 ───────────────────────────────────────────────────────────────────────
{
 "n": "04", "tailfig": "season-compare", "cat": "Season",
 "q": "When should you come, and what does the date cost?",
 "cols": "WINDOW · WHAT IT ASKS OF YOU",
 "fig": "season-grid",
 "lede": (
   "Cherry blossom is the reason most people first think about Japan and the worst single "
   "week to build a plan around. The bloom holds for roughly a week in any one city, the "
   "forecast that predicts it does not exist until February, and the rooms you would need "
   "were gone in October. You are asked to commit six months before anyone can tell you "
   "whether the thing you are committing to will be there."
 ),
 "table_title": "The four windows · what each one demands",
 "rows": [
   (f"late March – early April, bloom {EST}", "book ~6 months out, on faith"),
   (f"late April – early May, Golden Week {OFF}", "avoid moving cities entirely"),
   (f"second half of November, foliage {EST}", "book 2–3 months out, colour holds weeks"),
   (f"January – February, low season {EST}", "book weeks out, sites near-empty"),
 ],
 "verdict": (
   "<strong>If the dates are yours to choose, take late November.</strong> Autumn colour "
   "lasts weeks rather than days, the weather is settled, the booking lead is a third of "
   "spring's, and you are not paying peak prices for a probability. Cherry blossom is worth "
   "the gamble on a second trip, when the cities themselves are no longer new and losing the "
   "flowers costs you an image rather than the trip. Choose the season deliberately; it "
   "decides the booking deadline, which decides everything downstream of it."
 ),
 "reasoning": """<p>What makes the spring window genuinely hard is not the crowds but the order the
decisions arrive in. The rooms must be committed roughly six months out; the forecast that
would tell you whether to commit does not exist until February. {EST} You are not choosing
between a good bet and a bad one, you are choosing whether to bet at all, months before the
information exists.</p>

<p>Autumn inverts every term of that. The colour holds for weeks rather than a week, the
weather is settled rather than volatile, and a two-to-three month booking lead is short enough
that you are deciding with most of the information already in hand. The spectacle is quieter;
the planning is a different activity altogether.</p>""",
 "for": [
   "then come in spring → the blossom <em>is</em> the trip and you accept the odds",
   "then come in spring → you can book cancellable and move within a fortnight",
 ],
 "against": [
   "then move the dates → Golden Week or mid-August Obon, if the plan involves moving cities",
   "then move the dates → you want the famous gardens without the compressed crowds",
 ],
 "note": (
   f"{OFF} Golden Week is built from four fixed holidays between 29 April and 5 May, but the "
   "substitute-holiday rule changes the length of the run every year. Never freeze one year's "
   "dates into a plan — check the calendar for yours."
 ),
},

# ── 05 ───────────────────────────────────────────────────────────────────────
{
 "n": "05", "tailfig": "kyoto-bus", "cat": "Base",
 "q": "Which station should you sleep next to?",
 "cols": "AREA · WHAT THE LOCATION BUYS",
 "fig": "tokyo-lines",
 "lede": (
   "In a compact European capital the question is which neighbourhood you want to walk out "
   "into. Tokyo does not work like that. It is a transit graph before it is a set of "
   "neighbourhoods, and the practical question is not which district charms you on a map but "
   "which line you will be standing on at eight in the morning and eleven at night."
 ),
 "table_title": "Tokyo bases · what each one is for",
 "rows": [
   (f"Shinjuku {EST}", "most connections, least calm"),
   (f"Tokyo Station / Marunouchi {EST}", "Shinkansen at the door, quiet at night"),
   (f"Shibuya {EST}", "nightlife and the Yamanote line"),
   (f"Asakusa {EST}", "cheapest, oldest, furthest from the rest"),
 ],
 "verdict": (
   "<strong>Sleep on the Yamanote loop, and in Kyoto ignore the subway entirely.</strong> "
   "Almost everything a first trip does in Tokyo touches the Yamanote line, so a room within "
   "a few minutes of any of its stations removes a daily tax you would otherwise pay in "
   "transfers. Kyoto inverts the logic: it is a bus city with two subway lines that do not go "
   "where the temples are, so proximity to a major bus corridor beats proximity to a station."
 ),
 "reasoning": """<p>The Yamanote rule works because of what a first trip does rather than because of
anything about the neighbourhoods. Almost every destination on a standard Tokyo list sits on
or one stop from that loop, so a room near any of its stations turns most journeys into a
single ride with no transfer. {EST} A cheaper room three transfers away charges the difference
back twice a day, in the currency of a trip that is short.</p>

<p>Kyoto has to be reasoned about separately, and travellers who apply Tokyo logic there get
it wrong in a specific way. Kyoto has two subway lines and its temples are scattered around
the edges of the city, which is why the buses do the real work. {EST} A hotel chosen for
subway access can be further from the day's sights than one chosen for a bus corridor.</p>""",
 "for": [
   "then take Shinjuku → you want one station to solve every journey and do not mind the scale",
   "then take Marunouchi → you are taking the Shinkansen and value a quiet evening",
 ],
 "against": [
   "then look again → the room is cheap because it is three transfers from the loop",
   "then look again → you picked a Kyoto hotel by subway access and will be taking buses",
 ],
 "note": (
   f"{EST} In Kyoto the practical unit is the bus corridor, not the station; "
   "a hotel near Shijo or Kawaramachi reaches the eastern temples without a transfer."
 ),
},

# ── 06 ───────────────────────────────────────────────────────────────────────
{
 "n": "06",
 "plate": "A06", "plate_cap": "Mineral water and steam. This is the evening the ryokan is selling; it is a poor fit for a Kyoto night, where the city itself is the evening.", "cat": "Sleep",
 "q": "Is the ryokan worth it, and where should it be?",
 "cols": "NIGHT · WHAT IS INCLUDED",
 "lede": (
   "The ryokan is the one night of a Japan trip people describe years later, and it is also "
   "the one most often booked in the wrong city, on the wrong night, at a price the traveller "
   "never quite compares to anything. It is not a hotel with tatami. It is dinner, breakfast, "
   "a bath and a room sold as a single evening, which makes the nightly rate the wrong number "
   "to judge it by."
 ),
 "table_title": "What the rate covers",
 "rows": [
   (f"business hotel, city centre {EST}", "room only"),
   (f"ryokan, half board {EST}", "room + kaiseki dinner + breakfast + bath"),
   (f"the comparison people make {EST}", "rate vs rate — wrong"),
   (f"the comparison to make {EST}", "rate vs room + two meals out"),
 ],
 "verdict": (
   "<strong>One night, in an onsen town, not in Kyoto.</strong> A ryokan works when the "
   "building and the bath <em>are</em> the evening — which means arriving by mid-afternoon "
   "and going nowhere afterwards. That is a poor fit for Kyoto, where the evening is the city "
   "itself, and an excellent fit for Hakone, Kinosaki or the Japan Sea side. Price it against "
   "a hotel room plus two restaurant meals and the premium shrinks to something defensible."
 ),
 "reasoning": """<p>The comparison people make is rate against rate, and it is the wrong one. A ryokan
at half board is a room, a multi-course dinner, breakfast and the bath, sold as one evening;
a business hotel at half the price is a room. {EST} Priced against a hotel night plus two
restaurant meals, the premium narrows to something a traveller can actually judge.</p>

<p>Where it goes wrong is placement rather than price. The format asks you to arrive by
mid-afternoon, change, bathe, eat at the hour the kitchen serves, and stay in. That is a
poor fit for a Kyoto night, where the city itself is the evening, and an excellent one in a
hot-spring town where there is nowhere else to be.</p>""",
 "for": [
   "then book it → you can arrive by 15:00 and have nothing else scheduled that evening",
   "then book it → winter, when the outdoor bath is the entire argument",
 ],
 "against": [
   "then skip it → it is your Kyoto night and you wanted to eat in Gion",
   "then skip it → you have visible tattoos and have not checked that specific bath's rule",
 ],
 "note": (
   f"{EST} Tattoo policy is set per property and is still commonly enforced at public baths. "
   "Many ryokan solve it with a private or in-room bath — ask before booking, not on arrival."
 ),
},

# ── 07 ───────────────────────────────────────────────────────────────────────
{
 "n": "07", "tailfig": "eat-layers", "cat": "Eating",
 "q": "How do you eat well without a reservation system you can use?",
 "cols": "APPROACH · WHAT IT COSTS YOU",
 "lede": (
   "First-timers over-plan meals the way they over-plan sights, researching a specific "
   "restaurant for every slot on the itinerary — and in Japan that effort converts badly. The "
   "best places are small, often unlisted, frequently unbookable from abroad, and the ones "
   "that <em>are</em> bookable from abroad are disproportionately the ones that market to "
   "foreigners. Planning harder makes the food worse."
 ),
 "table_title": "Four ways to eat, and what each delivers",
 "rows": [
   (f"researched restaurant, booked from the US {EST}", "high effort, uneven result"),
   (f"depachika food hall, ground floor {EST}", "no booking, excellent, cheap"),
   (f"counter seat, walk in at opening {EST}", "no booking, the real thing"),
   (f"konbini, between meals {EST}", "very good, ¥500"),
 ],
 "verdict": (
   "<strong>Book two meals for the whole trip and let the rest happen.</strong> Reserve the "
   "one or two dinners you would be sad to miss and leave every other slot open, because the "
   "upside in Japan sits at counters you cannot book and department-store basements no guide "
   "sends you to. The failure mode here is not eating badly — it is hard to eat badly — it is "
   "spending the trip executing a spreadsheet through a country that rewards walking in."
 ),
 "reasoning": """<p>The reason effort converts badly here is structural. The places a first-timer would
most enjoy are small, frequently unlisted in English, and often unbookable from abroad — while
the ones that <em>are</em> easily bookable from abroad are disproportionately the ones that
market to foreigners. {EST} Sorting restaurants by how reachable they are from Ohio in February
selects against the thing you came for.</p>

<p>The layer that rewards walking in is also the layer that is hardest to research: counters
with six seats, a ticket machine at the door, one dish done for thirty years. {EST} Leaving
slots open is not a lack of planning. It is the plan that matches how the good places
actually work.</p>""",
 "for": [
   "then book ahead → a specific sushi counter or kaiseki room is a reason you came",
   "then book ahead → a birthday, an anniversary, anything that cannot be improvised",
 ],
 "against": [
   "then leave it open → you are filling slots because they are empty",
   "then leave it open → the restaurant takes foreign bookings easily (ask why)",
 ],
 "note": (
   f"{EST} Department-store basements — the depachika — take no booking, cost nothing to walk "
   "into, and carry prepared food of a standard that would be a destination restaurant "
   "elsewhere. It is the most reliable good meal in any Japanese city and almost no "
   "first-timer is sent there."
 ),
},

# ── 08 ───────────────────────────────────────────────────────────────────────
{
 "n": "08", "cat": "Arrival",
 "q": "Which airport, and what happens in the first six hours?",
 "cols": "AIRPORT · INTO THE CITY",
 "fig": "arrival",
 "lede": (
   "The airport looks like a price decision and behaves like an itinerary decision. Narita "
   "and Haneda are both fine airports with good transfers; the difference is what each one "
   "does to the evening you land, and a first evening lost to a ninety-minute train after "
   "eleven hours in the air is a real cost that never appears in the fare comparison."
 ),
 "table_title": "Getting into central Tokyo",
 "rows": [
   (f"Haneda {EST}", "~30 min, close to the centre"),
   (f"Narita {EST}", "~60–90 min depending on the service"),
   (f"either, after a 13:00 landing {EST}", "you get an evening"),
   (f"either, after a 20:00 landing {EST}", "you get a hotel bed"),
 ],
 "verdict": (
   "<strong>Pay a modest premium for Haneda, and pay more attention to the landing "
   "time.</strong> Haneda is meaningfully closer and worth a small fare difference, but the "
   "variable that decides your first day is when the wheels touch — an early "
   "afternoon landing at Narita beats a late-evening landing at Haneda every time. Set the "
   "transit card up before you fly and the first hour on the ground is a train, not a queue "
   "at a machine you are too tired to read."
 ),
 "reasoning": """<p>The reason landing time outranks the airport is that the transfer is fixed and your
capacity is not. An hour saved arriving at Haneda is a real hour, but it is an hour spent by
someone who has been awake for twenty. {EST} After a late landing, the difference between a
thirty-minute transfer and a ninety-minute one is the difference between going to bed and
going to bed later.</p>

<p>The variable worth optimising is therefore the schedule, not the airport code. An early
afternoon arrival gives you a usable evening from either airport: a walk, a first meal, and
enough daylight to start resetting the clock. That evening is also the cheapest day of the
trip to lose, which is why nothing worth seeing should be scheduled into it.</p>""",
 "for": [
   "then take Haneda → the fares are within a couple of hundred dollars",
   "then take Haneda → you land late and want the shortest possible transfer",
 ],
 "against": [
   "then take Narita → the saving is real and you land before mid-afternoon",
   "then take Narita → the schedule fits the rest of the route better",
 ],
 "note": (
   f"{VOL} Field Sheet. Airport transfer fares and the limousine-bus timetables. The rule — "
   "landing time outranks airport choice — does not move."
 ),
},
# ── 09 ───────────────────────────────────────────────────────────────────────
{
 "n": "09", "cat": "Sights",
 "q": "How many temples before they stop working?",
 "cols": "THE DAY · WHAT YOU KEEP",
 "lede": (
   "A first trip arrives with a list of famous names and the assumption that the constraint "
   "is time: fit in as many as the days allow. The constraint is not time. It is attention, "
   "and it runs out earlier than anyone plans for &#8212; which is why the classic Kyoto "
   "mistake is not missing something, it is seeing six things and remembering two."
 ),
 "table_title": "What the day returns, by how much you put in it",
 "rows": [
   ("two major temples, plus a market or a street {EST}", "both, distinctly"),
   ("three major temples, spaced {EST}", "two and a half"),
   ("four or more, back to back {EST}", "they blur"),
   ("one, at opening, then nothing scheduled {EST}", "the one you describe later"),
 ],
 "reasoning": """<p>Our own reporting has a word for this &mdash; temple fatigue &mdash; and it
is not a joke about tired feet. Japanese religious architecture is deliberately repetitive: the same forms, the
same materials, the same spatial logic, refined across centuries. That is precisely what
makes it extraordinary and precisely why the fifth one in a day reads as the fourth. The
distinctions that reward attention are the ones attention has stopped making. {EST}</p>

<p>The counter-move is not fewer days of sightseeing. It is contrast inside the day &#8212; a
market, an ordinary neighbourhood, a long lunch, a walk along a canal &#8212; because the next
temple lands properly only after something that is not a temple. Two major sites with
something unlike them in between returns more than four in sequence, and it is the same
number of hours. {EST}</p>""",
 "verdict": (
   "<strong>Two major temples a day, three if they are spread, and never four.</strong> Put "
   "something that is not a temple between them, and take the most famous one at opening "
   "when it is still a building rather than a queue. The instinct to maximise is the thing "
   "to resist: a Kyoto day that does less is a Kyoto day you can still describe a year "
   "later, and that is the only measure of a sight that matters once you are home."
 ),
 "for": [
   "then push to four &#8594; they are small, close together, and you are genuinely fresh",
   "then push to four &#8594; it is your only day in the city and you accept the blur",
 ],
 "against": [
   "then cut to two &#8594; you are on day six and everything is starting to look similar",
   "then cut to two &#8594; the weather is good and walking somewhere ordinary is available",
 ],
 "note": (
   "{EST} The rule generalises past Kyoto. It is the same arithmetic in any city whose "
   "attraction is an accumulation of related things &#8212; and it is why the quieter temples "
   "most visitors never make time for are often the ones they remember."
 ),
},
]
