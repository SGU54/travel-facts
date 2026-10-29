# -*- coding: utf-8 -*-
"""render_paged.py — the paginated render (replaces render_rome.py / render3.js).

Architecture: Paged.js slices the .flow into REAL page divs before printing.
Each printed sheet is a DOM element that paints the paper itself, carries the
@page margins INSIDE its box, and renders the running head + folio as margin
boxes on EVERY page — chapter starts and continuations alike. This is the only
architecture that survives this Chromium: header/footer templates clip their
backgrounds (white bands), @page margins are unpainted, and position:fixed
does not repeat across printed pages. All three were tried and shipped bugs.

It also runs the FEATHERING pass — the compositor's card. After pagination it
measures every chapter's tail page; a chapter that spills only a few orphan
lines is re-set one notch tighter (.tight, ~2 lines/page of give) so the tail
pulls back onto the page. Measured every build, never hand-listed.

Ship this INTO each build directory next to dossier3.html, together with
assets/paged.polyfill.js. It is destination-agnostic: everything project-specific
(paper colour, furniture strings, named pages) lives in the build's CSS.

Usage: python3 render_paged.py [build-dir]     (default: the script's own directory)
"""
import glob, os, re, sys
from playwright.sync_api import sync_playwright
from pypdf import PdfReader

BUILD = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))

INJECT = (
    "<script>window.PagedConfig={auto:false};</script>"
    # Book convention: a chapter opener announces itself, so its running head is
    # suppressed (folio stays). H1s exist only at page tops (chapters break-before).
    "<script>window.__openerHandler=function(P){"
    "class O extends P.Handler{afterPageLayout(el){"
    "if(!el||typeof el.querySelector!=='function')return;"
    "if(el.querySelector('.pagedjs_page_content h1, .pagedjs_page_content .bleed, .pagedjs_page_content .figx.pagetop')){"
    "el.querySelectorAll('.pagedjs_margin-top-left,.pagedjs_margin-top-right')"
    ".forEach(function(m){m.style.visibility='hidden'});}}}"
    "P.registerHandlers(O);};</script>"
    "<script src=\"paged.polyfill.js\"></script>"
    "<script>window.__openerHandler(window.Paged);</script>"
    # The inject lives in <head>. With LOCAL font files document.fonts.ready can
    # resolve while the parser is still inside <head>, so preview() would run
    # against a document with no <body> and Paged's wrapContent() throws on a
    # null querySelector("body"). Gate the whole chain on DOM readiness first.
    # This book ships its own fonts/, so it hits that path every time.
    "<script>(function(){function go(){"
    "document.fonts.ready.then(function(){"
    "return Promise.all(Array.from(document.images).map("
    "function(i){return i.decode().catch(function(){})}));}).then(function(){"
    "window.PagedPolyfill.preview().then(function(f){window.__pagedDone=f.total;})"
    ".catch(function(e){window.__pagedErr=(e&&e.stack)?e.stack:String(e);});});}"
    "if(document.readyState==='loading'){"
    "document.addEventListener('DOMContentLoaded',go);}else{go();}})();</script>"
)

PAGEMAP_JS = """() => [...document.querySelectorAll('.pagedjs_page')].map((pg, i) => {
  const r = pg.getBoundingClientRect();
  const els = [...pg.querySelectorAll('.pagedjs_page_content section > *, .pagedjs_page_content .closeblock > *')]
    .filter(e => !e.classList.contains('rh-src'))
    .map(e => { const b = e.getBoundingClientRect(); const sec = e.closest('section');
      return { tag: e.tagName.toLowerCase(), cls: e.className || '', dp: e.dataset.p || '',
               sec: sec ? (sec.dataset.id || sec.id || sec.dataset.ref || '') : '', top: Math.round(b.top - r.top), bottom: Math.round(b.bottom - r.top),
               left: Math.round(b.left - r.left), right: Math.round(b.right - r.left),
               split: !!e.dataset.splitFrom, text: (e.textContent || '').trim().slice(0, 40) }; });
  return { page: i + 1, els };
})"""

# what a .tight chapter gives back, per preceding page and per photo plate it holds
GIVE_PER_PAGE = 48.0     # px: 0.5px x ~34 lines + 1px x paragraphs + block margins
GIVE_TALL_PLATE = 90.0   # px: a 3.3in plate resets to 2.3in under .tight
GIVE_PLATE = 22.0        # px: a 2.55in plate resets to 2.3in
FEED_MAX_TAIL = 420.0    # px: a tail this size or less, with a plate available, gets fed
CONTENT_H = 892.0        # px: the body column, 92 -> 984

