#!/usr/bin/env python3
"""Three defects that ship because every other gate looks somewhere else.

Usage: python3 audit-source-defects.py BUILD_DIR [--json]
Exit 0 PASS · 1 FAIL · 2 BLOCKED.

WHY THIS EXISTS. An outside reader found three things in the shipped Barcelona
book in about ten minutes, and the book had passed every gate:

  1. Two summary cells ended mid-phrase: "say euros, use…" and "dinner on…".
     A generator had cut them to a character budget and the result was pasted
     back into the source, so the truncation was FROZEN. The full text was in
     calls.json the whole time.
  2. Three tables repeated their <thead> row as the first row of <tbody>.
  3. A word broke across a PAGE TURN ("comp|ared"), introduced by an edit that
     reflowed the chapter.

None of these is a factual error, so no amount of fact-checking finds them.
And content-integrity cannot either: it compares the final HTML with the final
PDF, and for 1 and 2 the defect is present and identical in BOTH. The only
place to catch them is the source, before it is rendered.

Checks 1 and 2 read the HTML. Check 3 needs the PDF and is skipped without it.
"""
from __future__ import annotations

import argparse
import html as htmllib
import json
import re
import sys
from pathlib import Path

ELLIPSIS = ("…", "&#8230;", "&hellip;", "...")
# Cells and list items are where a budget-truncated string lands. A paragraph
# ending in an ellipsis is usually deliberate prose, so it is not flagged.
CELL = re.compile(r"<(td|th|li)\b[^>]*>(.*?)</\1>", re.S | re.I)
THEAD_TBODY = re.compile(r"</thead>\s*<tbody[^>]*>\s*<tr[^>]*>\s*<th\b", re.I)


def strip_tags(fragment: str) -> str:
    """Tags collapse to a SPACE, never to nothing.

    Dropping them outright glues adjacent elements together — "…the room" and
    "Is the tourist tax…" become "roomIs", and the seam check then reports a
    clean page break as a split word. (The inverse mistake also exists: see the
    Greece notes, where TRIMMING before the test produced the same false
    positive from the other direction.)
    """
    return re.sub(r"\s+", " ", htmllib.unescape(re.sub(r"<[^>]+>", " ", fragment))).strip()


# A deliberate label ends in an ellipsis on purpose — Greece prints "IF YOU WANT…"
# and "IF YOU HAVE…" as column heads. A budget-truncated SENTENCE is long. Eight
# words separates them cleanly: the real truncations found across the fleet run
# 15-20 words, the deliberate labels three.
MIN_WORDS = 8


def truncated_cells(doc: str):
    out = []
    for m in CELL.finditer(doc):
        text = strip_tags(m.group(2))
        if not text or len(text.split()) < MIN_WORDS:
            continue
        if any(text.endswith(e) for e in ELLIPSIS):
            out.append(text[-74:])
    return out


def cut_mid_sentence(doc: str):
    """A cell cut mid-sentence that left NO ellipsis behind.

    Morocco shipped "For a week, don't pick a base, pick an" — the generator
    stopped at an <em> tag instead of a character budget, so there was no "…"
    for the check above to see, and the row read as a finished thought that
    simply made no sense. Thirty-eight characters, not a budget: a different
    cause, the same defect.

    The test is not "does it end in a period" — that would flag every book
    whose summary column drops the terminal period as house style (Morocco's
    does, in five untouched rows). It is: find this cell's text elsewhere in
    the document, and look at what FOLLOWS it there. A continuation that opens
    with a lower-case letter is the same sentence carrying on, so the cell holds
    a fragment of it. A continuation that opens with "." or "?" is a sentence
    that ended where the cell ended, which is correct.
    """
    out = []
    for m in CELL.finditer(doc):
        text = strip_tags(m.group(2))
        if not text or len(text.split()) < MIN_WORDS:
            continue
        if any(text.endswith(e) for e in ELLIPSIS):
            continue                               # already reported above
        rest = doc[m.end():] + doc[:m.start()]     # everywhere BUT this cell
        at = strip_tags(rest).find(text)
        if at < 0:
            continue                               # appears only here: nothing to compare
        tail = strip_tags(rest)[at + len(text):at + len(text) + 40].lstrip()
        if tail[:1].islower():
            out.append(f"{text[-60:]} ‖ continues: {tail[:40]}")
    return out


def repeated_headers(doc: str):
    return len(THEAD_TBODY.findall(doc))


def split_words(source_html: str, pdf: Path):
    """A page that begins mid-word carries half a word over the fold.

    Chromium has no hyphenate-limit-last:page, so this cannot be expressed in
    CSS and has to be measured. Taking the first run of body text on each page
    and finding it in the tag-stripped source tells us what precedes it: a
    letter there means the page opened inside a word.
    """
    try:
        import pypdf
    except ImportError:
        return None, "pypdf is unavailable"
    flat = re.sub(r"\s+", " ", strip_tags(re.sub(r"<(script|style).*?</\1>", "", source_html, flags=re.S)))
    try:
        reader = pypdf.PdfReader(str(pdf))
    except Exception as exc:                                   # noqa: BLE001
        return None, f"cannot read {pdf.name}: {exc}"
    found = []
    for n in range(1, len(reader.pages)):
        page = re.sub(r"\s+", " ", reader.pages[n].extract_text() or "")
        body = re.sub(r"^.*?·\s*\d+\s*", "", page).strip()     # drop running head + folio
        probe = body[:26]
        if len(probe) < 12:
            continue
        at = flat.find(probe)
        if at <= 0:
            continue
        if flat[at - 1].isalpha():
            found.append(f"p{n + 1} opens mid-word: …{flat[max(0, at - 24):at]}|{probe}…")
    return found, None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("build_dir", nargs="?", default=".")
    ap.add_argument("--html", default="dossier3.html")
    ap.add_argument("--pdf", default="dossier.pdf")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    root = Path(args.build_dir).resolve()
    source = root / args.html
    if not source.exists():
        report = {"gate": "source-defects", "status": "BLOCKED",
                  "errors": [f"{args.html} not found in {root}"]}
        print(json.dumps(report, indent=2) if args.json else f"BLOCKED  {report['errors'][0]}")
        return 2

    doc = source.read_text(encoding="utf-8", errors="ignore")
    cut = truncated_cells(doc)
    frag = cut_mid_sentence(doc)
    dup = repeated_headers(doc)

    pdf = root / args.pdf
    seams, seam_note = (None, f"{args.pdf} not found") if not pdf.exists() else split_words(doc, pdf)

    errors = []
    errors += [f"cell truncated mid-phrase: …{c}" for c in cut]
    errors += [f"cell cut mid-sentence, no ellipsis: {c}" for c in frag]
    if dup:
        errors.append(f"{dup} table(s) repeat the <thead> row inside <tbody>")
    errors += seams or []

    warnings = [seam_note] if seam_note else []
    status = "FAIL" if errors else ("PASS" if seams is not None else "PASS")
    report = {"gate": "source-defects", "status": status, "errors": errors, "warnings": warnings,
              "limits": "Looks for production damage in the source. Says nothing about whether a claim is true."}

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        for e in errors:
            print("  " + e)
        for w in warnings:
            print("  REVIEW: " + w)
        print(f"source-defects: {status}"
              + ("" if errors else " — no truncated cell, no repeated header, no word split across a page turn"))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
