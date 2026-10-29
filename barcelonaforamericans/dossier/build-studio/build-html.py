# -*- coding: utf-8 -*-
"""Assemble dossier3.html — the full book, second pass.
Fixes the CLUMSY verdict: a reasoning block in every decision, five new
chapters, and two more figures to break the text run."""

CSS = open('dossier.css').read()
MAP_NB = open('assets/map-neighborhoods.svg').read()
MAP_DT = open('assets/map-daytrips.svg').read()
FIG_MO = open('assets/fig-months.svg').read()
FIG_HZ = open('assets/fig-horizons.svg').read()
FIG_TR = open('assets/fig-traps.svg').read()
FIG_ZN = open('assets/fig-zone.svg').read()
FIG_WK = open('assets/fig-week.svg').read()
FIG_CQ = open('assets/fig-consequence.svg').read()


import os
def _img64(slot):
    # file reference, not base64: a 3MB data-URI DOM makes Paged.js exceed its
    # pagination timeout. The PDF embeds the image data on output regardless.
    return f'img/{slot}.jpg'

def photo(slot, cap, cls="wide"):
    """A NUMBERED plate. The letter is stamped after BODY is assembled, not here.

    It used to derive from the slot (A04 -> PL. D), which was fine while there
    were seven slots named A01..A07 and meant the label survived re-ordering.
    With 37 plates that scheme runs out at Z, and the slots are now named for the
    chapter they belong to. Letters are therefore assigned in READING order by
    _stamp_plates() below — which is also the only way to guarantee what the
    claims gate checks: no label used twice, and no gap in the sequence.
    """
    return (f'<figure class="photo {cls}">'
            f'<img src="{_img64(slot)}" width="1100" height="733" decoding="sync" loading="eager"/>'
            f'<figcaption><span class="pl">PL. §</span> &nbsp;{cap}</figcaption></figure>')

def band(slot, cap):
    """A chapter's HEAD band: the plate directly under the standfirst.

    Unnumbered on purpose. It is chapter furniture, like the kicker and the rule
    above it — every chapter has one, so a label would number the chapters rather
    than identify a plate, and it would exhaust the PL. series on decoration.
    The renderer never moves a band: _PHOTO_RE excludes `photo band`, because a
    tail-feed applied to one silently drags a chapter's opening image to its end.
    """
    return (f'<figure class="photo band">'
            f'<img src="{_img64(slot)}" width="1100" height="733" decoding="sync" loading="eager"/>'
            f'<figcaption>{cap}</figcaption></figure>')

def _stamp_plates(body):
    """Replace each PL. § with its letter, in the order the reader meets them."""
    MARK = 'PL. \u00a7'
    out, n = [], 0
    i = 0
    while True:
        k = body.find(MARK, i)
        if k < 0:
            out.append(body[i:]); break
        out.append(body[i:k])
        out.append('PL. ' + chr(65 + n))
        n += 1
        # len(), not a hard 6. '§' is one CHARACTER but two UTF-8 bytes, and the
        # hard-coded 6 ate the '<' of the closing </span> — every caption printed
        # as "PL. L/SPAN>".
        i = k + len(MARK)
    assert n <= 26, f'{n} numbered plates — the PL. series only runs to Z'
    return ''.join(out), n

def rh(s): return f'<span class="rh-src">{s}</span>'

COVER = '''
<div class="coverpage">
  <div class="cv-band"></div>
  <div class="cv-top"><span>Barcelona · for Americans</span><span>The Field Manual</span></div>
  <div class="cv-mid">
    <div class="cv-stamp">A Decision Manual</div>
    <h1>BARCELONA,<br>WITHOUT<br>THE <span class="b">TRAPS.</span></h1>
    <div class="cv-sub">How the city separates visitors from their money and their days — and the handful of calls that defend against it.</div>
    <div class="cv-rule"><span class="seg"></span><span class="d"></span><span class="seg"></span></div>
    <div class="cv-meta">
      Seven decisions, scored &nbsp;·&nbsp; the four-trap money web, solved<br>
      Where to base &nbsp;·&nbsp; how to sequence &nbsp;·&nbsp; the 2026 apartment trap<br>
      A stable <b>Book</b>, and a dated <b>Field Sheet</b> you re-check before you fly
    </div>
  </div>
  <div class="cv-strip"><img src="__COVERIMG__" width="1100" height="733" decoding="sync" loading="eager"/></div>
  <div class="cv-foot"><span>barcelonaforamericans.com</span><span>Edition 1 · 2026</span></div>
</div>'''
COVER = COVER.replace('__COVERIMG__', _img64('A01'))

OPENING = f'''
<section class="dec chap" id="contract">
  {rh("The contract")}
  <div class="kicker">Before anything else</div>
  <h1>The Contract</h1>
  <div class="standfirst">This book answers how to think about Barcelona, not merely what to see — so you can disagree with us and still come out ahead.</div>
  {band("h-contract", "The fabric the arguments are about. Every call in this book is finally about a street like this one, and which of them you sleep on.")}
  <p class="first dropcap">Every guide to Barcelona will tell you the same forty things: see the Sagrada Família, book Park Güell, watch your pockets on La Rambla. That information is free, infinite, and (six weeks before your trip, with thirty browser tabs open) completely useless as a way to <em>decide</em>. The problem was never a shortage of facts. It is that no single article holds the city in mind all at once and tells you which facts carry weight, and what they cost you when you get them wrong.</p>
  <p>That is the one thing this book does. Each of the calls that follows connects facts the free articles leave scattered: the tourist tax quoted nowhere in your nightly rate, the airport ticket your metro pass silently won't cover, the apartment booking that has quietly become a liability. None of these is secret. Each sits a page or two apart from the fact that would defend against it, on some website you'll never think to cross-reference at the right moment. The book puts them in one place, with the arithmetic shown, so the judgment is yours.</p>
  <p>We are not neutral. Every decision here ends in a verdict: a call you can argue with. Where we say stay in the Eixample, book the apartment only with a licence number, take Montserrat first, that is a position, and we show the reasoning so you can overrule it for your own trip. A guide that refuses to commit is just the forty facts again, rearranged. This one commits.</p>
  <p>A word on who this is for. It assumes a first or second visit, an American frame of reference, and a trip of roughly three to seven days, which is where nearly all the expensive mistakes cluster. If you have been four times and have opinions about which market has the better fishmonger, you already know most of this and should spend your money elsewhere. If you are going for a month, the calculus on apartments and transit changes and you should treat those two chapters as directional rather than binding. Everything in between is squarely the intended reader, and the calls are tuned for that case rather than hedged to cover every case badly.</p>
  <p>One more promise, about what this book deliberately isn't. It names no hotels and no restaurants. Those lists are what every free guide already sells, and they are wrong within a season: a place changes hands, a chef leaves, a street turns. What survives is the <em>rule</em>: which neighborhood suits which traveller and why, what a tourist-trap plate looks like from the doorway, which meal of the day carries the value. Learn the rule and you can walk into a street you have never heard of and order well. That is the trade this book makes on every page, and the last chapter says so plainly.</p>

  {photo("p-contract", "What the rules buy you: a street you had never heard of, ordered well.", "wide")}
</section>'''

HOWTO = f'''
<section class="dec chap" id="howto">
  {rh("How to read this")}
  <div class="kicker">The apparatus</div>
  <h1>How to Read This</h1>
  <div class="standfirst">Two documents, five marks, and one habit that makes it work on the trip.</div>
  {band("h-howto", "Where this book is meant to be read. The Book is for the desk; only the Field Sheet and the wallet card travel.")}
  <p class="first">This is built as two things. <strong>The Book</strong>, what you are holding, is the stable analysis: the calls, the reasoning, the geography. It is true for a couple of years, because it is about how the city is shaped rather than what a ticket costs this week. <strong>The Field Sheet</strong> is the dated annex, and it travels as its own sheet: the volatile figures (tax rates, ticket prices, the menú del día band) that move often enough that printing them in the body would date the book. When a claim rests on a number that drifts, it is marked, and the current figure lives on the Sheet.</p>
  <p>Every claim carries a mark, so you always know what kind of fact you are leaning on:</p>
  <div class="markskey">
    <div class="row"><span class="g mk est">&#9679;</span><span><strong>Established.</strong> Structural, durable — how the city and its systems are built. Won't change before your trip.</span></div>
    <div class="row"><span class="g mk off">&#9671;</span><span><strong>Official.</strong> A published rule or regulated figure — a licence regime, a fixed fare structure.</span></div>
    <div class="row"><span class="g mk sur">&#9650;</span><span><strong>Surveyed.</strong> An observation with a date — a crowd pattern, a light at an hour. True when checked; verify if it matters.</span></div>
    <div class="row"><span class="g mk call">&#9672;</span><span><strong>Our call.</strong> A judgment rather than a finding: a ranking, a recommendation, a trade we think is worth making. These are the ones to argue with.</span></div>
    <div class="row"><span class="g mk vol">&#9670;</span><span><strong>Volatile.</strong> A live price or schedule. The current value is on the Field Sheet — re-check before you rely on it.</span></div>
  </div>
  <p>The marks are not decoration. They tell you how much weight a sentence can bear. A structural claim you can plan a trip around; a surveyed observation you should sanity-check if a morning depends on it; a volatile figure you should never quote back to anyone from these pages. And a call marked <span class="mk call">&#9672;</span> is ours, not the city's, where we rank the day trips or name a default neighborhood, that is a position taken on your behalf, and the reasoning is shown precisely so you can reach a different one. Most guides blur all five into a single confident voice, which is why they age badly, and why you can never tell which parts to re-verify and which parts were only ever somebody's preference.</p>
  <p>There is one more reason the two documents are separate, and it is practical rather than editorial. A book that mixes durable analysis with live prices cannot be trusted a year later, because you cannot tell by looking which sentences have aged. Splitting them means the Book can be read with confidence at any point in its life, and the Sheet can be replaced without touching a word of the argument. If you are reading this well after the compiled date on the Sheet, the calls still stand; go and refresh the numbers, and nothing else needs re-checking.</p>
  <p>The habit: read the Book once at home to make your decisions, then carry the Field Sheet and the wallet card on the trip. The Book is for deciding; the Sheet is for the day. Don't try to memorise prices from these pages: that is what the Sheet is for, and it is the part we keep current.</p>

  {photo("p-howto", "The city the marks are about &mdash; durable where it is built, volatile where it is priced.", "wide")}
</section>'''

