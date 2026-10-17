# evidence.py — the evidence register (references/evidence-contract.md, v1).
# Writes evidence.json and release.json. Imported by build3.py for the claim
# display strings, so the book and the register cannot drift.
#
# Dates: every primary claim records the date the page was actually opened.
# The site's fact layer (travel-facts/vietnamforamericans/facts.json) opened the
# State Department, US Embassy, e-visa FAQ, CDC, customs and government-portal
# pages on 2026-10-12; the State Department page and the e-visa FAQ were
# re-opened for this edition on 2026-10-14. The airline's route page and the
# government's Tết announcement were read on 2026-10-14.
# ─────────────────────────────────────────────────────────────────────────────
import json, os, glob, datetime as _d

HERE = os.path.dirname(os.path.abspath(__file__))
RELEASE_DATE = "2026-10-17"
EDITION = "2026.10"
PROJECT = "vietnamforamericans — Vietnam, End to End."

def _plus(days, base=RELEASE_DATE):
    return (_d.date.fromisoformat(base) + _d.timedelta(days=days)).isoformat()

STATE = "https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Vietnam.html"
EMB   = "https://vn.usembassy.gov/vietnamese-visas-and-entry-exit/"
EVISA = "https://evisa.gov.vn/faq"
PREARR= "https://prearrival.immigration.gov.vn/"
GATES = "https://en.baochinhphu.vn/viet-nam-adds-41-international-border-gates-for-e-visa-holders.htm"
CUST  = "https://www.customs.gov.vn/index.jsp?pageId=2311&id=84471&cid=4203"
CDC   = "https://wwwnc.cdc.gov/travel/destinations/traveler/none/vietnam"
VNA   = "https://www.vietnamairlines.com/en-vn/direct-flights-from-the-us-to-vietnam"
TET   = "https://vietnamnews.vn/society/1801150/holiday-schedules-for-vietnamese-culture-day-lunar-new-year-national-day-approved.html"
DSVN  = "https://dsvn.vn/"
# v4 (2026-10-17) sources — read for the site's fact layer on the dates given
LAW36 = "https://english.luatvietnam.vn/an-ninh-trat-tu/law-on-road-traffic-order-and-safety-2024-no-36-2024-qh15-360844-d1.html"
LAW47 = "https://english.luatvietnam.vn/law-no-47-2014-qh13-on-entry-exit-transit-and-residence-of-foreigners-in-vietnam-87925-doc1.html"
DEC82 = "https://english.luatvietnam.vn/decree-no-82-2015-nd-cp-dated-september-24-2015-of-the-government-prescribing-visa-exemption-for-overseas-vietnamese-and-foreigners-who-are-spouses-98640-doc1.html"
SBV32 = "https://english.luatvietnam.vn/circular-no-32-2013-tt-nhnn-dated-december-26th-2013-of-the-state-bank-of-vietnam-on-guiding-the-implementation-of-regulations-on-restricting-the-use-83764-doc1.html"
FCDO  = "https://www.gov.uk/foreign-travel-advice/vietnam/safety-and-security"
STATE2= "https://travel.state.gov/en/international-travel/travel-advisories/vietnam.html"
KHMFA = "https://recberlin.mfaic.gov.kh/en-us/border-crossings"
HNT   = "https://hanoitimes.vn/ha-long-hai-phong-expressway-officially-opens-to-traffic-470.html"
VOH   = "https://voh.com.vn/xa-hoi/tam-dung-toan-bo-tau-du-lich-tren-vinh-ha-long-do-bao-so-3-606096.html"
OXAL  = "https://oxalisadventure.com/cave/son-doong-cave/"
SITE  = "https://www.vietnamforamericans.com/article/"

