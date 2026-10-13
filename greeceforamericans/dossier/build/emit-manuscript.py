#!/usr/bin/env python3
"""emit-manuscript.py — write the book's PROSE to manuscript.md.

The ai-smell gate reads a manuscript, and this tree shipped without one, so the
release audit fell back to globbing *.md and measured the build README's 192
words instead of the book's ten thousand. Run this after build.py.

Prose only: headings and body paragraphs. Ledger cells, figure captions and
running furniture are excluded — they are tabular or mechanical, and their
rhythm is not the prose rhythm the gate is trying to read.
"""
import os, re, html as _html

HERE = os.path.dirname(os.path.abspath(__file__))
doc = open(os.path.join(HERE, "dossier3.html"), encoding="utf-8").read()

out = []
for m in re.finditer(
        r'<section class=[\'"]([^\'"]*\bdec\b[^\'"]*)[\'"] id=[\'"]([^\'"]+)[\'"][^>]*>(.*?)</section>',
        doc, re.S):
    cls, sid, body = m.groups()
    if "fs" in cls.split() or sid in ("contents", "fs"):
        continue                       # field sheet + table of contents are not prose
    body = re.sub(r'<table.*?</table>', ' ', body, flags=re.S)     # ledgers
    body = re.sub(r'<figure.*?</figure>', ' ', body, flags=re.S)   # figures + captions
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
