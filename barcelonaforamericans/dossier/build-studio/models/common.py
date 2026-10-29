# -*- coding: utf-8 -*-
"""common.py — what every model's builder shares: the two chapters as data,
paths, the map recolouring, the marks font. Builders run from their own dir."""
import json, re, html as H, os

HERE = os.path.dirname(os.path.abspath(__file__))
CH = json.load(open(os.path.join(HERE, 'chapters.json'), encoding='utf-8'))
IMG = '../../img/'          # model dir → build/img
FONTS = '../fonts/'         # model dir → models/fonts
HOUSE = '../../assets/fonts/'

PAGE = '''@page{ size:8.5in 11in; margin:92px 82px 72px 82px; }
html,body{ -webkit-print-color-adjust:exact; print-color-adjust:exact; margin:0; }
.rh-src{ string-set:rh content(text); display:block; height:0; overflow:hidden; font-size:0; line-height:0; margin:0; }
'''

MARKS = ("@font-face{font-family:'Symbols';src:url('%sNotoSansSymbols2-Regular.ttf');}"
         "i.mk{font-style:normal;font-family:'Symbols';font-size:.9em;}" % HOUSE)

def esc(s): return H.escape(s, quote=False)

def map_svg(colours, scale=1.0, fonts=None):
    """The d01 neighbourhood map, recoloured into a model's palette and with its
    labels scaled (the house map's 7.5px labels fall under the printed floor
    once the figure is set narrower than the sheet)."""
    svg = CH['d01']['figure_svg']
    for k, v in colours.items(): svg = svg.replace(k, v)
    if fonts:
        for k, v in fonts.items(): svg = svg.replace('font-family="%s"' % k, 'font-family="%s"' % v)
    if scale != 1.0:
        svg = re.sub(r'font-size="([\d.]+)"', lambda m: 'font-size="%.1f"' % (float(m.group(1)) * scale), svg)
    return svg

def photo(src):
    return IMG + os.path.basename(src)

def write(html, path='model.html'):
    open(path, 'w', encoding='utf-8').write(html)
    print('wrote', path, len(html), 'bytes')
