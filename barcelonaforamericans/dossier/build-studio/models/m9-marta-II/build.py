# -*- coding: utf-8 -*-
"""MARTA II — L'Affiche, second season. Each poster draws its verdict instead of only
writing it. The composition comes from the call: the Eixample's chamfered blocks, the
sawn mountain, the dinner clock, two full squares and one empty. Two inks overprint like
a screenprint (multiply), photographs go duotone, type is set to the scale of the sheet
and allowed to leave it. The words are the book's; the drawn labels restate the ledger.
"""
import sys, os, json, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import esc, PAGE, MARKS, FONTS, IMG, write

D = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'decisions.json'), encoding='utf-8'))
RED, GOLD, INK, PAPER, GREY = '#A23520', '#E0A828', '#17201C', '#F4F2EC', '#6B7773'
W, H = 816, 1056

CSS = PAGE + MARKS + '''
@font-face{font-family:'Archivo';src:url('%(F)sArchivo.ttf');font-weight:100 900;font-stretch:62%% 125%%;}
@page{ margin:0; @top-left{content:none} @top-right{content:none} @bottom-left{content:none} @bottom-center{content:none} @bottom-right{content:none} }
html,body{ background:#F4F2EC; margin:0; } .pagedjs_sheet{ background:#F4F2EC; }
body{ font-family:'Archivo'; color:#17201C; }
.sh{ width:816px; height:1056px; position:relative; overflow:hidden; break-after:page; box-sizing:border-box; }
.sh.red{ background:#A23520; color:#F4F2EC; } .sh.gold{ background:#E0A828; color:#17201C; } .sh.paper{ background:#F4F2EC; } .sh.ink{ background:#17201C; color:#F4F2EC; }
.sh svg.bg{ position:absolute; inset:0; width:816px; height:1056px; }
.slug{ position:absolute; top:52px; left:82px; right:82px; display:flex; justify-content:space-between; font-size:9px; font-weight:600; letter-spacing:.22em; text-transform:uppercase; z-index:3; }
.g{ position:absolute; font-weight:800; line-height:.78; letter-spacing:-.05em; z-index:2; white-space:nowrap; }
.mult{ mix-blend-mode:multiply; }
.gloss{ position:absolute; font-size:13px; font-weight:600; letter-spacing:.14em; text-transform:uppercase; line-height:18px; z-index:3; }
.foot{ position:absolute; left:82px; right:82px; bottom:58px; display:grid; grid-template-columns:1fr 290px; column-gap:40px; align-items:end; z-index:3; }
.foot .big{ font-size:28px; line-height:31px; font-weight:700; letter-spacing:-.02em; font-stretch:92%%; }
.foot p{ margin:0; font-size:11.5px; line-height:16px; }
.red .foot p{ color:#F8E9E3; }
.lab{ font-family:'Archivo'; font-weight:700; letter-spacing:.14em; text-transform:uppercase; }
.duo{ position:absolute; inset:0 0 auto 0; height:760px; overflow:hidden; }
.duo img{ width:100%%; height:100%%; object-fit:cover; filter:grayscale(1) contrast(1.15) brightness(1.3); display:block; }
.duo .tone{ position:absolute; inset:0; mix-blend-mode:multiply; }
.duo .lift{ position:absolute; inset:0; mix-blend-mode:screen; }
.tail{ position:absolute; left:82px; right:82px; top:792px; display:grid; grid-template-columns:340px 1fr; column-gap:48px; font-size:11px; line-height:17px; }
.tail .cap{ font-size:9px; line-height:13px; font-weight:600; letter-spacing:.06em; text-transform:uppercase; color:#6B7773; margin-bottom:8px; }
''' % {'F': FONTS}


def foot(sid):
    d = D[sid]
    return f'<div class="foot verdict"><div class="big">{esc(d["strong"])}</div><p>{esc(d["rest"])}</p></div>'


def slug(sid, extra=''):
    d = D[sid]
    return f'<div class="slug"{extra}><span>{esc(d["kicker"])}</span><span>{esc(d["title"])}</span></div>'