SOURCES = [
 {"id":"s-state-entry", "kind":"primary", "url":STATE, "checked_at":"2026-10-14",
  "locator":"Entry, Exit and Visa Requirements section", "scope":"US passport holders entering Vietnam", "label":"US State Department — Vietnam country information"},
 {"id":"s-state-safety", "kind":"primary", "url":STATE, "checked_at":"2026-10-14",
  "locator":"Travel advisory header; Safety and Security; Local Laws; Transportation; Health sections", "scope":"US citizens in Vietnam", "label":"US State Department — Vietnam country information"},
 {"id":"s-embassy", "kind":"primary", "url":EMB, "checked_at":"2026-10-12",
  "locator":"Vietnamese visas and entry/exit page: e-visa fees; temporary residence registration", "scope":"US passport holders", "label":"US Embassy Hanoi"},
 {"id":"s-evisa-faq", "kind":"primary", "url":EVISA, "checked_at":"2026-10-14",
  "locator":"FAQ: validity of the e-visa; passport validity rule", "scope":"all e-visa applicants", "label":"Vietnam Immigration Department e-visa FAQ"},
 {"id":"s-prearrival", "kind":"primary", "url":PREARR, "checked_at":"2026-10-12",
  "locator":"Portal front page: purpose and timing of the declaration", "scope":"foreign passport holders arriving by air", "label":"Pre-Arrival Information portal"},
 {"id":"s-gates", "kind":"primary", "url":GATES, "checked_at":"2026-10-12",
  "locator":"Government portal news item on Resolution 389/NQ-CP, 3 December 2025", "scope":"e-visa entry gates", "label":"Vietnam Government Portal"},
 {"id":"s-customs", "kind":"primary", "url":CUST, "checked_at":"2026-10-12",
  "locator":"Duty-free allowances quoting Decree 134/2016/ND-CP Article 6", "scope":"all arriving travellers", "label":"Vietnam Customs Department"},
 {"id":"s-cdc", "kind":"primary", "url":CDC, "checked_at":"2026-10-12",
  "locator":"Vaccines and Medicines table; malaria transmission areas", "scope":"all travellers", "label":"CDC Travelers' Health — Vietnam"},
 {"id":"s-vna", "kind":"primary", "url":VNA, "checked_at":"2026-10-14",
  "locator":"Direct flights from the US to Vietnam page: 'The only direct flight from the U.S. to Vietnam provided by Vietnam Airlines is the flight from San Francisco'", "scope":"scheduled nonstop US–Vietnam service", "label":"Vietnam Airlines"},
 {"id":"s-tet", "kind":"secondary", "url":TET, "checked_at":"2026-10-14",
  "locator":"Viet Nam News report of Government Office Document No 10065/VPCP-KGVX approving the 2027 holiday schedule", "scope":"Vietnam public holidays 2027", "label":"Viet Nam News — holiday schedules approved"},
 {"id":"s-corpus-train", "kind":"corpus", "url":SITE+"reunification-express-train-guide", "checked_at":"2026-10-14",
  "locator":"Sections 'What the route actually is' and 'The one leg worth planning around'", "scope":"Reunification line journey times", "label":"vietnamforamericans.com — the Reunification Express"},
 {"id":"s-corpus-hue", "kind":"corpus", "url":SITE+"hue-to-hoian-how-to-travel", "checked_at":"2026-10-14",
  "locator":"Section 'By train to Da Nang, then car'", "scope":"Huế–Đà Nẵng rail", "label":"vietnamforamericans.com — Huế to Hội An"},
 {"id":"s-dsvn", "kind":"primary", "url":DSVN, "checked_at":"2026-10-14",
  "locator":"Vietnam Railways booking site (timetable lookup); no fixed schedule page is published", "scope":"rail timetables and fares", "label":"Vietnam Railways"},
 # ── v4 ──
 {"id":"s-law36", "kind":"primary", "url":LAW36, "checked_at":"2026-10-17",
  "locator":"Law 36/2024/QH15 on Road Traffic Order and Safety: Art 9 (prohibited acts), Art 11(4)(c) (red signal), Art 33(2) (helmets)", "scope":"all road users in Vietnam", "label":"Law on Road Traffic Order and Safety 2024 (LuatVietnam English text)"},
 {"id":"s-law47", "kind":"primary", "url":LAW47, "checked_at":"2026-10-17",
  "locator":"Law 47/2014/QH13 Art 33: declaration of temporary residence by the accommodation establishment", "scope":"foreigners staying overnight in Vietnam", "label":"Law on Entry, Exit, Transit and Residence of Foreigners 2014"},
 {"id":"s-dec82", "kind":"primary", "url":DEC82, "checked_at":"2026-10-17",
  "locator":"Decree 82/2015/ND-CP Arts 2, 3, 4, 6, 7, 8, 10", "scope":"overseas Vietnamese and their foreign spouses and children", "label":"Decree 82/2015 on visa exemption for overseas Vietnamese"},
 {"id":"s-sbv32", "kind":"primary", "url":SBV32, "checked_at":"2026-10-17",
  "locator":"Circular 32/2013/TT-NHNN Arts 3–4: restricting the use of foreign exchange in Vietnam", "scope":"pricing and payment inside Vietnam", "label":"State Bank of Vietnam Circular 32/2013"},
 {"id":"s-fcdo", "kind":"primary", "url":FCDO, "checked_at":"2026-10-17",
  "locator":"Safety and security: 'Methanol poisoning' and 'Drink spiking' paragraphs", "scope":"visitors buying alcoholic drinks in Vietnam", "label":"UK FCDO — Vietnam travel advice"},
 {"id":"s-state-2026", "kind":"primary", "url":STATE2, "checked_at":"2026-10-17",
  "locator":"Entry, exit and visa requirements: 'You must enter and exit Vietnam on the same passport'; Traveling with minors: notarized consent for Vietnamese minors", "scope":"US citizens, including dual nationals and their children", "label":"US State Department — Vietnam (2026 page)"},
 {"id":"s-khmfa", "kind":"primary", "url":KHMFA, "checked_at":"2026-10-17",
  "locator":"Border crossings table: e-visa accepted at Bavet; Kaam Samnor, Prek Chak and Phnom Den not listed for e-visa", "scope":"entry to Cambodia from Vietnam", "label":"Royal Embassy of Cambodia (Berlin) — border crossings"},
 {"id":"s-hnt", "kind":"primary", "url":HNT, "checked_at":"2026-10-17",
  "locator":"Report of the Hạ Long–Hải Phòng expressway and Bạch Đằng bridge opening, 1 September 2018", "scope":"Hanoi–Hạ Long road", "label":"Hanoi Times"},
 {"id":"s-voh", "kind":"secondary", "url":VOH, "checked_at":"2026-10-17",
  "locator":"Report of the Quảng Ninh waterways port authority suspending every tourist vessel on Hạ Long Bay for storm No 3", "scope":"Hạ Long Bay tourist vessels", "label":"VOH — Hạ Long Bay suspension notice"},
 {"id":"s-oxalis", "kind":"primary", "url":OXAL, "checked_at":"2026-10-17",
  "locator":"Sơn Đoòng cave expedition page: duration, price, grade", "scope":"Sơn Đoòng expeditions", "label":"Oxalis Adventure (operator)"},
]

def claim(id, text, scope, authority, volatility, topic, sources, book=None, sheet=None,
          critical=True, value=None, assumptions=None, survey=None, as_of="2026-10-12", stable=False,
          valid_from=None, calculation_id=None):
    c = {"id": id, "text": text, "scope": scope, "authority": authority,
         "volatility": volatility, "topic": topic, "status": "verified",
         "sources": sources, "as_of": as_of,
         "recheck_by": _plus(700 if stable else 85, as_of), "critical": critical,
         "display": {}}
    if book: c["display"]["book"] = book
    if sheet: c["display"]["sheet"] = sheet
    if value: c["value"] = value
    if assumptions: c["assumptions"] = assumptions
    if valid_from: c["valid_from"] = valid_from
    if calculation_id: c["calculation_id"] = calculation_id
    return c

