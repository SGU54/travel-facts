# prose.py — the framing matter. Contract, method, TOC, the refusals page, the send-off.
from content import E,O,S,V

OPENING = f"""
<div class="op-plate">
<div class="op-brand">ROME, SOLVED.</div>
<div class="op-rule"></div>
<div class="op-sub">A DECISION MANUAL FOR FIRST-TIME AMERICAN VISITORS</div>
</div>
<p class="b drop">Most Rome guides are encyclopedias: everything about everything, sorted
alphabetically, leaving the actual choosing to you at the worst possible moment — jet-lagged,
over-optioned, standing in a piazza while a man with a laminated menu explains why his is
the good one. This is not that. This book makes calls. It tells you where to sleep, what to
book before you fly, what to skip without regret, and exactly which small American habits
will cost you money or mornings — and then it shows its work, so that when you disagree, you
disagree from a position of knowledge and come out ahead anyway.</p>
<p class="b">The whole thing rests on one fact about Rome that reorganises everything else:
the city you came to see is smaller and more walkable than it looks, and the subway
famously cannot reach its heart. Get that right — sleep inside the ring, walk the centre,
stop reaching for trains that don't go where you're going — and half the classic mistakes
never get the chance to happen. The other half are habits: paying in dollars, tipping on
reflex, eating within sight of the fountains, buying passes for rides you'll never take.
Each one gets a page, a verdict, and the reasoning behind it.</p>
<p class="b">A word on what this book refuses to do. It names no hotels and no restaurants,
prints no ticket prices, and republishes no star ratings — not from timidity, but because
those are exactly the things that rot fastest and mislead most, and a manual that pretends
otherwise is lying to you about its own shelf life. What travels well is judgment: the
filter that survives every menu change, the sequence that beats every crowd, the rule
underneath the fact. The perishable numbers live in one place, the Field Sheet at the back,
dated and quarantined so you always know how fresh they are. Everything else is built to
last the life of a trip — and the trip after that.</p>
"""

HOWTO = f"""
<div class="eyebrow">HOW TO READ THIS BOOK</div>
<h1 class="t">Two documents, and a system of marks</h1>
<div class="standfirst">The book is stable; the world isn't. This page is how the design keeps
those two truths apart, so you always know which kind of claim you're holding.</div>
<p class="b">Every fact in these pages carries a small mark that tells you how durable it is —
whether it's the kind of thing that will still be true in two years, or the kind you must
check before you fly. Learn the four marks once and the book becomes self-documenting.</p>
<table class="marks">
<tr><td class="m">{E}</td><td class="md">ESTABLISHED</td><td>Stable facts of the city — its
geography, its food canon, the way its evenings run. Won't move in the life of this edition.</td></tr>
<tr><td class="m">{O}</td><td class="md">OFFICIAL</td><td>Rules and postures set by an authority
— dress codes, advisory levels, fines, closure days. Firm, but authorities revise them.</td></tr>
<tr><td class="m">{S}</td><td class="md">SURVEYED</td><td>Observed patterns and current practice,
dated where it matters — the quiet hours, the transit habits, the eSIM call. True as seen.</td></tr>
<tr><td class="m">{V}</td><td class="md">VOLATILE</td><td>Prices, live availability, launch
dates. These the book will not print — they live only on the Field Sheet, dated.</td></tr>
</table>
<p class="b">Hence the two documents. <b>The book</b> — everything up to the back-matter — is
the durable analysis: read it once before you go, and it holds for years. <b>The Field
Sheet</b> — the final pages, printed on its own banner — is the perishable layer: the fares,
the horizons, the dated authorisations, reissued every quarter. When the two ever seem to
disagree, the Sheet is the newer word, and the official source it names is newer still.</p>
<p class="b">On the ground, you need almost none of it. The decisions are made at home; the
Kit page near the back compresses the book to a single pocket card. Screenshot that,
carry the Field Sheet, and leave the rest on the shelf where it's working for your next
trip. {E}</p>
"""

