#!/usr/bin/env python3
"""
audit-ai-smell.py — does this dossier read like it was written by an AI?
Judges PROSE ONLY (excludes titles, tables, for/against, notes, marks) because
an em-dash in a heading is typography, not a tell. Run on the .md manuscript(s).

Usage: python3 audit-ai-smell.py file1.md [file2.md ...]
Exit 0 = CLEAN (ships), 1 = FLAGS (fix before render).
"""
import re,sys,statistics as st
from collections import Counter

files=sys.argv[1:] or ['decisions-draft.md','frame-and-fieldsheet.md']
raw='\n'.join(open(f).read() for f in files)

# keep prose only
prose_lines=[]
for l in raw.split('\n'):
    s=l.strip()
    if (not s or s.startswith('#') or s.startswith('|') or s.startswith('**for**')
        or s.startswith('**against**') or s.startswith('◆') or s.startswith('**cols')
        or s.startswith('**Lede') or s.startswith('**The trade') or s.startswith('**The')
        or set(s)<=set('- ') or s.startswith('>')): 
        # keep verdict bodies (**The call.** ...) — they ARE prose
        if s.startswith('**The call'): pass
        else: continue
    prose_lines.append(l)
prose=re.sub(r'\*\*[^*]+\*\*',' ',' '.join(prose_lines))   # strip bold labels
prose=re.sub(r'[*`_]',' ',prose)
sents=[s.strip() for s in re.split(r'(?<=[.!?])\s+',prose) if len(s.split())>3]
words=re.findall(r"[a-z']+",prose.lower()); N=max(len(words),1)
FLAGS=[]

# 1. LLM-tell vocabulary
llm=['delve','tapestry','testament','vibrant','bustling','nestled','myriad','plethora','embark',
 'seamless','moreover','furthermore','ultimately','notably','robust','curated','immerse','boasts',
 'breathtaking','stunning','elevate','crucial','landscape','realm','unlock','harness','leverage',
 'holistic','must-visit','gem','navigating','intricate','vibrant','rich tapestry','treasure trove']
found={w:len(re.findall(r'\b'+re.escape(w)+r'\b',prose,re.I)) for w in llm}
found={k:v for k,v in found.items() if v}
if found: FLAGS.append(f"LLM vocab: {found}")

# 2. antithesis tic "not X but Y"
anti=len(re.findall(r"\bnot (just |merely |only )?\w+.{0,40}?,? but\b",prose,re.I))
anti+=len(re.findall(r"it'?s not .{0,40}?,? it'?s",prose,re.I))
if anti>5: FLAGS.append(f"'not X but Y' tic x{anti}")

# 3. em-dash density in PROSE
em=prose.count('—'); d1k=em/N*1000
if d1k>8: FLAGS.append(f"em-dash {d1k:.1f}/1k (prose)")

# 4. sentence-length uniformity
lens=[len(s.split()) for s in sents]
cv=st.pstdev(lens)/max(st.mean(lens),1)
if cv<0.45: FLAGS.append(f"uniform rhythm CV {cv:.2f}")

# 5. tricolon overuse
tri=len(re.findall(r'\w+, \w+,? and \w+',prose))
if tri>N/350: FLAGS.append(f"tricolons x{tri}")

# 6. semicolon overuse (my own past failure mode)
semi=prose.count(';')
if semi/N*1000>12: FLAGS.append(f"semicolons {semi/N*1000:.1f}/1k")

print(f"AI-SMELL AUDIT — {N} words of prose across {len(files)} file(s)")
print(f"  em-dash {em/N*1000:.1f}/1k · rhythm CV {cv:.2f} · semicolons {semi/N*1000:.1f}/1k · tricolons {tri}")
if FLAGS:
    print("  FLAGS:"); [print("   ⚠",f) for f in FLAGS]
    print("\nSMELLS AI — fix before render."); sys.exit(1)
else:
    print("\nCLEAN — reads human. Ships."); sys.exit(0)
