# freehook.py — the ONE connection given away (model.md).
# "The buyer cannot see the whole book before paying, but one real connection,
#  free, proves the judgment is worth buying."
# It is the organising fact's own call: the order of the nights is the residue
# of three pins set by the ticket, the sea and the airport. Decision 02, whole.
import os, sys, html, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from design2 import CSS
from maps import fig_order, fig_island
from content import DECISIONS
from evidence import CLAIMS

d = [x for x in DECISIONS if x["n"] == "02"][0]
MARKS = {"{EST}": "<span class='mk est'>&#9679;</span>", "{OFF}": "<span class='mk off'>&#9671;</span>",
         "{SUR}": "<span class='mk sur'>&#9650;</span>", "{VOL}": "<span class='mk vol'>&#9670;</span>"}
MARK_RE = re.compile(r"<span class='mk (?:est|off|sur|vol)'>[^<]*</span>")
def season(block):
    def fix(m):
        inner = m.group(2); marks = MARK_RE.findall(inner)
        if not marks: return m.group(0)
        stripped = re.sub(r"\s+([.,;:])", r"\1", MARK_RE.sub("", inner)).rstrip()
        return f"<p{m.group('attrs')}>{stripped} {marks[0]}</p>"
    return re.sub(r"<p(?P<attrs>[^>]*)>(.*?)</p>", fix, block, flags=re.S)
def sub(t):
    for k, v in MARKS.items(): t = t.replace(k, v)
    t = re.sub(r'\{C:([a-z0-9-]+)\}', lambda m: html.escape(CLAIMS[m.group(1)]["display"]["book"], quote=True), t)
    t = re.sub(r'\bDecision (0[1-9]|1[0-9])\b', r'Decision \1', t)
    return t

rows = "".join(f'<tr><td>{sub(a)}</td><td>{sub(b)}</td></tr>' for a, b in d["rows"])
BODY = f"""
<section class="dec chap" id="hook">
  <div class="pack"><div class="opener">
    <div class="okind">A sample of the judgment &#183; free</div>
    <h1>{d["q"]}</h1>
    <div class="orule"></div>
  </div>
  <span class="rh-src">Free sample</span><span class="pos-src">Decision 02 of 11, given away</span>
  <p class="standfirst">This is one of the eleven connections the book makes. It is given away whole,
  figure and arithmetic included, so you can judge the rest of it before paying for it.</p>
  <p class="lede">{sub(d["lede"])}</p></div>
  <figure class="fig">{fig_island()}<figcaption><span class="fnum">FIG.1</span> &nbsp;Every base the site measured, ranked by road miles from the airport. Nothing is far in miles — four to sixty-two, the whole island; the colour is the kind of journey, which is why Sidemen and Padang Bai share 35 miles and not a band. The hours are the subject of the book.</figcaption></figure>
  <figure class="fig">{fig_order()}<figcaption><span class="fnum">FIG.2</span> &nbsp;The same ten nights, in two orders. The three pins are the points the trip cannot move; the second order puts each of them where it costs least.</figcaption></figure>
  <div class="ledger wrap"><div class="lcap">{d["table_title"]}</div>
  <table><tr><th>{d["cols"][0]}</th><th>{d["cols"][1]}</th></tr>{rows}</table></div>
  {season(sub(d["reasoning"]))}
  <div class="verdict"><span class="vlab">The call</span><p>{sub(d["verdict"])}</p></div>
  <div class="forks">
    <div class="fork f"><b>When the other call is right</b><ul>{"".join(f"<li>{x}</li>" for x in d["for"])}</ul></div>
    <div class="fork a"><b>When ours is wrong for you</b><ul>{"".join(f"<li>{x}</li>" for x in d["against"])}</ul></div>
  </div>
  <div class="note">{sub(d["note"])}</div>
  <p>The book makes ten more connections like this one &#8212; the nights, the month, the entry
  stack, the road, the island leg, the day, Nyepi, the flight, the health chain, and the money &#8212;
  each with the arithmetic on the page, so you can disagree with it and still come out ahead.</p>
  <div class="endmark">&#10070;</div>
</section>
"""
doc = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
       '<title>Bali, in Its Own Time. — free sample</title>'
       f'<style>{CSS}</style></head><body>'
       f'<div class="flow">{BODY}</div></body></html>')
here = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(here, "freehook.html")
open(out, "w", encoding="utf-8").write(doc)
print(f"wrote {out} ({os.path.getsize(out):,} bytes)")
