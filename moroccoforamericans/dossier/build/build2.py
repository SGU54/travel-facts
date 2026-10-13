#!/usr/bin/env python3
"""build2.py — assemble the 4-part manuscript into the paginated HTML."""
import re

SRC = '../dossier-mar/manuscript.md'

SMALL = {'a','an','and','the','or','of','in','on','to','for','with','at','by','from','as','but','nor','if'}

def smart_title(t):
    words = t.split()
    out = []
    for i, w in enumerate(words):
        core = w.lower()
        if i and i != len(words) - 1 and core in SMALL:
            out.append(core)
        elif "'" in w:                      # WON'T -> Won't, not Won'T
            head, _, tail = w.partition("'")
            out.append(head.capitalize() + "'" + tail.lower())
        else:
            out.append(w.capitalize())
    return ' '.join(out)

def inl(s):
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', s)
    return s

def table(md):
    lines = [l for l in md.strip().split('\n') if l.strip().startswith('|')]
    if len(lines) < 2:
        return ''
    head = [c.strip() for c in lines[0].strip('|').split('|')]
    rows = [[inl(c.strip()) for c in l.strip('|').split('|')] for l in lines[2:]]
    h = '<tr>' + ''.join(f'<th>{c}</th>' for c in head) + '</tr>'
    r = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in row) + '</tr>' for row in rows)
    return f'<table>{h}{r}</table>'

# visuals: chapter-title keyword -> (kind, src, height, caption)
VIS = {
    'THE GROUND':   ('photo', 'img/closing.jpg', '2.2in', 'Jemaa el-Fnaa after dark. Nothing here is hidden, which is why it works.'),
    '01 · MONEY':   ('map',   'fig4-moneyweb.svg', None,   'The four leaks, and where they meet. Each is legal; each is a default you refuse.'),
    'WHEN TO GO':   ('map',   'fig3-year.svg',   None,     'The year on the classic loop. April, May, October, November are the sweet spot.'),
    'THE HORIZONS': ('map',   'fig5-horizons.svg', None,   'The booking calendar, earliest first. Almost nothing needs booking far ahead.'),
    'THE THIRD PLACE': ('map','fig6-third.svg',  None,     'Where each option sits against the classic loop, to true scale.'),
    '05 · TRANSPORT': ('map', 'fig7-transport.svg', None,  'Three tools, three jobs. The train stops where the rail line stops.'),
    '03 · SEQUENCE':('map',   'fig1-route.svg',  None,     'The open-jaw line: arrive Marrakech, depart Fez, desert in the middle.'),
    '04 · DESERT':  ('map',   'fig2-desert.svg', None,     'Merzouga versus Zagora, drawn to true scale. The drive is the real cost.'),
    'MARRAKECH':    ('photo', 'img/ground.jpg',  '2.2in', 'The souks by daylight: the anchor price lives here, and so does the pleasure.'),
    'FEZ':          ('photo', 'img/medina.jpg',  '3.3in',  'The Chouara tanneries from a shop terrace: the view, and the sales route.'),
    'CLOSING':      ('photo', 'img/desert.jpg',  '2.2in', 'The camp at Erg Chebbi. Everything you came for, past a little preparation.'),
    '08 · SAFETY':  ('map',   'fig8-risk.svg',  None,     'Frequency, not severity: where the risk in Morocco actually sits.'),
    '07 · EATING':  ('photo', 'img/eating.jpg',  '2.2in', 'A tagine, slow-cooked. The pleasure is real; the tax on it is optional.'),
}

FIG = [0]

def visual_for(title):
    t = title.upper().strip()
    for k, v in VIS.items():
        # exact-key match on the chapter's leading token, never a loose substring
        ok = t == k or t.startswith(k + ' —') or t.startswith(k + ' ·') or t.startswith(k + ',')
        if not ok and k.startswith(('0',)):
            ok = t.startswith(k)
        if ok:
            FIG[0] += 1
            if v[0] == 'map':
                return (f'<figure class="map"><img src="{v[1]}">'
                        f'<figcaption>FIG. {FIG[0]} · {v[3]}</figcaption></figure>')
            cls = 'photo tall' if v[2] == '3.3in' else 'photo'
            return (f'<figure class="{cls}"><img src="{v[1]}" style="height:{v[2]}">'
                    f'<figcaption>FIG. {FIG[0]} · {v[3]}</figcaption></figure>')
    return ''

