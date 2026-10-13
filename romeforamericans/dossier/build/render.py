#!/usr/bin/env python3
# render.py — dossier3.html → PDF + the full Stage F gate suite.
import os, glob, json
from playwright.sync_api import sync_playwright
BUILD=os.path.dirname(os.path.abspath(__file__))
# Portable browser lookup. This indexed [-1] straight into a glob of a Linux
# container path, so on any other machine it raised IndexError at import and
# the tree could not be rebuilt at all.
_EXES=(sorted(glob.glob("/opt/pw-browsers/chromium_headless_shell-*/chrome-linux/headless_shell"))
       + sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome"))
       + sorted(glob.glob(os.path.expanduser(
           "~/Library/Caches/ms-playwright/chromium-*/chrome-mac/Chromium.app"
           "/Contents/MacOS/Chromium"))))
SHELL=_EXES[0] if _EXES else None
src=f"file://{BUILD}/dossier3.html"; out=f"{BUILD}/dossier3.pdf"

GATE = """()=>{
  const pg=[...document.querySelectorAll('.page')];
  const bottomOf=(el)=>{const pb=el.getBoundingClientRect();let last=0;
    el.querySelectorAll(':scope > *').forEach(c=>{
      if(String(c.className||'').includes('folio'))return;
      last=Math.max(last,c.getBoundingClientRect().bottom-pb.top);});return last;};
  return {
    pages: pg.length,
    overflow: pg.map((el,i)=>el.scrollHeight>el.clientHeight+2?{p:i+1,by:el.scrollHeight-el.clientHeight}:0).filter(Boolean),
    placeholders: document.querySelectorAll('.ph').length,
    imgsBroken: [...document.querySelectorAll('img')].filter(i=>!i.complete||!i.naturalWidth).length,
    imgs: document.querySelectorAll('img').length,
    sparse: pg.map((el,i)=>Math.round(100*bottomOf(el)/el.clientHeight)<55?i+1:0).filter(Boolean),
    capSize: getComputedStyle(document.querySelector('.map figcaption')).fontSize,
    bodySize: getComputedStyle(document.querySelector('p.b')).fontSize,
    figures: document.querySelectorAll('.map svg, .photo img').length,
  };}"""

with sync_playwright() as p:
    _launch={"args":["--no-sandbox"]}
    if SHELL: _launch["executable_path"]=SHELL
    b=p.chromium.launch(**_launch)
    pg=b.new_page(viewport={"width":816,"height":1056}, device_scale_factor=2)
    pg.goto(src, wait_until="networkidle")
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(2800)          # base64 imgs + webfonts settle late (Stage F)
    gate=pg.evaluate(GATE)
    pg.emulate_media(media="print")
    pg.pdf(path=out, width="8.5in", height="11in", print_background=True,
           prefer_css_page_size=True, margin={"top":"0","bottom":"0","left":"0","right":"0"})
    b.close()

print(json.dumps(gate, indent=1))
ok = (not gate["overflow"] and gate["placeholders"]==0 and gate["imgsBroken"]==0
      and not gate["sparse"]
      and float(gate["capSize"][:-2]) < float(gate["bodySize"][:-2]))
print("\nSTAGE F:", "ALL GATES PASS" if ok else "*** GATE FAILURES ABOVE ***")
print("wrote", out, f"({os.path.getsize(out)//1024} KB)")
