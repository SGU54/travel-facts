#!/usr/bin/env python3
"""Optional corpus/output length statistics; never a quality or publication gate.

Usage: python3 audit-depth.py BUILD_DIR [--pdf FILE]
Counts are descriptive. Length ratios do not establish source coverage or value.
"""
import argparse
import json
from pathlib import Path
import re
import sys

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("build_dir", type=Path)
    parser.add_argument("--pdf", type=Path)
    args = parser.parse_args()
    try:
        root = args.build_dir
        candidates = [root / "corpus.json", root / "articles.json"]
        source = next((p for p in candidates if p.is_file()), None)
        if source is None:
            raise ValueError("corpus.json or articles.json is needed for length statistics")
        obj = json.loads(source.read_text(encoding="utf-8"))
        articles = obj if isinstance(obj, list) else obj.get("articles", obj.get("data", []))
        if not isinstance(articles, list) or not articles or not all(isinstance(a, dict) for a in articles):
            raise ValueError("corpus must contain a nonempty array of articles")
        words_in = sum(len(re.sub("<[^>]+>", " ", str(a.get("content") or a.get("body") or "")).split()) for a in articles)
        pdf_path = args.pdf or root / "dossier.pdf"
        from pypdf import PdfReader
        pdf = PdfReader(str(pdf_path))
        words_out = sum(len((p.extract_text() or "").split()) for p in pdf.pages)
        print(json.dumps({"diagnostic": "lengths", "articles": len(articles),
                          "corpus_words": words_in, "output_pages": len(pdf.pages),
                          "output_words": words_out,
                          "output_to_corpus_word_ratio": words_out / words_in if words_in else None,
                          "interpretation": "Descriptive lengths only. No minimum, coverage inference, or release verdict."}, indent=2))
        return 0
    except (OSError, ValueError, TypeError, AttributeError, ImportError) as exc:
        print("DIAGNOSTIC UNAVAILABLE: " + str(exc), file=sys.stderr)
        return 2

if __name__ == "__main__":
    sys.exit(main())
