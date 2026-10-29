# -*- coding: utf-8 -*-
"""render-model.py <model-dir> — paginate one hand-composed model with Paged.js,
write model.pdf, page PNGs and a contact sheet. No compositor passes: the
maquettiste composed these pages by hand and they render as composed."""
import os, sys, glob, json
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw
import pymupdf
D = os.path.abspath(sys.argv[1]); os.chdir(D)
HERE = os.path.dirname(os.path.abspath(__file__))
INJECT = ('<script src="../../paged.polyfill.js"></script>'
  '<script>window.PagedConfig={auto:false};'
  'window.addEventListener("load",function(){document.fonts.ready.then(function(){return window.PagedPolyfill.preview();}).then(function(f){window.__pagedDone=f.total;})'
  '.catch(function(e){window.__pagedErr=(e&&e.stack)?e.stack:String(e);});});</script>')
html = open('model.html', encoding='utf-8').read().replace('</head>', INJECT + '</head>')
open('_render.html', 'w', encoding='utf-8').write(html)
exe = glob.glob(os.path.expanduser('~/Library/Caches/ms-playwright/chromium-*/chrome-mac/Chromium.app/Contents/MacOS/Chromium'))
with sync_playwright() as p:
    kw = {'args': ['--no-sandbox', '--font-render-hinting=none']}
    if exe: kw['executable_path'] = exe[0]
    b = p.chromium.launch(**kw); pg = b.new_page(viewport={'width': 816, 'height': 1056})
    pg.goto('file://' + os.path.join(D, '_render.html'), wait_until='load')
    pg.wait_for_function('window.__pagedDone !== undefined || window.__pagedErr !== undefined', timeout=120000)
    err = pg.evaluate('window.__pagedErr'); assert not err, err
    n = pg.evaluate('window.__pagedDone')
    pages = pg.evaluate("""() => [...document.querySelectorAll('.pagedjs_page')].map((pg,i)=>{const r=pg.getBoundingClientRect();
      const els=[...pg.querySelectorAll('.pagedjs_page_content > div > *, .pagedjs_page_content section > *')].map(e=>{const b=e.getBoundingClientRect();
      return {tag:e.tagName.toLowerCase(),cls:e.className||'',top:Math.round(b.top-r.top),bottom:Math.round(b.bottom-r.top),left:Math.round(b.left-r.left),right:Math.round(b.right-r.left)}});return {page:i+1,els}})""")
    json.dump(pages, open('_pages.json', 'w'), indent=0)
    clipped = pg.evaluate("() => [...document.querySelectorAll('.pagedjs_page .t, .pagedjs_page .side, .pagedjs_page .call, .pagedjs_page .stack > .t')].filter(e => e.scrollHeight > e.clientHeight + 2).map(e => e.className + ' ' + e.scrollHeight + '/' + e.clientHeight + ' «' + (e.textContent || '').trim().slice(0, 40) + '»')")
    for c in clipped: print('  CLIPPED', c)
    pg.pdf(path='model.pdf', print_background=True, prefer_css_page_size=True, display_header_footer=False,
           margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'})
    b.close()
doc = pymupdf.open('model.pdf'); assert len(doc) == n, (len(doc), n)
for f in glob.glob('p*.png'): os.remove(f)
thumbs = []
for i, page in enumerate(doc):
    pix = page.get_pixmap(dpi=110); pix.save(f'p{i+1:02d}.png'); thumbs.append(Image.open(f'p{i+1:02d}.png'))
W = 340; cols = min(len(thumbs), 4); rows = (len(thumbs) + cols - 1) // cols
th = int(W * 11 / 8.5)
sheet = Image.new('RGB', (cols * (W + 16) + 16, rows * (th + 30) + 16), '#444'); dr = ImageDraw.Draw(sheet)
for i, t in enumerate(thumbs):
    t = t.resize((W, th), Image.LANCZOS); x = 16 + (i % cols) * (W + 16); y = 16 + (i // cols) * (th + 30)
    sheet.paste(t, (x, y)); dr.text((x, y + th + 8), f'p{i+1}', fill='white')
sheet.save('contact.png')
print(f'{os.path.basename(D)}: {n} pages -> model.pdf, contact.png')
for pgm in pages:
    els = pgm['els']
    if not els: print(f'  p{pgm["page"]}: empty'); continue
    bottom = max(e['bottom'] for e in els); print(f'  p{pgm["page"]}: {len(els)} els, bottom {bottom}px')
