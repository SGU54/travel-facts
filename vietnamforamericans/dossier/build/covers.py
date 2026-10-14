# covers.py — the cover device.
# The test (cover.md): could this cover sit on any book about Vietnam? It must
# be reproducible ONLY by someone who did this book's analysis.
#
# Vietnam's organising fact is a LINE WITH THREE CLIMATES: the country runs
# three seasons at once down one 1,650 km spine, and the direction you travel it
# is locked by the ticket. So the cover draws the real spine (coordinates) and,
# beside it, the one strip that says it in a look — twelve months, three bands,
# never all green. One device, three labels, promise line at 22px.
# ─────────────────────────────────────────────────────────────────────────────
from maps import GEO, _proj, SEASON, SCOL, MONTHS

PAPER = "#F3EDE0"; INK = "#16140F"; RED = "#C9321D"; JADE = "#137A64"
GILT = "#D9A520"; DEEP = "#8F2112"; SOFT = "#8A8378"; PANEL = "#EAE3D3"
CW, CH = 816, 1056
MONO = "'Space Mono',monospace"; DISP = "'Anton',sans-serif"; BODY = "'Source Serif 4',serif"


def cover_svg():
    p = [f'<svg viewBox="0 0 {CW} {CH}" xmlns="http://www.w3.org/2000/svg">']
    # full-bleed cream, with the four plates as a top band — the site's identity
    p.append(f'<rect width="{CW}" height="{CH}" fill="{PAPER}"/>')
    p.append(f'<rect x="0" y="0" width="{CW}" height="18" fill="{RED}"/>')
    p.append(f'<rect x="0" y="18" width="{CW}" height="6" fill="{JADE}"/>')
    p.append(f'<rect x="0" y="24" width="{CW}" height="4" fill="{GILT}"/>')

    # ── the spine, from real coordinates, filling the left two-thirds ────────
    keys = ("Hà Giang","Sapa","Hanoi","Hạ Long","Ninh Bình","Huế","Đà Nẵng","Hội An","Nha Trang",
            "Ho Chi Minh City","Cần Thơ","Phú Quốc","Côn Đảo")
    f = _proj([GEO[k] for k in keys], 470, 600, 60)
    def P(k):
        x, y = f(*GEO[k]); return x + 40, y + 70
    spine = ["Hanoi","Ninh Bình","Huế","Đà Nẵng","Nha Trang","Ho Chi Minh City"]
    pts = " ".join(f"{P(k)[0]:.1f},{P(k)[1]:.1f}" for k in spine)
    # three climate fields behind the spine, by latitude
    def Y(lat): return f(lat, 106)[1] + 70
    for lo, hi, col in ((19.0, 23.6, JADE), (14.5, 19.0, GILT), (8.3, 14.5, RED)):
        y0, y1 = Y(hi), Y(lo)
        p.append(f'<rect x="40" y="{y0:.1f}" width="470" height="{y1-y0:.1f}" fill="{col}" opacity="0.10"/>')
    p.append(f'<polyline points="{pts}" fill="none" stroke="{INK}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>')
    for a, b in (("Hanoi","Sapa"),("Hanoi","Hạ Long"),("Ho Chi Minh City","Cần Thơ"),("Cần Thơ","Phú Quốc"),("Ho Chi Minh City","Côn Đảo"),("Hanoi","Hà Giang")):
        (x1,y1),(x2,y2) = P(a), P(b)
        p.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{SOFT}" stroke-width="1.6" stroke-dasharray="4 5" opacity=".8"/>')
    for k in keys:
        x, y = P(k)
        big = k in ("Hanoi","Ho Chi Minh City","Đà Nẵng")
        p.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{9 if big else 4.5}" fill="{PAPER}" stroke="{INK}" stroke-width="{3 if big else 1.8}"/>')
    # at most three labels, ≥24px (cover.md)
    for k, lab, dx, dy, an in (("Hanoi","HANOI",-18,10,"end"),("Đà Nẵng","ĐÀ NẴNG",18,10,"start"),("Ho Chi Minh City","SAIGON",18,10,"start")):
        x, y = P(k)
        p.append(f'<text x="{x+dx:.1f}" y="{y+dy:.1f}" font-size="26" fill="{INK}" text-anchor="{an}" font-family="{DISP}" letter-spacing="2">{lab}</text>')

    # ── the strip: twelve months, three bands, never all green ───────────────
    L, T = 548, 120
    cw = 18; rh = 26
    p.append(f'<text x="{L}" y="{T-30}" font-size="13" fill="{SOFT}" font-family="{MONO}" letter-spacing="1">THREE CLIMATES, ONE LINE</text>')
    p.append(f'<text x="{L}" y="{T-8}" font-size="12" fill="{SOFT}" font-family="{MONO}" letter-spacing="1">JANUARY TO DECEMBER</text>')
    for ri, (name, vals) in enumerate(list(SEASON.items())[:3]):
        y = T + ri * (rh + 22)
        lab = name.split("·")[0].strip()
        p.append(f'<text x="{L}" y="{y+rh+15}" font-size="12" fill="{INK}" font-family="{MONO}" letter-spacing="1">{lab}</text>')
        for i, v in enumerate(vals):
            x = L + i * cw
            op = {2: "0.95", 1: "0.55", 0: "0.5"}[v]
            p.append(f'<rect x="{x+1}" y="{y}" width="{cw-2}" height="{rh}" fill="{SCOL[v]}" opacity="{op}"/>')
    # one line under the strip
    p.append(f'<text x="{L}" y="{T+3*(rh+22)+16}" font-size="12" fill="{DEEP}" font-family="{MONO}" letter-spacing="0.5">NO MONTH IS GREEN</text>')
    p.append(f'<text x="{L}" y="{T+3*(rh+22)+32}" font-size="12" fill="{DEEP}" font-family="{MONO}" letter-spacing="0.5">AT BOTH ENDS</text>')

    # ── the title block ──────────────────────────────────────────────────────
    p.append(f'<line x1="60" y1="744" x2="{CW-60}" y2="744" stroke="{JADE}" stroke-width="2"/>')
    p.append(f'<text x="60" y="728" font-size="12" fill="{SOFT}" font-family="{MONO}" letter-spacing="1">A DECISION MANUAL &#183; FIRST TRIP &#183; FOR AMERICANS</text>')
    p.append(f'<text x="60" y="850" font-size="108" fill="{INK}" font-family="{DISP}" letter-spacing="1">Vietnam,</text>')
    p.append(f'<text x="60" y="946" font-size="92" fill="{RED}" font-family="{DISP}" letter-spacing="1">End to End.</text>')
    # the promise line — the dominant edge is DAYS and ORDER, not money
    p.append(f'<text x="60" y="988" font-size="22" fill="{INK}" font-family="{BODY}" font-style="italic">'
             f'A thousand-mile country, two weeks, three seasons that never agree.</text>')
    p.append(f'<text x="60" y="1017" font-size="22" fill="{INK}" font-family="{BODY}" font-style="italic">'
             f'The order that keeps the trip whole.</text>')
    p.append(f'<text x="60" y="1040" font-size="12" fill="{SOFT}" font-family="{MONO}" letter-spacing="1">VIETNAM FOR AMERICANS</text>')
    p.append(f'<text x="{CW-60}" y="1040" font-size="12" fill="{SOFT}" text-anchor="end" font-family="{MONO}" letter-spacing="1">FIRST EDITION &#183; 2026</text>')
    p.append('</svg>')
    return "".join(p)
