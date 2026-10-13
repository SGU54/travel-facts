# content2.py — terrain, neighborhoods, failure modes.
from content import E,O,S,V

GROUND_1 = f"""
<div class="eyebrow">CHAPTER ONE <span>· THE GROUND</span></div>
<h1 class="t">The city is smaller than it lets on</h1>
<div class="standfirst">One fact reorganises the trip: nearly everything a first visit wants
sits inside a core you can cross on foot in about thirty minutes — and the metro, by design,
cannot go there.</div>
<p class="b cap1">Rome arrives in the imagination at imperial scale, and the map obliges —
seven hills, a river, twenty-eight centuries of sprawl. Then you stand at the Pantheon and
the scale collapses. Piazza Navona is five minutes away. The Trevi Fountain, eight. Campo
de' Fiori, five in the other direction. The Colosseum, a twenty-minute walk past the edge
of the Forum; the Vatican, half an hour across the river; Trastevere, less. {E} The
classic-sights core measures roughly two kilometres by one and a half — a ring one
kilometre around the Pantheon captures most of what you flew for.</p>
<p class="b">The reason is buried, literally. The metro skirts the historic centre because
you cannot tunnel freely under two thousand years of ruins, and the surface lanes are too
tangled and too protected for cars to matter. {E} So the fastest vehicle in central Rome is
you — and the space between the sights, which a train would erase, is where the city keeps
its churches with the Caravaggios, its workshops, its fountains, its unplanned hours. The
walking is the sightseeing.</p>
<p class="b">Cross the Pantheon's threshold once and the thesis becomes physical: out of
the noon glare, through bronze doors, into a drum of cool shadow where a disc of sky hangs
in the dome's open eye — the best-preserved room of the ancient world, reached on foot
between an espresso and a fountain. {E} No itinerary produces that. Proximity does.</p>
{{PHOTO_A02}}
"""

GROUND_2 = f"""
<div class="eyebrow">THE GROUND <span>· THE RING</span></div>
<h1 class="t">One ring to plan inside</h1>
<div class="standfirst">Sleep inside it and the trip runs itself; sleep outside it and every
evening begins with a commute. The ring decides Decision 01 before you do.</div>
{{FIG_RING}}
<p class="b">The published walk-times hold up under arithmetic. Computed from raw
coordinates at an unhurried 4.5 km/h with a street factor for Rome's non-Euclidean lanes,
the hops come out the same: Monti to the Colosseum in nine minutes, Termini to the Pantheon
in thirty-four. {E} Those two numbers are Decision 01 in miniature — one base puts the
ancient city at the end of your street, the other puts a half-hour march before dinner.</p>
<p class="b">Two practical corollaries. First: shoes are equipment here, not fashion — the
sampietrini cobbles punish thin soles and fresh sneakers alike, and the free nasoni
fountains along the way are the hydration plan. {E} Second: when a hop is fifteen minutes on
foot, a taxi saves nothing once you have hailed, ridden and been dropped at the edge of the
pedestrian zone. Inside the ring, feet win on time, not just on charm.</p>
"""

GROUND_3 = f"""
<div class="eyebrow">THE GROUND <span>· TRANSIT REALITY</span></div>
<h1 class="t">Why the obvious tool doesn't help</h1>
<div class="standfirst">Every other capital trains you to reach for the metro map. Rome's
has a hole in the middle — and the hole is where you are going.</div>
{{FIG_TRANSIT}}
<p class="b">Lines A and B are capable workhorses — A delivers the Vatican flank at
Ottaviano and the Spanish Steps at Spagna; B touches the Colosseum — but between them lies
the entire historic centre, station-free. {E} Ride to the rim when it serves you: Ottaviano
for the Museums on a tired morning, Colosseo with luggage. Then surrender the map. Buses
and trams fill some gaps — the 40 and 64 cross toward the Vatican, a tram climbs out of
Trastevere — at the price of the densest pickpocket traffic in the city. {S} Decision 06
turns this picture into a rule; Decision 13 covers your pockets.</p>
"""