MEASURE_JS = """
() => {
  const secs = {};
  document.querySelectorAll('.pagedjs_page').forEach((pg, pi) => {
    pg.querySelectorAll('.pagedjs_page_content section.dec').forEach(s => {
      const ref = s.getAttribute('data-ref');
      const id = s.id || (secs[ref] && secs[ref].id) || null;
      const h = s.getBoundingClientRect().height;
      const imgs = s.querySelectorAll('figure.photo img');
      // map figures are this build's plates: count them as movable tall plates
      const maps = s.querySelectorAll('figure.map');
      let tall = 0, small = 0;
      imgs.forEach(i => { if ((i.style.height||'').indexOf('3.3') >= 0) tall++; else small++; });
      if (!secs[ref]) secs[ref] = { id: id, pages: [], tall: 0, small: 0, tailPhotos: 0, maps: 0, tailMaps: 0 };
      if (id && !secs[ref].id) secs[ref].id = id;
      secs[ref].pages.push({ page: pi + 1, h: h });
      secs[ref].tall += tall; secs[ref].small += small;
      secs[ref].maps += maps.length;
      secs[ref].tailPhotos = imgs.length;
      secs[ref].tailMaps = maps.length;   // last fragment wins = tail
    });
  });
  return Object.values(secs);
}
"""

# Per-FIGURE geometry: the page each one landed on, whether it opened that page,
# and how much column sits unused at the foot of the page before it.
MEASURE_FIGS_JS = """
() => {
  const PX = 96;
  const pages = [...document.querySelectorAll('.pagedjs_page')];
  const boxOf = pg => pg.querySelector('.pagedjs_page_content');
  const drawn = box => {
    const r = box.getBoundingClientRect(); const out = [];
    box.querySelectorAll('*').forEach(el => {
      const leaf = el.children.length === 0;
      if (!leaf && !/^(IMG|FIGURE|TABLE|HR|FIGCAPTION|SVG)$/.test(el.tagName)) return;
      const e = el.getBoundingClientRect();
      if (e.height > 0.5 && (leaf ? ((el.textContent||'').trim() || /^(IMG|HR)$/.test(el.tagName)) : true))
        out.push(e);
    });
    return out;
  };
  const out = [];
  pages.forEach((pg, pi) => {
    const box = boxOf(pg); if (!box) return;
    box.querySelectorAll('figure').forEach(fig => {
      const im = fig.querySelector('img'); if (!im) return;
      const fr = fig.getBoundingClientRect();
      const fs = getComputedStyle(fig);
      // getBoundingClientRect excludes margins, but the page must find room for
      // them too — ignoring them shrinks a figure to a size that still will not
      // fit, and it stays on its own page anyway.
      const fmar = (parseFloat(fs.marginTop)||0) + (parseFloat(fs.marginBottom)||0);
      const above = drawn(box).filter(x => x.bottom <= fr.top + 1).length;
      let prevFree = null;
      if (pi > 0) {
        const prev = boxOf(pages[pi-1]);
        if (prev) {
          const pr = prev.getBoundingClientRect();
          const rs = drawn(prev);
          const low = rs.length ? Math.max(...rs.map(r => Math.min(r.bottom, pr.bottom))) : pr.top;
          prevFree = (pr.bottom - low) / PX;
        }
      }
      out.push({ src: (im.getAttribute('src')||'').split('/').pop(),
                 page: pi+1, block: (fr.height+fmar)/PX,
                 img: im.getBoundingClientRect().height/PX,
                 atTop: above === 0, prevFree: prevFree });
    });
  });
  return out;
}
"""


