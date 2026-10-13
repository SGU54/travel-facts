# maps.py — every vector figure, drawn from real lat/lon. Palette C is EXTENDED by
# illus.py, never replaced (bug log #10).
import math

C = {"paper":"#F6EEDB","ink":"#2B241A","accent":"#8A3324","gilt":"#C9A84C",
     "muted":"#7A6B4E","soft":"#9C8C6B","line":"#DED0AF","line_soft":"#E7DCC0",
     "zone":"#E9DEC2","stone":"#E3D6B4","deep":"#6E241D","water":"#CFD8CE"}

MONO="IBM Plex Mono"; DISP="IM Fell English"; BODY="Sorts Mill Goudy"

LM = {  # public geography — the raw material of every figure
 "Pantheon":(41.8986,12.4769), "Colosseum":(41.8902,12.4922), "Trevi":(41.9009,12.4833),
 "Navona":(41.8992,12.4731), "Spanish Steps":(41.9060,12.4823), "St Peter's":(41.9022,12.4539),
 "Vatican Museums":(41.9065,12.4536), "Castel S. Angelo":(41.9031,12.4663),
 "Campo de' Fiori":(41.8956,12.4722), "Trastevere":(41.8895,12.4693), "Termini":(41.9010,12.5011),
 "Monti":(41.8945,12.4890), "Testaccio":(41.8758,12.4744), "Borghese":(41.9142,12.4922),
 "Capitoline":(41.8934,12.4828), "Forum":(41.8925,12.4853), "P. Venezia":(41.8958,12.4823),
 "P. del Popolo":(41.9109,12.4763), "Ghetto":(41.8927,12.4778), "Prati":(41.9080,12.4600),
}
TIBER = [(41.9280,12.4680),(41.9190,12.4660),(41.9120,12.4690),(41.9060,12.4665),
         (41.9010,12.4655),(41.8970,12.4680),(41.8940,12.4665),(41.8890,12.4700),
         (41.8840,12.4755),(41.8790,12.4740),(41.8720,12.4785),(41.8650,12.4770)]
MET_A = [("Ottaviano",41.9056,12.4577),("Lepanto",41.9098,12.4636),("Flaminio",41.9107,12.4757),
         ("Spagna",41.9066,12.4830),("Barberini",41.9037,12.4886),("Repubblica",41.9028,12.4954),
         ("Termini",41.9010,12.5011),("Vittorio Em.",41.8942,12.5060)]
MET_B = [("Castro Pret.",41.9070,12.5085),("Termini",41.9010,12.5011),("Cavour",41.8990,12.4923),
         ("Colosseo",41.8905,12.4930),("Circo Massimo",41.8858,12.4855),("Piramide",41.8765,12.4815)]

def km(a,b):
    (la1,lo1),(la2,lo2)=LM[a],LM[b]; R=6371; p=math.pi/180
    dx=(lo2-lo1)*p*math.cos((la1+la2)*p/2); dy=(la2-la1)*p
    return R*math.hypot(dx,dy)*1.25            # 1.25 street factor
def mins(a,b): return round(km(a,b)/4.5*60)    # 4.5 km/h

class Proj:
    def __init__(s, lat0,lat1, lon0,lon1, w,h, pad=16):
        p=math.pi/180; s.k=math.cos((lat0+lat1)/2*p)
        s.x0,s.x1 = lon0*s.k, lon1*s.k; s.y0,s.y1 = lat0,lat1
        sc = min((w-2*pad)/(s.x1-s.x0), (h-2*pad)/(s.y1-s.y0))
        s.sc=sc; s.w,s.h,s.pad=w,h,pad
        s.ox = (w - sc*(s.x1-s.x0))/2; s.oy = (h - sc*(s.y1-s.y0))/2
    def xy(s, lat, lon):
        return (s.ox + (lon*s.k - s.x0)*s.sc, s.h - (s.oy + (lat - s.y0)*s.sc))
    def r_km(s, r):   # km → svg units (1° lat = 111.32 km)
        return r/111.32*s.sc

class _Boxes:
    """Reserve every marker + fixed label FIRST; then place the rest around them."""
    def __init__(s): s.b=[]
    def _hit(s,x0,y0,x1,y1):
        return any(min(x1,a1)-max(x0,a0)>1 and min(y1,c1)-max(y0,c0)>1
                   for (a0,c0,a1,c1) in s.b)
    def add(s,x0,y0,x1,y1): s.b.append((x0,y0,x1,y1))
    def place(s, x, y, text, fs, anchor="start", tries=None):
        w=len(text)*fs*0.58; h=fs
        if tries is None:
            tries=[(0,0,anchor),(0,-fs-3,anchor),(0,fs+5,anchor),
                   (0,0,"end" if anchor=="start" else "start"),
                   (0,fs+7,"middle"),(0,-fs-9,"middle")]
        for dx,dy,an in tries:
            xx,yy=x+dx,y+dy
            x0 = xx if an=="start" else (xx-w/2 if an=="middle" else xx-w)
            if not s._hit(x0,yy-h*0.78,x0+w,yy+h*0.24):
                s.add(x0,yy-h*0.78,x0+w,yy+h*0.24); return xx,yy,an
        x0 = x if anchor=="start" else (x-w/2 if anchor=="middle" else x-w)
        s.add(x0,y-h*0.78,x0+w,y+h*0.24); return x,y,anchor

def TX(x,y,t,fs=11,anchor="start",fill=None,fam=MONO,ls=".06em",it=False,w=400):
    fill=fill or C["ink"]
    st=f"font-family:'{fam}';font-size:{fs}px;letter-spacing:{ls};fill:{fill};font-weight:{w}"
    if it: st+=";font-style:italic"
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" style="{st}">{t}</text>'