CLAIM_LIST = [
 claim("visa-required",
  "A visa is required for US passport holders and must be obtained before travel; the exception is a stay of 30 days or less on Phú Quốc, arriving and leaving the island directly.",
  "US ordinary passport holders, tourism", "official", "changeable", "legal", ["s-state-entry"], as_of="2026-10-14",
  book="A US passport needs a visa, applied for before you travel; the one exception is a stay of thirty days or fewer on Phú Quốc, arriving and leaving the island directly.",
  sheet="Visa: required for a US passport; apply before travel. Exception: 30 days or fewer on Phú Quốc only, arriving and leaving directly."),
 claim("visa-fee-single", "The single-entry e-visa fee is USD 25.", "US passport, e-visa, official portal", "official", "changeable", "fare", ["s-embassy"],
  value={"amount":"25","unit":"USD/visa"},
  sheet="E-visa, single entry: 25 USD, paid by bank transfer on the official portal."),
 claim("visa-fee-multi", "The multiple-entry e-visa fee is USD 50.", "US passport, e-visa, official portal", "official", "changeable", "fare", ["s-embassy"],
  value={"amount":"50","unit":"USD/visa"},
  sheet="E-visa, multiple entry: 50 USD, paid by bank transfer on the official portal."),
 claim("visa-fee", "The e-visa costs USD 25 for a single entry or USD 50 for multiple entries, payable by bank transfer.",
  "US passport, e-visa, official portal", "official", "changeable", "fare", ["s-embassy"],
  value={"amount":"25","unit":"USD/visa"},
  book="The e-visa costs twenty-five dollars for a single entry or fifty for multiple entries, paid by bank transfer on the official site, evisa.gov.vn, and nowhere else.",
  sheet="E-visa fee: 25 USD single entry / 50 USD multiple entry; bank transfer; official portal evisa.gov.vn only."),
 claim("visa-90", "E-visa validity runs up to 90 days, and Vietnam usually grants the period requested rather than the maximum.",
  "US passport, e-visa", "official", "changeable", "admission", ["s-evisa-faq","s-state-entry"], as_of="2026-10-14",
  book="Validity runs up to ninety days, and the period granted is usually exactly the one you asked for.",
  sheet="E-visa validity: up to 90 days; the period granted is normally the period requested."),
 claim("visa-processing", "E-visa applications are usually processed within 3 to 5 working days after the Immigration Department receives the completed application and payment; this may change with application volume or holidays.",
  "US passport, e-visa", "official", "changeable", "schedule", ["s-state-entry"], as_of="2026-10-14",
  book="Processing usually takes three to five working days once the Immigration Department has the completed application and the payment, and longer during surges and holidays.",
  sheet="E-visa processing: usually 3–5 working days from receipt of application and payment; longer at holidays and surges. Vietnam's embassy in India publishes 5–30 working days: treat 3–5 as a floor."),
 claim("visa-port", "The entry and exit points used must match the ports selected on the e-visa application.",
  "US passport, e-visa", "official", "changeable", "admission", ["s-state-entry"], as_of="2026-10-14",
  book="Your entry and exit points must match the ports you selected on the application.",
  sheet="Ports: the entry and exit points used must match those named on the application."),
 claim("visa-noext", "An e-visa cannot be renewed or extended from inside Vietnam.",
  "US passport, e-visa", "official", "changeable", "admission", ["s-state-entry"], as_of="2026-10-14",
  book="An e-visa cannot be renewed or extended from inside Vietnam.",
  sheet="Extension: none exists for an e-visa; a longer stay means leaving and applying again from outside."),
 claim("visa-gates", "An e-visa is valid at 83 designated gates (17 airports, 27 land crossings, 39 seaports) since Resolution 389/NQ-CP of 2 December 2025, which covers every international airport.",
  "e-visa holders", "official", "changeable", "admission", ["s-gates"],
  book="An e-visa is valid at eighty-three designated gates — seventeen airports, twenty-seven land crossings and thirty-nine seaports — which covers every international airport in the country.",
  sheet="E-visa gates: 83 (17 airports, 27 land, 39 sea) since Resolution 389/NQ-CP, 2 Dec 2025. Every international airport is covered; only some land crossings are."),
 claim("visa-print", "The official instruction is to carry a printed copy of the e-visa with the passport.",
  "US passport, e-visa", "official", "changeable", "admission", ["s-state-entry"], as_of="2026-10-14",
  sheet="Carry a printed e-visa with the passport."),
 claim("declaration", "A pre-arrival declaration is filed online, free, no earlier than three days before arrival; the State Department describes it as required for air arrivals on a non-Vietnamese passport, while Vietnam's own portal presents it as advisory.",
  "non-Vietnamese passport holders arriving by air", "official", "changeable", "admission", ["s-state-entry","s-prearrival"], as_of="2026-10-14",
  book="A separate pre-arrival declaration is filed online, free, within the three days before you land; the State Department calls it required for air arrivals on a foreign passport and Vietnam's own portal calls it advisory.",
  sheet="Pre-arrival declaration: prearrival.immigration.gov.vn, free, filed no earlier than 3 days before arrival. State Dept: required (air arrivals, foreign passport). Vietnam's portal: advisory. File it."),
 claim("passport-6m", "The passport must be valid for six months beyond the arrival date with blank pages for stamps; the State Department page gives both one page per stamp and two blank pages.",
  "US passport holders", "official", "changeable", "admission", ["s-state-entry"], as_of="2026-10-14",
  book="The passport must be valid for six months beyond the arrival date, with blank pages for stamps.",
  sheet="Passport: 6 months' validity beyond arrival; blank pages — the State Dept page says both one per stamp and at least two, so carry two."),
 claim("licence", "US driver's licences and International Driving Permits do not work in Vietnam; driving without a Vietnamese licence can mean a fine, arrest or jail, and renting a moped or motorbike without one is illegal.",
  "US licence holders visiting Vietnam", "official", "stable", "legal", ["s-state-safety"], as_of="2026-10-14", stable=True,
  book="A US driver's licence and an International Driving Permit are both invalid in Vietnam; driving without a Vietnamese licence can mean a fine, arrest or jail, and renting a motorbike without one is illegal.",
  sheet="Driving: US licence and IDP both invalid; renting a motorbike without a Vietnamese licence is illegal; fine, arrest or jail."),
 claim("insurance", "After an accident while riding without a valid licence, travel insurance may not pay medical bills.",
  "US visitors riding unlicensed", "official", "stable", "legal", ["s-state-safety"], as_of="2026-10-14", stable=True,
  book="After an accident without a valid licence, travel insurance may not pay your medical bills.",
  sheet="Insurance: after an accident without a valid licence, the policy may not pay the medical bills."),
 claim("zero-alcohol", "Vietnamese law requires zero alcohol while driving.",
  "anyone driving in Vietnam", "official", "stable", "legal", ["s-state-safety"], as_of="2026-10-14", stable=True,
  book="the law requires zero alcohol while driving, not a threshold.",
  sheet="Drink-driving limit: zero. Cameras and higher fines in Hanoi and Saigon."),
 claim("advisory", "The State Department places Vietnam at Level 1, Exercise Normal Precautions, advisory dated June 24, 2026.",
  "US citizens", "official", "changeable", "other", ["s-state-safety"], as_of="2026-10-14",
  book="The State Department places Vietnam at Level 1, Exercise Normal Precautions, the lowest of its four levels, in an advisory dated June 24, 2026.",
  sheet="Travel advisory: Level 1 — Exercise Normal Precautions (dated 24 June 2026). Re-read before you fly."),
 claim("cash-declare", "There is no limit on currency carried in or out, but more than 15,000,000 VND or more than USD 5,000 in foreign currency must be declared, in both directions.",
  "all travellers", "official", "changeable", "legal", ["s-state-entry"], as_of="2026-10-14",
  value={"amount":"5000","unit":"USD"},
  book="there is no limit on the currency you carry in or out, but anything over fifteen million đồng or five thousand US dollars must be declared, in both directions.",
  sheet="Currency declaration: above 15000000 VND or 5000 USD in foreign currency, on entry and on exit. No limit; a form, not a tax. The 7000 USD figure online traces to a 2005 notice."),
 claim("customs-alcohol", "Duty-free alcohol per entry: 1.5 litres at 20% ABV or above, or 2 litres under 20%, or 3 litres of beer; the limits are alternatives.",
  "all arriving travellers, per entry", "official", "stable", "legal", ["s-customs"], stable=True,
  sheet="Duty-free alcohol, per entry: 1.5 L at ≥20% ABV, or 2 L under 20%, or 3 L of beer — one of the three. A single bottle over by ≤1 L passes whole. Tobacco: 200 cigarettes or 250 g or 20 cigars. Other goods: 10,000,000 VND."),
 claim("vaccines", "No vaccinations are required to enter Vietnam; the CDC recommends Hepatitis A (unvaccinated, age one and over), Hepatitis B (unvaccinated, all ages) and typhoid (most travellers).",
  "all travellers", "official", "changeable", "other", ["s-state-safety","s-cdc"], as_of="2026-10-14",
  book="No vaccination is required to enter Vietnam; the CDC recommends Hepatitis A, Hepatitis B and typhoid for most travellers.",
  sheet="Vaccines: none required at the border. CDC recommends Hep A, Hep B and typhoid for most travellers; Japanese encephalitis and rabies are conditional."),
 claim("malaria", "CDC lists malaria transmission as rural only, with none in Da Nang, Hai Phong, Hanoi, Ho Chi Minh City, Nha Trang or Quy Nhon.",
  "all travellers", "official", "changeable", "other", ["s-cdc"],
  book="transmission is rural only, and the CDC lists none in Hanoi, Saigon, Đà Nẵng, Hải Phòng, Nha Trang or Quy Nhơn.",
  sheet="Malaria: rural only; none in Hanoi, Saigon, Đà Nẵng, Hải Phòng, Nha Trang, Quy Nhơn. Resistance in named provinces; the drug depends on the route — a clinic question."),
 claim("timezone", "Vietnam has a single time zone, UTC+7, with no daylight saving: 12 hours ahead of the US East Coast in Eastern Standard Time and 11 in Eastern Daylight Time.",
  "all travellers", "official", "stable", "geography", ["s-state-safety"], as_of="2026-10-14", stable=True,
  book="Vietnam keeps one time zone, seven hours ahead of UTC with no daylight saving, which puts it twelve hours ahead of the East Coast in winter and eleven in summer.",
  sheet="Time: UTC+7, no daylight saving; +12 h on US Eastern in winter, +11 h in summer."),
 claim("nonstop", "Vietnam Airlines' San Francisco – Ho Chi Minh City flight is the only nonstop between the United States and Vietnam; there is no nonstop to Hanoi.",
  "scheduled US–Vietnam nonstop service", "official", "changeable", "schedule", ["s-vna"], as_of="2026-10-14",
  book="The only nonstop between the United States and Vietnam is Vietnam Airlines' San Francisco to Ho Chi Minh City service, and there is no nonstop to Hanoi.",
  sheet="Nonstop US–Vietnam: Vietnam Airlines SFO–SGN only (about 15–17 h westbound); no nonstop to Hanoi. Days of operation vary by season: check the airline before fixing dates."),
 claim("tet-2027", "Tết falls on 6 February 2027; the official public holiday runs 4–10 February 2027 (Government Office Document No 10065/VPCP-KGVX).",
  "Vietnam, 2027", "reported", "changeable", "schedule", ["s-tet"], as_of="2026-10-14",
  book="In 2027 Tết falls on 6 February, with the official holiday running from 4 to 10 February.",
  sheet="Tết 2027: 6 February; official holiday 4–10 February (Document 10065/VPCP-KGVX). The surge runs about a week either side. 2028 will be announced in 2027 — check."),
 claim("natday-2027", "National Day 2027 runs 2–5 September.", "Vietnam, 2027", "reported", "changeable", "schedule", ["s-tet"], as_of="2026-10-14",
  book="In 2027 National Day runs from 2 to 5 September.",
  sheet="National Day 2027: 2–5 September. Reunification Day and Labour Day: 30 April – 1 May, span announced each year."),
 claim("exit-control", "Leaving Vietnam requires a valid visa, residence card or Immigration Department approval; a traveller unable to leave on time, including for a medical emergency, will likely pay overstay fines and face delays obtaining permission to leave.",
  "US passport holders", "official", "stable", "legal", ["s-state-entry"], as_of="2026-10-14", stable=True,
  book="Vietnam requires a valid visa, a residence card or Immigration Department approval to leave as well as to enter, and if you cannot leave on time for any reason, including a medical emergency, you will likely pay overstay fines and face delays getting permission to go.",
  sheet="Exit: valid status required to leave; overstaying — including for a medical emergency — likely means fines and delays obtaining permission to go."),
 claim("emergency", "Emergency numbers: 113 traffic police, 115 ambulance.", "all travellers", "official", "stable", "other", ["s-state-safety"], as_of="2026-10-14", stable=True,
  book="The emergency numbers are 113 for the traffic police and 115 for an ambulance.",
  sheet="Emergency: 113 traffic police · 115 ambulance · 1900-54-55-70 expressway hotline. Often answered in Vietnamese only."),
 claim("police-reg", "Every visitor must have their overnight address registered with the local police; hotels do this at check-in, hosts of informal stays are responsible.",
  "all visitors", "official", "stable", "legal", ["s-embassy"], stable=True,
  book="every visitor's overnight address must be registered with the local police, which the hotel does from the passport at check-in and a homestay host is responsible for.",
  sheet="Residence registration: every overnight address is registered with the police; hotels do it from your passport, a homestay host must."),
 claim("drugs", "Police sometimes test blood for drugs; substances used legally elsewhere can lead to arrest and a long sentence if detected; ingredients in some common prescriptions, including ADHD medicines, may be illegal.",
  "all travellers", "official", "stable", "legal", ["s-state-safety"], as_of="2026-10-14", stable=True,
  book="Police sometimes test blood for drugs, a substance used legally in another country can still lead to arrest and a long sentence if it is in your system, and ingredients in some common prescriptions, including ADHD medicines, may be illegal here.",
  sheet="Drugs: blood tests happen; a substance used legally abroad can mean arrest; some ADHD and other prescription ingredients are illegal — carry documentation."),
 claim("hue-dn-rail", "The Huế – Đà Nẵng train takes about two and a half to three hours along the coast over the Hải Vân Pass.",
  "Reunification line, Huế–Đà Nẵng", "reported", "changeable", "schedule", ["s-corpus-hue","s-dsvn"], as_of="2026-10-14",
  book="The Huế to Đà Nẵng train runs about two and a half to three hours along the coast and over the Hải Vân Pass, sea side if you ask for it.",
  sheet="Huế–Đà Nẵng by rail: about 2.5–3 h. Timetable and fares: dsvn.vn — confirm in your travel week; book the better carriages a day or two ahead."),
 claim("han-sgn-rail", "The Reunification line runs Hanoi to Ho Chi Minh City in roughly thirty-two to thirty-six hours.",
  "Reunification line, end to end", "reported", "changeable", "schedule", ["s-corpus-train","s-dsvn"], as_of="2026-10-14",
  book="the Reunification line covers Hanoi to Saigon in roughly thirty-two to thirty-six hours.",
  sheet="Hanoi–Saigon by rail: roughly 32–36 h end to end; almost nobody rides it through. Sleeper classes: 4-berth soft, 6-berth hard; berths sold individually."),
 # ── confirm-in-your-travel-week rows: judgments that name where to look ──
 claim("fares-domestic", "No primary fare schedule exists for domestic flights; fares move with date, carrier and the holiday calendar.",
  "domestic air fares", "judgment", "changeable", "other", ["s-vna"], as_of="2026-10-14",
  assumptions=["fares are read live from the carriers at booking; no figure is frozen here"],
  sheet="Domestic fares: confirm in your travel week on the carriers' own sites (Vietnam Airlines, VietJet, Bamboo). The gap between carriers is often smaller than the baggage fee. Reverses nothing in the book; sets the fly-or-train toss-up between 150 and 500 miles."),
 claim("cruise-terms", "Cruise prices, inclusions and cancellation terms are set per operator and change; the port authority decides cancellations.",
  "Hạ Long / Lan Hạ overnight cruises", "judgment", "changeable", "other", ["s-corpus-train"], as_of="2026-10-14",
  assumptions=["terms are read from the operator in writing before booking"],
  sheet="Bay cruises: confirm with the operator, in writing — which bay, cabin count, kayaking included, cave fees, and what happens when the port authority cancels (refund, reschedule, credit). Reverses Decision 06 only if the bay is closed for your dates."),
 claim("atm-structure", "Vietnamese ATMs charge a flat per-withdrawal fee and cap withdrawals; no bank's foreign-card tariff could be verified against a primary source.",
  "foreign cards at Vietnamese ATMs", "judgment", "changeable", "other", ["s-embassy"], as_of="2026-10-14",
  assumptions=["the structure (flat fee, low cap) is corpus-wide and consistent; the figures are not printed because none is primary-sourced"],
  sheet="ATM fee and cap: not printed — no bank's own foreign-card tariff could be verified. Read the machine's screen before confirming; your own bank's foreign charge is the half you can check before you fly."),
 # ── v4 claims, 2026-10-17 ──
 claim("helmets", "Every rider and every passenger on a motorbike, moped or motorised bicycle must wear a helmet to the national standard with the strap fastened (Law 36/2024 Art 33).",
  "all motorbike riders and pillion passengers", "official", "stable", "legal", ["s-law36"], as_of="2026-10-17", stable=True,
  book="every rider and every passenger on a motorbike must wear a helmet with the strap fastened, the pillion included.",
  sheet="Helmets: rider and pillion, strap fastened — Law 36/2024 Art 33. Ask the easy-rider operator what it issues."),
 claim("no-licence-act", "Driving a motor vehicle without the licence the law requires is itself a listed prohibited act under Law 36/2024 Art 9, as is letting an unqualified person drive.",
  "all drivers in Vietnam", "official", "stable", "legal", ["s-law36"], as_of="2026-10-17", stable=True,
  book="under Vietnam's own traffic law, driving without the licence it requires is a listed prohibited act, and so is handing the keys to someone who lacks one."),
 claim("red-light", "A red signal means stop; a right turn on red is lawful only where a supplementary arrow or sign permits it (Law 36/2024 Art 11).",
  "all road users in Vietnam", "official", "stable", "legal", ["s-law36"], as_of="2026-10-17", stable=True,
  book="red means stop here, and a right turn on red is lawful only where an arrow or a sign says so.",
  sheet="Red light: stop; right on red only with a supplementary arrow or sign (Law 36/2024 Art 11). Two 2015–16 guidebooks said the opposite."),
 claim("cambodia-evisa", "A Cambodian e-visa is accepted from Vietnam only at Bavet (the Mộc Bài road crossing); the Kaam Samnor river crossing from Châu Đốc, Prek Chak and Phnom Den are not e-visa gates.",
  "entry to Cambodia from Vietnam on a Cambodian e-visa", "official", "changeable", "admission", ["s-khmfa"], as_of="2026-10-17",
  book="on the Cambodian side an e-visa works only at Bavet, the road crossing on the Saigon–Phnom Penh bus route, so the river exit at Châu Đốc needs a Cambodian visa obtained another way.",
  sheet="Cambodian e-visa: accepted at Bavet (Mộc Bài road crossing) only; the Châu Đốc river post (Kaam Samnor), Hà Tiên (Prek Chak) and Tịnh Biên (Phnom Den) are not e-visa gates. Decision 03 and 08."),
 claim("methanol", "There have been deaths and serious illness from alcoholic drinks containing methanol in Vietnam; cases came from drinks bought in licensed bars, shops and hotels in tourist areas; even small amounts can kill and methanol cannot be identified by taste or smell.",
  "visitors drinking spirits or cocktails in Vietnam", "official", "changeable", "other", ["s-fcdo"], as_of="2026-10-17",
  book="there have been deaths and serious illness in Vietnam from drinks containing methanol, bought in licensed bars, shops and hotels in tourist areas, and methanol cannot be identified by taste or smell.",
  sheet="Methanol: deaths from spirits bought in licensed bars, shops and hotels in tourist areas; taste does not reveal it (UK FCDO). Beer and sealed wine by default; symptoms can arrive a day later as a hangover with blurred vision — a hospital, not sleep."),
 claim("same-passport", "A traveller must enter and exit Vietnam on the same passport, and domestic travel must be done on the passport used for entry.",
  "all travellers, decisive for dual US–Vietnamese nationals", "official", "stable", "legal", ["s-state-2026"], as_of="2026-10-17", stable=True,
  book="you must enter and leave Vietnam on the same passport, and fly domestically on it too.",
  sheet="One passport: enter, fly domestically and exit on the same document. Dual nationals choose before booking."),
 claim("child-exit", "In general a Vietnamese passport or a Vietnamese exit visa is required for a US-citizen child of Vietnamese parentage to exit Vietnam.",
  "US-citizen children of Vietnamese parentage", "official", "stable", "legal", ["s-embassy"], as_of="2026-10-17", stable=True,
  book="a US-citizen child of Vietnamese parentage may need a Vietnamese passport or a Vietnamese exit visa to leave the country, and the requirement attaches to parentage, not to the passport the child arrived on.",
  sheet="Children of Vietnamese parentage: a Vietnamese passport or exit visa may be required to leave; ask the Vietnamese consulate before booking (US Embassy)."),
 claim("minor-consent", "Notarised consent is required for all Vietnamese minors, including dual US citizens, to travel without a parent or guardian; Vietnamese authorities have sometimes blocked US-citizen minors from leaving without it.",
  "Vietnamese minors including dual US citizens", "official", "stable", "legal", ["s-state-2026"], as_of="2026-10-17", stable=True,
  book="a Vietnamese minor, a dual US citizen included, needs notarised consent to travel without a parent or guardian, and children have been stopped at departure without it.",
  sheet="Minors: notarised parental consent for any Vietnamese minor (dual US citizens included) travelling without a parent or guardian; a lone parent carries the other's consent or proof of sole custody."),
 claim("exemption-paper", "Overseas Vietnamese and their foreign spouses and children may apply for a visa-exemption paper valid up to five years, giving a six-month stay on each entry, on proof of Vietnamese origin or of the relationship (Decree 82/2015).",
  "overseas Vietnamese, including Vietnamese Americans, and their spouses and children", "official", "changeable", "admission", ["s-dec82"], as_of="2026-10-17",
  book="an overseas Vietnamese, or the spouse or child of one, can hold a visa-exemption paper valid for up to five years that admits them for six months at a time, on proof of Vietnamese origin or of the relationship.",
  sheet="Visa-exemption paper (Decree 82/2015): overseas Vietnamese and their spouses/children; up to 5 years, 6 months per entry; passport with 1 year left; proof of origin (birth certificate, renunciation or loss-of-nationality papers). Apply at a Vietnamese consulate. Fee set separately — ask."),
 claim("halong-road", "Hanoi to Hạ Long city by road takes about 2.5 hours since the Hạ Long–Hải Phòng expressway and Bạch Đằng bridge opened on 1 September 2018.",
  "Hanoi–Hạ Long road", "reported", "changeable", "schedule", ["s-hnt"], as_of="2026-10-17",
  book="the road from Hanoi to the bay has been about two and a half hours since the expressway opened in 2018, which is the same morning Ninh Bình costs.",
  sheet="Hanoi–Hạ Long by road: about 2.5 h on the expressway (since 2018). Ninh Bình: about 2 h. Guidebooks printed before 2019 still say four."),
 claim("bay-suspension", "When a storm or dangerous weather is forecast the Quảng Ninh waterways port authority stops issuing departure permits to every tourist vessel on Hạ Long Bay, day boats and overnight cruises alike.",
  "Hạ Long Bay tourist vessels", "reported", "stable", "other", ["s-voh"], as_of="2026-10-17", stable=True,
  book="the port authority stops every tourist vessel at once when a storm is forecast, day boats and overnight cruises alike, and the operators can only refund or reschedule.",
  sheet="Bay suspensions: the port authority grounds every tourist vessel at once on a storm forecast; operators refund or reschedule. A two-day window has no room to reschedule into — Decision 06."),
 claim("dong-only", "Inside Vietnam prices, quotes, advertising and payment must be in đồng; pricing or paying in foreign currency is restricted to listed cases such as duty-free shops (SBV Circular 32/2013).",
  "payments inside Vietnam", "official", "stable", "legal", ["s-sbv32"], as_of="2026-10-17", stable=True,
  book="prices, quotes and payment inside Vietnam are in đồng by law, with dollar pricing confined to listed cases such as duty-free shops.",
  sheet="Legal tender: đồng only for prices and payment inside Vietnam (SBV Circular 32/2013); dollar quotes are the exception, not a courtesy."),
 claim("host-reg", "By law the hotel, homestay or host declares a foreign guest's temporary residence to the local police within 12 hours of arrival (24 in remote areas), usually electronically; the statute requires no passport surrender.",
  "foreigners staying overnight in Vietnam", "official", "stable", "legal", ["s-law47"], as_of="2026-10-17", stable=True,
  book="the duty is the host's, within twelve hours of your arrival, and the statute asks for a declaration, not the surrender of the passport.",
  sheet="Residence declaration: the host files it within 12 h (24 h remote), usually online — Law 47/2014 Art 33. No passport surrender is required; a copy and a look are what the desk needs."),
 claim("son-doong", "Hang Sơn Đoòng is visited only on Oxalis Adventure's multi-day expedition, sold as six days and five nights, graded challenging, priced by the operator at VND 80,000,000 (about USD 3,000) per person.",
  "Sơn Đoòng expeditions", "reported", "changeable", "fare", ["s-oxalis"], as_of="2026-10-17",
  value={"amount":"3000","unit":"USD/person"},
  sheet="Sơn Đoòng: Oxalis only; 6 days / 5 nights, graded challenging; operator price about 3000 USD per person (VND 80000000); a day and a half of trekking to the mouth. Places are few and sell out far ahead."),
 claim("hoian-ticket", "Hội An's Ancient Town ticket covers a set number of heritage sites and its validity is reported differently by different visitors.",
  "Hội An Ancient Town entry", "judgment", "changeable", "other", ["s-corpus-hue"], as_of="2026-10-14",
  assumptions=["the booth states the current count and validity"],
  sheet="Hội An Ancient Town ticket: confirm at the booth how many sites it covers and how long it stays valid. The lantern night is the 14th of each lunar month."),
]

