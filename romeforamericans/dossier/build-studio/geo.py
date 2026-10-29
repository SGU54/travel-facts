"""geo.py — real public coordinates for Rome, and the distance/walk-time math.
Every figure computes from THESE; if the geography contradicts the thesis, the thesis is wrong.
Coordinates are public facts (lat, lon). Walk factor 1.30 (street vs crow), 4.5 km/h.
"""
import math

# --- landmarks (public coordinates) ---
LM = {
    "Pantheon":        (41.8986, 12.4769),
    "Trevi":           (41.9009, 12.4833),
    "Spanish Steps":   (41.9060, 12.4828),
    "Piazza Navona":   (41.8992, 12.4731),
    "Campo de' Fiori": (41.8955, 12.4723),
    "Colosseum":       (41.8902, 12.4922),
    "Roman Forum":     (41.8925, 12.4853),
    "Palatine":        (41.8891, 12.4876),
    "St Peter's":      (41.9022, 12.4539),
    "Vatican Museums": (41.9065, 12.4536),
    "Trastevere":      (41.8890, 12.4700),   # Piazza S. Maria in Trastevere
    "Termini":         (41.9010, 12.5010),   # Roma Termini
    "Borghese":        (41.9142, 12.4923),   # Galleria Borghese
    "Castel S.Angelo": (41.9031, 12.4663),
    "Piazza Venezia":  (41.8959, 12.4828),   # the centroid pin of the core
}

# --- neighborhood/base anchors (public coordinates) ---
HOODS = {
    "Centro Storico":  (41.8992, 12.4731),   # ~Navona
    "Monti":           (41.8946, 12.4917),
    "Trastevere":      (41.8890, 12.4700),
    "Prati":           (41.9080, 12.4620),
    "Termini":         (41.9010, 12.5010),
    "Testaccio":       (41.8760, 12.4750),
}

R_EARTH = 6371.0
STREET = 1.30
WALK_KMH = 4.5

def _ll(name):
    if name in LM:  return LM[name]
    if name in HOODS: return HOODS[name]
    raise KeyError(name)

def km(a, b):
    (la1, lo1), (la2, lo2) = _ll(a), _ll(b)
    p = math.pi / 180
    dx = (lo2 - lo1) * p * math.cos((la1 + la2) * p / 2)
    dy = (la2 - la1) * p
    return R_EARTH * math.hypot(dx, dy) * STREET

def mins(a, b):
    return round(km(a, b) / WALK_KMH * 60)

# --- core extent: bounding the classic-sights cluster ---
CORE_PTS = ["Pantheon","Trevi","Spanish Steps","Piazza Navona","Campo de' Fiori",
            "Colosseum","Roman Forum","Palatine","St Peter's","Trastevere","Piazza Venezia"]

def core_extent():
    las = [LM[p][0] for p in CORE_PTS]
    los = [LM[p][1] for p in CORE_PTS]
    la0,la1 = min(las),max(las); lo0,lo1 = min(los),max(los)
    p = math.pi/180
    w = R_EARTH*(lo1-lo0)*p*math.cos((la0+la1)*p/2)*STREET
    h = R_EARTH*(la1-la0)*p*STREET
    return dict(w_km=w, h_km=h, la0=la0, la1=la1, lo0=lo0, lo1=lo1)

if __name__ == "__main__":
    # validate the thesis against the geometry
    ext = core_extent()
    print(f"core bounding box: {ext['w_km']:.2f} x {ext['h_km']:.2f} km")
    print(f"end-to-end diagonal (Vatican->Colosseum): {km('St Peters' if False else 'Vatican Museums','Colosseum'):.2f} km, {mins('Vatican Museums','Colosseum')} min")
    print("--- key hops (should match the article's 5-30 min claims) ---")
    for a,b in [("Pantheon","Trevi"),("Trevi","Spanish Steps"),("Pantheon","Piazza Navona"),
                ("Piazza Navona","Campo de' Fiori"),("Pantheon","Colosseum"),
                ("Piazza Venezia","St Peter's"),("Pantheon","Trastevere")]:
        print(f"  {a:16}-> {b:16} {km(a,b):.2f} km  {mins(a,b):2d} min")
    print("--- how far the metro/Termini base sits OUTSIDE the walk core ---")
    for b in ["Termini"]:
        for t in ["Pantheon","Piazza Navona","Colosseum"]:
            print(f"  {b} -> {t:16} {mins(b,t):2d} min walk")
    print("--- neighborhood base -> centroid (Piazza Venezia) ---")
    for h in HOODS:
        print(f"  {h:16} {mins(h,'Piazza Venezia'):2d} min to core centre")
