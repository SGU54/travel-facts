# Disputes — human ruling required

Panel: claude, deepseek, gemini, grok. 22 facts auto-settled, 46 disputed, 173 recommendations pooled.

## 1. `identity.name_local`
- claude: "Elláda (Ελλάδα)"
- deepseek: "Ελλάδα"
- gemini: "Ελλάδα (Elláda)"
- grok: "Ελλάδα (Elláda)"

## 2. `identity.timezones`
- claude: ["EET (UTC+2), EEST (UTC+3) in summer"]
- deepseek: ["UTC+2 (EET)","UTC+3 (EEST daylight)"]
- gemini: ["UTC+2 (Eastern European Time)","UTC+3 (Eastern European Summer Time)"]
- grok: ["UTC+2"]

## 3. `identity.power_plug_voltage`
- claude: "230V, 50Hz, Type C and F (Americans need a plug adapter; 120V-only devices need a converter)"
- deepseek: "230V / 50Hz, Type C and F plugs"
- gemini: "230V / 50Hz, Types C and F"
- grok: "230V, 50Hz, types C and F"

## 4. `country_facts.visa.scam_sites_to_avoid`
- claude: ["Unofficial 'ETIAS' and 'Schengen visa' sites that charge inflated fees — only use the official EU europa.eu domain"]
- deepseek: ["Any site charging a fee for ETIAS before it is officially launched","Third-party visa services that are not the official EU or Greek consular sites"]
- gemini: ["Unofficial ETIAS application websites charging excessive service fees"]
- grok: ["Unofficial visa/ETIAS application sites charging high fees"]

## 5. `country_facts.documents.passport_validity_required`
- claude: "Passport must be valid for at least 3 months beyond your planned departure from the Schengen area, and issued within the previous 10 years"
- deepseek: "At least three months beyond intended departure date from the Schengen Area, and issued within the last 10 years."
- gemini: "Valid for at least 3 months beyond the intended date of departure from the Schengen area (6 months recommended)."
- grok: "At least 3 months beyond planned departure from Schengen; issued within last 10 years"

## 6. `country_facts.documents.onward_ticket_required`
- claude: "A return or onward ticket may be requested at the border"
- deepseek: "Not officially required for US citizens, but airlines may ask for proof of onward/return travel."
- gemini: true
- grok: "Not strictly required but may be requested as proof of intent to leave"

## 7. `country_facts.money.cash_vs_card`
- claude: "Cards (incl. contactless, Apple/Google Pay) are widely accepted in cities, hotels, and most tavernas. Carry some cash for small islands, village kafenia, markets, and some ferries."
- deepseek: "Cards widely accepted in cities and tourist areas, but cash is still preferred in smaller islands, tavernas, and for taxis. Always carry some euros."
- gemini: "Cards widely accepted, including Apple Pay/Google Wallet. Cash needed for small tips, kiosks (periptera), and some rural island spots."
- grok: "Cards widely accepted in cities/tourist areas; carry cash for tavernas, small shops, islands, and ferries"

## 8. `country_facts.money.atm_availability`
- claude: "ATMs plentiful in Athens and on main islands. Prefer bank ATMs; AVOID Euronet ATMs (poor rates/fees). Always choose to be charged in EUR, not USD (decline dynamic currency conversion)."
- deepseek: "ATMs widely available in cities, towns, and tourist hubs. Some islands have limited ATMs; get cash in advance."
- gemini: "Ubiquitous in cities and major islands. Use bank ATMs (Alpha Bank, Piraeus, Eurobank, National Bank of Greece) to avoid high fees from generic ATMs like Euronet."
- grok: "Excellent in Athens and major tourist spots; reliable ATMs with low fees using networks like Visa/Mastercard"

## 9. `country_facts.money.currency_import_export_limit`
- claude: "Amounts of €10,000 or more (cash equivalent) must be declared when entering/leaving the EU"
- deepseek: "Declare amounts over €10,000 (or equivalent) when entering or leaving the EU."
- gemini: "10,000 EUR or equivalent must be declared."
- grok: "Declare amounts over €10,000"

## 10. `country_facts.money.tipping_norm`
- claude: "Tipping is modest and not obligatory. Rounding up or leaving 5–10% at tavernas is appreciated; a few euros for hotel staff and taxi rounding. No US-style 18–20% expectation."
- deepseek: "Not mandatory; 5–10% rounding up is appreciated for good service in restaurants. Check if service charge is already included."
- gemini: "Leaving 5-10% at restaurants is customary but not strictly mandatory. Round up taxi fares. Tip hotel staff/porters 1-2 Euros."
- grok: "Not obligatory; round up or 5-10% for good service in restaurants; small for taxis/tours"

