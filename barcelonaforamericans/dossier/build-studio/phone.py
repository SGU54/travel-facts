# -*- coding: utf-8 -*-
"""phone.py — the phone edition of Barcelona, Without the Traps. (studio, 2026-10-26).

Same words as the book (the manuscript + the writer's answers to Ruth + Brunner's US style), same
pictures (Marta's ledger), in one column at reading size for a phone held upright: a 3.6 × 7.2 in page,
11 pt body, which a phone shows at about 16 CSS px. The Field Sheet is printed at the end.

  python3 phone.py     → phone.html, Barcelona-Without-the-Traps-phone.pdf (bookmarked)
"""
import os, re, sys, json
sys.path.insert(0, os.path.expanduser('~/.claude/skills/atelier/scripts'))
from bs4 import BeautifulSoup
from brunner_set import brunner_set, us_house
import writer, marta_pics as MP
from playwright.sync_api import sync_playwright
import pymupdf
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
doc = writer.write(open('dossier3.raw.html', encoding='utf-8').read())
sp = BeautifulSoup(doc, 'lxml')

# ── Marta's picture edit, on the manuscript ──
MP.CAPTION.update(MP.CAPTION_FIX)
os.makedirs('_phone/img', exist_ok=True)
def small(src):   # phone-sized copy: 1000 px wide is ample at 3.6 in
    out = '_phone/' + src
    if not os.path.exists(out):
        im = Image.open(src).convert('RGB'); im.thumbnail((1000, 1600)); im.save(out, quality=82)
    return out
BOOK_IMGS = set(re.findall(r'<img[^>]*src="(img/[^"]+)"', open('dossier3.html', encoding='utf-8').read()))   # only what the book prints
for fig in list(sp.find_all('figure')):
    img = fig.find('img')
    if img is None: continue
    src = img.get('src', '')
    if src in MP.REPLACE: src = MP.REPLACE[src]
    elif src in MP.KILLED or src in MP.MOVED_FROM or src not in BOOK_IMGS: fig.decompose(); continue
    for k in ('width', 'height', 'decoding', 'loading', 'style'): img.attrs.pop(k, None)
    img['src'] = small(src)
    cap = fig.find('figcaption')
    if cap is not None:
        for pl in cap.find_all(class_='pl'): pl.decompose()
        if src in MP.CAPTION: cap.string = MP.CAPTION[src]
for sid, (src, capt) in MP.MARGIN.items():
    sec = sp.find('section', id=sid)
    h2 = next((h for h in sec.find_all('h2') if 'Park Güell' in h.get_text()), None) if sec else None
    if h2 is not None:
        f = BeautifulSoup(f'<figure class="photo"><img src="{small(src)}"><figcaption>{capt}</figcaption></figure>', 'html.parser')
        h2.insert_after(f)
# closings the studio filled from Unsplash (howto, timing) print after their chapter
for sid, src in (('howto', 'img/u-howto.jpg'), ('timing', 'img/u-timing.jpg')):
    sec = sp.find('section', id=sid)
    if sec is not None and not sec.find('img', src=re.compile('u-')):
        sec.append(BeautifulSoup(f'<figure class="photo"><img src="{small(src)}"><figcaption>{MP.CAPTION[src]}</figcaption></figure>', 'html.parser'))
for j in json.load(open('_studio/writer/joins.json', encoding='utf-8')):   # the join the free guides never make, after the verdict
    sec = sp.find('section', id=j['section_id']); v = sec.find(class_='verdict') if sec else None
    if v is not None:
        v.insert_after(BeautifulSoup(f'<div class="join"><span class="lab">What the free guides never connect</span><p>{j["text"]}</p></div>', 'html.parser'))
for x in sp.select('.rh-src, .dots'): x.decompose()
# figure type in faces that are loaded (a missing family or weight is synthesised and embeds as Type3)
for svg in sp.find_all('svg'):
    for el in svg.find_all(True):
        if el.get('font-family'): el['font-family'] = 'Archivo, Symbols, sans-serif'
        if el.get('font-weight'): el['font-weight'] = {'300': '400', '500': '400', '600': '700', 'bold': '700', '900': '800'}.get(str(el['font-weight']), str(el['font-weight']))
        if el.get('font-style') == 'italic': del el['font-style']
    if svg.get('font-family'): svg['font-family'] = 'Archivo, Symbols, sans-serif'
    fig = svg.find_parent('figure')
    vb = [float(x) for x in re.split(r'[ ,]+', (svg.get('viewbox') or svg.get('viewBox') or '0 0 1 1').strip())]
    wide = len(vb) == 4 and vb[3] / vb[2] < 0.55   # only a figure much wider than tall gains by turning; a square map stays upright
    if fig is not None and not fig.find('img') and wide:   # a drawn figure: a quarter turn on its own page, read with the phone sideways
        fig['class'] = (fig.get('class') or []) + ['turn']
        rot = sp.new_tag('div', attrs={'class': 'rot'})
        for ch in list(fig.children): rot.append(ch.extract())
        fig.append(rot)
    # FIG. 6 (the booking horizons): the axis under the bars, the long label inside its bar (as in the book)
    if 'binding constraint' in svg.get_text():
        for t in svg.find_all('text'):
            if re.fullmatch(r'\d+w', t.get_text().strip()): t['y'] = '214'
            if t.get_text().startswith('weeks — shrinking'): t['x'] = str(float(t.get('x', 457)) - 16); t['text-anchor'] = 'end'; t['fill'] = '#F2F7F5'; t.string = 'weeks — supply shrinking, book early'
            if t.get_text().startswith('weeks ahead for the good stock'): t['x'] = str(float(t.get('x', 457)) - 16); t['text-anchor'] = 'end'; t['fill'] = '#F2F7F5'

