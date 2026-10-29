# -*- coding: utf-8 -*-
"""MARTA II on ROME — L'Affiche, second season, tried on *Rome, Solved.*

Same law as the Barcelona specimen: the poster's composition is made from the call.
Rome's sign is not Barcelona's octagon: it is the SAMPIETRINO, the small square basalt
stone laid in fans (coda di pavone) across the whole historic centre — the walkable core
under your feet, which is the book's thesis. La Tavola's palette: wax red, plate gilt,
foxed paper, iron-gall ink. The words are the book's (verdicts, ledgers); drawn labels
restate the ledger and add no fact.
"""
import sys, os, json, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
from common import esc, PAGE, MARKS, FONTS, write

D = json.load(open(os.path.join(HERE, 'decisions.json'), encoding='utf-8'))
IMG = '../../img/'
RED, GOLD, INK, PAPER, SEPIA = '#8A3324', '#C9A94A', '#2B241A', '#EFE4CC', '#6A5C42'
RED2, GOLD2, PINK = '#6F281B', '#B3923B', '#EBCDBF'
W, H = 816, 1056

CSS = PAGE + MARKS + '''
@font-face{font-family:'Archivo';src:url('%(F)sArchivo.ttf');font-weight:100 900;font-stretch:62%% 125%%;}
@page{ margin:0; @top-left{content:none} @top-right{content:none} @bottom-left{content:none} @bottom-center{content:none} @bottom-right{content:none} }
html,body{ background:#EFE4CC; margin:0; } .pagedjs_sheet{ background:#EFE4CC; }
body{ font-family:'Archivo'; color:#2B241A; }
.sh{ width:816px; height:1056px; position:relative; overflow:hidden; break-after:page; box-sizing:border-box; }
.sh.red{ background:#8A3324; color:#EFE4CC; } .sh.gold{ background:#C9A94A; color:#2B241A; } .sh.paper{ background:#EFE4CC; }
.sh svg.bg{ position:absolute; inset:0; width:816px; height:1056px; }
.slug{ position:absolute; top:52px; left:82px; right:82px; display:flex; justify-content:space-between; font-size:9px; font-weight:600; letter-spacing:.22em; text-transform:uppercase; z-index:3; }
.g{ position:absolute; font-weight:800; line-height:.78; letter-spacing:-.05em; z-index:2; white-space:nowrap; }
.gloss{ position:absolute; font-size:12px; font-weight:600; letter-spacing:.14em; text-transform:uppercase; line-height:17px; z-index:3; }
.foot{ position:absolute; left:82px; right:82px; bottom:56px; display:grid; grid-template-columns:1fr 300px; column-gap:40px; align-items:end; z-index:3; }
.foot .big{ font-size:27px; line-height:30px; font-weight:700; letter-spacing:-.02em; font-stretch:92%%; }
.foot p{ margin:0; font-size:10.5px; line-height:15px; }
.red .foot p{ color:#F3E3D6; }
.duo{ position:absolute; inset:0 0 auto 0; height:760px; overflow:hidden; }
.duo img{ width:100%%; height:100%%; object-fit:cover; filter:grayscale(1) contrast(1.15) brightness(1.3); display:block; }
.duo .tone{ position:absolute; inset:0; mix-blend-mode:multiply; } .duo .lift{ position:absolute; inset:0; mix-blend-mode:screen; }
.tail{ position:absolute; left:82px; right:82px; top:792px; display:grid; grid-template-columns:340px 1fr; column-gap:48px; font-size:11px; line-height:17px; }
.tail .cap{ font-size:9px; line-height:13px; font-weight:600; letter-spacing:.06em; text-transform:uppercase; color:#6A5C42; margin-bottom:8px; }
''' % {'F': FONTS}


def T(x, y, s, col, size=9, w=700, ls=1.3, anchor='start'):
    return f'<text x="{x:.1f}" y="{y:.1f}" font-family="Archivo" font-size="{size}" font-weight="{w}" letter-spacing="{ls}" fill="{col}" text-anchor="{anchor}">{esc(s)}</text>'


