#!/usr/bin/env python3
"""Stage E — emit the image brief the user hand-fills from Pexels/Unsplash.

Mirrors the article-batch `batch-NN-images.md` flow: alphanumeric IDs in download order,
one argument + one shot spec + 2-3 constructed gallery links per slot.

Usage:  python3 emit-image-brief.py <slots.json> > dossier-images.md
"""
import json, sys, urllib.parse

def links(query):
    q = urllib.parse.quote(query)
    return [f"https://unsplash.com/s/photos/{q}",
            f"https://www.pexels.com/search/{q}/"]

def emit(project, edition, slots):
    out=[f"# {project} — dossier image brief · Edition {edition}", ""]
    out+=[f"**{len(slots)} images.** **Name each file for its slot** — `A01.jpg`, `A02.jpg`, "
          "… — and hand them back. Order alone breaks the moment one upload fails.", ""]
    out+=["Every pick must be: ≥1600px · landscape · free-commercial licence (Pexels/Unsplash) ·",
          "**no recognizable faces** · **no brand or logo signage** · no selfie-stick tourists",
          "*unless the crowd is the argument*.", "",
          "These are pages to **pick from**, not direct downloads.", "", "---", ""]
    for i,s in enumerate(slots,1):
        sid=f"A{i:02d}"
        out+=[f"### {sid} · {s['chapter']} · `{s['id']}`",
              f"**Hand back as:** `{sid}.jpg`",
              f"**Argument it must prove:** {s['argument']}",
              f"**Shot:** {s['shot']}",
              f"**Orientation:** {s.get('orientation','landscape')}",
              "**Search:**"]
        out+= [f"- {u}" for u in links(s['query'])]
        for extra in s.get('verified',[]): out.append(f"- {extra}")
        out.append("")
    return "\n".join(out)

if __name__=="__main__":
    cfg=json.load(open(sys.argv[1]))
    print(emit(cfg["project"], cfg["edition"], cfg["slots"]))
