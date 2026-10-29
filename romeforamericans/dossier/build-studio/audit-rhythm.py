#!/usr/bin/env python3
"""Stage G gate — the VISUAL rhythm of the book, not the prose.

Rome v2 shipped 1 plate in its first half and 8 in its second, with a 15-page text-only
run straight through the decisions — the analytical heart, and the place a skimming
buyer decides. Ten refinement loops never caught it, because every loop read PAGES and
this is a defect of the SEQUENCE.

Usage:  python3 audit-rhythm.py <dossier3.html>
"""
import sys, re

MAX_TEXT_RUN = 6     # more than this and the reader stops seeing the page

def main():
    h = open(sys.argv[1] if len(sys.argv) > 1 else "dossier3.html").read()
    pages = re.split(r'<(?:div|section)[^>]*class="[^"]*\bpage\b', h)[1:]
    N = len(pages)
    row = ""
    for p in pages:
        if re.search(r'PL\. [A-Z]', p):   row += "P"
        elif 'class="map' in p:           row += "f"
        else:                             row += "."
    print(f"{N} pages\n")
    for i in range(0, N, 10):
        print(f"  p{i+1:2}-{min(i+10,N):2}  {row[i:i+10]}")
    print("\n  P = photograph   f = figure   . = text only\n")

    fails = []
    # 1. the longest text-only run
    runs, cur, ln = [], row[0], 1
    for ch in row[1:]:
        if ch == cur: ln += 1
        else: runs.append((cur, ln)); cur, ln = ch, 1
    runs.append((cur, ln))
    pos, longest = 0, 0
    at = 0
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
    # 3. A visual should land within the first few pages of BODY. Front matter (cover,
    #    contract, how-to-read, contents) is text by design — typically 3-4 pages — so a
    #    first visual by roughly page 6 of a full book is healthy, not late. Only flag a
    #    genuinely long visual-free opening run.
    first_vis = min([i for i, c in enumerate(row) if c in "Pf"] or [999])
    if first_vis > 6:
        fails.append(f"first visual at p{first_vis+1} — {first_vis} pages before anything "
                     "to see. Bring a figure or plate into the opening chapters")
    # 4. any visual at all, per 8-page window
    for i in range(0, N - 8, 4):
        w = row[i:i+8]
        if "P" not in w and "f" not in w:
            fails.append(f"p{i+1}–p{i+8}: eight pages with no visual of any kind")
            break
    if fails:
        print("RHYTHM GATE — FAILURES:")
        for f in fails: print(f"  ✗ {f}")
        return 1
    print("rhythm gate: PASS")
    return 0

if __name__ == "__main__":
    sys.exit(main())
