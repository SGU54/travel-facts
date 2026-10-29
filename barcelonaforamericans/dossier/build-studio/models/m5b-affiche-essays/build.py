# -*- coding: utf-8 -*-
"""MODEL 5b — L'AFFICHE beyond the decisions. Marta Serra composes the chapters that
have no verdict: an essay (The Ground) and two tools (The Plan, The Wallet Card).

Her rule for the book: COLOUR IS A VERDICT, PAPER IS AN ARGUMENT.
- Decisions open on a red or gold field with the call as a number or a name.
- Essays open on a PAPER poster: the chapter's thesis sentence in ink at poster size,
  the one red thing on it is the label. No number — an essay has no call to shout.
- Tools open on a poster that IS the tool: the plan's five days as five columns,
  fixed days in red fields, floating days in paper. The wallet card is a card.
Same family (Archivo), same stack, same rules, no boxes."""
import sys, os, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import *
from bs4 import BeautifulSoup

# the m5 stylesheet and helpers, exactly as Marta set them
src = open(os.path.join(HERE, 'm5-affiche', 'build.py'), encoding='utf-8').read()
exec(src.split('# ── d06')[0].split('from common import *', 1)[1])

CSS += '''
.poster.paper{ background:var(--paper); color:var(--ink); }
.poster .lab{ color:var(--red); }
.thesis{ font-weight:800; font-stretch:88%; font-size:64px; line-height:62px; letter-spacing:-.035em; margin-top:120px; }
.thesis em{ font-style:normal; color:var(--red); }
.poster .rule{ border-top:3px solid var(--ink); padding-top:12px; }
h2{ font-size:19px; line-height:21px; font-weight:800; font-stretch:92%; letter-spacing:-.02em; margin:0 0 10px; padding-top:10px; border-top:3px solid var(--ink); }
.prose i.mk{ color:var(--red); }
.sideq{ border-top:3px solid var(--red); padding-top:10px; }
.sideq .lab{ color:var(--red); font-size:9px; font-weight:700; letter-spacing:.2em; text-transform:uppercase; display:block; margin-bottom:6px; }
.sideq .big19{ font-size:19px; line-height:22px; font-weight:700; letter-spacing:-.02em; font-stretch:92%; }
.keyline{ font-size:9.5px; line-height:13px; color:var(--grey); margin-top:16px; border-top:1px solid var(--line); padding-top:8px; }
.keyline i.mk{ color:var(--red); }
figure.fig{ margin:0 0 22px; } figure.fig svg{ display:block; width:100%; height:auto; }
figure.fig figcaption{ font-size:9px; line-height:13px; font-weight:600; letter-spacing:.06em; text-transform:uppercase; color:var(--grey); margin-top:8px; }
/* the plan poster: five days as five columns */
.days{ display:grid; grid-template-columns:repeat(5,1fr); column-gap:10px; margin-top:40px; height:660px; }
.days .d{ padding:14px 12px 16px; display:flex; flex-direction:column; border-top:3px solid var(--ink); }
.days .d.fix{ background:var(--red); color:var(--paper); border-top-color:var(--red); }
.days .n{ font-weight:800; font-stretch:118%; font-size:150px; line-height:.8; letter-spacing:-.05em; margin-left:-4px; }
.days .t{ margin-top:auto; font-size:15px; line-height:17px; font-weight:700; letter-spacing:-.01em; font-stretch:92%; }
.days .k{ font-size:9px; font-weight:700; letter-spacing:.18em; text-transform:uppercase; margin-top:8px; }
.days .d:not(.fix) .k{ color:var(--grey); }
/* the plan's day sheet */
.dayrow{ display:grid; grid-template-columns:120px 1fr; column-gap:24px; border-top:3px solid var(--ink); padding:16px 0 26px; }
.dayrow.fix{ border-top-color:var(--red); }
.dayrow .n{ font-weight:800; font-stretch:118%; font-size:104px; line-height:.82; letter-spacing:-.05em; }
.dayrow.fix .n{ color:var(--red); }
.dayrow .k{ font-size:9px; font-weight:700; letter-spacing:.18em; text-transform:uppercase; color:var(--grey); }
.dayrow.fix .k{ color:var(--red); }
.dayrow .h{ font-size:19px; line-height:22px; font-weight:700; letter-spacing:-.02em; font-stretch:92%; margin:3px 0 5px; }
.dayrow p{ margin:0; }
/* the wallet card */
.rules2{ display:grid; grid-template-columns:1fr 1fr; column-gap:40px; border-top:3px solid var(--red); padding-top:12px; margin-bottom:26px; }
.rules2 .big{ font-size:30px; line-height:32px; font-weight:800; letter-spacing:-.025em; font-stretch:88%; }
.rules2 .big b{ color:var(--red); }
.rules2 p{ margin:6px 0 0; font-size:10px; line-height:14px; color:var(--grey); }
.wgrid{ display:grid; grid-template-columns:1fr 1fr; column-gap:40px; row-gap:18px; }
.wgrid .stack .it{ padding:7px 0 8px; } .wgrid .stack .opt{ font-size:15px; line-height:17px; }
.cards{ display:flex; gap:28px; margin-top:30px; align-items:flex-start; }
.card{ width:324px; height:204px; box-sizing:border-box; outline:1.5px dashed var(--grey); outline-offset:8px; padding:16px 18px; display:flex; flex-direction:column; }
.card.front{ background:var(--red); color:var(--paper); }
.card.front .g{ font-weight:800; font-stretch:118%; font-size:66px; line-height:.82; letter-spacing:-.045em; margin-top:12px; }
.card.front .s{ font-size:12px; line-height:15px; font-weight:700; margin-top:auto; }
.card .tag{ font-size:8.5px; font-weight:700; letter-spacing:.2em; text-transform:uppercase; display:flex; justify-content:space-between; }
.card.back{ background:#fff; }
.card.back .ln{ display:grid; grid-template-columns:92px 1fr; column-gap:8px; font-size:9.5px; line-height:12.5px; border-top:1px solid var(--line); padding:3px 0; }
.card.back .ln b{ font-weight:700; } .card.back .ln:first-of-type{ border-top:2px solid var(--ink); margin-top:6px; }
.wgrid .stack .it.wl{ display:grid; grid-template-columns:118px 1fr; column-gap:10px; align-items:baseline; padding:6px 0 6px; }
.wgrid .stack .it.wl .opt{ font-size:12px; line-height:15px; } .wgrid .stack .it.wl .v{ margin-top:0; font-size:8.5px; line-height:12px; }
.cards{ break-inside:avoid; }
.cut{ font-size:9px; font-weight:600; letter-spacing:.06em; text-transform:uppercase; color:var(--grey); margin-top:20px; }
'''

