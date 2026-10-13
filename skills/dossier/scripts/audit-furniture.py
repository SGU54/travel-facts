#!/usr/bin/env python3
"""Stage G — the FURNITURE gate. The check that catches the continuation-page bug.

The failure it exists for: a build where chapter-START pages look right (margin,
running head) while CONTINUATION pages start 2-3px from the trim with no furniture
at all — because the furniture mechanism only fired once per chapter. Rome shipped
that. Every dead-end fix (header templates, @page margins, position:fixed) passed
a glance at page 1 and failed on page 2.

So this gate checks EVERY page, and it checks four things per page:

  1. PAINT    — the paper colour reaches all four trim edges. No white band of any
                width, anywhere. (Chromium clips template backgrounds; an unpainted
                @page margin is white; both render as bands against coloured paper.)
  2. RUNHEAD  — ink in the head band on every page that needs one (continuation
                pages; openers legitimately suppress it, so a missing head is only
                a failure when the foot says the page isn't an opener — we accept
                either, but a page with NEITHER head ink NOR a folio fails).
  3. FOLIO    — ink in the foot band on every interior page. No exceptions except
                the cover.
  4. COLUMN   — body ink starts below the head band and ends above the foot band
                on every page. Margins are per-PAGE, not per-chapter.

Usage:  python3 audit-furniture.py <dossier.pdf> [--paper RRGGBB]
        exit 0 = every sheet is furnished and painted; anything else = list of pages
"""
import sys, os, glob, subprocess, tempfile

PAPER = "F6EEDB"          # override with --paper for another project's stock
TOL = 16                  # per-channel tolerance when matching the paper colour

# sheet fractions (robust to raster dpi). US Letter spec: head band ends 74/1056,
# body 92..984, foot band starts 984. Bands below include a small guard.
HEAD_BAND = (0.040, 0.076)     # where runhead ink legitimately sits
FOOT_BAND = (0.945, 0.975)     # where folio ink legitimately sits
HEAD_DEAD = (0.077, 0.086)     # must be clear: strip between runhead and body
FOOT_DEAD = (0.934, 0.944)     # must be clear: strip between body and folio

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    paper = PAPER
    if "--paper" in sys.argv:
        paper = sys.argv[sys.argv.index("--paper") + 1]
    pr, pg_, pb = int(paper[0:2], 16), int(paper[2:4], 16), int(paper[4:6], 16)
    pdf = args[0] if args else "dossier.pdf"
    if not pdf.lower().endswith(".pdf"):
        c = glob.glob(os.path.join(pdf, "*.pdf")); pdf = c[0] if c else sys.exit("no PDF")

    from PIL import Image
    bad = []
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(["pdftoppm", "-png", "-r", "72", pdf, f"{td}/p"], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        files = sorted(glob.glob(f"{td}/p-*.png"))
        for f in files:
            pno = int(os.path.basename(f).split("-")[1].split(".")[0])
            im = Image.open(f).convert("RGB"); W, H = im.size
            gray = im.convert("L"); gp = list(gray.getdata())

            # 1. PAINT — walk all four edges; any near-white pixel = unpainted band
            def unpainted(x, y):
                r, g, b = im.getpixel((x, y))
                near_paper = abs(r-pr) <= TOL and abs(g-pg_) <= TOL and abs(b-pb) <= TOL
                return (not near_paper) and (r > 235 and g > 235 and b > 230)
            edge_pts = ([(x, 1) for x in range(0, W, 4)] + [(x, H-2) for x in range(0, W, 4)]
                        + [(1, y) for y in range(0, H, 4)] + [(W-2, y) for y in range(0, H, 4)])
            white = sum(1 for x, y in edge_pts if unpainted(x, y))
            if white > 4:
                bad.append((pno, f"UNPAINTED edge ({white} white samples) — a margin band is not paper"))

            def band_ink(y0f, y1f, thresh=130):
                # furniture is small muted type: at 72dpi it rasters ~140-180 luminance
                # against ~237 paper, so the furniture bands use a higher threshold
                n = 0
                for y in range(int(H*y0f), int(H*y1f)):
                    n += sum(1 for x in range(int(W*0.08), int(W*0.92), 3) if gp[y*W+x] < thresh)
                return n

            if pno == 1:
                continue   # the cover is full-bleed by design: no furniture, own grid

            # 2/3. FURNITURE — folio always; runhead OR opener (openers suppress it)
            if band_ink(*FOOT_BAND, thresh=195) < 6:
                bad.append((pno, "NO FOLIO — foot band is empty"))
            # (head band may be empty only on opener pages; a page with an empty head
            #  band AND an empty first body region isn't an opener — it's unfurnished)
            if band_ink(*HEAD_BAND, thresh=195) < 6 and band_ink(0.087, 0.20) < 6:
                bad.append((pno, "NO RUNHEAD and no opener content — page is unfurnished"))

            # 4. COLUMN — the dead strips between furniture and body must be clear
            if band_ink(*HEAD_DEAD) > 8:
                bad.append((pno, "body ink ABOVE the column — top margin lost"))
            if band_ink(*FOOT_DEAD) > 8:
                bad.append((pno, "body ink BELOW the column — bottom margin lost"))

    print(f"\n  FURNITURE — {len(files)} pages, every sheet checked\n  " + "-"*46)
    if not bad:
        print("  \u2713 every sheet: painted to the trim, furnished, body inside the column")
        print("  furniture gate: PASS")
        return 0
    for pno, msg in bad[:20]:
        print(f"  \u2717 p{pno}: {msg}")
    print("\n  A page failed the sheet contract. If continuation pages fail while chapter")
    print("  starts pass, the furniture mechanism is per-chapter instead of per-page —")
    print("  see references/page-spec.md (the paged page model).")
    return 1

if __name__ == "__main__":
    sys.exit(main())