# A FIGURE AND THE TABLE UNDER IT ARE ONE ARGUMENT. Barcelona's decision chapters
# open with a scale map and then the ledger that reads it. Where the map is a
# little too tall, the ledger loses its last rows to the next sheet — the reader
# gets four options on one page and the fifth alone overleaf, which is exactly
# the comparison the table exists to prevent. CSS cannot fix this: nothing pulls
# content backwards, and break-inside:avoid on the table only strands it whole.
#
# So measure the spill and take it out of the figure, floored at the series'
# 85% ratio. Figures are addressed by their INDEX in document order because this
# build's arguing figures are inline <svg> with no id and no src to match on.
MEASURE_FITS_JS = """
() => {
  const PX = 96;
  const pageOf = new Map();
  const figs = [], tables = [];
  document.querySelectorAll('.pagedjs_page').forEach((pg, pi) => {
    const box = pg.querySelector('.pagedjs_page_content');
    if (!box) return;
    box.querySelectorAll('figure, table').forEach(el => {
      const ref = el.getAttribute('data-ref') || '';
      const r = el.getBoundingClientRect();
      const rec = { ref: ref, page: pi + 1, h: r.height / PX, top: r.top, bottom: r.bottom };
      const sec = el.closest('section.dec');
      rec.sec = sec ? (sec.id || sec.getAttribute('data-ref') || '') : '';
      if (el.tagName === 'FIGURE') figs.push(rec); else tables.push(rec);
    });
  });
  // document order, for addressing a figure the rewriter can find
  const allFigs = [...document.querySelectorAll('.pagedjs_page_content figure')];
  const order = new Map();
  let n = 0;
  const seen = new Set();
  allFigs.forEach(f => {
    const ref = f.getAttribute('data-ref') || ('x' + (n));
    if (!seen.has(ref)) { order.set(ref, n++); seen.add(ref); }
  });
  figs.forEach(f => { f.idx = order.has(f.ref) ? order.get(f.ref) : -1; });
  // how much column is free at the foot of a page
  const free = {};
  document.querySelectorAll('.pagedjs_page').forEach((pg, pi) => {
    const box = pg.querySelector('.pagedjs_page_content'); if (!box) return;
    const pr = box.getBoundingClientRect();
    let low = pr.top;
    box.querySelectorAll('*').forEach(el => {
      if (el.children.length && !/^(IMG|FIGURE|TABLE|HR|FIGCAPTION|SVG)$/.test(el.tagName)) return;
      const e = el.getBoundingClientRect();
      if (e.height > 0.5) low = Math.max(low, Math.min(e.bottom, pr.bottom));
    });
    free[pi + 1] = (pr.bottom - low) / PX;
  });
  return { figs: figs, tables: tables, free: free };
}
"""


# A HEADING SEPARATED FROM ITS TEXT. `h2,h3{break-after:avoid}` fixes the ugly
# half — a heading stranded at the foot of a page — but it fixes it by pushing
# the heading FORWARD, which leaves the page before it short and moves the
# heading away from where the argument puts it.
#
# Where the shortfall is small, pulling the text back is the better answer, and
# the head band is the lever: p33 was 0.22in short of holding its heading plus
# two lines, p35 0.06in. A photograph that gives up a quarter-inch is not a
# photograph anyone notices; a heading on the wrong page is.
#
# So this measures headings that START a sheet (a chapter opener excluded — it
# has an h1) and asks what the page before them was short by.
MEASURE_WIDOW_JS = """
() => {
  const PX = 96, out = [];
  const pages = [...document.querySelectorAll('.pagedjs_page')];
  const boxOf = pg => pg.querySelector('.pagedjs_page_content');
  const drawnLow = box => {
    const pr = box.getBoundingClientRect(); let low = pr.top;
    box.querySelectorAll('*').forEach(el => {
      if (el.children.length && !/^(IMG|FIGURE|TABLE|HR|FIGCAPTION|SVG)$/.test(el.tagName)) return;
      const e = el.getBoundingClientRect();
      if (e.height <= 0.5) return;
      if (!(el.textContent || '').trim() && !/^(IMG|HR)$/.test(el.tagName)) return;
      low = Math.max(low, Math.min(e.bottom, pr.bottom));
    });
    return low;
  };
  pages.forEach((pg, pi) => {
    if (pi === 0) return;
    const box = boxOf(pg); if (!box) return;
    // a chapter opener is not a pushed heading
    if (box.querySelector('h1')) return;
    // the FIRST drawn block on this sheet
    let first = null, top = Infinity;
    box.querySelectorAll('*').forEach(el => {
      if (el.children.length && !/^(IMG|FIGURE|TABLE|HR|FIGCAPTION|SVG)$/.test(el.tagName)) return;
      const e = el.getBoundingClientRect();
      if (e.height <= 0.5) return;
      if (!(el.textContent || '').trim() && !/^(IMG|HR)$/.test(el.tagName)) return;
      if (e.top < top) { top = e.top; first = el; }
    });
    if (!first) return;
    let h = first;
    while (h && !/^H[1-6]$/.test(h.tagName)) h = h.parentElement;
    if (!h || !/^H[23456]$/.test(h.tagName) || !box.contains(h)) return;
    const sec = h.closest('section.dec'); if (!sec) return;
    // Paged.js SPLITS a section across sheets, so this page's fragment holds
    // only this page's content — the head band sits in an earlier fragment and
    // a lookup inside `sec` finds nothing. Resolve it by data-ref across the
    // whole document instead. This silently found zero pushed headings.
    const ref = sec.getAttribute('data-ref');
    const sid = sec.id || '';
    let band = null;
    document.querySelectorAll('.pagedjs_page_content section.dec').forEach(o => {
      if (band) return;
      const same = (ref && o.getAttribute('data-ref') === ref) || (sid && o.id === sid);
      if (!same) return;
      const b = o.querySelector('.photo.band img');
      if (b) band = b;
    });
    if (!band) return;
    const prev = boxOf(pages[pi-1]); if (!prev) return;
    const pr = prev.getBoundingClientRect();
    const hs = getComputedStyle(h);
    const hh = (h.getBoundingClientRect().height
                + (parseFloat(hs.marginTop)||0) + (parseFloat(hs.marginBottom)||0)) / PX;
    out.push({ page: pi + 1,
               text: (h.textContent || '').trim().slice(0, 42),
               sec: sid || (function(){
                 let got = '';
                 document.querySelectorAll('.pagedjs_page_content section.dec').forEach(o => {
                   if (!got && ref && o.getAttribute('data-ref') === ref && o.id) got = o.id;
                 });
                 return got;
               })(),
               band: band.getBoundingClientRect().height / PX,
               prevFree: (pr.bottom - drawnLow(prev)) / PX,
               need: hh + (2 * 19) / PX });
  });
  return out;
}
"""

