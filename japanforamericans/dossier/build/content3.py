# content3.py — eating, and where money actually leaks.
#
# Eating is this corpus's second-strongest vein (10,523w across three categories)
# and the site declared no swamp for it at all — so it earns an essay as well as
# Decision 07. Money is deliberately SHORT: the corpus carries the tipping rule,
# the cash-only pockets and the Visit Japan Web change, and little else. Writing
# a long money chapter on that base would be the padding this book refuses.
# ─────────────────────────────────────────────────────────────────────────────

EST = "<span class='mk est'>●</span>"
OFF = "<span class='mk off'>◇</span>"
SUR = "<span class='mk sur'>▲</span>"
VOL = "<span class='mk vol'>◆</span>"

EATING = {
 "plate": "A04",
 "plate_cap": "Six seats, one cook, steam. Nothing here can be booked from abroad, which is exactly why it is where the best meal of the trip usually happens.",
 "plate_after": 4,
 "kind": "Eating",
 "title": "The rule that outlives the list",
 "standfirst": "Japan is the hardest country in the world to eat badly in, and the easiest "
               "to eat mediocrely in — by trying too hard.",
 "body": f"""
<p class="lede">Every guide to Japan opens its food chapter with names. The names are the part
that expires: the chef moves, the queue arrives, the lease ends, and a list assembled in one
spring is quietly wrong by the next. What does not expire is the structure of eating here
&#8212; which kinds of places exist, what each is for, and how you get into them &#8212; and
that structure is unusually legible once someone draws it for you.</p>

<h2>The four layers</h2>

<p>Japanese eating stacks into four layers that operate on completely different rules, and
most first-timers only know about the top one.</p>

<div class="ledger">
  <div class="lcap">What each layer is for</div>
  <table>
    <tr><th>Layer</th><th>How you get in</th></tr>
    <tr><td>The destination restaurant {EST}</td><td>booked, often months, sometimes impossible</td></tr>
    <tr><td>The counter &#8212; ramen, sushi, tempura {EST}</td><td>walk in, often a ticket machine</td></tr>
    <tr><td>The izakaya {EST}</td><td>walk in, small plates, drinking</td></tr>
    <tr><td>Depachika and konbini {EST}</td><td>no booking, no language, no wait</td></tr>
  </table>
</div>

<p>The counter layer is where a first trip&#8217;s best meals almost always happen, and it is
the one the planning instinct skips because it cannot be booked from Ohio in February. A ramen
shop with a vending machine at the door is not a downgrade from a restaurant &#8212; it is the
form the cuisine takes at its most serious, and the machine exists because the cook would
rather be cooking than taking your order. {EST}</p>

<h2>Ordering when you cannot read the menu</h2>

<p>This is the anxiety that keeps people in hotel restaurants, and it dissolves faster than
anyone expects. Ticket machines have photographs, and increasingly an English button. Plastic
food models in the window are a genuine ordering system, not a curiosity &#8212; you may point
at one. Many counters serve one thing, so sitting down is most of the order. And the reliable
fallback everywhere is to look at what the person beside you is eating and indicate that you
would like the same. {EST}</p>

<p>Slurping noodles is normal and faintly encouraged. Tipping is not done anywhere in the
country, and leaving money on a table causes confusion rather than pleasure. {EST} Payment
usually goes onto a small tray at the register rather than into a hand.</p>

<h2>What to book</h2>

<p>Two meals for a fortnight is the right order of magnitude &#8212; the one or two evenings
you would be genuinely sorry to miss, and nothing else. A kaiseki dinner, a specific sushi
counter, the ryokan meal that comes with the room: those are worth the calendar. Everything
else is better found than scheduled, because the upside sits in exactly the places
that do not take a reservation from abroad. A restaurant that eagerly accepts foreign
bookings months out is telling you something about who its customers are. {EST}</p>

<p>The failure mode here is not hunger. It is spending an extraordinary food country executing
a spreadsheet, and arriving home having eaten well but never once walked into somewhere
because it smelled good.</p>
""",
}

MONEY = {
 "kind": "Money",
 "title": "Where it leaks",
 "standfirst": "Japan is not an extractive destination. What it has instead is a handful of "
               "small, avoidable leaks.",
 "body": f"""
<p class="lede">It is worth saying plainly, because it contradicts the reflex an American
brings from other famous destinations: nobody in Japan is trying to take your money. There is
no tipping, no haggling, no dual-pricing, no menu with a different number for you, and the
scams that organise a trip to certain other capitals essentially do not feature. {EST} The
corpus behind this book contains almost no warnings of that kind, which is itself the finding.</p>

<p>What exists instead is leakage: money that goes nowhere useful because of a decision made
early and never revisited.</p>

<div class="ledger">
  <div class="lcap">The four leaks, largest first</div>
  <table>
    <tr><th>Leak</th><th>Where it is dealt with</th></tr>
    <tr><td>A rail pass on a route that does not need one {OFF}</td><td>Decision 02</td></tr>
    <tr><td>Peak-season rooms bought for a probability {EST}</td><td>Decision 04</td></tr>
    <tr><td>A ryokan judged on its rate rather than its inclusions {EST}</td><td>Decision 06</td></tr>
    <tr><td>A bigger room further out, paid for in daily transfers {EST}</td><td>Where to stay</td></tr>
  </table>
</div>

<h2>Cash, still</h2>

<p>Cards are widely accepted in the places a first trip spends most of its money, and the
country has moved a long way toward contactless. The exceptions are specific and worth
knowing: smaller and older restaurants, market stalls, temple and shrine entry fees and
charms, and rural businesses are still commonly cash-only. {EST} Carrying a modest amount of
cash removes the problem entirely, and the stored balance on a transit card covers a
surprising share of the small purchases besides.</p>

<h2>One administrative note</h2>

<p>Tax-free shopping registration through the government&#8217;s pre-arrival web service has
been changing, and the separate registration step it used to offer is being retired. {OFF}
This is exactly the class of fact that belongs on the Field Sheet rather than in a book: check
the current process close to departure rather than trusting any printed description of it,
including this one.</p>
""",
}

EXTRAS = [EATING, MONEY]
