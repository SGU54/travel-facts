# illus.py — drawn illustrations. EXTENDS maps.C (bug log #10) — never redefines it.
from maps import C, TX, frame, MONO, DISP, BODY
C.update({"arena":"#D9C89F"})   # one derived tint, no new hue family

def ILLUS_SECTION():
    """The Colosseum in section — standard tiers, arena deck, hypogeum below.
    Geometry is bounded: tier stacks run inward from x=64 and x=596 on a 660 canvas."""
    W,H=660,272
    gy=178                      # ground / arena-deck line
    L0,R0=200,460               # inner edges of the two seating banks
    o=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">',frame(W,H)]

    # ── seating banks, stepped outward-and-up from the arena edge
    def tiers(x0,dirn):
        pts=[(x0+dirn*dx, gy+dy) for dx,dy in ((0,0),(34,-22),(68,-44),(102,-66),(136,-88))]
        for i in range(4):
            (ax,ay),(bx,by)=pts[i],pts[i+1]
            o.append(f'<rect x="{min(ax,bx)}" y="{by}" width="{abs(bx-ax)}" height="{ay-by}" '
                     f'fill="{C["stone"]}" stroke="{C["muted"]}" stroke-width="1"/>')
    tiers(L0,-1); tiers(R0,+1)

    # ── ground line + the arena deck: half reconstructed (gilt), half open (dashed)
    o.append(f'<line x1="30" y1="{gy}" x2="{W-30}" y2="{gy}" stroke="{C["ink"]}" stroke-width="1.6"/>')
    o.append(f'<line x1="{L0}" y1="{gy}" x2="330" y2="{gy}" stroke="{C["gilt"]}" stroke-width="5"/>')
    o.append(f'<line x1="330" y1="{gy}" x2="{R0}" y2="{gy}" stroke="{C["muted"]}" '
             f'stroke-width="1.2" stroke-dasharray="4 5"/>')

    # ── hypogeum: chambers under the arena, one lift shaft to a trapdoor
    hy0,hy1=gy+8,232
    for i in range(6):
        x=215+i*40
        o.append(f'<rect x="{x}" y="{hy0}" width="30" height="{hy1-hy0}" fill="{C["zone"]}" '
                 f'stroke="{C["muted"]}" stroke-width="1"/>')
    lx=330
    o.append(f'<rect x="{lx-9}" y="{hy0-8}" width="18" height="{hy1-hy0+8}" fill="{C["paper"]}" '
             f'stroke="{C["deep"]}" stroke-width="1.6"/>')
    o.append(f'<line x1="{lx}" y1="{hy0-8}" x2="{lx}" y2="{hy1-6}" stroke="{C["deep"]}" '
             f'stroke-width="1.2" stroke-dasharray="2 3"/>')
    o.append(f'<circle cx="{lx}" cy="{hy1-6}" r="4" fill="none" stroke="{C["deep"]}" stroke-width="1.6"/>')
    o.append(f'<path d="M {lx-6} {gy} h 12" stroke="{C["accent"]}" stroke-width="3"/>')   # trapdoor

    # ── the three zones, each bracketed to what it actually is
    o.append(f'<path d="M 70 84 v -12 h 124 v 12" fill="none" stroke="{C["accent"]}" stroke-width="1.4"/>')
    o.append(TX(132,54,"STANDARD TICKET",8.5,"middle",C["accent"],w=500))
    o.append(TX(132,65,"the tiers — looking down",7,"middle",C["muted"]))
    o.append(f'<path d="M {L0} 154 v -12 h {R0-L0} v 12" fill="none" stroke="{C["gilt"]}" stroke-width="1.4"/>')
    o.append(TX(330,124,"ARENA FLOOR",8.5,"middle",C["deep"],w=500))
    o.append(TX(330,135,"the gladiator's eye-line",7,"middle",C["muted"]))
    o.append(f'<path d="M 215 238 v 12 h 230 v -12" fill="none" stroke="{C["deep"]}" stroke-width="1.4"/>')
    o.append(TX(330,264,"UNDERGROUND · HYPOGEUM — cells, machinery, the lift shafts",8,"middle",C["deep"],w=500))

    o.append(TX(20,22,"ONE BUILDING, THREE TICKETS",9.5,"start",C["accent"],w=500))
    o.append(TX(20,36,"what the Full Experience adds is not a better view of the same thing — it is two other rooms",
                7.5,"start",C["muted"]))
    o.append(TX(W-28,gy+5,"GROUND",6.5,"end",C["soft"]))
    o.append(TX(20,266,"SCHEMATIC · NOT TO SCALE",7,"start",C["soft"]))
    o.append('</svg>'); return "".join(o)