def octagon(cx, cy, s, c):
    """An Eixample block: a square of side s with its corners cut (the xamfrà), c = cut."""
    h = s / 2
    pts = [(cx - h + c, cy - h), (cx + h - c, cy - h), (cx + h, cy - h + c), (cx + h, cy + h - c),
           (cx + h - c, cy + h), (cx - h + c, cy + h), (cx - h, cy + h - c), (cx - h, cy - h + c)]
    return ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)


def _clip(poly, x0, y0, x1, y1):
    """Sutherland–Hodgman: the polygon cut to the sheet, so nothing is drawn past the trim."""
    def cut(pts, inside, inter):
        out = []
        for i, p in enumerate(pts):
            q = pts[i - 1]
            if inside(p):
                if not inside(q): out.append(inter(q, p))
                out.append(p)
            elif inside(q): out.append(inter(q, p))
        return out
    def ix(xc):
        return lambda a, b: (xc, a[1] + (b[1] - a[1]) * (xc - a[0]) / (b[0] - a[0]))
    def iy(yc):
        return lambda a, b: (a[0] + (b[0] - a[0]) * (yc - a[1]) / (b[1] - a[1]), yc)
    for inside, inter in ((lambda p: p[0] >= x0, ix(x0)), (lambda p: p[0] <= x1, ix(x1)),
                          (lambda p: p[1] >= y0, iy(y0)), (lambda p: p[1] <= y1, iy(y1))):
        poly = cut(poly, inside, inter)
        if not poly: return []
    return poly


def eixample_grid(fill, special=None, step=74, s=58, c=13, rot=-44, opacity=1, ground=None):
    """The district's grid, drawn once as a 288-dpi image of real polygons (the same geometry),
    with the special block on top as a vector shape inside the sheet.
    Why an image: a vector grid makes Paged.js split the poster inside the drawing; an SVG
    <pattern> renders at another scale in some PDF viewers (owner, 2026-10-25: oversized
    blocks beside a right-sized gold one). An image is the same in every viewer."""
    from PIL import Image, ImageDraw
    a = math.radians(rot); ca, sa = math.cos(a), math.sin(a)
    def tf(x, y):
        x, y = x - 400, y - 560
        return 408 + x * ca - y * sa, 528 + x * sa + y * ca
    K = 3   # 96 px → 288 dpi
    hexc = lambda h: tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))
    im = Image.new('RGB', (W * K, H * K), hexc(ground or '#000000'))
    dr = ImageDraw.Draw(im)
    for i in range(-12, 24):
        for j in range(-12, 26):
            if special and (i, j) == special[0]: continue
            pts = [tuple(map(float, p.split(','))) for p in octagon(i * step, j * step, s, c).split()]
            dr.polygon([(x * K, y * K) for x, y in (tf(*p) for p in pts)], fill=hexc(fill))
    name = f'm2-grid-{fill[1:]}-{step}.png'
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'img')
    im.save(os.path.join(out_dir, name), optimize=True)
    svg = f'<image href="{IMG}{name}" x="0" y="0" width="{W}" height="{H}" preserveAspectRatio="none"/>'
    if special:
        (i, j), col = special
        pts = [tuple(map(float, p.split(','))) for p in octagon(i * step, j * step, s, c).split()]
        svg += f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in (tf(*p) for p in pts))}" fill="{col}"/>'
    return svg


# ── cover ────────────────────────────────────────────────────────────────────
cover = f'''<div class="sh red">
<svg class="bg" viewBox="0 0 {W} {H}">{eixample_grid('#972F1C', special=((4, 6), GOLD), step=132, s=112, c=26, ground=RED)}</svg>
<div class="slug"><span>Barcelona for Americans</span><span>A decision manual · 2026</span></div>
<div class="g" style="left:72px;top:150px;font-size:148px;font-stretch:76%;color:{PAPER}">BARCELONA,<br>WITHOUT<br>THE TRAPS.</div>
<div class="gloss" style="left:82px;bottom:120px;width:360px;letter-spacing:.08em;text-transform:none;font-size:15px;line-height:21px;font-weight:500">How the city separates visitors from their money and their days — and the handful of calls that defend against it.</div>
<div class="gloss" style="left:82px;bottom:58px;font-size:9px">68 pages · 7 decisions · the Field Sheet</div>
<div class="gloss" style="right:82px;bottom:58px;font-size:9px;text-align:right">One block of the grid is yours.<br>Decision 01 says which.</div>
</div>'''

