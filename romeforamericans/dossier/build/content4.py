# content4.py — pre-departure + the PHOTOS dict (Stage E: slots emitted to the chat brief;
# files land in img/ and wire in by slot id).
import os, base64
from content import E,O,S,V
BUILD = os.path.dirname(os.path.abspath(__file__))

BEFORE = f"""
<div class="eyebrow">CHAPTER TWO <span>· BEFORE YOU FLY</span></div>
<h1 class="t">The checklist, every line with a deadline</h1>
<div class="standfirst">Ten minutes at the kitchen table, weeks out, buys back whole
mornings in Rome. Work top to bottom; the order is the sell-out order.</div>
<table class="ck">
<tr><td class="box">□</td><td class="when">WITH THE FLIGHTS</td>
 <td>Book the four timed entries — Borghese, Colosseum, Vatican Museums, Pantheon — matched
 to days three, one, two, one of The Plan. {S} Add the Papal Audience request if Wednesday
 and the Pope align. {O}</td></tr>
<tr><td class="box">□</td><td class="when">WITH THE FLIGHTS</td>
 <td>Reserve the room inside the ring (Decision 01). Shoulder-season rates move fastest. {V}</td></tr>
<tr><td class="box">□</td><td class="when">T−30 DAYS</td>
 <td>Passport validity: three months beyond departure from the Schengen area, and blank
 pages. The 90-in-180-day visa-free clock applies. {O}</td></tr>
<tr><td class="box">□</td><td class="when">T−30 DAYS</td>
 <td>ETIAS status check — the EU's travel authorisation was not yet required at press time,
 with launch signalled for late 2026. Confirm before you fly; it flips once. {O} {V}</td></tr>
<tr><td class="box">□</td><td class="when">T−14 DAYS</td>
 <td>One no-foreign-fee card confirmed working; a second card as spare. Tell no bank apps
 any 'travel plans' theatrics unless yours requires it. {E}</td></tr>
<tr><td class="box">□</td><td class="when">T−7 DAYS</td>
 <td>Install the eSIM and test it — land connected, skip the airport SIM queue and the
 roaming bill. {S} Provider picks age fast; Field Sheet §3.</td></tr>
<tr><td class="box">□</td><td class="when">T−7 DAYS</td>
 <td>High-speed seats for the fourth day, if Naples or Pompeii won Decision 14 — fast-train
 fares float like airfares. {E}</td></tr>
<tr><td class="box">□</td><td class="when">T−3 DAYS</td>
 <td>Break in the shoes you are bringing. The sampietrini will audit them. {E}</td></tr>
<tr><td class="box">□</td><td class="when">T−1 DAY</td>
 <td>Screenshot every booking QR to a folder that works offline; paper the Borghese
 confirmation. Charge the battery pack. {S}</td></tr>
<tr><td class="box">□</td><td class="when">IN THE TAXI HOME</td>
 <td>Check the U.S. advisory once — Level 2 at press time, standard Western Europe — and
 the strike-or-event news for your dates. {O} {V}</td></tr>
</table>
<div class="note">Season packing in one line: spring and fall want layers, summer wants a
sun plan and a refillable bottle for the nasoni, winter wants rain cover — and every month
wants church-legal shoulders and knees somewhere in the bag. {E}</div>
"""