def DOT(x,y,r=3.4,fill=None,ring=False):
    fill=fill or C["accent"]
    s=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}"/>'
    if ring: s+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r+2.6}" fill="none" stroke="{fill}" stroke-width="1"/>'
    return s

def tiber_path(P, wd=9):
    pts=" ".join(f"{P.xy(a,b)[0]:.1f},{P.xy(a,b)[1]:.1f}" for a,b in TIBER)
    return (f'<polyline points="{pts}" fill="none" stroke="{C["water"]}" stroke-width="{wd}" '
            f'stroke-linejoin="round" stroke-linecap="round"/>'
            f'<polyline points="{pts}" fill="none" stroke="{C["soft"]}" stroke-width="0.8" '
            f'stroke-dasharray="1 5" stroke-linejoin="round" stroke-linecap="round"/>')

def frame(w,h):
    return f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" fill="{C["paper"]}" stroke="{C["line"]}"/>'

_fign=[0]
def fig(svg, cap, cls="map"):
    _fign[0]+=1
    return (f'<figure class="{cls}">{svg}<figcaption><span class="fign">FIG. {_fign[0]}</span>'
            f' &nbsp;{cap}</figcaption></figure>')

# ── FIG · the ring — the organising fact ────────────────────────────────────
def GFX_RING():
    W,H=660,300; P=Proj(41.868,41.920, 12.446,12.512, W,H, 18)
    o=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">',frame(W,H)]
    o.append(tiber_path(P))
    px,py=P.xy(*LM["Pantheon"]); r1=P.r_km(1.0)
    o.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r1:.1f}" fill="{C["zone"]}" fill-opacity="0.5"/>')
    o.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r1:.1f}" fill="none" stroke="{C["accent"]}" '
             f'stroke-width="2.2" stroke-dasharray="3 6"/>')
    B=_Boxes()
    pts=["Pantheon","Navona","Campo de' Fiori","Trevi","Spanish Steps","P. del Popolo",
         "P. Venezia","Forum","Colosseum","Ghetto","St Peter's","Castel S. Angelo",
         "Trastevere","Monti","Termini","Borghese"]
    for k in pts:                       # pass 0 — every dot reserves first
        x,y=P.xy(*LM[k]); B.add(x-5,y-5,x+5,y+5)
    spokes=[("Trevi","8 MIN"),("Colosseum","20 MIN"),
            ("St Peter's","30 MIN"),("Trastevere","18 MIN")]
    o.append(f'<line x1="{px:.1f}" y1="{py:.1f}" x2="{P.xy(*LM["Navona"])[0]:.1f}" '
             f'y2="{P.xy(*LM["Navona"])[1]:.1f}" stroke="{C["gilt"]}" stroke-width="1.1"/>')
    for k,lab in spokes:
        x,y=P.xy(*LM[k])
        o.append(f'<line x1="{px:.1f}" y1="{py:.1f}" x2="{x:.1f}" y2="{y:.1f}" '
                 f'stroke="{C["gilt"]}" stroke-width="1.1"/>')
        mx,my=(px+x)/2,(py+y)/2
        xx,yy,anc=B.place(mx,my+1,lab,7.5,"middle",
                          tries=[(0,0,"middle"),(0,-13,"middle"),(0,13,"middle"),(16,3,"start"),(-16,3,"end")])
        w=len(lab)*7.5*0.58
        bx = xx-w/2 if anc=="middle" else (xx if anc=="start" else xx-w)
        o.append(f'<rect x="{bx-2:.1f}" y="{yy-8:.1f}" width="{w+4:.1f}" height="11" fill="{C["paper"]}"/>')
        o.append(TX(xx,yy,lab,7.5,anc,C["deep"],w=500))
    for k in pts:
        x,y=P.xy(*LM[k])
        big = k=="Pantheon"
        o.append(DOT(x,y, 4.2 if big else 3.2, C["deep"] if big else C["accent"], ring=big))
        an = "end" if x>W-90 else "start"
        lx = x-7 if an=="end" else x+7
        flip = "end" if an=="start" else "start"
        tries=[(0,0,an),(0,-12,an),(0,13,an),(-14 if an=="start" else 14,0,flip),
               (0,-24,an),(0,25,an),(0,-12,flip),(0,13,flip),(0,-36,"middle")]
        xx,yy,anc=B.place(lx,y+3.5,k.upper(),8.5,an,tries=tries)
        o.append(TX(xx,yy,k.upper(),8.5,anc,C["ink"]))
    sx,sy=W-150,H-22; sl=P.r_km(1.0)
    o.append(f'<line x1="{sx}" y1="{sy}" x2="{sx+sl:.1f}" y2="{sy}" stroke="{C["ink"]}" stroke-width="2"/>')
    o.append(f'<line x1="{sx}" y1="{sy-4}" x2="{sx}" y2="{sy+4}" stroke="{C["ink"]}" stroke-width="2"/>')
    o.append(f'<line x1="{sx+sl:.1f}" y1="{sy-4}" x2="{sx+sl:.1f}" y2="{sy+4}" stroke="{C["ink"]}" stroke-width="2"/>')
    o.append(TX(sx+sl/2,sy-8,"1 KM",8,"middle",C["muted"]))
    o.append(TX(20,26,"THE CENTRE, HELD IN ONE RING",9.5,"start",C["accent"],w=500))
    o.append(TX(20,40,"one kilometre around the Pantheon · walk-times as published",7.5,"start",C["muted"]))
    o.append('</svg>'); return "".join(o)

