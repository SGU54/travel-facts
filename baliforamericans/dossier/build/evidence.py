# evidence.py — the evidence register (references/evidence-contract.md, v1).
# Writes evidence.json and release.json. Imported by build3.py for the claim
# display strings, so the book and the register cannot drift.
#
# Dates: every primary claim records the date the page was actually opened.
# The site's fact layer (travel-facts/baliforamericans/facts.json, promoted
# 2026-10-13) opened the State Department, US Consular Agency, e-visa,
# Love Bali, customs, BPOM, CDC, Bank Indonesia, holiday-decree and provincial
# pages on 2026-10-13; the corpus articles that carry the schedule snapshot,
# the climate normals, the road distances and the travel-guide crossing times
# were published between 2026-10-13 and 2026-10-15 and read for this edition
# on 2026-10-15. No figure in this register was invented by the book.
# ─────────────────────────────────────────────────────────────────────────────
import json, os, glob, datetime as _d

HERE = os.path.dirname(os.path.abspath(__file__))
RELEASE_DATE = "2026-10-15"
EDITION = "2026.10"
PROJECT = "baliforamericans — Bali, in Its Own Time."

def _plus(days, base=RELEASE_DATE):
    return (_d.date.fromisoformat(base) + _d.timedelta(days=days)).isoformat()

STATE  = "https://travel.state.gov/en/international-travel/travel-advisories/indonesia.html"
CONSUL = "https://id.usembassy.gov/bali/"
EVISA  = "https://evisa.imigrasi.go.id/web/visa-selection"
EVISAX = "https://imigrasi.go.id/siaran_pers/2025/05/28/tekan-angka-pelanggaran-keimigrasian-wna-wajib-ke"
FEES   = "https://www.imigrasi.go.id/biaya_imigrasi/index"
LOVE   = "https://lovebali.baliprov.go.id/"
CIRC   = "https://bmc.baliprov.go.id/news/11462"
CUST   = "https://www.beacukai.go.id/barang-penumpang"
CUSTC  = "https://www.beacukai.go.id/faq-impor-pembawaan-uang-tunai"
IMEI   = "https://www.beacukai.go.id/faq-impor-registrasi-imei"
BPOM   = "https://sertifikasicdob.pom.go.id/wasdisobat/faq/"
CDC    = "https://wwwnc.cdc.gov/travel/destinations/traveler/none/indonesia"
CDCJL  = "https://wwwnc.cdc.gov/travel/page/jet-lag"
BI     = "https://www.bi.go.id/id/fungsi-utama/sistem-pembayaran/ritel/kanal-layanan/qris/qris-antarnegara"
SKB    = "https://setneg.go.id/baca/index/inilah_skb_3_menteri_libur_nasional_dan_cuti_bersama_2027"
HINDU  = "https://bimashindu.kemenag.go.id/"
NYEPI  = "https://en.tempo.co/read/2092403/bali-airport-and-toll-roads-to-close-for-24-hours-during-nyepi"
BADUNG = "https://bapenda.badungkab.go.id/"
GIANYAR= "https://pasal.id/peraturan/perda/perda-kab-gianyar-7-2023"
KEMNAKER="https://jdih.kemnaker.go.id/"
UULL   = "https://jdih.kemenkeu.go.id/api/download/fulltext/2009/22TAHUN2009UU.htm"
AAA    = "https://cluballiance.aaa.com/travel/idp/international-drivers-permit-countries"
GRAB   = "https://www.grab.com/global/airport-rides/i-gusti-ngurah-rai-international-airport/"
DOT    = "https://www.transportation.gov/airconsumer/fly-rights"
FC     = "https://www.flightconnections.com/flights-from-denpasar-dps"
OSRM   = "https://router.project-osrm.org/"
SITE   = "https://www.baliforamericans.com/article/"

