# -*- coding: utf-8 -*-
"""render-affiche.py — compose the book in Marta Serra's hand, lift the Field Sheet
out (fssplit), paginate both with Paged.js after the fonts are ready, and write
dossier.pdf + fieldsheet.pdf, a page map (_pages-affiche.json), page PNGs under
_affiche/ and a contact sheet. No compositor passes: these pages are composed.

Usage: python3 render-affiche.py [--no-compose]
"""
import os, sys, glob, json, subprocess
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw
import pymupdf

BUILD = os.path.dirname(os.path.abspath(__file__)); os.chdir(BUILD)
sys.path.insert(0, BUILD)
import fssplit

if '--no-compose' not in sys.argv:
    subprocess.run([sys.executable, 'compose-affiche.py'], check=True)
doc = open('dossier3.html', encoding='utf-8').read()
got = fssplit.split(doc)
book, sheet, fsid = got if got else (doc, None, None)
# fssplit rewrites the contents row for the sheet with bare glyphs; every provenance
# glyph in running text must sit in the marks font, or Chromium falls back to a system face
import re as _re
def _wrap_marks(h):
    parts = _re.split(r'(<[^>]+>)', h); out = []; depth_mk = 0
    for part in parts:
        if part.startswith('<'):
            if _re.match(r'<i class="mk"', part): depth_mk += 1
            elif part == '</i>' and depth_mk: depth_mk -= 1
            out.append(part)
        else:
            out.append(part if depth_mk else _re.sub(r'([●◇▲◆◈])', r'<i class="mk">\1</i>', part))
    return ''.join(out)
def _wrap_doc(h):
    if '</style>' not in h: return _wrap_marks(h)
    head, body = h.split('</style>', 1); return head + '</style>' + _wrap_marks(body)
book = _wrap_doc(book)
if sheet: sheet = _wrap_doc(sheet)
INJECT = ('<script src="paged.polyfill.js"></script><script>window.PagedConfig={auto:false};'
          'window.addEventListener("load",function(){document.fonts.ready.then(function(){return window.PagedPolyfill.preview();})'
          '.then(function(f){window.__pagedDone=f.total;}).catch(function(e){window.__pagedErr=(e&&e.stack)?e.stack:String(e);});});</script>')
PAGEMAP = """() => [...document.querySelectorAll('.pagedjs_page')].map((pg, i) => {
  const r = pg.getBoundingClientRect();
  const sec = e => { const s = e.closest('section'); return s ? (s.dataset.id || s.id || s.dataset.ref || '') : ''; };
  const els = [...pg.querySelectorAll('.pagedjs_page_content section > *, .pagedjs_page_content .pg > *, .pagedjs_page_content > div > .poster, .pagedjs_page_content > div > .photo')].map(e => {
    const b = e.getBoundingClientRect();
    return {tag: e.tagName.toLowerCase(), cls: e.className || '', sec: sec(e), top: Math.round(b.top - r.top), bottom: Math.round(b.bottom - r.top), left: Math.round(b.left - r.left), right: Math.round(b.right - r.left)}; });
  return {page: i + 1, els}; })"""
CLIP = """() => [...document.querySelectorAll('.pagedjs_page .card, .pagedjs_page .days .d, .pagedjs_page .poster')].filter(e => e.scrollHeight > e.clientHeight + 2).map(e => e.className + ' ' + e.scrollHeight + '/' + e.clientHeight)"""

