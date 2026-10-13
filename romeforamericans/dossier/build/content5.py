# content5.py — arrival ops, timing, booking horizons, the plan, stay, kit, field sheet.
from content import E,O,S,V
from maps import MAP_HOOD, GFX_TREE
from content2 import HOODS_TXT, hood_block

DAYZERO_1 = f"""
<div class="eyebrow">CHAPTER THREE <span>· DAY ZERO</span></div>
<h1 class="t">The landing, before the jet lag lifts</h1>
<div class="standfirst">Arrival is a solved problem the moment you stop improvising it. Two
decisions — how you get in, whether you connect — set the tone for everything after.</div>
{{FIG_ARRIVAL}}
<p class="b cap1">The corridor out of Fiumicino baggage claim is lined with soft offers —
'taxi, taxi, best price' — and they are the one unpriced option in the transfer.
Everything legitimate has a fixed number attached. {O} The Leonardo Express runs non-stop
to Termini about every fifteen minutes and cannot be caught in traffic; it is the default
for one or two travellers, and the fastest line on the board at roughly half an hour. {S}
For three or four people the flat-rate taxi divides into fair value and drops you at your
door; solo, it is a multiple of the train for the same jet lag.</p>
<p class="b">The clever move for Trastevere and Testaccio bases is the FL1 regional, which
pointedly skips Termini for Trastevere, Ostiense and Tiburtina — closer to your bed than
the grand station ever gets. {E} Whichever you pick, buy the airport leg as its own ticket;
no city pass and no day cap covers it. Ciampino, if you flew a budget carrier, runs on the
same logic with a smaller flat fare and no train at all. {V}</p>
<p class="b">Connectivity is the other Day Zero lever. An eSIM installed at home means you
walk out of arrivals already online — maps, tickets, the taxi's fixed-fare confirmation —
without the SIM-counter queue or the roaming shock. {S} It has become the clear default for
2026; the provider you pick is a Field Sheet §3 detail, the habit is the point.</p>
"""

TIMING_1 = f"""
<div class="eyebrow">CHAPTER FOUR <span>· TIMING</span></div>
<h1 class="t">The week, as the sights keep it</h1>
<div class="standfirst">Rome's monuments run on their own calendar, and it is not yours.
Reading it once turns a wasted Monday into a non-event.</div>
{{FIG_WEEK}}
<p class="b">The closures cluster with a logic worth internalising. Mondays take the
Borghese, Castel Sant'Angelo and Ostia Antica — a bad day to have scheduled any of the
three, a fine day for the ancient core, which does not close. {O} Sundays flip the board:
the Vatican Museums shut except the last Sunday of the month, when they open free and fill
to the walls — a bargain that costs you the experience. {O} Testaccio's market sleeps
Sundays too. And Wednesday mornings the Papal Audience claims St Peter's Square, running
the Museums as normal while the basilica waits for afternoon. {O}</p>
<p class="b">One recurring gift hides in the noise: state museums open free on the first
Sunday of each month. {O} It is real and worth timing — but the reservation-only sites, the
Borghese chief among them, still demand their booking, free entry or not. {E} The grid
above is the entire pattern; photograph it before you lock your days.</p>
"""

TIMING_2 = f"""
<div class="eyebrow">TIMING <span>· THE SEASON, UP CLOSE</span></div>
<h1 class="t">Twelve months, three pressures</h1>
<div class="standfirst">Heat, crowds and price move together but not identically — and August
is a special case that rewrites the daily plan entirely.</div>
{{FIG_MONTHS}}
<p class="b">The two windows — late April into May, September into October — are common
knowledge for the honest reason that they are correct: warm days, tolerable crowds, the
city at its photogenic best. {E} Winter inverts every value: short grey days and some rain,
against thin lines, low fares and a centro you can have to yourself by dusk. The
connoisseur's contrarian pick, if the light doesn't rule you.</p>
<p class="b">Summer demands a different document. From June the heat turns midday sightseeing
into an endurance test, and Ferragosto — August 15 and the days around it — empties Rome of
Romans: family shops shuttered, the trattoria owner at the coast, the monuments baking for
whoever stayed. {E} If you go then, go on purpose and invert the clock: ruins and outdoor
sites at opening, a long shaded siesta through the worst of it, museums and churches in the
afternoon, dinner and the passeggiata when the stone finally gives back its heat. {S} The
season doesn't have to beat you; it just has to be planned for.</p>
"""

