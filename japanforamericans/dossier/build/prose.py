# prose.py — the opening, the essays, the back matter.
# Register: Economist/Monocle. Calm, no enthusiasm, no fluff. Show the reasoning
# and let the reader disagree. Three wonder paragraphs in the whole book, no more.
# ─────────────────────────────────────────────────────────────────────────────

EST = "<span class='mk est'>●</span>"
OFF = "<span class='mk off'>◇</span>"
SUR = "<span class='mk sur'>▲</span>"
VOL = "<span class='mk vol'>◆</span>"

OPENING = {
 "kind": "The contract",
 "title": "What this book is for",
 "standfirst": "A first trip to Japan is not hard. It is over-decided — and the decisions "
               "are made in the wrong order.",
 "body": f"""
<p class="lede">Japan is among the easiest countries an American can travel in. You need no
visa for a short visit, the trains run to the second, the crime rate is low enough that the
question barely arises, and the food is excellent at nearly every price. Almost nothing about
the trip is difficult. What it is, instead, is over-decided: a dozen choices that each look
small, presented in isolation by a hundred articles, and connected to each other in ways that
only become visible after you have already committed to three of them.</p>

<p>This book exists because those connections are where the money and the days go. The season
you pick sets the booking deadline. The booking deadline decides how many cities you can
commit to. The number of cities decides whether a rail pass pays. Whether the pass pays
decides whether you spend two hundred dollars you did not need to — and, worse, whether you
then bend the route to justify the purchase. None of that is difficult. It is simply not
answerable one article at a time, which is exactly how it is usually answered.</p>

<h2>What we do and do not claim</h2>

<p>Every call in here is argued in the open, with the arithmetic on the page, so that you can
disagree with us and still come out ahead. That is the contract. Where we say buy, we show the
sum that says buy; where the sum is close, we say it is close. A recommendation you cannot
audit is worth nothing to someone spending four thousand dollars, and the number of places
where a confident voice is simply repeating a decade-old blog post is higher in Japan than
almost anywhere. {EST}</p>

<p>We do not tell you which hotel to book or which restaurant to eat at. Those are the two
things every guide leads with and the two that age fastest — a list of names is wrong within a
season, while the rule that generated the list keeps working. The back of this book says
plainly what it refuses to do, and why.</p>
""",
}

HOWTOREAD = {
 "kind": "How to read it",
 "title": "Marks, and the two documents",
 "standfirst": "Every claim in this book carries a mark that tells you how much weight it "
               "will still bear next year.",
 "body": f"""
<p class="lede">Travel writing rarely distinguishes between a fact that has been true for
forty years and a price that was checked once in spring. This book marks the difference on
every claim, because the two age at completely different rates and you are entitled to know
which one you are being handed.</p>

<div class="ledger">
  <div class="lcap">The four marks</div>
  <table>
    <tr><th>Mark</th><th>Means</th></tr>
    <tr><td>{EST} <b>ESTABLISHED</b> — structural, true for years</td><td>the book</td></tr>
    <tr><td>{OFF} <b>OFFICIAL</b> — a published fare or a rule in law</td><td>the book</td></tr>
    <tr><td>{SUR} <b>SURVEYED</b> — our own dated observation</td><td>the book, dated</td></tr>
    <tr><td>{VOL} <b>VOLATILE</b> — a price, an hour, a window</td><td>the Field Sheet</td></tr>
  </table>
</div>

<p>Anything carrying no mark is opinion, and we have tried to leave none of it in. The rule
we hold ourselves to is simple: if a sentence cannot carry a mark, it is not a claim, it is a
flourish, and it should be cut.</p>

<h2>Why there are two documents</h2>

<p>The book you are reading is built to stay true for about two years. It contains no live
prices, because a price printed in a book is a lie with a long shelf life. Every volatile
figure lives instead in the <b>Field Sheet</b> — a short dated annex, re-issued quarterly, that
carries the numbers and nothing else. When the two disagree, the Sheet is right and the book
is old.</p>

<p>Read the book once before you book anything. Carry the Sheet on the trip.</p>
""",
}

