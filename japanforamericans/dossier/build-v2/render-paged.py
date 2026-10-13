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
    "<script>window.__openerHandler(window.Paged);</script>"
    # The inject lives in <head>. With LOCAL font files document.fonts.ready can
    # resolve while the parser is still inside <head>, so preview() would run
    # against a document with no <body> and Paged's wrapContent() throws on a
    # null querySelector("body"). Gate the whole chain on DOM readiness first.
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
    // section.chap, NOT section.dec. The nine decisions carry "dec chap decision";
    // the sixteen prose chapters carry "chap" alone — so selecting .dec made the
    // whole feather pass blind to two thirds of the book, and the EATING chapter's
    // two-paragraph tail sat stranded on p.22 because the machinery built to pull
    // exactly that back was never looking at it. .toc is excluded: the contents
    // page is a fixed layout and must not be feathered.
    pg.querySelectorAll('.pagedjs_page_content section.chap:not(.toc)').forEach(s => {
      const ref = s.getAttribute('data-ref');
      const id = s.id || (secs[ref] && secs[ref].id) || null;
      const h = s.getBoundingClientRect().height;
      // figure.plate, NOT figure.photo — this book has never had a .photo, so
      // this list was always empty: the "feed the tail a plate" branch could
      // never fire and `give` never received its plate allowance. And these
      // plates are height:auto, so classify by MEASURED height; the old test
      // sniffed for "3.3" in an inline style none of them carries.
      const imgs = s.querySelectorAll('figure.plate img');
      let tall = 0, small = 0;
      imgs.forEach(i => { if (i.getBoundingClientRect().height >= 280) tall++; else small++; });
      if (!secs[ref]) secs[ref] = { id: id, pages: [], tall: 0, small: 0, tailPhotos: 0 };
      if (id && !secs[ref].id) secs[ref].id = id;
      secs[ref].pages.push({ page: pi + 1, h: h });
      secs[ref].tall += tall; secs[ref].small += small;
      secs[ref].tailPhotos = imgs.length;   // overwritten by each fragment; last wins = tail
    });
  });
  return Object.values(secs);
}
"""

def _add_class(h, sid, cls):
    """Add `cls` to the section carrying id=sid, whatever its existing classes.

    Raises if the section is not found or the class does not land — a feather
    pass that cannot place its class must fail loudly, not carry on printing
    that it worked.
    """
    pat = re.compile(r'(<section class="([^"]*)" id="%s")' % re.escape(sid))
    m = pat.search(h)
    if not m:
        raise AssertionError(f"feather: no <section ... id={sid!r}> to mark .{cls}")
    if cls in m.group(2).split():
        return h
    out = h[:m.start()] + f'<section class="{m.group(2)} {cls}" id="{sid}"' + h[m.end():]
    assert f'class="{m.group(2)} {cls}" id="{sid}"' in out, sid
    return out


# The plate tag carries an id: <figure class="plate" id="plate-A04">. A pattern
# ending at `">` right after the class matches none of them.
_PHOTO_RE = r'<figure class="plate[^"]*"[^>]*>.*?</figure>'

def _feed_tail(h, sid):
    """Move the section's photo plate to the chapter's end, right before the endmark,
    so it lands on (and fills) the tail page."""
    start = h.index(f'id="{sid}"')
    end = h.index("</section>", start)
    seg = h[start:end]
    m = re.search(_PHOTO_RE, seg, flags=re.S)
    if not m:
        # The caller only asks to feed a section MEASURE_JS just counted a plate
        # in, so failing to find one here means the two disagree about the
        # markup — which is exactly how this went unnoticed: the pass announced
        # "feeding tail a plate", this returned the document untouched, and the
        # stranded page stayed stranded.
        raise AssertionError(
            f"feather: section {sid!r} was selected for tail-feeding but no "
            f"plate matched {_PHOTO_RE!r} inside it")
    plate = m.group(0)
    seg2 = seg.replace(plate, "", 1)
    # A fed plate becomes the chapter's CLOSING plate. The class rewritten here
    # has to be the one the markup actually uses — this said "photo", which this
    # book has never emitted, so even had the branch fired the class would not
    # have landed.
    plate = re.sub(r'<figure class="(plate[^"]*)"', r'<figure class="\1 closing"', plate, count=1)
    if '<div class="endmark">' in seg2:
        seg2 = seg2.replace('<div class="endmark">', plate + '<div class="endmark">', 1)
    else:
        seg2 = seg2 + plate
    return h[:start] + seg2 + h[end:]

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
      const tag = el.tagName.toUpperCase();
      if (!leaf && !/^(IMG|FIGURE|TABLE|HR|FIGCAPTION|SVG)$/.test(tag)) return;
      const e = el.getBoundingClientRect();
      if (e.height > 0.5 && (leaf ? ((el.textContent||'').trim() || /^(IMG|HR)$/.test(tag)) : true))
        out.push(e);
    });
    return out;
  };
  const out = [];
  pages.forEach((pg, pi) => {
    const box = boxOf(pg); if (!box) return;
    box.querySelectorAll('figure').forEach(fig => {
      // an inline <svg> is as much a figure as an <img>; keying only on img
      // made every drawn diagram in this book invisible to the snug rule.
      const art = fig.querySelector('img, svg'); if (!art) return;
      const key = fig.getAttribute('data-fig'); if (key === null) return;
      const fr = fig.getBoundingClientRect();
      const fs = getComputedStyle(fig);
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
      // Anything with break-before:avoid immediately after the figure has to
      // land on the same page as it — the endmark does. Budgeting only for the
      // figure shrank it to a size that still did not fit, so it moved to the
      // page anyway and sat there alone.
      let glued = 0;
      let sib = fig.nextElementSibling;
      while (sib) {
        const ss = getComputedStyle(sib);
        if (ss.breakBefore !== 'avoid' && ss.pageBreakBefore !== 'avoid') break;
        const sr = sib.getBoundingClientRect();
        glued += sr.height + (parseFloat(ss.marginTop)||0) + (parseFloat(ss.marginBottom)||0);
        sib = sib.nextElementSibling;
      }
      const sec = fig.closest('section');
      out.push({ key: key, kind: art.tagName.toLowerCase(),
                 sec: sec ? (sec.id || sec.getAttribute('data-ref') || '') : '',
                 page: pi+1, block: (fr.height+fmar)/PX,
                 art: art.getBoundingClientRect().height/PX,
                 glued: glued/PX,
                 atTop: above === 0, prevFree: prevFree });
    });
  });
  return out;
}
"""

