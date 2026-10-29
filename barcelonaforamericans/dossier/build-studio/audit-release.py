#!/usr/bin/env python3
"""Stage G — the ONE release entry point. Runs all six gates and FAILS CLOSED.

Why this exists: SKILL.md required four clean gates, while references/g-audit.md
said "Run ONE command. Ship on green." and pointed at audit-book.py — which never
invoked audit-furniture.py, audit-layout.py or audit-ai-smell.py. Two competing
release contracts, and the shorter one won because it was the one written down as
a command. A book could ship having passed one gate out of four.

It also fails closed. audit-depth.py previously went quiet when it could not find
a corpus, so a missing input read as an absent problem — the same shape as a gate
that cannot run at all. Here, a gate whose inputs are missing is a BLOCKED result
and the release does not pass. State that you skipped it deliberately with
--skip <gate>, which is recorded in the output rather than hidden.

Usage:
  python3 audit-release.py <build-dir> [--paper RRGGBB] [--skip depth,ai-smell]

  <build-dir> is expected to hold: dossier.pdf, the paginated build HTML, the
  manuscript .md files, and corpus.json. Anything absent is reported by name.
"""
import glob, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True)
    return p.returncode, (p.stdout or "") + (p.stderr or "")


def sniff_paper(d):
    """Read the book's own paper colour out of its stylesheet.

    The furniture and book gates both carry a DEFAULT paper constant (Morocco's
    cream, F6EEDB). Every sheet of a book printed on any other stock reads as an
    unpainted white margin band against it: Barcelona failed all 32 pages on a
    book whose furniture was correct. A default that is one project's value is a
    landmine for the next project, so derive it and say so — an explicit --paper
    still wins.
    """
    import re
    for name in ("dossier3.html", "dossier.css"):
        p = os.path.join(d, name)
        if not os.path.exists(p):
            continue
        css = open(p, encoding="utf-8", errors="replace").read()
        m = re.search(r'--paper\s*:\s*#([0-9A-Fa-f]{6})', css)
        if m:
            return m.group(1).upper()
    return None


def main():
    args = sys.argv[1:]
    if not args or args[0].startswith("-"):
        print(__doc__)
        sys.exit(2)
    d = os.path.abspath(args[0])
    paper = None
    if "--paper" in args:
        paper = args[args.index("--paper") + 1]
    else:
        paper = sniff_paper(d)
    skip = set()
    if "--skip" in args:
        skip = {s.strip() for s in args[args.index("--skip") + 1].split(",") if s.strip()}

    pdf = os.path.join(d, "dossier.pdf")
    if not os.path.exists(pdf):
        alt = sorted(glob.glob(os.path.join(d, "*.pdf")))
        pdf = alt[0] if alt else None
    html = sorted(glob.glob(os.path.join(d, "*.html")))
    # The ai-smell gate must read the MANUSCRIPT, not whatever .md happens to sit
    # in the build directory. A bare glob fed it a build tree's 192-word README
    # and failed the release on that file's em-dash rate — a verdict about the
    # wrong text entirely. Prefer an explicit manuscript; fall back to other .md
    # only when there is none, and never a README or a changelog.
    # `manuscript*.md` was too narrow: one tree names its four parts
    # C-manuscript-part1.md … so the glob missed them and the fallback swept in
    # the PLANNING documents (batch plans, decision notes), measuring prose the
    # book never prints — 10.9 em-dashes per 1k against the manuscript's real 8.1.
    mds = sorted(glob.glob(os.path.join(d, "*manuscript*.md")))
    if not mds:
        mds = [p for p in sorted(glob.glob(os.path.join(d, "*.md")))
               if os.path.basename(p).lower() not in ("readme.md", "changelog.md", "notes.md")]
    corpus = [p for p in (os.path.join(d, "corpus.json"), os.path.join(d, "articles.json"))
              if os.path.exists(p)]

    gates = []
    # name, required inputs present?, command, what is missing
    gates.append(("furniture", bool(pdf),
                  [sys.executable, f"{HERE}/audit-furniture.py", pdf or ""] +
                  (["--paper", paper] if paper else []),
                  "dossier.pdf"))
    gates.append(("book", bool(pdf),
                  [sys.executable, f"{HERE}/audit-book.py", d] +
                  (["--paper", paper] if paper else []),
                  "dossier.pdf"))
    gates.append(("layout", bool(html),
                  [sys.executable, f"{HERE}/audit-layout.py", d],
                  "the paginated build HTML"))
    gates.append(("ai-smell", bool(mds),
                  [sys.executable, f"{HERE}/audit-ai-smell.py"] + mds,
                  "the manuscript .md files"))
    gates.append(("claims", bool(html),
                  [sys.executable, f"{HERE}/audit-claims.py", d],
                  "the paginated build HTML"))
    gates.append(("depth", bool(corpus and pdf),
                  [sys.executable, f"{HERE}/audit-depth.py", d],
                  "corpus.json (+ dossier.pdf)"))

    print(f"RELEASE AUDIT · {d}")
    if paper:
        src = "given" if "--paper" in args else "read from the build's stylesheet"
        print(f"paper stock #{paper} ({src})")
    print("=" * 64)
    verdicts = []
    for name, have, cmd, missing in gates:
        if name in skip:
            verdicts.append((name, "SKIPPED"))
            print(f"\n── {name} ── SKIPPED on request (recorded, not a pass)")
            continue
        if not have:
            verdicts.append((name, "BLOCKED"))
            print(f"\n── {name} ── BLOCKED: missing {missing}")
            continue
        rc, out = run(cmd)
        verdicts.append((name, "PASS" if rc == 0 else "FAIL"))
        print(f"\n── {name} ── {'PASS' if rc == 0 else 'FAIL'}")
        print("\n".join("   " + l for l in out.strip().splitlines()[-14:]))

    print("\n" + "=" * 64)
    for n, v in verdicts:
        print(f"  {v:8s} {n}")
    bad = [n for n, v in verdicts if v != "PASS"]
    if bad:
        print(f"\nNOT RELEASABLE — unresolved: {', '.join(bad)}")
        print("A BLOCKED gate is not a pass. Supply its input or state the skip.")
        sys.exit(1)
    print("\nProduction checks passed. This says the artefact is well-formed —")
    print("it does not say the reasoning is sound. The editorial release record")
    print("(comparisons, assembled trip, reversals) is a separate, human sign-off.")
    sys.exit(0)


main()