# ── FIG · transit reality — the hole where the centre is ───────────────────
def GFX_TRANSIT():
    W,H=660,300; P=Proj(41.868,41.920, 12.446,12.516, W,H, 18)
    o=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">',frame(W,H)]
    o.append(tiber_path(P,8))
    px,py=P.xy(*LM["Pantheon"]); r1=P.r_km(1.0)
    o.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r1:.1f}" fill="{C["zone"]}" fill-opacity="0.55"/>')
    o.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r1:.1f}" fill="none" stroke="{C["muted"]}" '
             f'stroke-width="1.4" stroke-dasharray="2 5"/>')
    B=_Boxes()
    for line,colr in ((MET_A,C["gilt"]),(MET_B,C["deep"])):
        pts=" ".join(f"{P.xy(la,lo)[0]:.1f},{P.xy(la,lo)[1]:.1f}" for _,la,lo in line)
        o.append(f'<polyline points="{pts}" fill="none" stroke="{colr}" stroke-width="3.4" '
                 f'stroke-linejoin="round"/>')
    for line,colr in ((MET_A,C["gilt"]),(MET_B,C["deep"])):
        for nm,la,lo in line:
            x,y=P.xy(la,lo); B.add(x-5,y-5,x+5,y+5)
            o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="{C["paper"]}" '
                     f'stroke="{colr}" stroke-width="2"/>')
    seen=set()
    for line in (MET_A,MET_B):
        for nm,la,lo in line:
            if nm in seen: continue
            seen.add(nm); x,y=P.xy(la,lo)
            an="end" if x>W-95 else "start"; lx=x-7 if an=="end" else x+7
            xx,yy,anc=B.place(lx,y+3,nm.upper(),7.5,an)
            o.append(TX(xx,yy,nm.upper(),7.5,anc,C["muted"]))
    for k in ("Pantheon","Navona","Trevi","Campo de' Fiori","Colosseum","St Peter's"):
        x,y=P.xy(*LM[k]); o.append(DOT(x,y,2.8,C["accent"]))
        B.add(x-4,y-4,x+4,y+4)
    xx,yy,anc=B.place(px, py-r1-14, "NO STATION INSIDE THIS RING", 9, "middle",
                      tries=[(0,0,"middle"),(0,-14,"middle"),(0,-28,"middle"),(0,26,"middle")])
    o.append(TX(xx,yy,"NO STATION INSIDE THIS RING",9,anc,C["accent"],w=500))
    o.append(TX(20,26,"WHY THE METRO CANNOT HELP YOU",9.5,"start",C["accent"],w=500))
    o.append(TX(20,40,"lines A and B, drawn to scale — the ruins forbid tunnelling under the core",
                7.5,"start",C["muted"]))
    lx=W-176
    o.append(f'<line x1="{lx}" y1="20" x2="{lx+22}" y2="20" stroke="{C["gilt"]}" stroke-width="3.4"/>')
    o.append(TX(lx+28,23,"LINE A",7.5,"start",C["muted"]))
    o.append(f'<line x1="{lx+82}" y1="20" x2="{lx+104}" y2="20" stroke="{C["deep"]}" stroke-width="3.4"/>')
    o.append(TX(lx+110,23,"LINE B",7.5,"start",C["muted"]))
    o.append('</svg>'); return "".join(o)

# ── FIG · arrival — the FCO fork, on a time axis ────────────────────────────
def GFX_ARRIVAL():
    W,H=660,240
    o=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">',frame(W,H)]
    ax0,ax1,ay=150,620,206
    o.append(f'<line x1="{ax0}" y1="{ay}" x2="{ax1}" y2="{ay}" stroke="{C["line"]}" stroke-width="1.4"/>')
    for m in (0,15,30,45,60):
        x=ax0+(ax1-ax0)*m/70
        o.append(f'<line x1="{x:.0f}" y1="{ay-3}" x2="{x:.0f}" y2="{ay+3}" stroke="{C["muted"]}" stroke-width="1.2"/>')
        o.append(TX(x,ay+15,f"{m}′",8,"middle",C["muted"]))
    o.append(TX(ax1,ay+15,"PLATFORM-TO-PLATFORM",7,"end",C["soft"]))
    o.append(TX(26,52,"FCO",15,"start",C["deep"],fam=DISP))
    o.append(TX(26,66,"FIUMICINO",7.5,"start",C["muted"]))
    lanes=[("LEONARDO EXPRESS","non-stop to Termini · every ~15′",32,32,C["accent"],"TERMINI","▲"),
           ("FL1 REGIONAL","skips Termini — Trastevere · Ostiense · Tiburtina",30,48,C["gilt"],"TRASTEVERE →","●"),
           ("TAXI · FIXED FARE","flat rate to inside the walls, luggage included",45,60,C["deep"],"YOUR DOOR","◇"),
           ("SHUTTLE BUS","cheapest seat · same traffic as the taxi",45,68,C["soft"],"TERMINI","▲")]
    y=56
    for name,sub,t0,t1,colr,dest,mk in lanes:
        x_0=ax0+(ax1-ax0)*t0/70; x_1=ax0+(ax1-ax0)*t1/70
        o.append(f'<line x1="{ax0}" y1="{y}" x2="{x_0:.0f}" y2="{y}" stroke="{colr}" stroke-width="3"/>')
        if t1>t0:
            o.append(f'<line x1="{x_0:.0f}" y1="{y}" x2="{x_1:.0f}" y2="{y}" stroke="{colr}" '
                     f'stroke-width="3" stroke-dasharray="2 4" opacity="0.75"/>')
        o.append(f'<circle cx="{ax0}" cy="{y}" r="3" fill="{colr}"/>')
        o.append(f'<circle cx="{x_1:.0f}" cy="{y}" r="4" fill="{C["paper"]}" stroke="{colr}" stroke-width="2.2"/>')
        o.append(TX(ax0,y-16,f"{name}  {mk}",9,"start",colr,w=500))
        o.append(TX(ax0,y-6,sub,7.5,"start",C["muted"]))
        o.append(TX(x_1+9,y+3,dest,7.5,"start",C["ink"]))
        y+=38
    o.append(TX(26,224,"FARES: FIELD SHEET §1 ◆",7.5,"start",C["soft"]))
    o.append('</svg>'); return "".join(o)