TOC = f'''
<section class="dec chap" id="contents">
  {rh("Contents")}
  <div class="kicker">What's inside</div>
  <h1>Contents</h1>
  <nav class="toc">
    <a href="#ground"><span class="num">I</span><span class="t">The Ground — how Barcelona takes your money</span><span class="dots"></span></a>
    <a href="#fly"><span class="num">II</span><span class="t">Before You Fly — the checklist, with deadlines</span><span class="dots"></span></a>
    <a href="#dayzero"><span class="num">III</span><span class="t">Day Zero — the arrival</span><span class="dots"></span></a>
    <a href="#timing"><span class="num">IV</span><span class="t">Timing — the shape of the year</span><span class="dots"></span></a>
    <a href="#setpieces"><span class="num">V</span><span class="t">The Set Pieces — order of operations</span><span class="dots"></span></a>
    <a href="#d01"><span class="num">01</span><span class="t">Where to base</span><span class="dots"></span></a>
    <a href="#d02"><span class="num">02</span><span class="t">The apartment question — the 2026 trap</span><span class="dots"></span></a>
    <a href="#d03"><span class="num">03</span><span class="t">The money-trap web</span><span class="dots"></span></a>
    <a href="#d05"><span class="num">04</span><span class="t">Sequencing the days</span><span class="dots"></span></a>
    <a href="#d06"><span class="num">05</span><span class="t">The Gaudí fork</span><span class="dots"></span></a>
    <a href="#d07"><span class="num">06</span><span class="t">Which day trip</span><span class="dots"></span></a>
    <a href="#d08"><span class="num">07</span><span class="t">How not to eat like a tourist</span><span class="dots"></span></a>
    <a href="#horizons"><span class="num">VI</span><span class="t">The Horizons — what to book, and when</span><span class="dots"></span></a>
    <a href="#risk"><span class="num">VII</span><span class="t">How worried should you be?</span><span class="dots"></span></a>
    <a href="#plan"><span class="num">VIII</span><span class="t">The Plan — the days as operations</span><span class="dots"></span></a>
    <a href="#fail"><span class="num">IX</span><span class="t">Failure Modes — by consequence</span><span class="dots"></span></a>
    <a href="#wallet"><span class="num">X</span><span class="t">The Wallet Card</span><span class="dots"></span></a>
    <a href="#back"><span class="num">XI</span><span class="t">What This Won't Tell You</span><span class="dots"></span></a>
    <a href="#beforeyoubook"><span class="num">·</span><span class="t">Before you book — decide these first</span><span class="dots"></span></a>
    <a href="#fs"><span class="num">&#9670;</span><span class="t">The Field Sheet</span><span class="dots"></span></a>
  </nav>
</section>'''

GROUND = f'''
<section class="dec chap" id="ground">
  {rh("The Ground")}
  <div class="kicker">The organising fact</div>
  <h1>The Ground</h1>
  <div class="standfirst">Barcelona doesn't overcharge you once. It charges you four small times, in four different places, and counts on you never seeing the pattern.</div>
  <p class="first dropcap">Here is the thing that reorganises a Barcelona trip once you see it. The city is very good at tourism, which means it is very good at the small, defensible extraction: the charge that is real, legal, and quoted just out of sight until the moment you pay it. No single one is large enough to resent. That is the design. The tourist tax isn't in your room rate. The airport ticket isn't the one your metro card holds. The card terminal offers you dollars with a helpful smile. The bright-blue ATM by the cathedral is happy to help. Each is a small leak; scattered across a week they are a real number, and because they arrive separately you never add them up.</p>
  <p>This is not a complaint about Barcelona, and it is not a claim that the city is dishonest. Every one of these charges is posted somewhere, legal, and in most cases funds something defensible. The point is structural: they are <em>distributed</em>. A visitor meets them one at a time, in four different moods: at check-out when you are leaving, at a gate when you are rushed, at a terminal when someone is waiting behind you, at a table when you are hungry. Each moment is individually a bad moment to do arithmetic. The city does not need to hide anything; the scattering does the work.</p>
  {band("A02", "The tourist spine at work. Nothing here is illegal, hidden, or even unusual — which is precisely why it costs so many visitors so much.")}
  <p>Everything downstream of this fact is defence. Where you sleep determines how much you walk versus pay to move. How you sequence the days determines whether you get the good version of each sight or the rushed one. What you order at lunch determines whether the city's food reputation works for you or against you. The calls in this book are not a list of sights ranked, the free web has that, they are the moves that keep the extraction machine from running on you by default.</p>
  <p>It is worth naming what this book is <em>not</em> claiming, because the honest version is more useful than the outraged one. Barcelona is not unusually expensive by Western European standards, and it is not unusually predatory. What it is, is unusually <em>practised</em>: a city that has hosted enormous visitor numbers for decades and has, over that time, evolved a dense and legal infrastructure for converting visitors into revenue at every plausible touchpoint. That infrastructure is not a conspiracy. It is what any city becomes when tourism is a major industry and nobody stops it. Knowing that changes your posture from indignation to preparation, which is the only posture that saves you anything.</p>
  <p>The sharpest single instance, the four-trap money web, is decision 03, and it is the one we would hand a friend for free. If you read only one page, read that one. The rest of the book applies the same discipline to the choices that cost you a day, or the shape of the trip, rather than a fistful of euros.</p>
  <h2>Why the metro map lies to you</h2>
  <p>The obvious tool for a compact European city is a transit pass, and Barcelona's is genuinely good <span class="mk est">&#9679;</span>, metro, city buses, trams, the Montjuïc funicular and the local rail lines run on one integrated fare system, and almost everything a visitor wants sits inside Zone 1. But the tool has a hole positioned exactly where you are most rushed. The standard multi-ride ticket, the T-casual, does not work at the airport metro <span class="mk est">&#9679;</span>. Visitors tap it all week, arrive at the airport with rides to spare, and are stopped at the gate needing a different ticket with a flight boarding.</p>
  <p>Say what the hole is, precisely, because the opposite mistake costs money too: it is the T-casual and the single ticket that stop at that gate. Other titles do carry you through it &#8212; the monthly T-usual, and the Hola Barcelona travel card, which includes the airport metro both ways inside its validity. So the rule is not &#8220;buy a separate airport ticket&#8221;, it is: <strong>check whether the ticket you already hold covers Zone 1 including the airport, and buy the airport ticket only if it does not</strong>. If you are on a T-casual, it does not.</p>
  <figure>{FIG_ZN}<figcaption>FIG. 1 &middot; One integrated system, one gap — and the gap is at the airport</figcaption></figure>
  <p>That is the city in miniature: a competently built default tool with one gap sited precisely where a visitor can least absorb it. It is why the transit question is folded into the money web rather than given a chapter of its own. It is not really a transit decision. It is one of the four extractions, wearing a transit costume.</p>

  {photo("p-ground", "The tourist-facing retail of a city that is very good at tourism. All of it legal, all of it posted.", "wide")}
</section>'''

FLY = f'''
<section class="dec chap" id="fly">
  {rh("Before You Fly")}
  <div class="kicker">The checklist</div>
  <h1>Before You Fly</h1>
  <div class="standfirst">Everything with a deadline, in deadline order. Most of it takes minutes; all of it is painful to discover at the airport.</div>
  {band("h-fly", "Everything on this list is cheaper and calmer now than it will be at a gate.")}
  <p class="first">The trip is largely decided before you leave. Two bookings truly bind, a handful of small preparations prevent the most common headaches, and one category, border paperwork, is mostly noise you can safely ignore this year, provided you know which part is real.</p>
  <h2>Weeks ahead</h2>
  <ul class="clean">
    <li><span class="deadline">On release</span> &nbsp; <strong>Sagrada Família.</strong> Book a morning slot on sagradafamilia.org, the only official seller <span class="mk off">&#9671;</span>. This is the binding constraint of the whole trip; everything else bends around it. Book the day your dates first appear: the calendar opens a fixed window ahead, not indefinitely, and the mornings go first. If your dates are not listed yet that is a release date, not a sell-out &#8212; do not pay a reseller over it. Authorised resellers hold real allocations <span class="mk off">&#9671;</span> only when the official calendar is genuinely full.</li>
    <li><span class="deadline">6 weeks</span> &nbsp; <strong>Park Güell.</strong> The monumental zone is timed and slotted. Book it, and book it early in the day.</li>
    <li><span class="deadline">8 weeks</span> &nbsp; <strong>Accommodation.</strong> In the centenary year the good central stock goes early. If you are considering an apartment, read decision 02 first — the licensing regime has changed the calculus.</li>
  </ul>
  <h2>The week before</h2>
  <ul class="clean">
    <li><strong>Tell your bank you are travelling</strong> — or set the travel notice in the app, so a Barcelona charge doesn't trigger a fraud freeze on day one <span class="mk call">&#9672;</span>.</li>
    <li><strong>Check your cards' foreign-transaction fees</strong> and bring the one or two that charge none. This pairs with the DCC rule in decision 03: the card is only half the defence, the answer you give at the terminal is the other half.</li>
    <li><strong>Buy an eSIM</strong> rather than relying on your US carrier's roaming <span class="mk call">&#9672;</span>. You install it before you fly and land with working data and no surprise bill. Roaming plans range from fine to painful, and the airport is a bad place to find out which you have.</li>
    <li><strong>Screenshot your bookings</strong> — including, if you booked an apartment, the licence number. Paper beats a dead phone at a door.</li>
  </ul>
  <h2>The border, calmly</h2>
  <p>Two European systems generate more anxiety and more scam websites than anything else on an American traveller's list. The accurate version for 2026: <strong>EES</strong>, the biometric entry–exit check, is live, fingerprints and a photo at the border instead of a stamp, and you barely interact with it beyond standing still <span class="mk off">&#9671;</span>. <strong>ETIAS</strong>, the pre-travel authorisation, is <em>not</em> live and you do not need it for a trip this year <span class="mk off">&#9671;</span>.</p>
  <p>Everything else people worry about before a Barcelona trip is optional. You do not need a transit pass bought in advance, a museum pass, a guided tour booked from home, or a restaurant reservation for most nights. Those are all decisions better made on the ground, with local information, once you know how the week is unfolding. The list above is short because the list of things that truly bind is short — and confusing the two is how planning turns into a second job.</p>
  <p>That second sentence is the one worth carrying, because an entire industry of fraudulent sites exists to charge Americans for an ETIAS that does not yet apply. If a website offers to sell you one, that is the tell. Check the Field Sheet before you fly in case the timeline has moved — it is the kind of fact this book keeps in the dated annex rather than the body.</p>

  {photo("p-fly", "The last calm hour you will get to sort out ticketing. Use it on the return leg too.", "wide")}
</section>'''

DAYZERO = f'''
<section class="dec chap" id="dayzero">
  {rh("Day Zero")}
  <div class="kicker">The arrival</div>
  <h1>Day Zero</h1>
  <div class="standfirst">The most anxious hours of any trip are the first six, and almost no guide writes them. Here they are.</div>
  {band("h-dayzero", "The first six hours, where the trip is least prepared and most often overcharged.")}
  <p class="first dropcap">You land at El Prat jet-lagged, and the first decisions of the trip are the ones you are least equipped to make well. This is the day to under-plan on purpose. Do not put a timed ticket on arrival day — you will be too fried to use it well, and a missed Sagrada slot is money gone and a morning wasted. The job of day zero is narrow: get into the city without overpaying, stay awake until a local bedtime, and eat one good early dinner.</p>
  <h2>Getting in</h2>
  <p>The ride from the airport is where the first small extraction waits, and it is the one this book flags hardest. The airport metro is the one gate a T-casual will not open <span class="mk est">&#9679;</span> — in either direction. A Hola Barcelona or a T-usual does cover it, so check what you hold before you buy anything extra. Buy the right one now, and buy the return leg at the same time while you are calm rather than at a gate on your last morning. The alternatives (the airport bus, a taxi, a pre-booked transfer) are all legitimate. What matters is choosing deliberately instead of letting a taxi queue or a transfer tout choose for you before you have seen the arithmetic in decision 03.</p>
  <h2>The first afternoon</h2>
  <p>Resist the timed sight. Walk the Gothic Quarter, which asks nothing of you but attention and repays it immediately. Sit in a plaça. Buy water. If you can stay upright until Spanish dinner, from about half past eight <span class="mk call">&#9672;</span>, do, because eating on local time from the first night is the fastest way to stop feeling like a visitor. If you cannot, eat early and badly and forgive yourself; the trip starts properly tomorrow.</p>
  <p>One habit to start today, because it pays across the week: when a card terminal asks whether you would like to be charged in dollars, say no. Always euros. You will be asked perhaps a dozen times across five days, and the answer never changes.</p>

  {photo("p-dayzero", "Under-plan on purpose. The job of day zero is to reach a local bedtime, nothing more.", "wide")}
</section>'''

