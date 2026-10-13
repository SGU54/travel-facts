#!/usr/bin/env python3
"""Batch A — 5 seasonal-timing depth articles for japanforamericans.

Written against facts.json depth_facts.seasonal (merged 2026-09-16 from a 3-member
panel, disputes ruled against official sources). Every article carries exactly ONE
vein piece: seasonal-timing. Rail-pass and IC-card vocabulary is deliberately kept
out of these articles — naming three vein pieces inside a 2-sentence window is the
pre-join failure the guide is sold against.

Image slots are scaffolding. They MUST be converted to real <figure> tags at upload
(4-publishing.md 3.5) or the images ship invisible.
"""
import json, re, os

A = []

# ─────────────────────────────────────────────────────────────── 1. TURN
A.append({
 "slug": "cherry-blossom-season-japan",
 "title": "Cherry Blossom Season in Japan: When to Go and What It Costs",
 "category_slug": "when-to-go",
 "excerpt": "Japan's bloom window is roughly a week long and moves north across the country. Here's the regional timetable, what the season does to prices, and why no one can promise you a date.",
 "featured_image": "japanforamericans/articles/cherry-blossom-season-japan-hero",
 "content": """<p>Cherry blossom season is the single most requested time to visit Japan, and also the hardest to plan, because the thing you are travelling for does not keep a schedule. The bloom moves north across the country over several weeks, but in any one city it lasts about a week. This guide covers where the blossom lands and when, what the season does to what you pay, and how to book around a date that nobody can guarantee.</p>

<h2>When the blossom actually arrives</h2>
<p>Cherry blossom reaches full bloom in Kyushu in late March, in Tokyo, Kyoto and Osaka from late March into the first days of April — most often somewhere around 28 March to 5 April — in Tohoku in mid to late April, and in Hokkaido from late April into early May. The pattern moves south to north and from low ground upward.</p>

<h3>The rough regional timetable</h3>
<p>Working from that gradient, a first trip usually targets the Tokyo–Kyoto corridor in the first days of April. Both cities sit in the same broad window, and they are close enough that a week spanning the turn of the month gives you a real chance in at least one of them. Travelling further north buys you a second attempt: if Tokyo has already dropped its petals, Tohoku is often still a fortnight away from opening.</p>

<h3>Why nobody can promise you a date</h3>
<p>Bloom timing depends on the winter that preceded it, and a warm February can pull the opening forward by a week. The Japan Meteorological Agency stopped issuing the official forecast in 2010, and private forecasters now publish the projections quoted everywhere. Those forecasts are useful from February onward — long after you needed to book flights and rooms. You are booking a <strong>window, not an event</strong>.</p>

<!-- IMAGE_SLOT_1: Cherry trees in full bloom along a canal or riverside path in Kyoto or Tokyo, with people walking beneath them — daylight, natural crowd density, not an empty staged shot. -->

<h2>What the season does to what you pay</h2>
<p>Bloom season is Japan's most expensive domestic travel period outside the New Year holiday. Accommodation in central Kyoto and Tokyo rises sharply for the same rooms, reserved seats on the fast trains fill early, and the better-regarded inns stop taking new bookings months out. The airfare from the US rises too, though less dramatically than the lodging.</p>

<h3>How far ahead to book</h3>
<p>Rooms in Kyoto and central Tokyo for the bloom window are commonly booked around six months ahead, and the well-regarded traditional inns go earlier still. That is the uncomfortable part of the timing problem: the booking deadline falls months before any forecast exists. Most people resolve it by choosing the first week of April, accepting the odds, and booking something cancellable.</p>

<p>If your dates are fixed by work or school, plan a trip you would enjoy regardless and treat the blossom as a bonus. A first trip built entirely around one week of flowers disappoints when the flowers run early.</p>

<h2>Where the crowds actually are</h2>
<p>Crowding in Tokyo and Kyoto during the roughly one-week bloom window concentrates in a small number of famous places rather than spreading evenly. The named parks, the photogenic riverside paths and the temple gardens that appear in every forecast article absorb enormous numbers of people, while ordinary neighbourhood streets a few minutes away carry the same trees with a fraction of the crowd.</p>

<p>Japan treats blossom viewing as a social occasion rather than a spectator sport, which is why the busiest spots stay busy from morning until well after dark. Early morning is the reliable answer at the famous sites — as is simply walking, since residential streets, campuses and canal banks carry the same trees and attract almost nobody.</p>

<h2>The three ways people actually play it</h2>
<p>Given a booking deadline roughly six months out and a bloom forecast that does not appear until February, travellers to Japan converge on three strategies: book the first days of April and accept the odds, travel south to north and take two chances, or book April for the season and treat the flowers as luck. It is worth choosing between them deliberately rather than drifting into one.</p>

<h3>Book the first week of April and accept the odds</h3>
<p>The most common approach: the Tokyo-Kyoto corridor most often reaches full bloom around the turn of the month, so a week straddling it has a genuine chance. The cost is peak-season prices paid for a probability, and a warm February leaves you late with nothing but green.</p>

<h3>Aim north and follow it</h3>
<p>Because the bloom climbs the country over several weeks, a trip that starts in the south and moves north converts a single window into several. Arriving in Kyoto in early April and reaching Tohoku a fortnight later means two separate chances rather than one. The trade-off is that you are committing to a lot of ground, which is a real constraint on a first trip where the cities themselves deserve time.</p>

<h3>Go for the season, not the flower</h3>
<p>The third option is to book April for the weather and the long daylight, and treat any blossom as luck. Late April is one of the most pleasant stretches of the Japanese year and noticeably cheaper — until the holiday cluster at the end of the month, which is a different problem entirely.</p>

<h2>What "full bloom" actually means</h2>
<p>Full bloom, the stage Japanese forecasts call mankai, is a specific point rather than a general condition, and the gap between the first flowers opening and the trees being fully out is usually several days. Forecasts quote both the opening date and the full-bloom date for each city, and the second is the one worth planning around — a tree at thirty per cent is a tree with some flowers on it, not the thing people travel for.</p>

<p>The end is quicker than the beginning. Once full bloom passes, a single day of rain or wind can strip a street, which is why advice to build in slack at the front of the window is better than assuming you can catch up at the back.</p>

<h2>The alternative nobody mentions</h2>
<p>Autumn, which peaks in Kyoto through the second half of November, is Japan's other great season and for a first trip arguably the easier one. Colour holds for weeks rather than days, the weather is more settled, and while it is busy it does not carry bloom season's compressed desperation. If you want Japan at its most beautiful and your dates are flexible, <a href="/article/best-time-to-visit-japan">the case for choosing a season deliberately</a> is worth reading before you commit to spring.</p>

<p>Late April is also worth knowing about, once the blossom has passed the main cities. The weather is excellent, prices ease, and the country is green rather than pink — right up until the holiday cluster at the end of the month, which is a different problem entirely.</p>

<h2>What the blossom decision is really attached to</h2>
<p>Notice what the bloom window has quietly done. A one-week target in Tokyo and Kyoto sets a booking deadline six months out, which fixes how far ahead you commit to rooms, which constrains which cities you can base yourself in, which changes how much of the country you can reach. Chasing the blossom is not a standalone preference — it decides four or five other things, six months before you travel.</p>

<p>That chain is where first trips come apart, usually not because any single decision was wrong but because they were each made separately. Working out how the timing, the bases and the routing between them fit together is what <span class="guide" data-guide="name">the complete Japan trip guide</span> is built to do.</p>
"""
})

