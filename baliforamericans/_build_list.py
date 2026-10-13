# Generates article-list.json + predictions.json for baliforamericans (Stage 1 / 1c).
# Re-run after editing ROWS; predictions.json rows are append-only once writing starts.
import json, datetime
TODAY = "2026-10-13"
SWAMPS = [
 ("base-split","Where to base, and how to split the nights","Bali drives far bigger than it looks on a map; the base you pick decides what is realistically reachable each day."),
 ("traffic-time","Planning days around south Bali traffic","Distances are short and drive times are not; an over-packed day or a late airport run is the classic first-timer failure."),
 ("wet-dry-season","Which season for which Bali","Rain, surf coasts, crowds and prices all move with the calendar, and they do not all point at the same month."),
 ("scooter-liability","Scooter, driver, or both","The cheap way around carries a licence and insurance chain that most renters only discover after a crash."),
 ("boat-day-buffer","Nusa and Gili boats, and what sits next to them","Fast boats depend on sea conditions; where the island leg falls relative to the flight home is the decision."),
 ("holiday-collision","Trip dates against the Balinese calendar","Some days close the island outright and others close roads and fill hotels; they move every year."),
 ("entry-stack","The pre-flight paperwork stack","Visa, levy, arrival form and passport rules are separate systems with separate sites, and each is easy to miss."),
 ("long-haul-arrival","Getting there from the US, and the first 48 hours","There is a long connection either way; the routing, ticket type and first-night base decide how much of the trip is lost."),
 ("health-chain","Stomach, medication, clinics, insurance","Each piece is manageable alone; what a traveler needs is how they connect when something goes wrong."),
 ("money-leak","Cash, cards and where the money leaks","ATMs, changers, surcharges and tax-plus-service each take a little; together they set the real budget."),
]
S="STRUCTURAL"; P="PRODUCE"; I="INVESTIGATE"; R="REJECT"
# (slug, title, category_slug, swamp, handoff, verdict, reason, rules_fired, analog, role)
ROWS = [
# ── Plan · visas & documents
("do-americans-need-a-visa-for-bali","Do Americans Need a Visa for Bali?","visas-and-documents","entry-stack","turn",S,"Spine role: entry. R1 fires on 'visa' (government-owned SERP; fleet analog morocco-visa-for-americans 176 imp @ 67.5). Written because the site makes no sense without it.",["R1:visa"],None,"entry"),
("bali-visa-on-arrival-vs-e-voa","Visa on Arrival vs. e-VOA for Bali: Which to Get","visas-and-documents","entry-stack","seed",I,"Options comparison (the R2 shape that wins), but the immigration portal is the canonical owner. One SERP look: does the portal answer 'which one', or only sell it?",["R3"],None,None),
("bali-tourist-levy-explained","The Bali Tourist Levy, Explained","visas-and-documents","entry-stack","seed",P,"Survives R1/R2. Direct fleet analog ranks: barcelona-tourist-tax-explained 67 imp @ 6.7.",[],"barcelona-tourist-tax-explained 67 imp @ 6.7",None),
("indonesia-arrival-declaration-form","Indonesia's Arrival Declaration Form: What to Fill In Before You Land","visas-and-documents","entry-stack","seed",I,"Government form = canonical owner, and the closest fleet analog LOST (thailand-digital-arrival-card-tdac 168 imp @ 56.9). Leaning STRUCTURAL unless the SERP look shows the official page does not explain the form.",["R3"],"thailand-digital-arrival-card-tdac 168 imp @ 56.9 (lost)",None),
("extending-a-bali-visa-on-arrival","Extending a Bali Visa on Arrival: How It Works","visas-and-documents","entry-stack","none",I,"Procedure, not place; volume unknown and immigration is the canonical owner.",["R3"],None,None),
("passport-validity-rules-for-indonesia","Passport Validity and Blank-Page Rules for Indonesia","visas-and-documents","entry-stack","seed",I,"Survives R1/R2; volume unknown. Airlines enforce this at US check-in, so the stake is real.",[],None,None),
("bringing-medication-into-bali","Bringing Medication into Bali and Indonesia","visas-and-documents","health-chain","seed",P,"Strongest repeatable shape in the fleet: bringing-medication-into-turkey 420 imp @ 8.1, bringing-medication-into-spain 169 imp @ 8.1.",[],"bringing-medication-into-turkey 420 imp @ 8.1; -into-spain 169 @ 8.1",None),
("bali-customs-alcohol-and-vape-rules","What You Can Bring into Bali: Customs, Alcohol and Vapes","visas-and-documents","none","none",P,"Survives R1/R2. Fleet analog: bringing-spanish-purchases-into-the-us 71 imp @ 7.8.",[],"bringing-spanish-purchases-into-the-us 71 imp @ 7.8",None),
# ── Plan · flights & arrival
("flights-from-the-us-to-bali","Flights from the US to Bali: Routes, Layovers and Realistic Travel Time","flights-and-arrival","long-haul-arrival","turn",P,"Survives R1/R2. Analogs rank in two of three cases: flights-to-barcelona-from-us 77 imp @ 8.7, flights-usa-to-turkey 83 @ 17.5 (flights-from-us-to-greece lost at 35.9).",[],"flights-to-barcelona-from-us 77 imp @ 8.7; flights-usa-to-turkey 83 @ 17.5",None),
("choosing-a-layover-city-for-bali","Choosing a Layover City for Bali from the US","flights-and-arrival","long-haul-arrival","seed",I,"Compares options for one journey (wins) but names cities (R2 risk). Volume unknown.",[],None,None),
("through-ticket-vs-separate-tickets-to-bali","Through Ticket vs. Separate Tickets to Bali","flights-and-arrival","long-haul-arrival","turn",I,"Shape ranks everywhere it was tried but on small queries: turkey 36 imp @ 7.6, spain 30 @ 7.2 — below the 50 floor.",[],"turkey-through-ticket-vs-separate-ticket 36 imp @ 7.6",None),
("arriving-at-bali-airport","Arriving at Bali Airport: Immigration to Curb, Step by Step","flights-and-arrival","long-haul-arrival","seed",P,"Survives R1/R2. Fleet analog: arriving-in-athens-guide 63 imp @ 8.0.",[],"arriving-in-athens-guide 63 imp @ 8.0",None),
("bali-airport-transfers","Bali Airport Transfers: Ride App, Taxi Counter or Pre-Booked Driver","flights-and-arrival","traffic-time","seed",I,"Options comparison, but adjacent to R1 'airport to city' (leonardo-express-fiumicino-trains 168 imp @ 52.6 lost).",["R1-adjacent:airport to city"],None,None),
("jet-lag-on-a-us-to-bali-trip","Jet Lag on a US-to-Bali Trip: A First-48-Hours Plan","flights-and-arrival","long-haul-arrival","seed",I,"Survives R1/R2; no fleet analog, volume unknown.",[],None,None),
("bali-departure-day-how-early-to-leave","Departure Day in Bali: How Early to Leave for the Airport","flights-and-arrival","traffic-time","turn",I,"'How early' shape ranked once on a small query (how-early-arrive-vatican 39 imp @ 9.1).",[],"how-early-arrive-vatican 39 imp @ 9.1",None),
# ── Plan · money
("money-in-bali-cash-cards-atms","Money in Bali: Cash, Cards and ATMs","money-and-costs","money-leak","turn",S,"Spine role: money. Broad query, written for the site, not for rank.",[],None,"money"),
("bali-atm-fees-real-cost","ATM Fees in Bali: What a Withdrawal Really Costs","money-and-costs","money-leak","seed",I,"The gate's own split case: turkey-atm-withdrawal-real-cost ranks 8 on a small query, atm-fees-thailand-real-cost sits at 52 on a bigger one.",[],"turkey pos 8 (15 imp) vs thailand pos 52 (104 imp)",None),
("bali-money-changer-short-change","Money Changers in Bali: How the Short-Change Works","money-and-costs","money-leak","seed",I,"Survives R1/R2; volume unknown.",[],None,None),
("is-bali-expensive","Is Bali Expensive? What Americans Actually Spend","money-and-costs","money-leak","seed",P,"Survives R1/R2. Fleet analog: is-turkey-expensive 102 imp @ 16.2; greece-trip-cost-from-us 30 @ 6.7.",[],"is-turkey-expensive 102 imp @ 16.2",None),
("tipping-in-bali","Tipping in Bali: Service Charge, Tax and When to Add More","money-and-costs","none","none",P,"Survives R1/R2. Fleet analog: money-cards-tipping-barcelona 53 imp @ 8.7.",[],"money-cards-tipping-barcelona 53 imp @ 8.7",None),
("paying-by-qr-code-in-bali","Paying by QR Code in Bali: Can Foreign Cards and Apps Use It?","money-and-costs","money-leak","none",I,"Shape ranks (morocco-mobile-payments 40 imp @ 9.5) but under the 50 floor.",[],"morocco-mobile-payments 40 imp @ 9.5",None),
# ── Plan · when to go
("best-time-to-visit-bali","Best Time to Visit Bali","when-to-go","wet-dry-season","turn",S,"Spine role: season. R1 fires on 'best' (best-time-to-visit-thailand 165 imp @ 83.2).",["R1:best"],None,"season"),
("bali-shoulder-season","Bali's Shoulder Season: When It Is and What You Trade","when-to-go","wet-dry-season","turn",P,"Survives R1/R2. Fleet analog: greece-shoulder-season 180 imp @ 9.2.",[],"greece-shoulder-season 180 imp @ 9.2",None),
("bali-rainy-season-what-its-like","Bali in Rainy Season: What It Is Actually Like","when-to-go","wet-dry-season","turn",I,"Survives R1/R2; volume unknown.",[],None,None),
("bali-in-july-and-august","Bali in July and August: Crowds, Prices and How Far Ahead to Book","when-to-go","wet-dry-season","seed",I,"Survives R1/R2; volume unknown.",[],None,None),
("nyepi-bali-day-of-silence","Nyepi in Bali: What the Day of Silence Shuts Down","when-to-go","holiday-collision","turn",P,"The fleet's single biggest winner is this shape: bayram-holidays-turkey-explained 479 imp @ 13.5. Note 479 is above the 300 ceiling the fleet has otherwise never cracked.",[],"bayram-holidays-turkey-explained 479 imp @ 13.5",None),
("galungan-and-kuningan-explained","Galungan and Kuningan Explained for Visitors","when-to-go","holiday-collision","seed",P,"Same local-holiday shape as the Bayram winner (479 imp @ 13.5).",[],"bayram-holidays-turkey-explained 479 imp @ 13.5",None),
("bali-public-holidays-what-closes","Public Holidays in Bali: What Closes and What Gets Crowded","when-to-go","holiday-collision","seed",I,"Shape ranks (turkish-public-holidays-what-closes 42 imp @ 10.2) but under the 50 floor.",[],"turkish-public-holidays-what-closes 42 imp @ 10.2",None),
# ── Plan · health & safety
("is-bali-safe","Is Bali Safe for American Travelers?","health-and-safety","health-chain","turn",S,"Spine role: safety. R1 fires on 'is X safe' (is-turkey-safe 220 imp @ 59.4, is-thailand-safe 159 @ 56.2).",["R1:is X safe"],None,"safety"),
("bali-belly","Bali Belly: Prevention, Treatment and When to See a Doctor","health-and-safety","health-chain","turn",I,"Almost certainly above the 300 ceiling and contested by health publishers. Needs a SERP look; may end up STRUCTURAL.",[],None,None),
("bali-hospitals-and-clinics-billing","Hospitals and Clinics in Bali: What to Expect and How Billing Works","health-and-safety","health-chain","turn",I,"Shape ranks in both tries but small: turkey-hospital-billing 41 imp @ 8.0, spain-hospital-billing 39 @ 5.2.",[],"turkey-hospital-billing-what-to-expect 41 imp @ 8.0",None),
("travel-insurance-for-bali-fine-print","Travel Insurance for Bali: The Scooter and Evacuation Fine Print","health-and-safety","scooter-liability","turn",I,"Insurance SERPs are affiliate-heavy; the scooter-exclusion angle is specific. Volume unknown.",[],None,None),
("vaccines-and-animal-bites-in-bali","Vaccines for Bali, and What to Do After a Dog or Monkey Bite","health-and-safety","health-chain","seed",I,"CDC is the canonical owner for vaccines; the bite-response half is not theirs.",["R3"],None,None),
("arak-and-methanol-in-bali","Arak and Methanol in Bali: How to Drink Safely","health-and-safety","health-chain","none",I,"Survives R1/R2; volume unknown, news-driven.",[],None,None),
("indonesia-drug-laws-for-travelers","Indonesia's Drug Laws: What Americans Must Know Before Bali","health-and-safety","none","none",I,"Survives R1/R2; volume unknown.",[],None,None),
("common-scams-in-bali","Common Scams in Bali and How Each One Works","health-and-safety","money-leak","none",I,"Survives R1/R2; volume unknown, many publishers.",[],None,None),
("dengue-and-mosquitoes-in-bali","Dengue and Mosquitoes in Bali","health-and-safety","health-chain","none",I,"Survives R1/R2; volume unknown.",[],None,None),
("can-you-drink-the-water-in-bali","Can You Drink the Tap Water in Bali?","health-and-safety","health-chain","none",I,"Survives R1/R2; volume unknown.",[],None,None),
# ── Plan · phones, culture
("esim-vs-local-sim-in-bali","eSIM vs. Local SIM in Bali","phones-and-internet","none","none",I,"Shape ranks (esim-phone-data-spain 31 imp @ 6.4) but small, and eSIM SERPs are affiliate-heavy.",[],"esim-phone-data-spain 31 imp @ 6.4",None),
("indonesia-phone-registration-for-tourists","Indonesia's Phone Registration Rule: Do Tourists Need It?","phones-and-internet","none","none",I,"Customs is the canonical owner; question is whether it answers the short-stay case.",["R3"],None,None),
("bali-temple-dress-code-and-etiquette","What to Wear in Bali: Temple Dress Code and Etiquette","culture-and-etiquette","none","none",I,"Shape ranks (what-to-wear-rome-dress-code 47 imp @ 9.6), just under the 50 floor.",[],"what-to-wear-rome-dress-code 47 imp @ 9.6",None),
("bali-rules-for-tourists","Bali's Rules for Tourists: What Gets People Fined or Deported","culture-and-etiquette","none","none",I,"Survives R1/R2; volume unknown.",[],None,None),
("offerings-ceremonies-and-road-closures-in-bali","Offerings, Ceremonies and Road Closures: Reading Daily Life in Bali","culture-and-etiquette","holiday-collision","none",I,"Survives R1/R2; volume unknown.",[],None,None),
# ── Getting around
("getting-around-bali","How to Get Around Bali","getting-around","traffic-time","turn",S,"Needed for the site to make sense; broad query owned by large publishers.",[],None,None),
("grab-and-gojek-in-bali","Grab and Gojek in Bali: Where They Work and Where They Don't","drivers-and-ride-apps","traffic-time","seed",P,"Survives R1/R2 (R3 would have wrongly killed the analog). grab-in-thailand-guide 265 imp @ 8.9; grab-and-taxi-coverage-thailand 35 @ 9.1.",[],"grab-in-thailand-guide 265 imp @ 8.9",None),
("hiring-a-private-driver-in-bali","Hiring a Private Driver in Bali: How It Works and What a Day Covers","drivers-and-ride-apps","traffic-time","turn",I,"Survives R1/R2; no fleet analog, volume unknown.",[],None,None),
("bali-traffic-real-drive-times","Bali Traffic: Real Drive Times Between the Main Areas","drivers-and-ride-apps","traffic-time","turn",I,"Survives R1/R2; volume unknown. Drive times must come from the fact pipeline as ranges, never frozen single figures.",[],None,None),
("taxis-in-bali","Taxis in Bali: Metered Cabs, Local Transport Zones and Ride-App Limits","drivers-and-ride-apps","traffic-time","seed",I,"Shape ranks small (rome-taxis-guide 24 imp @ 9.2).",[],"rome-taxis-guide 24 imp @ 9.2",None),
("renting-a-car-in-bali","Renting a Car in Bali: Self-Drive vs. Car with Driver","drivers-and-ride-apps","scooter-liability","seed",I,"Options comparison; volume unknown.",[],None,None),
("renting-a-scooter-in-bali","Renting a Scooter in Bali: License, Insurance and Police Stops","scooters","scooter-liability","turn",P,"Survives R1/R2. Fleet analogs: e-scooters-in-barcelona-rules 78 imp @ 8.9; scooters-and-atvs-in-turkey 34 @ 5.7.",[],"e-scooters-in-barcelona-rules 78 imp @ 8.9",None),
("international-driving-permit-for-bali","Do Americans Need an International Driving Permit in Bali?","scooters","scooter-liability","seed",I,"Survives R1/R2; volume unknown.",[],None,None),
("scooter-vs-driver-in-bali","Scooter vs. Driver in Bali","scooters","scooter-liability","turn",P,"Options-not-places comparison, the R2 shape that wins: taxis-uber-car-barcelona 194 imp @ 8.5.",[],"taxis-uber-car-barcelona 194 imp @ 8.5",None),
("fast-boats-to-nusa-penida-and-lembongan","Fast Boats to Nusa Penida and Lembongan: Ports, Operators and Sea Conditions","boats-and-ferries","boat-day-buffer","turn",I,"Operators and booking platforms own much of this; does any of them explain the crossing rather than sell it?",["R3"],None,None),
("when-bali-fast-boats-cancel","When Bali's Fast Boats Cancel: Your Options and the Buffer You Need","boats-and-ferries","boat-day-buffer","turn",P,"Survives R1/R2. Fleet analog: when-ferries-cancel-thailand 70 imp @ 6.6.",[],"when-ferries-cancel-thailand 70 imp @ 6.6",None),
("bali-to-gili-fast-boat-vs-flight","Bali to the Gili Islands: Fast Boat vs. Flying via Lombok","boats-and-ferries","boat-day-buffer","turn",P,"Two ways of doing one journey: fast-vs-slow-ferries-greece 63 imp @ 7.1.",[],"fast-vs-slow-ferries-greece 63 imp @ 7.1",None),
("indonesia-domestic-flights-baggage-and-changes","Indonesian Domestic Flights: Baggage Rules and Changes","boats-and-ferries","none","none",I,"Shape ranks small (thailand-domestic-flight-baggage-and-changes 23 imp @ 6.3). Category is the nearest fit — flag if you want a 'Domestic Flights' subcategory.",[],"thailand-domestic-flight-baggage-and-changes 23 imp @ 6.3",None),
# ── Where to go (the area spine — STRUCTURAL by design)
("bali-areas-explained","Bali's Areas Explained: Which Part of the Island Is Which","where-to-go","base-split","turn",S,"Spine role: anchor. Bali has no gateway city, so the area map is the page every trip starts from.",[],None,"anchor"),
("ubud-guide","Ubud: What It Is Actually Like and Who It Suits","ubud","base-split","seed",S,"Area spine. Per-place guides are where the fleet's losers come from; written for navigation and internal links.",[],None,None),
("canggu-seminyak-legian-kuta-explained","Canggu, Seminyak, Legian and Kuta: One Coast, Four Different Stays","seminyak-canggu-kuta","base-split","seed",S,"Area spine; replaces the rejected place-vs-place page.",[],None,None),
("uluwatu-and-the-bukit-guide","Uluwatu and the Bukit Peninsula: Cliffs, Surf and the Drive In","uluwatu","base-split","seed",S,"Area spine.",[],None,None),
("sanur-and-nusa-dua-guide","Sanur and Nusa Dua: The Calm Coast","sanur-nusa-dua","base-split","seed",S,"Area spine.",[],None,None),
("nusa-lembongan-and-ceningan-guide","Nusa Lembongan and Ceningan","nusa-islands","boat-day-buffer","seed",S,"Area spine.",[],None,None),
("nusa-penida-day-trip-or-overnight","Nusa Penida: Day Trip or Overnight?","nusa-islands","boat-day-buffer","turn",I,"Two ways of doing one thing (the winning R2 shape), no measured analog.",[],None,None),
("munduk-and-north-bali-guide","Munduk and North Bali","north-and-east-bali","base-split","seed",S,"Area spine.",[],None,None),
("sidemen-and-amed-east-bali-guide","Sidemen and Amed: East Bali","north-and-east-bali","base-split","seed",S,"Area spine.",[],None,None),
("adding-gili-or-lombok-to-a-bali-trip","Adding the Gili Islands or Lombok to a Bali Trip: How Many Days It Takes","beyond-bali","boat-day-buffer","turn",I,"Nearest analog ranks small (which-greek-islands-to-combine 33 imp @ 9.2); close to an R2 place comparison, so framed as a time decision.",[],"which-greek-islands-to-combine 33 imp @ 9.2",None),
("komodo-from-bali","Komodo from Bali: Getting There and How Many Days You Need","beyond-bali","none","none",I,"Survives R1/R2; volume unknown, tour operators heavy.",[],None,None),
# ── Things to do
("uluwatu-tanah-lot-besakih-lempuyang-visits","Uluwatu, Tanah Lot, Besakih, Lempuyang: What Each Temple Visit Involves","temples-and-culture","traffic-time","seed",I,"Avoids the R1 'best temples' title; volume unknown.",[],None,None),
("lempuyang-gates-of-heaven-queue","Lempuyang's Gates of Heaven: The Queue, the Photo and the Drive","temples-and-culture","traffic-time","seed",I,"Single-sight logistics; fleet has both a win (camp-nou-tour-guide 413 imp @ 7.8) and losses (colosseum-underground 66.6) on this shape.",["R3"],"camp-nou-tour-guide 413 imp @ 7.8 vs colosseum-underground @ 66.6",None),
("uluwatu-kecak-dance-tickets-and-timing","Uluwatu Kecak Dance: Tickets, Timing and the Sunset Traffic","temples-and-culture","traffic-time","seed",I,"Ticket-logistics shape ranks small (park-guell-tickets-guide 36 imp @ 9.1).",["R3"],"park-guell-tickets-guide 36 imp @ 9.1",None),
("ubud-monkey-forest-rules-and-bites","Ubud's Monkey Forest: Rules, Bites and What to Leave Behind","temples-and-culture","health-chain","seed",I,"The forest's own site is the canonical owner for tickets; the bite question is open.",["R3"],None,None),
("mount-batur-sunrise-trek","Mount Batur Sunrise Trek: What the Night Actually Looks Like","volcanoes-and-hikes","traffic-time","seed",I,"Tour sellers dominate; does anyone describe the night honestly?",["R3"],None,None),
("jatiluwih-rice-terraces","Jatiluwih Rice Terraces: Getting There and Walking the Trails","waterfalls-and-rice-terraces","traffic-time","none",I,"Replaces the rejected sight-vs-sight page; volume unknown.",[],None,None),
("bali-waterfalls-stairs-fees-and-drive","Bali's Waterfalls: Stairs, Entry Fees and Which Side of the Island They Are On","waterfalls-and-rice-terraces","traffic-time","none",I,"Avoids the R1 'best waterfalls' title; volume unknown.",[],None,None),
("surfing-in-bali-by-season-and-coast","Surfing in Bali: Which Coast Works in Which Season","beaches-and-surf","wet-dry-season","turn",I,"Survives R1/R2; surf publishers strong, volume unknown.",[],None,None),
("manta-rays-at-nusa-penida","Manta Rays at Nusa Penida: Season, Currents and Who Should Skip It","diving-and-snorkeling","boat-day-buffer","seed",I,"Survives R1/R2; volume unknown.",[],None,None),
("choosing-a-yoga-retreat-in-ubud","Choosing a Yoga Retreat in Ubud: What the Listings Don't Say","wellness-and-yoga","none","none",I,"Survives R1/R2; volume unknown, aggregator-heavy.",[],None,None),
# ── Itineraries (R1 by nature — STRUCTURAL)
("one-week-in-bali","One Week in Bali: A Realistic First-Timer Route","by-trip-length","base-split","turn",S,"Spine role: route. R1 fires on itinerary / N days (median fleet position for this shape is near 70).",["R1:itinerary"],None,"route"),
("ten-days-in-bali","Ten Days in Bali: Adding the Nusa Islands","by-trip-length","boat-day-buffer","turn",S,"R1 itinerary shape; needed by the planner and the Start Here path.",["R1:itinerary"],None,None),
("two-weeks-in-bali","Two Weeks in Bali: North, East and an Island Leg","by-trip-length","base-split","turn",S,"R1 itinerary shape.",["R1:itinerary"],None,None),
("how-many-days-in-bali","How Many Days Do You Need in Bali, Coming from the US?","by-trip-length","long-haul-arrival","turn",I,"Close to R1's 'N days' but a question, not an itinerary. Volume unknown.",["R1-adjacent:N days"],None,None),
("bali-honeymoon-how-to-split-the-nights","Bali Honeymoon: How to Split the Nights","by-trip-type","base-split","turn",I,"Survives R1/R2 as titled; honeymoon SERPs are publisher-heavy.",[],None,None),
("bali-with-kids","Bali with Kids: Bases, Car Seats and Pools","by-trip-type","base-split","seed",I,"Survives R1/R2; volume unknown.",[],None,None),
# ── Where to stay
("where-to-stay-in-bali","Where to Stay in Bali: Choosing a Base","choosing-your-base","base-split","turn",S,"R1 fires on 'where to stay'. The site's central decision page; written for the funnel.",["R1:where to stay"],None,None),
("one-base-or-two-in-bali","One Base or Two? How to Split a Bali Stay","choosing-your-base","base-split","turn",P,"Two ways of arranging one trip: colosseum-vs-vatican-where-to-stay 91 imp @ 11.5.",[],"colosseum-vs-vatican-where-to-stay 91 imp @ 11.5",None),
("central-ubud-vs-the-outskirts","Staying in Central Ubud vs. the Rice-Field Outskirts","choosing-your-base","base-split","seed",P,"Within-one-place stay decision: staying-near-termini 83 imp @ 9.2.",[],"staying-near-termini 83 imp @ 9.2",None),
("short-term-rentals-in-bali-what-to-check","Short-Term Rentals in Bali: Licenses, Deposits and Fake Listings","villas-and-resorts","base-split","seed",I,"Shape ranks small (airbnb-barcelona-rental-crackdown 44 imp @ 9.1). Title deliberately avoids the R1 noun 'villa'.",[],"airbnb-barcelona-rental-crackdown 44 imp @ 9.1",None),
# ── Food & drink
("balinese-food-what-to-order","Balinese Food: What to Order and What Is in It","balinese-food","none","none",S,"Needed for the section to exist; broad query.",[],None,None),
("eating-at-warungs-in-bali","Eating at Warungs: How to Pick One","balinese-food","health-chain","seed",I,"Survives R1/R2; volume unknown.",[],None,None),
("food-allergies-and-dietary-needs-in-bali","Food Allergies and Dietary Needs in Bali: How to Ask","balinese-food","health-chain","none",I,"Survives R1/R2; volume unknown.",[],None,None),
("alcohol-in-bali-prices-and-rules","Alcohol in Bali: Why It Costs What It Does, and the Rules","cafes-bars-beach-clubs","none","none",I,"Nearest analog vermouth-cava-barcelona 53 imp @ 9.9 is a drinks-culture page, not the same query.",[],"vermouth-cava-barcelona 53 imp @ 9.9 (loose)",None),
("bali-beach-clubs-how-they-work","Bali Beach Clubs: Minimum Spends, Daybeds and Booking","cafes-bars-beach-clubs","none","none",I,"Survives R1 as titled (not 'best beach clubs'); volume unknown.",[],None,None),
# ── REJECTED (taxonomy would prescribe them; not written)
("things-to-do-in-bali","Things to Do in Bali","things-to-do","none","none",R,"R1: 'things to do'. free-things-to-do-barcelona 239 imp @ 86.8.",["R1:things to do"],None,None),
("canggu-vs-seminyak","Canggu vs. Seminyak","seminyak-canggu-kuta","none","none",R,"R2: place versus place. krabi-vs-phuket @ 58.2, santorini-vs-mykonos @ 85.4. Covered structurally by the four-stays page.",["R2"],None,None),
("tegalalang-vs-jatiluwih","Tegalalang vs. Jatiluwih Rice Terraces","waterfalls-and-rice-terraces","none","none",R,"R2: sight versus sight. casa-batllo-vs-casa-mila 187 imp @ 59.0.",["R2"],None,None),
("best-beaches-in-bali","Best Beaches in Bali","beaches-and-surf","none","none",R,"R1: 'best' + 'beaches'. santorini-best-beaches 209 imp @ 78.4.",["R1:best","R1:beaches"],None,None),
("private-villa-vs-hotel-in-bali","Private Villa vs. Hotel in Bali","villas-and-resorts","none","none",R,"R1 fires on 'villa' and 'hotel' (beachfront-villas-thailand 264 imp @ 51.5). It is an options comparison, so say so if you want it kept as STRUCTURAL instead.",["R1:villa","R1:hotel"],None,None),
("best-villas-in-seminyak","Best Villas in Seminyak","villas-and-resorts","none","none",R,"R1: 'best' + 'villas'. best-luxury-hotels-istanbul 189 imp @ 53.4.",["R1:best","R1:villa"],None,None),
]