CLAIMS = {c["id"]: c for c in CLAIM_LIST}

CALCULATIONS = [
 {"id":"calc-single", "operation":"sum", "inputs":[{"claim_id":"visa-fee-single","quantity":{"amount":"1","unit":"visa"}}], "result":{"amount":"25","unit":"USD"}},
 {"id":"calc-multi",  "operation":"sum", "inputs":[{"claim_id":"visa-fee-multi","quantity":{"amount":"1","unit":"visa"}}], "result":{"amount":"50","unit":"USD"}},
 {"id":"calc-premium","operation":"difference", "inputs":[{"claim_id":"visa-fee-multi","quantity":{"amount":"1","unit":"visa"}},{"claim_id":"visa-fee-single","quantity":{"amount":"1","unit":"visa"}}], "result":{"amount":"25","unit":"USD"}},
]

DECISIONS_EV = [
 {"id":"d01-days", "question":"How many days do you really have, and how many regions do they buy?",
  "when":"planning any first trip from the United States", "action":"count days on the ground (leave minus two crossing days minus the arrival day), then pick adjacent regions: two for seven ground days, three for ten or more",
  "claim_ids":["timezone"],
  "exceptions":[{"condition":"a returning visitor who has already seen the centre", "action":"take the two ends and fly between them", "claim_ids":["timezone"]}]},
 {"id":"d02-season", "question":"Which month, and which end do you start from?",
  "when":"the dates are fixed by work and the ticket is not yet bought", "action":"run the line so the weather-sensitive end comes first; south-first if the SFO nonstop is needed; keep slack in the centre in autumn",
  "claim_ids":["nonstop","tet-2027"],
  "exceptions":[{"condition":"March or April, when all three regions are workable", "action":"treat direction as a tiebreaker only", "claim_ids":["nonstop"]},
                {"condition":"the trip is the centre only", "action":"fly in and out of Đà Nẵng; there is no line to run", "claim_ids":["nonstop"]}]},
 {"id":"d03-visa", "question":"What does the e-visa form commit you to?",
  "when":"before applying on the official portal", "action":"settle the route shape (gates in and out, entries, days with a buffer), then apply single-entry naming the airports actually used",
  "claim_ids":["visa-fee","visa-fee-single","visa-fee-multi","visa-processing","visa-noext","visa-gates","visa-port","declaration","visa-required","visa-90","cambodia-evisa"],
  "comparison":{"basis":"one US adult, one e-visa application on the official portal, government fee only, excluding agent markups and bank charges",
                "options":[{"label":"single entry","calculation_id":"calc-single"},{"label":"multiple entry","calculation_id":"calc-multi"}]},
  "exceptions":[{"condition":"the trip loops out to Cambodia or Laos and back into Vietnam", "action":"apply for multiple entry (USD 50), or a second visa approved from outside before returning, naming the re-entry gate", "claim_ids":["visa-fee-multi","visa-port"]},
                {"condition":"the exit is by river at Châu Đốc or by road at Mộc Bài", "action":"name that crossing as the exit port on the application; for the river exit obtain the Cambodian visa by a route other than the Cambodian e-visa, which Kaam Samnor does not accept", "claim_ids":["visa-port","visa-gates","cambodia-evisa"]},
                {"condition":"the whole trip is Phú Quốc, thirty days or fewer, arriving and leaving the island directly", "action":"no visa is needed", "claim_ids":["visa-required"]}]},
 {"id":"d04-road", "question":"Ride it yourself, ride pillion, or hire the driver?",
  "when":"any leg a visitor might cover by motorbike", "action":"do not rent; ride pillion with an easy-rider on the mountain route, take the train over the pass, a car with driver for regional legs, Grab in cities",
  "claim_ids":["licence","insurance","zero-alcohol","helmets","no-licence-act","red-light"],
  "exceptions":[{"condition":"flat quiet lanes around Hội An or Ninh Bình, with the risk accepted knowingly", "action":"rent a bicycle instead; if a scooter anyway, own helmet with the strap fastened, stop on red, photographs of every scratch, photocopy as deposit, no alcohol", "claim_ids":["licence","zero-alcohol","helmets","red-light"]}]},
 {"id":"d06-north", "question":"The bay, Ninh Bình, or Sapa — which one does the northern leg carry?",
  "when":"a northern leg of four or five days, or a two-day window outside Hanoi", "action":"short leg: Ninh Bình; standard leg: the overnight bay; Sapa only when the mountains are the reason; with two days, let the forecast decide between the boat and the rowboat and keep the other as the same-morning fallback",
  "claim_ids":["halong-road","bay-suspension"],
  "exceptions":[{"condition":"the forecast for the two days shows cloud, wind or a storm warning", "action":"go to Ninh Bình and sleep there; the port authority grounds every boat at once and a two-day window cannot reschedule", "claim_ids":["bay-suspension"]},
                {"condition":"the cruise is cancelled on the morning of departure", "action":"turn the day into a Ninh Bình day trip from the same hotel", "claim_ids":["halong-road","bay-suspension"]}]},
 {"id":"d05-legs", "question":"Fly, train, or sleep through it — leg by leg?",
  "when":"every intercity leg", "action":"fly above ~500 miles, never below ~150, take the Huế–Đà Nẵng train; morning departures on connecting days",
  "claim_ids":["hue-dn-rail","han-sgn-rail"],
  "exceptions":[{"condition":"the destination has no railway (Đà Lạt, Mũi Né, Phong Nha, the delta towns)", "action":"take the bus, by day where possible", "claim_ids":["han-sgn-rail"]},
                {"condition":"daylight hours matter more than the fare on Hanoi–Huế or Hanoi–Lào Cai", "action":"take the overnight train, soft sleeper", "claim_ids":["han-sgn-rail"]}]},
 {"id":"d10-tet", "question":"Your dates touch Tết. Go through it, or around it?",
  "when":"dates within about a week either side of the lunar new year", "action":"move the dates unless there is a reason to be there; if going through, book transport the day the dates are known and carry cash withdrawn in a city",
  "claim_ids":["tet-2027","natday-2027"],
  "exceptions":[{"condition":"a Vietnamese connection, an invitation into a home, or a resort or package stay", "action":"go through it, based in a larger city or resort area, and use the cheaper city hotels", "claim_ids":["tet-2027"]}]},
 {"id":"d11-cash", "question":"How much cash, and where does the card quietly stop?",
  "when":"setting up money before and during the trip", "action":"withdraw the maximum, rarely; decline dynamic currency conversion; carry cash into the countryside",
  "claim_ids":["cash-declare","police-reg","dong-only","host-reg"],
  "exceptions":[{"condition":"the trip stays in the four card cities and sleeps in chain hotels", "action":"rely on the card and carry a modest cash float", "claim_ids":["cash-declare"]},
                {"condition":"leaving overland into Cambodia", "action":"carry small US dollar notes rather than extra đồng", "claim_ids":["cash-declare"]}]},
]

