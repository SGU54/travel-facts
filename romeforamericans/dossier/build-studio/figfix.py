# -*- coding: utf-8 -*-
"""figfix.py — the figures and posters that must say what the text now says (Ruth recheck v5, writer's
_studio/writer/figure-edits.json; studio 2026-10-26). Applied to the composed HTML after the studio pass."""
import re
from bs4 import BeautifulSoup

TEXT = [   # (old, new) in any text node — posters, figure labels, captions
    ('SIX WEEKS OUT', 'THE DAY SALES OPEN'),
    ('WEEKS AHEAD — BOOK ON SALE', 'BOOK THE DAY SALES OPEN'),
    ('A day or two — Colosseum standard, Pantheon', '30 days out — Colosseum standard · Pantheon: no booking'),
    ('The standard Colosseum and the Pantheon need only a day or two.', 'The standard Colosseum goes on sale 30 days out: in peak season book it then, in winter a few days ahead; the Pantheon needs no booking.'),
    ('check the official page for its current release window (recently about a week out) and reserve the moment it opens', 'the arena’s window opens about 7 days ahead; reserve the moment it opens'),
    ("Through the Pantheon's bronze doors to the oculus: the threshold the chapter describes. It now charges admission and needs a timed slot; book it with the day.",
     'Inside the Pantheon, under the coffered dome and its open oculus. It now charges admission; booking is optional, so buy at the door.'),
    ('punish a late booking with “sold out.”.', 'punish a late booking with “sold out.”'),
    ('Leonardo + taxi', 'Leonardo + hop (metro or taxi)'),
    # Ruth's ChatGPT triage (X2, X8) — the writer's figure-edits.json
    ('A source and a date, as every mark here carries.', 'A claim and its date, cut in stone; every ◇ and ◆ claim in this book carries both, at the back.'),
    ('Minutes on foot to the center, from the core. From Termini, twenty-eight.', 'Minutes on foot to Piazza Venezia, the core’s center. From Termini, twenty-eight; to the Pantheon, thirty-five.'),
    # Ruth recheck v6 minors (n9–n12)
    ('so agree the fare before you load the bags', 'so check the meter is running before you load the bags'),
    ('The two-hours-versus-thirty-minutes asymmetry does not.', 'The two-and-a-half-hours-versus-half-an-hour asymmetry does not.'),
    ('~30 min each way, metro\u00a0ticket', '≈ 26 min each way by train, metro\u00a0ticket'),
    ('→ book weeks ahead, it’s guided and sells out; for the arena floor alone, check the current official release window (recently about a week\u00a0out)',
     '→ book the day sales open, 30 days ahead; it sells out fast. The arena floor alone opens about 7 days\u00a0ahead'),
    ('Book weeks ahead; for the arena floor alone, check the current official release window instead (Decision\u00a006).',
     'Book the day sales open: 30 days ahead for the underground, about 7 for the arena floor (Decision\u00a006).'),
    ('A day or two ahead', 'A few days ahead'),
    ('The top three punish a late booking with “sold out.”', 'The bars that reach 30 days, and the two whose window is unpublished, punish a late booking with “sold out.”'),
    # Ruth recheck v6, the 18 open minors (studio, 2026-10-28; owner: "vas y avec les remarques")
    ('The historic core is a kilometer and a half across. You walk it.', 'The historic core sits within a kilometer and a half of its center. You walk it.'),   # m2
    ('the fifteen or so choices that decide', 'the nine choices that decide'),   # m3
    ('resolving the fifteen calls in advance', 'resolving the nine calls in advance'),   # m3
    ('no line reaches it', 'no line crosses it'),   # m7
    ('The two metro lines cross at Termini and run to the edges;', 'Lines A and B cross at Termini and run to the edges, and Line C stops at the Colosseum;'),   # m7
    ('The cheapest and “best-connected” base is the farthest from what you actually walk to.', 'The cheapest and “best-connected” base, Termini, is twice as far from what you actually walk to as the core.'),   # m8
    ('you would rather have a whole day somewhere real than half a day somewhere famous.', 'you would rather spend half a day somewhere real than a whole day reaching somewhere famous.'),   # m9
    ('Costs you a good meal, or marks you as a tourist', 'Costs you a meal, a fine, or marks you as a tourist'),   # m14
    ('08:30 · at opening', '8:30 a.m. · at opening'),   # m16
    ('locals after 20:30', 'locals after 8:30 p.m.'),   # m16
    ('the center is restricted, the ZTL fines tourists automatically,', 'the center is a limited-traffic zone (ZTL) whose cameras fine unauthorized cars, rentals included,'),   # m17
    ('with a hard cap and no walk-ins whatsoever.', 'with a hard cap, every ticket booked; leftover “last-minute” tickets are never sold on free Sundays.'),   # m23
    ('no walk-ins, ever.', 'every ticket booked ahead.'),   # m23
    ('a hard cap and no walk-ins, so', 'a hard cap and every ticket booked, so'),   # m23
    ('mandatory slot, no walk-ins', 'mandatory slot, booked ahead'),   # m23
    ('book on sale — mandatory, no walk-ins', 'book on sale — required for every ticket'),   # m23
    ('A day or two — Colosseum standard, pantheon', '30 days out — Colosseum standard · Pantheon: none'),   # n10 (the v5 fix missed the lower-case p)
    ('the Colosseum’s arena floor vanish fastest — the arena’s window opens about 7 days ahead; reserve the moment it opens.', 'the Colosseum’s underground vanish fastest: the underground goes on sale 30 days ahead, the arena floor alone about 7.'),   # n10
    ('From April through October, book it when your dates are firm, because', 'From April through October, book it the day the 30-day sale opens, because'),   # n10
    ('The live booking windows are the Field Sheet’s core; the ordering above is stable.', 'The Field Sheet carries the windows that are published (the Colosseum’s) and says “check current” where none is; the ordering above is stable.'),   # n6
    ('Train times and site hours change; the Field Sheet carries the current ones.', 'Train times and site hours change: the Field Sheet carries the Ostia leg; check Pompeii’s the week you go.'),   # n6
]
EXACT = {   # whole text nodes, where a substring rule would also hit a longer label
    'Term': 'Termini',   # m6: Fig. 1 label
    'THE DAY SALES OPEN': '30 DAYS AHEAD',   # n10: the poster axis, in days
    'YOUR DATES ARE FIRM →': 'THE DAY YOU VISIT →',
}
X0, PXE = 136.3, 4.835          # Fig. 5: €0 at x 136.3, 4.835 px a euro
H0, PXH = 136.3, 28.2           # Fig. 9: 0 h at x 136.3, 28.2 px an hour
D0, PXD = 166.5, (480.4 - 166.5) / 30   # Fig. 7 redrawn: 0 to 30 days

