from pathlib import Path
import sys,json
from playwright.sync_api import sync_playwright
root=Path('/tmp/astra-pins-review');sys.path[:0]=[str(root/'pins/scripts'),str(root/'pins/references')]
import make_pins as m
import pins_rome_example as ref
out={}
with sync_playwright() as pw:
 b=pw.chromium.launch();page=b.new_page(viewport={'width':1000,'height':1500},device_scale_factor=2)
 p=next(p for p in ref.PINS if p['slug']=='rome-3-days-list')
 page.set_content(m.tpl_b(ref.SITE,p,True),wait_until='networkidle');page.evaluate('document.fonts.ready')
 page.add_style_tag(content='.foot {margin: auto -62px -58px;}')
 out['footer_fixed']=page.locator('.foot').bounding_box()
 page.screenshot(path=str(root/'footer-fixed.png'))
 pr=b.new_page(viewport={'width':236,'height':354}); errors=[];pr.on('console',lambda msg:errors.append(msg.text))
 f=root/'rendered/rome-3-days-list.png'
 pr.set_content(f"<body style='margin:0'><img src='{f.as_uri()}' style='width:236px;display:block'></body>");pr.wait_for_timeout(200)
 out['native_proof']={'image':pr.locator('img').evaluate('(i)=>({complete:i.complete,naturalWidth:i.naturalWidth})'),'console':errors}
 # Proposed proof repair: direct resize of the screenshot bytes is independent of URL origins.
 # Offline fallback test: do not let remote resources through.
 off=b.new_page(viewport={'width':1000,'height':1500},device_scale_factor=2);off.route('**/*',lambda r:r.abort())
 pp=next(p for p in ref.PINS if p['slug']=='colosseum-tickets')
 off.set_content(m.tpl_a(ref.SITE,pp,True),wait_until='networkidle');off.evaluate('document.fonts.ready')
 out['offline']={'fontfaces':off.evaluate('[...document.fonts].length'),'h1':off.locator('h1').bounding_box(),'footer':off.locator('.foot').bounding_box()}
 off.screenshot(path=str(root/'offline-colosseum.png'))
 # CSS reproduction showing custom hex-only alpha assumption, without changing the actual reference.
 s={**ref.SITE,'tokens':{**ref.SITE['tokens'],'dark_accent':'rgb(201,169,74)'}}
 pc=next(p for p in ref.PINS if p['template']=='C')
 page.set_content(m.tpl_c(s,pc,True),wait_until='networkidle')
 out['rgb_token']=page.locator('.col').first.evaluate('(e)=>({border:getComputedStyle(e).borderTopWidth,background:getComputedStyle(e).backgroundColor})')
 b.close()
(root/'checks.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