def slug(sid):
    d = D[sid]
    return f'<div class="slug"><span>{esc(d["kicker"])}</span><span>{esc(d["title"])}</span></div>'


def foot(sid, big_col=None, p_col=None):
    d = D[sid]
    bs = f' style="color:{big_col}"' if big_col else ''
    ps = f' style="color:{p_col}"' if p_col else ''
    # anchored from the TOP at a height estimated from the text: a bottom-anchored foot is filled line
    # by line by Paged.js, which splits a long paragraph onto a blank next sheet (Rome, 2026-10-25)
    est = max(math.ceil(len(d['rest']) / 50) * 15, math.ceil(len(d['strong']) / 24) * 30)
    top = 1055 - 56 - est - 6
    return f'<div class="foot verdict" style="top:{top}px;bottom:auto"><div class="big"{bs}>{esc(d["strong"])}</div><p{ps}>{esc(d["rest"])}</p></div>'


def sampietrini(cx, cy, R, col, stone=11, gap=2.4, clip=None, rows_from=1, special=None):
    """Fans of small square stones (coda di pavone): concentric arcs, each stone set
    tangent to its arc. One fan per call; tile by calling at several centres."""
    out = []
    pitch = stone + gap
    k = rows_from
    while k * pitch <= R:
        r = k * pitch
        n = max(1, int(2 * math.pi * r / pitch))
        for i in range(n):
            a = 2 * math.pi * i / n
            x, y = cx + r * math.cos(a), cy + r * math.sin(a)
            fill = special[1] if special and (k, i) == special[0] else col
            out.append(f'<rect x="{x - stone/2:.1f}" y="{y - stone/2:.1f}" width="{stone}" height="{stone}" fill="{fill}" transform="rotate({math.degrees(a):.1f} {x:.1f} {y:.1f})"/>')
        k += 1
    return ''.join(out)


def peacock_png(col, ground, stone=12, R=150):
    """The street pattern drawn once as a 288-dpi image (the same fans of stones): a vector field
    of thousands of stones past the trim makes Paged.js split the poster, and an image shows the
    same in every PDF viewer (Barcelona, 2026-10-25)."""
    from PIL import Image, ImageDraw
    K = 3; hexc = lambda h: tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))
    im = Image.new('RGB', (W * K, H * K), hexc(ground)); dr = ImageDraw.Draw(im)
    pitch = stone + 2.4; step_x, step_y = R * 1.5, R * 0.9
    for row in range(-1, int(H / step_y) + 2):
        for colm in range(-1, int(W / step_x) + 2):
            cx = colm * step_x + (step_x / 2 if row % 2 else 0); cy = row * step_y
            k = 1
            while k * pitch <= R:
                r = k * pitch; n = max(1, int(2 * math.pi * r / pitch))
                for i in range(n):
                    a = 2 * math.pi * i / n; x, y = cx + r * math.cos(a), cy + r * math.sin(a)
                    ca, sa = math.cos(a), math.sin(a); h = stone / 2
                    pts = [(x + (dx * ca - dy * sa), y + (dx * sa + dy * ca)) for dx, dy in ((-h, -h), (h, -h), (h, h), (-h, h))]
                    dr.polygon([(px * K, py * K) for px, py in pts], fill=hexc(col))
                k += 1
    name = f'm2-peacock-{col[1:]}-{stone}.png'
    im.save(os.path.join(HERE, '..', '..', 'img', name), optimize=True)
    return f'<image href="{IMG}{name}" x="0" y="0" width="{W}" height="{H}" preserveAspectRatio="none"/>'


def peacock(col, stone=12, R=150, special=None):
    """The street pattern: overlapping fans in offset rows across the whole sheet."""
    out = []
    step_x, step_y = R * 1.5, R * 0.9
    for row in range(-1, int(H / step_y) + 2):
        for colm in range(-1, int(W / step_x) + 2):
            cx = colm * step_x + (step_x / 2 if row % 2 else 0)
            cy = row * step_y
            sp = special if special and special[0] == (row, colm) else None
            out.append(f'<g>{sampietrini(cx, cy, R, col, stone, special=(sp[1], sp[2]) if sp else None)}</g>')
    return ''.join(out)


