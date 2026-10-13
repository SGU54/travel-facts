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
    "if(el.querySelector('.pagedjs_page_content h1')){"
    "el.querySelectorAll('.pagedjs_margin-top-left,.pagedjs_margin-top-right')"
    ".forEach(function(m){m.style.visibility='hidden'});}}}"
    "P.registerHandlers(O);};</script>"
    "<script src=\"paged.polyfill.js\"></script>"
    "<script>/* opener handler disabled: chapters flow, every page keeps its runhead */</script>"
    # The inject lives in <head>. With LOCAL font files document.fonts.ready can
    # resolve while the parser is still inside <head>, so preview() would run
    # against a document with no <body> and Paged's wrapContent() throws on a
    # null querySelector("body"). Gate the whole chain on DOM readiness first.
    # This book ships its own assets/fonts/, so it takes that path every time.
    "<script>(function(){function go(){"
    "document.fonts.ready.then(function(){"
    "return Promise.all(Array.from(document.images).map("
    "function(i){return i.decode().catch(function(){})}));}).then(function(){"
    "window.PagedPolyfill.preview().then(function(f){window.__pagedDone=f.total;})"
    ".catch(function(e){window.__pagedErr=(e&&e.stack)?e.stack:String(e);});});}"
    "if(document.readyState==='loading'){"
    "document.addEventListener('DOMContentLoaded',go);}else{go();}})();</script>"
)

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

# Per-DIAGRAM geometry: which page each one landed on, whether it sits at the
# very top of that page (i.e. it opened the page), and how much column is left
# unused at the foot of the page BEFORE it. That last number is what decides
# whether shrinking the diagram would pull it back a page.
MEASURE_MAPS_JS = """
() => {
  const PX = 96;
  const pages = [...document.querySelectorAll('.pagedjs_page')];
  const boxOf = pg => pg.querySelector('.pagedjs_page_content');
  // Only things that actually put ink down. Walking every element counted the
  // full-height wrappers too, so the foot of the page always measured as 0.
  const drawn = box => {
    const out = [];
    box.querySelectorAll('*').forEach(el => {
      const tag = el.tagName;
      const leaf = el.children.length === 0;
      if (!leaf && !/^(IMG|FIGURE|TABLE|HR|FIGCAPTION)$/.test(tag)) return;
      const r = el.getBoundingClientRect();
      if (r.height > 0.5 && (leaf ? (el.textContent || '').trim() || /^(IMG|HR)$/.test(tag) : true))
        out.push(r);
    });
    return out;
  };
  const out = [];
  pages.forEach((pg, pi) => {
    const box = boxOf(pg);
    if (!box) return;
    box.querySelectorAll('figure.map').forEach(fig => {
      const im = fig.querySelector('img');
      if (!im) return;
      const fr = fig.getBoundingClientRect();
      // getBoundingClientRect EXCLUDES margins, but the page has to find room
      // for them too — figure{margin:14px 0} is 0.29in that the first version
      // of this measurement ignored, so a diagram was shrunk to a size that
      // still would not fit and stayed on its own page anyway.
      const fs = getComputedStyle(fig);
      const fmar = (parseFloat(fs.marginTop) || 0) + (parseFloat(fs.marginBottom) || 0);
      // nothing drawn above it on this page => it opened the page
      const above = drawn(box).filter(r => r.bottom <= fr.top + 1).length;
      let prevFree = null;
      if (pi > 0) {
        const prev = boxOf(pages[pi - 1]);
        if (prev) {
          const pr = prev.getBoundingClientRect();
          const rs = drawn(prev);
          const low = rs.length ? Math.max(...rs.map(r => Math.min(r.bottom, pr.bottom))) : pr.top;
          prevFree = (pr.bottom - low) / PX;
        }
      }
      out.push({
        src: (im.getAttribute('src') || '').split('/').pop(),
        page: pi + 1,
        block: (fr.height + fmar) / PX,
        img: im.getBoundingClientRect().height / PX,
        atTop: above === 0,
        prevFree: prevFree
      });
    });
  });
  return out;
}
"""

# "photo tall" exists here too, so match any photo-classed figure.
_PHOTO_RE = r'<figure class="photo[^"]*"[^>]*>.*?</figure>'
_MAP_RE = r'<figure class="map"[^>]*>.*?</figure>'

