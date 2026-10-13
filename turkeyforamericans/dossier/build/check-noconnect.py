#!/usr/bin/env python3
"""
check-noconnect.py — refuse any article that makes the book's call.

WHY THIS EXISTS: on Thailand I wrote "the sensible answer is fewer, larger
withdrawals" into a retrofit article, under a skeleton whose first rule was
don't make the call. That one sentence killed D-money for the paid guide. The
plan stopped depending on my discipline and started depending on this.

USAGE
    python3 check-noconnect.py articles/*.html
    python3 check-noconnect.py --json import-batch-16.json

Exit 0 = clean. Exit 1 = at least one hit. NO ARTICLE ENTERS AN IMPORT BATCH
WITHOUT AN EXIT 0.

CALIBRATION (Thailand, live articles): when-ferries-cancel PASSED clean,
atm-fees failed at 7, scooter-rental at 1. It discriminates; it does not flag
everything.
"""
import json
import re
import sys

# Constructions that RESOLVE rather than report. Ordinary connective tissue
# ("a beautiful but stomach-churning journey") must NOT trip these — a threshold
# written against prose instead of against decision structure is a bad gate, and
# that mistake cost a revision pass on Thailand batch 18.
PATTERNS = [
    (r"\bthe (?:sensible|right|smart|obvious|real) (?:answer|call|move|choice)\b", "declares the answer"),
    (r"\bthe answer is\b",                                   "declares the answer"),
    (r"\bthe (?:trick|rule|key) is\b",                        "declares a rule"),
    # Imperative only at a clause boundary. "dates that never move" is DESCRIPTIVE;
    # "Never move your booking" is a call. Requiring sentence start or a preceding
    # [.;:!?] separates them — caught on Turkey batch 17, where two articles were
    # flagged for saying fixed holidays "never move".
    (r"(?:^|[.;:!?]\s+)(?:Always|Never)\s+[a-z]",              "imperative rule"),
    (r"^\s*(?:Always|Never|Make sure|Be sure to|Don't|Do not)\b", "opens with an imperative"),
    (r"\byou should\b|\bwe recommend\b|\bour advice\b",       "recommends"),
    (r"\bmatch (?:your|the) \w+ to (?:your|the) \w+",         "prescribes a mapping"),
    (r"\bif you only (?:do|book|read) one\b",                 "ranks for the reader"),
    (r"\b(?:worth|not worth) (?:it|paying|the money)\b",      "renders a verdict"),
    (r"\bdon't bother\b|\bskip the\b|\bgo with the\b",        "renders a verdict"),
    (r"\bbest to\b|\byour best bet\b",                        "renders a verdict"),
    # The margin/sequencing family is reserved for the book on EVERY project.
    (r"\bleave (?:at least )?\d+\s*(?:nights?|days?|hours?)\b", "MARGIN RULE — book-only"),
    (r"\bbuild in (?:a )?(?:buffer|slack|margin)\b",            "MARGIN RULE — book-only"),
    (r"\bgive yourself (?:at least )?\d+",                      "MARGIN RULE — book-only"),
    (r"\b(?:book|schedule) (?:it |the |your )?(?:for your )?first (?:morning|day)\b", "MARGIN RULE — book-only"),
]
COMPILED = [(re.compile(p, re.I | re.M), why) for p, why in PATTERNS]

# Quoting a rule someone else states is reporting, not prescribing.
QUOTED = re.compile(r'["""\u201c\u201d].{0,200}?["""\u201c\u201d]', re.S)


def strip_html(s: str) -> str:
    s = re.sub(r"<(script|style)\b.*?</\1>", " ", s, flags=re.S | re.I)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s))


def sentences(text: str):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]


def check(name: str, html: str):
    text = strip_html(html)
    masked = QUOTED.sub(" ", text)          # exempt quoted material
    hits = []
    for sent in sentences(masked):
        # A QUESTION is not a call. FAQ headings ("Are guided tours worth it?")
        # phrase the reader's doubt; the answer beneath them is what matters.
        if sent.rstrip().endswith("?"):
            continue
        for rx, why in COMPILED:
            if rx.search(sent):
                hits.append((why, sent[:130]))
                break
    return hits


def main(argv):
    paths = [a for a in argv if not a.startswith("-")]
    as_json = "--json" in argv
    if not paths:
        print(__doc__)
        return 2

    total, failed = 0, 0
    for path in paths:
        if as_json or path.endswith(".json"):
            for art in json.load(open(path, encoding="utf-8")):
                hits = check(art["slug"], art.get("content", ""))
                total += 1
                if hits:
                    failed += 1
                    print(f"\nFAIL  {art['slug']}  ({len(hits)} hit(s))")
                    for why, s in hits:
                        print(f"    [{why}] {s}")
                else:
                    print(f"ok    {art['slug']}")
        else:
            hits = check(path, open(path, encoding="utf-8").read())
            total += 1
            if hits:
                failed += 1
                print(f"\nFAIL  {path}  ({len(hits)} hit(s))")
                for why, s in hits:
                    print(f"    [{why}] {s}")
            else:
                print(f"ok    {path}")

    print(f"\n{total - failed}/{total} clean")
    if failed:
        print("An article that makes the call has nothing left for the book to sell.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
