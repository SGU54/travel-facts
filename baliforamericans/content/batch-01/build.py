#!/usr/bin/env python3
"""Assemble import-batch-NN.json from src/*.html. Checks: text word count, answer-first
(first block under each H2 is 40-80 words and does not open on a bare pronoun), every
fact span resolves to a facts.json key, guide-span counts match the article-list tags."""
import json,re,sys,os,html
HERE=os.path.dirname(os.path.abspath(__file__)); N=os.path.basename(HERE).split('-')[1]
ROOT=os.path.abspath(os.path.join(HERE,'..','..'))
META=json.load(open(os.path.join(HERE,'meta.json')))
LIST={a['slug']:a for a in json.load(open(os.path.join(ROOT,'article-list.json')))['articles']}
F=json.load(open(os.path.join(ROOT,'facts.json'))); KEYS={r['fact_key'] for k,v in F.items() if not k.startswith('_') for r in v.values()}
FOLDER='baliforamericans'; arts=[]; bad=0
def text(h): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',re.sub(r'<!--.*?-->',' ',h,flags=re.S)))).strip()
for m in META:
    slug=m['slug']; h=open(os.path.join(HERE,'src',slug+'.html')).read().strip(); a=LIST[slug]
    words=len(text(h).split()); issues=[]
    if not 1000<=words<=1250: issues.append(f'{words} words')
    for hm in re.finditer(r'<h2>(.*?)</h2>\s*(<p>.*?</p>|<ul>.*?</ul>)',h,flags=re.S):
        if hm.group(1)=='FAQ': continue
        t=text(hm.group(2)); n=len(t.split())
        if not 40<=n<=80: issues.append(f'answer-first {n}w under "{hm.group(1)[:30]}"')
        if re.match(r'(It|This|That|These|Those|They|Here|As mentioned)\b',t): issues.append(f'pronoun opener under "{hm.group(1)[:30]}"')
    for k in re.findall(r'data-fact="([^"]+)"',h):
        if k not in KEYS: issues.append('unknown fact key '+k)
    g=len(re.findall(r'class="guide"',h)); want={'turn':(1,2),'seed':(1,1),'none':(0,0)}[a['handoff']]
    if not want[0]<=g<=want[1]: issues.append(f'guide spans {g} for handoff {a["handoff"]}')
    slots=re.findall(r'<!-- IMAGE_SLOT_(\d+): (.*?) -->',h)
    ids=[f'{FOLDER}/articles/{slug}-hero']+[f'{FOLDER}/articles/{slug}-{n}' for n,_ in slots]
    arts.append({'slug':slug,'title':a['title'],'category_slug':a['category_slug'],'excerpt':m['excerpt'],'featured_image':ids[0],'content':h,'image_ids':ids})
    print(('OK  ' if not issues else 'FAIL'),slug,words,'words | facts',len(re.findall('data-fact',h)),'| guide',g,'| slots',len(slots),'|',issues); bad+=bool(issues)
json.dump({'schema_version':3,'articles':arts},open(os.path.join(HERE,f'import-batch-{N}.json'),'w'),indent=1,ensure_ascii=False)
sys.exit(1 if bad else 0)
