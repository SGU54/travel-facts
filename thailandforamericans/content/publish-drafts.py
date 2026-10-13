# -*- coding: utf-8 -*-
"""publish-drafts.py — bring the two entry drafts up to date and publish them.

The 15 Sep 2026 cut from 60 days to 30 changes what these two articles are FOR:

  · an extension used to be an edge case (few tourists outgrew 60 days) and is
    now ordinary arithmetic — a five-week trip needs one.
  · "border runs attract scrutiny" was the honest vague answer. There is now a
    hard published rule: two visa-exempt land entries per calendar year.

Both get the new facts as spans, so the next change is a DB row.
"""
import json, re, sys

DAYS = '<span class="fact" data-fact="entry.visa_free_days">30 days</span>'
LAND = '<span class="fact" data-fact="entry.land_border_limit">two visa-exempt entries per calendar year</span>'

EDITS = {
"thailand-visa-extension-process": [
 ("<p>Americans arriving in Thailand for tourism receive a visa exemption stamp at immigration. That stamp can usually be extended once, at an immigration office, for a fee. The process is routine and the details are rarely written down anywhere useful. Here they are.</p>",
  f"<p>Americans arriving in Thailand for tourism receive a visa exemption stamp at "
  f"immigration. That stamp can usually be extended once, at an immigration office, "
  f"for a fee. The process is routine and the details are rarely written down anywhere "
  f"useful. Here they are.</p>"
  f"<p>This matters more than it used to. Until 15 September 2026 the exemption ran "
  f"60 days, and almost no holiday outgrew it — extensions were the business of "
  f"long-stayers. The allowance is now {DAYS}, so a five-week trip, a slow "
  f"island-hopping route or a stay built around a diving course runs into the limit "
  f"where it previously would not have. The extension is what takes you back to "
  f"roughly the old length.</p>"),

 ("<p>Commonly once per entry for a visa exemption or tourist visa. Anything beyond a single extension is discretionary rather than routine.</p>",
  f"<p>Commonly once per entry for a visa exemption or tourist visa. Anything beyond a "
  f"single extension is discretionary rather than routine. One extension on top of the "
  f"current {DAYS} gives roughly 60 days in total — the same ceiling the exemption "
  f"used to grant outright, now reached in two steps with a fee and an office visit in "
  f"the middle.</p>"),

 ("<p>Repeated back-to-back entries attract additional scrutiny at immigration, and admission on a visa exemption is at the officer's discretion rather than automatic. Thai visa policy has tightened repeatedly in recent years, and the practical reception of frequent border runs has moved with it.</p>",
  f"<p>Repeated back-to-back entries attract additional scrutiny at immigration, and "
  f"admission on a visa exemption is at the officer's discretion rather than "
  f"automatic.</p>"
  f"<p>Since 15 September 2026 there is also a hard limit rather than just a frown: "
  f"entering visa-free across a <strong>land border</strong> is capped at {LAND}. "
  f"Arrivals by air and sea are not limited, so this does not touch a normal fly-in "
  f"holiday — but it does end the practice of stepping over a border and straight back "
  f"to reset the clock a third time. Where a border run was once the cheap alternative "
  f"to an extension, for land crossings it is now rationed.</p>"),
],

"thailand-entry-refusal-and-overstay": [
 ("<p>Back-to-back visa-exempt entries attract additional scrutiny, and admission on an exemption is at the officer's discretion rather than automatic. Thai policy in this area has tightened repeatedly, and what was routine in one year has not always been routine in the next.</p>",
  f"<p>Back-to-back visa-exempt entries attract additional scrutiny, and admission on "
  f"an exemption is at the officer's discretion rather than automatic. Thai policy in "
  f"this area has tightened repeatedly, and what was routine in one year has not always "
  f"been routine in the next.</p>"
  f"<p>Since 15 September 2026 part of that discretion has become a written rule: "
  f"visa-exempt entry across a <strong>land border</strong> is limited to {LAND}. "
  f"Arrivals by air and sea are not capped. The same set of changes cut the exemption "
  f"itself to {DAYS}, which shortens the runway on every deadline described above.</p>"),
],
}

def main():
    src = json.load(open("/tmp/live-now.json", encoding="utf-8"))
    arts = src["articles"] if isinstance(src, dict) and "articles" in src else src
    by = {a["slug"]: a for a in arts}
    out = []
    for slug, pairs in EDITS.items():
        a = by[slug]
        for old, new in pairs:
            if a["content"].count(old) != 1:
                sys.exit(f"NO MATCH ({a['content'].count(old)}) — {slug}\n  {old[:120]}…")
            a["content"] = a["content"].replace(old, new)
        a["status"] = "published"          # --set-status will honour this
        w = len(re.sub(r"<[^>]+>", " ", a["content"]).split())
        print(f"  {slug}: {w} words, status -> published")
        out.append(a)
    shell = dict(src) if isinstance(src, dict) else None
    if shell is not None and "articles" in shell:
        shell["articles"] = out
    else:
        shell = out
    json.dump(shell, open("publish-drafts.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("  → publish-drafts.json")

main()