# ── neighborhoods — six assessments on identical criteria ────────────────────
HOODS_TXT=[
 ("centro","Centro Storico","0′ — you are the centre","postcards at the door",
  "The walk-everywhere choice: Pantheon, Navona and the Trevi within a stroll, the river "
  "and Trastevere just beyond. You step out of the lobby into the Rome you came for and "
  "almost never touch transit. The price is the price — rooms run small, the most central "
  "lanes run loud at night, and you are paying for latitude and longitude.",
  "First visit, budget willing: this is the answer."),
 ("monti","Monti","14′ · Colosseum at 9′","wine bars, workshop lanes",
  "Tucked between the Colosseum and the station, Rome's oldest rione balances the map: "
  "central enough to walk to the Forum, local enough to have its own evening. Wine bars, "
  "boutiques, narrow lanes, lower rates than the tourist core and more personality per "
  "block. The ancient city is your neighbour; the Baroque one is a pleasant walk.",
  "The value play — central and characterful for less."),
 ("trastevere","Trastevere","20′ across the bridge","the city's best",
  "Ivy, cobbles, trattoria terraces, and the slow evening tide from aperitivo to dinner to "
  "gelato — the quarter everyone falls for, and a fine base if you accept the geometry: "
  "a bridge stands between you and most of your mornings. After dark you are already where "
  "the city wants to be; before ten you are commuting, pleasantly, on foot.",
  "Choose it when evenings outrank mornings."),
 ("prati","Prati · Borgo","20′ · St Peter's at 14′","calm, early, elegant",
  "Orderly streets, wide pavements, the Vatican at your doorstep and the centre a bridge "
  "away. Quieter by ten than Trastevere is by midnight — which is either the flaw or the "
  "feature. Good hotels at fairer rates than the core, painless metro access at Ottaviano, "
  "and the best possible start to a Museums morning.",
  "For calm sleepers with a Vatican-heavy plan."),
 ("termini","Termini · Esquilino","34′ — or a metro hop","thin, transactional",
  "The station quarter holds the city's largest stock of beds at its lowest prices, every "
  "rail line and both metro lines. It is not dangerous in any serious sense — gritty and "
  "unromantic is the fair charge, with pickpocket awareness required around the station "
  "itself. {S} What it lacks is the point of Rome: you will commute to your own holiday.",
  "Only for dawn trains, late landings, or hard budgets — eyes open."),
 ("testaccio","Testaccio","30′ · a tram ride out","Rome's own table",
  "The food quarter: the covered market, the Roman kitchen canon done without ceremony, "
  "streets where the tourists thin and the accents don't. Light on monuments — Ostiense's "
  "street art and the pyramid are the local sights — and heavier than anywhere on the "
  "reason people return. A base for second visits and first-visit eaters.",
  "Eat where Rome eats; commute to the marble."),
]

def hood_block(key,name,walk,eve,body,call, svg):
    return (f'<div class="na"><div class="loc">{svg}</div><div class="nb"><h3>{name}</h3>'
            f'<div class="crit">WALK <b>·</b> {walk} &nbsp;&nbsp; EVENINGS <b>·</b> {eve}</div>'
            f'<p>{body}</p><div class="call">{call}</div></div></div>')

