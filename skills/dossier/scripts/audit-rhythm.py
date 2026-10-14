#!/usr/bin/env python3
"""Stage G gate — the VISUAL rhythm of the book, not the prose.

Rome v2 shipped 1 plate in its first half and 8 in its second, with a 15-page text-only
run straight through the decisions — the analytical heart, and the place a skimming
buyer decides. Ten refinement loops never caught it, because every loop read PAGES and
this is a defect of the SEQUENCE.

READ THE PDF, NOT THE HTML (2026-10-14). The original gate split the HTML on
`class="page"` and called a page a photograph when it found a `PL. A` caption. Both
assumptions were wrong often enough that the gate was decorative:

  * `class="page"` only exists AFTER Paged.js has run in the browser. Builds that do
    not save the paginated DOM (Vietnam) gave it zero pages — on which it printed
    "0 pages" and then died on `row[0]`, an IndexError that looked like a crash
    rather than a gate that had measured nothing.
  * The `PL.` caption vocabulary is not fleet-wide. Measured over the eight shipped
    books: Greece has 31 photographs and ZERO `PL.` captions, Morocco 23 and zero,
    Japan 36 and two. The old detector would have scored all of Greece as text-only
    and passed it.

The rendered PDF is the only artefact every build produces and the only one that
shows what the reader actually sees, so that is what this reads now. A paginated
HTML still works if you pass one.

Usage:  python3 audit-rhythm.py <dossier.pdf | paginated.html>
"""
import sys, os, re

MAX_TEXT_RUN = 6      # more than this and the reader stops seeing the page
FIG_MIN      = 8      # vector paths on a page before it counts as carrying a figure
MIN_PLATES_PER_10PP = 4.0   # fleet floor, measured over the 8 shipped books
PAGE_END_MIN = 0.62   # body content ending above this is an unclosed page


def classify_pdf(path):
    """-> (row, pageinfo). row is the P/f/. string; pageinfo carries the geometry."""
    try:
        import pymupdf
    except ImportError:
        try:
            import fitz as pymupdf
        except ImportError:
            sys.exit("audit-rhythm needs PyMuPDF: pip install pymupdf")
    doc = pymupdf.open(path)
    row, info = "", []
    for pg in doc:
        n_img = len(pg.get_images())
        n_draw = len(pg.get_drawings())
        # Where does the body content stop? Render small and find the last inked
        # row, ignoring the running head and footer every page carries.
        pm = pg.get_pixmap(dpi=36, colorspace="gray")
        w, h = pm.width, pm.height
        buf = pm.samples
        top, bot = int(h * 0.06), int(h * 0.90)
        bg = 255
        for y in range(top, bot, 3):
            rowbytes = buf[y * pm.stride:y * pm.stride + w]
            bg = min(bg, max(rowbytes) if rowbytes else 255)
        last = 0
        for y in range(top, bot):
            rowbytes = buf[y * pm.stride:y * pm.stride + w]
            if any(b < 200 for b in rowbytes):
                last = y
        frac = (last - top) / max(1, bot - top)
        row += "P" if n_img else ("f" if n_draw >= FIG_MIN else ".")
        info.append({"img": n_img, "draw": n_draw, "end": frac})
    return row, info