# ── cover ──────────────────────────────────────────────────────────────────────
cover = f'''<div class="sh red">
<svg class="bg" viewBox="0 0 {W} {H}">{peacock_png(RED2, RED, stone=18, R=230)}
  <rect x="566" y="640" width="26" height="26" fill="{GOLD}" transform="rotate(18 579 653)"/></svg>
<div class="slug"><span>Rome for Americans</span><span>A decision manual · 2026</span></div>
<div class="g" style="left:70px;top:150px;font-size:212px;font-stretch:80%;color:{PAPER}">ROME,<br>SOLVED.</div>
<div class="gloss" style="left:82px;bottom:118px;width:380px;letter-spacing:.06em;text-transform:none;font-size:15px;line-height:21px;font-weight:500">Which of it is actually worth your time — and which is the photo everyone regrets. The historic core is a kilometre and a half across. You walk it.</div>
<div class="gloss" style="left:82px;bottom:58px;font-size:9px">9 decisions · the Field Sheet</div>
<div class="gloss" style="right:82px;bottom:58px;font-size:9px;text-align:right">The centre is paved in sampietrini.<br>One stone is where you sleep.</div>
</div>'''

# ── d01 13′ — the cobbled core, and the five bases on their walk-time rings ───────
cx, cy, k = 300, 560, 8.2           # 1 minute on foot = 8.2 px
bases = [('CENTRO STORICO', 13, 200, True), ('MONTI', 13, 330, True), ('TRASTEVERE', 20, 150, False), ('NEAR TERMINI', 28, 10, False), ('PRATI', 38, 250, False)]
rings = ''.join(f'<circle cx="{cx}" cy="{cy}" r="{m*k}" fill="none" stroke="{INK}" stroke-width="1" stroke-dasharray="2 4"/>' + T(cx + 4, cy - m * k - 5, f"{m}′", INK, 9, 700) for m in (10, 20, 30, 40))
dots = ''
for name, m, ang, pick in bases:
    a = math.radians(ang); x, y = cx + m * k * math.cos(a), cy + m * k * math.sin(a)
    dots += (f'<rect x="{x-9}" y="{y-9}" width="18" height="18" fill="{RED}"/>' if pick else f'<circle cx="{x}" cy="{y}" r="8" fill="none" stroke="{INK}" stroke-width="2.5"/>')
    lx = x + 16 if math.cos(a) >= -0.2 else x - 16
    dots += T(lx, y - 2, name, INK, 10, 800, 1.4, 'start' if math.cos(a) >= -0.2 else 'end') + T(lx, y + 11, f"{m}′ TO THE CORE", RED if pick else SEPIA, 8.5, 700, 1.2, 'start' if math.cos(a) >= -0.2 else 'end')
d01 = f'''<div class="sh gold">
<svg class="bg" viewBox="0 0 {W} {H}">
  <clipPath id="core"><circle cx="{cx}" cy="{cy}" r="{13*k}"/></clipPath>
  <circle cx="{cx}" cy="{cy}" r="{13*k}" fill="{GOLD2}"/>
  <g clip-path="url(#core)">{sampietrini(cx, cy, 13*k, INK, stone=7, gap=2.2)}</g>
  {dots}
  {T(cx, cy + 13*k + 20, 'THE WALKABLE CORE', INK, 9, 800, 1.6, 'middle')}</svg>
{slug('d01')}
<div class="g" style="right:60px;top:110px;font-size:300px;font-stretch:110%;color:{INK}">13′</div>
<div class="gloss" style="right:82px;top:360px;width:300px;text-align:right">Minutes on foot to the centre, from the core. From Termini, twenty-eight.</div>
{foot('d01')}
</div>'''