TIMING = f'''
<section class="dec chap" id="timing">
  {rh("Timing")}
  <div class="kicker">The shape of the year</div>
  <h1>Timing</h1>
  <div class="standfirst">Barcelona works year-round. What changes is heat, crowds, and whether the sea is in play — and only one of those three can spoil a trip.</div>
  {band("h-timing", "The same coast in the shoulder season. Nothing here is closed &mdash; there is simply nobody in it.")}
  <p class="first">The sweet spot is late spring and early autumn: May and June, September and October <span class="mk call">&#9672;</span>. Warm enough for the beach, not hot enough to flatten a day of walking, busy without the peak-summer crush. If your dates are flexible and you have no other constraint, book inside those four months and stop optimising.</p>
  <figure>{FIG_MO}<figcaption>FIG. 2 &middot; The year, coarsely — deliberately non-numeric, so it cannot go stale</figcaption></figure>
  <p>The trade-offs, if your dates are not flexible. <strong>July and August</strong> are the hottest and busiest, and the sea is at its warmest — a genuine argument for them if the beach is the point, and a genuine argument against if walking the Eixample at midday is. <strong>Winter</strong> is the quietest and cheapest stretch, mild by American standards, with the sea effectively out of play; the city itself is entirely intact, and the Gaudí interiors are considerably more pleasant without a queue in front of them.</p>
  <p>Festivals are the one thing that can override the seasonal logic entirely, in both directions. A major local festival turns an ordinary week into a memorable one and simultaneously makes accommodation scarce and expensive; if your dates happen to coincide with one, book much earlier than these pages otherwise suggest and treat the crowd guidance as optimistic. If you are actively crowd-averse, the same information tells you which weeks to avoid. Either way it is worth checking the calendar for your specific dates before committing, because the effect is large and entirely predictable.</p>
  <p>The 2026 wrinkle is the Gaudí centenary, which concentrates attention and crowds on the sights you came to see, Sagrada Família above all. It does not change which months are pleasant. It sharpens how far ahead you must book within any of them — treat the horizons later in this book as firmer this year than they would be in an ordinary one.</p>

  {photo("p-timing", "Late-spring light on ordinary rooftops. This is what the shoulder season is actually buying.", "wide")}
</section>'''

def decision(id_, num, cat, title, col_a, col_b, lede, cap, rows, reasoning, verdict, fors, againsts, note, fig=None, head=None, closer=None):
    rows_html = ''
    for opt, sub, num_cell in rows:
        rows_html += f'<tr><td><span class="opt">{opt}</span><span class="sub"> — {sub}</span></td><td class="num">{num_cell}</td></tr>'
    fa = '<div class="fa"><div class="col"><span class="lab">When the default holds</span>'
    for f in fors: fa += f'<p>{f}</p>'
    fa += '</div><div class="col"><span class="lab">When it doesn\'t</span>'
    for a in againsts: fa += f'<p>{a}</p>'
    fa += '</div></div>'
    figure = f'<figure>{fig[0]}<figcaption>{fig[1]}</figcaption></figure>' if fig else ''
    # a figure must not be wrapped in <p> — emit raw when the item is already markup
    def _reas_p(p):
        # '@nohyph ' prefix: this paragraph was measured breaking a word across
        # a PAGE TURN. Chromium has no hyphenate-limit-last:page, so the opt-out
        # is per-paragraph and has to be carried in the content.
        if p.lstrip().startswith('<figure'):
            return p
        if p.startswith('@nohyph '):
            return f'<p class="nohyph">{p[8:]}</p>'
        return f'<p>{p}</p>'
    reas = ''.join(_reas_p(p) for p in reasoning)
    return f'''
<section class="dec chap decision" id="{id_}">
  {rh(f"Decision {num} · {cat}")}
  <div class="kicker">Decision {num} · {cat}</div>
  <h1>{title}</h1>
  <div class="standfirst">{lede}</div>
  {band(head[0], head[1]) if head else ""}
  {figure}
  <table class="ledger">
    <caption>{cap}</caption>
    <thead><tr><th>{col_a}</th><th class="num">{col_b}</th></tr></thead>
    <tbody>{rows_html}</tbody>
  </table>
  {reas}
  <div class="verdict"><p>{verdict}</p></div>
  {fa}
  <div class="note">{note}</div>
  {photo(closer[0], closer[1], "wide") if closer else ""}
</section>'''

D01 = decision("d01","01","Base","Where to Base","OPTION","THE TRADE",
  "Where you sleep decides what kind of trip you have — because “central” in Barcelona means three incompatible things, and the mistake is picking the one whose character is wrong for your days.",
  "The base decision, by traveller · first-timer, 3–5 days",
  [("Eixample","the default: central, calm at night, deepest hotel stock, Gaudí on your walking route <span class='mk call'>&#9672;</span>","first trip"),
   ("El Born","medieval lanes, bars, the Picasso; central but lively after dark <span class='mk call'>&#9672;</span>","atmosphere"),
   ("Barceloneta / Poblenou","sand and boardwalk; Poblenou calmer and more local <span class='mk call'>&#9672;</span>","beach first"),
   ("Poble-sec","real prices, excellent eating, below Montjuïc; a metro hop from the core <span class='mk call'>&#9672;</span>","budget")],
  ["The reasoning is geometric before it is anything else. Barcelona's headline sights are not evenly distributed: the Gaudí anchors sit in and above the Eixample grid, the medieval density lies south-east of it, and the beach is east again. A base inside the Eixample puts the largest cluster on foot and everything else one short hop away — which is why it quietly saves money all week. Not because the rooms are cheaper, but because you stop paying to move.",
   photo("A03", "The grid from above. The base decision is geometric before it is anything else — and the geometry is invisible from the street.", "wide"),
   "The competing options each trade that geometry for a different good, and all three trades are legitimate. El Born trades quiet for atmosphere: you are inside the medieval city rather than a walk from it, and you accept bar noise as the price. The beach bases trade central access for the sea being fifty metres from the door — a superb trade if you will use it, a poor one if your itinerary is Gaudí and museums. Poble-sec trades a few minutes of metro for local prices and one of the better eating streets in the city.",
   "What none of them trade is safety or charm. There are no bad areas on this list, which is part of why the decision gets made carelessly. The failure mode is not picking somewhere unpleasant — it is picking a character that fights your itinerary and then paying for that mismatch twice a day for five days."],
  "<strong>First trip, no special agenda: the Eixample, and it isn't close.</strong> Central, quiet at night, deepest hotel stock, and it puts Gaudí's front doors on your walking route. Choose El Born only if atmosphere is the point and you sleep through noise; choose the beach only if you will actually be at the beach rather than commuting from it. Most first-timers who override the default are solving for a preference they do not really have.",
  ["<strong>Then El Born</strong> — if you came for the medieval city itself, want to walk out into it at night, and bar noise reads as life rather than nuisance."],
  ["<strong>Then skip the beach base</strong> — if your days are Gaudí, old city and Montjuïc, the beach is a place you visit, not sleep; basing there adds a daily commute to everything you came for."],
  "The one thing that has changed since your friends' 2019 trip: the apartment answer is now a real decision rather than a default. It is the next chapter. <span class='xref'>The nightly tax scales with hotel class — see the Field Sheet; sequencing is decision 04.</span>",
  fig=(MAP_NB, "FIG. 3 · The base decision — eight neighborhoods, the default in gold, anchor sights as diamonds"),)

D02 = decision("d02","02","Base","The Apartment Question","OPTION","THE MOVE",
  "If you would book an apartment the way you would in any other city — stop. Barcelona is eliminating tourist apartments entirely, and the naive move has quietly become the risky one.",
  "The apartment call, by traveller · inside the phase-out",
  [("First-timer, short trip","licence anxiety and a possible pulled booking, for a kitchen you won't use in three days <span class='mk call'>&#9672;</span>","book a hotel"),
   ("Family or longer stay","you want space and a kitchen, but the pull-risk is identical <span class='mk call'>&#9672;</span>","apart-hotel"),
   ("The determined apartment-booker","unlicensed listings that vanish; direct-transfer hosts with no recourse <span class='mk off'>&#9671;</span>","valid HUTB only")],
  ["The facts here are unusually settled for a travel question. In 2024 the city announced it would not renew its roughly ten thousand short-term tourist-apartment licences and would let them all expire by November 2028; in March 2025 Spain's Constitutional Court upheld the city's authority to do so <span class='mk off'>&#9671;</span>. This is not a proposal to be re-litigated on a forum. It is law on a countdown, and the motivation (a decade of apartments converting from homes into rentals, with the rent effects that follow) means the political pressure runs one direction only.",
   "Three consequences follow for a trip booked now. Licensed supply is shrinking, so what remains costs more and books earlier: the bargain flat-for-the-week deal that defined the last decade of Barcelona travel is going extinct on a schedule. A shrinking legal market makes room for unlicensed operators, so the listing pool you are browsing holds a rising share of places that should not be rented at all. And an unlicensed booking is not a legal abstraction — it is a reservation that can be pulled after you have paid, at the worst possible moment.",
   "The apart-hotel is the underrated answer, and the reason this decision has three rows rather than two. It gives you what people want from an apartment (space, a kitchen, room for a family) with the licensing and the recourse of a hotel. For most travellers leaning apartment for practical rather than romantic reasons, it is a straight upgrade rather than a compromise."],
  "<strong>For most American first-timers in this climate, the honest call is a hotel or an apart-hotel — not the apartment.</strong> What is left of the licensed market is pricier, books earlier, and sits in a pool increasingly padded with listings that should not exist. If you want a kitchen, the apart-hotel buys the feel without the licence roulette. Reserve the true apartment for when you have a valid HUTB number and real payment protection.",
  ["<strong>Then book it</strong> — you found a licensed place with a visible HUTB number, on a platform with payment protection, and you screenshotted the licence and the confirmation before flying."],
  ["<strong>Then don't</strong> — the listing quotes no licence number, or the host wants a direct bank transfer. That is the profile of the booking that disappears the week you arrive."],
  "<span class='mk vol'>&#9670; VOLATILE</span> — licences lapse on a rolling basis toward Nov 2028 and enforcement is tightening; re-check before booking any apartment. A valid licence is a <strong>HUTB number</strong> <span class='mk off'>&#9671;</span> — no HUTB, no booking. <span class='xref'>The neighborhood call is the previous decision; the tourist tax applies to apart-hotels too.</span>",
   head=('h-d02', 'The thing being bought. In 2026 the question is not whether it is nice but whether it is licensed.'), closer=('p-d02', 'The apart-hotel: the kitchen without the licence roulette, which is the call this chapter makes.'))

