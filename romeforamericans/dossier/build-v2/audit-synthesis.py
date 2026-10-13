#!/usr/bin/env python3
"""Stage A viability + Stage G quality — is there SYNTHESIS to sell?

The model: a dossier is worth buying because it makes the connections the free corpus
doesn't. The facts are scattered across many free articles; the paid book is the one place
they're joined. If the corpus's key facts are ALREADY connected inside single articles,
there is little synthesis to sell and the destination is a weak dossier candidate — better
to know that at Stage A than after building.

This measures it objectively, with no semantic judgment:
  - take the destination's core THEMES (the organising fact's components, passed in or
    auto-detected from the most frequent salient terms)
  - for each theme, count how many articles mention it (it's scattered = good raw material)
  - count how many single articles mention ALL of them (the synthesis is already free = bad)
  - scatter is high AND full-co-occurrence is low  →  strong dossier: the book's job exists

Usage:
  python3 audit-synthesis.py <corpus.json> "theme1 regex" "theme2 regex" ...

Reports a SYNTHESIS HEADROOM score = scatter breadth ÷ pre-connection. High = build it.
"""
import sys, os, json, re

def load(path):
    j = json.load(open(path))
    return j if isinstance(j, list) else j.get("articles", j.get("data", []))

def body(a):
    return (a.get("content") or a.get("body") or "") + " " + (a.get("title") or "")

def main():
    if len(sys.argv) < 4:
        sys.exit("usage: audit-synthesis.py <corpus.json> \"theme1 regex\" \"theme2 regex\" ...\n"
                 "  themes are the ORGANISING FACT's components (a Stage A2 judgment) — the\n"
                 "  2-5 things that must connect to make the book's central call. Do NOT guess;\n"
                 "  auto-detection picks filler and lies. Name the real parts of the thesis.")
    arts = load(sys.argv[1])
    n = len(arts)
    themes = sys.argv[2:]
    labels = [t if len(t) < 22 else t[:19]+"…" for t in themes]

    per = {}
    for t, lab in zip(themes, labels):
        per[lab] = sum(1 for a in arts if re.search(t, body(a), re.I))
    full = sum(1 for a in arts if all(re.search(t, body(a), re.I) for t in themes))

    print(f"\n  SYNTHESIS CHECK — {n} articles, {len(themes)} core themes\n" + "  " + "-"*50)
    for lab in labels:
        pct = 100*per[lab]//n
        print(f"  {lab:24} in {per[lab]:3} articles ({pct:2}%)")
    print("  " + "-"*50)
    scatter = sum(per.values())/(len(themes)*n)          # 0..1, breadth of raw material
    preconn = full/n                                      # 0..1, how often it's already joined
    headroom = (scatter) / (preconn + 0.02)               # high = lots to synthesize, rarely pre-joined
    print(f"  articles joining ALL {len(themes)} themes (synthesis already free): {full} ({100*full//n}%)")
    print(f"  scatter {scatter:.2f} · pre-connection {preconn:.2f} · HEADROOM {headroom:.1f}")
    print()
    if full > n*0.15:
        print("  WEAK — the corpus already connects these themes in many articles. The")
        print("  synthesis a buyer would pay for is largely free. Either find a DEEPER")
        print("  organising fact whose parts aren't pre-joined, or this is a thin dossier.")
        return 1
    if scatter < 0.15:
        print("  THIN RAW MATERIAL — these themes barely appear. Wrong themes, or the")
        print("  corpus doesn't cover this destination deeply enough to synthesize.")
        return 1
    print("  STRONG — the facts are scattered and rarely pre-connected. The book's whole")
    print("  value is making the connection the free articles don't. Build it, and give")
    print("  ONE connection away as the free hook (see references/model.md).")
    return 0

if __name__ == "__main__":
    sys.exit(main())