GROUND = {
 "kind": "The ground",
 "title": "Two legs, and a pass that needs four",
 "standfirst": "One number reorganises a first trip to Japan, and almost nobody arrives "
               "knowing it.",
 "fig": "corridor",
 "body": f"""
<p class="lede">The trip that nearly every first-timer takes has a shape so consistent it can
be described in a sentence: fly into Tokyo, spend several days, take one Shinkansen to Kyoto,
spend several more, fly home. Some variant of that is what the itinerary articles converge on,
what the week allows, and what people come back having enjoyed. It contains exactly two long
train journeys. {EST}</p>

<p>The Japan Rail Pass needs about four to pay for itself. {EST}</p>

<p>That collision is the single most useful thing to know before you plan anything else,
because it is counter-intuitive in a specific and expensive way. For twenty years the pass was
the correct reflex, and the entire English-language internet learned to recommend it. Then in
October 2023 the seven-day ordinary pass rose from roughly ¥29,650 to ¥50,000 — about seventy
per cent in a single step — and the advice did not move. {OFF}</p>

<h2>Why the sum is the interesting part</h2>

<p>Divide the pass price by the fare it is meant to save you and the answer falls out. A
reserved seat from Tokyo to Kyoto is about ¥13,850, so the pass needs a little under four
journeys of that length before it breaks even — roughly two round trips inside a seven-day
window. A trip with two long legs in it is not close to the line. It is at half. {OFF}</p>

<p>The second-order cost is the one that does the real damage, and no price comparison
catches it. A pass already paid for is an argument in your pocket for using it, and routes
quietly bend to justify the purchase. A day trip gets added because it is free, a city
inserted because the train is covered, and a fortnight that was going to be two calm bases
turns into five hotels and a lot of luggage on platforms. The purchase should follow the route. It
usually leads it.</p>

<h2>What the corridor looks like</h2>

<p>Japan for a first-timer is not the archipelago of the map. It is a corridor: Tokyo and
Kyoto, a little over two hours apart on the fastest services the pass does not cover, with
everything else reached as a day trip from one end or the other. Nara is forty-five minutes
from Kyoto. Hakone, Nikko and Kamakura are inside two hours of Tokyo. {EST} Those spokes run on
local and rapid lines at a fraction of bullet-train prices, which means the pass does not help
with them either.</p>

<p>Once the corridor is the mental model rather than the country, most of the remaining
decisions in this book get easier, and several of them stop being decisions at all.</p>
""",
}

BEFOREYOUFLY = {
 "kind": "Before you fly",
 "title": "The four things with deadlines",
 "standfirst": "Most of the preparation is optional. These four are not, and each has a date "
               "attached.",
 "body": f"""
<p class="lede">Japan asks very little of an American traveller in advance — no visa, no
vaccination paperwork, no entry fee. {OFF} What it does have is a small set of tasks whose cost
rises sharply the later you do them, and which are easy to leave until the week before because
nothing forces them earlier.</p>

<div class="ledger">
  <div class="lcap">What has a deadline · counted back from departure</div>
  <table>
    <tr><th>Task</th><th>When</th></tr>
    <tr><td>Rooms, if you are travelling in bloom season {EST}</td><td>~6 months</td></tr>
    <tr><td>Rooms, late November foliage {EST}</td><td>2–3 months</td></tr>
    <tr><td>A ryokan you actually want {EST}</td><td>2–3 months</td></tr>
    <tr><td>Transit card created and topped up {SUR}</td><td>before you board</td></tr>
  </table>
</div>

<p>The transit card is the one that looks trivial and is not. Creating a Suica in Apple Wallet
takes four minutes at home and can fail in a way that takes an afternoon to solve in Tokyo,
because a US-issued Visa is refused for top-ups while Mastercard and American Express are
accepted. {SUR} The failure produces an unhelpful error rather than an explanation, and the
place people discover it is a ticket gate with a queue behind them. Do it on the sofa.</p>

<h2>What does not need doing</h2>

<p>You do not need cash in advance at an airport exchange desk, you do not need a pocket
wi-fi device booked from abroad in most cases, and you do not need a rail pass ordered before
you have counted your legs. Each of these is sold hard to people planning a first trip and
each is, for the corridor-shaped trip most people take, either unnecessary or actively worse
than the alternative available on arrival.</p>
""",
}