# ─────────────────────────────────────────────────────────────── 2. TURN
A.append({
 "slug": "golden-week-japan-what-closes",
 "title": "Golden Week in Japan: What Closes and What It Costs",
 "category_slug": "when-to-go",
 "excerpt": "Golden Week is built from four public holidays at the turn of April into May. What actually shuts, what is merely crowded, and what to do if your dates cannot move.",
 "featured_image": "japanforamericans/articles/golden-week-japan-what-closes-hero",
 "content": """<p>Golden Week is the cluster of public holidays at the turn of April into May, and it is the period most often flagged as one to avoid. That advice is broadly right but rarely explained, which leaves travellers either cancelling a workable trip or walking into a week they were not prepared for. Here is what actually closes, what is simply full, and what to do if your dates are fixed.</p>

<h2>Which days Golden Week actually covers</h2>
<p>Golden Week is built from four national holidays: Showa Day on 29 April, Constitution Day on 3 May, Greenery Day on 4 May and Children's Day on 5 May. Those four dates are fixed in law. How long the resulting run of days lasts is not fixed — it depends entirely on which weekdays those dates land on in a given year.</p>

<h3>Why the length changes every year</h3>
<p>Japan applies a substitute holiday rule: when a national holiday falls on a Sunday, the next weekday that is not already a holiday becomes a holiday instead. A single working day sandwiched between two holidays also becomes one. In some years those rules knit the whole stretch from 29 April into a continuous break; in others the run is broken by two ordinary working days in the middle.</p>

<p>The practical instruction is to <strong>check the actual dates for your year</strong> rather than trusting any article that quotes a fixed span. The holidays are stable; the shape of the week is not.</p>

<h2>What genuinely closes</h2>
<p>Closures during Golden Week are narrower than most travellers expect. Major museums, big temples and shrines, department stores, and the large restaurant groups stay open and are extremely busy. What closes is the smaller layer: family-run restaurants, independent shops, small workshops and some local businesses, which take the break precisely because everyone else is off.</p>

<p>Government offices and banks close on the holidays themselves. That matters less than it once did, but it is worth not scheduling anything administrative into the week.</p>

<!-- IMAGE_SLOT_1: A very crowded Japanese train platform or a packed shopping street during a holiday period — dense but orderly, daylight, clearly showing scale of domestic crowds rather than a landmark. -->

<h2>What it does to prices and seats</h2>
<p>Golden Week moves the entire country at once, and the effect on transport and lodging is the real reason to plan around it. Reserved seats on the fast trains sell out well in advance on the main corridors, domestic flights fill, and accommodation prices in the popular cities rise sharply for the same rooms you could have had cheaply a fortnight earlier.</p>

<h3>The part that surprises Americans</h3>
<p>This is domestic travel, not international tourism. The crowds are Japanese families going home or taking their one reliable block of annual leave, which means the pressure lands hardest on routes and towns that are otherwise quiet. A rural hot-spring town can be harder to book than Tokyo.</p>

<p>It also means the crowding is front-loaded and back-loaded: the heaviest movement is at the start and end of the run, and the middle days are calmer in transit even while the sights stay packed.</p>

<h2>Which days inside the run are worst</h2>
<p>Pressure during Golden Week is not evenly spread across the days. The heaviest movement falls at the two ends — the outbound surge as the run begins and the return surge as it closes — because that is when the entire working population is travelling in the same direction at the same time.</p>

<p>The middle days behave differently. Transport eases because most people have already arrived where they are going, while the sights themselves stay packed. For a visitor who has to be in Japan during the run, that asymmetry is the single most useful thing to know: <strong>move at the middle, sit still at the ends</strong>.</p>

<h3>The administrative detail</h3>
<p>Banks and government offices close on the holidays themselves, and anything requiring a counter and a human becomes difficult across the run. It matters less than it used to, but it is worth handling anything administrative before the week begins rather than assuming a quiet Tuesday will be available.</p>

<h2>What the week is like if you stay</h2>
<p>Golden Week in Tokyo or Kyoto is not a write-off, and travellers who have been through it often report it as one of the more memorable stretches of a trip. Parks fill with families, temporary food stalls appear, and the ordinary rhythm of the cities gives way to something closer to a national festival. The crowds are good-natured rather than fraught, and the atmosphere is genuinely different from any other week of the year.</p>

<h2>If your dates cannot move</h2>
<p>A Golden Week trip is entirely workable if you accept two constraints. Book everything early — rooms and any reserved long-distance seats, months ahead rather than weeks. And stay put: this is the wrong week to be relocating between cities every second day, because the moving is where the pain concentrates.</p>

<p>Pick one base, use it properly, and take the pressure off by going out early. A city like <a href="/article/tokyo-travel-guide-first-timers">Tokyo absorbs crowds far better</a> than a small temple town does, simply because there is more of it. The same logic applies to choosing sights: the enormous, famous ones cope; the small, perfect ones do not.</p>

<h2>What the timing decision is attached to</h2>
<p>Golden Week, built on four fixed holidays between 29 April and 5 May, does not just make Japan busy — it changes what kind of trip is possible. It pushes you toward fewer bases, earlier commitment, bigger cities and larger sights, and it does that whether or not you planned for any of it. The same is true of the August holiday period and, in a different way, of blossom season.</p>

<p>Each of those is usually treated as a separate warning in a separate article. They are really one decision about when to come, which then reshapes the routing, the bases and the booking order underneath it. Working out that chain in advance, rather than discovering it in sequence, is what <span class="guide" data-guide="name">the complete Japan trip guide</span> sets out to do.</p>
"""
})