# ── FIG · the week grid — closures as a pattern ─────────────────────────────
def GFX_WEEK():
    W,H=660,264
    o=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">',frame(W,H)]
    days=["MON","TUE","WED","THU","FRI","SAT","SUN"]
    gx0,gy0,cw,ch=190,48,64,24
    for i,d in enumerate(days):
        o.append(TX(gx0+i*cw+cw/2,gy0-10,d,8,"middle",C["muted"],w=500))
    rows=[("Vatican Museums",{6:"closed"},{"note":(6,"LAST SUN FREE · MOBBED")}),
          ("Borghese Gallery",{0:"closed"},{}),
          ("Castel Sant'Angelo",{0:"closed"},{}),
          ("Ostia Antica (trip)",{0:"closed"},{}),
          ("Testaccio Market",{6:"closed"},{}),
          ("Papal Audience",{},{"gilt":(2,"WED AM")}),
          ("State museums",{},{"gilt":(6,"1st SUN FREE")})]
    y=gy0
    for name,closed,extra in rows:
        o.append(TX(gx0-10,y+ch/2+3,name,9.5,"end",C["ink"],fam=BODY,ls="0"))
        for i in range(7):
            x=gx0+i*cw
            if i in closed:
                o.append(f'<rect x="{x+2}" y="{y+2}" width="{cw-4}" height="{ch-4}" fill="{C["ink"]}"/>')
                o.append(TX(x+cw/2,y+ch/2+3,"CLOSED",6.5,"middle",C["paper"]))
            elif "gilt" in extra and extra["gilt"][0]==i:
                o.append(f'<rect x="{x+2}" y="{y+2}" width="{cw-4}" height="{ch-4}" fill="{C["gilt"]}"/>')
                o.append(TX(x+cw/2,y+ch/2+3,extra["gilt"][1],5.6,"middle",C["ink"],w=500))
            elif "note" in extra and extra["note"][0]==i:
                o.append(f'<rect x="{x+2}" y="{y+2}" width="{cw-4}" height="{ch-4}" fill="{C["ink"]}"/>')
                o.append(f'<rect x="{x+2}" y="{y+2}" width="{cw-4}" height="7" fill="{C["gilt"]}"/>')
                o.append(TX(x+cw/2,y+ch/2+6,"CLOSED*",6,"middle",C["paper"]))
            else:
                o.append(f'<rect x="{x+2}" y="{y+2}" width="{cw-4}" height="{ch-4}" fill="{C["zone"]}" '
                         f'stroke="{C["line_soft"]}"/>')
        y+=ch+3
    o.append(TX(20,26,"THE WEEK, AS THE SIGHTS KEEP IT",9.5,"start",C["accent"],w=500))
    o.append(TX(20,y+14,"* museums free on the LAST Sunday of each month — and at their most crowded  ◇",
                7.5,"start",C["muted"]))
    o.append('</svg>'); return "".join(o)