DAYZERO = {
 "plate": "A02",
 "plate_cap": "Tokyo Station, mid-afternoon. Everyone in this frame knows where they are going; on your first day you will not, which is the whole argument for landing early and setting the card up at home.",
 "plate_after": 3,
 "kind": "Day zero",
 "title": "The first six hours",
 "standfirst": "Nobody writes the arrival day, which is the one where a plan is most easily "
               "lost.",
 "body": f"""
<p class="lede">You land after eleven hours in the air, somewhere between mid-afternoon and
late evening, and what happens next is decided almost entirely by two things you chose months
earlier: which airport you fly into, and what time the wheels touch. Neither feels like an
itinerary decision at the time of booking. Both are.</p>

<p>Haneda sits close to central Tokyo and is reached in roughly thirty minutes. {EST} Narita
is a genuine distance out, and the transfer runs sixty to ninety minutes depending on which
service you take. {EST} On a normal day that difference is an hour. On the day you have not
slept properly, are carrying everything you brought, and are trying to work out a ticket
machine in a language you do not read, it is the difference between an evening and a
lie-down.</p>

<div class="ledger">
  <div class="lcap">The first six hours, in order</div>
  <table>
    <tr><th>Step</th><th>Why it is in this position</th></tr>
    <tr><td>Immigration, then straight past the exchange desks {EST}</td><td>the rate there is the worst you will see</td></tr>
    <tr><td>Train, on the card you set up at home {SUR}</td><td>the queue at a machine is the avoidable part</td></tr>
    <tr><td>Hotel, drop everything {EST}</td><td>you are carrying the whole trip otherwise</td></tr>
    <tr><td>A short walk and a konbini meal {EST}</td><td>daylight fights the jet lag; ambition does not</td></tr>
  </table>
</div>

<h2>The order that works</h2>

<p>Clear immigration, ignore the exchange desks, and go straight to the train — assuming the
transit card on your phone already works, which is why it is the one task on the pre-departure
list with a hard deadline. If it does not, buy a physical card from a station machine and feed
it cash: the machines take notes, carry an English interface, and sidestep the entire
card-network problem in one step. {EST}</p>

<p>Then do nothing ambitious. The first evening is for a short walk, a convenience-store meal
that will be better than it has any right to be, and an early night against the jet lag.
Japan is thirteen or fourteen hours ahead of the American east coast, and the trip is long
enough that one surrendered evening costs nothing while one badly-handled first night costs
two days.</p>
""",
}

FAILURE_MODES = {
 "kind": "Failure modes",
 "title": "What goes wrong, by what it costs",
 "standfirst": "Organised by consequence rather than by topic — which is the one thing a "
               "website of separate articles cannot do.",
 "body": f"""
<p class="lede">These are the failures that recur, sorted by what they take from you. A
website answers them one at a time, in the article where each happens to belong. Seeing them
ranked by cost is a different and more useful thing, because it tells you where to spend your
limited planning attention.</p>

<h2>Costs you a day</h2>

<div class="ledger">
  <div class="lcap">The expensive ones</div>
  <table>
    <tr><th>What happens</th><th>Where it is answered</th></tr>
    <tr><td>Transit card cannot be topped up; the morning goes on it {SUR}</td><td>Decision 03</td></tr>
    <tr><td>Three day trips in a five-day trip; the cities disappear {EST}</td><td>Decision 01</td></tr>
    <tr><td>Moving cities during Golden Week or Obon {OFF}</td><td>Decision 04</td></tr>
    <tr><td>Late-evening landing treated as a usable evening {EST}</td><td>Decision 08</td></tr>
  </table>
</div>

<h2>Costs you money</h2>

<div class="ledger">
  <div class="lcap">The avoidable ones</div>
  <table>
    <tr><th>What happens</th><th>Where it is answered</th></tr>
    <tr><td>Rail pass bought on a two-leg route {OFF}</td><td>Decision 02</td></tr>
    <tr><td>Green Car upgrade priced per week, not per journey {OFF}</td><td>Decision 02</td></tr>
    <tr><td>Ryokan rate compared against a room rate {EST}</td><td>Decision 06</td></tr>
    <tr><td>Bloom-season rooms booked at peak for a probability {EST}</td><td>Decision 04</td></tr>
  </table>
</div>

<h2>Costs you the thing you came for</h2>

<p>The quietest failure has no line item. It is arriving in a country you will probably visit
once, with a plan assembled from forty open tabs, and spending the fortnight executing it
rather than being there. Every over-planned meal, every day trip added because it was on a
list, every hour spent extracting value from a pass is a small subtraction from the trip you
imagined when you booked. The book is mostly arithmetic because the arithmetic is what buys
back the attention.</p>
""",
}

