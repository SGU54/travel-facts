# -*- coding: utf-8 -*-
"""expand-drafts.py — bring the six short drafts into the sanctioned band.

Not padding. Each article opens a promise it never keeps, and the addition is
that promise: the cost section a medical piece announces in its own intro, the
return journey an air-map piece only describes one way, the "so what do I do"
an airport-gap piece diagnoses and never answers. Every fact below is already in
this site's reporting or in facts.json — nothing new is claimed.

Each insertion goes BEFORE the closing "how this fits the trip" section, so the
article still ends by handing off to the guide.
"""
import json, re, sys

ADD = {
# 799 -> the road piece surveys surfaces and lighting but never states what the
# law requires of anyone riding on them. That is a road condition too.
"thailand-road-conditions-by-region": ("<h2>What the law requires on these roads</h2>", """
<h2>What the law requires on these roads</h2>
<p>Two rules travel with the conditions above. <strong>Helmets are legally required for both rider and passenger</strong>, and riding a motorbike legally needs a motorcycle licence from your home country plus an International Driving Permit — both, not either.</p>
<p>Enforcement is the part that misleads. Police checkpoints are common in tourist areas, and being stopped without the right permit or helmet typically means a fine of a few hundred baht, commonly in the region of 400 to 500. Travellers who have been stopped once tend to conclude the whole issue is minor.</p>
<p>The fine is not the risk. Many travel policies exclude a motorbike claim where the rider held no valid motorcycle licence or was not wearing a helmet — and on an unlit road with no footpath, that exclusion meets exactly the conditions this page describes. Our guide to <a href="/article/renting-a-car-in-thailand">renting a car or scooter</a> sets out the licence chain in full.</p>
"""),

# 779 -> the intro promises "what it costs" and the article never says.
"medical-care-in-thailand-for-visitors": ("<h2>What it costs</h2>", """
<h2>What it costs</h2>
<p>Private care in Thailand is inexpensive by American standards for small things and expensive in absolute terms for large ones, and the gap between those two is where travellers get caught.</p>
<p>A pharmacy consultation or a clinic visit for an infection or a stomach upset is the kind of sum you would not think twice about at home. A serious injury requiring surgery at a private hospital runs into the tens of thousands of US dollars, and a medical evacuation off a small island runs into five figures on top of that.</p>
<p>Neither number is the reason to worry — the reason is the payment order described below. A hospital that wants a guarantee of payment before treating you is asking a question your insurer answers, not your credit card, provided the call was made in time. Two things Americans routinely assume cover them generally do not: US domestic health insurance provides little or no coverage abroad, and credit-card travel benefits are usually thinner than a dedicated policy.</p>
"""),

# 767 -> diagnoses the gap thoroughly, never says what to do about it.
"bangkok-airport-transfer-bkk-dmk": ("<h2>What to do about it</h2>", """
<h2>What to do about it</h2>
<p>There are only three honest answers, and the first two are decided at booking.</p>
<p><strong>Put both legs on one ticket.</strong> Then the airline owns the connection, your bag is through-checked, and none of the arithmetic above is yours.</p>
<p><strong>Or give the gap a night.</strong> Sleep in Bangkok and fly south the next morning. This is the option that survives a delayed transpacific arrival, and it is cheaper than the replacement ticket a missed separately-booked flight costs.</p>
<p><strong>Or, if you must connect the same day, arrive early and not late.</strong> The road leg is the variable, and the variable is set by the clock: a mid-afternoon landing puts the transfer into Bangkok's worst traffic, where the same 50 km takes two and a half hours instead of forty-five minutes.</p>
"""),

# 750 -> presents a two-way choice without saying where the train does not go.
"domestic-flights-vs-overnight-train-thailand": ("<h2>Where the train does not go</h2>", """
<h2>Where the train does not go</h2>
<p>One limit is worth stating plainly, because the comparison above only holds on the routes where both options exist.</p>
<p>The sleeper serves Chiang Mai in the north and Surat Thani in the south. <strong>Surat Thani is a mainland town, not an island</strong> — it is the gateway for the Gulf islands, and reaching Koh Samui, Koh Phangan or Koh Tao from it still means a bus-and-boat or ferry transfer on top of the overnight journey.</p>
<p>For Phuket and Krabi there is no equivalent choice at all: neither is on the rail network, so the comparison there is a flight against a long overland bus, which is a different question from the one on this page.</p>
"""),

# 734 -> warns about separate tickets but never about the basket that hides them.
"thailand-domestic-flight-baggage-and-changes": ("<h2>The basket that looks like one ticket</h2>", """
<h2>The basket that looks like one ticket</h2>
<p>The distinction between one ticket and two is the whole of the section above, which makes it worth knowing how the two are told apart — because a booking site will happily sell you two and show you one confirmation.</p>
<p>A single ticket, or a connection between codeshare partners on one itinerary, carries one booking reference for the whole journey and through-checks the bag to the final destination. Two tickets sold together in one basket carry <strong>two separate references</strong>, and everything in the section above applies: no protection, no through-checking, and a forfeited fare if the first leg runs late.</p>
<p>The reference count is the test, and it is visible on the confirmation email before you fly rather than at a check-in desk after you land.</p>
"""),

# 705 -> describes the journey outbound only; the return is where it bites.
"getting-to-the-southern-islands-by-air": ("<h2>The return is the harder direction</h2>", """
<h2>The return is the harder direction</h2>
<p>Everything above describes the journey out. The same legs run in reverse at the end of the trip, and that is the direction that costs something, because an international departure is waiting at the end of them.</p>
<p>Going out, a delayed boat costs you an afternoon. Coming back, the same delay runs through a road transfer and a domestic flight before it reaches a long-haul ticket that was almost certainly booked separately — and a separately booked leg carries no protection at all. The undocumented last departure times matter most here: the question is not whether a boat runs that day but whether the one you need still connects.</p>
<p><strong>The practical answer is to come back a day early</strong> and spend the last night on the mainland or in Bangkok. It converts the whole chain from a risk into a buffer, and it is the one decision on this page that costs nothing to make in advance.</p>
"""),
}

def main():
    d=json.load(open("/tmp/left.json",encoding="utf-8"))
    arts=d["articles"] if isinstance(d,dict) and "articles" in d else d
    by={a["slug"]:a for a in arts}
    out=[]
    for slug,(marker,block) in ADD.items():
        a=by[slug]; c=a["content"]
        if marker in c: sys.exit(f"ALREADY PRESENT — {slug}: {marker}")
        # insert before the closing hand-off section (the last <h2> before FAQ)
        h2s=[m.start() for m in re.finditer(r'<h2[^>]*>', c)]
        faq=c.find('<h2>FAQ') if '<h2>FAQ' in c else len(c)
        before=[p for p in h2s if p < faq]
        if len(before) < 2: sys.exit(f"unexpected shape — {slug}")
        at=before[-1]                      # the "how this fits the trip" heading
        a["content"]=c[:at]+block.strip()+"\n\n"+c[at:]
        a["status"]="published"
        w=len(re.sub(r'<[^>]+>',' ',a["content"]).split())
        print(f"  {w:5d}w  (+{w-len(re.sub(r'<[^>]+>',' ',c).split()):3d})  {slug}")
        out.append(a)
    shell=dict(d) if isinstance(d,dict) else None
    if shell is not None and "articles" in shell: shell["articles"]=out
    else: shell=out
    json.dump(shell, open("publish-drafts-b.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
    print("  → publish-drafts-b.json")

main()