# ── FIG · the month strip — the season decision, seen ───────────────────────
def GFX_MONTHS():
    W,H=660,236
    o=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">',frame(W,H)]
    mo=["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
    heat  =[1,1,1,2,2,3,3,3,2,2,1,1]
    crowd =[1,1,2,3,3,3,3,3,3,3,1,2]
    price =[1,1,2,3,3,3,2,2,3,3,1,2]
    gx0,gy0,cw,ch=118,66,44,26
    shade={1:C["zone"],2:C["stone"],3:C["accent"]}
    for i,m in enumerate(mo):
        o.append(TX(gx0+i*cw+cw/2,gy0-12,m,7.5,"middle",C["muted"],w=500))
    for rname,vals,y in (("HEAT",heat,gy0),("CROWDS",crowd,gy0+ch+4),("PRICE",price,gy0+2*(ch+4))):
        o.append(TX(gx0-10,y+ch/2+3,rname,8,"end",C["muted"],w=500))
        for i,v in enumerate(vals):
            x=gx0+i*cw
            op = "0.9" if v==3 else "1"
            o.append(f'<rect x="{x+2}" y="{y+2}" width="{cw-4}" height="{ch-4}" '
                     f'fill="{shade[v]}" fill-opacity="{op}" stroke="{C["line_soft"]}"/>')
    by=gy0+3*(ch+4)+14
    for a,b,lab in ((3,4,"THE WINDOW"),(8,9,"THE WINDOW")):
        x0=gx0+a*cw+2; x1=gx0+(b+1)*cw-2
        o.append(f'<path d="M {x0} {by} v 6 h {x1-x0} v -6" fill="none" stroke="{C["deep"]}" stroke-width="1.6"/>')
        o.append(TX((x0+x1)/2,by+18,lab,7.5,"middle",C["deep"],w=500))
    marks=[(3.35,"EASTER · CROWDS ◇"),(7.5,"FERRAGOSTO AUG 15 · LOCALS LEAVE ▲"),(11.7,"HOLIDAYS")]
    for pos,lab in marks:
        x=gx0+pos*cw
        o.append(f'<path d="M {x:.0f} {gy0-32} l 4 6 l -4 6 l -4 -6 z" fill="{C["gilt"]}"/>')
    o.append(TX(gx0+3.35*cw+8,gy0-24,"EASTER",6.5,"start",C["muted"]))
    o.append(TX(gx0+7.5*cw+8,gy0-24,"FERRAGOSTO",6.5,"start",C["muted"]))
    o.append(TX(20,26,"TWELVE MONTHS, THREE PRESSURES",9.5,"start",C["accent"],w=500))
    o.append(TX(gx0,H-16,"darker = higher · winter is the quiet bargain, summer the survival exercise  ●",7.5,"start",C["muted"]))
    o.append('</svg>'); return "".join(o)

# ── FIG · order-of-ops flows ────────────────────────────────────────────────
def _flow(title, steps, footer):
    W,H=660,220
    o=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">',frame(W,H)]
    o.append(TX(20,26,title,9.5,"start",C["accent"],w=500))
    n=len(steps); bw=118; gap=(W-40-n*bw)/(n-1); x=20; y=64; bh=96
    for i,(head,body,mk) in enumerate(steps):
        o.append(f'<rect x="{x:.0f}" y="{y}" width="{bw}" height="{bh}" fill="{C["zone"]}" '
                 f'stroke="{C["line"]}"/>')
        o.append(f'<rect x="{x:.0f}" y="{y}" width="{bw}" height="4" fill="{C["accent"]}"/>')
        o.append(TX(x+9,y+22,f"{i+1:02d}",10,"start",C["accent"],w=500))
        wrapped=head.split("|")
        for j,ln in enumerate(wrapped):
            o.append(TX(x+9,y+40+j*13,ln,10.5,"start",C["ink"],fam=BODY,ls="0"))
        yb=y+40+len(wrapped)*13+2
        for j,ln in enumerate(body.split("|")):
            o.append(TX(x+9,yb+j*11,ln,7.5,"start",C["muted"]))
        o.append(TX(x+bw-8,y+bh-9,mk,8,"end",C["deep"]))
        if i<n-1:
            ax=x+bw+3
            o.append(f'<path d="M {ax:.0f} {y+bh/2} h {gap-12:.0f} m 0 0 l -7 -5 m 7 5 l -7 5" '
                     f'stroke="{C["deep"]}" stroke-width="1.6" fill="none"/>')
        x+=bw+gap
    for j,ln in enumerate(footer.split("|")):
        o.append(TX(20,y+bh+28+j*13,ln,8,"start",C["muted"]))
    o.append('</svg>'); return "".join(o)

def GFX_FLOW_COL():
    steps=[("Book the slot,|weeks out","one official seller —|everything else is|markup or a tour","◆"),
           ("Colosseum,|early","the timed entry;|security, then the tiers","▲"),
           ("Forum,|same ticket","walk straight in —|one combined admission","◇"),
           ("Palatine,|same ticket","finish on the hill;|the view back is the reward","●"),
           ("Capitoline|overlook","free balcony over the|Forum — the closing shot","●")]
    return _flow("THE ANCIENT CORE, RUN AS ONE OPERATION", steps,
                 "the combined ticket runs on a 24-hour clock ◇ — one morning, one admission, three sights|no same-day door tickets worth counting on ▲ · the release window lives on the Field Sheet ◆")

def GFX_FLOW_VAT():
    steps=[("Book timed|entry","non-negotiable in|season — slots sell out","▲"),
           ("Arrive T−25","security screens everyone;|no ticket skips it","●"),
           ("The Museums","Raphael Rooms first,|Sistine at the route's end","●"),
           ("St Peter's","separate line, free entry —|dress to code","◇"),
           ("The dome","551 steps; the lift|erases only 230","●")]
    return _flow("THE VATICAN, RUN AS ONE OPERATION", steps,
                 "Wednesday mornings the Papal Audience takes the square — Museums run, the basilica waits ◇|the early slot beats the tour groups; the late one outlives them ▲")

# ── FIG · the trap ring — original intel ────────────────────────────────────
def GFX_TRAP():
    W,H=660,300; P=Proj(41.8885,41.9045, 12.4665,12.4885, W,H, 20)
    o=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">',frame(W,H)]
    o.append(tiber_path(P,12))
    B=_Boxes()
    hot=["Navona","Pantheon","Trevi","Campo de' Fiori"]
    r=P.r_km(0.12)
    for k in hot:
        x,y=P.xy(*LM[k])
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{C["accent"]}" fill-opacity="0.14"/>')
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="none" stroke="{C["accent"]}" '
                 f'stroke-width="1.6" stroke-dasharray="3 4"/>')
        o.append(DOT(x,y,3.4,C["deep"]))
        B.add(x-5,y-5,x+5,y+5)
    for k in hot:
        x,y=P.xy(*LM[k])
        xx,yy,anc=B.place(x+8,y+3,k.upper(),9,"start")
        o.append(TX(xx,yy,k.upper(),9,anc,C["ink"]))
    escapes=[((41.8969,12.4712),"90″ WEST"),((41.9003,12.4796),"90″ EAST"),
             ((41.8946,12.4753),"90″ SOUTH")]
    for (la,lo),lab in escapes:
        x,y=P.xy(la,lo)
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="none" stroke="{C["gilt"]}" stroke-width="2"/>')
        xx,yy,anc=B.place(x+7,y+3,lab,7.5,"start")
        o.append(TX(xx,yy,lab,7.5,anc,C["deep"],w=500))
    gx,gy=P.xy(*LM["Ghetto"])
    o.append(DOT(gx,gy,3,C["gilt"]))
    xx,yy,anc=B.place(gx+7,gy+3,"GHETTO · GO",8,"start")
    o.append(TX(xx,yy,"GHETTO · GO",8,anc,C["deep"],w=500))
    tx,ty=P.xy(41.8895,12.4693)
    o.append(f'<path d="M {tx:.0f} {ty:.0f} l -26 18" stroke="{C["gilt"]}" stroke-width="1.4" fill="none"/>')
    o.append(TX(tx-30,ty+30,"TRASTEVERE, OVER THE BRIDGE · GO",8,"middle",C["deep"],w=500))
    o.append(TX(20,26,"THE RENT RING",9.5,"start",C["accent"],w=500))
    o.append(TX(20,40,"120 m around each famous square, the view is on the bill · the escape is always ninety seconds  ▲ 07/26",
                7.5,"start",C["muted"]))
    o.append('</svg>'); return "".join(o)

