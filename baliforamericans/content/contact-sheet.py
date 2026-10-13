#!/usr/bin/env python3
"""python3 contact-sheet.py 01  -> /Volumes/.../batch-01/cand/sheet-<k>.jpg (one row per slot, 4 across)
   python3 contact-sheet.py 01 crops key__n [key__n ...] -> 1:1 native crops for watermark/face/logo checks"""
import sys,os,json
from PIL import Image,ImageDraw
N=sys.argv[1]; D=f'/Volumes/Untitled/travel-facts/baliforamericans/content/batch-{N}/cand'
man=json.load(open(f'{D}/manifest.json'))
if len(sys.argv)>2 and sys.argv[2]=='crops':
    picks=sys.argv[3:]; W,H=640,420; sheet=Image.new('RGB',(W*3,(H+24)*len(picks)),'white'); d=ImageDraw.Draw(sheet)
    for r,p in enumerate(picks):
        im=Image.open(f'{D}/{p}.jpg').convert('RGB'); w,h=im.size
        for c,(fx,fy) in enumerate([(0.12,0.15),(0.5,0.5),(0.82,0.78)]):
            x=max(0,min(w-W,int(w*fx-W/2))); y=max(0,min(h-H,int(h*fy-H/2)))
            sheet.paste(im.crop((x,y,x+W,y+H)),(c*W,r*(H+24)+24))
        d.text((6,r*(H+24)+6),f'{p}  native {w}x{h}',fill='black')
    out=f'{D}/crops.jpg'; sheet.save(out,quality=88); print(out)
else:
    keys=list(man); per=5; TW,TH=440,293
    for s in range(0,len(keys),per):
        ks=keys[s:s+per]; sheet=Image.new('RGB',(TW*4,(TH+22)*len(ks)),'white'); d=ImageDraw.Draw(sheet)
        for r,k in enumerate(ks):
            d.text((6,r*(TH+22)+5),k,fill='black')
            for c,e in enumerate(man[k]):
                im=Image.open(f'{D}/{k}__{e["n"]}.jpg').convert('RGB'); im.thumbnail((TW,TH))
                sheet.paste(im,(c*TW,r*(TH+22)+22)); d.text((c*TW+6,r*(TH+22)+26),str(e['n']),fill='yellow')
        out=f'{D}/sheet-{s//per+1}.jpg'; sheet.save(out,quality=82); print(out)