def paras(sid):
    s = BeautifulSoup(open(os.path.join(HERE, f'_src-{sid}.html'), encoding='utf-8').read(), 'lxml')
    out = {}
    for p in s.find_all('p', attrs={'data-p': True}):
        h = p.decode_contents().strip()
        h = re.sub(r'<span class="mk (\w+)">([^<]*)</span>', r'<i class="mk">\2</i>', h)
        out[int(p['data-p'].split(':')[1])] = h
    return out

# ── THE GROUND · essay ─────────────────────────────────────────────────────────
G = paras('ground')
FOUR = [('The tourist tax', "isn't in your room rate", 'at check-out, when you are leaving'),
        ('The airport ticket', "isn't the one your metro card holds", 'at a gate, when you are rushed'),
        ('The dollars prompt', 'offered with a helpful smile', 'at a terminal, when someone is waiting'),
        ('The tourist rate', 'the bright-blue ATM; the tourist-priced table', 'at a table, when you are hungry')]
four = '<div class="stack"><span class="lab">Four small charges, four moods</span>' + ''.join(
    f'<div class="it"><div class="opt">{a}</div><div class="sub">{esc(b)}</div><div class="v" style="color:var(--red)">{esc(c)}</div></div>'
    for a, b, c in FOUR) + '</div>'
readwith = ('<div class="forks"><div class="it"><div class="q">Read with Decision 03</div>'
            '<p>The Money-Trap Web — the four extractions, in one place, with the arithmetic shown.</p></div></div>')