HORIZONS = f"""
<div class="eyebrow">CHAPTER FOUR <span>· HORIZONS</span></div>
<h1 class="t">What to book, and how far ahead</h1>
<div class="standfirst">The single ledger that turns Decision 04 into an afternoon's work.
Book from the top down; the order is the order things sell out.</div>
<div class="led-h"><span>The sell-out ledger · lead times as observed, windows on the Sheet</span>
<span class="cols">BOOK BY</span></div>
<table class="led">
<tr><td>Borghese Gallery — hard reservation, no walk-ins, small capacity {E}</td><td class="num">WEEKS</td></tr>
<tr><td>Colosseum · Full Experience — guided, smallest allocation, goes first {S}</td><td class="num">WEEKS</td></tr>
<tr><td>Papal Audience — free ticket, Wednesdays, ordered ahead {O}</td><td class="num">WEEKS</td></tr>
<tr><td>Vatican Museums — timed entry; season sets the horizon {S}</td><td class="num">DAYS–WEEKS</td></tr>
<tr><td>Colosseum · standard combined — releases move; buy early anyway {S}</td><td class="num">DAYS</td></tr>
<tr><td>Pantheon — newly ticketed, short horizon, real door queue {O}</td><td class="num">DAYS</td></tr>
<tr><td>High-speed day-trip seats — fares float like airfares {E}</td><td class="num">T−7</td></tr>
<tr><td>Good dinner rooms — a day out, like the locals {S}</td><td class="num">T−1</td></tr>
<tr><td>Everything else in Rome — decided over breakfast {E}</td><td class="num">SAME DAY</td></tr>
</table>
<p class="b">Two principles hold the ledger together. First, one official seller per site;
the rest are resale or tours wrapped around the same entry, and telling them apart before
you pay is most of the skill. {S} Second, a tour can rescue a slot you missed, but nothing
rescues a walk-up at a reservation-only door — the Borghese will turn you away in an empty
room. {E} Live release windows, official links and this season's Vatican horizon live on
the Field Sheet §2, because they are the numbers most likely to have moved since printing. {V}</p>
"""

# ── THE PLAN — three operational day pages ───────────────────────────────────
PLAN_1 = f"""
<div class="eyebrow">CHAPTER EIGHT <span>· THE PLAN</span></div>
<h1 class="t">Day one — the ancient core, then the centre on foot</h1>
<div class="standfirst">The pillars of imperial Rome in a single morning's sequence, then the
Baroque city as an afternoon's unplanned drift toward dinner across the river.</div>
{{FIG_DAY1}}
<p class="b">Start high and early on the booked Colosseum slot. Take the combined ticket
straight into the Forum and up the Palatine while the light is still kind, finishing on the
Capitoline's free balcony with the ancient city arranged below. {E} That is the
morning's work — one admission, one direction, done by lunch.</p>
<p class="b">The afternoon needs no schedule. Walk the Baroque centre the way it rewards —
Pantheon, Piazza Navona, the Trevi, Campo de' Fiori — letting the five-to-eight-minute hops
between them fill with churches, gelato and fountains you didn't plan on. {E} As the light
goes gold, cross into Trastevere for the first real Roman dinner; aperitivo at six is the
bridge, eight o'clock is the table.</p>
{{PHOTO_A08}}
"""

PLAN_2 = f"""
<div class="eyebrow">THE PLAN <span>· DAY TWO</span></div>
<h1 class="t">Day two — the Vatican, then back across the river</h1>
<div class="standfirst">One state, one morning operation, run on the early slot — then the
long diagonal home through the streets the tour buses never touch.</div>
{{FIG_DAY2}}
<p class="b">Book the first Museums slot and arrive twenty-five minutes ahead for security.
Walk with intent — Raphael Rooms, then the Sistine at the route's end — and step into St
Peter's afterward through its own line, dressed to the shoulders-and-knees code, the dome
climb a clear-headed yes or a guilt-free no. {S} By early afternoon the property is behind
you and the groups are just arriving.</p>
<p class="b">Cross back over the river via Castel Sant'Angelo — the terrace view is the dome
climb's cheaper rival — and let the afternoon dissolve into the centro's north end: Piazza
del Popolo, the Spanish Steps (admired standing; sitting is fined), the lanes toward
Navona. {O} Dinner wherever the Decision 10 filter points, a block off the postcard.</p>
"""

