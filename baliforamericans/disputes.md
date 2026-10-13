# Research disagreements

Candidates only. Consensus is not source verification. facts.json was not changed.

Facts: 148; equal supplied values: 6; disagreements: 38; incomplete responses: 112.

## identity.name_local
- chatgpt: "Republik Indonesia"
- claude: "Bali (Provinsi Bali), Republik Indonesia"
- deepseek: "Indonesia"

## identity.capital
- chatgpt: "Jakarta; Indonesia's capital-transition arrangements and the status of Nusantara should be checked against current government legislation before publishing an unqualified legal claim."
- claude: "Denpasar is the provincial capital of Bali; Jakarta is the national capital"
- deepseek: "Jakarta"

## identity.timezones
- chatgpt: ["WIB (UTC+7), western Indonesia","WITA (UTC+8), including Bali, Lombok and the Gili Islands","WIT (UTC+9), eastern Indonesia"]
- claude: ["WITA (Central Indonesia Time), UTC+8, no daylight saving"]
- deepseek: ["WIB (UTC+7)","WITA (UTC+8)","WIT (UTC+9)"]

## identity.power_plug_voltage
- chatgpt: "230 V, 50 Hz; commonly type C and type F plugs. Verify appliance compatibility and bring an appropriate adapter."
- claude: "Type C and F plugs, 230 V, 50 Hz"
- deepseek: "230 V / 50 Hz, plug types C and F"

## country_facts.visa.by_nationality[United States].type
- chatgpt: null
- claude: "visa required; obtainable as an e-visa in advance or as a visa on arrival at the airport"
- deepseek: "visa_on_arrival"

## country_facts.visa.by_nationality[United States].fee
- chatgpt: null
- claude: "IDR 500,000 (page shows 'Rp500.000')"
- deepseek: "IDR 500,000 (~USD 28)"

## country_facts.visa.by_nationality[United States].online_authorization_required
- chatgpt: null
- claude: "Yes, separately from the visa: an arrival card via the All Indonesia system, completable only within 72 hours (3 days) before arrival; free; produces a QR code shown to Immigration and Customs"
- deepseek: true

## country_facts.visa.scam_sites_to_avoid
- chatgpt: [{"name_or_type":"Unofficial visa application intermediaries","why":"Some charge service fees above the government visa fee or imitate official application pages. A third-party fee does not establish government endorsement."},{"name_or_type":"Unofficial Bali tourist levy payment websites","why":"Use the provincial Love Bali system and confirm the domain before entering passport or payment details."},{"name_or_type":"Unofficial arrival-card websites","why":"Use the official All Indonesia platform; distinguish an arrival declaration from a visa application."}]
- claude: []
- deepseek: ["Any site that is not evisa.imigrasi.go.id (for e-VOA)","Any site that is not lovebali.baliprov.go.id (for tourist levy)","Any site that is not allindonesia.imigrasi.go.id (for arrival card)"]

## country_facts.documents.passport_validity_required
- chatgpt: "At least six months of validity from entry is the published Indonesian VOA requirement. A damaged passport or insufficient blank pages can cause problems; the US State Department page also specifies two blank pages for entry."
- claude: "6 months beyond the arrival date and 2 blank pages; the 'endorsement' page at the back of the passport does not count as blank; entry is refused otherwise"
- deepseek: "6 months from date of entry"

## country_facts.documents.onward_ticket_required
- chatgpt: "A confirmed return or onward ticket may be requested by the airline or Indonesian Immigration. Travelers should have one before departure."
- claude: "Yes - 'Outbound ticket from Indonesia' is listed among the documents to present to the immigration officer on arrival"
- deepseek: true

## country_facts.documents.notes
- chatgpt: "Check the passport used to enter is also used to leave Indonesia. Keep visa approval, payment receipt, onward ticket, accommodation details and arrival-declaration QR confirmation accessible. The arrival declaration, visa, Bali tourist levy and customs declaration are distinct requirements or charges and should not be conflated. For travel with medication, verify each active ingredient with Indonesian authorities; a US prescription does not automatically authorize import."
- claude: "Carry a copy of the passport as proof of identity and visa status (State Dept)."
- deepseek: "All travelers must complete the All Indonesia arrival declaration (immigration, customs, health, quarantine) online within 3 days before arrival. The form is free."

