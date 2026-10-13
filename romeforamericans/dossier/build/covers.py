# covers.py — the cover device. The organising fact IS the cover: the ring, with real walk-times.
from maps import C, LM, Proj, TX, DOT, tiber_path, mins, MONO, DISP

def COVER_DEVICE():
    W,H=660,262; P=Proj(41.869,41.9185, 12.4465,12.510, W,H, 14)
    o=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    o.append(f'<rect width="{W}" height="{H}" fill="{C["paper"]}"/>')
    o.append(tiber_path(P,10))
    px,py=P.xy(*LM["Pantheon"]); r1=P.r_km(1.0)
    o.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r1:.1f}" fill="{C["zone"]}" fill-opacity="0.5"/>')
    o.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r1:.1f}" fill="none" stroke="{C["accent"]}" '
             f'stroke-width="2.4" stroke-dasharray="3 6"/>')
    ticks=[("Trevi","8′"),("Colosseum","20′"),("St Peter's","30′"),("Trastevere","18′")]
    for k,lab in ticks:
        x,y=P.xy(*LM[k])
        o.append(f'<line x1="{px:.1f}" y1="{py:.1f}" x2="{x:.1f}" y2="{y:.1f}" '
                 f'stroke="{C["gilt"]}" stroke-width="1.2"/>')
        mx,my=(px+x)/2,(py+y)/2
        o.append(f'<rect x="{mx-11:.1f}" y="{my-8:.1f}" width="24" height="12" fill="{C["paper"]}"/>')
        o.append(TX(mx+1,my+2,lab,8.5,"middle",C["deep"],w=500))
    names=["Pantheon","Colosseum","St Peter's","Trastevere","Trevi","Termini","Spanish Steps"]
    offs={"Pantheon":(8,-6,"start"),"Colosseum":(9,4,"start"),"St Peter's":(9,-6,"start"),
          "Trastevere":(-9,14,"end"),"Trevi":(9,-6,"start"),"Termini":(-9,4,"end"),
          "Spanish Steps":(9,-6,"start")}
    for k in names:
        x,y=P.xy(*LM[k]); big=(k=="Pantheon")
        o.append(DOT(x,y,4.4 if big else 3.2,C["deep"] if big else C["accent"],ring=big))
        dx,dy,an=offs[k]
        o.append(TX(x+dx,y+dy,k.upper(),9,an,C["ink"]))
    sx,sy=W-140,H-20; sl=P.r_km(1.0)
    o.append(f'<line x1="{sx}" y1="{sy}" x2="{sx+sl:.1f}" y2="{sy}" stroke="{C["ink"]}" stroke-width="2"/>')
    o.append(f'<line x1="{sx}" y1="{sy-4}" x2="{sx}" y2="{sy+4}" stroke="{C["ink"]}" stroke-width="2"/>')
    o.append(f'<line x1="{sx+sl:.1f}" y1="{sy-4}" x2="{sx+sl:.1f}" y2="{sy+4}" stroke="{C["ink"]}" stroke-width="2"/>')
    o.append(TX(sx+sl/2,sy-8,"1 KM",8.5,"middle",C["muted"]))
    o.append('</svg>'); return "".join(o)

def COVER(strip_img_html=""):
    return f"""<div class="cov">
  <div class="frame"></div>
  <div class="in">
    <div class="brand"><span>ROMEFORAMERICANS.COM</span><span>A DECISION MANUAL · FIRST EDITION</span></div>
    <h1>Rome,<br/><i>Solved.</i></h1>
    <div class="sub">Every decision a first visit forces — where to sleep, what to book, what
    to skip — argued in the open, with the arithmetic shown, so you can disagree with us and
    still come out ahead.</div>
    <div class="dev">{COVER_DEVICE()}</div>
    <div class="capline"><span>TAV. I &nbsp;·&nbsp; THE CENTRE, HELD IN ONE RING</span>
      <span>WALK-TIMES AS PUBLISHED&nbsp; ▲</span></div>
    {strip_img_html}
    <div class="foot"><span>FOR FIRST-TIME AMERICAN VISITORS</span>
      <b>EDITION 2026.07 &nbsp;·&nbsp; WITH THE QUARTERLY FIELD SHEET</b></div>
  </div>
</div>"""