CONFLICTS = [
 {"id":"x-declaration", "claim_ids":["declaration"], "source_ids":["s-state-entry","s-prearrival"], "status":"resolved",
  "resolution":"Both characterisations are published verbatim in the book and the sheet; the instruction given is to file it, which satisfies either reading. No action in the book depends on which government is right.",
  "resolved_at":"2026-10-14"},
 {"id":"x-blank-pages", "claim_ids":["passport-6m"], "source_ids":["s-state-entry","s-state-safety"], "status":"resolved",
  "resolution":"The State Department page states both 'one blank page per stamp' and 'at least two blank pages'; the conservative figure (two) is the instruction, and the inconsistency is stated.",
  "resolved_at":"2026-10-14"},
]

# ── the Field Sheet rows: (group, label, claim id, source url, what it reverses) ──
SHEET_ROWS = [
 ("Entry", "Visa", "visa-required", STATE, "Reverses Decision 03's Phú Quốc exception if the exemption changes."),
 ("Entry", "E-visa fee", "visa-fee", EMB, "Decision 03: the multiple-entry premium is the price of a loop."),
 ("Entry", "Single entry", "visa-fee-single", EMB, ""),
 ("Entry", "Multiple entry", "visa-fee-multi", EMB, ""),
 ("Entry", "Validity", "visa-90", EVISA, "Decision 01 and 03: the ceiling on days."),
 ("Entry", "Processing", "visa-processing", STATE, "Before you fly: the application deadline."),
 ("Entry", "Ports", "visa-port", STATE, "Decision 03 and 08: a river or road exit must be named."),
 ("Entry", "Extension", "visa-noext", STATE, "Decision 03: the duration is final."),
 ("Entry", "Gates", "visa-gates", GATES, "Decision 03: overland crossings are the ones to check."),
 ("Entry", "Print", "visa-print", STATE, ""),
 ("Entry", "Pre-arrival declaration", "declaration", PREARR, ""),
 ("Entry", "Passport", "passport-6m", STATE, "Before you fly."),
 ("Entry", "Leaving", "exit-control", STATE, "Day zero: the last night sleeps near the airport."),
 ("Entry", "One passport", "same-passport", STATE2, "Before you fly: dual nationals."),
 ("Entry", "Children of Vietnamese parentage", "child-exit", EMB, "Before you fly."),
 ("Entry", "Minors travelling without a parent", "minor-consent", STATE2, "Before you fly."),
 ("Entry", "Visa-exemption paper", "exemption-paper", DEC82, "Before you fly: replaces the e-visa for repeat trips by overseas Vietnamese."),
 ("Entry", "Cambodian e-visa gates", "cambodia-evisa", KHMFA, "Decision 03 and 08: the river exit needs a Cambodian visa by another route."),
 ("Money and customs", "Currency declaration", "cash-declare", STATE, "Decision 11."),
 ("Money and customs", "Duty-free", "customs-alcohol", CUST, ""),
 ("Money and customs", "ATM fee and cap", "atm-structure", EMB, "Decision 11: the rule stands whatever the figure."),
 ("Money and customs", "Residence registration", "police-reg", EMB, ""),
 ("Money and customs", "Residence declaration — the law", "host-reg", LAW47, "The host's duty; no passport surrender required."),
 ("Money and customs", "Legal tender", "dong-only", SBV32, "Decision 11: always đồng."),
 ("Safety and health", "Advisory", "advisory", STATE, "The risk chapter."),
 ("Safety and health", "Driving", "licence", STATE, "Decision 04."),
 ("Safety and health", "Insurance", "insurance", STATE, "Decision 04."),
 ("Safety and health", "Alcohol", "zero-alcohol", STATE, "Decision 04."),
 ("Safety and health", "Helmets", "helmets", LAW36, "Decision 04: the pillion too."),
 ("Safety and health", "Red light", "red-light", LAW36, "Decision 04."),
 ("Safety and health", "Methanol", "methanol", FCDO, "The risk chapter."),
 ("Safety and health", "Vaccines", "vaccines", CDC, "Before you fly: the clinic deadline."),
 ("Safety and health", "Malaria", "malaria", CDC, "Before you fly: prophylaxis depends on the route."),
 ("Safety and health", "Drugs", "drugs", STATE, "The risk chapter."),
 ("Safety and health", "Emergency numbers", "emergency", STATE, ""),
 ("Transport", "Nonstop from the US", "nonstop", VNA, "Decision 02: south-first if the nonstop is needed."),
 ("Transport", "Time zone", "timezone", STATE, "Decision 01: the calendar day lost."),
 ("Transport", "Huế–Đà Nẵng rail", "hue-dn-rail", DSVN, "Decision 05: the one leg never worth flying."),
 ("Transport", "Hanoi–Saigon rail", "han-sgn-rail", DSVN, "Decision 05: fly above five hundred miles."),
 ("Transport", "Domestic fares", "fares-domestic", VNA, ""),
 ("Transport", "Bay cruises", "cruise-terms", "", ""),
 ("Transport", "Hanoi–Hạ Long road", "halong-road", HNT, "Decision 06: the bay and Ninh Bình cost the same morning."),
 ("Transport", "Bay suspensions", "bay-suspension", VOH, "Decision 06: the forecast rule."),
 ("Transport", "Sơn Đoòng", "son-doong", OXAL, "The middle: a trip, not a stop."),
 ("Calendar", "Tết", "tet-2027", TET, "Decision 10, and every transport booking in the window."),
 ("Calendar", "Other holidays", "natday-2027", TET, "Decision 10."),
 ("Calendar", "Hội An ticket and lantern night", "hoian-ticket", "", "Decision 07."),
]

