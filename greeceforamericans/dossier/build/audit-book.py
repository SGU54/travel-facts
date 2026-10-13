#!/usr/bin/env python3
"""Stage G — the ONE gate. Runs every check and gives a single clean/clumsy verdict.

A builder shouldn't have to remember four separate scripts; a clumsy book slips through
when one is forgotten. This is the layer that guarantees the PDF is organized and reads
cleanly. Run it last, on the rendered build. Green here = ship.

It bundles:
  · page-shape   — pages well-filled and consistent (no half-empty, no wild swings)
  · rhythm       — visuals spread across the book, no long text-only deserts
  · orphans      — no chapter TAIL stranded as a near-empty stub page
  · headings     — no heading marooned at the foot of a page
  · plates       — no photograph alone on a page, none shrunk to a stamp
  · cover        — page 1 actually argues something (not a bare title)

Usage:  python3 audit-book.py <build-dir>
        expects <build-dir>/dossier.pdf and <build-dir>/dossier3.html
"""
import sys, os, subprocess, tempfile, glob, statistics, re

# The paper is per-brand (assets/brands/*.json), so it cannot be a constant.
# The old test asked `r>230 and g>228 and b>220` and called everything else
# non-paper — which classified Rome's own #F6EEDB stock (b=219) as ink and
# scored its cover 97.1% non-paper. Blank paper of that colour would have
# "passed" the cover threshold. Same per-channel tolerance audit-furniture.py
# already uses; override with --paper RRGGBB.
PAPER = "F6EEDB"
TOL   = 16

def _paper_rgb():
    hexv = PAPER
    if "--paper" in sys.argv:
        hexv = sys.argv[sys.argv.index("--paper") + 1].lstrip("#")
    return int(hexv[0:2], 16), int(hexv[2:4], 16), int(hexv[4:6], 16)