def _feed_tail(h, sid):
    """Move the section's plate to the chapter's end, right before the endmark,
    so it lands on (and fills) the tail page.

    The movable plate is the DIAGRAM, never the photo. Every chapter now opens
    with a photo directly under its head, and that position is the whole point of
    it. The earlier rule preferred to move the photo, which silently pulled the
    opening image down to the chapter's last page and left seven openers bare.
    A chapter with no diagram to move keeps its tail as it is, rather than being
    robbed of its opener to fill it."""
    start = h.index(f'id="{sid}"')
    end = h.index("</section>", start)
    seg = h[start:end]
    allmaps = list(re.finditer(_MAP_RE, seg, flags=re.S))
    if not allmaps:
        return h
    m = allmaps[-1]          # the LAST diagram in the chapter goes to its tail
    is_map = True
    plate = m.group(0)
    seg2 = seg.replace(plate, "", 1)
    # a fed plate becomes the chapter's CLOSING plate: tall, image-dominant
    if is_map:
        plate = plate.replace('<figure class="map"', '<figure class="map closing"', 1)
    else:
        plate = re.sub(r'<figure class="(photo[^"]*)"', r'<figure class="\1 closing"', plate, count=1)
    if '<div class="endmark">' in seg2:
        seg2 = seg2.replace('<div class="endmark">', plate + '<div class="endmark">', 1)
    else:
        seg2 = seg2 + plate
    return h[:start] + seg2 + h[end:]

SNUG_FLOOR = 0.85        # shrink only down to 85% of the standard block
SNUG_GAP   = 0.06        # breathing room so the fit is not hairline

def _snug(h, src, img_in):
    """Mark one diagram as snug and give it an explicit image height."""
    # NB: match any extra classes. _feed_tail runs first in the same loop and
    # renames the figure to "map closing", so an exact class="map" match here
    # silently did nothing on precisely the diagrams that most needed snugging.
    pat = re.compile(r'<figure class="map([^"]*)"([^>]*)>(\s*<img src="(?:[^"]*/)?'
                     + re.escape(src) + r'")')
    m = pat.search(h)
    if not m:
        return h
    extra = m.group(1).replace(" snug", "")
    return (h[:m.start()]
            + f'<figure class="map{extra} snug" style="--snug:{img_in:.2f}in"{m.group(2)}>'
            + m.group(3) + h[m.end():])


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

        tight, fed, loose, snug = set(), set(), set(), {}
        n_dom = 0
        for attempt in range(6):   # +2: a snug pass consumes an attempt
            h = html
            for sid in fed:
                h = _feed_tail(h, sid)
            for src, ih in snug.items():
                h = _snug(h, src, ih)
            for sid in loose:
                h = h.replace(f'class="dec chap" id="{sid}"', f'class="dec chap loose" id="{sid}"')
            for sid in tight:
                marked = h.replace(f'id="{sid}">', f'id="{sid}" data-t="1">')
                marked = re.sub(r'class="([^"]*)" id="%s" data-t="1"' % sid,
                                r'class="\1 tight" id="%s"' % sid, marked)
                assert f'class="dec chap tight" id="{sid}"' in marked or "tight" in marked, sid
                h = marked
            open(render_path, "w", encoding="utf-8").write(
                h.replace("</head>", INJECT + "</head>"))
            n_dom = _paginate(pg, render_path, timeout_ms)

            # FEATHER: (a) a small spill gets pulled back (.tight); (b) a tail too big
            # to pull back, in a chapter that holds a photo plate, gets FED the plate
            # (doctrine: chapter-break slack is where plates go), so the tail reads as
            # a designed closing-image page instead of a stranded fragment.
            # SNUG PASS — a diagram that opened a page of its own, where the
            # page before it was left with ALMOST enough room, is shrunk to fit
            # there rather than costing a whole sheet. Runs before the feather
            # decisions because it can remove the stranded tail they would
            # otherwise try to fix by moving things around.
            new_snug = {}
            for m in pg.evaluate(MEASURE_MAPS_JS):
                if m["src"] in snug or not m["atTop"] or m["prevFree"] is None:
                    continue
                free, block = m["prevFree"], m["block"]
                if block <= 0 or free >= block:
                    continue                      # it already fits, or no data
                if free < SNUG_FLOOR * block:
                    continue                      # too big a shrink to hide
                furniture = block - m["img"]      # caption + figure margins
                target = free - furniture - SNUG_GAP
                if target <= 0:
                    continue
                new_snug[m["src"]] = target
                print(f"snug pass {attempt+1}: {m['src']} p{m['page']} — "
                      f"{free:.2f}in free before it vs a {block:.2f}in block "
                      f"({free/block:.0%}) → image {m['img']:.2f}in → {target:.2f}in")
            if new_snug:
                snug.update(new_snug)
                continue                          # re-paginate with them shrunk

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

        if tight: print(f"feathered: {sorted(tight)}")
        if fed:   print(f"tail-fed:  {sorted(fed)}")
        if snug:  print(f"snugged:   "
                        f"{ {k: round(v,2) for k,v in snug.items()} }")
        if loose: print(f"loosened:  {sorted(loose)}")
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