SOURCES = [
 {"id":"s-state", "kind":"primary", "url":STATE, "checked_at":"2026-10-13",
  "locator":"Travel advisory header; Entry, Exit and Visa Requirements; Safety and Security; Local Laws; Health; Travel and Transportation sections", "scope":"US citizens in Indonesia, including Bali", "label":"US State Department — Indonesia"},
 {"id":"s-consul", "kind":"primary", "url":CONSUL, "checked_at":"2026-10-13",
  "locator":"US Consular Agency Bali page: passport validity and blank pages; emergency passports; enforcement campaign notice; contact number", "scope":"US citizens in Bali", "label":"US Consular Agency, Bali"},
 {"id":"s-evisa", "kind":"primary", "url":EVISA, "checked_at":"2026-10-13",
  "locator":"Visa selection for US passport holders: B1 Tourist (Visa On Arrival); fee; validity; required documents", "scope":"US passport, tourism", "label":"Directorate General of Immigration — e-visa"},
 {"id":"s-evisa-ext", "kind":"primary", "url":EVISAX, "checked_at":"2026-10-13",
  "locator":"Press release of 28 May 2025: photograph and interview required for stay-permit extensions from 29 May 2025", "scope":"visa-on-arrival holders extending", "label":"Directorate General of Immigration — press release"},
 {"id":"s-fees", "kind":"primary", "url":FEES, "checked_at":"2026-10-13",
  "locator":"Immigration fee schedule: visa on arrival; 30-day stay permit", "scope":"all applicants", "label":"Directorate General of Immigration — fees"},
 {"id":"s-love", "kind":"primary", "url":LOVE, "checked_at":"2026-10-13",
  "locator":"Love Bali front page and FAQ: amount, who pays, exemptions, payment methods, once per trip", "scope":"international tourists in Bali", "label":"Bali provincial government — Love Bali"},
 {"id":"s-circular", "kind":"primary", "url":CIRC, "checked_at":"2026-10-13",
  "locator":"Governor's Circular No. 7 of 2025, 'New Order for Foreign Tourists While in Bali': obligations and prohibitions", "scope":"foreign tourists in Bali", "label":"Bali provincial government — Circular 7/2025"},
 {"id":"s-customs", "kind":"primary", "url":CUST, "checked_at":"2026-10-13",
  "locator":"Passenger goods: duty-free value, alcohol, tobacco, e-cigarette allowances; red-channel items; excess destroyed", "scope":"all arriving passengers", "label":"Indonesian Customs — passenger goods"},
 {"id":"s-customs-cash", "kind":"primary", "url":CUSTC, "checked_at":"2026-10-13",
  "locator":"FAQ on carrying cash: declaration threshold and penalty", "scope":"all travellers", "label":"Indonesian Customs — cash declaration"},
 {"id":"s-imei", "kind":"primary", "url":IMEI, "checked_at":"2026-10-13",
  "locator":"FAQ on IMEI registration: the two cases in which a short-stay visitor need not register", "scope":"tourists and business visitors", "label":"Indonesian Customs — IMEI registration"},
 {"id":"s-bpom", "kind":"primary", "url":BPOM, "checked_at":"2026-10-13",
  "locator":"FAQ on bringing medicine for personal use: classes and day limits; prescription; declaration; seizure", "scope":"travellers carrying medicine", "label":"BPOM — medicine for personal use"},
 {"id":"s-cdc", "kind":"primary", "url":CDC, "checked_at":"2026-10-13",
  "locator":"Vaccines and Medicines; Malaria (no transmission in Bali resort areas, Ubud, Gili); Rabies; Zika notice; Avoid bug bites; Food and water", "scope":"all travellers to Indonesia", "label":"CDC Travelers' Health — Indonesia"},
 {"id":"s-cdc-jetlag", "kind":"primary", "url":CDCJL, "checked_at":"2026-10-13",
  "locator":"Jet lag page: shift sleep before travel, daylight after arrival, naps 15–20 minutes, arrive two days before an important event", "scope":"all travellers", "label":"CDC — jet lag"},
 {"id":"s-bi", "kind":"primary", "url":BI, "checked_at":"2026-10-13",
  "locator":"QRIS cross-border page: connected countries and the payment steps", "scope":"foreign QRIS users", "label":"Bank Indonesia — cross-border QRIS"},
 {"id":"s-skb", "kind":"primary", "url":SKB, "checked_at":"2026-10-13",
  "locator":"Joint ministerial decree on 2027 national holidays and collective leave", "scope":"Indonesia, 2027", "label":"State Secretariat — 2027 holiday decree"},
 {"id":"s-hindu", "kind":"primary", "url":HINDU, "checked_at":"2026-10-13",
  "locator":"Directorate of Hindu affairs: 2027 Hindu holiday letter (Nyepi, Galungan, Kuningan)", "scope":"Hindu holidays 2027", "label":"Ministry of Religious Affairs — Hindu holidays 2027"},
 {"id":"s-nyepi", "kind":"secondary", "url":NYEPI, "checked_at":"2026-10-13",
  "locator":"Tempo report of the airport operator's 2026 Nyepi announcement: regular commercial flights halted 06:00–06:00", "scope":"Bali airport, Nyepi 2026", "label":"Tempo — Bali airport on Nyepi"},
 {"id":"s-badung", "kind":"primary", "url":BADUNG, "checked_at":"2026-10-13",
  "locator":"Badung regency revenue office circular: 10% local tax on restaurants and hotels; 40% entertainment category from January 2024", "scope":"Badung regency", "label":"Badung regency — local tax"},
 {"id":"s-gianyar", "kind":"secondary", "url":GIANYAR, "checked_at":"2026-10-13",
  "locator":"Gianyar regency regulation 7/2023 as published: 10% on restaurants and hotels; entertainment category", "scope":"Gianyar regency", "label":"Gianyar regency — regulation 7/2023"},
 {"id":"s-kemnaker", "kind":"primary", "url":KEMNAKER, "checked_at":"2026-10-13",
  "locator":"Manpower ministry guidance on hotel service charges: distributed to workers, no fixed percentage", "scope":"hotels and hotel restaurants", "label":"Ministry of Manpower — service charge"},
 {"id":"s-uull", "kind":"primary", "url":UULL, "checked_at":"2026-10-13",
  "locator":"Law 22/2009 on road traffic: licence classes; penalties for riding without the required licence; helmets", "scope":"all drivers in Indonesia", "label":"Law 22/2009 on Road Traffic"},
 {"id":"s-aaa", "kind":"primary", "url":AAA, "checked_at":"2026-10-13",
  "locator":"AAA country list: Indonesia honours the International Driving Permit", "scope":"US licence holders", "label":"AAA — IDP countries"},
 {"id":"s-grab", "kind":"primary", "url":GRAB, "checked_at":"2026-10-13",
  "locator":"Grab airport page: GrabCar Lounge at the International Arrival Terminal; vehicle options", "scope":"Bali airport pickups", "label":"Grab — Ngurah Rai airport"},
 {"id":"s-dot", "kind":"primary", "url":DOT, "checked_at":"2026-10-13",
  "locator":"Fly Rights: connections, baggage transfer between airlines, Montreal Convention Article 19", "scope":"US air passengers", "label":"US Department of Transportation — Fly Rights"},
 {"id":"s-schedule", "kind":"secondary", "url":FC, "checked_at":"2026-10-15",
  "locator":"Schedule snapshot for Denpasar, October 2026: nonstop origins and approximate durations", "scope":"international routes into Bali", "label":"Schedule snapshot — flights into Denpasar"},
 {"id":"s-corpus-distances", "kind":"corpus", "url":SITE+"bali-traffic-real-drive-times", "checked_at":"2026-10-15",
  "locator":"Sections 'The distances, in miles', 'From Ubud' and 'The long ones': road-network distances the site measured and publishes; no drive times", "scope":"Bali road distances", "label":"baliforamericans.com — real drive times (distances)"},
 {"id":"s-corpus-time", "kind":"corpus", "url":SITE+"best-time-to-visit-bali", "checked_at":"2026-10-15",
  "locator":"Sections 'Bali's two seasons' and 'Month by month': Denpasar station normals in inches", "scope":"south Bali rainfall normals", "label":"baliforamericans.com — best time to visit"},
 {"id":"s-corpus-surf", "kind":"corpus", "url":SITE+"surfing-in-bali-by-season-and-coast", "checked_at":"2026-10-15",
  "locator":"Sections on the dry-season west coast and the wet-season east coast, citing surf guides", "scope":"surf coast by season", "label":"baliforamericans.com — surfing by season and coast"},
 {"id":"s-corpus-boats", "kind":"corpus", "url":SITE+"when-bali-fast-boats-cancel", "checked_at":"2026-10-15",
  "locator":"Harbour-master sailing approvals, the May 2023 wave forecast, the 5 August 2025 capsizing, the buffer, all as reported by the state news agency and travel guides", "scope":"Sanur–Nusa and Bali–Lombok crossings", "label":"baliforamericans.com — when fast boats cancel"},
 {"id":"s-corpus-crossing", "kind":"corpus", "url":SITE+"fast-boats-to-nusa-penida-and-lembongan", "checked_at":"2026-10-15",
  "locator":"Crossing times from Sanur as travel guides give them; ports; wet landing", "scope":"Nusa crossings", "label":"baliforamericans.com — fast boats to Nusa Penida and Lembongan"},
 {"id":"s-corpus-gili", "kind":"corpus", "url":SITE+"bali-to-gili-fast-boat-vs-flight", "checked_at":"2026-10-15",
  "locator":"Padang Bai crossing of about an hour and a half; Lombok airport to Bangsal by road", "scope":"Bali–Gili routes", "label":"baliforamericans.com — Bali to the Gilis"},
 {"id":"s-corpus-domestic", "kind":"corpus", "url":SITE+"indonesia-domestic-flights-baggage-and-changes", "checked_at":"2026-10-15",
  "locator":"Baggage by airline service group under Regulation PM 185/2015, as reported by Indonesian legal and business press", "scope":"Indonesian domestic flights", "label":"baliforamericans.com — domestic flights"},
 {"id":"s-corpus-batur", "kind":"corpus", "url":SITE+"mount-batur-sunrise-trek", "checked_at":"2026-10-15",
  "locator":"Climb time from Toya Bungkah, summit height and the guide requirement, citing travel guides", "scope":"Mount Batur trek", "label":"baliforamericans.com — Mount Batur sunrise trek"},
 {"id":"s-corpus-days", "kind":"corpus", "url":SITE+"how-many-days-in-bali", "checked_at":"2026-10-15",
  "locator":"Section 'What each length gives you': the site's own estimate of good days by nights", "scope":"trip length from the US", "label":"baliforamericans.com — how many days"},
]

