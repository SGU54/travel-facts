"""Two-pass fix: re-render page 1 (cover) with NO header/footer template, then splice it
over the furnished page 1 in dossier.pdf. Keeps body furniture, removes cover furniture."""
import subprocess, os, pypdf
from playwright.sync_api import sync_playwright

BUILD = os.path.dirname(os.path.abspath(__file__))

# 1. build a cover-only HTML (reuse the exact cover html+css from the modules)
import design, covers
ff_block = __import__('build3')._font_face_block()
css = design.css(ff_block) + covers.cover_css() + "@page{margin:0!important;} .coverpage{height:11in!important;}"
cover_only = f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{covers.cover_html()}</body></html>'
open(os.path.join(BUILD,'cover_only.html'),'w',encoding='utf-8').write(cover_only)

# 2. render cover-only with NO furniture template
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
                          args=['--no-sandbox','--font-render-hinting=none'])
    pg = b.new_page(device_scale_factor=2)
    pg.set_viewport_size({'width':816,'height':1056})
    pg.goto('file://'+os.path.join(BUILD,'cover_only.html'), wait_until='networkidle')
    pg.evaluate('async()=>{if(document.fonts&&document.fonts.ready)await document.fonts.ready}')
    pg.wait_for_timeout(2000)
    pg.pdf(path=os.path.join(BUILD,'cover_only.pdf'), width='8.5in', height='11in',
           print_background=True, prefer_css_page_size=False,
           display_header_footer=False, margin={'top':'0in','bottom':'0in','left':'0in','right':'0in'})
    b.close()

# 3. splice: cover_only page over dossier page 1
main = pypdf.PdfReader(os.path.join(BUILD,'dossier.pdf'))
cov = pypdf.PdfReader(os.path.join(BUILD,'cover_only.pdf'))
w = pypdf.PdfWriter()
w.add_page(cov.pages[0])
for pg in main.pages[1:]:
    w.add_page(pg)
with open(os.path.join(BUILD,'dossier.pdf'),'wb') as f:
    w.write(f)
print(f"spliced: cover (no furniture) + {len(main.pages)-1} body pages = {len(main.pages)} total")