# FIG. 1 redrawn at 1:1 on the 652px measure, so every label prints at its true size
fig1 = '''<svg viewBox="0 0 652 250" xmlns="http://www.w3.org/2000/svg" font-family="Archivo, sans-serif">
<circle cx="190" cy="128" r="128" fill="none" stroke="#17201C" stroke-width="3"/>
<text x="190" y="128" text-anchor="middle" font-size="44" font-weight="800" letter-spacing="-1.5" fill="#17201C">ZONE 1</text>
<text x="190" y="152" text-anchor="middle" font-size="12" fill="#6B7773">metro · bus · tram · funicular · local rail</text>
<text x="190" y="168" text-anchor="middle" font-size="12" fill="#6B7773">one ticket covers essentially everything</text>
<line x1="320" y1="132" x2="530" y2="132" stroke="#A23520" stroke-width="3" stroke-dasharray="9 7"/>
<line x1="402" y1="114" x2="426" y2="150" stroke="#A23520" stroke-width="5"/>
<line x1="426" y1="114" x2="402" y2="150" stroke="#A23520" stroke-width="5"/>
<text x="414" y="98" text-anchor="middle" font-size="11" font-weight="700" letter-spacing="2" fill="#A23520">T-CASUAL STOPS HERE</text>
<text x="414" y="178" text-anchor="middle" font-size="11" fill="#6B7773">Hola Barcelona · T-usual: through</text>
<circle cx="580" cy="132" r="46" fill="#A23520"/>
<text x="580" y="141" text-anchor="middle" font-size="26" font-weight="800" fill="#F4F2EC">BCN</text>
<text x="580" y="202" text-anchor="middle" font-size="12" font-weight="700" fill="#17201C">Airport metro</text>
</svg>'''

ground = f'''<div class="poster paper"><span class="rh-src">The Ground</span>
  <div class="slug"><span class="lab">The organising fact</span><span>The Ground</span></div>
  <div class="thesis">Barcelona doesn't overcharge you once. It charges you <em>four small times</em>, in four different places, and counts on you never seeing the pattern.</div>
  <div class="foot rule"><div class="big">The city does not need to hide anything; the scattering does the work.</div><p>Everything downstream of this fact is defence: where you sleep, how you sequence the days, what you order at lunch. The calls in this book are the moves that keep the extraction machine from running on you by default.</p></div>
</div>
<div class="pg">
  <h1>The Ground</h1>
  <div class="grid" style="margin-top:22px"><div class="prose">{''.join('<p>%s</p>' % G[i] for i in (0, 1, 2, 3))}</div>
    <div>{four}{readwith}</div></div>
</div>
<div class="pg">
  <div class="grid"><div class="prose"><p>{G[4]}</p></div>
    <div class="sideq"><span class="lab">If you read one page</span><div class="big19">Decision 03. It is the one we would hand a friend for free.</div></div></div>
  <figure class="fig" style="margin-top:14px"><h2>Why the metro map lies to you</h2>{fig1}<figcaption>Fig. 1 — One integrated system, one gap — and the gap is at the airport</figcaption></figure>
  <div class="grid"><div class="prose"><p>{G[5]}</p><p>{G[6]}</p></div>
    <div class="sideq"><span class="lab">The rule</span><div class="big19">Check whether the ticket you already hold covers Zone 1 including the airport. If you are on a T-casual, it does not.</div>
    <div class="keyline"><i class="mk">●</i> Established — structural, true for years</div></div></div>
</div>
<div class="photo"><img src="{photo('p-ground.jpg')}" style="object-position:50% 50%">
  <div class="tail"><div><div class="cap">The tourist-facing retail of a city that is very good at tourism. All of it legal, all of it posted.</div></div><p>{G[7]}</p></div>
</div>'''

# ── THE PLAN · tool ────────────────────────────────────────────────────────────
P = paras('plan')
DAYS = [(1, True, 'Sagrada, then the old city', 'Booked · fixed', 'Day one — the anchor, then the old city'),
        (2, True, 'Park Güell, then downhill', 'Booked · fixed', 'Day two — the second booking, then downhill'),
        (3, False, 'Market, hill, sea', 'Floats · absorbs overflow', 'Day three — the variety day'),
        (4, True, 'The day trip, a full clear day', 'Booked · fixed', 'Day four — out'),
        (5, False, 'No agenda: the city itself', 'Floats', "Day five — the city's own rhythm")]
cols = ''.join(f'<div class="d{" fix" if f else ""}"><div class="n">{n}</div><div class="t">{esc(t)}</div><div class="k">{esc(k)}</div></div>' for n, f, t, k, _ in DAYS)
rows = ''.join(f'<div class="dayrow{" fix" if f else ""}"><div class="n">{n}</div><div><div class="k">{esc(k)}</div><div class="h">{esc(h.split(" — ", 1)[1][:1].upper() + h.split(" — ", 1)[1][1:])}</div><p>{P[n + 1]}</p></div></div>' for n, f, t, k, h in DAYS)
RULES = ['Keep the morning anchor on day one, whatever it is.', 'Keep the day trip whole and mid-week.', 'Keep at least one day with nothing in it.']
rules = '<div class="stack"><span class="lab">Three rules that survive any substitution</span>' + ''.join(
    f'<div class="it pick"><div class="opt">{esc(r)}</div></div>' for r in RULES) + '</div>'