# the contents: page numbers mean nothing here; the links do
nav = sp.find('nav', class_='toc')
if nav is not None:
    for a in nav.find_all('a'): a.attrs = {'href': a.get('href', '')}

CSS = """
@page { size: 3.6in 7.2in; margin: 0.32in 0.24in 0.42in 0.24in; }   /* white sheet: a tinted page cannot reach Chrome's print margins */
:root{ --ink:#17201C; --red:#A23520; --gold:#E0A828; --paper:#F4F2EC; --grey:#6B7773; --line:#D9D6CE; }
html{ background:#fff; }
body{ font-family:'Archivo', 'Symbols', sans-serif; font-size:11pt; line-height:1.45; color:var(--ink); margin:0; -webkit-print-color-adjust:exact; print-color-adjust:exact; }
section{ margin-top:30pt; } section.decision, section#d01, section#d02, section#d03, section#d05, section#d06, section#d07, section#d08, section#fs, section#contract{ break-before:page; margin-top:0; }   /* essays flow on; a decision and the Sheet open a page */
.kicker{ font-size:7.5pt; font-weight:700; letter-spacing:.14em; text-transform:uppercase; color:var(--red); margin:0 0 4pt; }
h1{ font-size:24pt; line-height:1.0; font-weight:800; font-stretch:88%; letter-spacing:-.02em; margin:0 0 8pt; }
h2{ font-size:14pt; line-height:1.15; font-weight:800; margin:16pt 0 6pt; padding-top:6pt; border-top:2.5pt solid var(--ink); break-after:avoid; }
h3{ font-size:12pt; margin:12pt 0 4pt; break-after:avoid; }
.standfirst{ font-size:13pt; line-height:1.35; margin:0 0 12pt; }
body{ font-synthesis:none; } strong em, b em, .opt em, h1 em, h2 em, h3 em, .verdict strong em{ font-style:normal; }   /* no bold italic is loaded: never synthesise one */
p{ margin:0 0 8pt; hyphens:auto; } p.dropcap::first-letter{ font-weight:800; }
.verdict{ background:var(--red); color:var(--paper); padding:10pt 12pt; margin:10pt 0 12pt; break-inside:avoid; }
.verdict p{ margin:0; font-size:12pt; line-height:1.35; } .verdict strong{ display:block; font-size:15pt; line-height:1.15; margin-bottom:4pt; }
table{ width:100%; border-collapse:collapse; margin:8pt 0 12pt; font-size:10pt; }
table caption{ text-align:left; font-size:7.5pt; font-weight:700; letter-spacing:.12em; text-transform:uppercase; color:var(--grey); padding-bottom:4pt; }
th{ text-align:left; font-size:7.5pt; letter-spacing:.1em; text-transform:uppercase; color:var(--grey); border-bottom:1pt solid var(--line); padding:3pt 0; }
td{ vertical-align:top; padding:5pt 4pt 5pt 0; border-bottom:.6pt solid var(--line); }
table.ledger td:first-child{ width:58%; } .opt{ font-weight:700; display:block; } .sub{ display:block; color:var(--grey); font-size:9.5pt; }
td.n, td.num{ text-align:right; white-space:nowrap; }
.join{ border-top:2.5pt solid var(--gold); padding-top:6pt; margin:0 0 12pt; break-inside:avoid; } .join .lab{ display:block; font-size:7.5pt; font-weight:700; letter-spacing:.12em; text-transform:uppercase; color:var(--red); margin-bottom:3pt; } .join p{ font-size:10.5pt; margin:0; }
.fa .col{ border-left:2pt solid var(--gold); padding-left:8pt; margin:0 0 8pt; }
.note{ border-top:1.5pt solid var(--red); padding-top:6pt; margin:10pt 0; font-size:10pt; } .xref{ display:block; color:var(--grey); }
figure{ margin:10pt 0 12pt; break-inside:avoid; } figure img{ display:block; width:100%; height:auto; }
figure svg{ width:100%; height:auto; display:block; }
figure.turn{ break-before:page; break-after:page; height:6.3in; position:relative; margin:0; }
figure.turn > .rot{ position:absolute; width:6.1in; left:50%; top:50%; transform:translate(-50%,-50%) rotate(90deg); }
figure.turn > .rot figcaption{ font-size:8pt; margin-top:6pt; }
figure.turn::after{ content:"Turn your phone sideways"; position:absolute; bottom:0; left:0; font-size:7pt; letter-spacing:.12em; text-transform:uppercase; color:var(--grey); }
figcaption{ font-size:8.5pt; line-height:1.35; color:var(--grey); margin-top:4pt; }
.mk{ font-family:'Symbols'; font-weight:400; font-style:normal; color:var(--red); font-size:.85em; }
.fail{ border-top:.6pt solid var(--line); padding:5pt 0; } .fail .head{ display:block; font-weight:700; }
.askbox{ border-top:1.5pt solid var(--ink); padding-top:6pt; margin:10pt 0; } .askbox .who{ font-size:7.5pt; font-weight:700; letter-spacing:.12em; text-transform:uppercase; color:var(--red); }
.trip{ margin:10pt 0; } .tname{ font-weight:800; font-size:12pt; } .tassume, .twhy{ font-size:9.5pt; color:var(--grey); }
.wallet .row{ border-top:.6pt solid var(--line); padding:4pt 0; } .wallet .k{ display:block; font-size:7.5pt; font-weight:700; letter-spacing:.1em; text-transform:uppercase; color:var(--grey); }
nav.toc a{ display:block; color:var(--ink); text-decoration:none; padding:5pt 0; border-top:.6pt solid var(--line); }
nav.toc .num{ display:inline-block; width:22pt; font-weight:800; color:var(--red); }
.deadline{ display:block; font-size:7.5pt; font-weight:700; letter-spacing:.12em; text-transform:uppercase; color:var(--red); }
ul{ padding-left:14pt; } li{ margin-bottom:6pt; }
.markskey .line{ padding:3pt 0; }
.fsdate{ color:var(--red); font-weight:700; font-size:8pt; letter-spacing:.08em; text-transform:uppercase; }
.cover{ height:6.4in; background:var(--red); color:var(--paper); padding:18pt 14pt; box-sizing:border-box; display:flex; flex-direction:column; justify-content:flex-end; }
.cover .t{ font-size:38pt; line-height:.9; font-weight:800; font-stretch:80%; letter-spacing:-.03em; }
.cover .s{ font-size:11pt; margin-top:12pt; } .cover .e{ font-size:7.5pt; letter-spacing:.14em; text-transform:uppercase; margin-top:14pt; color:var(--gold); font-weight:700; }
"""
fonts = open('compose-affiche.py', encoding='utf-8').read()
FONTFACES = '\n'.join(re.findall(r"@font-face\{[^}]*\}", fonts))
body = ''.join(str(s) for s in sp.find_all('section'))
cover = ('<div class="cover"><div class="t">Barcelona,<br>Without<br>the Traps.</div>'
         '<div class="s">The decision manual for your first Barcelona trip.</div>'
         '<div class="e">Phone edition · same book, one column · the Field Sheet at the end</div></div>')