## 11. `country_facts.getting_there.main_international_airports`
- claude: ["Athens Eleftherios Venizelos International Airport (ATH)","Heraklion Nikos Kazantzakis (HER), Crete","Thessaloniki (SKG)","seasonal island airports: Santorini (JTR), Mykonos (JMK)"]
- deepseek: ["Athens International Airport 'Eleftherios Venizelos' (ATH)","Thessaloniki Airport 'Makedonia' (SKG)"]
- gemini: ["Athens International Airport (ATH)"]
- grok: ["Athens (ATH) - Eleftherios Venizelos","Heraklion (HER) Crete","Thessaloniki (SKG)"]

## 12. `country_facts.getting_there.national_carrier`
- claude: "Aegean Airlines (with Olympic Air for domestic)"
- deepseek: "Aegean Airlines"
- gemini: "AEGEAN Airlines"
- grok: "Aegean Airlines"

## 13. `country_facts.getting_around.intercity_rail`
- claude: "Limited rail network (Athens–Thessaloniki main line). Not the backbone for a first-timer island trip; ferries and domestic flights matter more."
- deepseek: "Limited; main line connects Athens to Thessaloniki and other northern cities. Not a primary option for island travel."
- gemini: "Limited network. Main route connects Athens to Thessaloniki. TrainOSE operates trains."
- grok: "Limited; useful for some mainland routes but not extensive"

## 14. `country_facts.getting_around.buses`
- claude: "KTEL intercity buses serve the mainland; on islands local buses are cheap but infrequent. KTEL for Athens-area day trips (e.g., Cape Sounion)."
- deepseek: "KTEL bus network covers mainland and some regional routes; reliable and affordable."
- gemini: "KTEL handles regional and intercity bus routes. Excellent, reliable coverage across the mainland and within larger islands."
- grok: "KTEL buses reliable for mainland and some islands; affordable"

## 15. `country_facts.getting_around.domestic_flights`
- claude: "Aegean, Olympic Air, Sky Express fly Athens to Santorini, Mykonos, Crete, Naxos, Paros (~45–55 min). Often faster than ferry for far islands like Crete; book ahead in summer."
- deepseek: "Available from Athens to many islands (Santorini, Mykonos, Crete, Rhodes, etc.) and Thessaloniki. Operated by Aegean, Olympic Air, Sky Express."
- gemini: "Operated mostly by AEGEAN/Olympic Air and Sky Express. Connects Athens to major islands (Santorini, Mykonos, Crete, Naxos, Paros). Takes ~45 mins."
- grok: "Aegean, Sky Express, Olympic Air; fast for distant islands"

## 16. `country_facts.getting_around.ride_sharing`
- claude: "Uber operates in Athens but dispatches licensed taxis (not private drivers); the local 'FREENOW' app is widely used. On islands, taxis are scarce — pre-book transfers."
- deepseek: "Limited; Uber operates in Athens (Uber Taxi and Uber X with licensed taxis), but not widely available on islands."
- gemini: "Uber exists in Athens but operates as a taxi-hailing app (Uber Taxi). FreeNow is widely used for taxis."
- grok: "Uber limited; taxis and local apps common"

## 17. `country_facts.getting_around.car_rental_and_driving`
- claude: "Greeks drive on the RIGHT. US license accepted in practice by many agencies, but Greek law requires an International Driving Permit (IDP) alongside it — get one from AAA before you go. Minimum rental age usually 21–25. Roads on islands can be narrow/steep; a car is great on Crete and Naxos, unnecessary on Santorini/Mykonos."
- deepseek: "Drive on the right. Americans need a valid US driver's license AND an International Driving Permit (IDP) to rent and drive legally. The IDP translates your license and is required by Greek law for non-EU drivers. Legal blood alcohol limit is 0.05%."
- gemini: "Drive on the right. International Driving Permit (IDP) formally required for US citizens alongside US license, though some rental agencies may not check. Strict BAC limit of 0.05% (0.02% for newer drivers)."
- grok: "Drive on right; international permit recommended; manual common; winding island roads"

## 18. `country_facts.when_to_go.climate_by_season`
- claude: "Mediterranean: hot dry summers (Jul–Aug highs 85–95°F/29–35°C, peak crowds), mild wet winters. Sea is warmest Aug–Sep. The meltemi wind can disrupt Cyclades ferries in Jul–Aug."
- deepseek: "Mediterranean: hot, dry summers (June–August); mild, wet winters (December–February); spring and fall are pleasant with moderate temperatures."
- gemini: "Mild, wet winters (Nov-Mar); Warm, blooming springs (Apr-May); Hot, dry summers (Jun-Aug); Warm, pleasant autumns (Sep-Oct)."
- grok: "Hot dry summers (Jun-Sep, 80-95F+ islands); mild springs/falls (60-80F); cool wet winters"

