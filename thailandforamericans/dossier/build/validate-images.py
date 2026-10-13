#!/usr/bin/env python3
"""Stage E gate — validate hand-picked photos BEFORE they reach the build.

Every rule here was paid for by a real failure on Rome:
  · a 2:3 phone shot needs ~7in of height to fill the column → always reads as a stamp
  · a 3:1 CSS box with object-fit:cover silently ate 50-78% of every frame
  · a portrait letterboxed into a 1.6in strip showed ~15% of the photograph

Usage:  python3 validate-images.py <img-dir> [--fix]
        --fix crops offenders to 3:2 at their densest band (originals kept).
Exit 1 if anything fails and --fix wasn't passed.
"""
import sys, os, glob, shutil, statistics

MIN_W      = 1400          # below this, 653px @2x on paper is soft
TARGET_AR  = 1.5           # the book's plate shape (3:2)
AR_MIN     = 1.20          # 4:3 is fine
AR_MAX     = 1.95          # wider than 2:1 letterboxes badly

def aspect(p):
    from PIL import Image
    with Image.open(p) as im: return im.size, im.size[0]/im.size[1]

def densest_band(path, bands=9):
    """Where does the detail live? Returns the fractional centre of the busiest band."""
    from PIL import Image
    im = Image.open(path).convert('L').resize((150, 225))
    px = list(im.getdata()); W, H = 150, 225
    energy = []
    for b in range(bands):
        y0, y1 = int(b*H/bands), int((b+1)*H/bands)
        rows = [px[y*W:(y+1)*W] for y in range(y0, y1)]
        energy.append(statistics.mean(
            abs(r[i+1]-r[i]) for r in rows for i in range(0, W-1, 3)))
    b = energy.index(max(energy))
    return (b + 0.5) / bands

def crop_to_ar(path, target=TARGET_AR):
    from PIL import Image
    im = Image.open(path); W, H = im.size
    c = densest_band(path)
    th = int(W/target)
    if th >= H:                      # too wide instead: cut the sides, centred
        tw = int(H*target); left = max(0, (W-tw)//2)
        out = im.crop((left, 0, left+tw, H))
    else:
        top = max(0, min(H-th, int(c*H - th/2)))
        out = im.crop((0, top, W, top+th))
    return out, c

def main():
    d = sys.argv[1] if len(sys.argv) > 1 else "img"
    fix = "--fix" in sys.argv
    files = sorted(f for f in glob.glob(os.path.join(d, "*.jpg"))
                   if "_originals" not in f)
    if not files:
        print(f"no images in {d}/"); return 1
    bad = 0
    print(f"{'file':10} {'pixels':12} {'ar':>5}  verdict")
    for f in files:
        (w, h), ar = aspect(f)
        why = []
        if w < MIN_W:            why.append(f"only {w}px wide (want ≥{MIN_W})")
        if ar < AR_MIN:          why.append(f"PORTRAIT {ar:.2f} — needs ~7in of height to fill the column")
        elif ar > AR_MAX:        why.append(f"too wide {ar:.2f} — will letterbox")
        name = os.path.basename(f)
        if not why:
            print(f"{name:10} {w}x{h:<6} {ar:5.2f}  OK")
            continue
        bad += 1
        print(f"{name:10} {w}x{h:<6} {ar:5.2f}  FAIL — {'; '.join(why)}")
        if fix and (ar < AR_MIN or ar > AR_MAX):
            od = os.path.join(d, "_originals"); os.makedirs(od, exist_ok=True)
            shutil.copy(f, os.path.join(od, name))
            out, c = crop_to_ar(f)
            out.save(f, quality=90, optimize=True)
            print(f"{'':10} → cropped to {out.size} at the densest band ({100*c:.0f}% down); "
                  f"original in {od}/")
            bad -= 1
    print()
    if bad:
        print(f"{bad} image(s) FAILED. Re-run with --fix, or ask for replacements.")
        return 1
    print(f"all {len(files)} images pass — every plate will render full-column.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
