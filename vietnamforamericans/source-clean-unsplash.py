#!/usr/bin/env python3
"""Source clean replacements for the 11 watermarked images.

THE ROOT CAUSE, and the fix: Unsplash's search API marks every paid preview
with `plus: true` / `premium: true`, and serves it from plus.unsplash.com
instead of images.unsplash.com. Whoever picked the originals took whatever
looked right; nothing filtered on those flags. This script refuses any result
that carries either flag or the plus host, so a watermarked file cannot enter
the candidate set at all.

Regular Unsplash photos are free for commercial use under the Unsplash License.
"""
import json
import os
import subprocess
import urllib.parse

SP = os.path.dirname(os.path.abspath(__file__))
OUT = f"{SP}/src"

# key -> (query, what the picture has to show)
SLOTS = {
    "best-cooking-classes-vietnam-hero":   "vietnamese cooking class kitchen",
    "best-street-food-tours-hanoi-saigon-hero": "hanoi street food stall evening",
    "hoi-an-travel-guide-hero":            "hoi an ancient town lanterns",
    "sim-card-vs-esim-vietnam-hero":       "sim card smartphone hand",
    "vegetarian-vegan-food-vietnam-hero":  "vietnamese vegetarian noodle bowl herbs",
    "best-cooking-classes-vietnam-1":      "vietnam market fresh herbs vegetables",
    "hoi-an-tailors-how-to-order-1":       "tailor shop fabric rolls",
    "vegetarian-vegan-food-vietnam-1":     "tofu dish fresh vegetables asian",
    "vietnam-itinerary-first-timers-1":    "ha long bay boat limestone",
    "vietnam-itinerary-for-families-1":    "vietnam rice field village countryside",
    "where-to-stay-hoian-danang-1":        "hoi an boutique hotel pool garden",
}

os.makedirs(OUT, exist_ok=True)
manifest = {}
for key, query in SLOTS.items():
    url = ("https://unsplash.com/napi/search/photos?query="
           + urllib.parse.quote(query) + "&per_page=24&orientation=landscape")
    raw = subprocess.run(["curl", "-s", "-H", "Accept-Version: v1", url],
                         capture_output=True, text=True).stdout
    try:
        results = json.loads(raw).get("results", [])
    except Exception:
        print(f"{key}: SEARCH FAILED"); continue

    clean = [
        r for r in results
        if not r.get("plus") and not r.get("premium")
        and r["urls"]["raw"].split("/")[2] == "images.unsplash.com"
    ]
    rejected = len(results) - len(clean)
    picks = clean[:4]
    manifest[key] = []
    for i, r in enumerate(picks, 1):
        dest = f"{OUT}/{key}__{i}.jpg"
        subprocess.run(["curl", "-s", "-o", dest,
                        r["urls"]["raw"] + "&w=1800&fm=jpg&q=88"], check=False)
        manifest[key].append({
            "n": i, "id": r["id"],
            "desc": (r.get("description") or r.get("alt_description") or "")[:70],
            "by": r["user"]["name"],
        })
    print(f"{key}: {len(clean)} clean of {len(results)} ({rejected} Unsplash+ rejected), took {len(picks)}")

json.dump(manifest, open(f"{OUT}/manifest.json", "w"), indent=1, ensure_ascii=False)
print("\nsaved", len(os.listdir(OUT)) - 1, "candidate files")