D03 = decision("d03","03","Money","The Money-Trap Web","WHAT IT COSTS","THE MOVE",
  "No single one of these will ruin your trip — which is exactly why they work. The city takes your money in four small bites, in four places, and counts on you never seeing the pattern. Here it is, in one place.",
  "The four extractions, and the defence · per couple, five days",
  [("The tourist tax you didn't budget","per person, per night, on top of the room rate; rose 1 Apr 2026 <span class='mk vol'>&#9670;</span> and lands at check-out","budget it"),
   ("The airport-metro ticket trap","T-casual and singles do not work at the airport metro <span class='mk est'>&#9679;</span>; Hola and T-usual do","right ticket"),
   ("The “pay in dollars?” prompt","the terminal or ATM offers USD on a helpful screen <span class='mk est'>&#9679;</span>; accept and you eat a markup <span class='mk sur'>&#9650;</span>","choose euros"),
   ("The tourist ATM and tourist lunch","blue standalone machines push DCC and layer fees <span class='mk est'>&#9679;</span>; the tourist dinner is the menú in reverse","bank ATM; eat the menú")],
  ["@nohyph Take them one at a time, because the defence differs. The <strong>tourist tax</strong> is charged per person per night on top of your room rate, and it rose on 1 April 2026 <span class='mk vol'>&#9670;</span>. It is neither a scam nor optional; it is simply quoted nowhere in the nightly rate you compared when booking, so it arrives as a surprise line at check-out. For two people over five nights it is a real number, and the entire defence is knowing it exists so you treat it as part of the room rather than meeting it at the desk on your last morning.",
   "The <strong>airport ticket</strong> catches the most people and is the only one of the four with a hard operational edge: your city ticket does not work at the airport metro, in either direction <span class='mk est'>&#9679;</span>. The cost of getting it wrong is not mainly the fare — it is standing at a gate sorting out ticketing while a flight boards. Buy the correct ticket on arrival and, critically, sort the return leg at the same time, while you are calm and have time.",
   "The <strong>dollars prompt</strong> is the purest of the four, because it is a question you will be asked out loud a dozen times. When a terminal or an ATM offers to charge you in dollars, it is offering to perform the currency conversion itself, at a rate it selects <span class='mk sur'>&#9650;</span>. Your own bank will almost always do better. The answer is euros, every time, without deliberation — and it is worth saying to your travelling companion once, at the start, so neither of you has to think about it again.",
   "The fourth is a habit rather than a charge: <strong>paying the tourist rate at the point of sale</strong>. It appears as the bright-blue standalone ATM clustered near the sights, which pushes the dollars prompt hard and layers its own fees on top <span class='mk est'>&#9679;</span> — a bank machine is the fix <span class='mk call'>&#9672;</span>. And it appears at the table, where the tourist-priced dinner is the exact inverse of the weekday lunch that locals price honestly. That thread gets its own chapter later, but it belongs on this page too, because it is the same mechanism in different clothes."],
  "<strong>The four moves take five minutes to internalise and defend the better part of a couple's discretionary week.</strong> Budget the bed tax so it cannot surprise you, buy the right airport ticket in both directions, say “euros” at every terminal, and pull cash from a bank machine. None of this is exotic and none of it needs an app — it needs knowing the four gates exist before you reach them. That is the entire edge: the charges are public, the pattern is not.",
  ["<strong>Nearly cashless?</strong> Three of the four still reach you at the card terminal — the dollars prompt is a card trap, not a cash one. “Cards only” is not “safe”."],
  ["<strong>Two nights rather than five?</strong> The tax shrinks toward a rounding error — but the airport ticket and the dollars prompt are flat and do not scale down. Those two reach you at the gate and on the flight home regardless."],
  "<span class='mk vol'>&#9670; VOLATILE</span> — the tax rates, the airport-ticket price and the menú del día band all move; current figures are on the Field Sheet. Re-check the tax before you budget: it has risen twice recently and is politically live. <span class='xref'>The airport ticket connects to Day Zero; the eating thread is decision 07.</span>",
  fig=(FIG_TR, "FIG. 4 · Where each one meets you — four moments across a single trip"),
   head=('h-d03', 'Four small charges, none of them large enough to resent. That is the design.'), closer=('p-d03', 'The gate the city ticket does not open. It is the one trap with a hard operational edge.'))

D05 = decision("d05","04","Time","Sequencing the Days","THE PIECE","COST OF THE WRONG SLOT",
  "Most itineraries treat the days as interchangeable boxes. They are not — three of the things you will do are time-locked in ways that collide, and slotting them wrong costs you the good version of each sight rather than the sight itself.",
  "The time-locked pieces, and where they belong · five days",
  [("Sagrada Família → a morning slot","the nave gold at 9:00–9:30, ahead of the crush <span class='mk sur'>&#9650;</span>","booked midday: the crush and the flattest light"),
   ("Arrival → a low-stakes afternoon","jet-lag-proof: old-city wander, early dinner, nothing timed <span class='mk call'>&#9672;</span>","a ticket you are too fried to use"),
   ("The day trip → a full clear day","Montserrat or Girona get the day they need <span class='mk call'>&#9672;</span>","wedged into a morning: a commute with a view"),
   ("The beach → a floating slot","moved to whichever afternoon turns warm <span class='mk call'>&#9672;</span>","pinned to a grey Thursday; never happens")],
  ["Sequencing matters more here than in most cities because Barcelona's signature experiences are not equally good at all hours, and two of them are booked weeks in advance — which means the mistake is locked in long before you arrive. Sagrada Família is the clearest case. The interior is the entire point, and the interior is a light show: the nave reads gold in the morning and fire-orange through the west windows late in the afternoon <span class='mk sur'>&#9650;</span>. Midday is both the crush and the flattest light. At the moment of booking you are choosing which version of the building you will see, and most people do not realise they are choosing at all.",
   "The day trip fails by a different mechanism. It does not degrade by hour; it degrades by compression. Montserrat wants a full day because the mountain, the monastery and the getting there <em>are</em> the trip <span class='mk call'>&#9672;</span> — wedged into a morning it becomes a commute with a view. It also belongs mid-trip rather than on your last full day, because that is the only position from which a grey forecast can still be swapped for a city day without losing the excursion entirely.",
   "The beach is the piece most often lost, and it is lost by the very act of scheduling it. Pin it to Thursday, and if Thursday turns grey it never happens — there is no slot left to move it into. Leave it deliberately unassigned, as the thing you do on whichever afternoon turns warm, and it happens almost every time. Arrival day, meanwhile, should hold nothing timed at all, for the reasons in Day Zero: you will be at your worst just when a timed ticket demands your best."],
  "<strong>Anchor three things and let everything else flow around them:</strong> Sagrada Família on a morning slot, the day trip on a full clear day mid-trip so a grey forecast can still be traded, and the beach kept deliberately unpinned. Arrival day holds nothing timed. Do this and every sight lands in its good version; skip it and you will technically see everything while getting the lesser cut of half of it. The order is the product here — the list is free on the blog.",
  ["<strong>Two or three days?</strong> The flex disappears and you pin the day trip too. Short trips cannot afford a weather buffer — take the Sagrada morning and accept the risk."],
  ["<strong>Five days feeling tight?</strong> Cut the day trip rather than rush it. A rushed Montserrat is worse than no Montserrat at all."],
  "<span class='mk sur'>&#9650; SURVEYED</span> — the morning-nave light and the crowd pattern are observations, not a published schedule; the after-16:00 slot is the fallback for west-window light. <span class='xref'>Which day trip to slot is decision 06; the booking horizons follow the decisions.</span>",
   head=('h-d05', 'The city keeps its own clock. Sequencing is the work of putting your day inside it.'), closer=('p-d05', 'The good version of the same view, which is a question of hour rather than of ticket.'))

D06 = decision("d06","05","Tickets","The Gaudí Fork","SITE","THE CALL",
  "Barcelona sells you a dozen Gaudí doors and implies you should walk through all of them. You should not — and the reason is attention rather than money. Three interiors in two days and the fourth is wallpaper.",
  "The Gaudí sites, ranked by what earns a ticket · first trip",
  [("Sagrada Família — the interior","the nave; the one building unlike any you have seen <span class='mk call'>&#9672;</span>","non-negotiable; morning slot"),
   ("Park Güell — the monumental zone","the mosaic terrace and the city view; timed and slotted <span class='mk call'>&#9672;</span>","worth it, booked, early"),
   ("One house: Batlló <em>or</em> La Pedrera","one dazzling interior and a rooftop; one is plenty <span class='mk call'>&#9672;</span>","pick ONE — two is saturation"),
   ("The rest (Vicens, Palau Güell…)","façades, enjoyable without the ticket queue <span class='mk call'>&#9672;</span>","free, from the street")],
  ["The scarce resource on a Gaudí itinerary is not money and it is not time — it is attention. These are dense, ornamented, high-information interiors, and they compete with one another for the same faculty. The first rearranges what you thought a building could be. The second is thrilling. By the fourth, a visitor who dutifully paid for all four is walking through a masterpiece checking their phone — and the disappointment gets blamed on the building rather than on the schedule that flattened it.",
   "So the fork is simply which few earn a ticket. Sagrada Família is not really a choice: the interior is the point, and no photograph prepares you for it. Park Güell earns its slot for the terrace and the view, with the practical note that riding up spares you a climb you will feel later in the day. Beyond those two, one house interior is the right dose (Casa Batlló for sheer invention, La Pedrera for the roof), and the second house is where saturation reliably begins.",
   "One practical note that changes the arithmetic for a lot of visitors: the two sites that earn a ticket are not near each other, and neither is near the third. Sagrada Família sits east of the grid, Park Güell well above it, and the Passeig de Gràcia houses in between. That is a real amount of movement, and it is the reason this chapter and the sequencing chapter have to be read together — two ticketed sites on the same day means crossing the city twice on someone else’s clock, which is how a pleasant morning turns into a logistics exercise.",
   "There is a second-order effect worth naming, because it is what makes the saturation trap expensive rather than merely tiring. Ticketed Gaudí sites are timed, which means each one costs you not just its admission but a fixed point in a day that would otherwise flex. Three ticketed interiors across a five-day trip means three mornings that cannot move, three commitments made weeks earlier against weather and mood you could not predict. Two is a schedule. Four is a timetable, and a timetable is the thing that makes people describe a holiday as exhausting.",
   "Everything else Gaudí, and there is a great deal of it, is a street pleasure. Casa Vicens, Palau Güell, the façades scattered through the Eixample: each rewards a two-minute stop on a walk between anchors, with no ticket, no queue and no scheduling. Treating them as encounters rather than destinations is what keeps the two you did pay for feeling like events."],
  "<strong>Two ticketed Gaudí sites and one house is the first-timer's sweet spot:</strong> Sagrada Família in the morning, Park Güell on your slot, and exactly one of Casa Batlló or La Pedrera. That is a full, un-saturated dose. Everything else folds into the walks between them. The saturation trap costs attention and money at once — the fourth interior you paid for is the one you barely see.",
  ["<strong>Modernisme is why you came?</strong> Batlló and Pedrera are a legitimate pairing if interiors do not blur for you. Know that it is an enthusiast's call rather than the default."],
  ["<strong>Crowds ruin things for you?</strong> In the centenary year Park Güell's monumental zone can disappoint — the free part of the park and a hilltop viewpoint may serve you better."],
  "<span class='mk vol'>&#9670; VOLATILE</span> — 2026 is the Gaudí centenary; demand, completion works and pricing all move this year. Book on sagradafamilia.org, the only official seller <span class='mk off'>&#9671;</span>; authorised resellers hold real allocations <span class='mk est'>&#9679;</span> when it is full. <span class='xref'>Morning-slot logic is decision 04; the horizons follow.</span>",
   head=('A04', 'The interior is the argument, and the argument is light. Book the hour and you are choosing which of these buildings you get to see.'), closer=('p-d06', 'Two ticketed sites is the dose. The third interior is where attention stops arriving.'))