# ── Stage 1c INVESTIGATE pass, 2026-10-13 ───────────────────────────────────
# One web-search look per INVESTIGATE row. The tool is a general web search, NOT
# Google's results page: it shows who covers a query and how directly, not rank
# order and not volume. Outcomes: PRODUCE (open: results thin, off-target, spam,
# sellers-only, or no US angle) · STRUCTURAL (contested but the site/guide needs
# it) · REJECT with rule "SERP-look" (contested and coverable inside another page).
SERP = {
"bali-visa-on-arrival-vs-e-voa":(S,"Several on-target explainers (visa agents, villa agencies, travel blogs). Contested; kept because the entry stack needs it."),
"indonesia-arrival-declaration-form":(S,"Official portal plus many step-by-step guides. Contested; kept because the form is mandatory and first-timers miss it."),
"extending-a-bali-visa-on-arrival":(R,"Crowded with visa-agent and blog guides; a one-to-two-week American trip rarely needs it. One paragraph in the visa page."),
"passport-validity-rules-for-indonesia":(R,"travel.state.gov answers it directly; the rest is thin. Merge into the visa page rather than a standalone."),
"choosing-a-layover-city-for-bali":(P,"OPEN: results were spam and scraped pages on unrelated domains; no credible US-origin comparison surfaced."),
"through-ticket-vs-separate-tickets-to-bali":(P,"OPEN: generic connection explainers and spam; nothing Bali-specific from a US origin."),
"bali-airport-transfers":(R,"Saturated by transfer sellers and large Bali sites. Fold the options into the arrival page."),
"jet-lag-on-a-us-to-bali-trip":(P,"Mostly open: one on-target page written for Australians, a hospital note, and spam. The US time-zone gap is unaddressed. Volume doubtful."),
"bali-departure-day-how-early-to-leave":(S,"Two small sites answer it directly with per-area pickup times. Contested; kept because it is the sharpest expression of the traffic swamp."),
"bali-atm-fees-real-cost":(R,"Wise, Revolut and several blogs own it; forum results are Australian. Fold the US-card angle into the money page."),
"bali-money-changer-short-change":(R,"Insurers and Bali sites have dedicated pages. Fold into the money page."),
"paying-by-qr-code-in-bali":(P,"OPEN for Americans: results are news items and a villa blog; the supported-country list they cite does not include the US, and nobody says what that means for a US visitor."),
"bali-rainy-season-what-its-like":(S,"Many dedicated pages. Contested; kept because the season swamp needs its wet half."),
"bali-in-july-and-august":(R,"Results are 'best time' pages that already cover it. Fold into the season page."),
"bali-public-holidays-what-closes":(P,"Fairly open: one calendar list and news items; 'what actually closes' is answered thinly. Analog turkish-public-holidays-what-closes 42 imp @ 10.2."),
"bali-belly":(S,"Saturated by health and travel publishers. Kept as the centre of the health chain."),
"bali-hospitals-and-clinics-billing":(P,"Fairly open: results are expat-insurance pages; the tourist billing sequence is not laid out. Analogs rank small (41 @ 8.0, 39 @ 5.2)."),
"travel-insurance-for-bali-fine-print":(P,"OPEN for Americans: every result is an Australian or NZ insurer or news story. No US-policy treatment surfaced."),
"vaccines-and-animal-bites-in-bali":(S,"A Bali hospital and news outlets cover the bite response well. Contested; kept for the health chain, and it absorbs the Monkey Forest page."),
"arak-and-methanol-in-bali":(P,"Partly open: older news pieces and one venue's guide. News-driven and volatile; low confidence."),
"indonesia-drug-laws-for-travelers":(P,"OPEN: results were cloned spam pages and a cannabis-clinic blog; no credible traveller explainer surfaced."),
"common-scams-in-bali":(R,"Saturated listicle territory. The two scams that matter live in the money and transport pages."),
"dengue-and-mosquitoes-in-bali":(R,"A large Bali site and news cover it. One section in the safety page."),
"can-you-drink-the-water-in-bali":(R,"Saturated by small sites. One section in the Bali belly page."),
"esim-vs-local-sim-in-bali":(S,"Saturated by eSIM sellers. Kept because the phones section needs one page."),
"indonesia-phone-registration-for-tourists":(P,"Fairly open: one dedicated blog and forum threads; the short-stay answer is buried."),
"bali-temple-dress-code-and-etiquette":(P,"Contested by small blogs only, no large publisher. Analog what-to-wear-rome-dress-code 47 imp @ 9.6."),
"bali-rules-for-tourists":(P,"OPEN: results are 2023 news reports of the announcement; no maintained explainer surfaced."),
"offerings-ceremonies-and-road-closures-in-bali":(R,"Open but thin and low-intent. Fold into the Galungan and public-holiday pages."),
"hiring-a-private-driver-in-bali":(S,"Driver-booking sites and Bali blogs cover it. Contested; kept because the traffic swamp turns on it."),
"bali-traffic-real-drive-times":(S,"One small site has per-route guides; the rest is spam. Kept as the factual core of the traffic swamp."),
"taxis-in-bali":(R,"Covered by several Bali sites. Fold into the Grab and Gojek page."),
"renting-a-car-in-bali":(R,"Rental sellers dominate. Fold into scooter-vs-driver."),
"international-driving-permit-for-bali":(P,"Partly open: one large Bali site and one thin US-specific page. The American angle (who issues it, which category) is lightly served."),
"fast-boats-to-nusa-penida-and-lembongan":(P,"OPEN on the R3 question: every result was a ticket seller. They sell the crossing; none explains ports, operators or sea state."),
"indonesia-domestic-flights-baggage-and-changes":(P,"Fairly open: a luggage-brand blog and old news; change fees unanswered. Small analog (23 imp @ 6.3)."),
"nusa-penida-day-trip-or-overnight":(S,"Several blogs answer it head-on. Contested; kept because the boat swamp turns on it."),
"adding-gili-or-lombok-to-a-bali-trip":(P,"OPEN: results were sailing charters and package deals, none answering the time question."),
"komodo-from-bali":(R,"Several on-target how-to pages; outside a first Bali trip. Parked."),
"uluwatu-tanah-lot-besakih-lempuyang-visits":(S,"'Best temples' listicles. Kept as the one temples page; absorbs Lempuyang and the Kecak show."),
"lempuyang-gates-of-heaven-queue":(R,"A strong dedicated blog page plus aggregators. Fold into the temples page."),
"uluwatu-kecak-dance-tickets-and-timing":(R,"A dedicated Bali-site page plus ticket sellers. Fold into the temples page."),
"ubud-monkey-forest-rules-and-bites":(R,"Saturated by travel blogs. The bite half moves to the vaccines-and-bites page."),
"mount-batur-sunrise-trek":(S,"Saturated by blogs and tour sellers. Kept so the volcano section is not empty."),
"jatiluwih-rice-terraces":(R,"Many dedicated pages. One section in the waterfalls-and-terraces page."),
"bali-waterfalls-stairs-fees-and-drive":(S,"'Best waterfalls' listicles. Kept as the one page for the section."),
"surfing-in-bali-by-season-and-coast":(S,"Surf camps own it. Kept because the season swamp needs the coast flip."),
"manta-rays-at-nusa-penida":(S,"Dive operators cover it thoroughly. Kept as the one diving page."),
"choosing-a-yoga-retreat-in-ubud":(S,"'Best retreats' listicles; the how-to-choose results are generic. Kept as the one wellness page."),
"how-many-days-in-bali":(S,"Large guidebook publishers answer it. Kept: the US travel-time angle feeds the long-haul swamp."),
"bali-honeymoon-how-to-split-the-nights":(S,"Hotel listicles and package sellers. Kept as a base-split page for a high-intent audience."),
"bali-with-kids":(S,"Guidebook and hotel-site pages. Kept as the one family page."),
"short-term-rentals-in-bali-what-to-check":(P,"Fairly open and timely: results are news stories about the licensing crackdown and one local site's verification note."),
"eating-at-warungs-in-bali":(R,"Several small on-target pages. Fold into the food page and the Bali belly page."),
"food-allergies-and-dietary-needs-in-bali":(P,"Partly open: one strong personal blog on peanuts only; other allergens unserved. Volume doubtful."),
"alcohol-in-bali-prices-and-rules":(R,"Three dedicated pages from Bali sites. The safety half stays in the arak page."),
"bali-beach-clubs-how-they-work":(P,"Fairly open: one venue's own blog dominates; no neutral explainer of minimum spends."),
}
# Handoffs after the pass: dry ground stays dry. Only these keep a seed; turns are capped below.
KEEP_SEED = {"bali-tourist-levy-explained","indonesia-arrival-declaration-form","bali-visa-on-arrival-vs-e-voa","bringing-medication-into-bali",
 "arriving-at-bali-airport","choosing-a-layover-city-for-bali","is-bali-expensive","galungan-and-kuningan-explained","grab-and-gojek-in-bali",
 "international-driving-permit-for-bali","central-ubud-vs-the-outskirts","short-term-rentals-in-bali-what-to-check","bali-public-holidays-what-closes"}