def chapter(title, body, idx, is_decision):
    sid = 'c%02d' % idx
    eyebrow = ''
    m = re.match(r'^(\d+)\s*·\s*([A-Z][A-Z &]*)\s*—\s*(.+)$', title)
    if m:
        eyebrow = f'Decision {m.group(1)} · {m.group(2).strip().title()}'
        disp = m.group(3).strip()
    else:
        parts = title.split('—', 1)
        eyebrow = parts[0].strip().title()
        disp = parts[1].strip() if len(parts) > 1 else parts[0].strip()
        if disp.isupper() or disp == disp.upper():
            disp = smart_title(disp)

    cls = 'dec chap' + (' decision' if is_decision else ' essay')
    out = [f'<section class="{cls}" id="{sid}" data-ref="{sid}">']
    dnum = m.group(1) if (is_decision and m) else None
    opcls = 'opener' if is_decision else 'opener essayop'
    out.append(f'<div class="{opcls}">')
    if dnum:
        out.append(f'<div class="onum">{dnum}</div>')
    out.append(f'<p class="okind">{eyebrow}</p>')
    out.append(f'<h1>{inl(disp)}</h1>')
    out.append('<div class="orule"></div></div>')
    open_pack_at = len(out)   # the lead paragraph is spliced in here later
    out.append(f'<span class="rh-src">{inl(disp)}</span>')
    pos = f'Decision {dnum} of 08' if dnum else eyebrow
    out.append(f'<span class="pos-src">{pos}</span>')

    mc = re.search(r'^\*\*cols:\*\*\s*(.+)$', body, flags=re.M)
    cols_caption = mc.group(1).strip() if mc else None
    body = re.sub(r'^\*\*cols:\*\*.*\n?', '', body, flags=re.M)
    blocks = re.split(r'\n\n+', body.strip())
    placed = False
    for i, b in enumerate(blocks):
        b = b.strip()
        if not b:
            continue
        if b.startswith('|'):
            tb = table(b)
            if is_decision or 'OPTION' in b.upper() or 'THE MOVE' in b.upper() or 'THE RULE' in b.upper():
                cap = cols_caption or 'The trade-off, scored'
                tb = f'<div class="ledger"><p class="lcap">{cap}</p>{tb}</div>'
            out.append(tb)
            if not placed:
                v = visual_for(title)
                if v:
                    out.append(v)
                    placed = True
            continue
        mb=re.match(r'^\*\*(.+?)\*\*\s*\n((?:- .+\n?)+)$', b)
        if mb:
            out.append(f'<h3 class="fmhead">{inl(mb.group(1))}</h3>')
            out.append(''.join(f'<p class="bullet">{inl(li[2:].strip())}</p>'
                               for li in mb.group(2).split('\n') if li.strip().startswith('- ')))
            continue
        if b.startswith('- '):
            out.append(''.join(f'<p class="bullet">{inl(li[2:].strip())}</p>'
                               for li in b.split('\n') if li.strip().startswith('- ')))
            continue
        if re.match(r'^\*\*(for|against)\*\*', b):
            cells = []
            for line in b.split('\n**'):
                line = line if line.startswith('**') else '**' + line
                mm = re.match(r'\*\*(for|against)\*\*\s*—\s*(.+)', line, re.S)
                if mm:
                    k = mm.group(1)
                    lbl = 'When the other call is right' if k == 'for' else 'When ours is wrong'
                    cells.append(f'<div class="fork {k[0]}"><b>{lbl}</b><p>{inl(mm.group(2).strip())}</p></div>')
            if cells:
                out.append('<div class="forks">' + ''.join(cells) + '</div>')
            continue
        if b.startswith('◆') or b.startswith('*No field-sheet'):
            out.append(f'<p class="note">{inl(b.strip("*"))}</p>')
            continue
        if b.startswith('**') and b.rstrip().endswith('**') and len(b) < 90:
            out.append(f'<h2>{inl(b.strip("*"))}</h2>')
            continue
        mm = re.match(r'^\*\*(The reasoning|The call|The four leaks[^*]*|The trade-off[^*]*|The shapes[^*]*|The tools[^*]*|The distinction[^*]*|The rules[^*]*|The calibration[^*]*)\.?\*\*\s*(.*)$', b, re.S)
        if mm:
            lab = mm.group(1).strip()
            if lab.lower() == 'the call':
                body_txt = inl(mm.group(2).strip())
                out.append(f'<div class="verdict"><p class="vlab">The call</p><p>{body_txt}</p></div>')
            else:
                out.append(f'<h2>{lab}</h2>')
                if mm.group(2).strip():
                    out.append(f'<p>{inl(mm.group(2).strip())}</p>')
            continue
        if b.startswith('*') and b.endswith('*'):
            out.append(f'<p class="aside">{inl(b.strip("*"))}</p>')
            continue
        lead = ' class="lead"' if i == 0 else ''
        out.append(f'<p{lead}>{inl(b)}</p>')
    if not placed:
        v = visual_for(title)
        if v:
            out.append(v)
    # OPENER PACK — an opener must never sit alone at the foot of a page.
    # Bind it to the first prose block (and a ledger if that comes first) so
    # the pair moves together; Paged.js honours break-inside far more
    # reliably than break-after.
    try:
        op_i = next(i for i, x in enumerate(out) if x.startswith('<div class="opener'))
        end_i, acc = None, 0
        for j in range(op_i + 1, len(out)):
            if out[j].startswith(('<p class="lead"', '<p>', '<div class="ledger"',
                                  '<h2', '<div class="verdict"')):
                acc += len(re.sub(r'<[^>]+>', ' ', out[j]).split())
                end_i = j
                if acc >= 55:      # the pack must carry real body, not one line
                    break
        if end_i is not None and end_i - op_i <= 9:
            pack = out[op_i:end_i + 1]
            out[op_i:end_i + 1] = ['<div class="openpack">' + ''.join(pack) + '</div>']
    except StopIteration:
        pass
    out.append('</section>')
    return '\n'.join(out)