# ── PHOTOS — the Stage E contract. Slot ids are stable; files arrive as img/<id>.jpg ──
PHOTOS = {
 "A01": dict(chapter="Cover · the evidence strip", id="cover-rooftops",
   query="rome rooftops domes golden hour",
   argument="The thesis in one frame: the centre reads as a single, compact, walkable mass.",
   shot="Rome from above at golden hour — domes and rooftops receding, no single monument "
        "dominating, the density itself the subject. Horizontal, calm, warm."),
 "A02": dict(chapter="The Ground · the threshold", id="pantheon-oculus",
   query="pantheon interior oculus light",
   argument="Proximity's reward: the ancient world's best room, reached on foot between an "
            "espresso and a fountain.",
   shot="Inside the Pantheon: the oculus and its light shaft, coffered dome filling the "
        "frame, floor-level crowd minimal or silhouetted, no flash, no faces."),
 "A03": dict(chapter="Set Pieces · the Vatican queue", id="vatican-queue",
   query="st peters square queue colonnade",
   argument="Free to enter — and no ticket in existence skips this. Security is out-scheduled, "
            "never bought.",
   shot="The security line snaking across the cobbles toward the colonnade, shot from "
        "behind or above so no face reads; the LENGTH is the subject. Morning light."),
 "A04": dict(chapter="Set Pieces · the ancient core", id="colosseum-forum",
   query="colosseum roman forum view",
   argument="One 24-hour admission covers all of this — which is why it is one morning, not "
            "three visits.",
   shot="The Colosseum with Forum ruins in the same frame — from the Palatine or the "
        "Capitoline side — whole building legible, foreground crowd-free."),
 "A05": dict(chapter="Decision 08 · below the deck", id="hypogeum",
   query="colosseum hypogeum underground corridors",
   argument="What the upgrade buys: the machinery hall under the arena, not a better view of "
            "the same oval.",
   shot="Looking down into the exposed hypogeum — cells, corridors, lift shafts, ideally the "
        "reconstructed deck edge visible. Texture and depth over sky."),
 "A06": dict(chapter="Failure Modes · the meal", id="trattoria-lane",
   query="rome trattoria side street tables",
   argument="Ninety seconds from the monument is a different city and a different bill.",
   shot="A quiet Roman side street with a small trattoria — handwritten menu or chalkboard, "
        "no photo boards, no touts, few or no people. Late afternoon."),
 "A07": dict(chapter="Eating · the first protocol", id="espresso-banco",
   query="italian espresso bar counter cups",
   argument="Coffee is a standing ritual with its own protocol — get it right and the city "
            "treats you differently.",
   shot="An espresso on a marble or steel counter, saucer and spoon, machine or barista "
        "blurred behind; standing-height perspective, no faces."),
 "A08": dict(chapter="The Plan · day one, evening", id="trastevere-dusk",
   query="trastevere rome evening street lanterns",
   argument="Cross the river at dusk and the first real Roman dinner is already waiting.",
   shot="Trastevere's cobbled lanes at blue hour — ivy, shutters, warm lamplight, tables "
        "just filling. Mood over landmarks; no readable faces."),
 "A09": dict(chapter="The Fourth Day · the substitution", id="ostia-antica",
   query="ostia antica ruins pines",
   argument="Pompeii's thrill at a sixth of the travel — and quiet enough to hear your own "
            "steps.",
   shot="Ostia Antica: brick streets or theatre under umbrella pines, long shadows, empty "
        "of visitors. Scale and stillness."),
 "A10": dict(chapter="Closing · the bridge", id="ponte-santangelo-dusk",
   query="ponte sant angelo dusk castel",
   argument="The walk home is the last sight of the day — the book ends where the evenings do.",
   shot="Ponte Sant'Angelo at dusk — Bernini's angels in silhouette, Castel Sant'Angelo or "
        "St Peter's beyond, river catching the last light."),
}

# Focal points: object-fit:cover crops to the band aspect. Centre-default would cut the
# Pantheon oculus (upper frame) and behead the espresso (lower frame). Vertical % per slot.
POS = {
 "A01":"center 55%",   # skyline band, not sky
 "A02":"center 31%",   # the oculus sits high in the frame
 "A03":"center 62%",   # the queue is the argument; keep colonnade feet for context
 "A04":"center 55%",   # Colosseum + Forum in one band, sky trimmed
 "A05":"center 61%",   # the hypogeum, with the deck edge above it
 "A06":"center 73%",   # portrait: the tables are the argument
 "A07":"center 66%",   # portrait: machine base + cup + glass
 "A08":"center 73%",   # portrait: tables + cobbles
 "A09":"center 53%",   # pines above, ruins below
 "A10":"center 56%",   # dome + bridge + reflection
}

def _img64(slot):
    p=f"{BUILD}/img/{slot}.jpg"
    if not os.path.exists(p): return None
    with open(p,"rb") as fh:
        return "data:image/jpeg;base64,"+base64.b64encode(fh.read()).decode()

_photn=[0]
def photo(slot, cap, cls="band", pos=None):
    """Renders the slot if its file exists; contributes nothing otherwise (never a
    hatched placeholder in a paid product — Stage E gate)."""
    src=_img64(slot)
    if not src: return ""
    _photn[0]+=1
    pos = pos or POS.get(slot,"center")
    return (f'<figure class="photo {cls}"><img src="{src}" style="object-position:{pos}"/>'
            f'<figcaption><span class="fign">PL. {chr(64+_photn[0])}</span> &nbsp;{cap}'
            f'</figcaption></figure>')

CAPTIONS = {
 "A01":"THE CENTRE AS ONE MASS — EVERYTHING IN THIS FRAME IS ON FOOT",
 "A02":"THE PANTHEON'S OCULUS — REACHED BETWEEN AN ESPRESSO AND A FOUNTAIN, NOT BY ITINERARY",
 "A03":"FREE TO ENTER, IMPOSSIBLE TO SKIP — SECURITY IS OUT-SCHEDULED, NEVER BOUGHT",
 "A04":"ONE ADMISSION, ONE MORNING — THE 24-HOUR TICKET MAKES THIS A SINGLE OPERATION",
 "A05":"THE UPGRADE'S ACTUAL PRODUCT — THE MACHINERY HALL, NOT A BETTER SEAT",
 "A06":"NINETY SECONDS OFF THE PIAZZA — THE FILTER'S 'GO' SIGNALS, ALL VISIBLE FROM HERE",
 "A07":"AL BANCO — PAY FIRST, STAND, TWO MINUTES; THE TABLE IS A DIFFERENT PRODUCT",
 "A08":"ACROSS THE BRIDGE AT BLUE HOUR — THE EVENING THE BASE DECISION BUYS",
 "A09":"OSTIA ANTICA — MOST OF POMPEII'S THRILL AT A SIXTH OF THE TRAVEL",
 "A10":"THE WALK HOME IS THE LAST SIGHT OF THE DAY",
}
