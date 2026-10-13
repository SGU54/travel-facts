**Task A — Errors found**

1. **Do Americans Need a Visa for Vietnam? — incorrect passport arithmetic.**  
   > “Combined with the six-month requirement below, a passport expiring in just over six months clears the border but cannot carry a full 90-day visa.”

   **Vietnam E-Visa: How to Apply Step by Step** repeats the error:
   > “A passport with seven months left cannot carry a 90-day visa, regardless of what you request.”

   Neither conclusion follows from the stated 30-day margin. Ninety days plus thirty days requires approximately four months, not more than seven. `facts.json` contains the same faulty inference; its “verified” label does not make that arithmetic correct. A future start date could change the calculation, but neither example specifies one.

2. **Vietnam E-Visa: How to Apply Step by Step — arrival-date logic is reversed.**  
   > “A delayed connection that pushes your arrival past your visa's start date is a problem you cannot fix from the airport, and the same applies on the way out.”

   Arrival **after the start date**, while still within the validity period, does not itself invalidate the visa. Arrival before validity begins and departure after validity ends are different problems. The sentence manufactures a failure from an ordinary delayed arrival.

3. **Both visa articles — obsolete border-gate count inherited from `facts.json`.**  
   **Do Americans Need a Visa for Vietnam?**
   > “An e-visa works at 42 designated border gates, and that list includes every international airport in Vietnam.”

   **Vietnam E-Visa: How to Apply Step by Step**
   > “The good news for anyone flying is that the approved list covers every international airport in Vietnam — 42 gates in total.”

   Neither the articles nor the fact file is current on the count. Vietnam’s official notice identifies **83 eligible gates: 17 airports, 27 land crossings and 39 seaports**, following Resolution 389/NQ-CP of December 2, 2025. This explicit expansion supersedes the supplied 42-gate figure. The second sentence also makes 42 sound like an airport count. [Cổng thông tin Bộ Ngoại Giao](https://vnembassy-daressalaam.mofa.gov.vn/en/tin-chi-tiet/chi-tiet/viet-nam-bo-sung-41-cua-khau-quoc-te-cho-phep-nguoi-nuoc-ngoai-nhap-canh-xuat-canh-bang-thi-thuc-dien-tu-e-visa-viet-nam-adds-41-international-border-gates-eligible-for-entry-and-exit-with-electronic-visas-e-visas--59736-1241.html?utm_source=chatgpt.com)

4. **Both visa articles — blanket reassurance contradicts their own airport restriction.**  
   **Do Americans Need a Visa for Vietnam?**
   > “For anyone arriving by air, the restriction you may have read about simply does not bite.”

   Later:
   > “Your entry and exit points must match what you selected on the application, so a visa naming Hanoi will not get you through Ho Chi Minh City.”

   **Vietnam E-Visa: How to Apply Step by Step**
   > “The constraint only becomes real if you are crossing overland into Cambodia or Laos, where many crossings are not on the list at all.”

   Airport eligibility and the selected entry port are distinct constraints. These reassurances blur them, despite both articles explicitly asserting that air arrivals remain bound by their selection.

5. **Do Americans Need a Visa for Vietnam? — unsupported expansion year.**  
   > “Vietnam does run a unilateral visa-exemption scheme, and it was expanded again in 2026.”

   The expansion identifiable from the supplied fact file’s Resolution 229/NQ-CP occurred in **2025**, effective August 15, 2025. I found official confirmation of that date, not evidence supporting “expanded again in 2026.” As written, the sentence appears to misdate the referenced expansion. [Cổng thông tin Bộ Ngoại Giao](https://vnembassy-bruxelles.mofa.gov.vn/vi/tin-chi-tiet/chi-tiet/thong-bao-ve-nghi-quyet-cua-chinh-phu-ve-viec-mien-thi-thuc-theo-chuong-trinh-kich-cau-phat-trien-du-lich-59009-1353.html?utm_source=chatgpt.com)

6. **Vietnam E-Visa: How to Apply Step by Step — false claim that every other domain is an intermediary.**  
   > “If a site is not evisa.gov.vn, you are paying someone to type.”

   Vietnam’s Immigration Department identifies **both** `evisa.gov.vn` and `thithucdientu.gov.vn` as official domains. Recommending the first is reasonable; declaring every alternative commercial is false. [National portal on Immigration](https://evisa.immigration.gov.vn/home?_58_struts_action=%2Flogin%2Flogin\&saveLastPath=false\&utm_source=chatgpt.com)

7. **Vietnam E-Visa: How to Apply Step by Step — multiple-entry recommendation does not address the problem described.**  
   > “If your itinerary is still fluid, a multiple-entry visa and a careful look at your exit point is money well spent.”

   Multiple entry addresses leaving and re-entering Vietnam. It does not, on the article’s own account, relax the selected-port requirement or make dates amendable. General itinerary uncertainty alone does not establish a benefit from paying twice the single-entry fee.

8. **Vietnam E-Visa: How to Apply Step by Step — possible airport remedy presented as assured.**  
   > “A mismatch in your name, passport number or date of birth can mean being refused entry on arrival, and the remedy at the airport is paying a travel agency for an expensive visa sponsorship on the spot.”

   `facts.json` and the current State Department wording describe possible refusal and a possible sponsorship expense, not a guaranteed remedy. Here the fact file’s qualified position is better supported and current. [Travel.State.gov](https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Vietnam.html?utm_source=chatgpt.com)

9. **Is Vietnam Safe for Americans? — misleading Western Europe comparison.**  
   > “The State Department places Vietnam at Level 1 — Exercise Normal Precautions, the lowest of its four levels and the same rating it gives most of Western Europe.”

   The Vietnam rating matches the supplied fact file. The added comparison does not: France, Germany, Belgium and Luxembourg, for example, currently carry Level 2 advisories. “Most of Western Europe” is not a sound reassurance as written. [Travel.State.gov](https://travel.state.gov/en/international-travel/travel-advisories/france.html?insider=kopxk-tammy-esteves\&utm_source=chatgpt.com)

10. **Is Vietnam Safe for Americans? — proposed scam defense does not cover its own examples.**  
    > “One habit defuses all of them — agree the number, in dong, before anything starts.”

    The preceding examples include fabricated damage charges at motorbike return. Agreeing the rental price does not resolve a subsequent dispute over pre-existing scratches. The motorbike article itself recognizes the separate need to document damage.

11. **Is Vietnam Safe for Americans? — unsafe absolute crossing instruction.**  
    > “Walk at a slow, constant, predictable pace and do not stop.”

    Predictability is presented as an unconditional command to keep moving, without regard to an approaching vehicle or blocked path. The following sentence compounds that implication:
    > “Traffic flows around you the way water flows around a rock.”

    That analogy cannot establish that drivers will yield or avoid the pedestrian. The paragraph turns a situational technique into an assurance of safety.

12. **Renting a Motorbike in Vietnam: What to Know — insurance possibility becomes certainty.**  
    > “Riding unlicensed is choosing to be uninsured in precisely the scenario most likely to need the insurance.”

    Earlier:
    > “If you are in an accident while riding without a valid licence, the State Department warns that your travel insurance may not pay your medical bills.”

    “May not pay” does not establish universal absence of coverage. `facts.json` preserves that distinction, as does the current State Department source; its qualified formulation is supported. The excerpt also pulls in the opposite direction:
    > “That does not make it legal — and it is your insurance that pays for the gap.”   [Travel.State.gov](https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Vietnam.html?utm_source=chatgpt.com)

13. **Renting a Motorbike in Vietnam: What to Know — unsupported escalation of the injury claim.**  
    > “A motorbike accident is the single most common way a visitor to Vietnam ends up in a hospital, and a serious one can mean a medical evacuation costing well into six figures.”

    The first clause changes **road traffic / serious injury**, as stated in `facts.json`, into **motorbikes / all hospital admissions**. Those are different populations and outcomes. Moreover, the fact file’s own supporting text cites extensive road warnings, not comparative injury statistics. Neither establishes this hospital-admission ranking.

14. **Vietnam Health and Vaccines for Travelers — Japanese encephalitis exclusion is too broad.**  
    > “Japanese encephalitis is aimed at people moving to affected rural areas or spending long periods there, not at a two-week city-and-coast trip.”

    CDC also says to consider vaccination for shorter trips involving relevant outdoor exposure or accommodation without appropriate mosquito protection. Two weeks and “coast” do not independently rule that out. The supplied fact file recognizes activity-dependent recommendations; the article narrows them improperly. [CDC](https://wwwnc.cdc.gov/travel/destinations/traveler/none/vietnam?utm_source=chatgpt.com)

15. **Vietnam Health and Vaccines for Travelers — malaria conclusion exceeds the cited geography.**  
    > “Hanoi, Ha Long Bay, Hoi An, Da Nang and Ho Chi Minh City covers what most first-time visitors actually do, and none of it is a malaria transmission area.”

    Followed by:
    > “A course of prophylaxis for that trip is an expense with no corresponding risk.”

    Ha Long Bay and Hoi An are not in the preceding CDC list of six named cities without transmission. Their absence does **not** prove that prophylaxis is necessary, but that list cannot establish the article’s categorical conclusion. `facts.json` says “essentially no” exposure; the article escalates that to none. [CDC](https://wwwnc.cdc.gov/travel/destinations/traveler/none/vietnam?utm_source=chatgpt.com)

16. **Vietnam Health and Vaccines for Travelers — resistance guidance loses its geographic qualification.**  
    > “Chloroquine and mefloquine resistance is present in Vietnam, so where prophylaxis is warranted the CDC points to atovaquone-proguanil, doxycycline or tafenoquine.”

    In context this implies that mefloquine is excluded wherever prophylaxis is indicated. CDC still lists it for transmission areas outside the specified resistant provinces. The article reproduces an overgeneralization in `facts.json`; the geographically differentiated CDC guidance is the better-supported current position. [CDC](https://wwwnc.cdc.gov/travel/destinations/traveler/none/vietnam?utm_source=chatgpt.com)

17. **Vietnam Health and Vaccines for Travelers — unwarranted assurance about ice.**  
    > “Commercial ice in Vietnam is factory-produced from treated water and is used in essentially every cafe and restaurant, including good street stalls — the cylindrical ice with a hole through the middle is the industrial product.”

    Followed by:
    > “Refusing all ice in Vietnam means refusing iced coffee, which is a significant sacrifice for very little risk.”

    Shape and widespread use do not establish safe water or handling. CDC’s Vietnam guidance specifically warns that ice is often made from unsafe tap water. That does not prove every ice supplier unsafe, but it contradicts this blanket dismissal of the precaution. The safety article repeats the reassurance without establishing the ice’s source. [CDC Yellow Book™](https://www.cdc.gov/yellow-book/hcp/asia/vietnam.html?utm_source=chatgpt.com)

18. **Vietnam Health and Vaccines for Travelers — turnover presented as a hygiene guarantee.**  
    > “A stall with a queue of locals is cooking food that has not been sitting, and high throughput is a better guarantee than any amount of visible tidiness.”

    A queue does not establish when ingredients were prepared, their storage temperature, water safety or cross-contamination controls. High turnover can be useful evidence; the sentence incorrectly treats it as proof and as overriding hygiene.

**Task B — Handoff scoring**

- **Do Americans Need a Visa for Vietnam? — PULL 84/100; TRUST 68/100 — FAIL.** The original visa question is answered, concrete route/stay/re-entry connections create a genuine turn, and “That sequencing — what you book first and what it silently forecloses — is worked out end to end in the complete Vietnam decision manual, alongside the rest of the connected decisions a first Vietnam trip turns on.” points to a system. Trust fails because the passport example manufactures a constraint and “the downside of being the one passenger at the counter without it” adds social fear to an acknowledged regulatory ambiguity. One guide mention.

- **Vietnam E-Visa: How to Apply Step by Step — TRUST 48/100 — FAIL.** One seed sentence and one guide mention, but the promised process is undermined by false date/passport constraints and the unsupported domain claim. “The four mistakes below are what actually cost people their trip.” and “it is quietly the most binding booking of your trip” inflate the stakes beyond a proportional seed. No automatic zero: the answer is not explicitly withheld for purchase.

- **Is Vietnam Safe for Americans? — TRUST 66/100 — FAIL.** “That choice turns out to sit inside a wider set of transport tradeoffs, which the complete Vietnam decision manual works through in sequence.” is a restrained, relevant seed, mentioned once. However, the handoff precedes substantive legal, health and emergency answers, while “the mechanics should alarm anyone from a state where cannabis is legal” explicitly pushes alarm. The absolute scam and crossing assurances also undermine honest proportionality.

- **Renting a Motorbike in Vietnam: What to Know — PULL 88/100; TRUST 62/100 — FAIL.** Legal exposure, insurance, mountain access and transport alternatives produce a genuine connected decision; “Which way those choices should run, and what each one forecloses, is worked out in order in the complete Vietnam decision manual.” sells the system once, after practical answers. Trust fails because “Riding unlicensed is choosing to be uninsured in precisely the scenario most likely to need the insurance.” converts contingent coverage into certainty, reinforced by an unestablished hospital-admission ranking.