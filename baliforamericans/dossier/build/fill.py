# fill.py — ink-based page fill from the rendered PDF: the lowest non-paper row
# inside the body zone (92–984px of 1056), excluding the head and foot bands.
import sys, pymupdf as fitz
from PIL import Image
pdf = sys.argv[1] if len(sys.argv) > 1 else 'dossier.pdf'
doc = fitz.open(pdf); out = []
for i, pg in enumerate(doc):
    pix = pg.get_pixmap(dpi=36); im = Image.frombytes('RGB', [pix.width, pix.height], pix.samples).convert('L')
    w, h = im.size; top = int(92/1056*h) + 2; bot = int(984/1056*h) - 2
    px = im.load(); last = top
    for y in range(bot, top, -1):
        if any(px[x, y] < 225 for x in range(int(82/816*w), int(734/816*w), 2)):
            last = y; break
    out.append(round((last - top) / (bot - top) * 100))
short = [(i+1, f) for i, f in enumerate(out) if f < 62 and i > 0]
import statistics
print(f"{len(out)} pages · median fill {statistics.median(out[1:])}% · under 62%: {len(short)} {short}")