# ── d02 TAP. — the contactless sign, the pass left unbought ──────────────────────
waves = ''.join(f'<path d="M{470 + i*58},{330} A{120 + i*58},{120 + i*58} 0 0 1 {470 + i*58},{590}" fill="none" stroke="{PAPER}" stroke-width="22" stroke-linecap="butt"/>' for i in range(3))
d02 = f'''<div class="sh red">
<svg class="bg" viewBox="0 0 {W} {H}">
  <rect x="82" y="330" width="330" height="208" rx="16" fill="{PAPER}"/>
  <rect x="112" y="380" width="54" height="40" rx="6" fill="{GOLD}"/>
  {T(112, 510, 'TAP A CARD', RED, 12, 800, 1.8)}
  {waves}
  <rect x="82" y="610" width="200" height="120" rx="10" fill="none" stroke="{GOLD}" stroke-width="2" stroke-dasharray="6 5"/>
  {T(98, 650, 'ROMA PASS', GOLD, 11, 800, 1.6)}{T(98, 668, 'SKIP IT', GOLD, 9, 700, 1.4)}
  {T(300, 676, '← LET THE CAP WORK', PAPER, 10, 700, 1.5)}</svg>
{slug('d02')}
<div class="g" style="left:62px;top:100px;font-size:230px;font-stretch:100%;color:{PAPER}">TAP.</div>
{foot('d02')}
</div>'''

# ── d03 €55 — one taxi, four seats, one price ─────────────────────────────────
seats = ''.join(f'<rect x="{110 + i*84}" y="420" width="62" height="62" fill="{INK}"/>' for i in range(4))
d03 = f'''<div class="sh gold">
<svg class="bg" viewBox="0 0 {W} {H}">
  <rect x="82" y="390" width="372" height="122" fill="none" stroke="{INK}" stroke-width="3"/>{seats}
  {T(82, 540, 'FIXED-FARE OFFICIAL TAXI · DOOR TO DOOR', INK, 10, 800, 1.4)}{T(82, 556, '€55 FLAT, UP TO 4', RED, 10, 800, 1.4)}
  <rect x="510" y="420" width="62" height="62" fill="none" stroke="{INK}" stroke-width="3"/><rect x="594" y="420" width="62" height="62" fill="none" stroke="{INK}" stroke-width="3"/>
  <line x1="660" y1="451" x2="726" y2="451" stroke="{INK}" stroke-width="3" stroke-dasharray="5 5"/>
  {T(510, 540, 'LEONARDO EXPRESS', INK, 10, 800, 1.4)}{T(510, 556, '≈ €28 FOR TWO, PLUS THE ONWARD HOP', SEPIA, 9, 700, 1.2)}</svg>
{slug('d03')}
<div class="g" style="left:60px;top:100px;font-size:260px;font-stretch:104%;color:{INK}">€55</div>
<div class="gloss" style="left:82px;top:322px;width:520px">One taxi, four seats, one price.</div>
{foot('d03')}
</div>'''

# ── d04 ½ — the half-day: the Forum first, at opening, the arena after ────────────
hx, hy, hr = 408, 600, 250
def wedge(a0, a1, r, col):
    p0 = (hx + r * math.cos(math.radians(a0)), hy + r * math.sin(math.radians(a0)))
    p1 = (hx + r * math.cos(math.radians(a1)), hy + r * math.sin(math.radians(a1)))
    return f'<path d="M{hx},{hy} L{p0[0]:.1f},{p0[1]:.1f} A{r},{r} 0 0 1 {p1[0]:.1f},{p1[1]:.1f} Z" fill="{col}"/>'