D07 = decision("d07","06","Time","Which Day Trip","THE TRIP","WHO IT'S FOR",
  "The day-trip mistake is not a bad choice among the options — they are all good. It is choosing by proximity or by a photograph instead of by fit, and then spending a travel day on the wrong one for you.",
  "The day trips, by fit · one day, by train from Barcelona",
  [("Montserrat — take this one first","serrated mountain, monastery, Black Madonna; FGC R5 then cable car <span class='mk call'>&#9672;</span>","the one to take if you take one"),
   ("Girona — medieval city","walled old town and the Onyar houses; fast train <span class='mk call'>&#9672;</span>","history walkers; cobbles, slopes and steps"),
   ("Sitges — beach town","resort beaches and whitewashed lanes, just south <span class='mk call'>&#9672;</span>","a sea day, not a sightseeing one"),
   ("Figueres — the Dalí museum","the surrealist's own staged museum <span class='mk call'>&#9672;</span>","Dalí devotees, specifically"),
   ("Tarragona — Roman ruins by the sea","amphitheatre and Roman remains on the coast <span class='mk call'>&#9672;</span>","ruins people over cathedral people")],
  ["What makes this a decision rather than a ranking is that the five are not competing on quality — they are competing on what kind of day you want. Montserrat is a landscape day with a monastery in it: rounded rock spires, a working Benedictine community, a famous Black Madonna, and hiking if you want it. Girona is an architecture-and-wandering day on a short ride — but the old town climbs: cobbled slopes, the wall walk and steps at the cathedral. Sitges is frankly a beach with a handsome town attached. Figueres is a single-museum pilgrimage. Tarragona is Roman stone above the sea.",
   "Montserrat leads because it is the least substitutable. Medieval streets, good beaches and fine museums exist in many places; a serrated mountain with a monastery wedged into it, an hour from a major city, is rare, and it is the trip visitors report remembering longest <span class='mk sur'>&#9650;</span>. Its logistics sound fiddlier than they are — there is no direct train, so it is the FGC R5 from Plaça d'Espanya and then a cable car or rack railway up <span class='mk est'>&#9679;</span> — and that mild complexity is what makes people default to somewhere easier and then wish they had not.",
   photo("A05", "Medieval streets and good beaches exist in many places. This does not — which is the whole case for taking it first.", "wide"),
   "The specialist picks deserve their honesty. Figueres is superb if you care about Dalí and underwhelming if you do not, because it is essentially one attraction at the end of a longer ride. Tarragona is quietly excellent for anyone who prefers ruins to cathedrals and quietly disappointing for anyone who does not. Neither is a bad day. Both are the wrong day for the wrong person, which is the only kind of mistake available here."],
  "<strong>If you take one, take Montserrat.</strong> It out-memories the city for most visitors, and the mountain-plus-monastery has no substitute within reach. Swap to Girona if you would rather have a medieval city and no climbing, or Sitges if what you want is a beach day with a change of scene. Figueres and Tarragona are specialist picks — superb for the Dalí devotee or the Roman-ruins person, underwhelming if you are neither. The wrong day trip is not ruinous; it is a day spent on someone else's ideal day.",
  ["<strong>A full week?</strong> A mountain day and a beach or medieval day both fit comfortably. Two is fine across seven days."],
  ["<strong>City list already full at five days?</strong> A day trip is a subtraction rather than an addition. The city earns the time first."],
  "There is no direct train up Montserrat <span class='mk est'>&#9679;</span> — FGC R5 from Plaça d'Espanya, then cable car or rack railway. <span class='xref'>Where the trip sits in the week is decision 04.</span>",
  fig=(MAP_DT, "FIG. 5 · The day trips — real distances from Barcelona, the first-timer's pick in gold"),)

D08 = decision("d08","07","Eating","How Not to Eat Like a Tourist","THE TRAP","THE RULE",
  "Barcelona is one of the great eating cities and one of the easiest to eat badly in — because the streets you will naturally walk are lined with places built for visitors who do not know the tells.",
  "The four eating traps, and the rule that beats each",
  [("The paella photograph out front","frozen, pre-made, uniform neon yellow <span class='mk est'>&#9679;</span>","real rice is cooked to order"),
   ("All-day tapas on La Rambla","tourist-register plates at tourist prices on the main drag <span class='mk est'>&#9679;</span>","eat off the tourist spine"),
   ("Dinner prices for what lunch does better","paying evening rates for the meal a weekday midday serves for less","eat the menú del día <span class='mk vol'>&#9670;</span>"),
   ("The meal-clock mismatch","eating on American time and getting the rooms that serve it <span class='mk est'>&#9679;</span>","lunch 1–4pm; dinner from ~8:30")],
  ["Start with the rice, because it is the dish most wanted and most often botched. Paella is Valencian rather than Catalan <span class='mk est'>&#9679;</span> — which does not mean you should avoid rice here, the coast does it beautifully, but it explains why the version pushed hardest at visitors is a costume. The tells are visible from the doorway: a photograph of the dish out front, a suspiciously fast arrival, and a uniform neon yellow that comes from colouring rather than saffron. Real rice is cooked to order, which takes twenty minutes or more, and the local cousin worth ordering is often fideà, made with short noodles instead of grain.",
   "The second trap is geographic and the easiest to fix: the tourist spine. La Rambla and its immediate tributaries are engineered for people who will eat there exactly once, and the all-day “tapas” on offer are a performance of a habit rather than the habit itself <span class='mk est'>&#9679;</span>. Two streets off, prices fall and quality rises. No special knowledge is required — only the willingness to walk five minutes away from wherever you happen to be standing when you get hungry.",
   photo("A06", "The local register: priced for people who eat here every week, not for people who will eat here once.", "wide"),
   "The third is the single biggest money lever in the city, and almost no visitor uses it. The menú del día is a fixed-price, multi-course lunch served on weekdays — a tradition rooted in feeding working people a proper midday meal, and priced for them rather than for you <span class='mk est'>&#9679;</span>. Structure the day so your main meal is lunch and dinner is something light, and you will eat better for less all week without a single act of self-denial.",
   "Worth saying plainly: none of this requires you to hunt for somewhere obscure, and the advice to “eat where the locals eat” is close to useless as given, because you cannot tell who is local from a doorway. What you can read from a doorway is the register — photographs of dishes, laminated menus in five languages, a host waving people in, food visible under heat lamps at four in the afternoon. Those are not signs of a bad kitchen so much as signs of a room built around one-time customers. Rooms built around returning customers look different, and they look different everywhere in the city, which is why this is a rule rather than a list.",
   "The fourth is a clock problem, and it quietly determines the other three. Spanish lunch runs roughly one to four, and dinner starts around half past eight <span class='mk est'>&#9679;</span>. Arrive on American time and the only rooms open are the ones that exist to serve people arriving on American time — a fairly reliable filter for the food you are trying to avoid. Eating late here is not an affectation. It is the mechanism that puts you in the right rooms."],
  "<strong>Eat the menú del día at least once, order rice where it is cooked to order, keep your tapas off the tourist spine, and eat on Spanish time.</strong> That is the defence entire, and three of the four rules cost you less while feeding you better — the tourist premium here buys a worse meal, which makes this the rare trap that is easy to refuse once you can see it. The city's food reputation is entirely earned. You simply have to order out of the local register rather than the one built for you.",
  ["<strong>On a budget?</strong> Structure the trip around the weekday lunch: the big meal at midday, something light at night. It is the biggest food-money lever in the city."],
  ["<strong>The tourist spot is sometimes fine</strong> — a coffee on a handsome plaça you are paying location rent for is a fair trade. The rule is about meals, not every euro; do not turn eating into an audit."],
  "<span class='mk vol'>&#9670; VOLATILE</span> — the menú del día band drifts by neighborhood and by year; the Field Sheet carries a current range. The meal-time windows are stable <span class='mk est'>&#9679;</span>. <span class='xref'>This is also the fourth node of the money web, decision 03.</span>",
   head=('h-d08', 'Cooked to order, which is the single tell that separates the two versions of this city.'))

HORIZONS = f'''
<section class="dec chap" id="horizons">
  {rh("The Horizons")}
  <div class="kicker">What to book, and when</div>
  <h1>The Horizons</h1>
  <div class="standfirst">Only two things genuinely bind. Everything else can be arranged a day ahead — worth knowing, because planning anxiety usually attaches to the wrong items.</div>
  {band("h-horizons", "Only two things on this board genuinely bind. Knowing which two is the whole chapter.")}
  <p class="first">The horizons below are structural rather than seasonal. They describe how far ahead a thing must be committed, not what it costs; prices live on the Field Sheet and these bars do not move with them.</p>
  <figure>{FIG_HZ}<figcaption>FIG. 6 &middot; Booking horizons — the two that bind are in gold; the rest are looser than people assume</figcaption></figure>
  <p>The two gold bars are the discipline. <strong>Sagrada Família</strong> is the binding constraint of the entire trip: it slots weeks ahead, it sells out, and, because choosing an hour also chooses a light and a crowd level (decision 04), a late booking costs you the good version rather than merely the convenient one. <strong>Park Güell</strong> is the same shape at a shorter horizon.</p>
  <p>Accommodation sits in the middle and is more urgent this year than most: the centenary concentrates demand, and in the apartment market the licensing phase-out shrinks supply on its own schedule (decision 02). Book the room earlier than you would in an ordinary year, and treat any apartment listing as needing verification rather than merely a deposit.</p>
  <p>One structural note about the two that bind. Their horizons are not really about scarcity in the ordinary sense — plenty of tickets exist. They are about <em>which</em> tickets exist by the time you look. Late in the cycle what remains is the midday slot on a crowded day, which is precisely the version of the experience decision 04 tells you to avoid. So the deadline is not "book or miss out"; it is "book early or pay the same money for the lesser version". That distinction is why these two bars are gold and everything else is not.</p>
  <p>What is <em>not</em> urgent deserves stating plainly, because it is where most planning anxiety goes to die. Day-trip rail seats are effectively walk-up <span class="mk est">&#9679;</span>. Museum and tour slots (the Palau, the Miró, the smaller houses) are comfortable a day ahead. Restaurants, with rare exceptions, are not a booking problem in a city that eats late and eats everywhere. You can land with two reservations made and improvise the rest without penalty, and that is the recommended posture rather than a concession.</p>

  {photo("p-horizons", "Booked weeks out, and the only part of the week that genuinely will not move.", "wide")}
</section>'''