plan = f'''<div class="poster paper"><span class="rh-src">The Plan</span>
  <div class="slug"><span class="lab">The days as operations</span><span>The Plan</span></div>
  <div class="days">{cols}</div>
  <div class="foot"><div class="big">Three anchors, two free days — the shape, not the list.</div><p>It assumes five days, an Eixample base and the two bookings made. Substitute freely inside a day; keep the order between them.</p></div>
</div>
<div class="pg">
  <h1>The Plan</h1>
  <div class="sf">Not an itinerary — a set of operations in an order that respects the constraints. Substitute freely inside a day; keep the order between them.</div>
  <div class="grid"><div class="prose"><p>{P[0]}</p><p>{P[1]}</p><p>{P[7]}</p><p>{P[8]}</p></div><div>{rules}</div></div>
  <figure class="band" style="margin-top:14px"><img src="{photo('h-plan.jpg')}" style="object-position:50% 50%;height:150px"><figcaption>The shape, from above. Three anchors and two deliberately empty days.</figcaption></figure>
</div>
<div class="pg">{rows}</div>'''

# ── THE WALLET CARD · tool ─────────────────────────────────────────────────────
W = [('At any card terminal or ATM', [('The prompt “charge in USD?”', 'always choose euros'), ('Which ATM', 'CaixaBank / BBVA / Santander / Sabadell'), ('Which to avoid', 'blue standalone machines by the sights')]),
     ('Transit', [('Airport metro', 'T-casual no · Hola / T-usual OK'), ('In-city', 'almost everything is Zone 1')]),
     ('Eating', [('Best-value meal', 'menú del día — weekday lunch, 1–4pm'), ('Real rice', 'cooked to order, 20+ min; try fideà'), ('Dinner starts', '~8:30pm — earlier rooms are tourist-only'), ('Trap tell', 'a photograph of the dish out front')]),
     ('Booking & documents', [('Sagrada Família', 'sagradafamilia.org · morning slot'), ('Apartment', 'valid HUTB number, or skip it'), ('ETIAS', "not live — don't pay for one")])]
wg = ''.join('<div class="stack"><span class="lab">%s</span>%s</div>' % (esc(h), ''.join(
    f'<div class="it wl"><div class="opt">{esc(k)}</div><div class="v">{esc(v)}</div></div>' for k, v in ls)) for h, ls in W)
BACK = [('Card / ATM', 'charge in EUROS, always'), ('Cash', 'a bank machine, not the blue one'), ('Airport metro', 'T-casual no · Hola / T-usual OK'),
        ('Lunch', 'menú del día, weekdays 1–4pm'), ('Dinner', 'from ~8:30pm'), ('Rice', 'cooked to order, 20+ min'), ('Apartment', 'HUTB number, or skip it')]
wallet = f'''<div class="pg"><span class="rh-src">The Wallet Card</span>
  <h1>The Wallet Card</h1>
  <div class="sf">Everything the trip needs at the point of decision, on one card. The Book is for home; this is for the street.</div>
  <div class="rules2"><div><div class="big">Say <b>euros</b> at every terminal.</div></div><div><div class="big">A <b>T-casual</b> will not open the airport gate.</div><p>A Hola Barcelona or a T-usual will.</p></div></div>
  <div class="wgrid">{wg}</div>
  <div class="cards"><div class="card front"><div class="tag"><span>Barcelona</span><span>Without the Traps</span></div><div class="g">EUROS.</div><div class="s">At every terminal. And a T-casual will not open the airport gate.</div></div>
    <div class="card back"><div class="tag" style="color:var(--red)"><span>The street card</span><span>2026</span></div>{''.join(f'<div class="ln"><b>{esc(k)}</b><span>{esc(v)}</span></div>' for k, v in BACK)}</div></div>
  <div class="cut">Cut along the dashed line, fold in two, keep it behind your card.</div>
</div>'''

html = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Model 5b — L\'Affiche, essays and tools</title><style>{CSS}</style></head><body>{ground}{plan}{wallet}</body></html>'
write(html)