# ── FIG · neighborhood locators (6 minis) ───────────────────────────────────
HOODS = {"centro":("Centro Storico","Pantheon", None),
         "monti":("Monti","Monti","Colosseum"),
         "trastevere":("Trastevere","Trastevere",None),
         "prati":("Prati · Borgo","Prati","St Peter's"),
         "termini":("Termini · Esquilino","Termini",None),
         "testaccio":("Testaccio","Testaccio",None)}

def MAP_HOOD(key):
    W,H=204,150; P=Proj(41.868,41.918, 12.446,12.508, W,H, 10)
    name, at, near = HOODS[key]
    o=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">',frame(W,H)]
    o.append(tiber_path(P,5))
    px,py=P.xy(*LM["Pantheon"]); r1=P.r_km(1.0)
    o.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r1:.1f}" fill="none" stroke="{C["line"]}" '
             f'stroke-width="1.1" stroke-dasharray="2 4"/>')
    o.append(f'<path d="M {px-3:.1f} {py:.1f} h 6 M {px:.1f} {py-3:.1f} v 6" '
             f'stroke="{C["muted"]}" stroke-width="1.3"/>')
    hx,hy=P.xy(*LM[at])
    o.append(f'<line x1="{px:.1f}" y1="{py:.1f}" x2="{hx:.1f}" y2="{hy:.1f}" '
             f'stroke="{C["gilt"]}" stroke-width="1.2"/>')
    o.append(DOT(hx,hy,4.4,C["accent"],ring=True))
    m = mins(at,"Pantheon")
    lab = f"{m}′ TO THE PANTHEON" if m>2 else "YOU ARE THE CENTRE"
    o.append(TX(W/2,H-9,lab,7.5,"middle",C["deep"],w=500))
    if near:
        nx,ny=P.xy(*LM[near])
        o.append(f'<circle cx="{nx:.1f}" cy="{ny:.1f}" r="2.2" fill="{C["muted"]}"/>')
    o.append('</svg>'); return "".join(o)

# ── FIG · the stay decision tree ────────────────────────────────────────────
def GFX_TREE():
    W,H=660,330
    o=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">',frame(W,H)]
    def node(x,y,w,h,head,sub="",leaf=False):
        fill = C["zone"] if not leaf else C["paper"]
        o.append(f'<rect x="{x-w/2:.0f}" y="{y-h/2:.0f}" width="{w}" height="{h}" fill="{fill}" '
                 f'stroke="{C["accent"] if leaf else C["line"]}" stroke-width="{1.6 if leaf else 1}"/>')
        o.append(TX(x,y-2 if sub else y+3.5,head,10 if leaf else 10.5,"middle",
                    C["deep"] if leaf else C["ink"],fam=BODY,ls="0"))
        if sub: o.append(TX(x,y+11,sub,7,"middle",C["muted"]))
    def edge(x1,y1,x2,y2,lab=""):
        mx=(x1+x2)/2
        o.append(f'<path d="M {x1:.0f} {y1:.0f} C {x1:.0f} {(y1+y2)/2:.0f} {x2:.0f} {(y1+y2)/2:.0f} {x2:.0f} {y2:.0f}" '
                 f'fill="none" stroke="{C["muted"]}" stroke-width="1.3"/>')
        if lab:
            o.append(f'<rect x="{mx-len(lab)*2.6-3:.0f}" y="{(y1+y2)/2-7:.0f}" width="{len(lab)*5.2+6:.0f}" height="12" fill="{C["paper"]}"/>')
            o.append(TX(mx,(y1+y2)/2+2,lab,7,"middle",C["accent"],w=500))
    node(330,46,236,32,"Is this the first visit?")
    edge(330,62,330,102,"YES"); edge(330,62,564,150,"NO — you know your Rome")
    node(330,118,300,32,"Can the budget carry the centre?")
    edge(330,134,150,196,"YES"); edge(330,134,400,196,"NO")
    node(150,212,190,32,"Mornings or evenings?")
    edge(150,228,74,286,"MORNINGS"); edge(150,228,232,286,"EVENINGS")
    node(74,296,128,44,"CENTRO STORICO","walk to everything · pay for it",leaf=True)
    node(232,296,128,44,"TRASTEVERE","the evenings win · bridge to cross",leaf=True)
    node(400,212,206,32,"Dawn train or tight budget?")
    edge(400,228,392,286,"CHARACTER FIRST"); edge(400,228,540,286,"LOGISTICS FIRST")
    node(392,296,128,44,"MONTI","central and cool for less",leaf=True)
    node(540,296,128,44,"TERMINI","convenience, eyes open",leaf=True)
    node(564,166,150,44,"TESTACCIO","eat where Rome eats",leaf=True)
    o.append(TX(20,26,"WHERE TO SLEEP, DECIDED IN FOUR QUESTIONS",9.5,"start",C["accent"],w=500))
    o.append(TX(20,H-14,"Prati answers a fifth question — calm, and the Vatican at your door — see the assessments  ●",7.5,"start",C["muted"]))
    o.append('</svg>'); return "".join(o)

