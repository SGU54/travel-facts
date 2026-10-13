# -*- coding: utf-8 -*-
"""rewrite-visa.py — state the settled rule instead of hedging.

Thailand cut the US visa exemption from 60 days to 30 on 15 Sep 2026. Nothing on
the site was WRONG — every article said "the rule has been changing, confirm for
your date" — but that hedge was only right while the rule was in flux. Now it is
settled, and telling the reader to go and look it up is handing them our job.

The number goes in a FACT SPAN, so the next change is one SQL statement rather
than ten article rewrites. The span's fallback text is the value as written today;
`entry.visa_free_days` in common.facts overrides it at render.
"""
import json, re, sys

SPAN = '<span class="fact" data-fact="entry.visa_free_days">30 days</span>'
EXT  = '<span class="fact" data-fact="entry.visa_free_extension">one 30-day extension at an immigration office, about 1,900 baht</span>'
VISA = '<a href="/article/do-americans-need-visa-thailand">visa-free</a>'
ENTRY = '<a href="/article/thailand-entry-requirements-americans">entry requirements</a>'
TDAC = '<a href="/article/thailand-digital-arrival-card-tdac">Thailand Digital Arrival Card (TDAC)</a>'

EDITS = {
"best-thailand-itinerary-first-timers": [(
 "<p>And before you book anything, confirm your entry requirements: Thailand's visa-free rules for Americans have been changing in 2026, and the permitted visa-exempt stay has been in flux. File the free Thailand Digital Arrival Card (TDAC) online before you fly.</p>",
 f"<p>One entry note before you book: since 15 September 2026, U.S. passport holders "
 f"receive {SPAN} visa-free on arrival, down from the 60 days granted in 2024–26. "
 f"This trip fits inside that comfortably. File the free Thailand Digital Arrival Card "
 f"(TDAC) online before you fly.</p>")],

"10-day-thailand-itinerary": [(
 "<p>One housekeeping note before you book: Thailand's <a href=\"/article/do-americans-need-visa-thailand\">visa-free</a> rules for U.S. passport holders have been changing in 2026, and the permitted length of a visa-exempt stay has been in flux. Ten days sits comfortably inside any version of the rule, so this trip is unaffected — but confirm the current entry requirements for your travel date, and file your free Thailand Digital Arrival Card (TDAC) online before you fly.</p>",
 f"<p>One housekeeping note before you book: since 15 September 2026, U.S. passport "
 f"holders enter {VISA} for {SPAN}, down from the 60 days granted in 2024–26. Ten "
 f"days sits well inside that, so this trip is unaffected. File your free Thailand "
 f"Digital Arrival Card (TDAC) online before you fly.</p>"),
 ("<p>U.S. tourists enter visa-free, and 10 days is within any version of the visa-exempt stay. The exact limit has been changing in 2026, so confirm the current rule for your travel date and file the free TDAC online before you fly.</p>",
 f"<p>U.S. tourists enter visa-free for {SPAN} as of 15 September 2026, so 10 days "
 f"is comfortably inside the limit. File the free TDAC online before you fly.</p>")],

"2-weeks-in-thailand-itinerary": [(
 "<p>As always, confirm your <a href=\"/article/thailand-entry-requirements-americans\">entry requirements</a> before booking. Thailand's <a href=\"/article/do-americans-need-visa-thailand\">visa-free</a> stay rules for Americans have been changing in 2026, though two weeks falls inside any version of the rule. File the free <a href=\"/article/thailand-digital-arrival-card-tdac\">Thailand Digital Arrival Card (TDAC)</a> online before you fly.</p>",
 f"<p>Check your {ENTRY} before booking. Since 15 September 2026 Americans enter "
 f"{VISA} for {SPAN}, down from 60, and two weeks sits well inside that. File the free "
 f"{TDAC} online before you fly.</p>")],

"3-weeks-in-thailand-itinerary": [(
 "<p>Confirm your <a href=\"/article/thailand-entry-requirements-americans\">entry requirements</a> before booking, since a three-week stay sits closer to the visa-exemption limits that have been changing in 2026. U.S. tourists enter <a href=\"/article/do-americans-need-visa-thailand\">visa-free</a>, but verify the current permitted length for your travel date, and file the free <a href=\"/article/thailand-digital-arrival-card-tdac\">Thailand Digital Arrival Card (TDAC)</a> online before you fly.</p>",
 f"<p>Check your {ENTRY} before booking, because this is the trip length where the "
 f"2026 change actually bites. Americans entering {VISA} now get {SPAN} rather than the "
 f"60 days granted in 2024–26. Twenty-one nights still fits, but the margin is nine "
 f"days rather than five and a half weeks — so a delayed flight home is no longer "
 f"absorbed by the exemption. If you intend to stay beyond 30 days you need "
 f"{EXT}, applied for inside Thailand before your permission expires. File the free "
 f"{TDAC} online before you fly.</p>"),
 ("<p>Three weeks is closer to the visa-exemption limits, which have been changing in 2026. U.S. tourists enter visa-free, but confirm the current permitted length for your dates and file the free TDAC before flying.</p>",
 f"<p>Three weeks fits inside the {SPAN} Americans receive visa-free since 15 September "
 f"2026, with nine days to spare. Going beyond 30 days means applying for an extension "
 f"inside Thailand. File the free TDAC before flying.</p>")],

"7-day-thailand-itinerary": [(
 "<p>A quick note before you start booking: Thailand's <a href=\"/article/do-americans-need-visa-thailand\">visa-free</a> rules for U.S. passport holders are in flux in 2026, and the permitted length of a visa-exempt stay has been changing. A week-long trip sits comfortably inside any version of the rule, so this itinerary is unaffected — but always confirm the current <a href=\"/article/thailand-entry-requirements-americans\">entry requirements</a> for your travel date, and file your free Thailand Digital Arrival Card (TDAC) online before you fly.</p>",
 f"<p>A quick note before you start booking: since 15 September 2026, U.S. passport "
 f"holders enter {VISA} for {SPAN}, down from the 60 days granted in 2024–26. A week "
 f"is nowhere near that limit, so this itinerary is unaffected. Check the rest of the "
 f"{ENTRY} and file your free Thailand Digital Arrival Card (TDAC) online before you "
 f"fly.</p>"),
 ("<p>U.S. tourists enter Thailand visa-free, and a week is well within any version of the visa-exempt stay. The exact day limit has been changing in 2026, so confirm the current rule for your travel date, and file the free TDAC online before you fly.</p>",
 f"<p>U.S. tourists enter Thailand visa-free for {SPAN} as of 15 September 2026, so a "
 f"week is well inside the limit. File the free TDAC online before you fly.</p>")],

"7-days-bangkok-and-beaches": [(
 "<p>Before booking, confirm your entry rules — Thailand's <a href=\"/article/do-americans-need-visa-thailand\">visa-free</a> stay for Americans has been changing in 2026, though a week falls well within any version of it. File the free <a href=\"/article/thailand-digital-arrival-card-tdac\">Thailand Digital Arrival Card (TDAC)</a> online before you fly.</p>",
 f"<p>Before booking: Americans enter {VISA} for {SPAN} since 15 September 2026, down "
 f"from 60, and a week falls well inside that. File the free {TDAC} online before you "
 f"fly.</p>"),
 ("<p>U.S. tourists enter visa-free, and a week is within any version of the visa-exempt stay. Confirm the current rule for your travel date and file the free TDAC online before flying.</p>",
 f"<p>U.S. tourists enter visa-free for {SPAN} as of 15 September 2026, so a week is "
 f"comfortably inside the limit. File the free TDAC online before flying.</p>")],

"7-days-northern-thailand": [(
 "<p>As always, confirm your <a href=\"/article/thailand-entry-requirements-americans\">entry requirements</a> before booking — Thailand's <a href=\"/article/do-americans-need-visa-thailand\">visa-free</a> rules for Americans have been changing in 2026, though a week is within any version. File the free Thailand Digital Arrival Card (TDAC) online before you fly.</p>",
 f"<p>Check your {ENTRY} before booking. Americans enter {VISA} for {SPAN} since "
 f"15 September 2026, down from 60, and a week sits well inside that. File the free "
 f"Thailand Digital Arrival Card (TDAC) online before you fly.</p>")],
}

def main():
    path = "visa-update-live.json"
    d = json.load(open(path, encoding="utf-8"))
    arts = d["articles"] if isinstance(d, dict) and "articles" in d else d
    by = {a["slug"]: a for a in arts}
    n = 0
    for slug, pairs in EDITS.items():
        a = by[slug]
        for old, new in pairs:
            if a["content"].count(old) != 1:
                sys.exit(f"NO MATCH — {slug}\n  {old[:110]}…")
            a["content"] = a["content"].replace(old, new)
            n += 1
    json.dump(d, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"  rewrote {n} passages across {len(EDITS)} itinerary articles")

main()