# ─────────────────────────────────────────────────────────────── 3. SEED
A.append({
 "slug": "autumn-foliage-japan-timing",
 "title": "Autumn Foliage in Japan: Timing Your Trip",
 "category_slug": "when-to-go",
 "excerpt": "Autumn colour moves from Hokkaido in October to Kyoto in late November. The regional timetable, why it is easier to plan than spring, and where to see it without the worst crowds.",
 "featured_image": "japanforamericans/articles/autumn-foliage-japan-timing-hero",
 "content": """<p>Autumn is Japan's other great season, and for a first trip it is the more forgiving one. The colour lasts weeks rather than days, the weather is settled, and the timing is far more predictable than spring. This guide covers when the colour peaks where, how to plan around it, and where to see it without standing in the worst of the crowds.</p>

<h2>When the colour peaks, region by region</h2>
<p>Autumn colour peaks in Hokkaido and the Japanese Alps during October, in Kyoto through the second half of November, and in Tokyo from late November into the first days of December. The colour moves in the opposite direction to the cherry blossom — north to south, and from high ground down into the valleys and cities.</p>

<h3>Reading the direction of travel</h3>
<p>That north-to-south, high-to-low movement is genuinely useful for planning. If you are in Japan in late October, the mountains are already turning while Kyoto is still green. Arrive in the third week of November and the cities are at their best while the high country is bare. A trip that moves from the mountains toward the cities over a fortnight can effectively follow the colour down.</p>

<h2>Why autumn is easier to plan than spring</h2>
<p>Autumn foliage in Kyoto or Tokyo holds for several weeks in a given place, where cherry blossom holds for roughly one. That difference changes everything about the booking problem. A spring trip is a bet on a seven-day window that nobody can forecast until February; an autumn trip aimed at the back half of November is very likely to land on good colour regardless of how the year has gone.</p>

<p>The weather helps as well. Late autumn in Japan is reliably clear and cool, with far less rain than early summer and none of the heat that makes August walking difficult. For a trip built around being outdoors, it is the most comfortable stretch of the year.</p>

<!-- IMAGE_SLOT_1: Japanese maple in deep red over a temple garden or stone path in Kyoto, late afternoon light, a few visitors visible for scale rather than an empty garden. -->

<h2>Where the crowds actually are</h2>
<p>Autumn crowding in Kyoto during the last ten days of November behaves much like spring crowding: it concentrates in a small number of celebrated places rather than spreading out. Kyoto's most famous temple gardens in the last ten days of November are genuinely difficult, with queues at the gate and paths moving at a shuffle. Fifteen minutes away, less-photographed temples carry the same maples and a tenth of the people.</p>

<p>Two things reliably help. Go early, because the famous gardens open before the tour groups reach them. And go up — hillside temples and walking routes thin out quickly, because most visitors will not climb for a view they can photograph from the flat.</p>

<h3>The evening illuminations</h3>
<p>Many temples run special evening openings during the colour season, lighting the maples after dark. They are beautiful and they are extremely popular, so treat them as their own outing rather than something you append to a full day of sightseeing. If you plan to do one, it is worth building the day around it.</p>

<h2>Colour beyond the famous gardens</h2>
<p>Autumn colour in Japan is not confined to the temple gardens that appear in every photograph. City parks, riverbanks, university campuses and the approach roads to ordinary shrines carry the same maples, and the mountains around Kyoto and Tokyo are within reach of a half-day walk. A trip that treats the celebrated gardens as one item among several, rather than the whole point, tends to see more colour and stand in fewer queues.</p>

<h2>What to book, and when</h2>
<p>Autumn does not demand spring's six-month lead, but the back half of November in Kyoto is one of the busiest lodging periods of the year and behaves accordingly. Rooms in central Kyoto get expensive and scarce; reserved seats on the fast trains fill on the main corridors at weekends. Two to three months ahead is usually comfortable, and earlier if you want a specific traditional inn.</p>

<p>Booking pressure is one of several ways the calendar quietly shapes a first trip — how many bases you can use, which cities work at which times, and how much of the route you can commit to before you know the weather. <span class="guide" data-guide="name">The complete Japan trip guide</span> works through how those pieces interact.</p>

<h2>Autumn against spring, as a decision</h2>
<p>Put Japan's two peak seasons side by side — a one-week bloom window in late March and early April against several weeks of colour from October to early December — and the choice becomes clearer than the marketing suggests. Spring offers a shorter, more dramatic spectacle on a window nobody can forecast in time to book. Autumn offers a longer, steadier one on a window you can plan around months ahead.</p>

<p>Spring wins on the strength of the image and on the atmosphere — the whole country is out under the trees, and there is nothing else quite like it. Autumn wins on almost everything practical: settled weather, a forgiving timetable, a shorter booking lead, and prices that, while high in Kyoto, do not reach spring's peaks across the board.</p>

<p>For a first trip where the cities and the routing are themselves new, the season that does not also demand a gamble is the easier one to build a plan on. For a return trip with a specific image in mind, spring's risk is worth taking.</p>

<h2>Combining colour with the rest of a trip</h2>
<p>Autumn's several-week span in Kyoto and Tokyo, against cherry blossom's single week, is what makes November easy to combine with everything else. Because you are not chasing a seven-day window, you can plan a normal route through the country and let the colour meet you along the way. A <a href="/article/japan-itinerary-7-days">standard first week through Tokyo and Kyoto</a> needs no adjustment at all in mid-November beyond booking earlier than you otherwise would.</p>

<p>The one date to keep an eye on is the very end of November in Kyoto, when the city is at its absolute peak and at its most crowded. If you would rather have the gardens than the photograph, aim a week either side.</p>
"""
})