# ── d01 EIXAMPLE — the word set over the district's own grid, one block red ───────
d01 = f'''<div class="sh gold">
<svg class="bg" viewBox="0 0 {W} {H}">{eixample_grid('#CC9822', special=((5, 7), RED), step=96, s=78, c=18, ground=GOLD)}</svg>
<div class="lab" style="position:absolute;left:592px;top:547px;font-size:10px;z-index:3;color:{INK}">← YOUR BLOCK</div>
{slug('d01')}
<div class="g mult" style="left:60px;top:190px;font-size:212px;font-stretch:62%;color:{INK}">EIXAMPLE</div>
<div class="gloss" style="left:82px;top:375px;width:420px">First trip, no special agenda —<br>and it isn't close.</div>
<div class="sh-shade" style="position:absolute;left:0;right:0;bottom:0;height:300px;background:{GOLD};z-index:1"></div>
{foot('d01')}
</div>'''

# ── d02 HOTEL — a facade: every window a hotel room, one window an apartment with its number ──
win = []
cols, rows_ = 9, 6
for r in range(rows_):
    for c_ in range(cols):
        x, y = 82 + c_ * 74, 360 + r * 64
        if (r, c_) == (3, 6):
            win.append(f'<rect x="{x}" y="{y}" width="44" height="40" fill="none" stroke="{PAPER}" stroke-width="2"/>'
                       f'<text x="{x+22}" y="{y+25}" font-family="Archivo" font-size="9" font-weight="800" letter-spacing=".8" fill="{PAPER}" text-anchor="middle">HUTB</text>')
        else:
            lit = (r * 7 + c_ * 3) % 5 != 0
            win.append(f'<rect x="{x}" y="{y}" width="44" height="40" fill="{GOLD if lit else "#7E2918"}"/>')
d02 = f'''<div class="sh red">
<svg class="bg" viewBox="0 0 {W} {H}">{"".join(win)}
  <line x1="82" y1="742" x2="734" y2="742" stroke="{PAPER}" stroke-width="3"/>
  <text x="548" y="764" font-family="Archivo" font-size="9" font-weight="700" letter-spacing="1.3" fill="{PAPER}" text-anchor="middle">↑ THE ONLY APARTMENT</text><text x="548" y="777" font-family="Archivo" font-size="9" font-weight="700" letter-spacing="1.3" fill="{PAPER}" text-anchor="middle">THE ONE WITH A NUMBER</text></svg>
{slug('d02')}
<div class="g" style="left:62px;top:96px;font-size:262px;font-stretch:84%;color:{PAPER}">HOTEL</div>
<div class="gloss" style="left:82px;top:300px;width:520px">Or an apart-hotel. The apartment only with a HUTB number.</div>
{foot('d02')}
</div>'''

# ── d03 4 — the numeral crossed by its four gates, overprinted ──────────────────
moves = ['BED TAX — BUDGET IT', 'AIRPORT TICKET — BOTH WAYS', 'EUROS — ALWAYS', 'A BANK MACHINE — NOT A TOURIST ONE']
bands = ''.join(f'<div class="mult" style="position:absolute;left:0;right:0;top:{250 + i*118}px;height:46px;background:{RED};z-index:2"></div>'
                f'<div class="lab" style="position:absolute;left:{470 if i % 2 == 0 else 82}px;top:{266 + i*118}px;font-size:12px;color:{PAPER};z-index:4">{i+1} · {m}</div>'
                for i, m in enumerate(moves))
