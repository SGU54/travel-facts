# -*- coding: utf-8 -*-
"""marta2.py — Marta Serra's Season II posters, for the book.

The posters are drawn in build/models/m9-marta-II/build.py (the specimen the owner
approved, 2026-10-25); this module lifts them into the book: their CSS scoped under
.m2 so it cannot touch the text pages, each poster wrapped as a full-sheet .poster
(the renderer and the gates read that class as a plate).
"""
import importlib.util, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location('m9', os.path.join(HERE, 'models', 'm9-marta-II', 'build.py'))
_cwd = os.getcwd(); os.chdir(os.path.join(HERE, 'models', 'm9-marta-II'))
m9 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(m9)
os.chdir(_cwd)

def _scope(css):
    out = []
    css = re.sub(r'@font-face\{[^}]*\}', '', css)
    css = re.sub(r'@page[^{]*\{(?:[^{}]|\{[^{}]*\})*\}', '', css)
    for sel, body in re.findall(r'([^{}]+)\{([^{}]*)\}', css):
        sel = sel.strip()
        if not sel or sel.startswith(('html', 'body', '.pagedjs', 'i.mk', '.rh-src', '@')): continue
        out.append(', '.join(('.m2' if x.strip().startswith('.sh') else '.m2 ') + x.strip() for x in sel.split(',') if x.strip()) + '{' + body + '}')
    return '\n'.join(out)

_raw = m9.POSTER_CSS.replace(m9.PAGE, '').replace(m9.MARKS, '')
CSS = _scope(_raw) + '''
.poster.m2{ padding:0 !important; display:block !important; }
.m2.sh{ break-after:auto; height:1055px; }
.m2 .verdict{ z-index:4; }
.poster.m2.cover2{ padding:0 !important; }
/* the sheet is 1055px (Paged.js rounding); a shadow of its own colour paints the last pixel row without counting as overflow */
.m2.sh.red{ box-shadow:0 3px 0 #A23520; } .m2.sh.gold{ box-shadow:0 3px 0 #E0A828; } .m2.sh.ink{ box-shadow:0 3px 0 #17201C; }   /* the verdict sits above every drawn element of the poster */
.m2 svg.bg{ height:1054px !important; }
'''

def has(sid): return sid in m9.POSTERS and sid != 'cover'

def cover():
    """The Season II cover: the Eixample grid, one block gold, the title on the sheet."""
    h = m9.POSTERS['cover']
    m = re.match(r'<div class="sh (\w+)">', h)
    return f'<div class="poster m2 sh {m.group(1)} cover2">' + h[m.end():].replace(m9.IMG, 'img/')

# the photograph that closes a decision, printed in the book's two inks with the verdict over it
WORD = {'d02': ('HOTEL', 230, 84), 'd03': ('4', 420, 110), 'd05': ('3', 420, 110), 'd06': ('2+1', 250, 118), 'd08': ('20:30', 200, 96)}
DUO_CSS = """
.photo.duo .dw{ position:relative; height:740px; overflow:hidden; }
.photo.duo .dw img{ height:740px; filter:grayscale(1) contrast(1.15) brightness(1.3); }
.photo.duo .dw .tone{ position:absolute; inset:0; background:#A23520; mix-blend-mode:multiply; }
.photo.duo .dw .lift{ position:absolute; inset:0; background:#3a140b; mix-blend-mode:screen; }
.photo.duo .dw .word{ position:absolute; left:52px; bottom:-8px; font-weight:800; line-height:.78; letter-spacing:-.05em; color:#E0A828; white-space:nowrap; }
"""

def poster(sid, kicker):
    """The poster IS the sheet: its own outer div becomes the book's .poster."""
    import html as H
    h = m9.POSTERS[sid]
    m = re.match(r'<div class="sh (\w+)">', h)
    shadow = ' style="box-shadow:0 3px 0 #17201C"' if sid == 'd07' else ''   # the mountain's ink runs to the foot
    return (f'<div class="poster m2 sh {m.group(1)}" id="{sid}-p"{shadow}><span class="rh-src">{H.escape(kicker, quote=False)}</span>'
            + h[m.end():].replace(m9.IMG, 'img/'))   # the specimen's image paths, from the book's folder

def faces():
    """Every (weight, stretch) the posters set, so the renderer can embed static instances."""
    got = set()
    for h in [m9.POSTER_CSS] + list(m9.POSTERS.values()):
        for m in re.finditer(r'font-stretch:(\d+)%', h):
            got.add((800, int(m.group(1))))
    return sorted(got)