def claim(id, text, scope, authority, volatility, topic, sources, book=None, sheet=None,
          critical=True, value=None, assumptions=None, survey=None, as_of="2026-10-13", stable=False,
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
 # ── entry ──
 claim("visa-required", "US passport holders need a visa for Indonesia; the B1 tourist visa (visa on arrival / e-VOA) gives 30 days, extendable once for 30 more; it can be bought online in advance or at the airport.",
  "US ordinary passport, tourism", "official", "changeable", "legal", ["s-state","s-evisa"],
  book="A US passport needs a visa for Bali: the B1 tourist visa, bought online in advance or at the airport, which gives thirty days, extendable once for another thirty.",
  sheet="Visa: required. B1 tourist visa (visa on arrival = e-VOA, same product), 30 days, extendable once for 30. Buy on the official site after flights and the final passport, or at the airport counter."),
 claim("visa-fee", "The B1 tourist visa (visa on arrival / e-VOA) costs IDR 500,000, set in rupiah.",
  "US passport, e-visa, official portal", "official", "changeable", "fare", ["s-evisa","s-fees"],
  value={"amount":"500000","unit":"IDR/visa"},
  sheet="Visa fee: 500000 IDR, same online or at the counter; the dollar amount moves with the rate. Online: Visa, Mastercard, JCB; one application covers up to five travellers. A higher price means an agency."),
 claim("visa-90", "Once issued, the e-VOA is valid for entry for 90 days; the application asks for a departure date and a booked return flight.",
  "US passport, e-VOA", "official", "changeable", "admission", ["s-evisa"],
  sheet="e-VOA validity for entry: 90 days from issue, so it can be bought well ahead; the form asks for a departure date and a booked return flight."),
 claim("visa-ext", "The visa on arrival can be extended once for 30 days by online application and payment; since 29 May 2025 the applicant must also attend an immigration office for a photograph and an interview; the fee is IDR 500,000 per application.",
  "visa-on-arrival holders", "official", "changeable", "admission", ["s-evisa-ext","s-fees"],
  book="The visa can be extended once, for another thirty days, by an online application and, since 29 May 2025, a photograph and an interview at an immigration office.",
  sheet="Extension: once, 30 days; online application and payment, then a photograph and interview at an immigration office (since 29 May 2025). Fee 500000 IDR per application. No official processing time is published: the site's margin is to file about two weeks before day 30."),
 claim("overstay", "Overstaying can bring a fine of IDR 1,000,000 per day, with possible detention, deportation or a ban on returning.",
  "all visa holders", "official", "changeable", "legal", ["s-state"],
  value={"amount":"1000000","unit":"IDR/day"},
  book="Overstaying is fined by the day, at a rate twice the cost of the extension itself, with possible detention, deportation or a ban on returning.",
  sheet="Overstay: 1000000 IDR per day (State Dept), with possible detention, deportation or a ban. Thirty days is counted from the stamp, not rounded; read the date on the record before leaving the desk."),
 claim("passport-6m", "A US passport must be valid for at least six months beyond the arrival date and have two blank pages; the endorsement pages do not count; an emergency passport cannot use the visa on arrival.",
  "US passport holders", "official", "stable", "admission", ["s-state","s-consul"], stable=True,
  book="A US passport must be valid for at least six months beyond the arrival date and have two blank visa pages, and the endorsement pages at the back do not count.",
  sheet="Passport: six months beyond the landing date; two blank VISA pages (endorsement pages do not count). An emergency or limited-validity passport cannot use the visa on arrival: apply at an embassy before travel."),
 claim("onward", "Immigration can ask for an outbound ticket from Indonesia; a domestic flight does not satisfy it.",
  "US passport, tourism", "official", "stable", "admission", ["s-state","s-evisa"], stable=True,
  sheet="Onward ticket: immigration can ask for a ticket out of Indonesia; a domestic hop to Lombok does not count. Carry the booking offline."),
 claim("same-passport", "A traveller must leave Indonesia on the passport used to enter; a replacement passport needs a special pass from immigration before departure.",
  "all travellers", "official", "stable", "admission", ["s-state"], stable=True,
  sheet="Leaving: on the same passport you entered with. A passport replaced during the trip needs a special pass from immigration before you can fly; allow time. US Consular Agency, Jimbaran: +62-361-958-6161."),
 claim("levy", "Bali's tourist levy is IDR 150,000 per person, paid once per trip, cashless, through the province's Love Bali system; a tourist who has not paid can be refused service at attractions under Governor's Circular 7/2025.",
  "international tourists in Bali", "official", "changeable", "fare", ["s-love","s-circular"],
  value={"amount":"150000","unit":"IDR/person"},
  book="Bali's tourist levy is a provincial charge, separate from the visa, paid once per trip and cashless on the province's own site; under the governor's 2025 circular a tourist who has not paid can be refused service at attractions.",
  sheet="Levy: 150000 IDR per person, once per trip (a Lombok or Gili side trip stays inside it). Pay at lovebali.baliprov.go.id by card (Visa, Mastercard, Amex, JCB) before you fly; voucher QR by email, one per traveller, saved offline. No cash anywhere. Exemptions are by visa type; none for children found."),
 claim("arrival-card", "Every traveller submits the All Indonesia arrival card (immigration, customs and health in one), free, within 72 hours before arrival; the site refuses earlier submissions; the QR code is shown to immigration and customs.",
  "all arriving travellers", "official", "changeable", "admission", ["s-state","s-evisa"],
  book="Every traveller submits Indonesia's All Indonesia arrival card, free, within the seventy-two hours before arrival; the site refuses earlier submissions, and the QR code it produces is shown to immigration and customs.",
  sheet="Arrival card (All Indonesia): free; opens only within 72 h of the LOCAL arrival date; one per traveller including infants; carries the customs and health declaration; QR code to immigration and customs. A site that charges is not the official one."),
 claim("customs", "Per adult per arrival: personal goods to USD 500 duty-free; 1 litre of alcohol (21+); 200 cigarettes or 25 cigars or 100 g tobacco; 30 ml open-system or 12 ml closed-system vape liquid (18+); alcohol, tobacco or vapes above the allowance are destroyed on the spot; medicines and cash at or above the threshold are red-channel items.",
  "all arriving travellers", "official", "changeable", "legal", ["s-customs"],
  book="The allowances per adult are goods to five hundred US dollars, one litre of alcohol at twenty-one or over, two hundred cigarettes, and thirty millilitres of open or twelve of closed vape liquid.",
  sheet="Customs, per adult: USD 500 of goods duty-free (10% duty + VAT above); 1 L alcohol (21+); 200 cigarettes / 25 cigars / 100 g; vape liquid 30 ml open or 12 ml closed (18+). EXCESS ALCOHOL, TOBACCO AND VAPES ARE DESTROYED, NOT TAXED. Duty-free bought at the hub counts. Medicine → red channel with the prescription."),
 claim("cash-declare", "Cash or other payment instruments worth IDR 100,000,000 or more, or the foreign-currency equivalent, must be declared on entry and exit; the penalty for not declaring is 10% up to IDR 300,000,000; taking that much rupiah out needs a Bank Indonesia permit.",
  "all travellers", "official", "changeable", "legal", ["s-customs-cash"],
  value={"amount":"100000000","unit":"IDR"},
  book="Cash or other payment instruments worth a hundred million rupiah or more, or the equivalent, must be declared on entry and exit; it is a declaration duty, not a limit.",
  sheet="Cash declaration: 100000000 IDR or equivalent, in and out; undeclared penalty 10%, max 300000000 IDR. Taking that much RUPIAH out needs a Bank Indonesia permit. Spend or change small notes before leaving."),
 claim("phone", "Indonesian customs does not require IMEI registration from a short-stay visitor who roams on a home SIM or uses an Indonesian SIM registered at an operator's outlet, which gives network access for up to 90 days.",
  "tourists and business visitors", "official", "stable", "legal", ["s-imei"], stable=True,
  sheet="Phone: no IMEI registration for a tourist roaming on a US SIM or using a local SIM registered at an operator's outlet (90 days' access). A foreign travel eSIM is the site's reading of the roaming case, not a customs statement. The phone must be unlocked for either."),
 # ── medicine and law ──
 claim("meds", "BPOM allows medicine for personal use in baggage with a prescription: ordinary prescribed medicine up to 90 days' use, psychotropic medicine up to 60 days, narcotic-class medicine and precursors not at all; over-the-counter products for at most three days' need; non-compliant medicine can be seized and destroyed.",
  "travellers carrying medicine", "official", "changeable", "legal", ["s-bpom"],
  book="Indonesia's food and drug agency allows up to ninety days of prescribed medicine with a prescription, sixty days of psychotropic medicine, and no narcotic-class medicine at all, with or without a prescription.",
  sheet="Medicine: prescribed, 90 days with the prescription; psychotropic, 60 days; NARCOTIC CLASS, NONE (prescription or not); over-the-counter, three days' need. Original packaging, prescription per item, a letter by generic name. Declare it on the arrival card; the red channel is where it is looked at. BPOM publishes a contact for individual questions."),
 claim("adhd", "The State Department says some prescription medications, including those for ADHD, are illegal in Indonesia, and that the customs office does not share a list of prohibited drugs.",
  "US travellers with prescriptions", "official", "changeable", "legal", ["s-state"],
  book="The State Department says some prescription medications, including those for ADHD, are illegal in Indonesia, and that customs publishes no list of prohibited drugs.",
  sheet="ADHD and other stimulants: the State Dept says some, including ADHD medicines, are illegal; no official list exists. Ask your doctor which class your drug is in and what you would switch to."),
 claim("cbd", "Marijuana, cannabis and CBD products are illegal in Indonesia with no exception for medical use or a product bought legally in a US state; the Narcotics Law puts cannabis in Class I; convictions can bring heavy fines, long sentences and in extreme cases the death penalty.",
  "all travellers", "official", "stable", "legal", ["s-state"], stable=True,
  book="Marijuana, cannabis and CBD products are illegal in Indonesia, with no exception for a product bought legally in a US state, and convictions can bring heavy fines, long sentences and in extreme cases the death penalty.",
  sheet="Cannabis and CBD: illegal in every form, Class I under the Narcotics Law; importing carries 5–15 years and, above 1 kg of plant or 5 g in other forms, life or death. Check jacket pockets and toiletry bags before packing."),
 claim("licence", "A US driver's licence alone is not recognised in Indonesia; foreign drivers must carry an International Driving Permit; Law 22/2009 requires a licence matching the type of vehicle driven and treats motorcycles as a separate class.",
  "US licence holders in Indonesia", "official", "stable", "legal", ["s-state","s-uull","s-aaa"], stable=True,
  book="A US driver's licence alone is not recognised in Indonesia and foreign drivers must carry an International Driving Permit; Indonesian law requires a licence matching the type of vehicle driven, and motorcycles are a class of their own.",
  sheet="Driving: US licence alone not recognised; carry an IDP (AAA, issued at home) WITH the licence. Motorcycles are a separate licence class: an IDP translates a car licence and adds nothing. The site's reading: no motorcycle endorsement = unlicensed on a scooter."),
 claim("licence-fine", "Law 22/2009 sets a maximum of four months' detention or a fine of IDR 1,000,000 for riding without the required licence, with lower maxima for not carrying a licence and for riding without a helmet.",
  "all drivers in Indonesia", "official", "stable", "legal", ["s-uull"], stable=True,
  book="The traffic law sets a maximum of four months' detention or a fine of a million rupiah for riding without the required licence, with lower maxima for not carrying one and for riding without a helmet.",
  sheet="Riding unlicensed: up to 4 months' detention or 1000000 IDR (statutory maxima, not a roadside price). Helmets required for rider and passenger. If fined: ask for an official receipt (State Dept)."),
 claim("presumed", "In collisions between cars and motorcycles the driver of the larger vehicle is often presumed responsible; drivers involved in an accident should stay at the scene and notify the police.",
  "drivers in Indonesia", "official", "stable", "legal", ["s-state"], stable=True,
  book="in a collision between a car and a motorcycle the driver of the larger vehicle is often presumed responsible, and the guidance after any accident is to stay at the scene and notify the police.",
  sheet="After an accident: stay at the scene, notify the police; the larger vehicle's driver is often presumed responsible. The police report is what a claim will ask for."),
 claim("circular", "Governor's Circular 7/2025 requires foreign tourists to stay in licensed accommodation, dress modestly at sacred places, keep out of a temple's inner and middle courtyards unless praying in Balinese dress, use licensed changers and pay in rupiah, hold a valid licence and helmet if riding, pay the levy, and not use single-use plastics; residents report violations to a provincial hotline.",
  "foreign tourists in Bali", "official", "changeable", "legal", ["s-circular"],
  sheet="Circular 7/2025: licensed accommodation only; modest dress at sacred places; inner and middle temple courtyards for worshippers in Balinese dress only; licensed changers, pay in rupiah; licence + helmet to ride; pay the levy; no single-use plastics; roadworthy registered hire cars. Residents report via a WhatsApp hotline."),
 claim("enforcement", "The US Consular Agency in Bali reports a current enforcement campaign by police, immigration, transport and tourism officials, with stepped-up attention to traffic violations, visa violations and drug possession by foreigners.",
  "US citizens in Bali", "official", "changeable", "legal", ["s-consul"],
  sheet="Enforcement: the US Consular Agency reports an active campaign on traffic and vehicle violations, illegal work and visa violations, and drug possession by foreigners. The rules above are being applied."),
 # ── safety and health ──
 claim("advisory", "The State Department's advisory for Indonesia, including Bali, is Level 2, Exercise Increased Caution, citing natural disasters, unrest and terrorism; Level 4 applies to two provinces in Papua.",
  "US citizens", "official", "changeable", "other", ["s-state"],
  book="The State Department places Indonesia, Bali included, at Level 2, Exercise Increased Caution, citing natural disasters, unrest and terrorism; its strongest warning applies to two provinces in Papua, far from Bali.",
  sheet="Travel advisory: Level 2 — Exercise Increased Caution (Indonesia as a whole; Level 4 for two Papua provinces). Read it again before you fly; advisories are revised."),
 claim("medical-pay", "Hospitals and doctors in Indonesia often require payment or a sizable deposit before treatment; most providers accept only cash; most US health plans, Medicare and Medicaid do not pay abroad; a traveller with supplemental insurance is responsible for seeking reimbursement.",
  "US citizens needing care in Indonesia", "official", "stable", "other", ["s-state"], stable=True,
  book="Hospitals and doctors often require payment or a sizable deposit before treatment, most accept only cash, most US health plans, Medicare and Medicaid pay nothing abroad, and a traveller with supplemental insurance pays first and claims afterwards.",
  sheet="Care: deposit before treatment, mostly cash; US plans, Medicare and Medicaid pay nothing abroad; insurance reimburses from the medical report, itemised bill, proof of payment and police report. Ask the clinic for an estimate; no price is printed here because none is official."),
 claim("ambulance", "Ambulance services are not widely available and can take 45 minutes or longer; travellers may prefer a taxi or private vehicle; emergency numbers 112 (unified), 110 police, 119 ambulance, 113 fire; the State Department also gives 118 for medical emergencies.",
  "all travellers", "official", "stable", "other", ["s-state"], stable=True,
  book="Ambulances are not widely available and can take forty-five minutes or longer, so a taxi or private vehicle may be the faster way to a hospital.",
  sheet="Emergency: 112 unified (free, works without credit) · 110 police · 119 ambulance (State Dept also lists 118) · 113 fire. Ambulances can take 45 min or more: a taxi is the ambulance. Ask your accommodation on day one which clinic it would send a guest to."),
 claim("evacuation", "The US government strongly recommends supplemental insurance covering medical evacuation; an injured traveller will likely need to travel to a major city for appropriate care; patients must cover all costs of transfer to or between hospitals.",
  "US citizens in Indonesia", "official", "stable", "other", ["s-state"], stable=True,
  book="the US government strongly recommends supplemental insurance covering medical evacuation, an injured traveller will likely need to reach a major city, and patients pay all costs of transfer to or between hospitals.",
  sheet="Evacuation: strongly recommended by the State Dept; transfers between hospitals are the patient's cost. Read what triggers it, who decides and where it takes you; check the scooter, diving, trekking and boat clauses by name."),
 claim("rabies", "The CDC says dogs infected with rabies are commonly found in Indonesia; rabies vaccines are typically available after an exposure; any bite or scratch should be washed and seen immediately; pre-travel vaccination depends on activities and access to treatment.",
  "all travellers", "official", "changeable", "other", ["s-cdc"],
  book="The CDC says dogs infected with rabies are commonly found in Indonesia and its instruction after any bite or scratch is to seek medical attention immediately.",
  sheet="Rabies: common in Indonesia's dogs. After ANY bite or scratch: soap and running water, then a clinic the same day, and call the insurer. Pre-travel vaccine: a doctor's decision for remote travel, small children or long stays."),
 claim("malaria", "The CDC reports no malaria transmission in the resort areas of Bali, in Ubud, or in the Gili Islands; dengue is a risk throughout Indonesia, its mosquitoes bite by day and night, and no dengue vaccine is available in the United States.",
  "all travellers", "official", "changeable", "other", ["s-cdc"],
  book="The CDC reports no malaria transmission in the resort areas of Bali, in Ubud or in the Gili Islands, and lists dengue as a risk throughout Indonesia.",
  sheet="Malaria: none in Bali's resort areas, Ubud or the Gilis (CDC); present elsewhere in Indonesia. Dengue: everywhere, bites by day, no US vaccine; warning signs come 24–48 h AFTER the fever breaks."),
 claim("zika", "The CDC has a Level 2 travel health notice for Zika in Bali, advising all travellers to prevent mosquito bites and sexual transmission during and after travel; anyone pregnant or planning a pregnancy should read it before booking.",
  "all travellers to Bali", "official", "changeable", "other", ["s-cdc"],
  sheet="Zika: CDC Level 2 travel health notice for Bali at this edition. Pregnant or planning: read the current notice and talk to a doctor before booking. Notices change; check the date."),
 claim("vaccines", "No vaccination is required for entry; the CDC recommends routine vaccines and hepatitis A, hepatitis B and typhoid for most travellers to Indonesia; Japanese encephalitis is conditional.",
  "all travellers", "official", "changeable", "other", ["s-state","s-cdc"],
  book="No vaccination is required to enter Indonesia; the CDC recommends routine vaccines and hepatitis A, hepatitis B and typhoid for most travellers.",
  sheet="Vaccines: none required at the border. CDC recommends routine, hepatitis A, hepatitis B and typhoid; Japanese encephalitis only for long or rural stays. Some need spaced doses: 6–8 weeks out."),
 claim("water", "In many areas of Indonesia tap water is not safe to drink; many restaurants and hotels serve tap water unless bottled is requested; the CDC advises brushing teeth with bottled or disinfected water and avoiding ice where water is a concern.",
  "all travellers", "official", "stable", "other", ["s-state","s-cdc"], stable=True,
  book="Tap water in many areas of Indonesia is not safe to drink, many restaurants and hotels serve it unless bottled water is asked for, and the CDC's advice extends the rule to ice and to brushing teeth.",
  sheet="Water: sealed bottled water from a major brand (State Dept); ask for it by name and check the seal; no ice where unsure; brush teeth with bottled water. A filter bottle squares this with the plastics rule."),
 claim("methanol", "The State Department warns of drink poisoning in Indonesia, including alcohol mixed with methanol, and of drink spiking in Bali, Lombok and the Gili Islands; methanol cannot be detected by taste or smell and symptoms may not appear for 1 to 72 hours; antidotes exist and should be given as soon as possible.",
  "all travellers", "official", "stable", "other", ["s-state","s-cdc"], stable=True,
  book="The State Department warns of drink poisoning in Indonesia, including alcohol mixed with methanol, and of drink spiking in Bali, Lombok and the Gilis; methanol cannot be told by taste or smell, and the CDC says its effects may not appear for one to seventy-two hours.",
  sheet="Drinks: methanol poisoning and spiking are both reported (State Dept). Sealed, branded, opened in sight; spirits from a labelled bottle only; nothing from strangers; nothing left unattended. A hangover out of proportion, or any change in vision: hospital, and say methanol."),
 claim("consular", "The US Consular Agency in Bali is in Jimbaran, reachable at +62-361-958-6161; the embassy is in Jakarta.",
  "US citizens", "official", "stable", "other", ["s-consul"], stable=True,
  sheet="US Consular Agency, Jimbaran: +62-361-958-6161 (lost passport, arrest, consular help). Local emergency numbers first for medical or safety emergencies. Embassy: Jakarta."),
 # ── calendar ──
 claim("nyepi-2027", "Nyepi falls on Monday 8 March 2027 by the official holiday decree; mobile data and broadcasts are switched off 06:00–06:00 under a ministerial circular; for Nyepi 2026 the airport halted all regular commercial flights for the same 24 hours; residents and tourists are asked not to leave their accommodation.",
  "Bali, 2027", "official", "changeable", "schedule", ["s-skb","s-hindu","s-nyepi"],
  book="Nyepi falls on Monday 8 March 2027 by Indonesia's official holiday decree; mobile data and broadcasts are switched off from six in the morning for twenty-four hours, and in 2026 the airport halted all regular commercial flights for the same window.",
  sheet="Nyepi 2027: Monday 8 March (2026 was 19 March; 2028 to be decreed). Mobile data, TV and radio off 06:00–06:00; in 2026 the airport halted regular flights for the same 24 h — 2027 hours NOT yet announced at this edition: confirm with your airline. Land a full day before; stay inside your accommodation on the day."),
 claim("holidays-2027", "Indonesia's 2027 decree sets Eid al-Fitr on 10–11 March with collective leave on 9, 12 and 15 March; with Nyepi on the 8th and the weekends, no working day falls between Saturday 6 and Monday 15 March 2027; other 2027 holidays include Chinese New Year 6 Feb, Good Friday 26 Mar, Eid al-Adha 17 May, Vesak 20 May, Independence Day 17 Aug, Christmas 25 Dec.",
  "Indonesia, 2027", "official", "changeable", "schedule", ["s-skb"],
  book="The 2027 decree puts Eid al-Fitr on 10 and 11 March with collective leave on 9, 12 and 15 March, so that no working day falls between Saturday 6 and Monday 15 March.",
  sheet="2027 national holidays near a Bali trip: 1 Jan · 6 Feb Chinese New Year (leave 5) · 8 Mar Nyepi · 10–11 Mar Eid al-Fitr (leave 9, 12, 15) · 26 Mar Good Friday (leave 25) · 1 May · 6 May · 17 May Eid al-Adha (leave 18) · 20 May Vesak (leave 19) · 1 Jun · 6 Jun · 17 Aug · 25 Dec (leave 24). Government offices closed; book rooms early for long weekends."),
 claim("galungan-2027", "Galungan falls on Wednesday 13 January and Wednesday 11 August 2027, with Kuningan on 23 January and 21 August; neither is a national holiday and no official restriction on visitors attaches to them.",
  "Bali, 2027", "official", "changeable", "schedule", ["s-hindu"],
  book="Galungan falls on 13 January and 11 August 2027, with Kuningan ten days after each; neither is a national holiday and no official restriction on visitors attaches to them.",
  sheet="Galungan 2027: 13 Jan and 11 Aug; Kuningan 23 Jan and 21 Aug. Penjor on the roads, families at the temples, no closure; confirm drivers and guides a few days before."),
 # ── getting there ──
 claim("nonstop", "No airline flies nonstop between the United States and Bali; the October 2026 schedule for Denpasar lists dozens of international routes and no US city; the longest nonstop into Bali is from Istanbul at about 13 hours.",
  "scheduled service into Denpasar", "reported", "changeable", "schedule", ["s-schedule"], as_of="2026-10-15",
  book="No airline flies nonstop between the United States and Bali, so every itinerary has at least one connection.",
  sheet="Nonstop US–Bali: none (October 2026 schedule). Every routing connects once; book both flights on one ticket for a first trip."),
 claim("hubs", "Second-leg durations into Bali on the October 2026 schedule: Singapore ~3.5 h (several airlines); Kuala Lumpur, Bangkok, Manila listed; Hong Kong and Taipei ~5–6 h; Tokyo and Seoul ~7–8 h; Dubai and Doha ~10 h; Istanbul ~13 h.",
  "international routes into Bali", "reported", "changeable", "schedule", ["s-schedule"], as_of="2026-10-15",
  book="The October 2026 schedule lists nonstop flights into Bali from Singapore at about three and a half hours, Hong Kong and Taipei at five to six, Tokyo and Seoul at seven to eight, Dubai and Doha at about ten, and Istanbul at about thirteen.",
  sheet="Hubs, second leg into Bali (Oct 2026 snapshot): Singapore ~3.5 h · KL / Bangkok / Manila listed · Hong Kong, Taipei ~5 to 6 h · Tokyo, Seoul ~7 to 8 h · Dubai, Doha ~10 h · Istanbul ~13 h. Routes change by season: search your own dates."),
 claim("timezone", "Bali is on Central Indonesian Time, UTC+8, with no daylight saving: 12 hours ahead of New York in daylight time and 13 in winter; 15 or 16 ahead of Los Angeles.",
  "all travellers", "official", "stable", "geography", ["s-state"], stable=True,
  book="Bali is eight hours ahead of UTC with no daylight saving, which puts it twelve or thirteen hours ahead of New York and fifteen or sixteen ahead of Los Angeles.",
  sheet="Time: UTC+8, no clock change. +12 h on New York in summer, +13 in winter; +15/+16 on Los Angeles. The flight west crosses the date line: count hotel nights from the LOCAL arrival date on the ticket."),
 claim("bags-dot", "The US Department of Transportation ranks itineraries for checked-bag security as nonstop, then through flight, then a connection on one airline, then a connection between two airlines; it advises asking whether bags will be transferred on any two-airline connection, and notes that delay expenses on international itineraries may be claimed under Article 19 of the Montreal Convention.",
  "US air passengers", "official", "stable", "other", ["s-dot"], stable=True,
  book="The Department of Transportation ranks a connection between two different airlines as the least secure arrangement for checked bags, behind a nonstop, a through flight and a connection on one airline, and advises asking whether bags will be transferred.",
  sheet="Two tickets: ask the second airline, before buying, what it does for a passenger stranded by the first airline's delay; assume bags are NOT transferred (collect, enter the hub country, re-check). Delay expenses: a Montreal Convention claim afterwards, with receipts."),
 claim("domestic-bags", "Under Transport Ministry regulation PM 185/2015, as reported by Indonesian legal and business press, a full-service domestic airline includes up to 20 kg of checked baggage in an economy fare, a medium-service airline up to 15 kg, and a no-frills airline may charge for checked bags.",
  "Indonesian domestic flights", "reported", "changeable", "other", ["s-corpus-domestic"], as_of="2026-10-15",
  book="Under Indonesian regulation a full-service airline includes up to twenty kilograms of checked baggage in an economy fare, a medium-service airline up to fifteen, and a no-frills airline may charge for every bag.",
  sheet="Domestic flights: 20 kg full-service / 15 kg medium / no-frills may charge (PM 185/2015 as reported); the fare conditions are the authority. Separate ticket from your international one; never on the same day as the flight home. Different terminals at Denpasar."),
 # ── the island ──
 claim("distances", "Road-network distances measured by the site: airport to Kuta 4 mi, Seminyak 7, Canggu 12, Nusa Dua 8, Sanur 11, Uluwatu 13, Ubud 22, Padang Bai 35, Kintamani 48, Munduk 51, Amed 61, Lovina 62; Ubud to Tegallalang 6, Sanur 14, Canggu 19, Sidemen 22, Kintamani 27, Besakih 27, Uluwatu 34, Munduk 39, Lempuyang 45, Amed 49; Amed to Munduk 93.",
  "Bali road distances", "reported", "stable", "geography", ["s-corpus-distances"], as_of="2026-10-15", stable=True,
  book="The road distances in this book are the site's own, measured on the road network: the airport is about four miles from Kuta, seven from Seminyak, twelve from Canggu, eight from Nusa Dua, eleven from Sanur, thirteen from Uluwatu and twenty-two from Ubud.",
  sheet="Road miles from the airport: Kuta 4 · Seminyak 7 · Nusa Dua 8 · Sanur 11 · Canggu 12 · Uluwatu 13 · Ubud 22 · Padang Bai 35 · Kintamani 48 · Munduk 51 · Amed 61 · Lovina 62. Drive times: none printed; a live map at your hour and day, the night before, and the longer of its answer and your driver's."),
 claim("rain", "Denpasar station climate normals: about 14 inches of rain in January, 11 in February, 9 in March, 4 in April, under 4 in May, under 3 in June, 1 in July, 1.4 in August, 2.5 in September and October, 5 in November, 13 in December; average temperature about 79–83°F in every month.",
  "south Bali, sea level", "reported", "stable", "other", ["s-corpus-time"], as_of="2026-10-15", stable=True,
  book="South Bali's climate normals show about an inch of rain in July and about fourteen in January, with the average temperature between seventy-nine and eighty-three degrees in every month.",
  sheet="Rain, inches, Denpasar normals: Jan 14 · Feb 11 · Mar 9 · Apr 4 · May <4 · Jun <3 · Jul 1 · Aug 1.4 · Sep 2.5 · Oct 2.5 · Nov 5 · Dec 13. 79–83°F all year. Sea level only; Ubud, the mountains and the north are not described. The meteorological agency forecasts each season's start by zone: read it in your travel month."),
 claim("surf-coast", "Surf guides describe the west-facing coast (Canggu to Uluwatu) as best in the dry season, about April to October, when south-east trade winds blow offshore, with the largest swells June to August; and the east-facing coast (Sanur, Nusa Dua, Keramas) as best in the wet season, about November to March, when the wind turns north-west.",
  "Bali surf by season", "reported", "stable", "other", ["s-corpus-surf"], as_of="2026-10-15", stable=True,
  book="Surf guides describe the west-facing coast as best from about April to October and the east-facing coast from about November to March, because the wind reverses between the seasons.",
  sheet="Surf: west coast and the Bukit April–October (biggest swells June–August); east coast (Keramas, Sanur, Nusa Dua) November–March. A base follows the coast. Beginners: a school chooses the beach and the hour; many Bukit waves break over reef."),
 claim("crossing", "Travel guides put the Sanur crossing at roughly 30 minutes to Nusa Penida and 35–45 minutes to Lembongan (most Lembongan boats a wet landing), Lembongan–Penida about 10 minutes by local boat, Padang Bai–Gili about 1.5 hours (longer from the south; Amed shortest), and the Lombok airport–Bangsal drive at about 1 h 40 to 2 h; none is an official timetable.",
  "Bali island crossings", "reported", "changeable", "schedule", ["s-corpus-crossing","s-corpus-gili"], as_of="2026-10-15",
  book="Travel guides put the crossing from Sanur at roughly thirty minutes to Nusa Penida and thirty-five to forty-five to Lembongan, and the Padang Bai boat to the Gilis at about an hour and a half; none is an official timetable.",
  sheet="Crossings (travel-guide figures, no official timetable): Sanur–Penida ~30 min (Toyapakeh, Buyuk, Sampalan) · Sanur–Lembongan 35–45 min (Jungutbatu or Mushroom Bay; wet landing) · Lembongan–Penida ~10 min · Padang Bai–Gili ~1.5 h, Amed shortest, south ~2.5 h · Lombok airport–Bangsal 1 h 40–2 h by road. Morning boats, in daylight; a named boat and time; a life jacket per seat."),
 claim("strait", "The harbour master's office (KSOP Benoa) issues a sailing approval for each Sanur departure and has told operators not to sail in poor weather; the state news agency reported waves above 2.5 m as the risk line for the route and, on 5 August 2025, a fast boat from Nusa Penida with 75 passengers capsizing at the Sanur harbour entrance with two deaths in waves forecast at 2–4 m; travel guides describe the Bali–Lombok sea as roughest in July and August.",
  "Sanur–Nusa and Bali–Lombok crossings", "reported", "changeable", "other", ["s-corpus-boats"], as_of="2026-10-15",
  book="Travel guides describe the sea between Bali and Lombok as roughest in July and August, when the swells are strongest, and the fast boat that capsized at Sanur in August 2025 was in waves forecast at two to four metres.",
  sheet="The sea: sailing approvals are issued per boat by the harbour master, who holds boats in poor weather; waves above 2.5 m put the Sanur route at risk; a boat capsized at Sanur on 5 Aug 2025 (two deaths). Roughest: July–August. No cancellation rate exists. BUFFER: one full day before an international flight, two in July, August or the wet season."),
 claim("batur", "Travel guides put the Mount Batur climb at about two hours from Toya Bungkah to a summit of about 1,700 m (5,600 ft), with a local guide required from the Association of Mount Batur Trekking Guides; the mountain is an active volcano and access depends on its status.",
  "Mount Batur sunrise trek", "reported", "changeable", "other", ["s-corpus-batur"], as_of="2026-10-15",
  book="Travel guides put the Batur climb at about two hours from Toya Bungkah to a summit of about seventeen hundred metres, with a required local guide from the Association of Mount Batur Trekking Guides.",
  sheet="Batur: ~2 h climb from Toya Bungkah, ~1,700 m, guide required (local association, office in Toya Bungkah); pickup well before dawn, earlier the further south you sleep; cold at the top; an active volcano, so confirm its status the day before. Prices: none printed; ask what the package includes."),
 claim("good-days", "The site's own estimate: 5 nights give about three good days (one base), 7 about five (two bases), 10 about eight (three bases), 14 about twelve (four bases), assuming the first two days slow and the last partly spent leaving.",
  "trips from the US", "judgment", "stable", "other", ["s-corpus-days","s-cdc-jetlag"], as_of="2026-10-15", stable=True,
  assumptions=["the first two days are slow (CDC: two days before anything important)","the last day is partly spent leaving","a base needs three nights"],
  sheet="Nights → good days (the site's estimate): 5 → ~3, one base · 7 → ~5, two · 10 → ~8, three · 14 → ~12, four. Ten nights is the site's recommended first-trip length from the US."),
 # ── money ──
 claim("tax", "In Badung regency (Kuta, Legian, Seminyak, Canggu, Jimbaran, Uluwatu, Nusa Dua) and Gianyar (Ubud) the local tax on restaurant food and drink and on hotel stays is 10%; a service charge at hotels and hotel restaurants is set by the business and must be distributed to staff under a manpower regulation; the 2023 regulations set a 40% rate on bars, nightclubs, karaoke and spas from January 2024, which was publicly contested and may have been amended.",
  "Badung and Gianyar regencies", "official", "changeable", "fare", ["s-badung","s-gianyar","s-kemnaker"],
  value={"amount":"10","unit":"percent"},
  book="In Badung regency, which covers Kuta, Seminyak, Canggu, Jimbaran, Uluwatu and Nusa Dua, the local tax on restaurant food and drink and on hotel stays is ten percent, and Gianyar, which includes Ubud, sets the same rate.",
  sheet="On the bill: 10% local tax on food, drink and rooms in Badung and Gianyar (Denpasar's rate not sourced; Sanur: read the menu). Service charge: the business's own rate, to staff by regulation. Entertainment (bars, clubs, spas): 40% set from Jan 2024, contested and possibly amended — read how the venue states prices."),
 claim("qris", "Bank Indonesia's cross-border QRIS scheme connects Thailand, Malaysia, Singapore, Japan, South Korea and China; the United States is not included, so a US banking app or wallet cannot pay a QRIS code.",
  "foreign QRIS users", "official", "changeable", "other", ["s-bi"],
  book="Bank Indonesia's cross-border QR scheme connects Thailand, Malaysia, Singapore, Japan, South Korea and China, and the United States is not among them.",
  sheet="QRIS: not usable from a US banking app (connected: Thailand, Malaysia, Singapore, Japan, South Korea, China). Cards and rupiah cash are the two methods. The official sites take Visa, Mastercard, JCB (visa) and Amex too (levy); charged in rupiah."),
 claim("changer", "Governor's Circular 7/2025 tells visitors to change money only at authorised changers, bank or non-bank, identified by a licence number and a Bank Indonesia QR-code logo, and to pay in rupiah.",
  "foreign tourists in Bali", "official", "changeable", "legal", ["s-circular"],
  book="Bali's 2025 rules tell visitors to change money only at authorised changers, identified by a licence number and a Bank Indonesia logo with a QR code, and to transact in rupiah.",
  sheet="Changers: licence number + Bank Indonesia QR logo at the counter, or no deal; agree the amount, count it yourself, be the last to touch the stack. ATMs: US cards accepted, fees possible (State Dept); secure locations, check for tampering; no official limit or fee figure exists."),
 claim("atm", "No official source exists for withdrawal limits or operator fees at Bali's ATMs; the figures in travel blogs disagree.",
  "foreign cards at Bali ATMs", "judgment", "changeable", "other", ["s-state"], as_of="2026-10-15",
  assumptions=["the State Department confirms US cards work and fees may apply; the figures are not printed because none is primary-sourced"],
  sheet="ATM fee and cap: not printed — none is primary-sourced. Read the machine's screen; your own bank's foreign schedule is the half you can check before you fly. Decline the dollar offer; pay in rupiah."),
 claim("costs", "The site prints no daily budget and no prices for drivers, SIMs, boats, entrance fees, beach clubs or retreats; where it gives planning ranges they are third-party averages, labelled as such.",
  "all prices in Bali", "judgment", "changeable", "other", ["s-corpus-time"], as_of="2026-10-15",
  assumptions=["prices move with season and rate; the Field Sheet carries only regulated figures"],
  sheet="Prices: confirm in your travel week — a driver's day rate, hours, fuel, parking and stops in writing; entrance fees at the booth, small notes; boat tickets with the cancellation terms; beach-club minimum spends per person or per bed, before or after tax. The book prints none of these, on purpose."),
]

