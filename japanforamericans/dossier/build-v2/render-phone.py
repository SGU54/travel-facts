#!/usr/bin/env python3
"""render-phone.py — the same book, set for a phone instead of a desk.

The review's finding: all six PDFs are US Letter, so a reader on the trip — the
person the "read it standing up" copy is addressed to — is pinching and panning a
216 mm page on a 70 mm screen.

The fix is not a smaller page with the same type. It is a NARROWER COLUMN. Print
sets ~6.8in of column; this sets ~3.8in. Displayed at the same screen width, every
glyph is 1.8× larger, without changing a single font-size — the gain comes from
the measure, not from scaling. Line length lands near 45 characters, which is
short for print and right for a phone held one-handed.

This does not replace the print book. It is written alongside it from the same
dossier3.html, so the two can never diverge in content.

Run:  python3 render-phone.py <build-dir>
Out:  <build-dir>/dossier-phone.pdf
"""
import os, re, sys, importlib.util

# 4.5 x 8 in ≈ 16:9, the shape of the device this is for. Margins are small
# because a screen has no thumb resting on it and no gutter to lose.
PHONE_CSS = r'''
/* ══ PHONE EDITION ══ set from the same source as the print book ══════════ */
@page{ size:4.5in 8in !important; margin:0.34in 0.30in 0.30in 0.30in !important;
  @top-left{ content:none !important } @top-right{ content:none !important }
  @bottom-left{ content:none !important } @bottom-center{ content:none !important }
  @bottom-right{ content:counter(page) !important } }
@page annex{ margin:0.34in 0.30in 0.30in 0.30in !important; }

/* Every cover is composed for an 8.5x11 sheet in absolute insets — a drawn
   device, a display line broken to a measured width, a rule that meets the trim.
   Re-typesetting that at a third of the area would be redesigning five covers.
   Scale the whole composition instead. Chromium's prefer-css-page-size takes ONE
   size for the document, so the cover sheet cannot be trimmed to the scaled
   height; the sheet below the composition is painted in the cover's own ground
   instead, which reads as a cover with air under it rather than as a fault. */
@page cover{ margin:0 !important;
  @top-left{ content:none !important } @top-right{ content:none !important }
  @bottom-left{ content:none !important } @bottom-center{ content:none !important }
  @bottom-right{ content:none !important } }
.pagedjs_page:has(.coverpage), .pagedjs_page:has(.cover),
.pagedjs_page:has(.coverpage) .pagedjs_page_content,
.pagedjs_page:has(.cover) .pagedjs_page_content,
.pagedjs_page:has(.coverpage) .pagedjs_area,
.pagedjs_page:has(.cover) .pagedjs_area,
.pagedjs_page:has(.coverpage) .pagedjs_sheet,
.pagedjs_page:has(.cover) .pagedjs_sheet{ background:__COVERBG__ !important; }
.cover, .coverpage{ width:8.5in !important; height:11in !important;
  min-height:0 !important; max-height:none !important;
  transform:scale(0.52941) !important; transform-origin:top left !important;
  overflow:hidden !important; }

/* Display type is sized for a 6.8in measure and overflows a 3.8in one. */
h1{ font-size:24px !important; line-height:1.12 !important; }
h1.t, h1.q{ font-size:24px !important; }
h2{ font-size:11px !important; }
.standfirst, .lead, .lede{ font-size:13px !important; line-height:1.5 !important; }
.dropcap::first-letter, .dropcap-l{ font-size:2.4em !important; }

/* Any art authored at a fixed inch height was measured against the print column;
   let it take the width it is given and keep its own aspect. */
figure img, .photo img, figure.head img, figure.closer img, .plate img,
.photo.band img, .drawnimg{ height:auto !important; max-width:100% !important;
  width:100% !important; object-fit:cover !important; max-height:2.6in !important; }
figure svg, svg{ width:100% !important; height:auto !important; }
figure{ break-inside:avoid; }
figcaption{ font-size:8px !important; line-height:1.4 !important; }

/* Three-column instruments do not fit a 3.8in measure. Let them break, shrink the
   type a step, and let the folio column collapse to its digits. */
table{ font-size:10.5px !important; break-inside:auto !important; }
td, th{ padding-left:0 !important; padding-right:6px !important; }
.ledger, .verdict, .forks, .kit, table.ledger{ break-inside:auto !important; }
.ledger td, .ledger th, table.ledger td{ padding:5px 6px !important; font-size:10.5px !important; }
.toc td{ font-size:10.5px !important; padding:2.6px 0 !important; }
.forks{ display:block !important; }
.fork{ margin-bottom:8px !important; }

/* A photograph that opened a chapter at 2.2in of a 9.3in page is a band; at 2.2in
   of a 7.4in page it is a wall. */
figure.head img, .photo.band img{ max-height:1.5in !important; }
figure.closer img, .photo.closing img{ max-height:2.0in !important; }
'''


def main():
    build = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
    src = os.path.join(build, 'dossier3.html')
    d = open(src, encoding='utf-8').read()
    k = d.rfind('</style>')
    assert k > 0, 'no </style> to append to'
    # Read the cover's own ground out of the book rather than guessing it: four of
    # the five inherit var(--paper) and Thailand paints a dark literal.
    css = d[:d.find('</style>')]
    bg = 'var(--paper)'
    for sel in (r'\.coverpage', r'\.cover'):
        for rule in re.findall(sel + r'\s*\{[^}]*\}', css):
            m = re.search(r'background(?:-color)?\s*:\s*([^;}!]+)', rule)
            if m:
                bg = m.group(1).strip(); break
        else:
            continue
        break
    out_html = os.path.join(build, 'dossier3-phone.html')
    open(out_html, 'w', encoding='utf-8').write(
        d[:k] + PHONE_CSS.replace('__COVERBG__', bg) + d[k:])
    print(f'  cover ground: {bg}')

    spec = importlib.util.spec_from_file_location(
        'rp', os.path.join(build, 'render-paged.py'))
    rp = importlib.util.module_from_spec(spec)
    sys.argv = [sys.argv[0], build]          # render-paged reads BUILD from argv
    spec.loader.exec_module(rp)
    n = rp.render(html_name='dossier3-phone.html', pdf_name='dossier-phone.pdf')
    print(f'  phone edition: {n} pages at 4.5 x 8in')
    return 0


if __name__ == '__main__':
    sys.exit(main())