SNUG_FLOOR = 0.70        # 0.85 is the comfortable band; 0.70 is the floor at
                         # which a shrink is still defensible. Two diagrams in
                         # this book sit at 74% and cost a whole sheet each.
SNUG_GAP   = 0.14        # real clearance — 0.06 left figures adrift by
                         # hundredths of an inch and they broke anyway

def _snug(h, key, art_in):
    """Mark one figure snug and give its artwork an explicit height. Addressed
    by data-fig, which survives _feed_tail moving the figure about."""
    pat = re.compile(r'<figure class="([^"]*)"([^>]*?)data-fig="' + re.escape(key) + r'"([^>]*)>')
    m = pat.search(h)
    if not m:
        return h
    cls = m.group(1).replace(" snug", "")
    rest = (m.group(2) + m.group(3)).replace(' style="--snug:', ' data-old-style="--snug:')
    return (h[:m.start()]
            + f'<figure class="{cls} snug" style="--snug:{art_in:.2f}in"{rest}'
            + f'data-fig="{key}">' + h[m.end():])

_PHOTO_RE = r'<figure class="photo">.*?</figure>'

def _feed_tail(h, sid):
    """Move the section's photo plate to the chapter's end, right before the endmark,
    so it lands on (and fills) the tail page."""
    start = h.index(f'id="{sid}"')
    end = h.index("</section>", start)
    seg = h[start:end]
    m = re.search(_PHOTO_RE, seg, flags=re.S)
    if not m:
        return h
    plate = m.group(0)
    seg2 = seg.replace(plate, "", 1)
    # a fed plate becomes the chapter's CLOSING plate: tall, image-dominant
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

    # portable browser lookup: the Linux container path first, then macOS's
    # playwright cache, then playwright's own resolution.
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
        snug_secs = set()
        snug_tries, snug_base = {}, {}
        n_dom = 0
        for attempt in range(7):   # a snug pass consumes an attempt
            h = html
            for sid in fed:
                h = _feed_tail(h, sid)
            for fkey, ih in snug.items():
                h = _snug(h, fkey, ih)
            # Both of these MUST match any section class, not just a decision's.
            # The loose branch used to be a literal replace of
            # class="dec chap decision", which exists on the nine decisions and
            # nowhere else — so for a prose chapter it silently matched nothing
            # while the log above happily announced "loosening <id>". A pass that
            # reports work it did not do is worse than one that does nothing.
            # The assert is per-section for the same reason: `or "tight" in marked`
            # passed as soon as ANY section anywhere carried the class.
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
            new_snug = {}
            for mf in pg.evaluate(MEASURE_FIGS_JS):
                if not mf["atTop"] or mf["prevFree"] is None:
                    continue
                # A figure can measure as FITTING and still be pushed to its own
                # page: the paginator's usable area is smaller than the content
                # box we measure. So a page-opening figure is allowed to be
                # re-snugged, a notch at a time, until it actually lands back —
                # bounded by SNUG_FLOOR of the size it started at.
                tries = snug_tries.get(mf["key"], 0)
                if tries >= 4:
                    continue
                free, block = mf["prevFree"], mf["block"]
                need = block + mf.get("glued", 0)
                # A figure can measure as FITTING (free >= need) and still be
                # pushed to its own page — two diagrams here sat at 102% and
                # broke anyway, adrift by hundredths of an inch. So the skip is
                # only for figures genuinely too big; anything from the floor
                # upward gets nudged down to a size with real clearance. The
                # cap means a roomy page never ENLARGES a figure.
                if need <= 0 or free < SNUG_FLOOR * need:
                    continue
                fit = free - (block - mf["art"]) - mf.get("glued", 0) - SNUG_GAP
                nudge = mf["art"] * 0.92          # it "fits" and broke anyway
                target = min(fit, nudge)
                base = snug_base.setdefault(mf["key"], mf["art"])
                if target <= 0 or target < SNUG_FLOOR * base:
                    continue
                if target >= mf["art"] - 0.02:
                    continue
                new_snug[mf["key"]] = target
                snug_tries[mf["key"]] = tries + 1
                if mf.get("sec"): snug_secs.add(mf["sec"])
                print(f"snug pass {attempt+1}: fig {mf['key']} ({mf['kind']}) p{mf['page']} — "
                      f"{free:.2f}in free vs {need:.2f}in needed "
                      f"({free/need:.0%}) → art {mf['art']:.2f} → {target:.2f}in")
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
                if s["id"] in fed:
                    continue
                if s["id"] in tight:
                    # tighten didn't clear the tail — escalate to feeding it the plate
                    if (s["tall"] + s["small"]) > 0 and s["tailPhotos"] == 0:
                        new_feed.add(s["id"]); tight.discard(s["id"])
                    continue
                if s["id"] in loose:
                    continue
                if tail <= give:
                    new_tight.add(s["id"])
                elif tail <= FEED_MAX_TAIL and (s["tall"] + s["small"]) > 0 and s["tailPhotos"] == 0:
                    new_feed.add(s["id"])
                elif tail < 0.42 * CONTENT_H:
                    # thin tail, nothing to pull it back or feed it — set the chapter
                    # a notch more open so the tail page receives enough lines
                    new_loose.add(s["id"])
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