CLAIMS = {c["id"]: c for c in CLAIM_LIST}

CALCULATIONS = [
 {"id":"calc-stack", "operation":"sum", "inputs":[{"claim_id":"visa-fee","quantity":{"amount":"1","unit":"visa"}},{"claim_id":"levy","quantity":{"amount":"1","unit":"person"}}], "result":{"amount":"650000","unit":"IDR"}},
]

DECISIONS_EV = [
 {"id":"d01-nights", "question":"How many nights do you really have, and how many bases do they buy?",
  "when":"planning any first trip from the United States", "action":"count nights on the island from the local arrival date, divide by three for the ceiling on bases: 7 → two, 10 → three, 14 → four",
  "claim_ids":["timezone","nonstop","good-days"],
  "exceptions":[{"condition":"already in Asia and in the time zone", "action":"five nights, one base, is reasonable", "claim_ids":["good-days"]}]},
 {"id":"d02-order", "question":"Which base first, which last, and where does the boat go?",
  "when":"the nights are counted and the places not yet booked", "action":"inland first, the island leg in the middle third with the boat back a full day before the flight, the south coast last",
  "claim_ids":["crossing","strait","timezone","distances"],
  "exceptions":[{"condition":"a late-night arrival", "action":"first night at the shortest drive from the terminal, move inland after breakfast", "claim_ids":["distances"]}]},
 {"id":"d03-month", "question":"Which month, and which coast does it point to?",
  "when":"the dates are open, or fixed by work", "action":"May, June or September if free; otherwise let the month choose the coast and the length, and check March against Nyepi",
  "claim_ids":["rain","surf-coast","strait","nyepi-2027"],
  "exceptions":[{"condition":"a dry-season surf trip to the west coast", "action":"July, with the island leg by air or not at all", "claim_ids":["surf-coast","strait"]}]},
 {"id":"d04-stack", "question":"What does the entry stack commit you to, and in what order?",
  "when":"before any booking", "action":"passport test first; e-VOA on the official site after flights and the final passport; levy from home; arrival card in the last 72 hours; medicine declared",
  "claim_ids":["passport-6m","visa-required","visa-fee","visa-90","visa-ext","overstay","levy","arrival-card","customs","onward","same-passport"],
  "exceptions":[{"condition":"a trip booked at short notice", "action":"buy the visa at the airport counter: same visa, same fee, longer queue", "claim_ids":["visa-required","visa-fee"]},
                {"condition":"a stay past thirty days", "action":"file the extension about two weeks before day 30, from a base near an immigration office, avoiding the holiday clusters", "claim_ids":["visa-ext","overstay","holidays-2027"]}]},
 {"id":"d05-road", "question":"Ride it yourself, ride pillion, or hire the driver?",
  "when":"any journey on the island", "action":"no scooter on a car-only licence; a driver for days out, apps for short hops in the south, pillion on an app bike for a solo short hop",
  "claim_ids":["licence","licence-fine","presumed","medical-pay","evacuation","circular"],
  "exceptions":[{"condition":"a licensed, experienced rider making short local trips in daylight", "action":"rent, with helmet, photographs, a cash deposit and no alcohol", "claim_ids":["licence","circular"]}]},
 {"id":"d06-island", "question":"A day trip, island nights, the Gilis, or none — and where in the trip?",
  "when":"ten nights or more, or a week that wants the cliffs", "action":"three nights on Lembongan with a Penida day, in the middle third, boat back a full day before the flight; a Penida day trip on a week; the Gilis on a fortnight",
  "claim_ids":["crossing","strait","domestic-bags"],
  "exceptions":[{"condition":"the Gilis in July, August or the wet season", "action":"fly via Lombok, back two days before the international flight", "claim_ids":["strait","domestic-bags"]}]},
 {"id":"d07-day", "question":"How many stops does a day hold, and from which base?",
  "when":"every day out", "action":"three or four stops in one direction, grouped by the base they are a short outing from; a live map at the actual hour the night before",
  "claim_ids":["distances","batur"],
  "exceptions":[{"condition":"a transfer day between bases", "action":"stops along the road, ending at a check-in rather than a reservation", "claim_ids":["distances"]}]},
 {"id":"d08-nyepi", "question":"Your dates touch March. Through Nyepi, or around it?",
  "when":"any trip in March, or near the moving dates", "action":"around it on a short trip; through it only on purpose, landing a full day before and sleeping it where you would spend 24 hours",
  "claim_ids":["nyepi-2027","holidays-2027","galungan-2027"],
  "exceptions":[{"condition":"a stay whose first thirty days end in March", "action":"start the extension earlier; the office is shut for most of the cluster", "claim_ids":["holidays-2027","visa-ext"]}]},
 {"id":"d09-flight", "question":"Which hub, one ticket or two, and what hour do you land?",
  "when":"before buying the international ticket", "action":"one ticket; the shortest final leg the home airport allows; a connection that survives an hour's delay; the arrival hour matched to the first night's distance",
  "claim_ids":["nonstop","hubs","timezone","bags-dot","onward","passport-6m"],
  "exceptions":[{"condition":"two tickets priced against a night at the hub", "action":"stop overnight at the hub, confirm entry to that country, carry the second booking", "claim_ids":["bags-dot","onward"]}]},
 {"id":"d10-health", "question":"What breaks the chain: the medicine bag, the deposit, or the policy?",
  "when":"before the trip, in this order", "action":"the medicine's class, the policy's scooter and evacuation clauses, the clinic's address, then the habits",
  "claim_ids":["meds","adhd","cbd","medical-pay","ambulance","evacuation","rabies","malaria","zika","vaccines","water","methanol"],
  "exceptions":[{"condition":"remote travel, small children or a long stay", "action":"ask a doctor about the pre-travel rabies series", "claim_ids":["rabies"]}]},
 {"id":"d11-money", "question":"Which card, how much cash, and where do the small percentages land?",
  "when":"setting up money before and during the trip", "action":"two cards on different networks, one without a foreign fee; rupiah cash counted by the zeros; decline dollar billing; read the foot of the menu; no plan that depends on QR",
  "claim_ids":["qris","changer","tax","cash-declare","atm"],
  "exceptions":[{"condition":"the far side of the island or an island", "action":"carry more cash; the ATM may be a boat away", "claim_ids":["changer"]}]},
]