d04 = f'''<div class="sh red">
<svg class="bg" viewBox="0 0 {W} {H}">
  {wedge(180, 270, hr, GOLD)}{wedge(270, 360, hr, PAPER)}
  <line x1="{hx-hr-30}" y1="{hy}" x2="{hx+hr+30}" y2="{hy}" stroke="{PAPER}" stroke-width="2"/>
  {T(hx - 128, hy - 70, 'FORUM + PALATINE', INK, 12, 800, 1.6, 'middle')}{T(hx - 128, hy - 54, 'FIRST, AT OPENING', INK, 9, 700, 1.3, 'middle')}
  {T(hx + 128, hy - 70, 'COLOSSEUM', RED, 12, 800, 1.6, 'middle')}{T(hx + 128, hy - 54, 'SHADE SAVED FOR THE ARENA', RED, 9, 700, 1.3, 'middle')}
  {T(hx - hr - 30, hy + 22, 'MORNING', PAPER, 9, 700, 1.4)}{T(hx + hr + 30, hy + 22, 'MIDDAY', PAPER, 9, 700, 1.4, 'end')}
  {T(hx, hy + 22, 'ONE 24-HOUR TICKET · NOT THE VATICAN THE SAME DAY', PINK, 9, 700, 1.3, 'middle')}</svg>
{slug('d04')}
<div class="g" style="left:62px;top:96px;font-size:250px;font-stretch:110%;color:{PAPER}">½</div>
<div class="gloss" style="left:300px;top:150px;width:420px">The ancient core gets its own half-day.</div>
{foot('d04')}
</div>'''

# ── d05 TWO LINES. — two queues; the ticket only touches one ───────────────────
q1 = ''.join(f'<circle cx="{82 + i*19}" cy="500" r="6" fill="{INK}"/>' for i in range(8))
q1 += f'<rect x="240" y="488" width="64" height="24" fill="{RED}"/>' + T(272, 504, 'TIMED', PAPER, 9, 800, 1.2, 'middle')
q2 = ''.join(f'<circle cx="{82 + i*19}" cy="640" r="6" fill="{INK}"/>' for i in range(39))
d05 = f'''<div class="sh gold">
<svg class="bg" viewBox="0 0 {W} {H}">{q1}{q2}
  {T(82, 470, '1 · THE TICKET LINE — BOOK OFFICIAL, SKIP IT', INK, 11, 800, 1.6)}
  {T(82, 610, '2 · THE SECURITY LINE — EVERYONE, TICKET OR NOT', INK, 11, 800, 1.6)}
  {T(82, 680, 'ST PETER’S: FREE ENTRY · SECURITY ONLY · PASSAGE-TOUR OR GO EARLY', SEPIA, 9, 700, 1.3)}
  {T(82, 540, 'A THIRD-PARTY “SKIP THE LINE” PREMIUM: USUALLY THE TIMED TICKET + A MARKUP', SEPIA, 9, 700, 1.3)}</svg>
{slug('d05')}
<div class="g" style="left:58px;top:110px;font-size:190px;font-stretch:96%;color:{INK}">TWO<br>LINES.</div>
{foot('d05')}
</div>'''

# ── d06 3 — the calendar: three squares go first ────────────────────────────────
cal = ''
for wk in range(6):
    for dy in range(7):
        x, y = 82 + dy * 52, 380 + wk * 52
        cal += f'<rect x="{x}" y="{y}" width="44" height="44" fill="none" stroke="{PAPER}" stroke-width="1.2"/>'
for (wk, dy, lab) in [(0, 2, 'VATICAN MUSEUMS'), (0, 4, 'BORGHESE'), (1, 1, 'COLOSSEUM UNDERGROUND')]:
    x, y = 82 + dy * 52, 380 + wk * 52
    cal += f'<rect x="{x}" y="{y}" width="44" height="44" fill="{GOLD}"/>'
labs = T(470, 400, 'WEEKS AHEAD — BOOK ON SALE', GOLD, 10, 800, 1.5) + T(470, 420, 'VATICAN MUSEUMS · BORGHESE · UNDERGROUND', PAPER, 9, 700, 1.3)
labs += T(470, 560, 'A DAY OR TWO — COLOSSEUM STANDARD, PANTHEON', PINK, 9, 700, 1.3) + T(470, 580, 'NOTHING — ST PETER’S, FREE', PINK, 9, 700, 1.3)
labs += f'<line x1="82" y1="702" x2="446" y2="702" stroke="{PAPER}" stroke-width="2"/>' + T(82, 720, 'SIX WEEKS OUT', PAPER, 9, 700, 1.3) + T(446, 720, 'YOUR DATES ARE FIRM →', PAPER, 9, 700, 1.3, 'end')
d06 = f'''<div class="sh red">
<svg class="bg" viewBox="0 0 {W} {H}">{cal}{labs}</svg>
{slug('d06')}
<div class="g" style="right:70px;top:96px;font-size:300px;font-stretch:110%;color:{GOLD}">3</div>
<div class="gloss" style="left:82px;top:140px;width:360px">Three sell out. Book them the moment your dates are firm; leave the rest to the trip week.</div>
{foot('d06')}
</div>'''

