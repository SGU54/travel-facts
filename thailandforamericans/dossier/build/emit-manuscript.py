# -*- coding: utf-8 -*-
"""emit-manuscript.py — write the prose out as .md so Stage G can judge it.

The manuscript lives in content.py because the builder needs it as data. The
ai-smell gate reads .md and, without these files, reports BLOCKED — which is not
a pass. This emits the SAME strings the PDF prints, so the gate judges the shipped
prose rather than a copy that can drift from it.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content as C

HERE = os.path.dirname(os.path.abspath(__file__))


def clean(t):
    for k in C.MARKS:
        t = t.replace("{" + k + "}", "")
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t)).strip()


def sec(out, title, d, kind):
    out += [f"# {title}", ""]
    for key in ("scope",):
        if d.get(key):
            out.append(f"**{key}:** {clean(d[key])}")
    if d.get("open_call"):
        out += ["", clean(d["open_call"]), "", clean(d["open_exception"])]
    out += ["", clean(d["lede"]), ""]
    out += [clean(p) for p in d["body"]]
    if d.get("call"):
        out += ["", "**The call.** " + clean(d["call"])]
    if d.get("plate"):
        out += ["", clean(d["plate"]["caption"])]
    out += ["", ""]
    return out


def main():
    dec, frame = ["# Thailand, Covered. — the decisions", ""], \
                 ["# Thailand, Covered. — frame, essays and field sheet", ""]
    for d in C.DECISIONS:
        dec = sec(dec, f"Decision {d['n']} · {d['cat']} — {d['q']}", d, "decision")
    for e in C.ESSAYS_FRONT + [C.ESSAY_RISK] + C.ESSAYS_BACK + [C.REFUSALS]:
        frame = sec(frame, f"Essay · {e['q']}", e, "essay")
    for P in C.PARTS:
        frame += [f"# Part · {P['title']}", "", clean(P["blurb"]), ""]
    frame += [f"# {C.HOWTO['title']}", "", clean(C.HOWTO["standfirst"]), ""]
    frame += [clean(b) for _, b in C.HOWTO["blocks"]] + [""]
    frame += [f"# {C.FIELD_SHEET['q']}", "", clean(C.FIELD_SHEET["scope"]), ""]
    for card in C.FIELD_SHEET["cards"]:
        frame += [f"## {card['title']}", "", clean(card["sub"]), ""]
        frame += [clean(v) for _, v in card["items"]] + [""]

    for name, lines in (("decisions-draft.md", dec),
                        ("frame-and-fieldsheet.md", frame)):
        path = os.path.join(HERE, name)
        open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
        print(f"  wrote {name}  ({len(' '.join(lines).split()):,} words)")


main()
