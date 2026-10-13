#!/usr/bin/env python3
"""Stage G gate — do the pages hold a consistent, well-filled shape?

Reads the RENDERED PDF, not the DOM. This matters: once chapters FLOW (layout.md), the
HTML has no per-page divs — the print engine makes the pages — so a DOM measurement sees
only the fixed pages and reports a mirage (10 pages when the book is 34). The PDF is the
only ground truth.

The folio sits in the bottom ~6% of every page; we scan above it so the running foot
doesn't read as "content reaches the bottom".

    Rome  (reads well)  — median fill ~71%
    Greece pre-flow     — median 60%, 25/41 pages half-empty  (FAIL)
    Greece post-flow    — median 85%                          (PASS)

Usage:  python3 audit-page-shape.py <dossier.pdf | dossier3.html>
        (if given the .html, it looks for a sibling dossier.pdf)
Needs:  pdftoppm (poppler-utils), Pillow
"""
import sys, os, subprocess, tempfile, glob, statistics

FLOOR_MEDIAN   = 66     # Rome sits at 71
MAX_UNDERFILL  = 0.30   # share of pages allowed below 60%
FOOTER_BAND    = 0.94   # ignore ink below this (the folio)
INK            = 145

def find_pdf(arg):
    if arg.lower().endswith(".pdf"):
        return arg
    # given the html — use a sibling dossier.pdf
    cand = os.path.join(os.path.dirname(os.path.abspath(arg)), "dossier.pdf")
    if os.path.exists(cand):
        return cand
    sys.exit(f"page-shape gate reads the rendered PDF; no PDF found next to {arg}")

def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else "dossier.pdf"
    pdf = find_pdf(arg)
    from PIL import Image
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(["pdftoppm", "-jpeg", "-r", "70", pdf, f"{td}/p"], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        fills = []
        for f in sorted(glob.glob(f"{td}/p-*.jpg")):
            n = int(os.path.basename(f).split("-")[1].split(".")[0])
            im = Image.open(f).convert("L"); W, H = im.size; px = list(im.getdata())
            last = 0
            for y in range(int(H*FOOTER_BAND), int(H*0.06), -3):
                if min(px[y*W+x] for x in range(0, W, 4)) < INK:
                    last = y; break
            fills.append((n, 100*last/H))
    v = [f for _, f in fills]
    med = statistics.median(v)
    under = [n for n, f in fills if f < 60]
    print(f"{len(fills)} pages · median fill {med:.0f}% · range {min(v):.0f}-{max(v):.0f}%\n")
    for n, f in fills:
        flag = "  ← nearly empty" if f < 45 else ("  ← half empty" if f < 60 else "")
        print(f"  p{n:>3} {f:>3.0f}%{flag}")
    print()
    fails = []
    if med < FLOOR_MEDIAN:
        fails.append(f"median fill {med:.0f}% (want >={FLOOR_MEDIAN}%; Rome is 71%) — the pages "
                     "are half empty. FLOW the chapters (layout.md); it is not a corpus limit.")
    if len(under) > len(fills)*MAX_UNDERFILL:
        fails.append(f"{len(under)}/{len(fills)} pages under 60% — pages {under[:10]}")
    # the first page is the cover; ignore it in the spread test
    body = v[1:] if len(v) > 1 else v
    if body and max(body) - min(body) > 62:
        fails.append(f"body fill ranges {min(body):.0f}-{max(body):.0f}% — pages are wildly "
                     "uneven. A book with a consistent page reads as designed; Rome is 57-90.")
    if fails:
        print("PAGE-SHAPE GATE — FAILURES:")
        for f in fails: print(f"  \u2717 {f}")
        print("\n  Fix = more argument per page (flow, another ledger row, the figure the")
        print("  corpus supports) — never bigger type or fatter margins.")
        return 1
    print("page-shape gate: PASS")
    return 0

if __name__ == "__main__":
    sys.exit(main())