## country_facts.money.cash_vs_card
- chatgpt: "Use a combination of Indonesian rupiah cash and cards. Cash remains useful for small vendors, markets, local transport and smaller businesses; card acceptance is more common at established hotels and larger restaurants. Confirm fees and acceptance with the specific merchant."
- claude: "Cash still needed for small vendors, drivers, entrance fees and many warungs; cards widely taken at hotels, larger restaurants and shops, often with a surcharge"
- deepseek: "Cash is widely used for small purchases, local warungs, and markets. Cards (Visa/Mastercard) are accepted at hotels, mid-range to upscale restaurants, and larger shops. QR code payments (QRIS) are common but generally require an Indonesian bank account or e-wallet; foreign cards and apps typically cannot use QRIS directly."

## country_facts.money.atm_availability
- chatgpt: "ATMs are available in major visitor areas but reliability, withdrawal limits, fees and machine security vary. Use bank-affiliated machines in secure locations and decline dynamic currency conversion when it offers a clearly unfavorable rate."
- claude: "ATMs are common in south Bali and Ubud and sparse on the Nusa islands and in the north/east"
- deepseek: "ATMs are widely available in tourist areas (Kuta, Seminyak, Ubud, Sanur). Withdrawal limits are typically IDR 2,500,000–3,000,000 per transaction. Foreign card fees apply. Use ATMs inside banks or major convenience stores to reduce skimming risk."

## country_facts.money.currency_import_export_limit
- chatgpt: "The US State Department reports a maximum of IDR 100000000 for currency on entry and exit and notes that currency at or above the declaration threshold must be declared. Customs says cash and/or payment instruments totaling IDR 100000000 or more must be declared. Do not treat the stated maximum as permission to evade a declaration requirement."
- claude: "Not a cap but a DECLARATION duty: cash and/or other payment instruments worth at least IDR 100,000,000 (rupiah or foreign equivalent) must be declared to Customs on entry or exit. Taking IDR 100,000,000 or more in rupiah OUT also needs a Bank Indonesia permit; bringing that much rupiah IN must be declared and checked for authenticity. An individual may not carry foreign banknotes worth IDR 1,000,000,000 or more. Not declaring: administrative penalty of 10% of the amount carried, capped at IDR 300,000,000"
- deepseek: "IDR 100,000,000 (approximately USD 5,600) or equivalent in foreign currency must be declared. Amounts exceeding this require a customs declaration."

## country_facts.money.tipping_norm
- chatgpt: "Tipping is discretionary rather than universally mandatory. Check whether a service charge is already included; a small additional tip may be appropriate for good service. Norms vary by service, venue and local practice."
- claude: "Not obligatory. Many restaurant and hotel bills already add service and tax; small tips for drivers, guides and spa staff are customary"
- deepseek: "Tipping is not mandatory but appreciated. Many hotels and restaurants add a 5–10% service charge and 10% government tax. If a service charge is already included, additional tipping is optional. For private drivers, IDR 50,000–100,000 per day is customary. For spa therapists, IDR 20,000–50,000 is common."

## country_facts.getting_there.main_international_airports
- chatgpt: [{"name":"I Gusti Ngurah Rai International Airport, Denpasar/Bali","iata":"DPS","role":"Primary airport for Bali and the main international gateway for this project."},{"name":"Soekarno-Hatta International Airport, Jakarta","iata":"CGK","role":"Major international hub for onward domestic or international connections."}]
- claude: ["I Gusti Ngurah Rai International Airport, Denpasar (DPS)"]
- deepseek: ["I Gusti Ngurah Rai International Airport (DPS), Denpasar, Bali","Soekarno-Hatta International Airport (CGK), Jakarta"]