PLAN = f'''
<section class="dec chap" id="plan">
  {rh("The Plan")}
  <div class="kicker">The days as operations</div>
  <h1>The Plan</h1>
  <div class="standfirst">Not an itinerary — a set of operations in an order that respects the constraints. Substitute freely inside a day; keep the order between them.</div>
  {band("h-plan", "The shape, from above. Three anchors and two deliberately empty days.")}
  <p class="first">This is what the decisions produce when you run them forward. It assumes five days, an Eixample base and the two bookings made. Every named sight is replaceable; the <em>shape</em> is the part doing the work — which is why it is set out as operations rather than as an hour-by-hour itinerary.</p>
  <p>The distinction matters. An itinerary tells you where to be at ten o'clock and breaks the moment a queue runs long or a morning turns wet. A shape tells you what each day is <em>for</em>, which anchors are fixed, and which parts are designed to absorb the overflow. Three of these five days carry an anchor; two are deliberately free, and the free ones are load-bearing rather than filler — they are where a delayed morning, a grey afternoon or a longer lunch goes without costing you anything you planned.</p>

  <h3>Day one — the anchor, then the old city</h3>
  <p>Sagrada Família on your morning slot, because that is the constraint everything bends around. Afterwards walk rather than ride: the Modernisme hospital sits ten minutes away and is half-empty by comparison, which makes it the ideal decompression from the basilica. A long lunch. The Gothic Quarter for the late afternoon, when the day-trippers thin out and the lanes are at their best. A late dinner, on local time from the first full day.</p>
  <h3>Day two — the second booking, then downhill</h3>
  <p>Park Güell on your slot, early. Then let gravity do the planning: Gràcia sits immediately below and is the right kind of nothing — plazas, lunch, no monuments to tick off. One Gaudí house in the afternoon if you are doing one. The evening belongs in a neighborhood that eats well rather than one that photographs well.</p>
  <h3>Day three — the variety day</h3>
  <p>A market in the morning, a great interior around midday, the hill in the afternoon, the sea at golden hour. This is the day that shows you the city's range, and it is deliberately unbooked so that it can absorb whatever the first two days ran long on.</p>
  <h3>Day four — out</h3>
  <p>The day trip, whichever one decision 06 landed on. A full day, mid-trip, so a grey forecast can still be traded for a city day. Nothing scheduled for the evening: travel days end tireder than they look on paper.</p>
  <h3>Day five — the city's own rhythm</h3>
  <p>Stop sightseeing. A market breakfast, a neighborhood you have not walked, the beach if the afternoon turns warm, a hilltop at sunset. The unscheduled day is the one people describe most fondly afterwards, which is a strong argument for building it in rather than hoping it emerges from the gaps.</p>
  <figure>{FIG_WK}<figcaption>FIG. 7 &middot; The five-day shape — three anchors, two days that float</figcaption></figure>
  <h2>Substituting without breaking it</h2>
  <p>Every sight named above can be swapped; the constraints cannot. Keep the morning anchor on day one, whatever it is — the point is that the day's fixed commitment happens while you are fresh and the light is good, not that it is specifically a basilica. Keep the day trip whole and mid-week. Keep at least one day with nothing in it. Those three rules survive any amount of substitution, and they are what separate this from a list.</p>
  <p>Compressing to three days: keep day one intact, merge days two and three, and cut the day trip rather than rushing it — a half-day excursion is the worst version of both the city day it replaced and the trip it pretends to be. Expanding to seven: add a second day trip and one more unscheduled day, not more sights. The marginal value of a sixth ticketed interior is close to zero; the marginal value of a second unhurried morning is high, and visitors reliably underestimate this in both directions.</p>

  {photo("p-plan", "The floating day, which is load-bearing rather than filler.", "wide")}
</section>'''

FAIL = f'''
<section class="dec chap" id="fail">
  {rh("Failure Modes")}
  <div class="kicker">Organised by consequence</div>
  <h1>Failure Modes</h1>
  <div class="standfirst">The thing a website of separate articles structurally cannot give you: the mistakes, grouped by what they cost you.</div>
  {band("h-fail", "Sorted by consequence rather than by topic, because that is how the day presents them.")}
  <p class="first">Most travel advice sorts mistakes by topic (transport errors here, food errors there) the ordering that makes them hard to triage. You cannot tell, scanning a list like that, which items would merely irritate you and which would remove a day from a five-day trip. The list below is sorted the other way: by consequence. Read the third group twice.</p>
  <figure>{FIG_CQ}<figcaption>FIG. 8 &middot; The three tiers &mdash; and why the ordering matters more than the count</figcaption></figure>
  <h2>Costs you money</h2>
  <div class="fail"><span class="head">Said yes to being charged in dollars.</span><p>The conversion markup, on every swipe and withdrawal, across the trip. Always choose euros. <em>(03)</em></p></div>
  <div class="fail"><span class="head">Used the bright-blue tourist ATM by the sight.</span><p>Those machines push the dollars prompt and layer their own fees. Use a bank machine. <em>(03)</em></p></div>
  <div class="fail"><span class="head">Didn't budget the tourist tax.</span><p>Per person, per night, sprung at check-out. Known in advance it is a line item; unknown it is a sour last morning. <em>(03)</em></p></div>
  <div class="fail"><span class="head">Paid dinner rates for what lunch does better.</span><p>The menú del día is the biggest food-money lever in the city, and it runs only on weekday middays. <em>(07)</em></p></div>
  <div class="fail"><span class="head">Relied on US carrier roaming.</span><p>An eSIM bought before you fly costs a fraction and lands working. <em>(Before You Fly)</em></p></div>
  <div class="fail"><span class="head">Paid for an ETIAS you don't need.</span><p>It is not live. The sites selling it are the tell. <em>(Before You Fly)</em></p></div>
  <h2>Costs you a day</h2>
  <div class="fail"><span class="head">Arrived at the airport metro with a T-casual.</span><p>It does not work there. A scramble for the right ticket with a flight boarding. <em>(03)</em></p></div>
  <div class="fail"><span class="head">Booked Sagrada Família for midday.</span><p>The crush and the flattest light, on the one interior that is the point. <em>(04)</em></p></div>
  <div class="fail"><span class="head">Wedged the day trip into a half-day.</span><p>The rushed version of a trip that deserved its own day — a commute with a view. <em>(06)</em></p></div>
  <div class="fail"><span class="head">Pinned the beach to a fixed day.</span><p>The day turned grey and it never happened. Leave it floating. <em>(04)</em></p></div>
  <div class="fail"><span class="head">Put a timed ticket on arrival day.</span><p>Jet-lagged, you got the lesser version of something you had paid for. <em>(Day Zero)</em></p></div>
  <h2>Costs you the shape of the trip</h2>
  <div class="fail"><span class="head">Booked an unlicensed apartment.</span><p>The listing can be pulled after you have paid. No HUTB number, no booking. <em>(02)</em></p></div>
  <div class="fail"><span class="head">Based at the beach while sightseeing inland.</span><p>A daily commute to everything you came for. Base central; visit the beach. <em>(01)</em></p></div>
  <div class="fail"><span class="head">Did three Gaudí interiors in two days.</span><p>Saturation — the fourth is wallpaper you paid for, and you blame the building. <em>(05)</em></p></div>
  <div class="fail"><span class="head">Scheduled every day fully.</span><p>The unscheduled day is the one people remember. Build it in deliberately. <em>(The Plan)</em></p></div>

  {photo("p-fail", "The forecast that takes a day off you, and the reason one day was left unpinned.", "wide")}
</section>'''

WALLET = f'''
<section class="dec chap" id="wallet">
  {rh("The Wallet Card")}
  <div class="kicker">Print it, carry it</div>
  <h1>The Wallet Card</h1>
  <div class="standfirst">Everything the trip needs at the point of decision, on one card. The Book is for home; this is for the street.</div>
  {band("h-wallet", "The point of decision, where the Book is no longer with you and the card is.")}
  <div class="wallet">
    <h3>At any card terminal or ATM</h3>
    <div class="line"><span class="k">The prompt “charge in USD?”</span><span class="v">always choose EUROS</span></div>
    <div class="line"><span class="k">Which ATM</span><span class="v">CaixaBank / BBVA / Santander / Sabadell</span></div>
    <div class="line"><span class="k">Which to avoid</span><span class="v">blue standalone machines by the sights</span></div>
    <h3 style="margin-top:14px;">Transit</h3>
    <div class="line"><span class="k">Airport metro</span><span class="v">T-casual NO · Hola/T-usual OK</span></div>
    <div class="line"><span class="k">In-city</span><span class="v">almost everything is Zone 1</span></div>
    <h3 style="margin-top:14px;">Eating</h3>
    <div class="line"><span class="k">Best-value meal</span><span class="v">menú del día — weekday lunch, 1–4pm</span></div>
    <div class="line"><span class="k">Real rice</span><span class="v">cooked to order, 20+ min; try fideà</span></div>
    <div class="line"><span class="k">Dinner starts</span><span class="v">~8:30pm — earlier rooms are tourist-only</span></div>
    <div class="line"><span class="k">Trap tell</span><span class="v">a photograph of the dish out front</span></div>
    <h3 style="margin-top:14px;">Booking &amp; documents</h3>
    <div class="line"><span class="k">Sagrada Família</span><span class="v">sagradafamilia.org · morning slot</span></div>
    <div class="line"><span class="k">Apartment</span><span class="v">valid HUTB number, or skip it</span></div>
    <div class="line"><span class="k">ETIAS</span><span class="v">not live — don't pay for one</span></div>
  </div>
  <p style="margin-top:12px;">Two rules cover most of the week: <strong>euros at every terminal</strong>, and <strong>a T-casual will not open the airport gate</strong> — a Hola Barcelona or a T-usual will. If you remember nothing else from this book at the moment it matters, remember those two.</p>
</section>'''

