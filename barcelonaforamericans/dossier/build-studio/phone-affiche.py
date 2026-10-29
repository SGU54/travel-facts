# -*- coding: utf-8 -*-
"""phone-affiche.py — the phone edition of the Barcelona book (same method as Rome's) (atelier law 11, owner 2026-10-27).

Same source as the desktop book (dossier3.html after compose-affiche.py), split the same
way (fssplit). Set on a 4.5 x 8 in page. Body text keeps its size (11/17 px): the gain
comes from the narrower page, not from larger type.

What changes:
- the text column takes the page's width; floats, two-column grids and the margin
  apparatus become one column, in reading order;
- the posters (.poster, .m2) and photograph pages are recomposed for 432 x 768 px
  (positions re-proportioned, the giant words scaled, reading text never below 9 px);
- a drawn figure much wider than tall turns a quarter on its own page, so it prints
  wider than on the desktop page ("turn your phone sideways").

Run:  python3 phone-affiche.py [--no-compose]
Out:  dossier-phone.pdf, fieldsheet-phone.pdf, _phone/ (page PNGs, contact sheet, overflow report)
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

W, H = 432, 768                      # 4.5 x 8 in at 96 px/in
MT, MR, MB, ML = 40, 28, 38, 28      # page margins
CW, CH = W - ML - MR, H - MT - MB    # 376 x 690 text area

PHONE_CSS = r'''
/* @page rules take no !important: Paged.js drops the whole rule.
   ══ PHONE EDITION (phone-affiche.py) ══════════════════════════════════════ */
@page{ size:4.5in 8in; margin:40px 28px 38px 28px; }
@page annex{ size:4.5in 8in; margin:36px 28px 34px 28px; }
@page poster{ size:4.5in 8in; margin:0; }
/* text pages: one column, the page's width; body size unchanged */
.prose p, p.t{ width:auto !important; }
.sf{ width:auto !important; font-size:14px !important; line-height:20px !important; }
h1{ font-size:38px !important; line-height:.95 !important; }
h1.long{ font-size:32px !important; }
.aside{ float:none !important; width:auto !important; margin:14px 0 16px !important; }
.aside figure.mside img{ width:100% !important; }
.cols2, .forks2, .wgrid{ display:block !important; }
.cols2 > *, .forks2 > *, .wgrid > *{ width:auto !important; }
figure.band img{ height:200px !important; }
figure.band.bes{ display:block !important; } figure.band.bes figcaption{ margin-top:8px !important; }
figure.band.whole{ width:auto !important; display:block !important; }
figure.band.whole img{ width:100% !important; }
figure.band.whole figcaption{ margin-top:8px !important; }
.tier{ grid-template-columns:62px 1fr !important; column-gap:14px !important; }
.tier .n{ font-size:56px !important; }
.tier .h{ font-size:20px !important; line-height:22px !important; margin-top:4px !important; }
.nine .it{ grid-template-columns:40px 1fr 28px !important; column-gap:10px !important; }
.nine .n{ font-size:28px !important; }
/* a grid row at a page's foot is clipped by Paged.js instead of carried over: the contents rows are flex */
.toc a, .toc .fsrow{ display:flex !important; align-items:baseline !important; gap:10px !important; }
.cols2.toc > div{ display:contents !important; }   /* the two desktop columns become one list */
.toc .num{ flex:0 0 40px !important; } .toc .t{ flex:1 1 auto !important; } .toc a::after{ flex:0 0 30px !important; line-height:14px !important; }   /* the page numbers arrive after pagination: they must not grow the row */
.nine .pn, .nine .pn a::after, a.pref::after{ line-height:inherit !important; }
.fb .it{ grid-template-columns:1fr !important; row-gap:3px !important; }
.wl{ grid-template-columns:116px 1fr !important; }
.cards{ flex-direction:column !important; gap:30px !important; align-items:flex-start !important; margin-left:10px !important; }
.card{ width:324px !important; }
.fs .sf{ width:auto !important; }
.srcs .cols{ column-count:1 !important; }
.fs .r{ grid-template-columns:1fr 1.15fr !important; }
.fs div[style*="grid-template-columns"]{ display:block !important; }   /* the sheet's two desktop columns become one */

/* Barcelona's own components */
.grid{ display:block !important; }
h2, h3, .note, .li, .pg > .join, figure.fig.half{ width:auto !important; }
.ribbon, .ribbon.n5{ grid-template-columns:1fr 1fr !important; row-gap:10px !important; }
.ribbon .it + .it{ border-left:0 !important; padding-left:0 !important; margin-left:0 !important; }
.ribbon .it:nth-child(even){ border-left:1px solid var(--line) !important; padding-left:12px !important; }
.fails, .asks, .trips, .rules2{ display:block !important; }
.trips .trip + .trip{ margin-top:22px !important; }
.tier{ grid-template-columns:84px 1fr !important; column-gap:14px !important; padding:12px 0 16px !important; }
.tier .n{ font-size:76px !important; } .tier .h{ font-size:21px !important; line-height:23px !important; margin-top:6px !important; }
.tiers{ margin-top:24px !important; }
.seven .it{ grid-template-columns:44px 1fr 28px !important; column-gap:10px !important; } .seven .n{ font-size:32px !important; }
.fb .it{ grid-template-columns:1fr !important; row-gap:3px !important; }
.days{ display:block !important; height:auto !important; margin-top:20px !important; }
.days .d{ display:grid !important; grid-template-columns:64px 1fr !important; column-gap:12px !important; padding:10px 8px 12px !important; align-items:end !important; }
.days .n{ font-size:64px !important; grid-row:1 / span 2 !important; } .days .t{ margin-top:0 !important; }
.dayrow{ grid-template-columns:64px 1fr !important; column-gap:14px !important; padding:12px 0 18px !important; }
.dayrow .n{ font-size:60px !important; }
.rules2 .big{ font-size:22px !important; line-height:25px !important; } .rules2 > * + *{ margin-top:12px !important; }
.wgrid .stack .it.wl{ grid-template-columns:110px 1fr !important; }
.cover .title{ font-size:60px !important; margin-top:36px !important; }
.cover .sub{ width:auto !important; font-size:14px !important; line-height:20px !important; margin-top:20px !important; }
.cover .meta{ display:block !important; } .cover .meta > * + *{ margin-top:8px !important; }
.poster .giant{ margin-top:18px !important; }
.poster .under{ font-size:12px !important; }
.fs .sf{ width:auto !important; }
.fstable{ font-size:10.5px !important; }
/* posters with a flowing composition */
.poster:not(.m2){ width:432px !important; height:768px !important; padding:34px 28px 32px !important; }
.poster.paper:not(.m2){ height:767px !important; }
.poster .foot{ display:block !important; }
.poster .foot > * + *{ margin-top:12px !important; }
.poster .big{ font-size:21px !important; line-height:24px !important; }
.thesis{ font-size:40px !important; line-height:40px !important; margin-top:56px !important; }
.thesis.long{ font-size:34px !important; line-height:35px !important; margin-top:44px !important; }
/* photograph pages */
.photo{ width:432px !important; height:767px !important; }
.photo img, .photo.duo .dw, .photo.duo .dw img, .photo.typo .field{ height:420px !important; }
.photo .tail, .photo .tail.one{ padding:18px 28px 0 !important; display:block !important; }
.photo .tail > * + *{ margin-top:12px !important; }
.photo.duo .dw .word{ left:26px !important; }
#d04 .photo.duo .dw .word, #d06 .photo.duo .dw .word{ top:24px !important; right:28px !important; left:auto !important; }
#d09 .photo.duo .dw .word{ top:24px !important; }
.photo.typo .field .call{ left:28px !important; right:28px !important; bottom:32px !important; font-size:46px !important; }
.photo.typo .field .lab{ left:28px !important; top:36px !important; }
/* the m2 sheets: re-proportioned by PREP below */
.m2.sh{ width:432px !important; height:767px !important; }
.m2.sh svg.bg{ width:432px !important; height:767px !important; }
.m2 .slug{ top:30px !important; left:28px !important; right:28px !important; }
.m2 .foot{ left:28px !important; right:28px !important; bottom:32px !important; display:block !important; }
.m2 .foot > * + *{ margin-top:10px !important; }
.m2 .foot .big{ font-size:20px !important; line-height:23px !important; }
.m2 .duo{ height:420px !important; }
.m2 .tail{ left:28px !important; right:28px !important; top:440px !important; display:block !important; }
.m2 .tail > * + *{ margin-top:10px !important; }
/* a wide figure turned a quarter on its own page */
figure.fig.turn, .mapwrap.turn{ break-before:page; break-after:page; position:relative; width:376px; margin:0 !important; }
figure.fig.turn > .turnbox, .mapwrap.turn > .turnbox{ position:absolute; top:0; left:0; transform-origin:0 0; }
figure.fig.turn .turnhint, .mapwrap.turn .turnhint{ position:absolute; left:0; bottom:0; font-size:9px; font-weight:600; color:var(--grey); }
'''

# Before pagination: re-proportion the absolutely placed m2 posters and the giant words,
# and turn the wide figures. sx for widths and sizes, sy for vertical positions.
PREP = r'''function __prep(){
  var sx=%(sx)f, sy=%(sy)f, CW=%(CW)d, CH=%(CH)d;
  // Paged.js sizes the sheet from its own :root variables (letter by default); inline values win.
  var R=document.documentElement.style;
  ['','-right','-left'].forEach(function(k){ R.setProperty('--pagedjs-width'+k,'4.5in'); R.setProperty('--pagedjs-height'+k,'8in'); });
  function px(v){ var m=/(-?[\d.]+)px/.exec(v||''); return m?parseFloat(m[1]):null; }
  document.querySelectorAll('.m2.sh').forEach(function(sh){
    var svg=sh.querySelector('svg.bg'); if(svg) svg.setAttribute('preserveAspectRatio','xMidYMin meet');   // the drawing at the words' scale; the sheet's own ground fills below
    sh.querySelectorAll('.g, .gloss, .verdict, [style*="position"], [style*="left:"], [style*="top:"]').forEach(function(e){
      if(e.closest('svg')) return;
      if(e.classList.contains('foot')){ e.style.top='auto'; e.style.bottom='32px'; return; }   // the verdict sits on the foot of the sheet
      var s=e.style, gl=e.classList.contains('gloss');
      ['left','right'].forEach(function(k){ var v=px(s[k]); if(v!==null) s[k]=(v>=70&&v<=90?28:Math.round(v*sx))+'px'; });
      ['top','bottom'].forEach(function(k){ var v=px(s[k]); if(v!==null) s[k]=Math.round(v*sx)+'px'; });   // one scale with the drawing
      var w=px(s.width); if(w!==null) s.width=Math.min(Math.round(w*(gl?0.8:sx)), CW)+'px';
      if(gl){ var L=px(s.left); if(L!==null){ var room=%(W)d-24-L; s.maxWidth=room+'px'; if(px(s.width)!==null && px(s.width)>room) s.width=room+'px'; } }   // a gloss never runs past the sheet's edge
      var f=px(s.fontSize);
      if(f!==null){ var nf = gl ? Math.max(9, Math.min(f, Math.round(f*0.8))) : Math.round(f*sx);
        s.fontSize=nf+'px'; var lh=px(s.lineHeight); if(lh!==null) s.lineHeight=Math.round(lh*nf/f)+'px'; }
    });
  });
  document.querySelectorAll('.photo.duo .dw .word, .m2 .g').forEach(function(e){
    if(e.dataset.scaled) return; var f=px(e.style.fontSize); if(f!==null && !e.closest('.m2.sh')){ e.style.fontSize=Math.round(f*sx)+'px'; } e.dataset.scaled=1; });
  // a giant word is fitted to the sheet's width (never wider than the page minus its margins)
  document.querySelectorAll('.m2 .g, .photo.duo .dw .word, .photo.typo .field .call, .thesis, .poster .giant, .cover .title').forEach(function(e){
    var sh=e.closest('.m2.sh, .photo, .poster'); if(!sh) return; var lim=sh.getBoundingClientRect().right-24;
    var rg=document.createRange(); rg.selectNodeContents(e);
    for(var k=0;k<60;k++){ var r=rg.getBoundingClientRect(); if(r.right<=lim && r.left>=sh.getBoundingClientRect().left+12) break;
      var f=parseFloat(getComputedStyle(e).fontSize); e.style.setProperty('font-size',(f*0.95)+'px','important'); }
  });
  document.querySelectorAll('figure.fig, .mapwrap').forEach(function(fig){
    var svg=fig.querySelector('svg'); if(!svg||!svg.viewBox||!svg.viewBox.baseVal||!svg.viewBox.baseVal.width) return;
    var vb=svg.viewBox.baseVal, r=vb.width/vb.height; if(r<1.6) return;
    var capH=46, wide=Math.min(CH-4, Math.floor((CW-capH)*r)), tall=Math.ceil(wide/r)+capH;
    var box=document.createElement('div'); box.className='turnbox'; box.style.width=wide+'px';
    while(fig.firstChild) box.appendChild(fig.firstChild);
    fig.appendChild(box); fig.classList.add('turn'); fig.style.height=CH+'px';
    box.style.transform='translate('+tall+'px,0) rotate(90deg)';
    var hint=document.createElement('div'); hint.className='turnhint'; hint.textContent='Turn your phone sideways'; fig.appendChild(hint);
  });
}''' % {'sx': W / 816, 'sy': H / 1056, 'CW': CW, 'CH': CH, 'W': W}

CHIPS = ('function __chips(){document.querySelectorAll("figure.fig svg text").forEach(function(t){try{if(t.hasAttribute("data-nochip"))return;var b=t.getBBox();if(!b.width)return;'
         'var r=document.createElementNS("http://www.w3.org/2000/svg","rect");r.setAttribute("x",b.x-1.5);r.setAttribute("y",b.y+b.height*0.12);'
         'r.setAttribute("width",b.width+3);r.setAttribute("height",b.height*0.78);r.setAttribute("fill","#EFE4CC");r.setAttribute("class","chip");'
         't.parentNode.insertBefore(r,t);t.style.stroke="none";t.style.paintOrder="normal";t.style.strokeWidth="0";}catch(e){}});}')
# PagedConfig must exist BEFORE the polyfill loads, or it paginates on its own at load,
# before __prep has touched the posters.
INJECT = ('<style>' + PHONE_CSS + '</style><script>window.PagedConfig={auto:false};</script><script src="paged.polyfill.js"></script><script>' + CHIPS + PREP +
          'window.addEventListener("load",function(){document.fonts.ready.then(function(){__prep();return window.PagedPolyfill.preview();})'
          '.then(function(f){__chips();window.__pagedDone=f.total;}).catch(function(e){window.__pagedErr=(e&&e.stack)?e.stack:String(e);});});</script>')
XREF = """() => { let done = 0, miss = []; document.querySelectorAll('a[href^="#"]').forEach(a => {
  const id = a.getAttribute('href').slice(1); const t = document.getElementById(id) || document.querySelector('[data-id="' + CSS.escape(id) + '"]');
  const page = t && t.closest('.pagedjs_page'); const n = a.querySelector('.n') || a; if (page) { n.dataset.page = page.dataset.pageNumber; done++; } else miss.push(id); });
  return {done, miss}; }"""
# Anything that spills out of its page, or text set below 9 px (the figure labels aside).
OVERFLOW = """() => { const out = [];
  document.querySelectorAll('.pagedjs_page').forEach((pg, i) => { const r = pg.getBoundingClientRect();
    pg.querySelectorAll('.pagedjs_page_content *').forEach(e => {
      if (e.closest('svg') || e.closest('.turn') || !e.childNodes.length) return;
      const own = [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
      if (!own) return; const b = e.getBoundingClientRect(); if (!b.width) return;
      const fs = parseFloat(getComputedStyle(e).fontSize);
      if (b.right > r.right + 1 || b.left < r.left - 1 || b.bottom > r.bottom + 1) out.push({page: i + 1, why: 'outside the page', text: e.textContent.trim().slice(0, 50)});
      else if (fs < 8.5 && !e.closest('.card.back') && !e.closest('.srcs')) out.push({page: i + 1, why: 'set at ' + fs + 'px', text: e.textContent.trim().slice(0, 50)});
    }); });
  const seen = new Set(); return out.filter(o => { const k = o.page + o.why + o.text; if (seen.has(k)) return false; seen.add(k); return true; }); }"""


def phone_pages(html):
    """Paged.js keeps the first page size it reads, so the book's own @page rules are
    rewritten in the copy set for the phone (the desktop source is never touched)."""
    html = html.replace('@page{ size:8.5in 11in; margin:92px 82px 72px 82px;', '@page{ size:4.5in 8in; margin:40px 28px 38px 28px;')
    html = html.replace('@page annex{ margin:72px 82px 60px 82px; }', '@page annex{ margin:36px 28px 34px 28px; }')
    assert '8.5in 11in;' not in html.split('</style>')[0], 'a desktop page size is left'
    return html


def paginate(html, name, pdf):
    html = phone_pages(html)
    open(name, 'w', encoding='utf-8').write(html.replace('</head>', INJECT + '</head>'))
    with sync_playwright() as p:
        b = p.chromium.launch(args=['--no-sandbox', '--font-render-hinting=none']); pg = b.new_page(viewport={'width': W, 'height': H})
        pg.emulate_media(media='print')   # paginate in the media it prints in: screen rows run a few px shorter
        pg.goto('file://' + os.path.join(BUILD, name), wait_until='load')
        pg.wait_for_function('window.__pagedDone !== undefined || window.__pagedErr !== undefined', timeout=300000)
        err = pg.evaluate('window.__pagedErr'); assert not err, err
        n = pg.evaluate('window.__pagedDone')
        xref = pg.evaluate(XREF); print(f'  cross-references resolved: {xref["done"]}; unresolved: {xref["miss"]}')
        over = pg.evaluate(OVERFLOW)
        # the sheet size is given to Chromium directly: Paged.js leaves its letter default on the sheet
        pg.pdf(path=pdf, width='4.5in', height='8in', print_background=True, prefer_css_page_size=False, display_header_footer=False, margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'})
        b.close()
    return n, over


os.makedirs('_phone', exist_ok=True)
for f in glob.glob('_phone/p*.png'): os.remove(f)
# the cover states its page count: the phone edition says its own (re-render once if it moved)
import re as _rc
def _count(h, k): return _rc.sub(r'>\d+ pages · ', '>%d pages · ' % k, h, count=1)
guess = 95
n, over = paginate(_count(book, guess), '_render-phone.html', 'dossier-phone.pdf')
if n != guess:
    n, over = paginate(_count(book, n), '_render-phone.html', 'dossier-phone.pdf')
print(f'phone book: {n} pages -> dossier-phone.pdf')
# bookmarks: the desktop book's outline titles, at their phone pages
try:
    desk = pymupdf.open('dossier.pdf').get_toc(); ph = pymupdf.open('dossier-phone.pdf'); toc = []
    for lvl, title, _ in desk:
        key = title.strip()[:40]
        for i, page in enumerate(ph):
            if key and page.search_for(key[:28]):
                toc.append([lvl, title, i + 1]); break
    if toc: ph.set_toc(toc); ph.saveIncr()
    ph.close(); print(f'  bookmarks: {len(toc)} of {len(desk)}')
except Exception as ex: print('  bookmarks FAILED', ex)
json.dump(over, open('_phone/overflow.json', 'w'), indent=1, ensure_ascii=False)
print(f'  overflow / small text: {len(over)}')
for o in over[:40]: print(f'    p{o["page"]}: {o["why"]} — «{o["text"]}»')
if sheet:
    try:
        ns, so = paginate(sheet, '_render-phone-sheet.html', 'fieldsheet-phone.pdf'); print(f'phone field sheet: {ns} pages -> fieldsheet-phone.pdf · overflow {len(so)}')
        for o in so[:20]: print(f'    sheet p{o["page"]}: {o["why"]} — «{o["text"]}»')
    except Exception as e: print('field sheet FAILED:', str(e)[:200])
d = pymupdf.open('dossier-phone.pdf'); thumbs = []
for i, page in enumerate(d):
    pix = page.get_pixmap(dpi=110); pix.save(f'_phone/p{i+1:02d}.png'); thumbs.append(Image.open(f'_phone/p{i+1:02d}.png'))
TW = 150; th = int(TW * 8 / 4.5); cols = 10; rows = (len(thumbs) + cols - 1) // cols
cs = Image.new('RGB', (cols * (TW + 10) + 10, rows * (th + 24) + 10), '#3a3a3a'); dr = ImageDraw.Draw(cs)
for i, t in enumerate(thumbs):
    x = 10 + (i % cols) * (TW + 10); y = 10 + (i // cols) * (th + 24)
    cs.paste(t.resize((TW, th), Image.LANCZOS), (x, y)); dr.text((x, y + th + 6), f'p{i+1}', fill='white')
cs.save('_phone/contact.png'); print('  contact sheet: _phone/contact.png')