PLAN_3 = f"""
<div class="eyebrow">THE PLAN <span>· DAY THREE</span></div>
<h1 class="t">Day three — the gallery, then the city that eats</h1>
<div class="standfirst">The day the trip stops being a checklist: one sublime gallery by
appointment, then the neighborhoods where Rome feeds itself.</div>
{{FIG_DAY3}}
<p class="b">Open on the Borghese, on the timed ticket you booked weeks ago — two hours with
Bernini's marble made flesh and the Caravaggios, in a building that admits no one without a
slot. {E} Walk it off downhill through the Villa Borghese gardens to the top of the Spanish
Steps and into the shopping streets, or straight to an early lunch in the Jewish Ghetto,
where the fried artichokes are the point. {S}</p>
<p class="b">Give the afternoon to the quarters that don't perform for visitors — Testaccio's
covered market and Roman-canon trattorie, Ostiense's street art and the pyramid — and let
dinner be the trip's best, booked a day ahead in a room full of locals. {S} This is the day
people mean when they say they want to go back.</p>
"""

# ── STAY — intro grid + assessments + tree ──────────────────────────────────
def STAY_ASSESS_1():
    blocks="".join(hood_block(k,n,w,e,b,c,MAP_HOOD(k)) for k,n,w,e,b,c in HOODS_TXT[:3])
    return f"""<div class="eyebrow">CHAPTER NINE <span>· WHERE TO STAY</span></div>
<h1 class="t">Six bases, one yardstick</h1>
<div class="standfirst">Decision 01 gives the verdict; these pages give the evidence. Each
locator sets the neighborhood against the same ring, measured to the same point.</div>
{blocks}"""

def STAY_ASSESS_2():
    blocks="".join(hood_block(k,n,w,e,b,c,MAP_HOOD(k)) for k,n,w,e,b,c in HOODS_TXT[3:])
    return f"""<div class="eyebrow">THE ASSESSMENTS <span>· CONTINUED</span></div>{blocks}
<p class="b">The pattern the locators make is the whole argument: the closer the dot sits to
the Pantheon's cross-hair, the less this trip spends on getting around and the more it spends
on Rome. {E} Distance is not disqualifying — Monti and Prati trade a few minutes for real
value, Trastevere trades them for its evenings — but it should be a choice you make with the
meter in view, not a discovery you make on the third tired night.</p>
<div class="note">Rooms are the one price this book refuses to print — they move by season, by dates, by the week you happen to search (Decision 03). {V} The verdict is durable; the rate is yours to hunt.</div>"""

def STAY_TREE():
    return f"""<div class="eyebrow">WHERE TO STAY <span>· IN FOUR QUESTIONS</span></div>
<h1 class="t">The base, decided on one page</h1>
<div class="standfirst">Every assessment on the previous pages, compressed to the four
questions that actually separate the neighborhoods.</div>
{GFX_TREE()}
<p class="b">The tree encodes the same logic the assessments argue at length: first visits
pay for the centre if the budget allows; mornings-people and evenings-people split on the
river; the budget-bound choose between Monti's character and Termini's convenience with
clear eyes. {E} No branch is wrong — they simply optimise for different things, which is the
real shape of the decision.</p>"""