# ---- parse manuscript ----
raw = open(SRC).read()
FOOT = {'PART ONE': 'None of this is hard. All of it is easier decided at a desk than at a gate.', 'PART TWO': 'Each one shows its arithmetic. Disagree with the verdict and you can still use the ledger.', 'PART THREE': 'Places treated as set pieces: what to do first, and in which order.', 'PART FOUR': 'The hour you land, the habits that travel well, and the calendar behind it all.'}
PART_TITLES = {
    'PART ONE': ('Part One', 'Before you go', 'What to settle, when to go, and what it costs.',
        [('Before you fly', 'Entry, health, connectivity, and packing for a country that gets cold.'),
         ('When to go', 'Four real seasons, a regional summer, and what Ramadan actually changes.')]),
    'PART TWO': ('Part Two', 'The eight decisions', 'The calls that set the shape of the trip, in the order you meet them.',
        [('01 · Money', 'The four leaks, joined — the connection the free articles never make.'),
         ('02 · Base', 'Not a base but an axis: Marrakech to Fez, and why it matters.'),
         ('03 · Sequence', 'Seven days, and the open-jaw ticket most people miss.'),
         ('04 · Desert', 'Merzouga or Zagora — and when the honest answer is neither.'),
         ('05 · Transport', 'Which tool for which leg, and where the train simply stops.'),
         ('06 · Guides', 'One question sorts the licensed guide from the tout.'),
         ('07 · Eating', 'The queue is the review that matters.'),
         ('08 · Safety', 'The risk is your wallet, not your person — recalibrate.')]),
    'PART THREE': ('Part Three', 'The places', 'Marrakech, Fez, and the one more thing — as set pieces, in order.',
        [('Marrakech', 'Jemaa el-Fnaa from above then within, and the monument loop.'),
         ('Fez', 'The guided first morning, the tanneries, and the terrace fee.'),
         ('The third place', 'Chefchaouen, Essaouira, the Atlas — or nothing at all.')]),
    'PART FOUR': ('Part Four', 'On the ground', 'The first three hours, the customs that matter, and what to book when.',
        [('Day zero', 'The airport hour, written out in the order it happens.'),
         ('The customs that matter', 'Dress, the right hand, and the hammam worth doing once.'),
         ('The horizons', 'The whole booking calendar on one page.')]),
}