FIT_FLOOR = 0.85   # the series ratio: never shrink a figure below 85% of itself
FIT_GAP   = 0.05   # in — a fit that is hairline is not a fit
BAND_FULL = 1.75   # in — a decision chapter's head band at its designed height
BAND_MIN  = 1.20   # in — and the floor it may be cut to, Rome's value


def _cut_band(h, sid, height_in):
    """Cut one chapter's head band. TAKEN BEFORE THE FIGURE, because a band is
    furniture and a figure is an argument: half an inch off a photograph costs
    the reader nothing, half an inch off a scale map costs its labels."""
    m = re.search(r'<section\b[^>]*\bid="%s"[^>]*>' % re.escape(sid), h)
    if not m:
        return h
    k = h.find('<figure class="photo band"', m.end())
    if k < 0:
        return h
    e = h.index('>', k)
    tag = h[k:e + 1]
    if '--band' in tag:
        return h
    return h[:k] + tag[:-1] + f' style="--band:{height_in:.2f}in">' + h[e + 1:]


def _fit(h, idx, target_in):
    """Give the idx-th <figure> in document order an explicit height."""
    pos, n = 0, 0
    while True:
        k = h.find('<figure', pos)
        if k < 0:
            return h
        if n == idx:
            e = h.index('>', k)
            tag = h[k:e + 1]
            if 'data-fit' in tag:
                return h
            new = tag[:-1] + f' data-fit="1" style="--fit:{target_in:.2f}in">'
            return h[:k] + new + h[e + 1:]
        n += 1
        pos = k + 1


# A CLOSING PLATE IS CUT TO THE PAGE IT CLOSES, not to one standard height.
# Every chapter ends with a plate, and a fixed 4.6in leaves whatever the chapter
# happened to spill — sometimes four inches of white under the picture. Rome
# solved this by measuring the room actually left on each chapter's last sheet
# and sizing that chapter's plate to it. Same measurement here.
MEASURE_LAST_JS = """
() => {
  const PX = 96, out = [];
  const pages = [...document.querySelectorAll('.pagedjs_page')];
  pages.forEach((pg, pi) => {
    const box = pg.querySelector('.pagedjs_page_content'); if (!box) return;
    const pr = box.getBoundingClientRect();
    const figs = [...box.querySelectorAll('figure.photo')];
    if (!figs.length) return;
    const fig = figs[figs.length - 1];
    const im = fig.querySelector('img'); if (!im) return;
    if (fig.classList.contains('band')) return;      // never a head band
    // it must be the LAST drawn thing on the sheet
    let low = pr.top;
    box.querySelectorAll('*').forEach(el => {
      if (el.children.length && !/^(IMG|FIGURE|TABLE|HR|FIGCAPTION|SVG)$/.test(el.tagName)) return;
      const e = el.getBoundingClientRect();
      if (e.height > 0.5) low = Math.max(low, Math.min(e.bottom, pr.bottom));
    });
    const fr = fig.getBoundingClientRect();
    if (fr.bottom < low - 2) return;                  // something sits below it
    // does the plate OWN this sheet? nothing drawn above it either
    let alone = true;
    box.querySelectorAll('*').forEach(el => {
      if (fig.contains(el) || el.contains(fig)) return;
      if (el.children.length && !/^(IMG|FIGURE|TABLE|HR|FIGCAPTION|SVG)$/.test(el.tagName)) return;
      const e = el.getBoundingClientRect();
      if (e.height > 0.5 && (el.textContent||'').trim()) alone = false;
    });
    out.push({ src: (im.getAttribute('src')||'').split('/').pop(),
               page: pi + 1, alone: alone,
               img: im.getBoundingClientRect().height / PX,
               free: (pr.bottom - low) / PX });
  });
  return out;
}
"""