CONFLICTS = [
 {"id":"x-ambulance-number", "claim_ids":["ambulance"], "source_ids":["s-state","s-consul"], "status":"resolved",
  "resolution":"The State Department's Indonesia page lists 118 and 119 for emergency medical services while the unified line is 112; the book and the sheet print 112, 110, 119 and 113 and note the 118 figure. No action depends on which number is reached first; the instruction is a taxi to the clinic the accommodation named on day one.",
  "resolved_at":"2026-10-15"},
 {"id":"x-nyepi-airport-2027", "claim_ids":["nyepi-2027"], "source_ids":["s-nyepi","s-skb"], "status":"resolved",
  "resolution":"The decree fixes the 2027 date; the airport closure is reported for 2026 and the 2027 hours were not announced at this edition. The book states both as such, the sheet marks the row confirm with your airline, and the instruction (a full day clear of the date, inside your accommodation on the day) holds under any announcement. No action in the book depends on the unannounced hours.",
  "resolved_at":"2026-10-15"},
 {"id":"x-entertainment-tax", "claim_ids":["tax"], "source_ids":["s-badung","s-gianyar"], "status":"resolved",
  "resolution":"The 40% rate was set by the 2023 regulations and publicly contested after January 2024; neither regency's current position could be confirmed from a primary page. The book and the sheet state the rate as set and contested and instruct the reader to read the venue's own pricing; the 10% restaurant and hotel rate, which the decisions turn on, is not in dispute.",
  "resolved_at":"2026-10-15"},
]

