# -*- coding: utf-8 -*-
"""marta2.py — Marta Serra's Season II posters for *Rome, Solved.*

The posters are drawn in build-v2/models/m9-marta-II/build.py (the Rome specimen the owner
liked, 2026-10-25: the sampietrino as Rome's sign); this module lifts them into the book,
their CSS scoped under .m2, each poster the full sheet (the renderer and the gates read
.poster as a plate). Same engine rules as Barcelona: sheet 1055px, nothing past the trim,
a shadow of the sheet's colour paints the last pixel row.
"""
import importlib.util, os, re
import html as H
HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location('m9rome', os.path.join(HERE, 'models', 'm9-marta-II', 'build.py'))
_cwd = os.getcwd(); os.chdir(os.path.join(HERE, 'models', 'm9-marta-II'))
m9 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(m9)
os.chdir(_cwd)

RED, GOLD, INK, PAPER = m9.RED, m9.GOLD, m9.INK, m9.PAPER


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
CSS = _scope(_raw) + f'''
.poster.m2{{ padding:0 !important; display:block !important; }}
.m2.sh{{ break-after:auto; height:1055px; }}
.m2 svg.bg{{ height:1054px !important; }}
.m2 .verdict{{ z-index:4; }}
.m2.sh.red{{ box-shadow:0 3px 0 {RED}; }} .m2.sh.gold{{ box-shadow:0 3px 0 {GOLD}; }}
'''


def has(sid): return sid in m9.POSTERS and sid != 'cover'


def _wrap(h, cls, attrs=''):
    m = re.match(r'<div class="sh (\w+)">', h)
    return f'<div class="poster m2 sh {m.group(1)} {cls}"{attrs}>' + h[m.end():].replace(m9.IMG, 'img/')


def cover():
    return _wrap(m9.POSTERS['cover'], 'cover2')


def poster(sid, kicker):
    h = m9.POSTERS[sid]
    m = re.match(r'<div class="sh (\w+)">', h)
    return (f'<div class="poster m2 sh {m.group(1)}" id="{sid}-p"><span class="rh-src">{H.escape(kicker, quote=False)}</span>'
            + h[m.end():].replace(m9.IMG, 'img/'))


# the decision's closing photograph in the book's two inks, its verdict overprinted in gold
WORD = {'d01': ('13′', 300, 110), 'd02': ('TAP.', 230, 100), 'd03': ('€55', 260, 104), 'd04': ('½', 330, 110),
        'd05': ('TWO LINES.', 118, 96), 'd06': ('3', 420, 110), 'd07': ('€', 420, 100), 'd08': ('90″', 260, 104), 'd09': ('OSTIA', 230, 86)}
DUO_CSS = f"""
.photo.duo .dw{{ position:relative; height:740px; overflow:hidden; }}
.photo.duo .dw img{{ height:740px; filter:grayscale(1) contrast(1.15) brightness(1.3); }}
.photo.duo .dw .tone{{ position:absolute; inset:0; background:{RED}; mix-blend-mode:multiply; }}
.photo.duo .dw .lift{{ position:absolute; inset:0; background:#34160d; mix-blend-mode:screen; }}
.photo.duo .dw .word{{ position:absolute; left:52px; bottom:-8px; font-weight:800; line-height:.78; letter-spacing:-.05em; color:{GOLD}; white-space:nowrap; word-spacing:.18em; }}
"""