def paginate(html, name, pdf):
    open(name, 'w', encoding='utf-8').write(html.replace('</head>', INJECT + '</head>'))
    with sync_playwright() as p:
        b = p.chromium.launch(args=['--no-sandbox', '--font-render-hinting=none']); pg = b.new_page(viewport={'width': 816, 'height': 1056})
        pg.goto('file://' + os.path.join(BUILD, name), wait_until='load')
        pg.wait_for_function('window.__pagedDone !== undefined || window.__pagedErr !== undefined', timeout=600000)
        err = pg.evaluate('window.__pagedErr'); assert not err, err
        n = pg.evaluate('window.__pagedDone')
        # cross-references: Paged.js sets the anchor's attribute but never inserts the counter
        # rule in this build, so the page numbers are resolved here, after pagination
        xref = pg.evaluate("""() => { let done = 0, miss = []; document.querySelectorAll('a[href^="#"]').forEach(a => {
            const id = a.getAttribute('href').slice(1); const t = document.getElementById(id) || document.querySelector('[data-id="' + CSS.escape(id) + '"]');
            const page = t && t.closest('.pagedjs_page'); if (page) { a.dataset.page = page.dataset.pageNumber; done++; } else miss.push(id); });
            return {done, miss}; }""")
        print(f'  cross-references resolved: {xref["done"]}; unresolved: {xref["miss"]}')
        pages = pg.evaluate(PAGEMAP); clipped = pg.evaluate(CLIP)
        pg.pdf(path=pdf, print_background=True, prefer_css_page_size=True, display_header_footer=False, margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'})
        b.close()
    m = len(pymupdf.open(pdf)); assert m == n, (m, n)
    return n, pages, clipped

n, pages, clipped = paginate(book, '_render-affiche.html', 'dossier.pdf')
json.dump(pages, open('_pages-affiche.json', 'w'), indent=0)
# the full-sheet pages (posters, photograph pages): no furniture by design — the gates read this
full = sorted({pgm['page'] for pgm in pages if any(('poster' in e['cls'] or e['cls'].split()[0] == 'photo') for e in pgm['els'] if e['cls'])})
json.dump({'full_sheet_pages': full, 'why': 'posters and photograph pages in the Affiche hand carry no furniture, like the cover'}, open('_fullsheet.json', 'w'))
print(f'book: {n} pages -> dossier.pdf · {len(full)} full-sheet pages -> _fullsheet.json')
for c in clipped: print('  CLIPPED', c)
if sheet:
    ns, _, _ = paginate(sheet, '_render-affiche-sheet.html', 'fieldsheet.pdf'); print(f'field sheet: {ns} pages -> fieldsheet.pdf')

# page PNGs and the contact sheet
os.makedirs('_affiche', exist_ok=True)
for f in glob.glob('_affiche/p*.png'): os.remove(f)
d = pymupdf.open('dossier.pdf'); thumbs = []
for i, page in enumerate(d):
    pix = page.get_pixmap(dpi=100); pix.save(f'_affiche/p{i+1:02d}.png'); thumbs.append(Image.open(f'_affiche/p{i+1:02d}.png'))
W = 204; th = int(W * 11 / 8.5); cols = 8; rows = (len(thumbs) + cols - 1) // cols
sheet_img = Image.new('RGB', (cols * (W + 10) + 10, rows * (th + 24) + 10), '#3a3a3a'); dr = ImageDraw.Draw(sheet_img)
for i, t in enumerate(thumbs):
    x = 10 + (i % cols) * (W + 10); y = 10 + (i // cols) * (th + 24)
    sheet_img.paste(t.resize((W, th), Image.LANCZOS), (x, y)); dr.text((x, y + th + 6), f'p{i+1}', fill='white')
sheet_img.save('_affiche/contact.png')

# the page report: fill per page, chapter, kind
TOP, BOT = 92, 984
for pgm in pages:
    els = pgm['els']
    if not els: print(f'  p{pgm["page"]:02d} EMPTY'); continue
    full = any(('poster' in e['cls'] or 'photo' == e['cls'].split()[0]) for e in els if e['cls'])
    bottom = max(e['bottom'] for e in els); secs = sorted({e['sec'] for e in els if e['sec']})
    fill = 1.0 if full else (min(bottom, BOT) - TOP) / (BOT - TOP)
    flag = '' if (full or fill >= 0.6) else '   <<< under 60 %'
    print(f'  p{pgm["page"]:02d} {",".join(secs):18} {"poster/photo" if full else f"{fill:.0%}":12}{flag}')
