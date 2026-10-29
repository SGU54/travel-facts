# -*- coding: utf-8 -*-
"""render-affiche.py — compose the Rome book in Marta Serra's hand (Season II) — adapted from render-edition.py, lift the Field
Sheet out (fssplit), paginate with Paged.js after the fonts are ready, resolve the
cross-reference page numbers, run the FIGURE TEXT WHOLE check, write dossier.pdf +
fieldsheet.pdf, the page map, bookmarks, page PNGs, the contact sheet, and a large
capture of every figure for the Eye (_affiche/figures/).

Figure text whole (atelier/references/gates.md): every <text> of every figure must lie
inside its figure's frame and inside the page body, and no line, dot or other label
may cross it. Measured on the paginated DOM: text boxes against the svg box, against
each other, and against points sampled every 1.5px along every stroked path.

Usage: python3 render-edition.py [--no-compose]
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
# The figure labels' paper halo was a stroked text (paint-order: stroke), which Chromium embeds as Type3.
# Before pagination, each label gets a paper chip (a rect from its own bbox) behind it and loses the stroke:
# same masking of the lines that pass under it, a real TrueType face in the PDF (2026-10-25).
CHIPS = ('function __chips(){document.querySelectorAll("figure.fig svg text").forEach(function(t){try{if(t.hasAttribute("data-nochip"))return;var b=t.getBBox();if(!b.width)return;'
         'var r=document.createElementNS("http://www.w3.org/2000/svg","rect");r.setAttribute("x",b.x-1.5);r.setAttribute("y",b.y+b.height*0.12);'
         'r.setAttribute("width",b.width+3);r.setAttribute("height",b.height*0.78);r.setAttribute("fill","#EFE4CC");r.setAttribute("class","chip");'
         't.parentNode.insertBefore(r,t);t.style.stroke="none";t.style.paintOrder="normal";t.style.strokeWidth="0";}catch(e){}});}')
INJECT = ('<script src="paged.polyfill.js"></script><script>window.PagedConfig={auto:false};' + CHIPS +
          'window.addEventListener("load",function(){document.fonts.ready.then(function(){return window.PagedPolyfill.preview();})'
          '.then(function(f){__chips();window.__pagedDone=f.total;}).catch(function(e){window.__pagedErr=(e&&e.stack)?e.stack:String(e);});});</script>')
PAGEMAP = """() => [...document.querySelectorAll('.pagedjs_page')].map((pg, i) => {
  const r = pg.getBoundingClientRect();
  const sec = e => { const s = e.closest('section'); return s ? (s.dataset.id || s.id || s.dataset.ref || '') : ''; };
  const els = [...pg.querySelectorAll('.pagedjs_page_content section > *, .pagedjs_page_content .pg > *, .pagedjs_page_content .body2 > *, .pagedjs_page_content figure.fig')].map(e => {
    const b = e.getBoundingClientRect();
    return {tag: e.tagName.toLowerCase(), cls: e.className || '', sec: sec(e), fig: e.dataset.fig || '', top: Math.round(b.top - r.top), bottom: Math.round(b.bottom - r.top), left: Math.round(b.left - r.left), right: Math.round(b.right - r.left)}; });
  return {page: i + 1, els}; })"""
FIGCHECK = """() => {
  const out = [];
  document.querySelectorAll('.pagedjs_page').forEach((pg, pi) => {
    const pr = pg.getBoundingClientRect();
    pg.querySelectorAll('figure.fig svg').forEach(svg => {
      const fr = svg.getBoundingClientRect(); const fid = svg.id || '?';
      // the glyph box, not the line box: Chromium's text rect carries the face's ascent and descent,
      // so two stacked labels touch before their letters do. Shrink to the em core.
      const texts = [...svg.querySelectorAll('text')].map(t => { const b = t.getBoundingClientRect(); const dy = b.height * 0.2; return {el: t, s: t.textContent.trim(), x0: b.left + 1, y0: b.top + dy, x1: b.right - 1, y1: b.bottom - dy, halo: /stroke/.test(getComputedStyle(t).paintOrder) || (t.previousElementSibling && t.previousElementSibling.getAttribute('class') === 'chip')}; });
      const body = {x0: pr.left + 82, y0: pr.top + 92, x1: pr.left + 816 - 82, y1: pr.top + 1056 - 72};
      const hit = (a, b, pad) => !(a.x1 + pad < b.x0 || a.x0 - pad > b.x1 || a.y1 + pad < b.y0 || a.y0 - pad > b.y1);
      texts.forEach(t => {
        if (t.x0 < fr.left - .5 || t.x1 > fr.right + .5 || t.y0 < fr.top - .5 || t.y1 > fr.bottom + .5) out.push({page: pi + 1, fig: fid, text: t.s, why: 'outside the figure frame'});
        if (t.x0 < body.x0 - .5 || t.x1 > body.x1 + .5 || t.y0 < body.y0 - .5 || t.y1 > body.y1 + .5) out.push({page: pi + 1, fig: fid, text: t.s, why: 'outside the page body'});
      });
      for (let i = 0; i < texts.length; i++) for (let j = i + 1; j < texts.length; j++)
        if (hit(texts[i], texts[j], -0.5)) out.push({page: pi + 1, fig: fid, text: texts[i].s, why: 'crossed by the label «' + texts[j].s + '»'});
      // stroked paths, lines and small filled markers, sampled along their length
      svg.querySelectorAll('path, line, polyline, circle').forEach(p => {
        const st = p.getAttribute('stroke'), fill = p.getAttribute('fill'); const role = p.dataset.role || '';
        const bb = p.getBoundingClientRect(); const small = bb.width < 9 && bb.height < 9;
        if (!(st && st !== 'none') && !small) return;        // a filled area is a ground, not a crossing
        if (bb.width > 400 && bb.height > 200 && !(st && st !== 'none')) return;
        let pts = [];
        try {
          const L = p.getTotalLength ? p.getTotalLength() : 0; const m = p.getScreenCTM();
          if (small) { pts = [{x: bb.left + bb.width / 2, y: bb.top + bb.height / 2}]; }
          else if (L && m) { for (let d = 0; d <= L; d += 1.5) { const q = p.getPointAtLength(d); pts.push({x: q.x * m.a + q.y * m.c + m.e, y: q.x * m.b + q.y * m.d + m.f}); } }
        } catch (e) { return; }
        texts.forEach(t => {
          if (pts.some(q => q.x >= t.x0 - 0.5 && q.x <= t.x1 + 0.5 && q.y >= t.y0 - 0.5 && q.y <= t.y1 + 0.5)) {
            // a line that only touches the label's own marker edge is still a crossing: report it
            out.push({page: pi + 1, fig: fid, text: t.s, why: (small ? 'a dot sits on the label' : 'a line crosses the label') + (t.halo && !small ? ' (hidden by the paper halo)' : '')});
          }
        });
      });
    });
  });
  // dedupe
  const seen = new Set(); return out.filter(o => { const k = o.page + '|' + o.fig + '|' + o.text + '|' + o.why; if (seen.has(k)) return false; seen.add(k); return true; });
}"""
XREF = """() => { let done = 0, miss = []; document.querySelectorAll('a[href^="#"]').forEach(a => {
  const id = a.getAttribute('href').slice(1); const t = document.getElementById(id) || document.querySelector('[data-id="' + CSS.escape(id) + '"]');
  const page = t && t.closest('.pagedjs_page'); const n = a.querySelector('.n') || a; if (page) { n.dataset.page = page.dataset.pageNumber; done++; } else miss.push(id); });
  return {done, miss}; }"""

def paginate(html, name, pdf, check=True):
    open(name, 'w', encoding='utf-8').write(html.replace('</head>', INJECT + '</head>'))
    with sync_playwright() as p:
        b = p.chromium.launch(args=['--no-sandbox', '--font-render-hinting=none']); pg = b.new_page(viewport={'width': 816, 'height': 1056})
        pg.goto('file://' + os.path.join(BUILD, name), wait_until='load')
        pg.wait_for_function('window.__pagedDone !== undefined || window.__pagedErr !== undefined', timeout=240000 if check else 120000)
        err = pg.evaluate('window.__pagedErr'); assert not err, err
        n = pg.evaluate('window.__pagedDone')
        xref = pg.evaluate(XREF); print(f'  cross-references resolved: {xref["done"]}; unresolved: {xref["miss"]}')
        pages = pg.evaluate(PAGEMAP); figs = pg.evaluate(FIGCHECK) if check else []
        pg.pdf(path=pdf, print_background=True, prefer_css_page_size=True, display_header_footer=False, margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'})
        b.close()
    m = len(pymupdf.open(pdf)); assert m == n, (m, n)
    return n, pages, figs

n, pages, figs = paginate(book, '_render-affiche.html', 'dossier.pdf')
json.dump(pages, open('_pages-affiche.json', 'w'), indent=0)
full = sorted({pgm['page'] for pgm in pages if any(('poster' in e['cls'].split() or e['cls'].split()[:1] == ['photo']) for e in pgm['els'] if e['cls'])})
json.dump({'full_sheet_pages': full, 'why': 'posters, the cover and photograph pages in the Affiche hand carry no furniture by design'}, open('_fullsheet.json', 'w'))
# bookmarks: every section's first page, titled from its heading
try:
    toc = []; seen = set()
    titles = {}
    import re as _re
    for m in _re.finditer(r'<section class="chap[^"]*" id="([^"]+)">(.*?)</section>', book, _re.S):
        sid, body = m.group(1), m.group(2)
        t = _re.search(r'<h1[^>]*>(.*?)</h1>', body, _re.S) or _re.search(r'<span class="rh-src">(.*?)</span>', body, _re.S)
        titles[sid] = _re.sub(r'<[^>]+>', '', t.group(1)).strip() if t else sid
    titles['cover'] = 'Cover'
    for pgm in pages:
        for e in pgm['els']:
            sid = e.get('sec')
            if sid and sid not in seen and sid in titles:
                seen.add(sid); toc.append([1 if not sid.startswith('d0') else 2, titles[sid], pgm['page']])
    dd = pymupdf.open('dossier.pdf'); dd.set_toc(toc); dd.saveIncr(); dd.close(); print(f'  bookmarks: {len(toc)}')
except Exception as ex: print('  bookmarks FAILED', ex)
print(f'book: {n} pages -> dossier.pdf · {len(full)} opener/cover pages -> _fullsheet.json')
json.dump(figs, open('_figure-text.json', 'w'), indent=1, ensure_ascii=False)
hard = [f for f in figs if 'hidden by the paper halo' not in f['why']]; soft = [f for f in figs if f not in hard]
if hard:
    print(f'  FIGURE TEXT WHOLE — {len(hard)} violation(s):')
    for f in hard: print(f'    p{f["page"]} {f["fig"]}: «{f["text"]}» — {f["why"]}')
if soft: print(f'  figure text whole — {len(soft)} line(s) pass under a haloed label (hidden, reported for the Eye): ' + ', '.join(sorted({f["fig"] for f in soft})))
else: print('  FIGURE TEXT WHOLE — every figure label is whole and uncrossed')
if sheet:
    try:
        ns, _, _ = paginate(sheet, '_render-affiche-sheet.html', 'fieldsheet.pdf', check=False); print(f'field sheet: {ns} pages -> fieldsheet.pdf')
    except Exception as e: print('field sheet FAILED:', str(e)[:200])

# page PNGs, contact sheet, and the figure captures for the Eye
os.makedirs('_affiche/figures', exist_ok=True)
for f in glob.glob('_affiche/p*.png') + glob.glob('_affiche/figures/*.png'): os.remove(f)
d = pymupdf.open('dossier.pdf'); thumbs = []
for i, page in enumerate(d):
    pix = page.get_pixmap(dpi=100); pix.save(f'_affiche/p{i+1:02d}.png'); thumbs.append(Image.open(f'_affiche/p{i+1:02d}.png'))
W = 204; th = int(W * 11 / 8.5); cols = 8; rows = (len(thumbs) + cols - 1) // cols
sheet_img = Image.new('RGB', (cols * (W + 10) + 10, rows * (th + 24) + 10), '#3a3a3a'); dr = ImageDraw.Draw(sheet_img)
for i, t in enumerate(thumbs):
    x = 10 + (i % cols) * (W + 10); y = 10 + (i // cols) * (th + 24)
    sheet_img.paste(t.resize((W, th), Image.LANCZOS), (x, y)); dr.text((x, y + th + 6), f'p{i+1}', fill='white')
sheet_img.save('_affiche/contact.png')
nfig = 0
for pgm in pages:
    for e in pgm['els']:
        if e['tag'] == 'figure' and 'fig' in e['cls'].split():
            page = d[pgm['page'] - 1]; sc = 72 / 96
            clip = pymupdf.Rect(e['left'] * sc - 6, e['top'] * sc - 6, e['right'] * sc + 6, e['bottom'] * sc + 6)
            page.get_pixmap(dpi=220, clip=clip).save(f'_affiche/figures/fig{e["fig"] or "x"}-p{pgm["page"]:02d}.png'); nfig += 1
print(f'  figure captures for the Eye: {nfig} -> _affiche/figures/')

TOP, BOT = 92, 984
for pgm in pages:
    els = pgm['els']
    if not els: print(f'  p{pgm["page"]:02d} EMPTY'); continue
    opener = pgm['page'] in full
    bottom = max(e['bottom'] for e in els); secs = sorted({e['sec'] for e in els if e['sec']})
    fill = (min(bottom, BOT) - TOP) / (BOT - TOP)
    flag = '' if (opener or fill >= 0.6) else '   <<< under 60 %'
    print(f'  p{pgm["page"]:02d} {",".join(secs)[:30]:30} {"opener" if opener else f"{fill:.0%}":8}{flag}')