# ─────────────────────────────────────────────────────────────── 4. SEED
A.append({
 "slug": "obon-japan-mid-august",
 "title": "Obon in Japan: What Changes in Mid-August",
 "category_slug": "when-to-go",
 "excerpt": "Obon is not a public holiday, yet it is one of Japan's heaviest travel weeks. What the observance is, what closes, and how to travel through it without being caught out.",
 "featured_image": "japanforamericans/articles/obon-japan-mid-august-hero",
 "content": """<p>Obon is the mid-August observance when families return to their home towns to honour their ancestors, and it produces one of the heaviest domestic travel weeks of the Japanese year. What catches American visitors out is that it is not a public holiday at all — the calendar shows ordinary working days while the country moves. Here is what changes, and what to do about it.</p>

<h2>When Obon falls</h2>
<p>Obon is observed around 13 to 16 August across most of Japan, though the observance is not a national holiday and the dates are not fixed by law. Some regions, including parts of Tokyo, keep it in mid-July instead, following the older calendar. For a visitor, the mid-August window is the one that matters, because that is when the bulk of the country travels.</p>

<h3>Why a non-holiday empties the cities</h3>
<p>Most Japanese companies close for several days around Obon even though the state does not require it, which produces the effect of a national holiday without one appearing on any calendar. Because the tradition is about returning to a family home, the movement runs out of the big cities and into the provinces — the opposite direction to a tourist week.</p>

<h2>What actually closes</h2>
<p>Closures during Obon fall on the small and family-run layer of Japanese business: independent restaurants, neighbourhood shops, small workshops, and family-owned inns whose owners are themselves observing. Larger museums, department stores, chain restaurants and the major temples and shrines generally stay open.</p>

<p>The pattern is inconsistent enough that it is worth checking specific places rather than assuming. A restaurant you were looking forward to may simply be shut for four days with a handwritten note on the door, and that is normal rather than a sign of anything going wrong.</p>

<!-- IMAGE_SLOT_1: Evening Obon scene — lanterns, or a traditional Bon Odori dance in a neighbourhood square with people in yukata, warm summer light. -->

<h2>What it does to travel</h2>
<p>Obon, across roughly 13 to 16 August, puts enormous pressure on long-distance transport in both directions: out of the cities at the start, back into them at the end. Reserved seats on the fast trains sell out on the main corridors, domestic flights fill, and expressways congest badly. Accommodation tightens most in the provincial towns and hot-spring resorts that are quiet the rest of the year.</p>

<h3>Where the pressure is lighter</h3>
<p>Central Tokyo and central Kyoto are, unusually, somewhat calmer during Obon than in the weeks either side, because a substantial share of their residents has left. The cities do not empty — inbound visitors are still there — but the domestic layer thins out. If you are staying put in a big city, Obon is more manageable than its reputation suggests.</p>

<p>The difficulty lands on anyone moving between places in the two or three days at each end of the observance. That is the window to avoid for long journeys, rather than the whole period.</p>

<h2>What you can see during the observance</h2>
<p>Obon is a religious and family occasion rather than a spectacle staged for visitors, and most of it happens privately — graves tended, household altars prepared, relatives gathered. What is public are the neighbourhood dances held on summer evenings across the country, open to anyone who wants to join the circle, and the lanterns set out to guide ancestors home and away again. Encountering one is a matter of being in a neighbourhood at the right hour rather than buying a ticket.</p>

<h2>The other August problem</h2>
<p>Obon sits inside Japan's hardest month for weather. August highs in Tokyo and Kyoto run around 33 to 35C with high humidity, and Kyoto's basin geography makes it feel worse than the number suggests. Heat is a genuine constraint on how much walking an itinerary can carry, not merely a comfort note — a plan that works in April will not survive August unmodified.</p>

<p>August is also the peak of the typhoon season, which can remove a travel day at short notice. Neither is a reason to cancel a trip that has to happen in August, but both are reasons to build a lighter plan with indoor options, early starts and long afternoon breaks.</p>

<h2>The July observance, and why it confuses people</h2>
<p>Parts of Japan, including some Tokyo districts, observe Obon in mid-July rather than mid-August, following the older lunar reckoning. The result is that a visitor can encounter Obon decorations and observances in July in one neighbourhood and find nothing unusual a few train stops away.</p>

<p>The July observance does not produce the national travel surge, which is what makes the August window the one that matters for planning. If you are in Tokyo in mid-July and notice lanterns going up, that is the local calendar rather than a sign that the country is about to move.</p>

<h2>Reading the direction of the crowd</h2>
<p>Obon travel runs out of Tokyo, Osaka and the other major cities and into the provinces, which is the reverse of almost every other busy period and the reason the usual advice does not apply cleanly. A tourist week concentrates people in Tokyo and Kyoto; Obon disperses residents from them toward home towns, hot-spring resorts and rural districts.</p>

<p>For a visitor, that inversion is worth using rather than fighting. A city-based few days across the observance can be easier than the weeks either side, while a plan built around small provincial towns runs straight into the heaviest demand of the year for exactly the kind of accommodation those towns have least of.</p>

<h2>Travelling through it deliberately</h2>
<p>Obon, in the middle four days of August, is workable if you treat it as a fixed feature of the map rather than a surprise. Book long-distance travel and rooms well ahead, avoid moving cities in the peak days at either end, and expect small restaurants to be closed.</p>

<p>Choosing when to come is one of the decisions that quietly reshapes everything else about a first trip, which <span class="guide" data-guide="name">the complete Japan trip guide</span> works through in order.</p>

<p>If your dates are flexible and August is not fixed, the first half of the month is easier than the second, and September is easier than both once the worst of the heat begins to break.</p>
"""
})

