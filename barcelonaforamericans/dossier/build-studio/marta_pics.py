# -*- coding: utf-8 -*-
"""marta_pics.py — Marta Serra's picture edit of Barcelona (ledger: _studio/marta/pictures.json, 2026-10-25),
applied to the composed book. The ledger is the source of truth: kills, moves, replacements, captions.

  a frame the ledger kills is not printed; on a closing page its place is taken by a typographic field:
    a decision keeps its verdict word in gold on the ink field (HOTEL, 4, 3, 2+1, 20:30);
    an essay closes on its own name, large on the red field (its call is already on the poster); a closing
    with almost no text (<200 characters) has no page: its words join the prose;
  a frame that moves is printed where the ruling sends it, with the caption the ledger proposes;
  a frame that stays takes its proposed caption; A03 and A05 print whole at the measure.
"""
import json, os, re
from bs4 import BeautifulSoup

LEDGER = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_studio', 'marta', 'pictures.json')
L = json.load(open(LEDGER, encoding='utf-8'))
KILLED = {e['src'] for e in L if e.get('killed')}
CAPTION = {e['src']: e['caption_proposed'] for e in L if e.get('caption_proposed') and not e.get('killed')}
# Unsplash frames chosen by Marta 2026-10-26 (_studio/marta/unsplash-picks.json; Unsplash License, free commercial use)
UNSPLASH = {'img/u-howto.jpg': 'https://images.unsplash.com/photo-1623654810065-0ada78ee958e',
            'img/u-timing.jpg': 'https://images.unsplash.com/photo-1780686748774-57b60840b00e',
            'img/u-parkguell-bench.jpg': 'https://images.unsplash.com/photo-1729286286747-f5f8e1d8ce2d'}
MARGIN = {'setpieces': ('img/u-parkguell-bench.jpg', "Park Güell's serpentine bench on the terrace: the part your timed slot buys, and the free park does not.")}
REPLACE = {'img/p-howto.jpg': 'img/u-howto.jpg', 'img/p-timing.jpg': 'img/u-timing.jpg', 'img/p-dayzero.jpg': 'img/p-fly.jpg',
           'img/A07.jpg': 'img/h-plan.jpg', 'img/h-risk.jpg': 'img/p-contract.jpg'}
CAPTION_FIX = {'img/u-howto.jpg': "Passeig de Gràcia at Provença, La Pedrera behind: the street points to every door; the Book has already said which.",
               'img/u-timing.jpg': "Barceloneta on a gray day, the sand nearly empty: the sea out of play, the city behind it intact.",
               'img/p-fly.jpg': "El Prat, the terminal lettered BARCELONA: a T-casual stops at its metro gate, though the train and the bus still take it."}   # Ruth N2, 2026-10-25
MOVED_FROM = {'img/p-contract.jpg', 'img/p-fly.jpg', 'img/h-plan.jpg'}   # their old places print no picture
POS = {'img/h-plan.jpg': '23% 50%', 'img/u-howto.jpg': '0% 50%', 'img/u-timing.jpg': '100% 50%'}   # window x 0.06–0.795: Sagrada Família whole
WHOLE = {'img/A03.jpg', 'img/A05.jpg'}   # print whole at the measure, never a band

CSS = """
/* Marta's picture edit (studio 2026-10-25) */
.photo.typo .field{ height:740px; background:var(--red); color:var(--paper); position:relative; overflow:hidden; }
.photo.typo .field .call{ position:absolute; left:76px; right:82px; bottom:56px; font-weight:800; font-stretch:88%; font-size:96px; line-height:.9; letter-spacing:-.03em; word-spacing:.12em; }
.photo.typo .field .lab{ position:absolute; left:82px; top:72px; font-size:9px; font-weight:700; letter-spacing:.2em; text-transform:uppercase; }
.photo.duo.typo .dw{ background:var(--ink); }
figure.band.whole{ width:652px; clear:both; display:grid; grid-template-columns:340px 264px; column-gap:48px; align-items:end; }   /* whole, on the 340 column, flush left; the caption beside it in the margin, on its foot */
figure.band.whole img{ width:340px !important; height:auto !important; object-fit:initial; }
figure.band.whole figcaption{ margin:0; }
.aside figure.mside{ margin:0 0 20px; break-inside:avoid; } .aside figure.mside img{ display:block; width:264px; height:auto; } .aside figure.mside figcaption{ font-size:9px; line-height:13px; font-weight:600; color:var(--grey); margin-top:8px; }
"""