d03 = f'''<div class="sh gold">
{slug('d03')}
<div class="g" style="left:40px;top:120px;font-size:760px;font-stretch:110%;color:{INK};z-index:1">4</div>
{bands}
<div class="gloss" style="left:470px;top:150px;width:260px;font-size:11px;line-height:16px">Four gates, four moves. Five minutes to learn; they defend the week.</div>
{foot('d03')}
</div>'''

# ── d05 3 — three anchors, solid; everything else floats ───────────────────────
anch = [(250, 400, 118, '1', 'SAGRADA FAMÍLIA', 'A MORNING SLOT'), (520, 520, 96, '2', 'ARRIVAL', 'NOTHING TIMED'), (300, 690, 86, '3', 'THE DAY TRIP', 'A FULL CLEAR DAY')]
circ = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{PAPER}"/><text x="{x}" y="{y+18}" font-family="Archivo" font-size="{r*0.9:.0f}" font-weight="800" fill="{RED}" text-anchor="middle">{n}</text>'
               f'<text x="{x + r + 14}" y="{y - 4}" font-family="Archivo" font-size="12" font-weight="800" letter-spacing="1.6" fill="{PAPER}">{a}</text>'
               f'<text x="{x + r + 14}" y="{y + 14}" font-family="Archivo" font-size="10" font-weight="600" letter-spacing="1.4" fill="#F1C9BC">{b}</text>'
               for x, y, r, n, a, b in anch)
floats = [(640, 330, 26, 'THE BEACH'), (690, 430, 12, ''), (150, 560, 16, ''), (640, 700, 20, 'TAPAS'), (180, 300, 10, ''), (720, 610, 9, ''), (470, 360, 11, ''), (560, 790, 14, 'A MUSEUM')]
fl = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{PAPER}" stroke-width="2"/>' + (f'<text x="{x}" y="{y + r + 16}" font-family="Archivo" font-size="9" font-weight="700" letter-spacing="1.3" fill="{PAPER}" text-anchor="middle">{t}</text>' if t else '') for x, y, r, t in floats)
d05 = f'''<div class="sh red">
<svg class="bg" style="z-index:1" viewBox="0 0 {W} {H}">{fl}{circ}</svg>
{slug('d05')}
<div class="g" style="right:-30px;top:170px;font-size:820px;font-stretch:110%;color:#8E2C1A;z-index:0">3</div>
<div class="gloss" style="left:82px;top:120px;width:330px">Three anchors. The rest floats.<br>Arrival day holds nothing timed.</div>
{foot('d05')}
</div>'''

# ── d06 2+1 — two full squares, one empty, the rest dots from the street ─────────
sq = [(82, 'SAGRADA FAMÍLIA', 'THE INTERIOR', True), (282, 'PARK GÜELL', 'THE MONUMENTAL ZONE', True), (554, 'ONE HOUSE', 'BATLLÓ OR LA PEDRERA', False)]
sqs = ''.join((f'<rect x="{x}" y="340" width="180" height="180" fill="{PAPER}"/>' if full else
               f'<rect x="{x+1.5}" y="341.5" width="177" height="177" fill="none" stroke="{GOLD}" stroke-width="3"/>') +
              f'<text x="{x}" y="560" font-family="Archivo" font-size="12" font-weight="800" letter-spacing="1.5" fill="{PAPER}">{a}</text>'
              f'<text x="{x}" y="576" font-family="Archivo" font-size="10" font-weight="600" letter-spacing="1.3" fill="#F1C9BC">{b}</text>' for x, a, b, full in sq)