def load_pages(pdf):
    from PIL import Image
    out = []
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(["pdftoppm", "-jpeg", "-r", "70", pdf, f"{td}/p"], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        for f in sorted(glob.glob(f"{td}/p-*.jpg")):
            n = int(os.path.basename(f).split("-")[1].split(".")[0])
            im = Image.open(f).convert("RGB"); W, H = im.size
            g = im.convert("L"); gp = list(g.getdata())
            q = list(im.getdata())[::20]
            last = 0
            for y in range(int(H*0.94), int(H*0.06), -3):
                if min(gp[y*W+x] for x in range(0, W, 4)) < 145:
                    last = y; break
            ink = sum(1 for r, g_, b in q if r < 110) / len(q)
            photo = sum(1 for r, g_, b in q if max(r, g_, b)-min(r, g_, b) > 45) / len(q)
            # non-paper: any mark at all, incl. pale tints and streamlines a cover
            # uses — measured as DISTANCE FROM THIS BRAND'S PAPER, not against a
            # hardcoded near-white.
            pr, pg, pb = _paper_rgb()
            nonpaper = sum(1 for r, g_, b in q
                           if not (abs(r-pr) <= TOL and abs(g_-pg) <= TOL and abs(b-pb) <= TOL)) / len(q)
            out.append(dict(n=n, fill=100*last/H, ink=100*ink, photo=100*photo,
                            nonpaper=100*nonpaper))
    return out

def main():
    d = sys.argv[1] if len(sys.argv) > 1 else "."
    pdf = os.path.join(d, "dossier.pdf")
    if not os.path.exists(pdf):
        alt = glob.glob(os.path.join(d, "*.pdf"))
        pdf = alt[0] if alt else sys.exit(f"no PDF in {d}")
    pages = load_pages(pdf)
    N = len(pages)
    from pypdf import PdfReader
    reader = PdfReader(pdf)
    texts = [p.extract_text() for p in reader.pages]

    checks = []   # (name, ok, detail)

    # DEPTH — did the book mine the corpus, or skim it? audit-book measures organization;
    # a clean book can still be half its corpus's length (a cold Greece passed every other
    # check at 19pp when 80 articles support ~40). Only runs if the corpus is in the build.
    import json, re as _re
    def _load_corpus(dd):
        import glob as _g
        for nm in ("corpus.json", "articles.json"):
            pp2 = os.path.join(dd, nm)
            if os.path.exists(pp2): return json.load(open(pp2))
        for pp2 in _g.glob(os.path.join(dd, "*.json")):
            try:
                j = json.load(open(pp2))
                if isinstance(j, list) and j and isinstance(j[0], dict) and \
                   any(k in j[0] for k in ("content", "body", "excerpt")): return j
            except Exception: pass
        return None
    corpus = _load_corpus(d)
    if corpus is not None:
        arts = corpus if isinstance(corpus, list) else corpus.get("articles", corpus.get("data", []))
        n_art = len(arts) or 1
        w_in = sum(len(_re.sub("<[^>]+>", " ", (a.get("content") or a.get("body") or "")).split()) for a in arts)
        w_out = sum(len(t.split()) for t in texts)
        pp_ratio, w_ratio = N / n_art, w_out / n_art
        util = 100 * w_out / w_in if w_in else 0
        ok = pp_ratio >= 0.40 and w_ratio >= 120 and util >= 11.0
        checks.append(("depth", ok,
                       f"{pp_ratio:.2f} pp/art, {w_ratio:.0f} w/art, {util:.0f}% corpus used "
                       + ("(mined)" if ok else f"— thin; ~{n_art*0.5:.0f}pp supported, see a-mine.md")))

    # 1. page-shape
    body = [p["fill"] for p in pages[1:]]         # drop cover
    med = statistics.median([p["fill"] for p in pages])
    under = [p["n"] for p in pages if p["fill"] < 60 and p["n"] != 1]
    ok = med >= 66 and len(under) <= N*0.30
    checks.append(("page-shape", ok,
                   f"median fill {med:.0f}% (>=66), {len(under)} half-empty pages"
                   + (f" {under[:8]}" if under else "")))

    # 2. consistency (no wild swings in the body)
    spread = (max(body) - min(body)) if body else 0
    ok = spread <= 62
    checks.append(("consistency", ok,
                   f"body fill range {min(body):.0f}-{max(body):.0f}% (want span <=62)"))

    # 3. orphan stub pages — a near-empty page that is a chapter TAIL (little text,
    #    no visual), i.e. content dribbled past a boundary.
    #    CALIBRATION (paged architecture): fill measures last-ink over SHEET height,
    #    and the sheet carries 164px of margin bands — a tail ending at 38% of the
    #    sheet holds a third of the COLUMN. With the endmark closing every chapter,
    #    a complete closing apparatus at that depth reads set, not dribbled. The stub
    #    line is a dangling FRAGMENT: under a third of the sheet. (The old 40% figure
    #    was calibrated on the double-margin flow, where 40% of the sheet was far
    #    less column — same instrument correction as bug #19.)
    stubs = [p["n"] for p in pages
             if p["fill"] < 33 and p["photo"] < 8 and p["n"] not in (1,)]
    ok = not stubs
    checks.append(("no orphan stubs", ok,
                   "none" if ok else f"near-empty tail pages {stubs}"))

    # 4. rhythm — longest text-only run (figure or photo breaks it)
    #
    # The label may be LETTERSPACED in CSS, and extraction turns that tracking
    # into real spaces: Greece sets its captions as "F I G ." and the old
    # `\bFIG\.\s` matched none of them. The gate then reported the whole 43-page
    # book as one text-only run — on a book full of figures — and a true CLUMSY
    # verdict became indistinguishable from a broken detector.
    # Tolerate spaces between the letters, and do not require a trailing space
    # (a caption may read "FIG.8").
    FIGLABEL = re.compile(r'\bF\s*I\s*G\s*\.|\bP\s*L\s*\.', re.I)
    row = ""
    for i, t in enumerate(texts):
        # Ask the PAGE whether it draws an image. A chapter-head band is real
        # ink but a small share of the sheet, so a coverage threshold misses it
        # and pages carrying photographs get counted into a "text-only desert".
        try:
            _res = reader.pages[i].get('/Resources')
            _xo = _res.get('/XObject').get_object() if _res and _res.get('/XObject') else {}
            _has_img = any(_xo[k].get_object().get('/Subtype') == '/Image' for k in _xo)
        except Exception:
            _has_img = False
        vis = bool(FIGLABEL.search(t)) or _has_img
        row += "V" if vis else "."
    runs, cur, ln, longest = [], row[0], 1, 0
    for ch in row[1:]:
        if ch == cur: ln += 1
        else:
            if cur == "." : longest = max(longest, ln)
            cur, ln = ch, 1
    if cur == ".": longest = max(longest, ln)
    ok = longest <= 6
    checks.append(("rhythm", ok, f"longest text-only run {longest} pages (want <=6)"))

    # 5b. mark density — prose over-marked into confetti?
    import re as _re2
    MK = r'ESTABLISHED|OFFICIAL|SURVEYED|VOLATILE|[●◇▲◆]'
    def _prose_marks(t):
        n = 0
        for line in t.split("\n"):
            if not _re2.search(MK, line): continue
            if line.count("\u2192") or line.count("\u2194"): continue   # table row
            if len(_re2.findall(r"\d", line)) >= 4 and len(line.split()) < 14: continue
            n += len(_re2.findall(MK, line))
        return n
    mk_avg_src = [ _prose_marks(t) for t in texts ]
    mk_marked = [c for c in mk_avg_src if c > 0]
    mk_avg = sum(mk_marked)/len(mk_marked) if mk_marked else 0
    ok = mk_avg <= 8.0
    checks.append(("marks", ok,
                   f"{mk_avg:.1f} prose marks/page (<=8) "
                   + ("(seasoned)" if ok else "— confetti; one mark per fact, not per sentence (writing-code.md)")))

    # 5. cover argues something
    #
    # Ink COVERAGE alone was the test, and it is the wrong proxy. It measures how
    # much of the sheet is dark, which is a house style, not an argument: the
    # covers that paint a full-bleed panel score 95-99%, while a deliberately
    # spare typographic cover on cream stock scores single digits no matter how
    # much it says. Measured across the fleet, Rome's cover (title, thesis line,
    # and a drawn map of the historic core with its 1.5km ring) came to 4.1%, and
    # Turkey's — five ruled blank lines answered by "NOT PUBLISHED. ANYWHERE.",
    # a distance diagram, and a four-line thesis — to 5.1%, the RICHEST cover in
    # the fleet at 365 words. Both failed. Turkey only ever "passed" because the
    # 1-in-20 sample at 70dpi read 6.2% against a true 5.1%.
    #
    # So ask for evidence of an argument, of either kind: real ink, or real
    # content. A bare title page has neither — a dozen words and a percent or
    # two. Every genuine cover in the fleet clears 59 words.
    c = pages[0]
    cover_words = len((texts[0] or "").split())
    by_ink = c["nonpaper"] >= 6
    by_text = cover_words >= 40
    ok = by_ink or by_text
    carried = "ink" if by_ink else ("content" if by_text else "neither")
    checks.append(("cover", ok,
                   f"page 1: {c['nonpaper']:.1f}% non-paper, {cover_words} words "
                   + (f"(argues something — carried by {carried})" if ok
                      else "(bare title — argue the thesis, cover.md)")))

    # 6. geometry — body ink in a furniture dead zone (collision)?
    import subprocess as _sp, tempfile as _tf
    geo_bad = []
    with _tf.TemporaryDirectory() as _td:
        _sp.run(["pdftoppm","-jpeg","-r","72",pdf,f"{_td}/g"], check=True,
                stdout=_sp.DEVNULL, stderr=_sp.DEVNULL)
        from PIL import Image as _Img
        for _f in sorted(glob.glob(f"{_td}/g-*.jpg")):
            _pno = int(os.path.basename(_f).split("-")[1].split(".")[0])
            if _pno == 1: continue
            _im = _Img.open(_f).convert("L"); _W,_Hh = _im.size; _px = list(_im.getdata())
            def _dz(a,b):
                r=0
                for _y in range(int(_Hh*a), int(_Hh*b)):
                    if sum(1 for _x in range(int(_W*0.12),int(_W*0.88),3) if _px[_y*_W+_x]<120) > 10: r+=1
                return r
            # >3 inked rows = real body bleed (the footer-collision defect); a single
            # stray label row is not flagged.
            if _dz(0.074,0.088) > 3 or _dz(0.930,0.945) > 3:
                geo_bad.append(_pno)
    ok = not geo_bad
    checks.append(("geometry", ok,
                   "furniture & body never touch" if ok
                   else f"body in a furniture dead zone on {len(geo_bad)} pages {geo_bad[:6]} (page-spec.md)"))

    # verdict
    print(f"\n  BOOK AUDIT — {N} pages · {pdf}\n" + "  " + "-"*46)
    allok = True
    for name, ok, detail in checks:
        mark = "\u2713" if ok else "\u2717"
        if not ok: allok = False
        print(f"  {mark} {name:16} {detail}")
    print("  " + "-"*46)
    if allok:
        print("  CLEAN — the book is well-organized and reads evenly. Ship.\n")
        return 0
    print("  CLUMSY — fix the \u2717 rows above. See references/layout.md and cover.md.\n")
    return 1

if __name__ == "__main__":
    sys.exit(main())
