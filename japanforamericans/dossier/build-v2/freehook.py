# freehook.py — the ONE connection given away (model.md).
# "The buyer cannot see the whole book before paying, but one real connection,
#  free, proves the judgment is worth buying."
# It is the organising fact's own call: two long legs against a pass that needs four.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from design2 import CSS
from maps import fig_breakeven

EST = "<span class='mk est'>&#9679;</span>"
OFF = "<span class='mk off'>&#9671;</span>"
VOL = "<span class='mk vol'>&#9670;</span>"

BODY = f"""
<section class="chap" id="hook">
  <div class="opener">
    <div class="okind">A sample of the judgment &#183; free</div>
    <h1>Two legs, and a pass that needs four</h1>
    <div class="orule"></div>
  </div>
  <p class="standfirst">This is one of the connections the book makes. It is given away whole,
  arithmetic included, so you can judge the rest of it before paying for it.</p>

  <p class="lede">The trip nearly every first-timer takes has a shape so consistent it fits in
  a sentence: fly into Tokyo, spend several days, take one Shinkansen to Kyoto, spend several
  more, fly home. It contains exactly two long train journeys. {EST}</p>

  <p>The Japan Rail Pass needs about four to pay for itself. {EST}</p>

  <p>Those two facts live in different corners of the internet and almost never meet. For
  twenty years the pass was the correct reflex and the entire English-language web learned to
  recommend it. Then in October 2023 the seven-day ordinary pass rose from roughly
  &#165;29,650 to &#165;50,000 &#8212; about seventy per cent in one step &#8212; and the
  advice did not move. {OFF}</p>

  {fig_breakeven()}
  <div class="note" style="border:0;padding:0;margin:7px 0 0">
    <span class="fnum" style="font-family:var(--mono);font-size:8.5px;letter-spacing:.18em;color:var(--gilt)">FIG.</span>
    &nbsp;The break-even, drawn. Pay-as-you-go against the flat pass price.
  </div>

  <h2>The sum, in the open</h2>

  <p>A reserved ordinary seat from Tokyo to Kyoto costs about &#165;13,850. {OFF} Divide the
  pass price by that fare and it needs a little under four journeys of the same length before
  it breaks even &#8212; roughly two round trips inside a seven-day window. A trip with two
  long legs in it is not close to the line. It is at half.</p>

  <p>The second-order cost is the one no price comparison catches, and it is the reason this
  matters beyond the money. A pass already paid for is an argument in your pocket for using
  it. Routes bend to justify the purchase: a day trip added because it is free, a city
  inserted because the train is covered, a fortnight that was going to be two calm bases
  turning into five hotels and a lot of luggage on platforms. The purchase should follow the
  route. It usually leads it.</p>

  <div class="verdict"><span class="vlab">The call</span>
  <p><strong>Count your long journeys before you buy, not after.</strong> If the answer is two
  &#8212; and for the classic first trip it is &#8212; the national pass is a loss, and a
  regional pass or point-to-point tickets will cost you less and shape your route better.</p></div>

  <p>The book makes eight more connections like this one, each with the arithmetic on the page
  so you can disagree with it and still come out ahead.</p>

  <div class="note">{VOL} Prices move. They live on the Field Sheet, which is dated and
  reissued quarterly &#8212; the method above outlives every number in it.</div>
  <div class="endmark">&#9670;</div>
</section>
"""

doc = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
       '<title>Japan, Worked Out. — free sample</title>'
       f'<style>{CSS}</style></head><body>'
       f'<div class="flow">{BODY}</div></body></html>')
here = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(here, "freehook.html")
open(out, "w", encoding="utf-8").write(doc)
print(f"wrote {out} ({os.path.getsize(out):,} bytes)")