# ── FIG · day trips on the rail-minutes axis ────────────────────────────────
def MAP_DAYTRIPS():
    W,H=660,320
    o=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">',frame(W,H)]
    ax0,ax1=120,624
    def X(m): return ax0+(ax1-ax0)*m/120
    for m in (30,60,90,120):
        x=X(m)
        o.append(f'<line x1="{x:.0f}" y1="52" x2="{x:.0f}" y2="{H-44}" stroke="{C["line_soft"]}" stroke-width="1"/>')
        o.append(TX(x,H-28,f"{m}′",8,"middle",C["muted"]))
    o.append(TX(ax1,H-14,"RAIL MINUTES, ONE WAY  ●/▲",7,"end",C["soft"]))
    rx,ry=ax0,166
    o.append(f'<rect x="{rx-34}" y="{ry-12}" width="34" height="24" fill="{C["ink"]}"/>')
    o.append(TX(rx-17,ry+3,"ROME",8,"middle",C["paper"],w=500))
    lanes=[("N",92,[("Orvieto",60,"hill town · funicular up","intercity"),("Florence",92,"possible · not advisable","high-speed")]),
           ("E",166,[("Tivoli",60,"two villas in one day","regional"),("Castelli Romani",40,"wine towns in the hills","regional")]),
           ("S",240,[("Ostia Antica",33,"the substitution play","metro-rail"),("Naples",70,"the blockbuster line","high-speed"),("Pompeii",110,"Naples + Circumvesuviana","chained")])]
    B=_Boxes()
    for dirn,y,stops in lanes:
        o.append(TX(ax0-58,y+3,dirn,10,"middle",C["soft"],w=500))
        o.append(f'<line x1="{rx}" y1="{ry}" x2="{ax0+18}" y2="{y}" stroke="{C["line"]}" stroke-width="1.2"/>')
        prev=ax0+18
        stops=sorted(stops,key=lambda s:s[1])
        for nm,m,sub,kind in stops:
            x=X(m)
            dash = ' stroke-dasharray="2 4"' if kind=="chained" else ""
            o.append(f'<line x1="{prev:.0f}" y1="{y}" x2="{x:.0f}" y2="{y}" stroke="{C["deep"]}" stroke-width="2.4"{dash}/>')
            o.append(f'<circle cx="{x:.0f}" cy="{y}" r="4.6" fill="{C["paper"]}" stroke="{C["accent"]}" stroke-width="2.4"/>')
            B.add(x-6,y-6,x+6,y+6)
            prev=x
        for nm,m,sub,kind in stops:
            x=X(m)
            xx,yy,anc=B.place(x,y-14,nm.upper(),9,"middle",
                              tries=[(0,0,"middle"),(0,-13,"middle"),(0,34,"middle"),(14,3,"start")])
            o.append(TX(xx,yy,nm.upper(),9,anc,C["ink"],w=500))
            xx2,yy2,anc2=B.place(x,y+22,sub,7,"middle",
                              tries=[(0,0,"middle"),(0,11,"middle"),(14,14,"start"),(0,-30,"middle")])
            o.append(TX(xx2,yy2,sub,7,anc2,C["muted"]))
    o.append(TX(20,26,"EVERY ESCAPE, PRICED IN MINUTES",9.5,"start",C["accent"],w=500))
    o.append(TX(20,40,"centre-to-centre by rail — the axis every day-trip argument stands on",7.5,"start",C["muted"]))
    o.append('</svg>'); return "".join(o)

# ── FIG · the day routes (numbered plate badges) ────────────────────────────
def _badge(o,x,y,n):
    o.append(f'<g transform="translate({x:.1f},{y:.1f}) rotate(45)">'
             f'<rect x="-7.5" y="-7.5" width="15" height="15" rx="2.5" fill="{C["accent"]}"/></g>')
    o.append(TX(x,y+3.2,str(n),8.5,"middle",C["paper"],w=500))

def MAP_DAY(n):
    routes={1:(["Colosseum","Forum","Capitoline","Pantheon","Navona","Trevi","Trastevere"],
               "DAY ONE — THE ANCIENT CORE, THEN THE CENTRE ON FOOT",(41.874,41.912,12.452,12.505)),
            2:(["Vatican Museums","St Peter's","Castel S. Angelo","Navona","Campo de' Fiori"],
               "DAY TWO — THE VATICAN, THEN BACK ACROSS THE RIVER",(41.882,41.916,12.440,12.492)),
            3:(["Borghese","Spanish Steps","Ghetto","Testaccio"],
               "DAY THREE — THE GALLERY, THEN THE CITY THAT EATS",(41.868,41.922,12.452,12.505))}
    stops,title,(la0,la1,lo0,lo1)=routes[n]
    W,H=660,208; P=Proj(la0,la1,lo0,lo1,W,H,16)
    o=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">',frame(W,H)]
    o.append(tiber_path(P,7))
    pts=[P.xy(*LM[k]) for k in stops]
    d="M "+" L ".join(f"{x:.1f} {y:.1f}" for x,y in pts)
    o.append(f'<path d="{d}" fill="none" stroke="{C["gilt"]}" stroke-width="2.2" stroke-dasharray="1 4" stroke-linecap="round"/>')
    B=_Boxes()
    for (x,y) in pts: B.add(x-9,y-9,x+9,y+9)
    for i,((x,y),k) in enumerate(zip(pts,stops),1):
        _badge(o,x,y,i)
        an="end" if x>W-100 else "start"; lx=x-12 if an=="end" else x+12
        xx,yy,anc=B.place(lx,y+3,k.upper(),8.5,an)
        o.append(TX(xx,yy,k.upper(),8.5,anc,C["ink"]))
    o.append(TX(20,24,title,9.5,"start",C["accent"],w=500))
    o.append('</svg>'); return "".join(o)