# ── KIT — the wallet card ────────────────────────────────────────────────────
KIT = f"""
<div class="eyebrow">CHAPTER TWELVE <span>· THE KIT</span></div>
<h1 class="t">The wallet card</h1>
<div class="standfirst">The whole book, compressed to what fits in a pocket. Screenshot this
page; it is the only one you need on the ground.</div>
<div class="wallet">
<div class="wh"><span>ROME · THE POCKET CARD</span><span>2026.07</span></div>
<div class="wb">
<div class="wc"><h5>ON ARRIVAL</h5>
<div>Leonardo Express if 1–2; flat taxi if 3–4 / midnight {S}</div>
<div>FL1 for Trastevere / Testaccio beds {E}</div>
<div>eSIM already on — skip the SIM queue {S}</div>
<div>Airport leg is its own ticket {E}</div></div>
<div class="wc"><h5>EVERY DAY</h5>
<div>Walk it — inside the ring, feet win {E}</div>
<div>Tap contactless; the cap protects you {V}</div>
<div>Validate any paper ticket {O}</div>
<div>Bag front on 64/40, Termini, Metro A {S}</div></div>
<div class="wc"><h5>MONEY</h5>
<div>EUROS at every prompt {E}</div>
<div>Bank-attached ATMs only {S}</div>
<div>Small notes: coperto, coffee, market {S}</div>
<div>Tip = round up €1–2 {E}</div></div>
</div>
<div class="wb" style="border-top:1px solid var(--line)">
<div class="wc"><h5>EATING</h5>
<div>Coffee standing, al banco, pay first {E}</div>
<div>Ninety seconds off the piazza {S}</div>
<div>Cacio e pepe · carbonara · amatriciana · gricia {E}</div>
<div>Dinner from 8; book good rooms a day out {S}</div></div>
<div class="wc"><h5>THE BIG FOUR</h5>
<div>Borghese — weeks out, no walk-ins {E}</div>
<div>Colosseum — one official seller {S}</div>
<div>Vatican — first slot, T−25 security {S}</div>
<div>Pantheon — short horizon, still a queue {O}</div></div>
<div class="wc"><h5>THE CODE</h5>
<div>No sitting on the Spanish Steps {O}</div>
<div>Validate transit tickets {O}</div>
<div>Shoulders + knees for churches {O}</div>
<div>Street gifts are invoices — walk on {S}</div></div>
</div>
</div>
"""

# ── THE FIELD SHEET — the volatile layer, drawn ONLY from the fact-DB keys ────
# §1 values are the 12 data-fact spans, verbatim; nothing else earns a number here.
FS_1 = """
<div class="fs-band">
<div class="eyebrow">THE FIELD SHEET · §1</div>
<h1>Verified at press time</h1>
<div class="standfirst">EDITION 2026.07 · ROME, SOLVED. · REISSUED QUARTERLY</div>
</div>
<p class="b" style="margin-bottom:14px">Every number the book pushed to this page, resolved
from the site's fact database at export — 14 July 2026. Confirm the starred lines in your
own travel week (§2); use the rest as your working figures.</p>
<div class="led-h"><span>Getting in from the airport</span><span class="cols">FIXED FARE</span></div>
<table class="led">
<tr><td>Leonardo Express — Fiumicino to Termini, non-stop</td><td class="num">€14</td></tr>
<tr><td>FL1 regional — Fiumicino to Trastevere / Ostiense / Tiburtina</td><td class="num">€8</td></tr>
<tr><td>Taxi, flat fare — Fiumicino to inside the Aurelian walls</td><td class="num">€55</td></tr>
<tr><td>Taxi, flat fare — Ciampino to inside the walls</td><td class="num">€40</td></tr>
</table>
<div class="led-h"><span>Getting around the city</span><span class="cols">PRICE / RULE</span></div>
<table class="led">
<tr><td>Single bus / metro ticket (BIT)</td><td class="num">€1.50</td></tr>
<tr><td>BIT validity — from first validation</td><td class="num">100 MIN</td></tr>
<tr><td>Fine for an unvalidated / no ticket</td><td class="num">€100+</td></tr>
<tr><td>Colosseum combined ticket — validity window</td><td class="num">24 H</td></tr>
</table>
<div class="led-h"><span>Entry &amp; the paperwork clock</span><span class="cols">STATUS</span></div>
<table class="led">
<tr><td>Schengen visa-free stay — U.S. passport, per 180 days</td><td class="num">90 DAYS</td></tr>
<tr><td>ETIAS travel authorisation — at press time *</td><td class="num">NOT YET REQUIRED</td></tr>
<tr><td>ETIAS — signalled launch *</td><td class="num">LATE 2026</td></tr>
<tr><td>U.S. State Dept advisory for Italy *</td><td class="num">LEVEL 2</td></tr>
</table>
<div class="note">Method — figures resolved from the site's fact database at export, 14 July
2026. A number here is a starting point, not a promise; the machine at the counter is the
final authority. Starred lines change by government or season — cross-check in §2.</div>
"""

