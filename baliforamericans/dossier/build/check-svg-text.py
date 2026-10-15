#!/usr/bin/env python3
"""check-svg-text.py — every <text> in every figure must sit inside its viewBox
with 6 units of clearance and must not overlap another <text> (d-draw.md:
'a character-count estimate can only PROPOSE a position — it cannot certify
containment'). Measures real getBBox() after the fonts load. Exit 1 on any hit.

Run:  python3 check-svg-text.py <build-dir>   (needs maps.FIGURES, covers.cover_svg, design2.CSS)"""
import glob, os, sys, json
from playwright.sync_api import sync_playwright
BUILD = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.getcwd()
sys.path.insert(0, BUILD); os.chdir(BUILD)
import maps, covers
from design2 import CSS
parts=[f'<figure id="fig-{k}">{fn()}</figure>' for k,(fn,c) in maps.FIGURES.items()]
html=f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS} body{{padding:20px}} figure{{width:652px;margin:0 0 20px}}</style></head><body><div id="cover" style="width:816px;height:1056px;position:relative">{covers.cover_svg()}</div>{"".join(parts)}</body></html>'
open('_svgcheck.html','w').write(html)
JS = r"""
() => {
  const out=[];
  document.querySelectorAll('svg').forEach((svg,si)=>{
    const vb=svg.viewBox.baseVal; const fig=svg.closest('figure'); const name=fig?fig.id:'cover';
    const texts=[...svg.querySelectorAll('text')];
    const boxes=texts.map(t=>{const b=t.getBBox(); return {t:t.textContent.trim(), x:b.x,y:b.y,w:b.width,h:b.height};});
    boxes.forEach((b,i)=>{
      if(b.t.length&&(b.x<vb.x-0.5||b.y<vb.y+1||b.x+b.w>vb.x+vb.width-1||b.y+b.h>vb.y+vb.height-1)) out.push({fig:name,kind:'overflow',text:b.t,x:Math.round(b.x),right:Math.round(b.x+b.w),bottom:Math.round(b.y+b.h),vw:vb.width,vh:vb.height});
      for(let j=i+1;j<boxes.length;j++){const c=boxes[j];
        const ox=Math.min(b.x+b.w,c.x+c.w)-Math.max(b.x,c.x), oy=Math.min(b.y+b.h,c.y+c.h)-Math.max(b.y,c.y);
        if(b.t.length&&c.t.length&&ox>1.5&&oy>1.5&&!(name==='cover'&&(b.h>40||c.h>40))) out.push({fig:name,kind:'overlap',text:b.t,other:c.t,ox:Math.round(ox),oy:Math.round(oy)});}
    });
  });
  return out;
}"""
exes=sorted(glob.glob(os.path.expanduser("~/Library/Caches/ms-playwright/chromium-*/chrome-mac/Chromium.app/Contents/MacOS/Chromium")))
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=exes[0] if exes else None, args=["--no-sandbox"])
    pg=b.new_page(viewport={"width":900,"height":1200})
    pg.goto("file://"+os.path.abspath('_svgcheck.html')); pg.wait_for_timeout(800)
    pg.evaluate("document.fonts.ready"); hits=pg.evaluate(JS); b.close()
n=0
for h in hits:
    n+=1
    if h['kind']=='overflow': print(f"OVERFLOW {h['fig']}: '{h['text'][:50]}' right={h['right']}/{h['vw']} bottom={h['bottom']}/{h['vh']} x={h['x']}")
    else: print(f"OVERLAP  {h['fig']}: '{h['text'][:40]}' × '{h['other'][:40]}' ({h['ox']}×{h['oy']})")
print(f"checked {sum(len(list(fn().split('<text'))) - 1 for fn,c in maps.FIGURES.values())} figure labels + cover: {n} hit(s)")
sys.exit(1 if n else 0)