FILL_MIN  = 0.45   # in — below this the page is basically full; leave it alone
FILL_CAP  = 6.60   # in — a plate taller than this stops being a plate


def _fill(h, src, spec):
    """Give the plate with this src an explicit closing height, and — when it
    owns its sheet — the top margin that centres it optically.

    A landscape plate cannot be grown to a full portrait page: covering 6.8 x 9.2in
    from a 3:2 frame throws away more than half the picture. So the height stops
    at FILL_CAP and the leftover column is split above and below instead, which
    reads as a composed full-page plate rather than a picture that ran out."""
    img_in, pad_in = spec
    pat = re.compile(r'<figure class="([^"]*)"([^>]*)>(\s*<img src="(?:[^"]*/)?'
                     + re.escape(src) + r'")')
    m = pat.search(h)
    if not m:
        return h
    cls = m.group(1).replace(" fill", "")
    style = f'--fill:{img_in:.2f}in'
    if pad_in > 0.12:
        style += f';--fillpad:{pad_in:.2f}in'
    return (h[:m.start()]
            + f'<figure class="{cls} fill" style="{style}"{m.group(2)}>'
            + m.group(3) + h[m.end():])

SNUG_FLOOR = 0.85        # shrink only down to 85% of what the figure needs
SNUG_GAP   = 0.06        # breathing room so the fit is not hairline

def _snug(h, src, img_in):
    """Mark one figure snug and give it an explicit image height. Matches any
    extra classes: the tail-feed pass runs first and may already have renamed
    the figure, and an exact class match silently does nothing."""
    pat = re.compile(r'<figure class="([^"]*)"([^>]*)>(\s*<img src="(?:[^"]*/)?'
                     + re.escape(src) + r'")')
    m = pat.search(h)
    if not m:
        return h
    cls = m.group(1).replace(" snug", "")
    return (h[:m.start()]
            + f'<figure class="{cls} snug" style="--snug:{img_in:.2f}in"{m.group(2)}>'
            + m.group(3) + h[m.end():])

_PHOTO_RE = r'<figure class="photo(?! band)[^"]*"[^>]*>.*?</figure>'
# NB: a chapter-HEAD band is excluded. The tail-feed exists to move a plate
# down to fill a chapter's last page; applied to a head band it silently
# pulls the chapter's opening image to its end, which is the opposite of
# what the band is for. Nine chapters lost their opener this way.
_MAP_RE = r'(?!x)x'   # this build has no map figures — never matches

def _add_class(h, sid, cls):
    """Add one class to the <section> carrying this id, whatever else it wears.

    The previous writer matched the literal `class="dec chap" id="sid"`, in that
    order and with exactly those two classes. Every chapter that carries a third
    (`decision`, `fs`) was silently skipped — the pass printed that it had
    tightened a chapter it had not touched.
    """
    m = re.search(r'<section\b[^>]*\bid="%s"[^>]*>' % re.escape(sid), h)
    assert m, f"no <section> with id={sid}"
    tag = m.group(0)
    if re.search(r'\bclass="[^"]*\b%s\b' % cls, tag):
        return h
    c = re.search(r'class="([^"]*)"', tag)
    new = (tag.replace(c.group(0), 'class="%s %s"' % (c.group(1), cls))
           if c else tag[:-1] + ' class="%s">' % cls)
    return h[:m.start()] + new + h[m.end():]


