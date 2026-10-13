#!/usr/bin/env python3
"""Stage G — the GEOMETRY gate. Does every page obey the specimen's zones?

The spec (references/page-spec.md): body content lives in 92–984px; the head band (40–74)
and foot band (984–1056) carry furniture ONLY. A build that lets body text into a band
produces the footer-colliding-with-prose mess. This measures each rendered page and fails
any page with body ink in a forbidden band.

The folio and running head are THEMSELVES in the bands, so we can't just check "any ink."
We check for ink OUTSIDE the narrow furniture lines — i.e. body prose that has bled up into
the head band or down into the foot band beyond where the single furniture line sits.

Usage:  python3 audit-geometry.py <dossier.pdf>
"""
import sys, os, glob, subprocess, tempfile
from pypdf import PdfReader

# fractions of page height (robust to the exact raster resolution)
# the DEAD ZONES: strips that must be empty because they sit BETWEEN furniture and body.
# Furniture legitimately occupies the band edges; only the gap must be clear.
HEAD_DEAD = (0.074, 0.088)     # dead strip below the running head, above body
FOOT_DEAD = (0.930, 0.945)     # dead strip below body, above the folio

def main():
    pdf = sys.argv[1] if len(sys.argv) > 1 else "dossier.pdf"
    if not pdf.lower().endswith(".pdf"):
        c = glob.glob(os.path.join(pdf, "*.pdf")); pdf = c[0] if c else sys.exit("no PDF")
    from PIL import Image
    n_pages = len(PdfReader(pdf).pages)
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(["pdftoppm", "-jpeg", "-r", "72", pdf, f"{td}/p"], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        bad = []
        for f in sorted(glob.glob(f"{td}/p-*.jpg")):
            pno = int(os.path.basename(f).split("-")[1].split(".")[0])
            if pno == 1:      # cover is full-bleed by design
                continue
            im = Image.open(f).convert("L"); W, H = im.size; px = list(im.getdata())
            def dead_zone_ink(y0f, y1f):
                # ANY substantial ink in the dead zone = body has bled into furniture space
                inky_rows = 0
                for y in range(int(H*y0f), int(H*y1f)):
                    row_ink = sum(1 for x in range(int(W*0.12), int(W*0.88), 3) if px[y*W+x] < 120)
                    if row_ink > 10:
                        inky_rows += 1
                return inky_rows
            if dead_zone_ink(*HEAD_DEAD) > 3:
                bad.append((pno, "head", dead_zone_ink(*HEAD_DEAD)))
            if dead_zone_ink(*FOOT_DEAD) > 3:
                bad.append((pno, "foot", dead_zone_ink(*FOOT_DEAD)))
    print(f"\n  GEOMETRY — {n_pages} pages against the specimen\n" + "  " + "-"*46)
    if not bad:
        print("  \u2713 every page respects the head/foot bands — furniture and body never touch")
        print("  geometry gate: PASS")
        return 0
    print("  GEOMETRY GATE — FAILURES:")
    for pno, band, rows in bad[:12]:
        print(f"  \u2717 p{pno}: body text in the {band.upper()} band ({rows} inked rows where furniture is ~2-3)")
    print("\n  Body content has entered a furniture band. Inset the body to 92\u2013984px and")
    print("  pin the running head/folio into the bands (references/page-spec.md, verbatim CSS).")
    return 1

if __name__ == "__main__":
    sys.exit(main())