# ── d07 € — the reader's screen: euros, always ─────────────────────────────────
d07 = f'''<div class="sh gold">
<svg class="bg" viewBox="0 0 {W} {H}">
  <rect x="300" y="300" width="300" height="420" rx="28" fill="{INK}"/>
  <rect x="330" y="340" width="240" height="200" rx="6" fill="{PAPER}"/>
  {T(450, 380, 'PAY IN', INK, 11, 800, 2, 'middle')}
  <rect x="350" y="400" width="96" height="84" fill="{RED}"/>{T(398, 452, 'EUR', PAPER, 22, 800, 1, 'middle')}
  <rect x="456" y="402" width="94" height="80" fill="none" stroke="{INK}" stroke-width="2"/>{T(503, 452, 'USD', INK, 22, 800, 1, 'middle')}
  {''.join(f'<rect x="{340 + c*76}" y="{570 + r*44}" width="60" height="30" rx="4" fill="#4A4031"/>' for r in range(3) for c in range(3))}
  {T(300, 760, 'READER ASKS DOLLARS OR EUROS?', INK, 10, 800, 1.5)}{T(300, 776, 'EUROS. ALWAYS. (DECLINE DCC.)', RED, 10, 800, 1.5)}</svg>
{slug('d07')}
<div class="g" style="left:40px;top:120px;font-size:420px;font-stretch:100%;color:{RED};z-index:1">€</div>
{foot('d07')}
</div>'''

# ── d08 90″ — the piazza, the ninety-second ring, the kitchens outside it ─────────
px, py, pr = 408, 560, 190
inside = [(-80, -60), (40, -100), (90, 40), (-30, 90), (-110, 30), (60, -20)]
outside = [(-250, -150), (230, -170), (260, 80), (-240, 130), (150, 240), (-140, 250), (300, -40)]
tabs = ''.join(f'<circle cx="{px+dx}" cy="{py+dy}" r="10" fill="none" stroke="{PAPER}" stroke-width="2"/>' for dx, dy in inside)
tabs += ''.join(f'<circle cx="{px+dx}" cy="{py+dy}" r="10" fill="{GOLD}"/>' for dx, dy in outside)
d08 = f'''<div class="sh red">
<svg class="bg" viewBox="0 0 {W} {H}">
  <circle cx="{px}" cy="{py}" r="{pr}" fill="{RED2}"/>
  <g>{sampietrini(px, py, 46, PAPER, stone=6, gap=2)}</g>
  <circle cx="{px}" cy="{py}" r="{pr}" fill="none" stroke="{PAPER}" stroke-width="2" stroke-dasharray="3 5"/>
  {tabs}
  {T(px, py + 66, 'THE FAMOUS PIAZZA', PAPER, 10, 800, 1.6, 'middle')}
  {T(px, py - pr - 12, 'NINETY SECONDS ON FOOT', PAPER, 9, 700, 1.4, 'middle')}
  <circle cx="86" cy="{830 - 67}" r="3.6" fill="none" stroke="{PINK}" stroke-width="1.4"/>{T(96, 830 - 64, 'PHOTO-MENU, FLAGS, A TOUT AT THE DOOR — WALK AWAY', PINK, 9, 700, 1.3)}
  <circle cx="86" cy="{830 - 51}" r="4" fill="{GOLD}"/>{T(96, 830 - 48, 'SHORT ITALIAN MENU, ROMAN CLASSICS, LOCALS AFTER 8:30 P.M.', GOLD, 9, 700, 1.3)}</svg>
{slug('d08')}
<div class="g" style="left:60px;top:100px;font-size:220px;font-stretch:104%;color:{PAPER}">90″</div>
{foot('d08')}
</div>'''

