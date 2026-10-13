#!/usr/bin/env python3
"""Optional keyword co-occurrence inventory, not a willingness-to-pay test.

Usage: python3 audit-synthesis.py corpus.json "theme regex" "theme regex" ...
Mentions do not prove that an article connects ideas or that a book is original.
"""
import argparse
import json
from pathlib import Path
import re
import sys

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("corpus", type=Path)
    parser.add_argument("themes", nargs="+")
    args = parser.parse_args()
    try:
        obj = json.loads(args.corpus.read_text(encoding="utf-8"))
        articles = obj if isinstance(obj, list) else obj.get("articles", obj.get("data", []))
        if not isinstance(articles, list) or not articles or not all(isinstance(a, dict) for a in articles):
            raise ValueError("corpus must contain a nonempty array of articles")
        patterns = [re.compile(t, re.I) for t in args.themes]
        texts = [str(a.get("title") or "") + " " + str(a.get("content") or a.get("body") or "") for a in articles]
        rows = [{"theme": theme, "articles_mentioning": sum(bool(pattern.search(t)) for t in texts)}
                for theme, pattern in zip(args.themes, patterns)]
        full = sum(all(pattern.search(text) for pattern in patterns) for text in texts)
        print(json.dumps({"diagnostic": "keyword_cooccurrence", "articles": len(articles),
                          "themes": rows, "articles_mentioning_all": full,
                          "interpretation": "Search aid only. Read the passages; no semantic synthesis, originality, sales, or release verdict."}, indent=2))
        return 0
    except (OSError, ValueError, TypeError, AttributeError, re.error) as exc:
        print("DIAGNOSTIC UNAVAILABLE: " + str(exc), file=sys.stderr)
        return 2

if __name__ == "__main__":
    sys.exit(main())
