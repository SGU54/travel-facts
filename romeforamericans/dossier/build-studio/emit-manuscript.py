#!/usr/bin/env python3
"""emit-manuscript.py — the book's PROSE to manuscript.md, for the ai-smell gate.

Without one the release audit falls back to globbing *.md and measures whatever
documentation happens to sit in the build directory.
"""
import os, re, html as _html
HERE = os.path.dirname(os.path.abspath(__file__))
doc = open(os.path.join(HERE, "dossier3.html"), encoding="utf-8").read()
out = []
for m in re.finditer(r'<(?:section|div)\s+class="((?:dec chap|dec)[^"]*)"[^>]*>(.*?)'
                     r'(?=<(?:section|div)\s+class="(?:dec chap|dec)\b|$)', doc, re.S):
    body = m.group(2)
    body = re.sub(r'<table.*?</table>', ' ', body, flags=re.S)
    body = re.sub(r'<figure.*?</figure>', ' ', body, flags=re.S)
    body = re.sub(r'<svg.*?</svg>', ' ', body, flags=re.S)
    h = re.search(r'<h[123][^>]*>(.*?)</h[123]>', body, re.S)
    if h:
        out.append("## " + _html.unescape(re.sub(r'<[^>]+>', '', h.group(1))).strip())
    for p in re.findall(r'<p[^>]*>(.*?)</p>', body, re.S):
        t = " ".join(_html.unescape(re.sub(r'<[^>]+>', '', p)).split())
        if len(t.split()) >= 5:
            out.append(t)
text = "\n\n".join(out) + "\n"
open(os.path.join(HERE, "manuscript.md"), "w", encoding="utf-8").write(text)
print(f"wrote manuscript.md ({len(text.split()):,} words, {len(out)} blocks)")