def apply(html):
    CAPTION.update(CAPTION_FIX)
    html = html.replace('</style>', CSS + '</style>', 1)
    sp = BeautifulSoup(html, 'html.parser')
    for img in list(sp.find_all('img')):
        src = img.get('src', '')
        if img.find_parent('svg') or img.find_parent(class_='poster'): continue
        photo = img.find_parent(class_='photo'); fig = img.find_parent('figure')
        if src in REPLACE:
            new = REPLACE[src]; img['src'] = new
            if new in POS: img['style'] = f'object-position:{POS[new]}'
            cap = (photo.find(class_='cap') if photo else None) or (fig.find('figcaption') if fig else None)
            if cap is not None and new in CAPTION: cap.string = CAPTION[new]
            if fig is not None and photo is None and 'band' in (fig.get('class') or []): fig['class'] = fig['class'] + ['whole']
            continue
        if src in KILLED or src in MOVED_FROM:
            if photo is not None:   # a closing page: the typographic field
                sec = photo.find_parent('section')
                cap = photo.find(class_='cap')
                if cap is not None: cap.decompose()
                photo['class'] = photo.get('class', []) + ['typo']
                dw = img.find_parent(class_='dw')
                if dw is not None:   # a decision: its verdict word stays, on ink
                    for x in dw.find_all(class_=['tone', 'lift']): x.decompose()
                    img.decompose()
                elif sec is not None and sec.find_all(class_='pg') and (len((photo.find(class_='tail') or photo).get_text(' ', strip=True)) < 200 or sec.get('id') in MARGIN):   # a chapter that already carries a margin picture closes in its prose
                    # an essay with no true picture ends in its prose: the tail joins the text page, no closing page
                    # (a field naming the chapter read as a new opener; a field repeating the poster printed twice)
                    last_pg = sec.find_all(class_='pg')[-1]
                    tail = photo.find(class_='tail')
                    for el in list(tail.find_all(['p', 'div'], recursive=True)) if tail else []:
                        if el.name == 'p' and el.find_parent(class_='vol') is None:
                            el['class'] = (el.get('class') or []) + ['t']; last_pg.append(el.extract())
                    vol = tail.find(class_='vol') if tail else None
                    if vol is not None: last_pg.append(vol.extract())
                    photo.decompose()
                else:
                    big = sec.select_one('.poster .foot .big') if sec else None
                    title = sec.find('h1') if sec else None
                    field = sp.new_tag('div', attrs={'class': 'field'})
                    # the field closes the chapter on its name: its call is already on the poster (Marta: nothing prints twice)
                    lab = sp.new_tag('span', attrs={'class': 'lab'}); lab.string = 'End of chapter'
                    call = sp.new_tag('div', attrs={'class': 'call'}); call.string = title.get_text(' ', strip=True) if title else ''
                    field.append(lab); field.append(call); img.replace_with(field)
            elif fig is not None:
                fig.decompose()
            else:
                img.decompose()
            continue
        if src in CAPTION:
            cap = (photo.find(class_='cap') if photo else None) or (fig.find('figcaption') if fig else None)
            if cap is not None: cap.string = CAPTION[src]
        if src in WHOLE and fig is not None:
            fig['class'] = (fig.get('class') or []) + ['whole']
            if img.get('style'): del img['style']   # a fixed band height shrank the frame and centred it
    for sid, (src, cap) in MARGIN.items():   # a margin picture beside the prose it proves
        sec = sp.find('section', id=sid)
        h2 = next((h for h in sec.find_all('h2') if 'Park Güell' in h.get_text()), None) if sec else None
        if h2 is not None:   # beside the section it proves, not stacked under the top margin (it pushed the prose)
            box = sp.new_tag('div', attrs={'class': 'aside'})
            fig = sp.new_tag('figure', attrs={'class': 'mside'}); im = sp.new_tag('img', attrs={'src': src})
            fc = sp.new_tag('figcaption'); fc.string = cap; fig.append(im); fig.append(fc); box.append(fig); h2.insert_after(box)
    return str(sp)