def write():
    ev = {"schema_version": 1, "project": PROJECT, "release_date": RELEASE_DATE,
          "sources": SOURCES, "claims": CLAIM_LIST, "decisions": DECISIONS_EV,
          "calculations": CALCULATIONS,
          "field_sheet": {"checked_at": RELEASE_DATE,
                          "claim_ids": [r[2] for r in SHEET_ROWS]},
          "conflicts": CONFLICTS}
    json.dump(ev, open(os.path.join(HERE, "evidence.json"), "w"), ensure_ascii=False, indent=1)
    assets = sorted(os.path.relpath(p, HERE) for p in glob.glob(os.path.join(HERE, "fonts", "*.woff2")))
    assets += sorted(os.path.relpath(p, HERE) for p in glob.glob(os.path.join(HERE, "img", "A*.jpg")))
    rel = {"schema_version": 1, "title": "Vietnam, End to End.", "edition": EDITION,
           "release_date": RELEASE_DATE, "purpose": "publication", "evidence": "evidence.json",
           "review": "review.json",
           "documents": [
             {"id": "book", "template": "book.template.html", "html": "_book.html", "pdf": "dossier.pdf",
              "critical_json": "book-critical.json", "page_size_pt": [612, 792]},
             {"id": "sheet", "template": "sheet.template.html", "html": "_sheet.html", "pdf": "fieldsheet.pdf",
              "critical_json": "sheet-critical.json", "page_size_pt": [612, 792]}],
           "assets": assets}
    json.dump(rel, open(os.path.join(HERE, "release.json"), "w"), ensure_ascii=False, indent=1)
    print(f"evidence.json: {len(SOURCES)} sources, {len(CLAIM_LIST)} claims, {len(DECISIONS_EV)} decisions, "
          f"{len(CALCULATIONS)} calculations, {len(CONFLICTS)} conflicts; sheet rows {len(SHEET_ROWS)}")
    print(f"release.json: {len(assets)} assets")

if __name__ == "__main__":
    write()