BACK = f'''
<section class="dec chap" id="back">
  {rh("What This Won't Tell You")}
  <div class="kicker">The honest edges</div>
  <h1>What This Won't Tell You</h1>
  <div class="standfirst">What a decision manual is for, and what it deliberately leaves to you and to the day.</div>
  {band("h-back", "The street this book will not name for you, which is the point of the last chapter.")}
  <p class="first backmatter">This book will not name your hotel. It tells you which neighborhood and which type, on criteria you can apply to any well-reviewed room — because the specific property that suits your dates and your budget is a search rather than a recommendation, and a named list dates the moment a place changes hands.</p>
  <p class="backmatter">It will not name your restaurant. It gives you the rules (the menú del día, the clock, the tells of a tourist-trap plate) that outlive any list, because a list of names is stale the season after it is written. A rule you understand travels to a street we have never heard of. A name does not.</p>
  <p class="backmatter">It will not print this week's prices in these pages. Those live on the Field Sheet, dated, so the Book stays true for years while the numbers stay current where you can actually re-check them. And it will not republish ratings or reviews — those are someone else's aggregated opinion, and laundering them into a paid book would be precisely the thing we are arguing against.</p>
  <p class="backmatter">Finally, it will not pretend the calls are neutral. Every verdict here is a position, shown with the reasoning that produced it, so that you can take it apart and rebuild it around your own trip. If you read decision 01 and conclude that you are exactly the person who should base in El Born, the book has worked. The rules outlive the lists — that is the whole design.</p>
</section>'''

CLOSING = f'''
<section class="dec chap" id="then">
  {rh("A last word")}
  <div class="kicker">A last word</div>
  <h1>Barcelona, Then</h1>
  <div class="standfirst">Once the traps are handled they disappear from the trip — which was always the point of handling them.</div>
  <p class="first dropcap">Do the defending in advance and none of it is on your mind while you are standing in the nave at nine in the morning with the light coming gold through Gaudí's stone forest. None of it is on your mind over rice cooked properly, twenty minutes after you ordered it, at a table where nobody is performing anything for you. None of it is on your mind on a free hilltop at dusk while the city goes orange below and half of Barcelona arrives with something to drink, because they know too.</p>
  {band("A07", "What the defending is for. Handle the four gates in advance and none of them are in your head when the city does this.")}
  <p>The calls in this book are not the trip. They are what clears the way for it — the small, deliberate competence that lets a great city be great to you instead of merely expensive. That is the whole ambition here: not to see Barcelona for you, but to make sure the version you see is the good one.</p>
  <p>Go, and come out ahead.</p>
</section>'''

FS = f'''
<section class="dec chap fs" id="fs">
  {rh("The Field Sheet")}
  <div class="kicker">The dated annex</div>
  <h1>The Field Sheet</h1>
  <div class="standfirst">The volatile figures, dated. The current sheet is always at <b>barcelonaforamericans.com/guide/sheet</b>.</div>
  <p class="first"><span class="fsdate">Compiled 2026 · verify before travel</span> — these are the figures with a short shelf life. Keeping them here, dated, is what lets the Book's calls stay true for years — when a number moves, only the arithmetic changes, never the reasoning.</p>
  <h2>Tourist tax (per person, per night)</h2>
  <table class="fstable">
    <thead><tr><th>Accommodation</th><th>Tax / person / night</th></tr></thead>
    <tbody>
    <tr><td>5-star hotels</td><td class="n">&asymp; &euro;12.00 &#9670;</td></tr>
    <tr><td>4-star hotels</td><td class="n">&asymp; &euro;8.40 &#9670;</td></tr>
    <tr><td>Licensed tourist apartments</td><td class="n">higher surcharge tier &#9670;</td></tr>
    </tbody>
  </table>
  <p class="note" style="border:0;">Rates rose 1 April 2026 and combine a Catalan regional rate with Barcelona's municipal surcharge. The surcharge is politically live and has risen twice recently — confirm the current figure with your accommodation when you book.</p>
  <h2>Transit</h2>
  <table class="fstable">
    <thead><tr><th>Ticket</th><th>Price</th></tr></thead>
    <tbody>
    <tr><td>Airport metro ticket (L9 Sud, T1/T2) — unless you hold Hola/T-usual</td><td class="n">&asymp; &euro;5.90 &#9670;</td></tr>
    <tr><td>T-casual (10 rides, Zone 1) — does NOT cover the airport metro</td><td class="n">check current &#9670;</td></tr>
    <tr><td>Hola Barcelona travel card (48h / 72h / 96h / 120h)</td><td class="n">check current &#9670;</td></tr>
    </tbody>
  </table>
  <h2>Sights and eating</h2>
  <table class="fstable">
    <thead><tr><th>Item</th><th>Figure</th></tr></thead>
    <tbody>
    <tr><td>Sagrada Família — basilica entry (centenary-year demand)</td><td class="n">sagradafamilia.org &#9670;</td></tr>
    <tr><td>Park Güell — monumental zone, timed</td><td class="n">check current &#9670;</td></tr>
    <tr><td>Menú del día — weekday lunch, typical band</td><td class="n">&asymp; &euro;13&ndash;18 &#9670;</td></tr>
    <tr><td>Conversion markup if you accept USD at a terminal</td><td class="n">3&ndash;8% per transaction &#9650;</td></tr>
    </tbody>
  </table>
  <h2>Border systems</h2>
  <table class="fstable">
    <thead><tr><th>System</th><th>Status for 2026</th></tr></thead>
    <tbody>
    <tr><td>EES — biometric entry/exit</td><td class="n">live &#9670;</td></tr>
    <tr><td>ETIAS — pre-travel authorisation</td><td class="n">not yet live &#9670;</td></tr>
    </tbody>
  </table>
  <p class="note" style="border:0;">&#9670; VOLATILE — verify at the source before travel. &#9650; SURVEYED — an observed range, not a fixed rate. The Book's calls hold regardless of the exact figures; these are the inputs to the arithmetic, kept here so the analysis stays current where you can check it. If a website offers to sell you an ETIAS, that is the tell — it is not yet in force.</p>
</section>'''


SETPIECES = f'''
<section class="dec chap" id="setpieces">
  {rh("The Set Pieces")}
  <div class="kicker">Order of operations</div>
  <h1>The Set Pieces</h1>
  <div class="standfirst">Two operations on this trip have enough moving parts to go wrong on the day, even when you booked correctly. Here is the order of operations for each.</div>
  {band("h-setpieces", "The queue is not the failure. Arriving at the hour that produces it is.")}
  <p class="first dropcap">A booked ticket is not the same as a solved visit. Both of Barcelona's ticketed anchors have a second layer of decisions that the booking page raises and most visitors answer blind — an add-on chosen at checkout, an approach route nobody mentions, a fallback if the calendar is empty. None of this is difficult. All of it is easier to settle at your kitchen table than in a queue.</p>
  <h2>Sagrada Família</h2>
  <p><strong>The order.</strong> Book on the official site, take a morning slot, decide the tower question at checkout, and arrive knowing that the nave is the point and everything else is an addition to it.</p>
  <p>The tower question is the one that catches people. Tower access is an add-on chosen when you buy <span class="mk est">&#9679;</span> — you pick <em>one</em>, ride an elevator up, and walk down a long, tight spiral staircase. You cannot switch on the day and you cannot do both on one ticket. The Nativity tower faces the rising sun and overlooks the older, more ornate façade that Gaudí personally designed and partly saw built; the Passion tower aligns with afternoon light and gives the city-centre panorama <span class="mk est">&#9679;</span>. For a morning slot, which is what this book recommends, take Nativity, and take it knowing the façade beneath you is the more spectacular of the two.</p>
  <p>Be honest about the descent before you add it. You go up by elevator but come down a continuous spiral staircase with a low ceiling and no alternative, which rules it out for anyone with significant mobility limits, serious knee trouble, claustrophobia or vertigo <span class="mk est">&#9679;</span>. There is no shame in skipping the towers entirely: they are a bonus view, and the nave below is the actual masterpiece. A first-timer who skips the climb and spends the extra twenty minutes inside has made the better trade more often than not.</p>
  <h2>Park Güell</h2>
  <p><strong>The order.</strong> Book the monumental zone, ride up rather than climb, arrive at your slot, and know your fallback before you need it.</p>
  <p>Two things wear one name here <span class="mk est">&#9679;</span>. The <em>monumental zone</em> is Gaudí's stage set — the Dragon Stairway, the hypostyle room of tilted columns, the terrace with the curving trencadís bench and the postcard view to the sea — and it is timed-ticket only. The rest of the park is free, large and genuinely pleasant, and most visitors do not realise it exists as a separate thing.</p>
  <p>The approach is the part nobody warns you about. The park sits on a steep hill in Gràcia, and taking the metro to Park Güell means taking the metro to the bottom of a serious climb <span class="mk est">&#9679;</span>. The usual advice is Metro L3 to Vallcarca and the public escalators up Baixada de la Glòria, which does most of the ascent and leaves roughly fifteen minutes of walking — when they are running. They are an installation, not a street: the park's own pages have carried contradictory notices about them. Check the access notice on the official site the week you go, and keep Lesseps as the fallback. Getting off at Lesseps instead buys you a twenty-minute uphill walk you did not plan for, at the start of a day you wanted to spend upright.</p>
  <p>If the calendar is empty, the fallback is ranked <span class="mk call">&#9672;</span>: re-check the official site early in Spanish morning, when small batches of returns appear; then look at guided tours and combinations, which often hold allocations when bare entry is gone; and failing both, take the free park — enter from the Carretera del Carmel side and climb to the Turó de les Tres Creus, which gives you the city and the sea from above, without a ticket. Be clear about what that is <em>not</em>: the terrace, the viaducts and the Gaudí monuments all sit inside the ticketed monumental zone, and no free route reaches them. That third option is not a consolation prize. On a crowded day in a centenary year, several visitors will prefer it.</p>

  {photo("p-setpieces", "The detail you only reach by booking the hour rather than the day.", "wide")}
</section>'''