def _feed_tail(h, sid):
    """Move the section's plate to the chapter's end, right before the endmark,
    so it lands on (and fills) the tail page. Prefers a photo plate; falls back to
    this build's map figures (its plates) when there is no photo."""
    start = h.index(f'id="{sid}"')
    end = h.index("</section>", start)
    seg = h[start:end]
    m = re.search(_PHOTO_RE, seg, flags=re.S)
    is_map = False
    if not m:
        # this build is figure-rich: a map figure is the movable plate
        allmaps = list(re.finditer(_MAP_RE, seg, flags=re.S))
        if not allmaps:
            return h
        m = allmaps[-1]      # move the LAST map in the chapter to its tail
        is_map = True
    plate = m.group(0)
    seg2 = seg.replace(plate, "", 1)
    # a fed plate becomes the chapter's CLOSING plate: tall, image-dominant
    if is_map:
        plate = plate.replace('<figure class="map"', '<figure class="map closing"', 1)
    else:
        plate = plate.replace('<figure class="photo">', '<figure class="photo closing">', 1)
    if '<div class="endmark">' in seg2:
        seg2 = seg2.replace('<div class="endmark">', plate + '<div class="endmark">', 1)
    else:
        seg2 = seg2 + plate
    return h[:start] + seg2 + h[end:]

def _paginate(pg, path, timeout_ms):
    pg.goto(f"file://{path}", wait_until="load")
    pg.wait_for_function(
        "window.__pagedDone !== undefined || window.__pagedErr !== undefined",
        timeout=timeout_ms)
    err = pg.evaluate("window.__pagedErr")
    assert not err, f"paginator failed: {err}"
    return pg.evaluate("window.__pagedDone")

