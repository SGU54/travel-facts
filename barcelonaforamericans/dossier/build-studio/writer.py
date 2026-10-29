# -*- coding: utf-8 -*-
"""writer.py — the writer's answers to Ruth Calloway's filings (studio, 2026-10-25), applied to the raw
manuscript before composing. Each edit: (Ruth's id, the text as it stands, the text as it becomes, the source).
Her reading: _studio/ruth/critic.md. A edit that no longer matches stops the build (the text moved: re-read it)."""
import re

OFF = '<span class="mk off">&#9671;</span>'
OFF_Q = "<span class='mk off'>&#9671;</span>"
EDITS = [
 # B2 — the basilica refuses resold tickets: General Conditions 3.9 and 4.3 (sagradafamilia.org, read by Ruth 2026-10-25)
 ('B2', 'Book a morning slot on sagradafamilia.org, the only official seller ' + OFF + '.',
        'Book a morning slot on sagradafamilia.org, the official seller ' + OFF + '.', 'conditions 4.3'),
 ('B2', 'Authorised resellers hold real allocations ' + OFF + ' only when the official calendar is genuinely full.',
        'If it is full, re-check the official site for released mornings: the basilica refuses resold tickets at the door ' + OFF + '.', 'conditions 3.9, 4.3; no published list (Ruth recheck)'),
 ('B2', "Book on sagradafamilia.org, the only official seller " + OFF_Q + "; authorised resellers hold real allocations <span class='mk est'>&#9679;</span> when it is full.",
        "Book on sagradafamilia.org " + OFF_Q + "; when it is full, re-check it for released slots rather than buying elsewhere, since the basilica refuses any ticket bought through a reseller " + OFF_Q + ".", 'conditions 3.9, 4.3'),
 ('B2', "Take an authorised reseller's allocation rather than an unofficial one,",
        "Re-check sagradafamilia.org for released mornings rather than buying elsewhere (a resold ticket is refused at the door),", 'conditions 3.9, 4.3'),
 # B1 — one numbering of days across the book: the arrival day holds nothing timed (p17)
 ('B1', 'It assumes five days, an Eixample base and the two bookings made.',
        'It assumes five full days after the arrival day (Day Zero, which holds nothing timed), an Eixample base and the two bookings made.', 'p17'),
 # M2 — "the arithmetic" is promised and never computed: the book shows the reasoning; the Sheet shows the sums
 ('M2', 'The book puts them in one place, with the arithmetic shown, so the judgment is yours.',
        'The book puts them in one place, with the reasoning shown and the sums on the Field Sheet, so the judgment is yours.', '—'),
 ('M2', 'before you have seen the arithmetic in decision 03.', 'before you have read decision 03.', '—'),
 # M4 — the T-casual still reaches the airport by train or bus (ATM: "you can still reach the airport… using the Rodalies de Catalunya train network or by bus")
 ('M4', 'The alternatives (the airport bus, a taxi, a pre-booked transfer) are all legitimate.',
        'A T-casual still gets you there another way: the Rodalies R2 Nord train, which serves Terminal 2 only, or the city bus ' + OFF + '. From T1 the metro ticket saves the shuttle to T2, which is when it is still the better buy. The alternatives (the Aerobús, a taxi, a pre-booked transfer) are all legitimate.', 'atm.cat (Ruth sheet-values row 8)'),
 # M5 — the hotel binds too in the centenary year (Fig. 6, p14)
 ('M5', 'Only two things genuinely bind. Everything else can be arranged a day ahead —',
        'Only two things genuinely bind, and the bed, which you book early in a centenary year. Everything else can be arranged a day ahead —', 'Fig. 6, p14'),
 # M6 — p52 refers to a checklist item that did not exist
 ('M6', "<li><strong>Check your cards' foreign-transaction fees</strong>",
        "<li><strong>Save your card issuers’ emergency numbers</strong> somewhere that is not your wallet.</li>\n    <li><strong>Check your cards' foreign-transaction fees</strong>", 'p52'),
 # M10 — the emergency number and the passport rule (Schengen Borders Code art. 6; travel.state.gov, Spain)
 ('M10', 'For a lost passport, contact the US Consulate.',
         'The emergency number anywhere in Spain is 112 ' + OFF + '. For a lost passport, contact the US Consulate.', '112.gob / EU'),
 ('M10', ' and you do not need it for a trip this year ' + OFF + '.</p>',
         ' and you do not need it for a trip this year ' + OFF + '. Your passport must be valid three months past the day you leave the Schengen area ' + OFF + '.</p>', 'travel.state.gov'),
 # M3 — the Field Sheet: every row the book defers to carries a value (atc.gencat.cat tariff from 1 April 2026)
 ('M3', '<tr><td>Licensed tourist apartments</td><td class="n">higher surcharge tier &#9670;</td></tr>',
        '<tr><td>3-star hotels and below</td><td class="n">&asymp; &euro;7.00 &#9670;</td></tr>\n    <tr><td>Licensed tourist apartments</td><td class="n">&asymp; &euro;9.50 &#9670;</td></tr>', 'atc.gencat.cat'),
 ('M3', "Rates rose 1 April 2026 and combine a Catalan regional rate with Barcelona's municipal surcharge. The surcharge is politically live and has risen twice recently — confirm the current figure with your accommodation when you book.",
        "Catalan rate plus Barcelona's surcharge, from 1 April 2026: two people, five nights at a 4-star ≈ €84. The surcharge moves — confirm it when you book.", 'Field Sheet on one sheet'),
 ('M3', "The Book's calls hold regardless of the exact figures; these are the inputs to the arithmetic, kept here so the analysis stays current where you can check it. If a website",
        "The Book's calls hold whatever the figures. If a website", 'Field Sheet on one sheet'),
 # M3 v2 — official values read by Ruth on 2026-10-25 (_studio/ruth/sheet-values.md)
 ('M3', '<td class="n">check current &#9670;</td></tr>\n    <tr><td>Hola Barcelona travel card',
        '<td class="n">&asymp; &euro;13.00 &#9670;</td></tr>\n    <tr><td>Hola Barcelona travel card', 'atm.cat t-casual; tmb.cat'),
 ('M3', '<td>Sagrada Família — basilica entry (centenary-year demand)</td><td class="n">sagradafamilia.org &#9670;</td>',
        '<td>Sagrada Família — basilica entry, on sagradafamilia.org only</td><td class="n">&asymp; &euro;26.00 &#9670;</td>', 'sagradafamilia.org/en/prices'),
 ('M3', '<td>Park Güell — monumental zone, timed</td><td class="n">check current &#9670;</td>',
        '<td>Park Güell — monumental zone, timed, online</td><td class="n">&asymp; &euro;18.00 &#9670;</td>', 'parkguell.barcelona prices'),
 ('M3', '<span class="fsdate">Compiled 2026 · verify before travel</span>',
        '<span class="fsdate">Compiled October 2026 · verify before travel</span>', '—'),
]