# ─────────────────────────────────────────────────────────────── 5. SEED
A.append({
 "slug": "japan-rainy-season-typhoons",
 "title": "Japan's Rainy Season and Typhoons: What They Mean for Your Trip",
 "category_slug": "when-to-go",
 "excerpt": "The rainy season moves north across Japan from May to July, and typhoon season peaks in late summer. What each actually does to a trip, and when they are worth planning around.",
 "featured_image": "japanforamericans/articles/japan-rainy-season-typhoons-hero",
 "content": """<p>Two weather patterns get Japan's early summer written off in travel advice: the rainy season and the typhoon season. Both are real, and both are routinely described in a way that makes them sound worse than they are. This guide covers when each actually happens, what they do to a trip in practice, and when they are genuinely worth rearranging plans around.</p>

<h2>When the rainy season runs</h2>
<p>Japan's rainy season runs from roughly early June to mid or late July in the Tokyo and Kyoto regions, and it moves south to north across the country. Okinawa runs from early May to late June; Kyushu and Shikoku from late May or early June into mid-July; the Tokyo and Kyoto regions from roughly early June to mid or late July; and Tohoku later still. Hokkaido is generally considered not to have one at all.</p>

<h3>What it actually feels like</h3>
<p>The most useful thing to know is that the rainy season is not weeks of continuous rain. In practice it means high humidity with heavy bursts — a downpour that soaks a street and stops, followed by grey warmth or sudden sun. Whole days are lost to rain much less often than the name implies.</p>

<p>What it does reliably deliver is humidity, which matters more for comfort than the rain does. Temples and gardens look extraordinary in wet weather, the moss is at its best, and the famous places are noticeably less crowded. For a traveller willing to carry an umbrella, June is one of the better-value months of the year.</p>

<!-- IMAGE_SLOT_1: A Japanese garden or temple path in rain — wet stone, intense green moss, hydrangeas if possible, a clear umbrella. Atmospheric rather than bleak. -->

<h2>When typhoon season matters</h2>
<p>Typhoons are possible in Japan from roughly May through October, with the peak in August and September. Okinawa, Kyushu and Shikoku are the most exposed; direct hits on Tokyo and Kyoto are less common, though disruption to transport from a storm passing nearby is not.</p>

<h3>How disruption actually works</h3>
<p>Japanese rail operators announce planned suspensions in advance rather than cancelling services as a storm arrives. That practice is unfamiliar to most American travellers and is genuinely reassuring: you usually know the day before that a line will stop running, which gives you time to move a plan rather than being stranded by it.</p>

<p>A typhoon that affects your trip will most likely cost you one day, not a week. The sensible response is to keep a flexible day in the plan and avoid scheduling anything unmissable — a long-distance journey, or the flight home — for the tail end of a trip in early September.</p>

<h2>Should you avoid the summer entirely?</h2>
<p>Summer in Japan is worth taking on its own terms rather than avoiding outright, and its real problem is heat rather than either weather pattern. August highs in Tokyo and Kyoto run around 33 to 35C with high humidity, and Kyoto's basin geography makes it feel hotter still. That is a genuine constraint on how much walking a day can hold, and it is the reason August itineraries need to be lighter than spring ones.</p>

<p>Set against that, summer carries the festival calendar, long daylight, and the mountains and northern regions at their most pleasant — Hokkaido in August is excellent. Summer is not a season to avoid so much as one to plan differently.</p>

<h3>If your dates are fixed in early summer</h3>
<p>June and early July are genuinely good months to travel in Japan provided you plan for the humidity: early starts, indoor anchors in the middle of the day, and no assumption that every afternoon will be dry. Prices sit below both peak seasons and the major sights are calmer than at any other point between March and November.</p>

<h2>Early summer, month by month</h2>
<p>June, July and September differ enough from one another that treating early summer as a single block is misleading. June carries the rainy season and the lowest crowds of the warm half of the year; July turns hot once the rains lift in the middle of the month; September sits at the typhoon peak while the heat finally begins to ease. Each asks for a different kind of itinerary.</p>

<h3>June</h3>
<p>June carries the rainy season across most of the main island and is, for that reason, one of the quietest and best-value months in the calendar. Gardens are at their most saturated, the famous sites are noticeably calmer, and the temperature is warm rather than punishing. The cost is humidity and an umbrella in the bag every day.</p>

<h3>July</h3>
<p>July begins wet and ends hot, with the rainy season lifting somewhere in the middle and the serious heat arriving behind it. The second half of the month starts to demand the lighter, slower kind of itinerary that August requires outright.</p>

<h3>September</h3>
<p>September sits at the peak of the typhoon season while the heat begins to ease, which makes it a month of trade-offs rather than a straightforward improvement on August. The back half is generally more comfortable than the front, and the crowds are lighter than either peak season.</p>

<h2>Building a plan that survives a lost day</h2>
<p>A Japan trip in August or September should be built to absorb one lost day, because that is the realistic cost of a typhoon passing near Tokyo or Kyoto rather than the week-long disruption travellers fear. Building that slack in costs very little.</p>

<p>The practical version is to avoid scheduling a long-distance journey or anything unmissable on the final days, and to keep one flexible afternoon in reserve rather than filling every slot.</p>

<p>Because suspensions are announced ahead rather than sprung on passengers, the warning usually arrives with enough time to reorder a plan. What it cannot do is create space in an itinerary that had none, which is the real argument for planning early summer more loosely than spring.</p>

<h2>Choosing a season on purpose</h2>
<p>Weather is only one input into when to visit Japan, and rarely the decisive one — the rainy season's six weeks and the typhoon peak in August and September matter less to most itineraries than the holiday clusters do.</p>

<p>Weather interacts with those clusters, with lodging prices, and with how much ground an itinerary can cover — a choice that cascades into how many bases you use and how far ahead you commit. <a href="/article/best-time-to-visit-japan">Comparing the seasons against each other</a> is a more useful exercise than ruling any single month out.</p>

<p>How that timing decision then reshapes the route, the bases and the booking order underneath it is what <span class="guide" data-guide="name">the complete Japan trip guide</span> is built to work through.</p>
"""
})

# ── normalise whitespace: the pipeline expects compact HTML, not pretty-printed
for a in A:
    a["content"] = re.sub(r"\n\s*\n", "", a["content"]).replace("\n", "").strip()

here = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(here, "import-batch-A.array.json")
json.dump(A, open(out, "w"), ensure_ascii=False, indent=2)

print(f"écrit : {out}")
for a in A:
    w = len(re.sub(r"<[^>]+>", " ", a["content"]).split())
    print(f"  {a['slug']:<36} {w:>5} mots")