def _bar(svg, y, x, w, fill):
    p = svg.find('path', d=re.compile(rf'^M{x:.1f},{y:.1f} h'))
    if p is not None: p['d'] = f'M{x:.1f},{y:.1f} h{w:.1f} v{p["d"].split(" v")[1].split(" ")[0]} h-{w:.1f} Z'; p['fill'] = fill
    return p

def fig7(sp):
    rows = [('Colosseum Underground', 30, 'on sale 30 days ahead, sells out fast', 'bar'),
            ('Colosseum Standard', 30, 'on sale 30 days ahead', 'bar'),
            ('Vatican Museums', 30, 'timed · sells out in peak · window: check current', 'open'),
            ('Borghese Gallery', 30, 'booking required for every ticket · window: check current', 'open'),
            ('Colosseum Arena', 7, 'opens ≈ 7 days ahead', 'bar'),
            ('Pantheon', 0, 'no booking needed · buy at the door', 'dot'),
            ('St. Peter’s Basilica', 0, 'free · no ticket, only timing', 'dot')]
    out = ['<path d="M28.2,210.0 h475.5 v0.8 h-475.5 Z" fill="#DED0AF"/>', '<path d="M28.3,1.5 h475.2 v201.6 h-475.2 Z" fill="#F6EEDB"/>',
           '<text class="mono" font-size="5.8" x="96.0" y="18.5">days ahead → visit</text>']
    for dd in (0, 7, 14, 21, 30):
        x = D0 + dd * PXD
        out.append(f'<path d="M{x:.1f},23.1 L{x:.1f},182.0" fill="none" stroke="#DED0AF" stroke-width="0.36"/>')
        out.append(f'<text class="mono" font-size="5.8" x="{x - 3:.1f}" y="18.5">{dd}</text>')
    for k, (name, dd, note, kind) in enumerate(rows):
        y = 28.0 + k * 22.5
        out.append(f'<text class="lab" font-size="8.3" x="28.0" y="{y + 9:.1f}">{name}</text>')
        w = dd * PXD
        if kind == 'bar':
            out.append(f'<path d="M{D0:.1f},{y:.1f} h{w:.1f} v11.0 h-{w:.1f} Z" fill="#8A3324"/>')
            if w > 200: out.append(f'<text class="mono" font-size="5.8" x="{D0 + w - 4:.1f}" y="{y + 7.6:.1f}" text-anchor="end" fill="#F6EEDB" style="fill:#F6EEDB" data-nochip="1">{note}</text>')
            else: out.append(f'<text class="mono" font-size="5.8" x="{D0 + w + 5:.1f}" y="{y + 7.6:.1f}">{note}</text>')
        elif kind == 'open':
            out.append(f'<path d="M{D0:.1f},{y + 0.5:.1f} h{w:.1f} v10.0 h-{w:.1f} Z" fill="none" stroke="#8A3324" stroke-width="0.9" stroke-dasharray="3 2"/>')
            out.append(f'<text class="mono" font-size="5.8" x="{D0 + 5:.1f}" y="{y + 7.6:.1f}">{note}</text>')
        else:
            out.append(f'<circle cx="{D0:.1f}" cy="{y + 5.5:.1f}" r="4" fill="#C9A84C"/>')
            out.append(f'<text class="mono" font-size="5.8" x="{D0 + 9:.1f}" y="{y + 7.6:.1f}">{note}</text>')
    return ''.join(out)