## 19. `country_facts.safety_health.advisory_level`
- claude: "Typically US State Department Level 1 (Exercise Normal Precautions) — verify current level and date before travel"
- deepseek: "Level 1: Exercise Normal Precautions (as of October 2025 advisory, per State Department)."
- gemini: "Level 1: Exercise Normal Precautions"
- grok: "Level 1: Exercise Normal Precautions (US State Dept)"

## 20. `country_facts.safety_health.main_risk`
- claude: "Petty theft/pickpocketing in crowded tourist areas (Athens metro, Monastiraki, Acropolis crowds); occasional strikes/demonstrations in Athens; summer heat and wildfire risk inland."
- deepseek: "Petty theft and pickpocketing in crowded tourist areas, especially Athens and islands. Scams targeting tourists."
- gemini: "Pickpocketing in crowded tourist areas and on public transit (e.g., Athens Metro). Heat exhaustion in summer. Occasional strikes/demonstrations in central Athens."
- grok: "Petty theft in tourist areas; traffic; heat in summer"

## 21. `country_facts.safety_health.vaccines`
- claude: "No special vaccines required for US travelers; routine vaccinations recommended. Check CDC before travel."
- deepseek: "No special vaccines required; routine vaccines (MMR, DPT, etc.) should be up to date."
- gemini: "No special vaccines required. Routine vaccines recommended."
- grok: "Routine US vaccines; no special required"

## 22. `country_facts.safety_health.tap_water_safe`
- claude: "Tap water is safe to drink in Athens and most of the mainland. On many islands (incl. Santorini, Mykonos) tap water is brackish/desalinated — locals drink bottled; fine for brushing teeth."
- deepseek: "Generally safe in cities and tourist centers; some islands use desalinated water which is safe but may taste different. Bottled water is widely available."
- gemini: "Safe in Athens and mainland cities. Usually not recommended or palatable on most islands (stick to bottled water)."
- grok: "Generally safe in Athens but bottled preferred on islands"

## 23. `country_facts.safety_health.emergency_numbers`
- claude: {"police":"100 (or 112 EU-wide)","ambulance":"166 (or 112)","fire":"199 (or 112)"}
- deepseek: {"police":"100","ambulance":"166","fire":"199"}
- gemini: {"police":"100","ambulance":"166","fire":"199","tourist_police":"1571","european_emergency":"112"}
- grok: {"police":"100 or 112","ambulance":"166 or 112","fire":"199 or 112"}

## 24. `country_facts.safety_health.common_scams`
- claude: ["Taxi overcharging from Athens airport — agree on meter or fixed tariff","Bar 'friendly local' scams in Athens nightlife districts","Euronet ATM fee/rate gouging","Inflated 'skip-the-line' resellers near the Acropolis"]
- deepseek: ["Overpriced taxi rides (insist on meter or agree on fare beforehand)","Fake ticket sellers at tourist sites","Restaurant menu scams (check prices before ordering)","Street vendors offering 'free' gifts then demanding payment","Distraction theft (someone spills something on you, etc.)","Fake booking/hijacking scams (verify reservations directly with hotels)"]
- gemini: ["Overcharging at tourist trap restaurants (especially around Acropolis or Mykonos beaches)","Taxi drivers refusing to use meter or taking 'scenic' routes","Bar scams inviting tourists for a drink and handing a massive bill"]
- grok: ["Overpriced tourist tavernas","Fake taxi overcharges","Pickpocketing in crowds"]

## 25. `country_facts.connectivity.sim_esim`
- claude: "eSIM is the easiest option for Americans — Airalo, Holafly, or local Cosmote/Vodafone/Nova eSIMs work well. EU roaming means a Greek SIM works across the EU. Verizon/AT&T/T-Mobile international day passes are pricier but simplest."
- deepseek: "eSIMs available from providers like Airalo, Holafly; local SIMs from Cosmote, Vodafone, and Wind with tourist plans (e.g., €13–€15 for data + calls)."
- gemini: "eSIMs (Airalo, Holafly) highly recommended for modern US phones. Local physical SIMs available at airport and city stores (Cosmote, Vodafone, Nova) with passport."
- grok: "eSIMs easy via Airalo etc.; local SIMs at airport/kiosks"