## country_facts.getting_there.flight_from_audience_origins
- chatgpt: []
- claude: [{"from":"any US airport","nonstop":null,"note":"Whether any nonstop US-Bali service exists must be checked against current schedules before it is stated either way; plan on at least one connection, commonly through East Asian, Southeast Asian or Gulf hubs."}]
- deepseek: [{"origin":"LAX","min_duration_hours":20,"typical_duration_hours":"22–30","stops":"1–2"},{"origin":"SFO","min_duration_hours":19,"typical_duration_hours":"21–28","stops":"1–2"},{"origin":"SEA","min_duration_hours":20,"typical_duration_hours":"22–30","stops":"1–2"},{"origin":"JFK","min_duration_hours":22,"typical_duration_hours":"24–32","stops":"1–2"},{"origin":"EWR","min_duration_hours":22,"typical_duration_hours":"24–32","stops":"1–2"},{"origin":"ORD","min_duration_hours":21,"typical_duration_hours":"23–30","stops":"1–2"},{"origin":"DFW","min_duration_hours":22,"typical_duration_hours":"24–32","stops":"1–2"},{"origin":"IAH","min_duration_hours":23,"typical_duration_hours":"25–33","stops":"1–2"}]

## country_facts.getting_around.intercity_rail
- chatgpt: "Bali has no intercity passenger rail network. Trains can be useful on Java, but reaching Bali from Java requires a road-and-ferry connection or a flight."
- claude: "None on Bali"
- deepseek: "No intercity rail on Bali. Indonesia has limited rail on Java (Jakarta–Surabaya) but it does not connect to Bali."

## country_facts.getting_around.buses
- chatgpt: "Bali has public buses and shuttle services, but coverage and frequency do not make them a universal substitute for private transport. Check the specific route, stop and operating schedule before planning around a bus."
- claude: "Limited public and tourist shuttle services; not a practical backbone for a short trip"
- deepseek: "Public buses (Trans Metro Dewata) exist in Denpasar and surrounding areas but are not practical for most tourist itineraries. Private shuttles and minivans (Perama, Kura-Kura) connect major tourist areas (Kuta, Ubud, Padang Bai, Amed)."

## country_facts.getting_around.domestic_flights
- chatgpt: "Domestic flights connect Bali with major Indonesian destinations. Airlines, schedules, baggage allowances and change fees vary; check the operating airline's rules for the actual fare."
- claude: "DPS has domestic links, including to Lombok and to Labuan Bajo for Komodo"
- deepseek: "Domestic flights connect DPS to Jakarta (CGK), Surabaya (SUB), Yogyakarta (YIA), Lombok (LOP), and other Indonesian cities. Garuda Indonesia, Lion Air, Citilink, and Batik Air operate these routes. Baggage allowances are typically 20 kg checked plus 7 kg carry-on; low-cost carriers charge for checked bags."

## country_facts.getting_around.ride_sharing
- chatgpt: "Grab and Gojek operate in parts of Bali, with availability and pickup rules varying by location. Some tourist attractions, ports and locally regulated areas can complicate pickups. Confirm availability in the app and agree on a lawful pickup point."
- claude: "Grab and Gojek operate; licensed taxis are widely available and Blue Bird is described as generally the most reliable"
- deepseek: "Grab and Gojek are the dominant ride-hailing apps. They operate widely in Bali but are banned in certain areas (e.g., some traditional markets, parts of Ubud, and certain beach areas) to protect local transport cooperatives. In banned zones, you must walk to a designated pickup point or use a local taxi."

## country_facts.getting_around.car_rental_and_driving
- chatgpt: "Indonesia drives on the left. Foreign visitors should verify their license, applicable international driving permit and motorcycle-specific entitlement before driving. Scooter rental does not confer legal permission to ride. Insurance exclusions, road conditions, congestion and local enforcement are material risks. No current official blood-alcohol limit or detailed licensing rule was verified in this research pass."
- claude: "A US licence alone is not recognized; foreign drivers must carry an International Driving Permit. Helmets are mandatory on motorcycles. Carry ID and vehicle registration. After an accident, stay and notify police. If fined, ask for an official receipt"
- deepseek: "Driving is on the left side of the road. A valid US driver's license alone is not sufficient for renting a car or scooter; an International Driving Permit (IDP) with the appropriate class (motorcycle endorsement for scooters) is required. Police checks are common. BAC limit is 0.0% for drivers under 21; for others, the legal limit is 0.05%."