def apply(html):
    sp = BeautifulSoup(html, 'html.parser')
    for n in list(sp.find_all(string=True)):
        t = str(n)
        for a, b in TEXT:
            if a in t: t = t.replace(a, b)
            elif '\xa0' in t and ' ' in a:   # the typesetter's no-break spaces (widow control) must not hide a match
                t = re.sub(re.escape(a).replace('\\ ', ' ').replace(' ', '[ \xa0]'), lambda m: b, t)
        if t.strip() in EXACT and n.parent is not None and n.parent.name == 'text': t = t.replace(t.strip(), EXACT[t.strip()])
        if t != str(n): n.replace_with(t)
    back = sp.select_one('#the-wallet-card .card.back')   # X7: the card points to the current figures
    if back is not None and 'guide/sheet' not in back.get_text():
        back.append(BeautifulSoup('<div class="ln sheetref"><b>Current figures</b><span>the Field Sheet · romeforamericans.com/guide/sheet</span></div>', 'html.parser'))
    f5 = sp.select_one('figure.fig[data-fig="5"] svg')
    if f5 is not None:   # two people: train ≈ €28 + hop up to €13 = ≈ €31–41; near Termini the train alone, ≈ €28
        _bar(f5, 36.8, 136.3, 28 * PXE, '#8A3324'); p = f5.find('path', d=re.compile(r'^M204\.7,36\.8 h'))
        if p is not None: p['d'] = f'M{X0 + 28 * PXE:.1f},36.8 h{13 * PXE:.1f} v11.5 h-{13 * PXE:.1f} Z'
        _bar(f5, 110.2, 136.3, 28 * PXE, '#8A3324')
        for t in f5.find_all('text'):
            s = t.get_text()
            if s == '≈€27': t.string = '≈€31–41'; t['x'] = f'{X0 + 41 * PXE + 4:.1f}'
            elif s == '≈€14': t.string = '≈€28'; t['x'] = f'{X0 + 28 * PXE + 4:.1f}'
            elif s == 'onward': t['x'] = f'{X0 + 28 * PXE + 4:.1f}'
            elif s == 'CENTRAL BASE (Decision 01)': t.string = 'CENTRAL BASE (Decision 01) · TWO PEOPLE'
    f9 = sp.select_one('figure.fig[data-fig="9"] svg')
    if f9 is not None:   # Pompeii: ≈ 2½ h + 6–7 h + ≈ 2½ h = ≈ 12 h door to door
        segs = [(136.3, 2.5, '#7A6B4E'), (H0 + 2.5 * PXH, 7, '#8A3324'), (H0 + 9.5 * PXH, 2.5, '#7A6B4E')]
        old = [p for p in f9.find_all('path') if re.match(r'^M[\d.]+,102\.3 h', p.get('d', ''))]
        for p, (x, h, c) in zip(old, segs): p['d'] = f'M{x:.1f},102.3 h{h * PXH:.1f} v13.0 h-{h * PXH:.1f} Z'; p['fill'] = c
        for t in f9.find_all('text'):
            s = t.get_text()
            if s == 'train + Circumvesuviana': t.string = '≈ 2½ h'; t['x'] = f'{H0 + 6:.1f}'
            elif s == 'the ruins' and float(t.get('y', 0)) > 100: t.string = 'the ruins · 6–7 h'; t['x'] = f'{H0 + 2.5 * PXH + 8:.1f}'
            elif s == 'return': t.string = '≈ 2½ h'; t['x'] = f'{H0 + 9.5 * PXH + 6:.1f}'
            elif s.startswith('≈ 12 h door-to-door'): t.string = '≈ 12 h door to door · train + Circumvesuviana each way · “don’t pair with anything”'
    f7 = sp.select_one('figure.fig[data-fig="7"] svg')
    if f7 is not None:
        f7.clear(); f7.append(BeautifulSoup(fig7(sp), 'html.parser'))
    return str(sp)