street = ''.join(f'<circle cx="{82 + i*22}" cy="640" r="5" fill="none" stroke="{PAPER}" stroke-width="1.5"/>' for i in range(14))
sqimg = (f'<div style="position:absolute;left:82px;top:340px;width:180px;height:180px;overflow:hidden;z-index:1"><img src="{IMG}A04.jpg" style="width:100%;height:100%;object-fit:cover;object-position:50% 30%;filter:grayscale(1) contrast(1.2) brightness(1.05)"></div>'
         f'<div style="position:absolute;left:282px;top:340px;width:180px;height:180px;overflow:hidden;z-index:1"><img src="{IMG}m2-guell.jpg" style="width:100%;height:100%;object-fit:cover;object-position:50% 50%;filter:grayscale(1) contrast(1.2) brightness(1.05)"></div>'
         f'<div style="position:absolute;left:566px;top:352px;width:156px;height:156px;overflow:hidden;z-index:1"><img src="{IMG}m2-batllo.jpg" style="width:100%;height:100%;object-fit:cover;filter:grayscale(1) contrast(1.1) brightness(1.15)"><div style="position:absolute;inset:0;background:{GOLD};mix-blend-mode:multiply"></div><div style="position:absolute;inset:0;background:{RED};opacity:.35"></div></div>')
d06 = f'''<div class="sh red">
<svg class="bg" viewBox="0 0 {W} {H}">{sqs}
  <text x="508" y="462" font-family="Archivo" font-size="80" font-weight="800" fill="{GOLD}" text-anchor="middle">+</text>
  {street}<text x="400" y="644" font-family="Archivo" font-size="9" font-weight="700" letter-spacing="1.3" fill="{PAPER}">THE REST — FROM THE STREET, FREE</text></svg>
{sqimg}
{slug('d06')}
<div class="g" style="left:66px;top:96px;font-size:210px;font-stretch:118%;color:{PAPER}">2+1</div>
{foot('d06')}
</div>'''

# ── d07 MONTSERRAT — the sawn mountain, the word on its ridge ────────────────────
pk = [(0, 1056), (0, 600), (40, 590), (62, 520), (86, 540), (104, 470), (128, 500), (150, 430), (170, 455), (196, 380), (214, 410),
      (240, 350), (258, 372), (282, 318), (300, 352), (326, 300), (344, 330), (368, 286), (390, 322), (412, 296), (434, 340), (458, 312),
      (480, 360), (504, 330), (528, 392), (552, 360), (576, 420), (600, 396), (628, 460), (652, 430), (680, 500), (706, 480), (736, 540),
      (770, 520), (816, 590), (816, 1056)]
mtn = ' '.join(f'{x},{y + 120}' for x, y in pk)
d07 = f'''<div class="sh gold">
<svg class="bg" viewBox="0 0 {W} {H}"><polygon points="{mtn}" fill="{INK}"/>
  <circle cx="404" cy="600" r="9" fill="{RED}"/><text x="420" y="604" font-family="Archivo" font-size="9" font-weight="700" letter-spacing="1.3" fill="{PAPER}">THE MONASTERY · ONE HOUR BY TRAIN</text></svg>
{slug('d07')}
<div class="g" style="left:60px;top:150px;font-size:150px;font-stretch:66%;color:{INK}">MONTSERRAT</div>
<div class="gloss" style="left:82px;top:282px;width:400px">It out-memories the city, and has no substitute within reach.</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:250px;background:{INK};z-index:1"></div>
<div class="foot verdict" style="color:{PAPER}"><div class="big">{esc(D['d07']['strong'])}</div><p style="color:#C9CFCC">{esc(D['d07']['rest'])}</p></div>
</div>'''

# ── d08 20:30 — the dinner clock: the American hour empty, the Spanish hour full ───
cx, cy, R = 408, 360, 180
def arc(a0, a1, r, w, col):
    def pt(h):
        a = math.radians(h / 24 * 360 - 90); return cx + r * math.cos(a), cy + r * math.sin(a)
    (x0, y0), (x1, y1) = pt(a0), pt(a1); large = 1 if (a1 - a0) / 24 * 360 > 180 else 0
    return f'<path d="M{x0:.1f},{y0:.1f} A{r},{r} 0 {large} 1 {x1:.1f},{y1:.1f}" fill="none" stroke="{col}" stroke-width="{w}"/>'