html = f'<!DOCTYPE html><html lang="en-US"><head><meta charset="utf-8"><title>Barcelona, Without the Traps. — phone edition</title><style>{FONTFACES}{CSS}</style></head><body>{cover}{body}</body></html>'
html = us_house(brunner_set(html))
# every provenance glyph in the marks font (a fallback face embeds as Type3)
html = re.sub(r'(?<!class="mk">)([●◇▲◆◈])', r'<span class="mk">\1</span>', html.split('</style>',1)[1]) and (html.split('</style>',1)[0] + '</style>' + re.sub(r'(?<!class="mk">)([●◇▲◆◈])', r'<span class="mk">\1</span>', html.split('</style>',1)[1]))
open('phone.html', 'w', encoding='utf-8').write(html)

OUT = 'Barcelona-Without-the-Traps-phone.pdf'
with sync_playwright() as p:
    b = p.chromium.launch(args=['--no-sandbox', '--font-render-hinting=none'])
    pg = b.new_page(); pg.goto('file://' + os.path.join(HERE, 'phone.html'), wait_until='load')
    pg.evaluate('document.fonts.ready')
    pg.pdf(path=OUT, prefer_css_page_size=True, print_background=True, display_header_footer=True,
           header_template='<span></span>',
           footer_template='<div style="width:100%;font-family:Helvetica,Arial,sans-serif;font-size:7px;color:#6B7773;padding:0 0.24in;display:flex;justify-content:space-between"><span>Barcelona, Without the Traps.</span><span class="pageNumber"></span></div>')
    b.close()
# bookmarks: each chapter's h1, found on its page
d = pymupdf.open(OUT); toc = [[1, 'Cover', 1]]
titles = [(s.get('id'), s.find('h1').get_text(' ', strip=True)) for s in sp.find_all('section') if s.find('h1')]
start = 0
for sid, t in titles:
    for i in range(start, d.page_count):
        if t[:24] in d[i].get_text().replace('\n', ' '):
            toc.append([2 if re.match(r'd0\d$', sid or '') else 1, t, i + 1]); start = i; break
d.set_toc(toc); d.save(OUT + '.tmp', garbage=3, deflate=True); d.close(); os.replace(OUT + '.tmp', OUT)
print('phone edition:', pymupdf.open(OUT).page_count, 'pages,', len(toc), 'bookmarks,', os.path.getsize(OUT) // 1024, 'KB')
