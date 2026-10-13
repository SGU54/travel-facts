# -*- coding: utf-8 -*-
"""geo.py — real public coordinates for every place the corpus covers, and the
corpus-stated ferry/flight facts the figures are computed from.

Coordinates are public geographic facts (port/airport/island centroids); the
DURATIONS and FREQUENCIES below are quoted from the greeceforamericans corpus,
never invented. Each fact carries the slug it came from so a claim can be traced.
"""
import math

# --- real coordinates (lat, lon) — ports, airports, island centroids ---
PLACES = {
    "Athens":     (37.9838, 23.7275),
    "Piraeus":    (37.9470, 23.6376),   # the ferry hub
    "Santorini":  (36.3932, 25.4615),   # Thira
    "Mykonos":    (37.4467, 25.3289),
    "Naxos":      (37.1036, 25.3768),
    "Paros":      (37.0855, 25.1510),
    "Ios":        (36.7233, 25.2820),
    "Milos":      (36.7420, 24.4270),
    "Crete":      (35.3387, 25.1442),   # Heraklion
    "Delos":      (37.3928, 25.2718),
    "Delphi":     (38.4824, 22.5010),
    "Sounion":    (37.6503, 24.0245),
}

# airports (for the fly-vs-ferry figure) — real IATA points
AIRPORTS = {
    "ATH": (37.9364, 23.9445),  # Athens Eleftherios Venizelos
    "JTR": (36.3992, 25.4793),  # Santorini
    "JMK": (37.4351, 25.3481),  # Mykonos
    "HER": (35.3397, 25.1803),  # Heraklion, Crete
    "JNX": (37.0811, 25.3681),  # Naxos
    "PAS": (37.0203, 25.1131),  # Paros
}

def _km(a, b):
    (la1, lo1), (la2, lo2) = PLACES[a], PLACES[b]
    R = 6371.0088
    p = math.pi / 180
    dx = (lo2 - lo1) * p * math.cos((la1 + la2) * p / 2)
    dy = (la2 - la1) * p
    return R * math.hypot(dx, dy)

def sea_km(a, b):
    """Great-circle sea distance; the meltemi/fast-ferry argument uses relative
    distances, so no street factor — this is open water."""
    return _km(a, b)

# --- corpus-stated facts: (from_slug, value) ---------------------------------
# durations quoted from the corpus. Ranges kept as the corpus states them.
FERRY = {   # Piraeus -> island, hours (fast, slow) and flight minutes
    "Santorini": dict(fast=5.0, slow=8.0, fly=45,  src="santorini,itineraries"),
    "Mykonos":   dict(fast=3.0, slow=5.0, fly=40,  src="mykonos"),
    "Naxos":     dict(fast=4.0, slow=5.0, fly=None, src="naxos"),
    "Paros":     dict(fast=3.0, slow=4.0, fly=None, src="paros"),
    "Crete":     dict(fast=None, slow=9.0, fly=60,  src="crete,ferries-and-ports"),
}
# Piraeus <-> central Athens, metro
METRO_PIRAEUS = dict(lo=20, hi=30, src="athens,sample-ferry-routes")

# high-speed Cyclades hop, corpus: "around 2 to 3 hours"
HOP_FAST = dict(lo=2.0, hi=3.0, src="sample-ferry-routes")

# the wind fact the cover turns on
MELTEMI = dict(
    months="July–August",
    hits="north coasts hardest; fast catamarans most",
    effect="disrupts or cancels Cyclades crossings, especially fast catamarans",
    src="island-hopping,things-to-do,mykonos",
)

# pacing rule the book's spine rests on
PACE = dict(
    min_nights=3, max_islands="two or three in 10 days",
    rule="at least three nights per island; no more than two or three islands",
    src="island-hopping,things-to-do",
)

if __name__ == "__main__":
    for a in ("Santorini", "Mykonos", "Naxos", "Paros", "Crete", "Ios"):
        print(f"  Piraeus->{a:10} {sea_km('Piraeus', a):6.1f} km sea")
    print(f"  Santorini<->Mykonos {sea_km('Santorini','Mykonos'):.1f} km")
    print(f"  Paros<->Naxos       {sea_km('Paros','Naxos'):.1f} km")