TURN_TO_SEED = {"through-ticket-vs-separate-tickets-to-bali","bali-rainy-season-what-its-like","bali-hospitals-and-clinics-billing","surfing-in-bali-by-season-and-coast",
 "how-many-days-in-bali","bali-honeymoon-how-to-split-the-nights","ten-days-in-bali","two-weeks-in-bali","bali-traffic-real-drive-times","fast-boats-to-nusa-penida-and-lembongan","adding-gili-or-lombok-to-a-bali-trip"}
NEW=[]
for i,r in enumerate(ROWS):
    r=list(r)
    if r[0] in SERP:
        assert r[5]==I, r[0]
        v,note=SERP[r[0]]
        r[6]="SERP look 2026-10-13: "+note+" | Before the look: "+r[6]
        r[5]=v
        if v==R: r[7]=list(r[7])+["SERP-look"]
        if v==P and not r[8]: r[8]="no fleet analog; decision rests on the SERP look"
    if r[5]==R: r[3],r[4]="none","none"
    elif r[4]=="seed" and r[0] not in KEEP_SEED: r[4]="none"
    elif r[0] in TURN_TO_SEED: r[4]="seed"
    NEW.append(tuple(r))
assert not [x for x in SERP if x not in {r[0] for r in ROWS}]
assert not [r[0] for r in NEW if r[5]==I]
ROWS=NEW
slugs=[r[0] for r in ROWS]; assert len(slugs)==len(set(slugs)), "duplicate slug"
sw={s[0] for s in SWAMPS}|{"none"}; roles=[r[9] for r in ROWS if r[9]]
assert len(roles)==len(set(roles)); assert all(r[3] in sw for r in ROWS); assert all(r[4] in("turn","seed","none") for r in ROWS)
arts=[]; preds=[]
for slug,title,cat,swamp,hand,verd,reason,rules,analog,role in ROWS:
    a={"title":title,"slug":slug,"category_slug":cat,"swamp":swamp,"handoff":hand}
    if role: a["role"]=role
    a["opportunity"]={"verdict":verd,"reason":reason,"rules_fired":rules}
    if verd==S: a["structural"]=True
    arts.append(a)
    if verd==P:
        preds.append({"slug":slug,"title":title,"decided_on":TODAY,"volume_estimate":None,
          "volume_source":"none for this domain (new site, no GSC history). Evidence is not a Bali volume measurement: "+analog,
          "verdict":"PRODUCE","rules_fired":rules,
          "confidence":"unrated — prospective filing; the analog shows the shape has ranked on a sibling domain, it does not show Bali query volume",
          "risk":"Bali volume for this query is unmeasured; a sibling's result on another destination may not transfer. Rows decided by the SERP look used a general web-search tool, not Google's results page","reason":reason})
out={"schema_version":4,"project":"baliforamericans","status":"APPROVED by user 2026-10-13 (categories, 73-article list, 10 swamps)","drafted_on":TODAY,
 "_README":"Stage 1 article plan. swamps = hypothesis-grade terrain map (the dossier cold-mine may re-rank). Per article: swamp + handoff (turn|seed|none) and the Stage 1c opportunity verdict. REJECT rows are kept as a record and are NOT written. Titles are working titles: any named product, form or rule in a title is confirmed in Stage 2 before it is written.",
 "swamps":[{"id":i,"name":n,"one_liner":o} for i,n,o in SWAMPS],"articles":arts}
json.dump(out,open("article-list.json","w"),indent=1,ensure_ascii=False)
json.dump(preds,open("predictions.json","w"),indent=1,ensure_ascii=False)
import collections
c=collections.Counter(a["opportunity"]["verdict"] for a in arts); h=collections.Counter(a["handoff"] for a in arts if a["opportunity"]["verdict"]!=R)
print("rows",len(arts),dict(c),"| to write:",len(arts)-c[R],"| handoff",dict(h),"| predictions",len(preds),"| roles",sorted(roles))
print("cats used:",len({a['category_slug'] for a in arts}))