# ── failure modes — twenty, ordered by consequence ───────────────────────────
FM = [
 ("YOU LOSE THE MORNING",[
  ("No Borghese reservation","Mandatory booking, no walk-ins, small rooms. The door does not negotiate. "
   +E+" Fix: book with the flights (Decision 04)."),
  ("Walking to the Vatican without a slot","In season the ticket line is the longest wait on the property, and slots sell out. "
   +S+" Fix: timed entry, arrive T−25 for security."),
  ("Buying the Colosseum at the door","Same-day supply is scalper territory; the men with laminated badges sell markup. "
   +S+" Fix: the one official seller, weeks out."),
  ("A Monday at the closed doors","Borghese, Castel Sant'Angelo and Ostia Antica all sit dark on Mondays. "
   +O+" Fix: the week grid, Timing chapter."),
  ("Wednesday at the basilica","The Papal Audience owns the square until early afternoon; the Museums run regardless. "
   +O+" Fix: flip the day's order, or come for the Audience."),
 ]),
 ("YOU LOSE MONEY",[
  ("Answering 'dollars' at the reader","The conversion is a worse rate in a courtesy costume, charged every time. "
   +E+" Fix: euros, always (Decision 12)."),
  ("Riding on an unvalidated ticket","A paper ticket unstamped is a fine in waiting, and inspectors do not debate. "
   +O+" Fix: validate, or tap contactless instead."),
  ("Taking the arrivals-hall 'taxi'","The soliciting man is the only unpriced option at the airport. "
   +S+" Fix: the rank outside, the flat fare, or the train (Decision 05)."),
  ("Sleeping cheap at Termini to save a little","The nightly saving returns to the transit system, with interest paid in evenings. "
   +S+" Fix: run Decision 01 with your own numbers."),
  ("Buying a pass on vibes","'Sounds comprehensive' is the product. The Vatican isn't even in it. "
   +E+" Fix: the break-even table, Decision 07."),
 ]),
 ("YOU LOSE THE MEAL",[
  ("Dining on the famous square","Front-row tables price the view into every plate; the kitchen knows you won't return. "
   +S+" Fix: the ninety-second rule (Decision 10)."),
  ("Trusting a photo menu","Lamination is a confession. Five flags and a host outside complete it. "
   +S+" Fix: posted prices, a coperto, Romans in the room."),
  ("Dinner at six","You will dine alone with the staff in a room built for eight o'clock. "
   +E+" Fix: aperitivo is the bridge (Decision 11)."),
  ("Ordering the canon 'improved'","Cream in a carbonara is the kitchen telling you who it cooks for. "
   +E+" Fix: plain classics, or a different room."),
 ]),
 ("YOU LOSE THE DAY'S SHAPE",[
  ("The Forum at noon in July","Unshaded stone at 35°C flattens the afternoon and the visitor. "
   +E+" Fix: dawn slots, siesta, evening returns — the summer protocol."),
  ("The one-day death march","Ten sights scheduled, six seen, none felt. "
   +E+" Fix: Decision 02 — the third day is where Rome happens."),
  ("Florence squeezed into a Tuesday","Three-plus hours of rail wrapped around a sprint past the David. "
   +S+" Fix: Ostia or Orvieto (Decision 14); give Florence its own nights."),
 ]),
 ("YOU LOSE YOUR FOOTING",[
  ("Fresh sneakers on the sampietrini","The cobbles are charming and orthopedic only in memory. "
   +E+" Fix: broken-in soles; the nasoni handle the water."),
  ("The open bag on the 64","The Vatican bus is the city's densest theft corridor; crowds are the tool. "
   +S+" Fix: zipped, worn front, phone away in crushes (Decision 13)."),
  ("Stopping for the bracelet","Petitions, roses, friendship knots — every gift on the street is an invoice. "
   +S+" Fix: keep walking; refusal is not rudeness."),
 ]),
]

def failure_pages():
    pages=[]; cur=[]; count=0
    for group,(items) in [(g,i) for g,i in FM]:
        block=f'<div class="cons">{group}</div>'
        for h,body in items:
            count+=1
            block+=(f'<div class="fm"><h4><span class="x">{count:02d}</span> &nbsp;{h}</h4>'
                    f'<p>{body}</p></div>')
        cur.append(block)
    # split 2 / 2 / 1 groups across three pages
    pages.append(f"""<div class="eyebrow">CHAPTER ELEVEN <span>· FAILURE MODES</span></div>
<h1 class="t">Twenty ways it goes wrong</h1>
<div class="standfirst">Ordered by what they cost you — the one arrangement a website of
articles can never hold. Read once before you fly; skim again on the plane.</div>
{cur[0]}{''}""")
    pages.append(f"""<div class="eyebrow">FAILURE MODES <span>· CONTINUED</span></div>
{cur[1]}{cur[2]}{{PHOTO_A06}}""")
    pages.append(f"""<div class="eyebrow">FAILURE MODES <span>· CONTINUED</span></div>
{cur[3]}{cur[4]}
<div class="note">Every mode above traces to a decision page — the failure is always the
same one: arriving with American defaults where Rome has its own. {E}</div>""")
    return pages
