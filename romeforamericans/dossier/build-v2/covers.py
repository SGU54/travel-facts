# -*- coding: utf-8 -*-
"""covers.py — the cover. Its device is the organising fact made visual: the 1.5km walk-ring
from real coordinates (D.5). Subtitle leads on EXPERIENCE per the counted dominant-edge tally,
NOT savings. Own render pass; cover >=6% non-paper ink.
"""
from design import PALETTE as C
from maps import cover_ring

def cover_html():
    ring = cover_ring()
    return f"""
<div class="coverpage">
  <div class="cov-frame">
    <div class="cov-top">
      <div class="cov-imprint">LA TAVOLA \u00b7 A DECISION MANUAL</div>
      <div class="cov-rule"></div>
    </div>

    <div class="cov-title">
      <h1>Rome,<br>Solved.</h1>
      <p class="cov-sub">Which of it is actually worth your time \u2014<br>and which is the photo everyone regrets.</p>
    </div>

    <div class="cov-ring">{ring}</div>

    <div class="cov-foot">
      <div class="cov-thesis">The historic core is a kilometre and a half across.<br>
        You walk it. This book is that one fact, worked out.</div>
      <div class="cov-meta">
        <span>FIRST EDITION</span><span class="dot">\u25c6</span><span>ROME FOR AMERICANS</span>
      </div>
    </div>
  </div>
</div>
"""

def cover_css():
    c = C
    return f"""
.coverpage{{ width:8.5in; height:8.85in; background:{c['paper']}; position:relative;
  overflow:hidden; page-break-after:always; }}
.coverpage::before{{ content:""; position:absolute; inset:0;
  background:
    radial-gradient(circle at 50% 40%, {c['stone']}55 0%, transparent 60%),
    {c['paper']}; }}
.cov-frame{{ position:absolute; inset:34px; border:1px solid {c['gilt']};
  padding:30px 40px; display:flex; flex-direction:column; }}
.cov-frame::after{{ content:""; position:absolute; inset:7px; border:0.5px solid {c['line']}; pointer-events:none; }}

.cov-top{{ position:relative; z-index:2; }}
.cov-imprint{{ font-family:'IBM Plex Mono'; font-size:10px; letter-spacing:.34em;
  color:{c['accent']}; text-transform:uppercase; }}
.cov-rule{{ height:1px; background:{c['gilt']}; margin-top:14px; }}

.cov-title{{ position:relative; z-index:2; margin-top:40px; }}
.cov-title h1{{ font-family:'IM Fell English'; font-weight:normal; font-size:104px;
  line-height:0.92; margin:0; color:{c['ink']}; letter-spacing:-0.01em; }}
.cov-sub{{ font-family:'IM Fell English'; font-style:italic; font-size:21px; line-height:1.42;
  color:{c['deep']}; margin:22px 0 0 0; max-width:5.2in; }}

.cov-ring{{ position:relative; z-index:1; flex:1; display:flex; align-items:center;
  justify-content:center; margin:8px 0; }}
.cov-ring svg{{ width:82%; height:auto; max-height:3.7in; }}

.cov-foot{{ position:relative; z-index:2; }}
.cov-thesis{{ font-family:'Sorts Mill Goudy'; font-size:13px; line-height:1.6;
  color:{c['muted']}; padding-top:18px; border-top:1px solid {c['line']}; }}
.cov-meta{{ font-family:'IBM Plex Mono'; font-size:9.5px; letter-spacing:.24em;
  color:{c['soft']}; text-transform:uppercase; margin-top:16px;
  display:flex; align-items:center; gap:14px; }}
.cov-meta .dot{{ color:{c['gilt']}; letter-spacing:0; }}
"""
