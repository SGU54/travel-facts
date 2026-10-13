#!/usr/bin/env python3
"""Stage G — the DEPTH gate. Did the book mine the corpus, or skim it?

audit-book.py proves the book is CLEAN (well-filled, evenly paced, good cover). It cannot
see whether the book is COMPLETE. A cold rebuild of Greece passed audit-book.py green at 19
pages — half the length its 80-article corpus supports — because every page it *did* build
was clean. The audit that measures organization waved through a book that skimmed 9% of its
own corpus.

This gate closes that hole. It reads the corpus and the rendered PDF and checks three
independent signals of under-mining, calibrated on three real builds:

                    pp/article   words/article   % of corpus used
  our Greece  34pp     0.42          145            14.1%   ← good
  Rome        50pp     0.52          134            12.7%   ← good
  cold Greece 19pp     0.24           90             8.8%   ← THIN (this gate catches it)

Usage:  python3 audit-depth.py <build-dir>
        expects <build-dir>/corpus.json (or *.json with an article list) and dossier.pdf
"""
import sys, os, glob, json, re

PP_PER_ARTICLE   = 0.40   # pages out per article in
WORDS_PER_ART    = 120    # words out per article in
CORPUS_UTIL      = 11.0   # % of corpus words that survive into the book

def load_corpus(d):
    for name in ("corpus.json", "articles.json"):
        p = os.path.join(d, name)
        if os.path.exists(p):
            return json.load(open(p))
    for p in glob.glob(os.path.join(d, "*.json")):
        try:
            j = json.load(open(p))
            if isinstance(j, list) and j and isinstance(j[0], dict) and \
               any(k in j[0] for k in ("content", "body", "excerpt")):
                return j
        except Exception:
            pass
    return None

def words(a):
    txt = a.get("content") or a.get("body") or ""
    return len(re.sub("<[^>]+>", " ", txt).split())

def main():
    d = sys.argv[1] if len(sys.argv) > 1 else "."
    corpus = load_corpus(d)
    if corpus is None:
        sys.exit(f"depth gate needs the corpus; no article JSON found in {d}")
    arts = corpus if isinstance(corpus, list) else corpus.get("articles", corpus.get("data", []))
    n_art = len(arts)
    w_in = sum(words(a) for a in arts)

    pdf = os.path.join(d, "dossier.pdf")
    if not os.path.exists(pdf):
        alt = glob.glob(os.path.join(d, "*.pdf")); pdf = alt[0] if alt else sys.exit("no PDF")
    from pypdf import PdfReader
    r = PdfReader(pdf)
    n_pp = len(r.pages)
    w_out = sum(len(p.extract_text().split()) for p in r.pages)

    pp_ratio = n_pp / n_art
    w_ratio  = w_out / n_art
    util     = 100 * w_out / w_in if w_in else 0

    print(f"\n  DEPTH AUDIT — {n_pp}pp from {n_art} articles ({w_in:,}w in \u2192 {w_out:,}w out)")
    print("  " + "-"*52)
    rows = [
        ("pages / article", pp_ratio, PP_PER_ARTICLE, f"{pp_ratio:.2f}  (>= {PP_PER_ARTICLE})"),
        ("words / article", w_ratio,  WORDS_PER_ART,  f"{w_ratio:.0f}   (>= {WORDS_PER_ART})"),
        ("corpus used",     util,     CORPUS_UTIL,    f"{util:.1f}% (>= {CORPUS_UTIL}%)"),
    ]
    allok = True
    for name, val, floor, detail in rows:
        ok = val >= floor
        if not ok: allok = False
        print(f"  {'\u2713' if ok else '\u2717'} {name:16} {detail}")
    print("  " + "-"*52)
    if allok:
        exp = n_art * 0.5
        print(f"  MINED — the book uses its corpus. (model expects ~{exp:.0f}pp; got {n_pp}.)\n")
        return 0
    exp = n_art * 0.5
    print(f"  THIN — the corpus supports ~{exp:.0f}pp; this book is {n_pp}. The decisions are")
    print("  complete but shallow, or veins were left unwritten. Before shipping:")
    print("   \u00b7 do the SECOND mining pass (a-mine.md) \u2014 name every strong vein, write each")
    print("   \u00b7 deepen thin decisions \u2014 a decision is 250-350w of body, not 90")
    print("   \u00b7 add the figures the corpus supports \u2014 each is a page that argues")
    print("  NOT by padding: bigger type or air will fail audit-book.py's page-shape check.\n")
    return 1

if __name__ == "__main__":
    sys.exit(main())
