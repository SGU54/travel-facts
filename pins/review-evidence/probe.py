from pathlib import Path
import sys,json
from PIL import Image,ImageDraw
from playwright.sync_api import sync_playwright
root=Path('/tmp/astra-pins-review')
sys.path[:0]=[str(root/'pins/scripts'),str(root/'pins/references')]
import make_pins as m
import pins_rome_example as ref
out=root/'rendered'
m.render(ref.SITE,ref.PINS,out,True,True)
metrics=[]
with sync_playwright() as pw:
 b=pw.chromium.launch()
 page=b.new_page(viewport={'width':1000,'height':1500},device_scale_factor=2)
 for p in ref.PINS:
  page.set_content(m.TEMPLATES[p['template']](ref.SITE,p,True),wait_until='networkidle')
  page.evaluate('document.fonts.ready')
  data=page.evaluate('''() => ({fonts:[...document.fonts].map(f=>({family:f.family,status:f.status,weight:f.weight})), nodes:[...document.querySelectorAll('.inner,.ph,h1,.sub,ol,li,.foot,.grid,.val,.lab,.s,.verdict')].map(e=>{let r=e.getBoundingClientRect(),c=getComputedStyle(e);return {tag:e.tagName,cls:e.className,text:e.innerText,x:r.x,y:r.y,w:r.width,h:r.height,bottom:r.bottom,font:c.fontSize,line:c.lineHeight,marginTop:c.marginTop,scroll:e.scrollHeight,client:e.clientHeight}})})''')
  data['slug']=p['slug'];data['template']=p['template']; metrics.append(data)
  print(p['slug'],[(n['cls'] or n['tag'],round(n['y'],1),round(n['bottom'],1),n['marginTop']) for n in data['nodes'] if n['tag']=='H1' or n['cls'] in ['foot mono','inner']],flush=True)
  im=Image.open(out/(p['slug']+'.png')).convert('RGB'); im.resize((236,354),Image.Resampling.LANCZOS).save(out/(p['slug']+'-actual236.png'))
 b.close()
(root/'metrics.json').write_text(json.dumps(metrics,indent=2))
canvas=Image.new('RGB',(4*256,3*395),'white');d=ImageDraw.Draw(canvas)
for i,p in enumerate(ref.PINS):
 x=(i%4)*256;y=(i//4)*395;canvas.paste(Image.open(out/(p['slug']+'-actual236.png')),(x+10,y));d.text((x+10,y+357),p['slug'],fill='black')
canvas.save(root/'contact.png')
print('loaded fonts',metrics[0]['fonts'])