# ── d09 OSTIA — two days drawn as bars: half a day, or the whole day ──────────────
x0, x1 = 82, 734
hrs = lambda h: x0 + (h - 7) / 17 * (x1 - x0)      # 07:00 → 24:00
bar = (f'<rect x="{hrs(9):.1f}" y="420" width="{hrs(14)-hrs(9):.1f}" height="56" fill="{INK}"/>'
       f'<rect x="{hrs(19):.1f}" y="420" width="{hrs(23)-hrs(19):.1f}" height="56" fill="{RED}"/>'
       + T(hrs(9) + 10, 454, 'OSTIA ANTICA · METRO', PAPER, 11, 800, 1.4) + T(hrs(19) + 10, 454, 'THE EVENING IN ROME', PAPER, 9.5, 800, 1.4)
       + f'<rect x="{hrs(7.5):.1f}" y="560" width="{hrs(19.5)-hrs(7.5):.1f}" height="56" fill="none" stroke="{INK}" stroke-width="3"/>'
       + T(hrs(7.5) + 10, 594, 'POMPEII · ~12H DOOR-TO-DOOR, THE WHOLE DAY', INK, 11, 800, 1.4)
       + T(x0, 410, 'HALF A DAY; KEEP THE EVENING', INK, 9, 700, 1.3) + T(x0, 550, 'THE GREATER SITE — AT THE FULL DAY’S PRICE', INK, 9, 700, 1.3))
ticks = ''.join(f'<line x1="{hrs(h):.1f}" y1="650" x2="{hrs(h):.1f}" y2="{662 if h % 6 else 672}" stroke="{INK}" stroke-width="1.5"/>' + (T(hrs(h), 690, f"{h:02d}:00", INK, 9, 700, 1, 'middle') if h % 6 == 0 else '') for h in range(7, 25))
d09 = f'''<div class="sh gold">
<svg class="bg" viewBox="0 0 {W} {H}">{bar}<line x1="{x0}" y1="650" x2="{x1}" y2="650" stroke="{INK}" stroke-width="1.5"/>{ticks}</svg>
{slug('d09')}
<div class="g" style="left:58px;top:110px;font-size:230px;font-stretch:86%;color:{INK}">OSTIA</div>
<div class="gloss" style="left:82px;top:300px;width:520px">Not Pompeii — for one spare day.</div>
{foot('d09')}
</div>'''

# ── a duotone photograph page — the Vatican, in La Tavola's two inks ─────────────
duo = f'''<div class="sh paper">
<div class="duo"><img src="{IMG}p24-0.jpeg" style="object-position:50% 35%"><div class="tone" style="background:{RED}"></div><div class="lift" style="background:#34160d"></div></div>
<div class="g" style="left:52px;top:430px;font-size:170px;font-stretch:96%;color:{GOLD};z-index:2">TWO<br>LINES.</div>
<div class="tail"><div><div class="cap">The Vatican Museums — the line a timed ticket skips, and the one it doesn’t</div>
<p style="margin:0">The closing frame printed in the book's two inks, so the photograph belongs to the poster before it.</p></div>
<div style="border-top:3px solid {RED};padding-top:8px;font-size:10px;line-height:14px"><span style="color:{RED};font-size:9px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;display:block;margin-bottom:5px">Specimen note</span>Rome's sign is the sampietrino: the cover's field, the paved core of 13′, the piazza of 90″.</div></div>
</div>'''

POSTERS = {'cover': cover, 'd01': d01, 'd02': d02, 'd03': d03, 'd04': d04, 'd05': d05, 'd06': d06, 'd07': d07, 'd08': d08, 'd09': d09}
POSTER_CSS = CSS
html = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Marta II · Rome</title><style>{CSS}</style></head><body>{cover}{d01}{d02}{d03}{d04}{d05}{d06}{d07}{d08}{d09}{duo}</body></html>'
if __name__ == '__main__':
    write(html)