FS_2 = """
<h1 class="t">§2 · Confirm in your travel week</h1>
<div class="standfirst">These the book deliberately prints no number for — they move too
often to trust in ink. Each line names the one official source that carries the live figure.</div>
<div class="led-h"><span>What to check, and where the truth lives</span><span class="cols">SOURCE</span></div>
<table class="led">
<tr><td>Pantheon entry fee &amp; timed-slot booking</td><td class="num">museiitaliani · official</td></tr>
<tr><td>Colosseum / Forum / Palatine — price &amp; the Full Experience release window</td><td class="num">parcocolosseo · coopculture</td></tr>
<tr><td>Borghese Gallery — slot availability &amp; reservation</td><td class="num">galleriaborghese · official</td></tr>
<tr><td>Vatican Museums — hours, price, this season's booking horizon</td><td class="num">museivaticani.va</td></tr>
<tr><td>Vatican — the free last Sunday (open &amp; mobbed)</td><td class="num">museivaticani.va</td></tr>
<tr><td>Papal Audience — Wednesday calendar &amp; free ticket</td><td class="num">Prefecture of the Papal Household</td></tr>
<tr><td>State museums — the first-Sunday free list</td><td class="num">cultura.gov.it</td></tr>
<tr><td>Roma Pass / Omnia — current price &amp; covered sites</td><td class="num">romapass · official</td></tr>
<tr><td>High-speed fares — Rome to Naples / Florence</td><td class="num">Trenitalia · Italo apps</td></tr>
<tr><td>Regional day-trip fares — Ostia, Castelli, Tivoli, Orvieto corridor</td><td class="num">Trenitalia regionale</td></tr>
<tr><td>ETIAS — whether it is live for your dates</td><td class="num">travel-europe.europa.eu</td></tr>
<tr><td>Advisory notes &amp; any strike / event for your week</td><td class="num">travel.state.gov · local news</td></tr>
</table>
<div class="note">Rule of thumb — if a figure could embarrass you at a ticket window, it
belongs on this list, not in the book. One official seller per site; everything else resells
it or wraps a tour around it.</div>
"""

FS_3 = f"""
<h1 class="t">§3 · Calendar notes &amp; habits</h1>
<div class="standfirst">The moving pieces that aren't prices — dates that shift yearly, and the
two small habits that keep the trip smooth.</div>
<div class="led-h"><span>Dates that move each year</span><span class="cols">WHEN</span></div>
<table class="led">
<tr><td>Ferragosto — the mid-August shutdown; locals leave, shops shutter</td><td class="num">AUG 15 ±</td></tr>
<tr><td>Easter week — beautiful, mobbed, peak-priced</td><td class="num">MOVES</td></tr>
<tr><td>First Sunday of the month — state museums free</td><td class="num">MONTHLY</td></tr>
<tr><td>Last Sunday of the month — Vatican free &amp; overwhelmed</td><td class="num">MONTHLY</td></tr>
<tr><td>Christmas &amp; New Year — holiday closures and surges</td><td class="num">DEC–JAN</td></tr>
</table>
<div class="led-h"><span>Two habits worth keeping</span><span class="cols">DO</span></div>
<table class="led">
<tr><td>eSIM — install &amp; test at home; land connected (provider picks age fast)</td><td class="num">T−7</td></tr>
<tr><td>Booking QRs — screenshot to an offline folder; paper the Borghese</td><td class="num">T−1</td></tr>
</table>
<div class="cl">
<div class="clh">CHANGE LOG</div>
<div class="clr"><b>2026.07</b> — First edition. All §1 figures resolved from the site's fact
database at export (14 July 2026). ETIAS logged as not yet required, launch signalled late
2026 — the line most likely to flip before the next issue. {V}</div>
</div>
<div class="fsfoot">Rome, Solved. · the book holds what is stable; this sheet holds what is
not. When the two disagree, the sheet is newer — and the official source is newer still.</div>
"""