## country_facts.when_to_go.climate_by_season
- chatgpt: "Bali generally has a wetter period around November through March and a relatively drier period around April through October, but timing varies by year, altitude and locality. Rain can occur during the nominal dry season; monthly climate descriptions are not daily forecasts. Check BMKG's current regional seasonal forecast."
- claude: "Tropical: a drier season roughly April-October and a wetter season roughly November-March; warm all year"
- deepseek: "Tropical climate with two main seasons: Dry season (April/May–October) with sunny days, lower humidity, and calmer seas. Rainy season (November–March) with frequent afternoon downpours, higher humidity, and occasional strong winds. Temperatures average 26–30°C (79–86°F) year-round."

## country_facts.safety_health.advisory_level
- chatgpt: "US Department of State: Level 2, Exercise Increased Caution for Indonesia. Advisory issued 2026-07-07. It cites natural disasters, unrest and terrorism; the advisory specifically says not to travel to Central Papua and Highland Papua. These restrictions are not a statement that Bali itself is under a blanket do-not-travel warning."
- claude: "Level 2 - Exercise increased caution (natural disasters, unrest, terrorism); Level 4 Do Not Travel applies only to Central Papua and Highland Papua"
- deepseek: "Level 2 — Exercise increased caution (issued July 7, 2026)"

## country_facts.safety_health.main_risk
- chatgpt: "Road crashes, especially involving motorcycles; mosquito-borne illness; gastrointestinal illness; ocean currents and drowning; volcanic activity, earthquakes and other natural hazards; theft and scams; alcohol adulteration; and severe legal consequences for prohibited drugs. Risk varies substantially by activity and location."
- claude: "Road traffic, especially scooters"
- deepseek: "Natural disasters (earthquakes, volcanic eruptions, tsunamis), terrorism (low but present), demonstrations that can turn violent, and road safety (scooter accidents are a leading cause of injury for tourists)."

## country_facts.safety_health.vaccines
- chatgpt: "Consult a travel-health clinician at least a month before departure. CDC recommends routine vaccines be up to date and recommends hepatitis A for unvaccinated travelers aged one year or older and hepatitis B for unvaccinated travelers of all ages. Typhoid is recommended for most travelers. Rabies pre-exposure vaccination depends on exposure and access to prompt care. Japanese encephalitis vaccination depends on itinerary and duration. CDC reported Zika cases in returning travelers from Bali in a notice dated 2026-08-07; mosquito and sexual-transmission precautions are important, and pregnancy-related travel advice needs particular care."
- claude: "None required for entry (State Dept). CDC recommends hepatitis A, hepatitis B and typhoid for most travelers, routine vaccines up to date, Japanese encephalitis for longer or higher-risk stays, and a pre-exposure rabies discussion"
- deepseek: "No vaccines are mandatory for US citizens arriving directly from the US. CDC recommends routine vaccines (MMR, Tdap, polio, influenza) plus hepatitis A, typhoid, and rabies (for certain travelers). Yellow fever vaccine is required only if arriving from a country with yellow fever transmission. COVID-19 vaccination is no longer required."

## country_facts.safety_health.tap_water_safe
- chatgpt: "Do not assume tap water is potable. Travelers generally use sealed bottled water or water treated by a reliable provider for drinking; ice and food hygiene require judgment. Avoid claiming that all water or ice in every establishment is unsafe or safe."
- claude: "Not treated as drinkable; use bottled or filtered water"
- deepseek: false

## country_facts.safety_health.emergency_numbers
- chatgpt: {"police":"110","ambulance":"118 or 119; availability and dispatch arrangements can vary","fire":"113"}
- claude: {"unified":"112","police":"110","ambulance":"119","fire":"113","search_and_rescue":"115"}
- deepseek: {"police":"110","ambulance":"118 or 119","fire":"113"}

## country_facts.safety_health.common_scams
- chatgpt: ["ATM skimming, card fraud and misleading currency-conversion offers","Unofficial taxi or transfer offers and unclear fares","Rental damage disputes involving scooters or vehicles","Fake or misleading accommodation listings and deposit requests","Unofficial visa, arrival-card and tourist-levy payment websites","Overpriced or unclear tour, boat-transfer and activity terms"]
- claude: ["money-changer sleight of hand","look-alike taxis imitating the reputable operator","'free' tours with commission stops"]
- deepseek: ["Scooter rental damage scams (inflated repair charges)","Money changers with hidden fees or short-changing","ATM skimming","Fake tourist levy payment sites (only use lovebali.baliprov.go.id)","Unofficial visa or arrival form sites charging fees (official sites are free or clearly marked)"]