## 26. `country_facts.connectivity.coverage`
- claude: "Excellent 4G/5G in cities and on main islands; can be patchy in remote mountain/coastal spots on Crete and smaller Cyclades."
- deepseek: "Good 4G/5G coverage in cities and tourist areas; may be spotty on remote islands and mountainous regions."
- gemini: "Excellent 4G/5G in cities and popular islands. Can be spotty on ferry crossings and in remote mountain areas."
- grok: "Good in populated areas and most islands"

## 27. `country_facts.culture_etiquette.dress_norms`
- claude: "Casual and beachy on islands; smart-casual for nicer dinners. Cover shoulders and knees to enter churches and monasteries (e.g., on Crete, in Athens). Bring sun protection and sturdy sandals for ancient-site stones."
- deepseek: "Casual and modest clothing is acceptable. For churches and monasteries, cover shoulders and knees. Beachwear is for beaches only."
- gemini: "Casual but neat. Modest dress required for monasteries/churches (shoulders covered, long pants/skirts). Beachwear belongs only at the beach."
- grok: "Modest at religious sites (cover shoulders/knees); beachwear fine at beaches"

## 28. `country_facts.culture_etiquette.dos_and_donts`
- claude: ["Do say 'kaliméra' (good morning) / 'efcharistó' (thank you)","Do expect late dinners (9pm+) and a slow, lingering meal pace","Don't rush the waiter for the check — you ask for it","Don't flush toilet paper where bins are provided (older island plumbing)","Don't expect everything open midday — some shops close for afternoon rest"]
- deepseek: undefined
- gemini: ["DO greet shop owners with 'Kalimera' (good morning) or 'Kalispera' (good evening).","DO embrace a slower pace; meals can take hours.","DON'T flush toilet paper anywhere in Greece; use the bin provided.","DON'T show the 'moutza' (open palm with fingers extended toward someone's face) as it is highly offensive."]
- grok: ["Greet with 'Kalimera'","Don't rush meals","Respect siesta hours","Tip modestly in cash"]

## 29. `cities[Athens].facts.how_to_get_there`
- claude: "Primary US gateway (ATH). Metro Line 3 connects the airport to the city center (~40 min, ~€9); taxi ~€40 flat daytime tariff to the center."
- deepseek: "Fly into Athens International Airport (ATH) from US hubs. Then take Metro (Line 3), suburban rail, bus (X95), or taxi into the city. For islands, take ferry from Piraeus port (Metro Line 1) or fly domestically."
- gemini: "Direct flights from US hubs. Gateway for the islands."
- grok: "Metro/bus/taxi from ATH airport (~30-45 min to center)"

## 30. `cities[Athens].facts.local_transport`
- claude: "Walkable historic core (Plaka, Monastiraki). Clean, cheap metro reaches the Acropolis, port (Piraeus), and airport. Single ticket ~€1.20."
- deepseek: "Metro (Lines 1, 2, 3), buses, trams, and taxis. Metro is efficient for major sights. Buy tickets at stations or via the 'Ath.ena' app."
- gemini: "Excellent Metro system, buses, trams. Walkable historical core."
- grok: "Metro, buses, walking; tickets affordable"

## 31. `cities[Athens].facts.airport`
- claude: "Athens Eleftherios Venizelos International (ATH)"
- deepseek: "Athens International Airport 'Eleftherios Venizelos' (ATH)"
- gemini: "Athens International Airport (ATH) - Eleftherios Venizelos"
- grok: "Athens International Airport (ATH)"

## 32. `cities[Santorini].facts.how_to_get_there`
- claude: "Ferry from Piraeus (~5h high-speed to ~8h conventional) or ~45-min flight from Athens. Ferries dock at Athinios port; book transfers — it's a steep climb to the caldera towns."
- deepseek: "Ferry from Piraeus (5–8 hours) or Rafina (4–5 hours); high-speed ferries available. Also domestic flights from Athens (45–50 minutes)."
- gemini: "45-min flight from Athens or fast ferry (~5 hours) from Piraeus."
- grok: "Fly to JTR or ferry from Athens/Piraeus"

## 33. `cities[Santorini].facts.local_transport`
- claude: "Local buses hub at Fira; cars/ATVs popular but parking is tight in Oia/Fira. Pre-booked transfers easiest for the airport/port."
- deepseek: "Buses connect Fira to Oia, beaches, and the port. Taxis and ATVs/cars are available; roads can be narrow and steep."
- gemini: "KTEL public buses connect villages to Fira. Rental cars/ATVs popular but roads are narrow and steep. Taxis are scarce."
- grok: "Buses, taxis, rentals, ATVs"

