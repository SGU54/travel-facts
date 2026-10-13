import glob, os, re, sys
from playwright.sync_api import sync_playwright
src = open("render-paged.py", encoding="utf-8").read()
ns = {}; exec(re.search(r'INJECT = \((.*?)\n\)\n', src, re.S).group(0), ns)
html = open("dossier3.html", encoding="utf-8").read()
open("_probe.html", "w", encoding="utf-8").write(html.replace("</head>", ns["INJECT"] + "</head>"))
home = os.path.expanduser("~")
exes = sorted(glob.glob(f"{home}/Library/Caches/ms-playwright/chromium-*/chrome-mac*/*.app/Contents/MacOS/*"))
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=exes[0] if exes else None)
    pg = b.new_page(viewport={"width": 816, "height": 1056})
    pg.goto("file://" + os.path.abspath("_probe.html"), wait_until="load")
    pg.wait_for_function("window.__pagedDone!==undefined||window.__pagedErr!==undefined", timeout=600000)
    print(pg.evaluate("""() => {
      const out = {};
      document.querySelectorAll('.pagedjs_page figure.drawn img').forEach(s => {
        const k = (s.getAttribute('alt')||'').slice(0,26);
        out[k] = [(out[k]?out[k][0]:0) + 1,
                  s.complete && s.naturalWidth > 0 ? 'loaded' : 'BROKEN'];
      });
      return out;
    }"""))
    b.close()
os.remove("_probe.html")