def classify_html(path):
    h = open(path).read()
    pages = re.split(r'<(?:div|section)[^>]*class="[^"]*\bpage\b', h)[1:]
    row = ""
    for p in pages:
        if re.search(r'PL\. [A-Z]', p) or '<img' in p: row += "P"
        elif 'class="map' in p or 'class="fig' in p:  row += "f"
        else:                                         row += "."
    return row, [{"img": 0, "draw": 0, "end": 1.0} for _ in pages]


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: audit-rhythm.py <dossier.pdf | paginated.html>")
    path = sys.argv[1]
    if not os.path.exists(path):
        sys.exit(f"audit-rhythm: no such file: {path}")

    if path.lower().endswith(".pdf"):
        row, info = classify_pdf(path)
        src = "PDF"
    else:
        row, info = classify_html(path)
        src = "HTML"
    N = len(row)

    # A gate that measured nothing must SAY so and fail — never print a verdict.
    # This is the whole reason the Vietnam build shipped unchecked.
    print(f"audit-rhythm: read {N} pages from {src} {os.path.basename(path)}")
    if N == 0:
        print("\n  ✗ GATE COULD NOT RUN — zero pages found.")
        if src == "HTML":
            print("    This HTML has no `class=\"page\"` wrapper, which only exists after")
            print("    Paged.js runs. Pass the rendered PDF instead.")
        return 2
    print()

    for i in range(0, N, 10):
        print(f"  p{i+1:>2}-{min(i+10,N):<2}  {row[i:i+10]}")
    plates = row.count("P"); figs = row.count("f")
    per10 = plates / N * 10
    print(f"\n  P = photograph   f = figure   . = text only")
    print(f"  {plates} photographs, {figs} figure pages, {N - plates - figs} text-only"
          f"   ({per10:.1f} plates per 10pp)\n")

    fails = []
    # 1. the longest text-only run
    runs, cur, ln = [], row[0], 1
    for ch in row[1:]:
        if ch == cur: ln += 1
        else: runs.append((cur, ln)); cur, ln = ch, 1
    runs.append((cur, ln))
    pos, longest, at = 0, 0, 0
    for c, l in runs:
        if c == "." and l > longest: longest, at = l, pos
        pos += l
    if longest > MAX_TEXT_RUN:
        fails.append(f"a {longest}-page text-only run at p{at+1}–p{at+longest} "
                     f"(max {MAX_TEXT_RUN}) — the reader stops seeing the page")
    # 2. photographs must not clump in one half
    half = N // 2
    h1 = row[:half].count("P"); h2 = row[half:].count("P")
    if h1 and h2 and max(h1, h2) > 3 * min(h1, h2):
        fails.append(f"photographs clump: {h1} in the first half, {h2} in the second")
    elif h1 == 0 or h2 == 0:
        fails.append(f"photographs only in one half: {h1} first, {h2} second")
    # 3. a visual must land early
    first_vis = min([i for i, c in enumerate(row) if c in "Pf"] or [999])
    if first_vis > 6:
        fails.append(f"first visual at p{first_vis+1} — {first_vis} pages before anything "
                     "to see. Bring a figure or plate into the opening chapters")
    # 4. any visual at all, per 8-page window
    for i in range(0, max(0, N - 8), 4):
        w = row[i:i+8]
        if "P" not in w and "f" not in w:
            fails.append(f"p{i+1}–p{i+8}: eight pages with no visual of any kind")
            break
    # 5. plate DENSITY against the fleet floor. Vietnam shipped 2.7/10pp against a
    #    range of 4.7–8.7 with 98 usable frames sitting unused in its own library;
    #    every rhythm check above passed, because the plates it did have were evenly
    #    spread. Spacing and quantity are different defects.
    if per10 < MIN_PLATES_PER_10PP:
        want = int(MIN_PLATES_PER_10PP * N / 10) - plates
        fails.append(f"plate density {per10:.1f} per 10pp is below the fleet floor of "
                     f"{MIN_PLATES_PER_10PP} — add about {want} plates")
    # 6. Pages whose text runs out mid-page with nothing to close them. REPORTED,
    #    NEVER FAILED — measured across the eight shipped books, this is house style,
    #    not a defect: Turkey shipped pages ending at 39/41/43%, Morocco at 44/46/47%,
    #    Japan one at 33%, all accepted. Failing it would fire on five of the seven
    #    books already sold, which is how a gate teaches people to ignore it. It is
    #    printed because it is the cheapest list of places a spare plate would land.
    stubs = [(i+1, d["end"]) for i, d in enumerate(info)
             if d["end"] < PAGE_END_MIN and d["img"] == 0 and i >= 4]
    if stubs:
        shown = ", ".join(f"p{p} ({e*100:.0f}%)" for p, e in sorted(stubs, key=lambda x: x[1])[:8])
        more = f" (+{len(stubs)-8} more)" if len(stubs) > 8 else ""
        print(f"  note: {len(stubs)} page(s) end above {int(PAGE_END_MIN*100)}% with no "
              f"closing plate — candidates for a spare plate, not a failure:")
        print(f"        {shown}{more}\n")

    if fails:
        print("RHYTHM GATE — FAILURES:")
        for f in fails: print(f"  ✗ {f}")
        return 1
    print("rhythm gate: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