def render(html_name="dossier3.html", pdf_name="dossier.pdf", timeout_ms=600_000):
    html = open(os.path.join(BUILD, html_name), encoding="utf-8").read()
    assert "</head>" in html
    render_path = os.path.join(BUILD, "_render.html")

    # Portable browser lookup: the Linux container path first, then macOS's
    # playwright cache, then playwright's own resolution. This used to hard-exit
    # unless chromium sat in /opt/pw-browsers, so the tree could only be rebuilt
    # on the container it was first built in.
    exes = (glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome")
            + glob.glob("/opt/pw-browsers/chromium_headless_shell-*/chrome-linux/headless_shell")
            + glob.glob(os.path.expanduser(
                "~/Library/Caches/ms-playwright/chromium-*/chrome-mac/Chromium.app"
                "/Contents/MacOS/Chromium")))

    with sync_playwright() as p:
        launch = {"args": ["--no-sandbox", "--font-render-hinting=none"]}
        if exes:
            launch["executable_path"] = sorted(exes)[0]
        b = p.chromium.launch(**launch)
        pg = b.new_page(viewport={"width": 816, "height": 1056}, device_scale_factor=2)

        tight, fed, loose, snug, fit, fill, cut = set(), set(), set(), {}, {}, {}, {}
        n_dom = 0
        for attempt in range(9):   # the fit and snug passes each consume one
            h = html
            for sid_, bh in cut.items():
                h = _cut_band(h, sid_, bh)
            for idx, target in sorted(fit.items()):
                h = _fit(h, idx, target)
            for src, ih in fill.items():
                h = _fill(h, src, ih)
            for sid in fed:
                h = _feed_tail(h, sid)
            for src, ih in snug.items():
                h = _snug(h, src, ih)
            for sid in loose:
                h = _add_class(h, sid, "loose")
            for sid in tight:
                h = _add_class(h, sid, "tight")
            open(render_path, "w", encoding="utf-8").write(
                h.replace("</head>", INJECT + "</head>"))
            n_dom = _paginate(pg, render_path, timeout_ms)

            # FEATHER: (a) a small spill gets pulled back (.tight); (b) a tail too big
            # to pull back, in a chapter that holds a photo plate, gets FED the plate
            # (doctrine: chapter-break slack is where plates go), so the tail reads as
            # a designed closing-image page instead of a stranded fragment.
            # SNUG PASS — a figure that opened a page of its own, where the
            # page before it was left with ALMOST enough room, is shrunk to fit
            # there rather than costing a whole sheet. Runs before the feather
            # decisions because it removes the stranded tail they would
            # otherwise try to fix by moving things around.
            # WIDOW HEADINGS — run before the table fit, because recovering a
            # heading changes where everything after it falls.
            new_widow = {}
            for w in pg.evaluate(MEASURE_WIDOW_JS):
                sid_ = w["sec"]
                if not sid_ or sid_ in cut or w["band"] <= 0:
                    continue
                short = w["need"] - w["prevFree"]
                if short <= 0:
                    continue
                give = min(short + 0.04, w["band"] - BAND_MIN)
                if give < 0.05:
                    print(f"  heading: \"{w['text']}\" opens p{w['page']} and the "
                          f"page before is {short:.2f}in short — more than its band "
                          f"can give, left where it is")
                    continue
                # Only a trade the reader cannot see. 0.83in off a 2.35in band is
                # a third of the photograph to rescue one heading — past that,
                # break-after:avoid pushing it forward is the better answer.
                if short > 0.5:
                    print(f"  heading: \"{w['text']}\" opens p{w['page']} — "
                          f"{short:.2f}in short, more than a band should pay; "
                          f"left where break-after put it")
                    continue
                new_widow[sid_] = w["band"] - give
                print(f"  heading: \"{w['text']}\" opens p{w['page']}, {short:.2f}in "
                      f"short — cut {sid_}'s band {w['band']:.2f}in -> "
                      f"{w['band'] - give:.2f}in to pull it back with two lines")
            if new_widow:
                cut.update(new_widow)
                continue

            # FIT: a table split away from the figure that introduces it
            mf2 = pg.evaluate(MEASURE_FITS_JS)
            by_ref = {}
            for t in mf2["tables"]:
                by_ref.setdefault(t["ref"], []).append(t)
            new_fit, new_cut = {}, {}
            for ref, parts in by_ref.items():
                pages = sorted({p["page"] for p in parts})
                if len(pages) < 2:
                    continue
                spill = sum(p["h"] for p in parts if p["page"] != pages[0])
                # the figure that opens the same page as the table's first part
                cands = [f for f in mf2["figs"]
                         if f["page"] == pages[0] and f["idx"] >= 0 and f["h"] > 1.0]
                if not cands:
                    continue
                fg = max(cands, key=lambda f: f["h"])
                if fg["idx"] in fit:
                    continue
                need = spill + FIT_GAP - mf2["free"].get(str(pages[0]),
                                                         mf2["free"].get(pages[0], 0.0))
                if need <= 0:
                    continue
                # LEVER 1: the chapter's head band, down to its floor.
                sid_ = parts[0].get("sec") or ""
                if need > 0 and sid_ and sid_ not in cut:
                    give = min(need, BAND_FULL - BAND_MIN)
                    if give > 0.05:
                        new_cut[sid_] = BAND_FULL - give
                        need -= give
                        print(f"  fit pass {attempt+1}: cut {sid_}'s band "
                              f"{BAND_FULL:.2f}in -> {BAND_FULL - give:.2f}in "
                              f"to give its table {give:.2f}in")
                if need <= 0:
                    continue
                # LEVER 2: the figure, never below 85%.
                target = fg["h"] - need
                if target < FIT_FLOOR * fg["h"]:
                    print(f"  fit pass {attempt+1}: figure {fg['idx']} on p{pages[0]} "
                          f"would still need {1 - target/fg['h']:.0%} off — past the "
                          f"85% floor, left where it fell")
                    continue
                new_fit[fg["idx"]] = target
                print(f"  fit pass {attempt+1}: figure {fg['idx']} p{pages[0]} "
                      f"{fg['h']:.2f}in -> {target:.2f}in ({target/fg['h']:.0%}) "
                      f"so its table keeps {spill:.2f}in of rows")
            if new_fit or new_cut:
                fit.update(new_fit); cut.update(new_cut)
                continue

            new_snug = {}
            for mf in pg.evaluate(MEASURE_FIGS_JS):
                if mf["src"] in snug or not mf["atTop"] or mf["prevFree"] is None:
                    continue
                free, block = mf["prevFree"], mf["block"]
                if block <= 0 or free >= block or free < SNUG_FLOOR * block:
                    continue
                target = free - (block - mf["img"]) - SNUG_GAP
                if target <= 0:
                    continue
                new_snug[mf["src"]] = target
                print(f"snug pass {attempt+1}: {mf['src']} p{mf['page']} — "
                      f"{free:.2f}in free vs a {block:.2f}in block "
                      f"({free/block:.0%}) → image {mf['img']:.2f} → {target:.2f}in")
            if new_snug:
                snug.update(new_snug)
                continue

            secs = pg.evaluate(MEASURE_JS)
            new_tight, new_feed, new_loose = set(), set(), set()
            for s in secs:
                if not s["id"] or len(s["pages"]) < 2:
                    continue
                tail = s["pages"][-1]["h"]
                give = (GIVE_PER_PAGE * (len(s["pages"]) - 1)
                        + GIVE_TALL_PLATE * s["tall"] + GIVE_PLATE * s["small"])
                has_plate = (s["tall"] + s["small"]) > 0 or s.get("maps", 0) > 0
                # a plate already sitting on the tail page shouldn't be re-fed
                tail_has_plate = s["tailPhotos"] > 0 or s.get("tailMaps", 0) > 0
                if s["id"] in fed:
                    continue
                if s["id"] in tight:
                    # tighten didn't clear the tail — escalate to feeding it a plate
                    if has_plate and not tail_has_plate:
                        new_feed.add(s["id"]); tight.discard(s["id"])
                    continue
                if s["id"] in loose:
                    continue
                if tail <= give:
                    new_tight.add(s["id"])
                elif tail <= FEED_MAX_TAIL and has_plate and not tail_has_plate:
                    new_feed.add(s["id"])
                elif tail < 0.42 * CONTENT_H and not has_plate:
                    # thin tail, nothing to pull it back or feed it — set the chapter
                    # a notch more open so the tail page receives enough lines
                    new_loose.add(s["id"])
                elif tail < 0.42 * CONTENT_H and has_plate and not tail_has_plate:
                    # thin tail but the chapter has a plate to move down — feed it
                    new_feed.add(s["id"])
            if not new_tight and not new_feed and not new_loose:
                break
            tight |= new_tight; fed |= new_feed; loose |= new_loose
            if new_tight: print(f"feather pass {attempt+1}: tightening {sorted(new_tight)}")
            if new_feed:  print(f"feather pass {attempt+1}: feeding tail a plate {sorted(new_feed)}")
            if new_loose: print(f"feather pass {attempt+1}: loosening {sorted(new_loose)}")

        # FILL — last, and only once: the page shape is settled by now, and a
        # plate that grows into space nothing else wanted cannot move anything.
        grew = {}
        for mf in pg.evaluate(MEASURE_LAST_JS):
            if mf["src"] in fill or mf["free"] < FILL_MIN:
                continue
            target = min(mf["img"] + mf["free"] - 0.10, FILL_CAP)
            if target <= mf["img"] + 0.1:
                continue
            left = mf["free"] - (target - mf["img"])
            pad = left / 2 if (mf.get("alone") and left > 0.3) else 0.0
            grew[mf["src"]] = (target, pad)
            print(f"  fill: {mf['src']} p{mf['page']} closes the chapter with "
                  f"{mf['free']:.2f}in spare — {mf['img']:.2f}in -> {target:.2f}in"
                  + (f", centred on a sheet it owns (+{pad:.2f}in above)" if pad else ""))
        if grew:
            fill.update(grew)
            h = html
            for sid_, bh in cut.items():
                h = _cut_band(h, sid_, bh)
            for idx, target in sorted(fit.items()):
                h = _fit(h, idx, target)
            for src, ih in fill.items():
                h = _fill(h, src, ih)
            for sid in fed:
                h = _feed_tail(h, sid)
            for src, ih in snug.items():
                h = _snug(h, src, ih)
            for sid in loose:
                h = _add_class(h, sid, "loose")
            for sid in tight:
                h = _add_class(h, sid, "tight")
            open(render_path, "w", encoding="utf-8").write(
                h.replace("</head>", INJECT + "</head>"))
            n_dom = _paginate(pg, render_path, timeout_ms)

        if tight: print(f"feathered: {sorted(tight)}")
        if fed:   print(f"tail-fed:  {sorted(fed)}")
        if snug:  print(f"snugged:   "
                        f"{ {k: round(v,2) for k,v in snug.items()} }")
        if loose: print(f"loosened:  {sorted(loose)}")
        if fill:  print(f"filled:    "
                        f"{ {k: round(v[0],2) for k,v in fill.items()} }")
        if cut:   print(f"bands cut: "
                        f"{ {k: round(v,2) for k,v in cut.items()} }")
        if fit:   print(f"fitted:    "
                        f"{ {k: round(v,2) for k,v in sorted(fit.items())} }")
        # ATELIER (model 2): the page map the composition loop reads — every
        # composed element with its sheet, box and paragraph id.
        try:
            pages = pg.evaluate(PAGEMAP_JS)
            import json as _json
            _json.dump(pages, open(os.path.join(BUILD, f"_pages-{pdf_name}.json"), "w"), indent=0)
            print(f"page map: {len(pages)} pages -> _pages.json")
        except Exception as e:
            print("page map failed:", e)
        pg.pdf(path=os.path.join(BUILD, pdf_name),
               print_background=True, prefer_css_page_size=True,
               display_header_footer=False,
               margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
        b.close()

    n_pdf = len(PdfReader(os.path.join(BUILD, pdf_name)).pages)
    print(f"paginated: {n_dom} pages in DOM -> {n_pdf} pages in {pdf_name}")
    assert n_dom == n_pdf, "DOM page count != PDF page count — a page split or vanished in print"
    return n_pdf

if __name__ == "__main__":
    render()
