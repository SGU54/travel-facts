#!/usr/bin/env python3
"""Stage G — the mark-density gate. Is the prose seasoned, or is it confetti?

Provenance marks (● ◇ ▲ ◆) certify a claim is sourced. They are a seasoning, one per
load-bearing fact. A build that marks every sentence turns the page to noise: the first
cold build to skip the writing code hit 11.6 marks/page, up to 28 on one page, and the
prose became unreadable. This counts marks per page from the rendered PDF — pure string
count, no semantic judgment — and fails a book that over-marks.

Usage:  python3 audit-marks.py <dossier.pdf>
"""
import sys, os, glob, re
from pypdf import PdfReader

AVG_MAX      = 8.0        # confetti build is 11.5; a legend page + tables put a good
                         # build ~5-6. Above 8 avg = marking prose, not facts.
PER_PAGE_REVIEW = 12      # pages above this are worth a human glance (could be legend/table,
                         # could be over-marked) — reported, not auto-failed
MARKS = r'ESTABLISHED|OFFICIAL|SURVEYED|VOLATILE|[●◇▲◆]'

def main():
    pdf = sys.argv[1] if len(sys.argv) > 1 else "dossier.pdf"
    if not pdf.lower().endswith(".pdf"):
        c = glob.glob(os.path.join(pdf, "*.pdf")); pdf = c[0] if c else sys.exit("no PDF")
    pages = [p.extract_text() for p in PdfReader(pdf).pages]
    # count PROSE marks only — a mark inside a line that reads like prose (long line, few
    # digits), not a table row (short line, lots of numbers/arrows). Table rows legitimately
    # carry one mark each; prose should not.
    def prose_marks(t):
        n = 0
        for line in t.split("\n"):
            if not re.search(MARKS, line):
                continue
            digits = len(re.findall(r"\d", line))
            arrows = line.count("\u2192") + line.count("\u2194")
            words = len(line.split())
            is_table = (arrows >= 1) or (digits >= 4 and words < 14)
            if not is_table:
                n += len(re.findall(MARKS, line))
        return n
    counts = [prose_marks(t) for t in pages]
    marked = [c for c in counts if c > 0]
    avg = sum(marked)/len(marked) if marked else 0
    hot = [(i+1, c) for i, c in enumerate(counts) if c > PER_PAGE_REVIEW]

    print(f"\n  MARK-DENSITY — {len(pages)} pages\n" + "  " + "-"*44)
    print(f"  pages carrying marks: {len(marked)}")
    print(f"  avg marks per marked page: {avg:.1f}  (want <= {AVG_MAX})")
    print(f"  worst page: {max(counts)} marks")
    print("  " + "-"*44)
    fails = []
    if avg > AVG_MAX:
        fails.append(f"average {avg:.1f} marks/page (> {AVG_MAX}) — the prose is over-marked."
                     " A mark is one per load-bearing fact, not one per sentence. This is the"
                     " confetti failure (writing-code.md).")
    if hot:
        # per-page is a REVIEW flag, not a hard fail — legend pages and comparison tables
        # legitimately concentrate marks. Only escalate if the average ALSO fails.
        note = ", ".join(f"p{p}({c})" for p, c in hot[:8])
        if avg > AVG_MAX:
            fails.append(f"worst pages: {note} — mark-per-sentence, cut them.")
        else:
            print(f"  ⚠ pages to eyeball (legend/table concentrate marks legitimately;"
                  f" over-marking does too): {note}")
    # also check for mid-sentence marks: a mark followed by a lowercase word
    midsent = 0
    for t in pages:
        midsent += len(re.findall(r'(?:ESTABLISHED|OFFICIAL|SURVEYED|VOLATILE)\s+[a-z]', t))
    if midsent > 3:
        fails.append(f"{midsent} marks appear mid-sentence (followed by a lowercase word) — "
                     "marks go at the END of the sentence they certify, never breaking a clause.")
    if fails:
        print("  MARK GATE — FAILURES:")
        for f in fails: print(f"  \u2717 {f}")
        print("\n  Fix: cut marks down to one per paragraph on the load-bearing claim only;")
        print("  most paragraphs (analysis, synthesis) carry NO mark. See writing-code.md.")
        return 1
    print("  mark gate: PASS — marks are seasoning, not confetti")
    return 0

if __name__ == "__main__":
    sys.exit(main())