# ── the Field Sheet rows: (group, label, claim id, source url, what it reverses) ──
SHEET_ROWS = [
 ("Entry", "Visa", "visa-required", STATE, "Decision 04: the thirty-day outer edge."),
 ("Entry", "Visa fee", "visa-fee", FEES, ""),
 ("Entry", "e-VOA validity", "visa-90", EVISA, "Before you fly: buy after the flights and the final passport."),
 ("Entry", "Extension", "visa-ext", EVISAX, "Decision 04 and 08: the office visit, and the holiday clusters."),
 ("Entry", "Overstay", "overstay", STATE, "Decision 04."),
 ("Entry", "Passport", "passport-6m", CONSUL, "Before you fly: renew first."),
 ("Entry", "Onward ticket", "onward", STATE, "Decision 09: a one-way into Bali needs its second booking."),
 ("Entry", "Leaving", "same-passport", STATE, ""),
 ("Entry", "Tourist levy", "levy", LOVE, "Decision 04: the second system; carried to the temple gate."),
 ("Entry", "Arrival card", "arrival-card", STATE, "Decision 04: the step that cannot be done early."),
 ("Entry", "Customs", "customs", CUST, "Decision 04: duty-free bought at the hub counts."),
 ("Entry", "Cash declaration", "cash-declare", CUSTC, "Decision 11."),
 ("Entry", "Phone", "phone", IMEI, ""),
 ("Medicine and law", "Medicine", "meds", BPOM, "Decision 10: the first link."),
 ("Medicine and law", "ADHD and stimulants", "adhd", STATE, "Decision 10."),
 ("Medicine and law", "Cannabis and CBD", "cbd", STATE, "The risk chapter."),
 ("Medicine and law", "Driving", "licence", STATE, "Decision 05."),
 ("Medicine and law", "Riding unlicensed", "licence-fine", UULL, "Decision 05."),
 ("Medicine and law", "After an accident", "presumed", STATE, "Decision 05 and 10: the police report."),
 ("Medicine and law", "Bali's rules", "circular", CIRC, "The set pieces: temples, changers, accommodation."),
 ("Medicine and law", "Enforcement", "enforcement", CONSUL, "The risk chapter."),
 ("Safety and health", "Advisory", "advisory", STATE, "The risk chapter."),
 ("Safety and health", "Care and billing", "medical-pay", STATE, "Decision 10: the third link."),
 ("Safety and health", "Emergency numbers", "ambulance", STATE, ""),
 ("Safety and health", "Evacuation", "evacuation", STATE, "Decision 10: the clause to read first."),
 ("Safety and health", "Rabies", "rabies", CDC, "Decision 10: the decision made at home."),
 ("Safety and health", "Malaria and dengue", "malaria", CDC, "Before you fly."),
 ("Safety and health", "Zika", "zika", CDC, "Before you fly."),
 ("Safety and health", "Vaccines", "vaccines", CDC, "Before you fly: the clinic deadline."),
 ("Safety and health", "Water", "water", STATE, ""),
 ("Safety and health", "Drinks", "methanol", STATE, "The risk chapter."),
 ("Safety and health", "US Consular Agency", "consular", CONSUL, ""),
 ("Calendar", "Nyepi 2027", "nyepi-2027", SKB, "Decision 08, and every flight within a day of it."),
 ("Calendar", "National holidays 2027", "holidays-2027", SKB, "Decision 08 and 04: offices shut in the clusters."),
 ("Calendar", "Galungan 2027", "galungan-2027", HINDU, "Decision 08."),
 ("Getting there", "Nonstop", "nonstop", FC, "Decision 09."),
 ("Getting there", "Hubs", "hubs", FC, "Decision 09: the shortest final leg."),
 ("Getting there", "Time", "timezone", STATE, "Decision 01: the calendar day lost."),
 ("Getting there", "Two tickets", "bags-dot", DOT, "Decision 09."),
 ("Getting there", "Domestic flights", "domestic-bags", SITE+"indonesia-domestic-flights-baggage-and-changes", "Decision 06: the Lombok route."),
 ("The island", "Road miles", "distances", SITE+"bali-traffic-real-drive-times", "Decision 02 and 07; the last night's drive."),
 ("The island", "Nights and good days", "good-days", SITE+"how-many-days-in-bali", "Decision 01."),
 ("The island", "Rain", "rain", SITE+"best-time-to-visit-bali", "Decision 03."),
 ("The island", "Surf coast", "surf-coast", SITE+"surfing-in-bali-by-season-and-coast", "Decision 03: the base follows the coast."),
 ("The island", "Crossings", "crossing", SITE+"fast-boats-to-nusa-penida-and-lembongan", "Decision 06."),
 ("The island", "The sea and the buffer", "strait", SITE+"when-bali-fast-boats-cancel", "Decision 02 and 06: where the boat sits."),
 ("The island", "Batur", "batur", SITE+"mount-batur-sunrise-trek", "Decision 07."),
 ("Money", "On the bill", "tax", BADUNG, "Decision 11."),
 ("Money", "QRIS", "qris", BI, "Decision 11: cards and cash only."),
 ("Money", "Changers and ATMs", "changer", CIRC, "Decision 11."),
 ("Money", "ATM fee and cap", "atm", STATE, "Decision 11: the rule stands whatever the figure."),
 ("Money", "Prices", "costs", "", "Every decision that names a booking."),
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
    rel = {"schema_version": 1, "title": "Bali, in Its Own Time.", "edition": EDITION,
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