## 34. `cities[Santorini].facts.airport`
- claude: "Santorini (Thira) National Airport (JTR)"
- deepseek: "Santorini (Thira) National Airport (JTR)"
- gemini: "Santorini Thira International Airport (JTR)"
- grok: "Santorini Airport (JTR)"

## 35. `cities[Mykonos].facts.how_to_get_there`
- claude: "Ferry from Piraeus (~3–5h) or ~40-min flight from Athens. Two ports: Old Port (near town) and New Port (most big ferries); confirm which."
- deepseek: "Ferry from Piraeus (2.5–5 hours) or Rafina; high-speed options. Domestic flights from Athens (40 minutes)."
- gemini: undefined
- grok: "Fly to JMK or ferry"

## 36. `cities[Mykonos].facts.local_transport`
- claude: "Buses connect town to main beaches; taxis scarce and pricey — pre-book transfers. Sea taxis link beach clubs in summer."
- deepseek: "Buses connect the town to beaches. ATVs, scooters, and cars are popular; roads are narrow. Water taxis serve some beaches."
- gemini: undefined
- grok: "Buses, taxis, rentals"

## 37. `cities[Mykonos].facts.airport`
- claude: "Mykonos National Airport (JMK)"
- deepseek: "Mykonos Island National Airport (JMK)"
- gemini: undefined
- grok: "Mykonos Airport (JMK)"

## 38. `cities[Crete].facts.how_to_get_there`
- claude: "~1h flight from Athens to Heraklion (HER) or Chania (CHQ); or overnight ferry from Piraeus (~9h). It's big — pick a base or plan to drive."
- deepseek: "Ferry from Piraeus (8–9 hours to Heraklion, overnight options); domestic flights from Athens (50 minutes) to Heraklion (HER) or Chania (CHQ)."
- gemini: undefined
- grok: undefined

## 39. `cities[Crete].facts.local_transport`
- claude: "A rental car is the best way to see Crete; KTEL buses link main towns along the north coast. Distances are large (Chania to Heraklion ~2h drive)."
- deepseek: "Buses connect major cities and sights. Renting a car is highly recommended to explore the island's diverse regions."
- gemini: undefined
- grok: undefined

## 40. `cities[Crete].facts.airport`
- claude: "Heraklion (HER) and Chania (CHQ)"
- deepseek: "Heraklion International Airport 'Nikos Kazantzakis' (HER), Chania International Airport 'Ioannis Daskalogiannis' (CHQ)"
- gemini: undefined
- grok: undefined

## 41. `cities[Naxos].facts.how_to_get_there`
- claude: "Ferry from Piraeus (~4–5h) or short hops from Santorini/Mykonos/Paros; small airport with Athens flights. Central Cyclades hub."
- deepseek: "Ferry from Piraeus (4–6 hours) or from other Cyclades islands; high-speed options. Domestic flights from Athens (40 minutes)."
- gemini: undefined
- grok: undefined

## 42. `cities[Naxos].facts.local_transport`
- claude: "Buses from Naxos Town (Chora) to main beaches and villages; a rental car/ATV opens up the mountain villages. Walkable port town."
- deepseek: "Buses connect the port town to beaches and mountain villages. Car or ATV rental is recommended for exploring."
- gemini: undefined
- grok: undefined

## 43. `cities[Naxos].facts.airport`
- claude: "Naxos Island National Airport (JNX) — small, Athens only"
- deepseek: "Naxos Island National Airport (JNX)"
- gemini: undefined
- grok: undefined

## 44. `cities[Paros].facts.how_to_get_there`
- claude: "Ferry from Piraeus (~3–4.5h) and a major Cyclades connection hub (easy hops to Naxos/Mykonos/Santorini); small airport with Athens flights."
- deepseek: "Ferry from Piraeus (3–5 hours) or from other Cyclades; high-speed options. Domestic flights from Athens (40 minutes)."
- gemini: undefined
- grok: undefined

## 45. `cities[Paros].facts.local_transport`
- claude: "Buses link Parikia (main port), Naoussa, and beaches; ATV/car common. Two main towns: Parikia and prettier Naoussa."
- deepseek: "Buses connect Parikia to Naoussa and beaches. Car/ATV rental is popular."
- gemini: undefined
- grok: undefined

## 46. `cities[Paros].facts.airport`
- claude: "Paros National Airport (PAS) — small, Athens only"
- deepseek: "Paros National Airport (PAS)"
- gemini: undefined
- grok: undefined

Rule on each, write the resolution into facts.json with status "disputed" + a note of who dissented. Unresolvable -> null + _open_questions.