## country_facts.connectivity.sim_esim
- chatgpt: "Travelers can consider an international eSIM, a local Indonesian SIM or roaming. Device compatibility, data allowance, ID registration and whether a foreign handset needs IMEI registration depend on the plan and circumstances. Confirm current tourist registration rules with the carrier and Indonesian authorities; do not state that every short-term visitor must register a foreign handset without verifying the applicable exemption."
- claude: "Travel eSIMs and local SIMs both work; a local number helps with ride apps"
- deepseek: "eSIMs from providers like Ubigi, Airalo, and Holafly work in Indonesia and can be purchased before travel. Local prepaid SIM cards (Telkomsel, XL, Indosat) are widely available at airports and convenience stores. Tourists must register a local SIM with their passport; no Indonesian tax ID (NPWP) is required."

## country_facts.connectivity.coverage
- chatgpt: "Coverage is generally better in developed tourist areas than in remote, mountainous or offshore locations. Coverage on Nusa Penida, Nusa Lembongan, the Gilis and remote parts of Bali varies by carrier and terrain. Download offline maps and retain key bookings offline."
- claude: "Good in south Bali and Ubud; patchier in the highlands, the north and parts of Nusa Penida"
- deepseek: "4G/LTE coverage is good in Bali's tourist areas (Kuta, Seminyak, Ubud, Sanur, Nusa Dua). 5G is available in some areas. Rural and remote areas (north Bali, Nusa Penida interior) may have weaker or spotty coverage."

## country_facts.culture_etiquette.dress_norms
- chatgpt: "Beachwear is appropriate at many beaches and pools but not generally suitable for temple visits or formal religious settings. At temples, follow posted rules and staff guidance, cover shoulders and knees as required, and use a sarong where requested. Dress expectations differ between ordinary public spaces and religious ceremonies."
- claude: "Temples require a sarong and sash and covered shoulders; beachwear stays at the beach"
- deepseek: "Dress modestly at temples: sarong and sash required (usually available for rent or loan at temple entrances). Shoulders and knees should be covered. Beachwear is fine at the beach but not in towns or temples."

## country_facts.culture_etiquette.dos_and_donts
- chatgpt: ["Respect temple rules, sacred spaces and local directions.","Ask permission before photographing people or ceremonies.","Do not step on or deliberately disturb Balinese daily offerings.","Dress appropriately when entering temples and other religious sites.","Do not touch another person's head or use feet to point at people or sacred objects.","Avoid littering and respect environmental restrictions.","Do not assume that foreign prescriptions, cannabis, CBD or recreational drugs are legal in Indonesia.","Respect Nyepi restrictions and local instructions.","Check the full price and conditions of tours, rentals, boat transfers and accommodation before paying."]
- claude: ["do not step on daily offerings when it can be avoided","do not climb on temple structures or sacred trees","keep ceremonies' road closures in mind when timing a drive"]
- deepseek: ["DO: Use your right hand for giving/receiving, eating, and pointing.","DO: Remove shoes before entering a home or temple.","DON'T: Step on offerings (small palm-leaf trays on the ground).","DON'T: Touch someone's head (considered sacred).","DON'T: Point with your index finger; use your thumb or whole hand.","DON'T: Display affection publicly (holding hands is fine; kissing is not).","DON'T: Raise your voice or show anger; maintain calm and patience."]

## cities[Nusa Penida].facts.how_to_get_there
- chatgpt: "Commonly reached by fast boat from Bali, often from Sanur. Boat schedules, ports, sea conditions and operator procedures vary."
- claude: null
- deepseek: "Fast boat from Sanur, Padang Bai, or Kusamba to Toya Pakeh or Sampalan (30–45 min). Boats are frequent in the morning but can be cancelled due to rough seas."

