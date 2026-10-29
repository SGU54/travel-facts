# -*- coding: utf-8 -*-
"""marta_pics.py — Marta Serra's picture edit of Rome (ledger: atelier-critic-2026-10-25/pictures-calibration.json; from Barcelona's module, 2026-10-26),
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

LEDGER = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'atelier-critic-2026-10-25', 'pictures-calibration.json')
L = json.load(open(LEDGER, encoding='utf-8'))
KILLED = {e['src'] for e in L if e.get('killed')} | {'img/p03-0.jpeg'}   # p5: the Forum again, the twice loser (p68's Forum is kept)
CAPTION = {e['src']: e['caption_proposed'] for e in L if e.get('caption_proposed') and not e.get('killed')}
# Unsplash frames chosen by Marta 2026-10-26 (_studio/marta/unsplash-picks.json; Unsplash License, free commercial use)
UNSPLASH = {}   # filled from _studio/marta/unsplash-picks.json when Marta's Rome picks land
MARGIN = {}   # the sampietrini frame had no margin to stand in (Before you fly is a full-width checklist): not printed
SECTION_NEW = {'how-to-read-this-book': ('img/u-pantheon-fountain.jpg', 'The Pantheon fountain: a claim cut in 1711, the restoration dated 1974 beneath it. A source and a date, as every mark here carries.', '62% 45%'), 'why-the-obvious-tool-doesn-t': ('img/u-metro-barberini.jpg', "Line A at Barberini, on the core's edge: the train for the hop across the river, not for the centre it curves around.", '100% 50%'), 'd06': ('img/u-borghese-pluto.jpg', "Bernini's Pluto and Proserpina in the Galleria Borghese: no walk-ins, ever. One of the three you book the day your dates are firm.", '40% 60%'), 'the-plan-as-operations': ('img/u-momo-stair.jpg', 'The Momo stair at the Vatican Museums: the Vatican is its own half-day, booked early, and it never shares one with the Forum.', '50% 55%'), 'day-trips-ranked-by-the-day-': ('img/u-orvieto.jpg', "The central portal of Orvieto's cathedral, an hour out by direct train: the near name, not the famous one.", '50% 65%')}   # Unsplash closings chosen by Marta 2026-10-26 (_studio/marta/unsplash-picks.json)
REPLACE = {'img/p21-0.jpeg': 'img/p49-0.jpeg'}   # the Forum moves to Decision 04's closing (ruling)
CAPTION_FIX = {}
MOVED_FROM = {'img/p49-0.jpeg'}   # its p68 closing then closes typographically
POS = {'img/p49-0.jpeg': '50% 50%'}
WHOLE = {'img/stay-rooftops.jpeg', 'img/p28-0.jpeg'}   # whole on the 340 column, caption beside (the owner's Barcelona ruling)

CSS = """
/* Marta's picture edit (studio 2026-10-26, Rome) */
#d04 .photo.duo .dw .word{ top:44px; bottom:auto; left:auto; right:56px; }   /* the ½ in the clear sky right of the Vittoriano */
#d09 .photo.duo .dw .word{ top:44px; bottom:auto; }
#d06 .photo.duo .dw .word{ top:44px; bottom:auto; left:auto; right:56px; }   /* the 3 in the ceiling, top right (Marta) */   /* OSTIA in the open sky above the arcades */
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
            sec0 = photo.find_parent('section') if photo is not None else None
            if photo is not None and sec0 is not None and sec0.get('id') in SECTION_NEW and not photo.get('data-new'):
                nsrc, ncap, npos = SECTION_NEW[sec0['id']]; img['src'] = nsrc; img['style'] = f'object-position:{npos}'; photo['data-new'] = '1'
                cap = photo.find(class_='cap')
                if cap is not None: cap.string = ncap
                continue
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
            elif fig is not None:   # a figure printed with no caption gets the one the ledger proposes
                fc = sp.new_tag('figcaption'); fc.string = CAPTION[src]; fig.append(fc)
        if src in WHOLE and fig is not None:
            fig['class'] = (fig.get('class') or []) + ['whole']
            if fig.get('style'): del fig['style']   # the composer's own grid would override the 340 + caption-beside rule
            if img.get('style'): del img['style']   # a fixed band height shrank the frame and centred it
    for sid, (src, cap) in MARGIN.items():   # a margin picture beside the prose it proves: at the foot of the chapter's first margin
        sec = sp.find('section', id=sid); aside = sec.find(class_='aside') if sec else None
        if aside is not None:
            fig = sp.new_tag('figure', attrs={'class': 'mside'}); im = sp.new_tag('img', attrs={'src': src})
            fc = sp.new_tag('figcaption'); fc.string = cap; fig.append(im); fig.append(fc); aside.append(fig)
    return str(sp)