ticks = ''.join(f'<line x1="{cx + (R-14)*math.cos(math.radians(h*15-90)):.1f}" y1="{cy + (R-14)*math.sin(math.radians(h*15-90)):.1f}" x2="{cx + R*math.cos(math.radians(h*15-90)):.1f}" y2="{cy + R*math.sin(math.radians(h*15-90)):.1f}" stroke="{PAPER}" stroke-width="{3 if h % 6 == 0 else 1.2}"/>' for h in range(24))
nums = ''.join(f'<text x="{cx + (R+22)*math.cos(math.radians(h*15-90)):.1f}" y="{cy + (R+22)*math.sin(math.radians(h*15-90)) + 4:.1f}" font-family="Archivo" font-size="11" font-weight="700" fill="{PAPER}" text-anchor="middle">{h:02d}</text>' for h in (0, 6, 12, 18))
ha = math.radians(20.5 * 15 - 90)
d08 = f'''<div class="sh red">
<svg class="bg" viewBox="0 0 {W} {H}">
  <circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{PAPER}" stroke-width="1.2"/>{ticks}{nums}
  {arc(18, 19.5, R - 40, 30, '#C24A33')}{arc(20.5, 23.5, R - 40, 34, GOLD)}
  <text x="{cx - 72}" y="{cy + 46}" font-family="Archivo" font-size="9" font-weight="700" letter-spacing="1.2" fill="#F1C9BC" text-anchor="middle">18:00 · EMPTY ROOMS</text>
  <text x="{cx + (R+44)*math.cos(math.radians(22.4*15-90)):.1f}" y="{cy + (R+44)*math.sin(math.radians(22.4*15-90)):.1f}" font-family="Archivo" font-size="9" font-weight="700" letter-spacing="1.2" fill="{GOLD}" text-anchor="middle">THE RIGHT ROOMS</text>
  <line x1="{cx}" y1="{cy}" x2="{cx + (R-6)*math.cos(ha):.1f}" y2="{cy + (R-6)*math.sin(ha):.1f}" stroke="{PAPER}" stroke-width="5" stroke-linecap="square"/>
  <circle cx="{cx}" cy="{cy}" r="8" fill="{PAPER}"/></svg>
{slug('d08')}
<div class="g" style="left:60px;top:592px;font-size:150px;font-stretch:96%;color:{PAPER}">20:30</div>
<div class="gloss" style="left:82px;top:100px;width:300px;font-size:11px;line-height:16px">Dinner on Spanish time — the rule that puts you in the right rooms.</div>
{foot('d08')}
</div>'''

# ── a duotone photograph page (d06) — the frame in the book's two inks ───────────
duo = f'''<div class="sh paper">
<div class="duo"><img src="{IMG}A04.jpg" style="object-position:50% 40%"><div class="tone" style="background:{RED}"></div><div class="lift" style="background:#3a140b"></div></div>
<div class="g" style="left:52px;top:560px;font-size:250px;font-stretch:118%;color:{GOLD};z-index:2">2+1</div>
<div class="tail"><div><div class="cap">Sagrada Família, the nave — the one interior worth its queue</div>
<p style="margin:0">Duotone: the photograph printed in the book's two inks, ink and red, so the frame belongs to the poster it follows instead of arriving from a stock library.</p></div>
<div style="border-top:3px solid {RED};padding-top:8px;font-size:10px;line-height:14px"><span class="lab" style="color:{RED};font-size:9px;display:block;margin-bottom:5px">Specimen note</span>The verdict's numeral overprints the image in gold; where the gold crosses the red it darkens, as two screen inks do.</div></div>
</div>'''

POSTERS = {'cover': cover, 'd01': d01, 'd02': d02, 'd03': d03, 'd05': d05, 'd06': d06, 'd07': d07, 'd08': d08}
POSTER_CSS = CSS
html = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Marta II</title><style>{CSS}</style></head><body>{cover}{d01}{d02}{d03}{d05}{d06}{d07}{d08}{duo}</body></html>'
if __name__ == '__main__':
    write(html)