def CONTENTS(pagemap):
    def row(num,title,dots=True):
        return (f'<div class="tocrow"><span class="tt">{title}</span>'
                f'<span class="tp">{num}</span></div>')
    secs=[("The ground — why Rome is smaller than it looks","I"),
          ("Before you fly — the checklist with deadlines","II"),
          ("Day zero — the landing, solved","III"),
          ("Timing — the week and the season","IV"),
          ("The fourteen decisions","—"),
          ("Set pieces — the Colosseum & the Vatican","V"),
          ("Eating — the filter and the canon","VI"),
          ("Money — where it leaks","VII"),
          ("The plan — three days, hour by hour","VIII"),
          ("Where to stay — six bases, one yardstick","IX"),
          ("The fourth day — every escape, priced","X"),
          ("Failure modes — twenty ways it goes wrong","XI"),
          ("The kit — the wallet card","XII"),
          ("What this book won't tell you","—"),
          ("The Field Sheet — verified at press time","§")]
    body="".join(f'<div class="tocrow"><span class="tt">{t}</span>'
                 f'<span class="tnum">{n}</span></div>' for t,n in secs)
    return f"""
<div class="eyebrow">CONTENTS</div>
<h1 class="t">What's inside</h1>
<div class="standfirst">Fifteen movements, front to back — the analysis first, the perishable
numbers quarantined at the end.</div>
<div class="toc">{body}</div>
<div class="toc-note">Roman numerals mark the twelve chapters; the fourteen decisions run as
a single sequence between chapters four and five; the Field Sheet stands on its own at the
back, dated and reissued quarterly. {E}</div>
"""

BACKMATTER = f"""
<div class="eyebrow">THE REFUSALS</div>
<h1 class="t">What this book won't tell you</h1>
<div class="standfirst">A manual is defined as much by what it leaves out as by what it
commits to. Here is what we withhold, and the reasoning in each case — so the omissions read
as discipline, not gaps.</div>
<div class="ref">
<div class="ri"><h4>No hotel names</h4><p>The right base is a <i>neighborhood</i> decision,
and that we make plainly (Decision 01). Which specific property is right for your dates,
budget and taste changes faster than any book prints, and a named list would only age into
bad advice. We give you the map and the yardstick; you run the search with today's inventory. {E}</p></div>
<div class="ri"><h4>No restaurant names</h4><p>The rule outlives the list. A filter you can
run from the pavement — Decision 10 — survives every closure, chef change and rent rise that
would turn a named recommendation stale by spring. Learn the tells, order the canon, walk
the ninety seconds. That travels; a list does not. {S}</p></div>
<div class="ri"><h4>No prices, in the book</h4><p>Every fare, fee and ticket price lives on
the Field Sheet, dated and quarantined — never in the body. A price printed in the analysis
is a small lie about how long the analysis lasts. The levers that set your budget are
durable and here; the numbers are perishable and there. {V}</p></div>
<div class="ri"><h4>No republished ratings</h4><p>Star averages are a snapshot of a crowd's
mood, gamed as often as earned, and meaningless a season later. We'd rather hand you the
reasoning to judge a room yourself in ten seconds than a number that outsourced the judgment
to strangers. {S}</p></div>
<div class="ri"><h4>No nightlife, shopping or deep accessibility guide</h4><p>This is a
first-visit decision manual, and it stays in its lane rather than padding. Rome's clubs,
its boutiques, and the genuine specifics of step-free access each deserve their own honest
treatment — more than a bolted-on chapter here could give. {E}</p></div>
<div class="ri"><h4>No flight strategy</h4><p>Airfare is its own moving science, decided
before this book's job begins and untethered from anything specific to Rome. We start the
moment you've landed — where the choices are Roman, and ours to have an opinion about. {E}</p></div>
</div>
<div class="colophon">
<div class="cbrand">ROME, SOLVED.</div>
<p>A decision manual from romeforamericans.com · First edition, 2026.07 · Issued with the
quarterly Field Sheet. The book holds what is stable; the Sheet holds what is not. Written
for the traveller who would rather understand the call than be handed it.</p>
</div>
"""

CLOSING = f"""
<div class="eyebrow">CLOSING</div>
<h1 class="t">Then put the book down</h1>
<div class="standfirst">You booked the four things. You know the marks, the filter, the ring.
The rest of Rome is supposed to happen to you.</div>
{{PHOTO_A10}}
<p class="b">Here is the paradox this book has been building toward: the point of planning
Rome this carefully is to earn the right to stop planning it. Once the Borghese slot is
held, the Vatican morning is booked, the base is inside the ring and the dollars-or-euros
reflex is broken, the machinery recedes and the city steps forward. The unplanned hours —
the church you ducked into for shade that held a Caravaggio, the trattoria one turn off the
piazza, the fountain you found by getting pleasantly lost — those were never going to come
from an itinerary. They come from having handled everything an itinerary is for, so that
your attention is free when Rome offers them.</p>
<p class="b">Cross Ponte Sant'Angelo at dusk on your last evening, Bernini's angels going to
silhouette and the dome catching the last of the light downriver, and the whole argument of
this book resolves into something you can feel: the walking was the sightseeing, the
proximity was the plan, and the evening is entirely yours. That is Rome, solved — not
reduced to a checklist, but freed from one.</p>
"""