BACKMATTER = {
 "kind": "Back matter",
 "title": "What this book will not tell you",
 "standfirst": "The refusals are the product. They are what keeps the rest of it true.",
 "body": f"""
<p class="lede">Four things this book deliberately does not do. Each is a thing most guides
lead with, and each is a thing we would have to get wrong in order to include.</p>

<ul class="refuse">
<li><b>It does not name hotels.</b> We have not slept in them. An assessment of a room we have
not been in is a repackaged booking-site listing with a confident voice on top, and you can
read those for free. What the book does instead is tell you which station to sleep near and
why, which is the part that survives a change of ownership.</li>

<li><b>It does not name restaurants.</b> A list of restaurants is wrong within a season — the
chef moves, the queue finds it, the lease ends. The rule that generated the list is still
right in five years, so the book gives you the rule. Decision 07 is that argument in full.</li>

<li><b>It does not print current prices.</b> Prices belong in the Field Sheet, which is dated
and re-issued. A price set in a book is a claim that stops being true quietly, and the reader
has no way to tell when it did.</li>

<li><b>It does not republish anyone's ratings.</b> Aggregate scores from the booking platforms
are contractually and editorially radioactive, and reprinting them would add nothing you
cannot see for yourself.</li>
</ul>

<p>There is a fifth refusal that belongs here too, because it shaped this edition: where the
corpus behind this book was thin on a subject, we left the subject out rather than writing
around the gap. A chapter assembled to fill a page is detectable, and it devalues the chapters
that were earned.</p>
""",
}

CLOSING = {
 "plate": "A07",
 "plate_cap": "An ordinary platform, no sight, no landmark. The tactile line, the marked door positions, the empty track — a country working, which is the part no itinerary can schedule.",
 "plate_after": 2,
 "kind": "Closing",
 "title": "The country, not the plan",
 "standfirst": "",
 "body": f"""
<p class="lede">There is a moment, usually on the second or third morning, when the planning
stops mattering. It tends to arrive somewhere ordinary — a station platform at seven in the
morning, everyone moving in the same direction without hurry, a vending machine humming, the
train arriving at the second it said it would. Nothing about it is a sight. It is just a
country working, at a level of consideration that is difficult to explain to someone who has
not stood in it.</p>

<p>That is the thing the arithmetic is protecting. Every decision in this book exists to
subtract a small anxiety from the fortnight so that more of it is available for the parts
that are not decidable in advance: the walk you took because the light was good, the counter
with six seats you went into because it was raining, the temple you had entirely to yourself
at eight in the morning because you were awake and nobody else was.</p>

<p>Work the sums out before you go. Then put the book down and stop optimising — the country
is better than any plan you can make of it.</p>
""",
}

ESSAYS = [OPENING, HOWTOREAD, GROUND, BEFOREYOUFLY, DAYZERO]
BACK    = [FAILURE_MODES, BACKMATTER, CLOSING]
