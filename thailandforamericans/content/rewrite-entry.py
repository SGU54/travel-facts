# -*- coding: utf-8 -*-
"""rewrite-entry.py — the three entry articles now STATE the rule.

Until 15 Sep 2026 these pages deliberately refused to print a number: "we
deliberately don't quote a fixed number here — it could mislead you." That was
correct while the figure was genuinely in motion. It is settled now, and a page
that sends the reader off to find the answer has handed them our job.

The number is a FACT SPAN. When Thailand moves it again, one row of
common.facts changes every one of these sentences.
"""
import json, re, sys

DAYS = '<span class="fact" data-fact="entry.visa_free_days">30 days</span>'
EXT  = '<span class="fact" data-fact="entry.visa_free_extension">one 30-day extension at an immigration office, about 1,900 baht</span>'
LAND = '<span class="fact" data-fact="entry.land_border_limit">two visa-exempt entries per calendar year</span>'

EDITS = {
"do-americans-need-visa-thailand": [
 ("<p>For most American tourists, Thailand is refreshingly easy to enter — you generally don't need to arrange a visa in advance for a normal vacation. But the rules have a few important details, and Thailand has been changing its visa-exemption terms during 2026, so it's essential to verify the current requirements for your specific travel date. Here's what you need to know.</p>",
  f"<p>For most American tourists, Thailand is refreshingly easy to enter — you "
  f"generally don't need to arrange a visa in advance for a normal vacation. The one "
  f"thing that did change recently is how long you may stay: on 15 September 2026 the "
  f"visa-free allowance was cut from 60 days back to {DAYS}. Here's what you need to "
  f"know.</p>"),

 ("<p>U.S. passport holders are on Thailand's <strong>visa-exemption list</strong>, which means you can enter for tourism without arranging a visa beforehand — you receive permission to stay on arrival. This covers normal vacation trips. You will, however, need to complete the mandatory <strong>digital arrival card</strong> (see below), and there are conditions on the length of stay that have been in flux in 2026.</p>",
  f"<p>U.S. passport holders are on Thailand's <strong>visa-exemption list</strong>, "
  f"which means you can enter for tourism without arranging a visa beforehand — you "
  f"receive permission to stay on arrival. This covers normal vacation trips. You will, "
  f"however, need to complete the mandatory <strong>digital arrival card</strong> (see "
  f"below), and there is a limit on how long that permission lasts.</p>"),

 ("<p>This is the part that's been changing. The permitted length of a visa-exempt tourist stay for Americans has been the subject of policy changes in 2026, with the maximum number of days under review and revision. Because the exact figure depends on the rule in force on your entry date, <strong>we deliberately don't quote a fixed number here</strong> — it could mislead you. Check the current permitted stay on the official Thai immigration or e-Visa website close to your travel date. Whatever the figure, a normal one-to-three-week vacation comfortably fits within it.</p>",
  f"<p><strong>{DAYS}.</strong> That has been the rule since 15 September 2026, when "
  f"Thailand rolled back the 60-day allowance it had granted since 2024. The Cabinet "
  f"approved the change in May and the Ministry of Interior notices were published in "
  f"the Royal Gazette at the end of August.</p>"
  f"<p>If you want longer, there is {EXT}, applied for inside Thailand before your "
  f"current permission runs out. Approval is at immigration's discretion, so it is not "
  f"something to build a plan around, but it takes a normal trip to roughly 60 days.</p>"
  f"<p>One thing to understand about how this works in practice: the date that governs "
  f"you is the <strong>\"admitted until\" date the officer writes on your entry "
  f"stamp</strong>. Not the allowance in the abstract, not what a booking site said. "
  f"Officers apply the rule in force on the day you land, so read the stamp before you "
  f"leave the desk. A normal one-to-three-week vacation fits comfortably either way.</p>"
  f"<p>There is also a new restriction that does not affect most visitors: entering "
  f"visa-free over a <strong>land border</strong> is now limited to {LAND}. Arrivals by "
  f"air and sea are not limited, so a normal fly-in holiday is unaffected — it targets "
  f"repeated border runs.</p>"),

 ('<p>For a normal American vacation, you don\'t pre-arrange a visa — you enter under the visa exemption and complete the free TDAC online beforehand. Just confirm the current permitted length of stay and <a href="/article/thailand-entry-requirements-americans">entry requirements</a> on official sources close to your travel date, since these have been changing.',
  f'<p>For a normal American vacation, you don\'t pre-arrange a visa — you enter under '
  f'the visa exemption for {DAYS}, and complete the free TDAC online beforehand. Check '
  f'the rest of the <a href="/article/thailand-entry-requirements-americans">entry '
  f'requirements</a> before you fly.'),

 ("<p>For tourism, generally no — U.S. passport holders enter under Thailand's visa exemption without arranging a visa in advance. You must still complete the free online TDAC, and should confirm the current permitted stay for your dates.</p>",
  f"<p>For tourism, generally no — U.S. passport holders enter under Thailand's visa "
  f"exemption without arranging a visa in advance, currently for {DAYS}. You must still "
  f"complete the free online TDAC.</p>"),

 ("<p>The permitted visa-exempt stay has been changing in 2026, so check the official Thai immigration or e-Visa site for the current figure near your travel date. A normal one-to-three-week vacation fits within any version of the rule.</p>",
  f"<p>{DAYS}, since 15 September 2026, when the 60-day allowance was rolled back. A "
  f"normal one-to-three-week vacation fits comfortably. For longer, there is one "
  f"30-day extension available inside Thailand.</p>"),
],

"thailand-entry-requirements-americans": [
 ("<p>Entering Thailand as an American is generally straightforward, but there's a checklist of requirements worth getting right before you fly — from passport validity to the mandatory digital arrival card. Some of these are strictly enforced, others occasionally checked, and a few details have been changing in 2026. Here's the complete picture.</p>",
  f"<p>Entering Thailand as an American is generally straightforward, but there's a "
  f"checklist of requirements worth getting right before you fly — from passport "
  f"validity to the mandatory digital arrival card. Some are strictly enforced, others "
  f"only occasionally checked, and the visa-free allowance was cut to {DAYS} on "
  f"15 September 2026. Here's the complete picture.</p>"),

 ('<p>U.S. passport holders can enter Thailand for tourism <strong>without arranging a visa in advance</strong>, under Thailand\'s visa-exemption scheme — you receive permission to stay on arrival. The permitted <strong>length of that stay has been changing during 2026</strong>, so rather than rely on a fixed number, confirm the current allowance on the official Thai immigration or e-Visa site near your travel date. A normal vac',
  f'<p>U.S. passport holders can enter Thailand for tourism <strong>without arranging a '
  f'visa in advance</strong>, under Thailand\'s visa-exemption scheme — you receive '
  f'permission to stay on arrival. That permission is <strong>{DAYS}</strong> as of '
  f'15 September 2026, reduced from the 60 days granted since 2024; a further 30-day '
  f'extension can be applied for inside Thailand. Whatever the rule says, the date that '
  f'binds you is the one stamped in your passport on arrival. A normal vac'),

 ("<p>A passport valid 6+ months, entry under the visa exemption for tourism, the completed free TDAC, and ideally proof of onward travel and funds. Confirm the current permitted stay on official sites before traveling.</p>",
  f"<p>A passport valid 6+ months, entry under the visa exemption for tourism "
  f"({DAYS} since 15 September 2026), the completed free TDAC, and ideally proof of "
  f"onward travel and funds.</p>"),
],

"thailand-for-americans-first-timer-guide": [
 ("<p>For tourism, no — you enter visa-free under the exemption, but must complete the free online TDAC and have a passport valid six months out. Confirm the current permitted stay on official sites, as it's been changing.</p>",
  f"<p>For tourism, no — you enter visa-free under the exemption for {DAYS} (reduced "
  f"from 60 on 15 September 2026), but must complete the free online TDAC and have a "
  f"passport valid six months out.</p>"),
],
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
                sys.exit(f"NO MATCH ({a['content'].count(old)}) — {slug}\n  {old[:130]}…")
            a["content"] = a["content"].replace(old, new)
            n += 1
    json.dump(d, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"  rewrote {n} passages across {len(EDITS)} entry articles")

main()
