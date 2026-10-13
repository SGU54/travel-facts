#!/usr/bin/env python3
"""emit-manuscript.py — write the book's PROSE to manuscript.md.

The ai-smell gate reads a manuscript. This tree has none — build2.py consumes a
`../dossier-mar/manuscript.md` that was never archived — so the gate had nothing
to read and the release came back BLOCKED. dossier3.html is the source of record
here, so the manuscript is derived from it.

Prose only: chapter titles and body paragraphs. Ledgers, figure captions and
running furniture are excluded; their rhythm is not the prose rhythm the gate
is trying to read.
"""
import os, re, html as _html

HERE = os.path.dirname(os.path.abspath(__file__))
doc = open(os.path.join(HERE, "dossier3.html"), encoding="utf-8").read()

out = []
for m in re.finditer(r'<section class="([^"]*)" id="([^"]*)"[^>]*>(.*?)</section>', doc, re.S):
    cls, sid, body = m.groups()
    if "partdiv" in cls:
        continue                                   # part dividers carry no prose
    body = re.sub(r'<table.*?</table>', ' ', body, flags=re.S)
    body = re.sub(r'<figure.*?</figure>', ' ', body, flags=re.S)
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', body, re.S)
    if h1:
        out.append("## " + _html.unescape(re.sub(r'<[^>]+>', '', h1.group(1))).strip())
    for p in re.findall(r'<p[^>]*>(.*?)</p>', body, re.S):
        t = _html.unescape(re.sub(r'<[^>]+>', '', p))
        t = " ".join(t.split())
        if len(t.split()) >= 5:
            out.append(t)

text = "\n\n".join(out) + "\n"
path = os.path.join(HERE, "manuscript.md")
open(path, "w", encoding="utf-8").write(text)
print(f"wrote {path}  ({len(text.split()):,} words, {len(out)} blocks)")