def _rows(rows):
    return '<tbody>' + ''.join(f'<tr><td><span class="opt">{k}</span></td><td><span class="sub">{v}</span></td><td class="num"></td></tr>' for k, v in rows) + '</tbody>'
PLAN5 = [('Arrival day', 'Nothing timed. The Gothic Quarter on foot, a plaça, an early dinner — and the airport return ticket bought while you are calm.'),
         ('Day 1', 'Sagrada Família on the morning slot, then the Eixample on foot: one house, Batlló or La Pedrera, not both.'),
         ('Day 2', 'Park Güell early on your slot, Gràcia afterwards, menú del día at lunch.'),
         ('Day 3', 'The variety day, unbooked: a market, an interior, the hill in the afternoon, the sea at golden hour.'),
         ('Day 4', "Montserrat, the whole day. FGC R5 from Plaça d'Espanya, then the cable car."),
         ('Day 5', 'The floating day: the beach if it is warm, Montjuïc if it is not. Nothing booked, on purpose.')]
PLAN3 = [('Arrival day', 'Nothing timed, the old city on foot.'),
         ('Day 1', 'Sagrada Família in the morning, one Gaudí house in the afternoon.'),
         ('Day 2', 'Park Güell on an early slot, then Gràcia or the Born at your own pace — and the menú del día, which is the one food rule that fits a short trip.'),
         ('Day 3', 'The floating day: a market, a neighborhood you have not walked, the beach if it is warm.')]
def plans(doc):
    """N1 (Ruth recheck): the two shapes count days as The Plan does (p54) — the arrival day, then five
    full days in its order; three days = The Plan compressed (day one kept, two and three merged, no day trip)."""
    for name, new_name, rows in (('Five days, first visit, Eixample base', 'Five days after the arrival day, first visit, Eixample base', PLAN5),
                                 ('Three days, first visit, no day trip', 'Three days after the arrival day, first visit, no day trip', PLAN3)):
        i = doc.find(f'<p class="tname">{name}</p>')
        if i < 0: raise SystemExit(f'writer: plan "{name}" not found')
        j = doc.find('<tbody>', i); k = doc.find('</tbody>', j) + len('</tbody>')
        doc = doc[:i] + doc[i:j].replace(name, new_name) + _rows(rows) + doc[k:]
    return doc

def renumber_days(doc):
    """B1: the before-you-book plans count the arrival day as the book does — Day Zero holds nothing timed,
    Day 1 is the first full day (The Plan, p54)."""
    a = doc.find('id="beforeyoubook"'); b = doc.find('</section>', a)
    if a < 0: raise SystemExit('writer: before-you-book section not found')
    seg = doc[a:b]
    seg = re.sub(r'<span class="opt">Day (\d)</span>', lambda m: '<span class="opt">' + ('Arrival day' if m.group(1) == '1' else f'Day {int(m.group(1)) - 1}') + '</span>', seg)
    return doc[:a] + seg + doc[b:]

def write(doc):
    for fid, old, new, src in EDITS:
        if doc.count(old) != 1: raise SystemExit(f'writer: {fid} no longer matches once ({doc.count(old)}×): {old[:60]}')
        doc = doc.replace(old, new)
    return plans(doc)   # (renumber_days is superseded: the plans are rebuilt from The Plan)