RISK = f'''
<section class="dec chap" id="risk">
  {rh("How Worried Should You Be?")}
  <div class="kicker">Risk, calibrated</div>
  <h1>How Worried Should You Be?</h1>
  <div class="standfirst">Barcelona's reputation frightens people out of proportion to the actual risk — and in the wrong direction. Here is the calibrated version.</div>
  {band("h-risk", "The street the reputation is built on, on an ordinary afternoon. The risk is real, non-violent and concentrated.")}
  <p class="first dropcap">Violent crime against visitors is rare <span class="mk est">&#9679;</span>. People walk the central neighborhoods late without incident, and solo travellers, including women, generally report feeling comfortable. What Barcelona has instead is exceptionally skilled, <em>non-violent</em> property crime: pickpockets and bag-snatchers who are fast, professional, and who go out of their way not to confront you. That distinction matters more than any statistic, because it tells you what to defend against. The correct posture is not fear. It is the ordinary alertness you would bring to any major city, applied in about four specific places.</p>
  <h2>Where it actually happens</h2>
  <p>The risk is concentrated in predictable places, and knowing them is most of the defence <span class="mk call">&#9672;</span>. <strong>La Rambla</strong> is the single most worked stretch in the city — crowded, distracting, and staffed by people who do this professionally. <strong>The metro</strong>, particularly the L3 line that serves the tourist sights and the airport routes, with the doors-closing moment being the classic grab. And <strong>the crowds at Sagrada Família and Park Güell</strong>, or anywhere else visitors cluster together and look upward with their phones out.</p>
  <p>That list maps closely onto the places this book already sends you, which means the defence costs nothing: you are not avoiding anywhere, only paying attention in four named places rather than worrying diffusely everywhere.</p>
  <h2>The scams, which are all one scam</h2>
  <p>Beyond straightforward pickpocketing, a handful of distraction routines recur, and they share one structure: something claims your attention while a partner takes your things <span class="mk est">&#9679;</span>. <strong>The petition</strong> — someone with a clipboard asks you to sign for a cause, and while you read, an accomplice works your pockets. <strong>The spill</strong> — a stranger points out a stain on your jacket and helpfully cleans it; they put it there. Once you see that every version is the same move, the catalogue stops mattering. Anything sudden that asks for your attention in a crowd is the tell, and the response never changes: hands on your bag, step back, keep walking.</p>
  <h2>The habits that make you a hard target</h2>
  <p>No gadgets and no paranoia are required — just a few consistent behaviours <span class="mk call">&#9672;</span>. Bags zipped and worn in front; a crossbody bag across your chest with the zipper toward you defeats most attempts. Nothing valuable in a back pocket, and nothing in the outer pocket of a backpack. Phone away in crowds and on the metro — the phone-in-hand pose on La Rambla is the single most reliable way to be selected. Use it, then put it away rather than walking with it out.</p>
  <p>If it happens anyway, you almost certainly will not catch them, and you should not try <span class="mk call">&#9672;</span>. File a police report, a <em>denuncia</em>, which you will need for insurance and for replacing documents. Cancel cards immediately using the backup numbers you saved before flying, which is the reason that item is on the pre-flight checklist. For a lost passport, contact the US Consulate.</p>
  <p><strong>The bottom line: a manageable, non-violent risk — not a reason to weigh skipping one of Europe's great cities.</strong> Tens of millions visit safely every year, and those who get caught out are, with dull consistency, carrying a phone in one hand and an open bag on one shoulder along the busiest street in the city. Handle those two and the odds tip permanently in your favour.</p>

  {photo("p-risk", "If it happens anyway: the denuncia, the backup card numbers, and no attempt to chase anyone.", "wide")}
</section>'''


# ── "Before you book": generated by add-tools.py from calls.json +
# tools_content.py, then brought back into the source so a rebuild keeps it.
TOOLS = '''<section class="dec chap" id="beforeyoubook"><span class="rh-src">BEFORE YOU BOOK</span><div class="kicker">BEFORE YOU BOOK</div><h1>Decide these first</h1><div class="standfirst">Seven calls, in the order they bind. The page number is where each one is argued, and every one of them is a position you can overrule once you have read the reasoning.</div>
  <figure class="photo band"><img src="img/h-beforeyoubook.jpg" width="1100" height="733" decoding="sync" loading="eager"/><figcaption>Everything on this spread is decided before you leave, and most of it in one sitting.</figcaption></figure><table class="ledger"><caption>The seven calls, in the order they bind</caption><thead><tr><th>DECIDE</th><th>THE CALL THIS BOOK MAKES</th><th class="num">PAGE</th></tr></thead><tbody><tr><td><span class="opt">Which of the three 'centrals' do you sleep in?</span></td><td><span class="sub">The Eixample, and it isn't close</span></td><td class="num"><span class="ckl"><a href="#d01"></a></span></td></tr><tr><td><span class="opt">Apartment or hotel, in the year the licences are being withdrawn?</span></td><td><span class="sub">A hotel or apart-hotel — not the apartment, unless you hold a valid HUTB number</span></td><td class="num"><span class="ckl"><a href="#d02"></a></span></td></tr><tr><td><span class="opt">Where does the city actually take your money?</span></td><td><span class="sub">Four gates, four moves: budget the bed tax, buy the airport ticket both ways, say euros, use a bank machine</span></td><td class="num"><span class="ckl"><a href="#d03"></a></span></td></tr><tr><td><span class="opt">What goes on which day?</span></td><td><span class="sub">Anchor three things and float the rest; arrival day holds nothing timed</span></td><td class="num"><span class="ckl"><a href="#d05"></a></span></td></tr><tr><td><span class="opt">How many Gaudí interiors do you pay to go inside?</span></td><td><span class="sub">Two ticketed sites and exactly one house — the fourth interior is the one you don't see</span></td><td class="num"><span class="ckl"><a href="#d06"></a></span></td></tr><tr><td><span class="opt">Which day trip, if you take one?</span></td><td><span class="sub">Montserrat. It out-memories the city, and has no substitute within reach</span></td><td class="num"><span class="ckl"><a href="#d07"></a></span></td></tr><tr><td><span class="opt">How do you avoid eating badly in a great eating city?</span></td><td><span class="sub">Menú del día at least once, rice cooked to order, tapas off the tourist spine, dinner on Spanish time</span></td><td class="num"><span class="ckl"><a href="#d08"></a></span></td></tr></tbody></table><h2>What to ask, before you pay</h2><p>Say these in these words. Each settles something this book spends pages on, and none of them needs the name of a hotel or a restaurant — which is why they still work a season from now.</p><div class="askbox"><p class="who">A hotel or apart-hotel, before you book the room</p><ul><li>Is the tourist tax included in this rate, or added at check-out — and how much per person per night?</li><li>Which metro line is nearest, and is it one that reaches the airport?</li><li>Is the room on the street side or the interior courtyard?</li></ul></div><div class="askbox"><p class="who">An apartment listing, if you are still considering one</p><ul><li>What is the HUTB licence number, and can you send me a photograph of the licence itself?</li><li>If the licence is withdrawn before my dates, what is the refund — in writing, now?</li><li>Is there a legal alternative you would move me to, and who pays the difference?</li></ul></div><div class="askbox"><p class="who">A restaurant, from the doorway, at lunch</p><ul><li>Do you serve a menú del día today, and what is on it?</li><li>Is the rice cooked to order, or is it ready?</li><li>Is bread, or anything else on the table, charged separately?</li></ul></div><div class="askbox"><p class="who">A card terminal or a cash machine</p><ul><li>Charge it in euros, please — not dollars.</li><li>Is this machine operated by a bank, or by an independent operator?</li><li>What is the fee on this withdrawal, before I accept?</li></ul></div><h2>Two shapes that follow the calls</h2><p>Both are built from the seven calls and nothing else. The assumptions are printed because they are what makes the shape right — change one and the shape changes.</p><div class="trip"><p class="tname">Five days, first visit, Eixample base</p><p class="tassume">Assumes: an Eixample hotel or apart-hotel; a Sagrada Família morning slot booked the day the calendar opened for those dates, and Park Güell about six weeks out; late spring or early autumn; no car.</p><table class="ledger"><caption></caption><thead><tr><th>WHEN</th><th>WHAT HAPPENS</th><th class="num"></th></tr></thead><tbody><tr><td><span class="opt">Day 1</span></td><td><span class="sub">Arrival. Nothing timed. The Gothic Quarter on foot, a plaça, an early dinner — and the airport-metro return ticket bought while you are calm.</span></td><td class="num"></td></tr><tr><td><span class="opt">Day 2</span></td><td><span class="sub">Sagrada Família on the morning slot, then the Eixample on foot: one house, Batlló or La Pedrera, not both.</span></td><td class="num"></td></tr><tr><td><span class="opt">Day 3</span></td><td><span class="sub">Montserrat, the whole day. FGC R5 from Plaça d'Espanya, then the cable car.</span></td><td class="num"></td></tr><tr><td><span class="opt">Day 4</span></td><td><span class="sub">Park Güell early on your slot, Gràcia afterwards, menú del día at lunch.</span></td><td class="num"></td></tr><tr><td><span class="opt">Day 5</span></td><td><span class="sub">The floating day: the beach if it is warm, Montjuïc if it is not. Nothing booked, on purpose.</span></td><td class="num"></td></tr></tbody></table><p class="twhy">Three anchors, two free days, and the free days are load-bearing rather than filler — they are where a grey morning or a long queue goes without costing you anything.</p></div><div class="trip"><p class="tname">Three days, first visit, no day trip</p><p class="tassume">Assumes: the same base and the same two bookings; you would rather see one city properly than add a fourth destination; the day trip is deliberately given up.</p><table class="ledger"><caption></caption><thead><tr><th>WHEN</th><th>WHAT HAPPENS</th><th class="num"></th></tr></thead><tbody><tr><td><span class="opt">Day 1</span></td><td><span class="sub">Arrival, nothing timed, the old city on foot.</span></td><td class="num"></td></tr><tr><td><span class="opt">Day 2</span></td><td><span class="sub">Sagrada Família in the morning, one Gaudí house in the afternoon.</span></td><td class="num"></td></tr><tr><td><span class="opt">Day 3</span></td><td><span class="sub">Park Güell on an early slot, then Gràcia or the Born at your own pace — and the menú del día, which is the one food rule that fits a short trip.</span></td><td class="num"></td></tr></tbody></table><p class="twhy">At three days the day trip is the thing to cut, not the thing to squeeze: wedged into a morning, Montserrat becomes a commute with a view and takes the day with it.</p></div><div class="fbwrap"><h2>When the plan does not survive the day</h2><table class="ledger"><caption></caption><thead><tr><th>WHEN THIS HAPPENS</th><th>DO THIS</th><th class="num"></th></tr></thead><tbody><tr><td><span class="opt">The Sagrada Família calendar is full for your dates</span></td><td><span class="sub">Take an authorised reseller's allocation rather than an unofficial one, and take any morning over a better-priced midday — the light and the crush are the whole point of the slot. Then rebuild the week around the morning you were given.</span></td><td class="num"></td></tr><tr><td><span class="opt">The forecast turns grey on your day-trip day</span></td><td><span class="sub">This is what the floating day is for: trade the two. Montserrat in cloud is a different and lesser mountain, and the beach day was never fixed to a date.</span></td><td class="num"></td></tr><tr><td><span class="opt">Your apartment cannot produce a licence number</span></td><td><span class="sub">Treat it as a booking that may not exist and move to a hotel or apart-hotel now, while there is still stock, rather than at the door. A refund promised verbally is not a bed.</span></td><td class="num"></td></tr><tr><td><span class="opt">Park Güell's monumental zone is sold out</span></td><td><span class="sub">Walk the free part of the park and the Gràcia streets below it, and spend the ticket money on the second Gaudí house you had ruled out — the one call in this book that is safe to reverse mid-trip.</span></td><td class="num"></td></tr></tbody></table></div></section>'''

BODY = (COVER + OPENING + HOWTO + TOC + GROUND + FLY + DAYZERO + TIMING + SETPIECES +
        D01 + D02 + D03 + D05 + D06 + D07 + D08 +
        HORIZONS + RISK + PLAN + FAIL + WALLET + BACK + CLOSING + TOOLS + FS)

BODY, _NPL = _stamp_plates(BODY)

HTML = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>Barcelona, Without the Traps.</title>
<style>{CSS}</style></head><body>{BODY}</body></html>'''

open('dossier3.html','w').write(HTML)
import re
print(f"wrote dossier3.html ({len(HTML):,} bytes) · {_NPL} numbered plates")
print(f"body word count ~{len(re.sub('<[^>]+>',' ', BODY).split()):,}")
