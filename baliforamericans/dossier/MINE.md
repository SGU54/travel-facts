# Bali — Stage A / A2 / A3 record · 2026-10-15

## Stage A — the corpus

77 published articles, 85,873 words (corpus.json, exported 2026-10-15 from schema `bali`
via PostgREST, status=published). Yield model: 77 × 0.5 ≈ **38 pages**; the decisions are
deepened (250–350w of body each) and the figure count raised rather than the page count
padded. Guide-spans stripped before every tally (45 spans, each with its sentence).

Category inventory (words): health-and-safety 10,142 · visas-and-documents 8,959 ·
flights-and-arrival 6,865 · when-to-go 6,616 · boats-and-ferries 4,538 · money-and-costs
4,474 · by-trip-length 4,331 · choosing-your-base 3,466 · drivers-and-ride-apps 3,197 ·
scooters 3,106 · balinese-food 2,314 · by-trip-type 2,300 · phones-and-internet 2,254 ·
nusa-islands 2,252 · north-and-east-bali 2,163 · culture-and-etiquette 2,148 · singletons
1,056–1,211 each (beach clubs, temples, volcano, Ubud, areas, Seminyak strip, yoga, surf,
Sanur, diving, waterfalls, Uluwatu, getting around, villas, beyond-bali).

By swamp (words): base-split 16,825 · boat-day-buffer 8,900 · traffic-time 8,789 ·
health-chain 7,958 · long-haul-arrival 6,837 · wet-dry-season 4,483 · entry-stack 4,360 ·
scooter-liability 4,288 · money-leak 3,398 · holiday-collision 3,245 · untagged 16,790.

Edge tally (raw cues): MONEY 673 · EXPERIENCE 368 · BREAKAGE 191 · EXTRACTION 11.
Read: the money cues are tax lines, fee words and rupiah figures, not losses — the corpus
refuses to print a daily budget and quotes almost no price. The high-stakes material is
BREAKAGE (a boat that does not run the day before the flight, a scooter crash with a
car-only licence, a narcotic-class prescription seized, a Nyepi arrival, an overstay at a
million rupiah a day) and the **night economy** — where the nights go on an island whose
miles are short and whose hours are long. The cover leads with *time and order*, not savings.

Synthesis check (audit-synthesis.py, the organising fact's four parts):
jet lag / airport miles / boat crossings / base count → in 16/26/29/10 of 77 articles,
joined in **3** → scatter 0.26, pre-connection 0.04, **HEADROOM 4.5, STRONG**.

## Stage A2 — the shape

**Shape:** a region (one island plus its satellites), hub-and-spoke from a single airport
on a neck of land — the base you pick decides what the trip contains. Not a city (no walk
thesis), not a corridor (no direction), not an archipelago (one boat, not a network).
**Organising fact:** Bali is eighty-nine miles wide and its distances are counted in
hours, not miles; three fixed points — the hour the long flight lands, the sea under the
one boat, and the drive to the airport on the last morning — decide where the nights go
and in what order, and the corpus never prints a drive time because none would be true.
**What this audience gets wrong:** books the trip as "a week" and lands with five good
days; chooses a villa by its photographs and commutes; rents a scooter on a car-only
licence and finds the insurer reads the policy after the crash; puts the island nights at
the end so the boat sits against the flight home; assumes July's dry weather means a calm
strait; pays the visa and thinks the levy and the arrival card are the same thing; packs
an ADHD prescription that Indonesia classes as a narcotic.
**Cover device:** the island drawn from coordinates with the airport at its neck, each
base placed at its real position, and the three pinned points marked — arrival, the sea,
the airport run — as a timeline under it. Unclonable without the night-placement analysis.
**Standard chapters that don't apply:** the walk-time terrain chapter and the transit
chapter. Replaced by THE GROUND (miles vs hours, from the airport outward) and a
BASE-ORDER decision; the "legs" chapter becomes the day as a spoke from a base.

## Decisions (shortlist, with veins)

| # | decision | vein | words |
|---|---|---|---|
| 01 | Nights: how many do you really have, and how many bases do they buy? | how-many-days, one-week, ten-days, two-weeks, one-base-or-two, jet lag | ~6,500 STRONG |
| 02 | Order: which base first, which last, and where does the boat go? (FREE HOOK) | one-week, two-weeks, honeymoon, departure day, jet lag, traffic, boats | ~7,000 STRONG |
| 03 | Month: which month, and which coast does it point to? | best-time, shoulder, rainy, surfing, holidays | ~6,600 STRONG |
| 04 | The entry stack: what does it commit you to, and in what order? | visa, VOA vs e-VOA, levy, arrival card, passport, extension, customs, medication | ~9,000 STRONG |
| 05 | Ride, pillion, or driver — the licence and the insurer | scooter, IDP, scooter-vs-driver, insurance, Grab, rules | ~6,500 STRONG |
| 06 | The island leg: day trip, nights, the Gilis, or none — and where in the trip? | Lembongan, Penida, Gili, fast boats, cancellations, Gili vs flight, manta, ten-days | ~8,900 STRONG |
| 07 | The day: how many stops, from which base? | traffic, driver, getting around, temples, Batur, waterfalls | ~8,800 STRONG |
| 08 | Your dates touch March. Through Nyepi, or around it? | Nyepi, holidays, Galungan + mentions in 20 articles | ~3,200 (scatter 20) VIABLE-by-scatter |
| 09 | The flight: which hub, one ticket or two, and what hour do you land? | flights, layover, through-ticket, arriving, jet lag | ~6,800 STRONG |
| 10 | The health chain: what breaks it — the medicine bag, the deposit, the policy? | medication, Bali belly, hospitals, insurance, vaccines, water, dengue, arak, drug laws | ~10,000 STRONG |
| 11 | Money: which card, how much cash, and where the small percentages land | money, tipping, QR, is-bali-expensive, customs cash, beach clubs | ~5,600 VIABLE |

Refused (THIN or not a decision): phones and SIMs (a rule, folded into Before You Fly);
beach clubs as a decision (a checklist, folded into the set pieces); yoga retreats (a
checklist); Balinese food as a decision (experience, no losable call — the eating chapter);
temple dress (a rule, folded into the set pieces and the pocket card); the far west (the
corpus has one paragraph).

## Stage A3 — the name (★ user confirms)

Pattern: destination + promise of resolution. Proposed:
1. **Bali, in Its Own Time.** — the site's live thesis ("Bali keeps its own time") carried
   into the book: hours not miles, the sea's clock, a date line, a day the island stops (default)
2. Bali, Night by Night.
3. Bali, Base by Base.

Thesis line: *Ninety miles wide, measured in hours. Sixteen hours from home, one boat
that answers to the sea, and a day the island stops. Where the nights go, and in what order.*

Hooks by swamp id (raw, accurate first) are emitted in DELIVERABLES.md after Stage C.

## Image library

767 files on the volume under `content/batch-NN/{images,cand}/`; 154 are the article
images actually published (10 per batch), all landscape ≥1200px. Each candidate carries its
Unsplash description in `cand/manifest.json`, which is the fact layer for what a photo
shows; the published images were matched back to their candidate by pixel signature
(`_sheets/used-desc.json`). Contact sheets `_sheets/used-00..07`. Eleven of the published
images are not Bali (Lofoten, Lisbon, Frankfurt, JFK, the Azores, Sri Lanka, Bangka,
Banyuwangi, a Malay nasi lemak); none is used as a plate captioned as Bali.