# ── geometry gate (strict, per d-draw) ──────────────────────────────────────
import re as _re
def geometry_gate(svg):
    W,H=[float(v) for v in _re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"',svg).groups()]
    bad=[]
    texts=[]
    for m in _re.finditer(r'<text x="([\d.-]+)" y="([\d.-]+)" text-anchor="(\w+)" style="[^"]*font-size:([\d.]+)px[^"]*">([^<]*)</text>',svg):
        x,y,an,fs,t=float(m[1]),float(m[2]),m[3],float(m[4]),m[5]
        w=len(t)*fs*0.58
        x0 = x if an=="start" else (x-w/2 if an=="middle" else x-w)
        texts.append((x0,y-fs*0.78,x0+w,y+fs*0.24,t))
        if x0< -1 or x0+w>W+1 or y-fs>H or y<0: bad.append(("outside",t))
    # Rects must sit inside the canvas — this is what let the Colosseum tiers run off both
    # edges. Markers are positioned by <g transform>, so resolve translate/rotate first.
    cur=(0.0,0.0,False); stack=[]
    tok=_re.finditer(r'<g transform="translate\(([-\d.]+),([-\d.]+)\)([^"]*)"|</g>'
                     r'|<rect x="([-\d.]+)" y="([-\d.]+)" width="([-\d.]+)" height="([-\d.]+)"', svg)
    for m in tok:
        if m.group(0).startswith("<g"):
            stack.append(cur); cur=(cur[0]+float(m[1]), cur[1]+float(m[2]), "rotate" in (m[3] or ""))
        elif m.group(0)=="</g>":
            cur = stack.pop() if stack else (0.0,0.0,False)
        else:
            rx,ry,rw,rh=[float(v) for v in m.groups()[3:7]]
            ox,oy,rot = cur
            if rot:   # rotated marker: bound it by its half-diagonal about its centre
                cx,cy = ox+rx+rw/2, oy+ry+rh/2; half=((rw*rw+rh*rh)**0.5)/2
                x0,y0,x1,y1 = cx-half,cy-half,cx+half,cy+half
            else:
                x0,y0,x1,y1 = ox+rx, oy+ry, ox+rx+rw, oy+ry+rh
            if x0< -1 or y0< -1 or x1>W+1 or y1>H+1:
                bad.append(("rect-outside", f"x{x0:.0f} y{y0:.0f} -> x{x1:.0f} y{y1:.0f}"))
    for m in _re.finditer(r'<circle cx="([\d.-]+)" cy="([\d.-]+)" r="([\d.]+)"',svg):
        cx,cy,cr=float(m[1]),float(m[2]),float(m[3])
        if cr>6: continue
        for (x0,y0,x1,y1,t) in texts:
            if x0<cx<x1 and y0<cy<y1: bad.append(("dot-in-glyph",t))
    return bad

# ── FIG · the cost stack — ordinal, never magnitudes (the Book prints no prices) ─
def GFX_LEAKS():
    W,H=660,250
    o=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">',frame(W,H)]
    rows=[("FLIGHTS","this book refuses to pull it","OUTSIDE THIS BOOK",0.94,C["soft"]),
          ("THE ROOM","set before you land","DECISIONS 01 · 03",0.80,C["accent"]),
          ("FOOD","the filter decides it","DECISION 10",0.58,C["deep"]),
          ("ADMISSIONS","fixed, and sold out early","DECISIONS 04 · 07–09",0.40,C["gilt"]),
          ("TRANSIT","the pass math never starts","DECISION 06",0.16,C["stone"])]
    x0,y=210,66; bh=26
    for name,sub,dec,frac,colr in rows:
        bw=(W-x0-150)*frac
        o.append(f'<rect x="{x0}" y="{y}" width="{bw:.0f}" height="{bh}" fill="{colr}" '
                 f'fill-opacity="0.85" stroke="{C["line"]}"/>')
        o.append(TX(x0-10,y+17,name,9.5,"end",C["ink"],w=500))
        o.append(TX(x0-10,y+27,sub,6.8,"end",C["muted"]))
        o.append(TX(x0+bw+8,y+17,dec,7.5,"start",C["deep"],w=500))
        y+=bh+13
    o.append(TX(20,26,"THE COST STACK",9.5,"start",C["accent"],w=500))
    o.append(TX(20,40,"spend your attention from the top down — the leaks live at the bottom, the levers at the top",
                7.5,"start",C["muted"]))
    o.append(f'<line x1="{x0}" y1="58" x2="{x0}" y2="{y-6}" stroke="{C["muted"]}" stroke-width="1"/>')
    o.append(TX(20,H-16,"SCHEMATIC · ORDER OF SIZE, NOT MAGNITUDE — this book prints no prices  ●",
                7.5,"start",C["soft"]))
    o.append('</svg>'); return "".join(o)