## cities[Nusa Penida].facts.local_transport
- chatgpt: "Private driver or locally arranged transport is often more practical than assuming easy self-driving. Roads can be rough, narrow and slow, and access to viewpoints may involve steep steps."
- claude: null
- deepseek: "Scooter rental is the main way to explore (roads are rough; only for experienced riders). Private drivers with cars are also available for hire."

## cities[Nusa Penida].facts.airport
- chatgpt: "No commercial airport is normally used for tourist access; boat transfers from Bali are the usual route."
- claude: null
- deepseek: "No airport on Nusa Penida; nearest is DPS (Bali)"

## itineraries[One Week in Bali: A Realistic First-Timer Route].plan
- chatgpt: [{"day":1,"morning":"Arrive at DPS, complete immigration and customs procedures, and transfer to the first accommodation.","afternoon":"Keep the schedule light; rest, hydrate and adjust to the time difference.","evening":"Have an easy meal near the accommodation and confirm transport for the next day."},{"day":2,"morning":"Explore central Ubud and its cultural center.","afternoon":"Visit a nearby landscape or rice-terrace area with a driver.","evening":"Dinner in Ubud and an early night if jet lag persists."},{"day":3,"morning":"Choose one major cultural site or countryside excursion.","afternoon":"Allow time for the return journey rather than stacking distant attractions.","evening":"Relax in Ubud."},{"day":4,"morning":"Transfer to a southern Bali base such as Sanur, Seminyak or Uluwatu.","afternoon":"Check in and explore the immediate area.","evening":"Beachfront or local dinner."},{"day":5,"morning":"Explore the chosen coast, beach or cultural attraction.","afternoon":"Keep travel within the same general area to reduce traffic time.","evening":"Optional sunset activity, subject to weather and transport."},{"day":6,"morning":"Choose a local activity, a beach visit or a half-day excursion.","afternoon":"Leave time for rest, shopping or weather disruption.","evening":"Pack and reconfirm airport transport."},{"day":7,"morning":"Depart for DPS with a traffic buffer appropriate to the flight and starting area.","afternoon":"Airport departure if scheduled.","evening":"In transit or at destination."}]
- claude: null
- deepseek: [{"day":1,"morning":"Arrive at DPS. Complete immigration, collect bags, get SIM/transport.","afternoon":"Check into hotel in Seminyak or Canggu. Rest and recover from jet lag.","evening":"Sunset at a beach club (e.g., Potato Head or Finns). Dinner nearby."},{"day":2,"morning":"Explore Seminyak: boutique shops, cafes.","afternoon":"Beach time at Seminyak or Double Six Beach.","evening":"Dinner at a warung or beachfront restaurant."},{"day":3,"morning":"Day trip to Uluwatu Temple (cliff views).","afternoon":"Visit Padang Padang or Bingin Beach.","evening":"Kecak fire dance at Uluwatu at sunset."},{"day":4,"morning":"Transfer to Ubud (1.5–2 hours).","afternoon":"Visit Sacred Monkey Forest and Ubud Art Market.","evening":"Dinner in central Ubud. Optional: Balinese dance performance."},{"day":5,"morning":"Tegallalang Rice Terraces and Tirta Empul Temple.","afternoon":"Campuhan Ridge Walk or spa treatment.","evening":"Night market food tour."},{"day":6,"morning":"Day trip to Nusa Penida (fast boat from Sanur).","afternoon":"Kelingking Beach and Broken Beach.","evening":"Return to Bali. Dinner in Sanur or Ubud."},{"day":7,"morning":"Final souvenir shopping or relax at hotel.","afternoon":"Transfer to DPS for departure (allow 3+ hours for international flights).","evening":"Depart Bali."}]

## itineraries[One Week in Bali: A Realistic First-Timer Route].assumptions
- chatgpt: "Seven calendar days in Bali, international arrival and departure through DPS, ordinary sightseeing pace, no overnight trip to Nusa Penida or the Gilis, and no live prices or operating hours assumed. For a US-origin trip, account for date-line effects and possible arrival on a different calendar date."
- claude: null
- deepseek: "Assumes arrival and departure from DPS. Does not include Nusa islands overnight or Gili/Lombok extension. Based on typical traffic and boat schedules. Adjust for jet lag and personal pace."

Open appropriate sources, check scope and effective dates, then write verified facts separately. Review all unresolved items; never cap their count.