pieces = re.split(r'\n# (?=[A-Z])', '\n' + raw)
flow, fs_html = [], ''
idx = 0
for piece in pieces:
    if not piece.strip():
        continue
    head = piece.split('\n')[0].strip()
    body = piece[len(head):]

    if head.startswith('THE FIELD SHEET'):
        fs = ['<div class="flow fs"><section class="dec chap essay" id="fsheet" data-ref="fsheet">',
              '<p class="eyebrow">Dated annex</p><h1>The Field Sheet</h1><span class="rh-src">The Field Sheet</span>']
        for b in re.split(r'\n\n+', body.strip()):
            b = b.strip()
            if not b:
                continue
            if b.startswith('*') and b.endswith('*'):
                fs.append(f'<p class="note">{inl(b.strip("*"))}</p>'); continue
            m2 = re.match(r'^\*\*(.+?)\*\*\s*([◆●◇]?)\s*(.*)$', b, re.S)
            if m2:
                fs.append(f'<h2>{inl(m2.group(1))} {m2.group(2)}</h2>')
                for li in m2.group(3).split('\n'):
                    li = li.strip().lstrip('-').strip()
                    if li:
                        fs.append(f'<p class="fsrow">{inl(li)}</p>')
                continue
            fs.append(f'<p class="fsrow">{inl(b)}</p>')
        fs.append('</section></div>')
        fs_html = '\n'.join(fs)
        continue

    key = next((k for k in PART_TITLES if head.startswith(k)), None)
    if key:
        n, t, sub, toc = PART_TITLES[key]
        rows = ''.join(f'<p class="ptoc"><b>{c[0]}</b><span>{c[1]}</span></p>' for c in toc)
        flow.append(f'<section class="partdiv"><p class="pnum">{n}</p>'
                    f'<h1 class="ptitle">{t}</h1><span class="rh-src">{t}</span><p class="psub">{sub}</p>'
                    f'<div class="ptocwrap">{rows}</div>'
                    f'<p class="pfoot">{FOOT.get(key,"")}</p></section>')

    for cm in re.finditer(r'\n## (.+?)\n(.*?)(?=\n## |\Z)', body, re.S):
        idx += 1
        title = cm.group(1).strip()
        is_dec = bool(re.match(r'^\d+\s*·', title))
        flow.append(chapter(title, cm.group(2), idx, is_dec))

cover = '''<div class="coverpage">
<img class="bg" src="img/cover.jpg"><div class="scrim"></div>
<div class="ct"><p class="kick">A decision manual · Morocco for Americans</p>
<h1 class="cover">Morocco,<br>Without<br>the Traps.</h1>
<p class="sub">The connections the free guides never make.</p></div>
<div class="foot">2026 edition · written &amp; checked for US travelers</div></div>'''

html = ('<!doctype html><html><head><meta charset="utf-8">\n<style>\n'
        "@font-face{font-family:'Fraunces';src:url('assets/fonts/Fraunces.ttf');font-weight:100 900;}\n"
        "@font-face{font-family:'Newsreader';src:url('assets/fonts/Newsreader.ttf');font-weight:100 900;}\n"
        "@font-face{font-family:'IBM Plex Mono';src:url('assets/fonts/IBMPlexMono.ttf');}\n"
        '</style>\n<style>\n' + open('dossier.css').read() + '\n</style>\n</head><body>\n'
        + cover + '\n<div class="flow">' + '\n'.join(flow) + '</div>\n' + fs_html + '\n</body></html>')

open('dossier3.html', 'w').write(html)
print(f"chapters: {idx} · figures: {FIG[0]} · {len(html)} bytes")
