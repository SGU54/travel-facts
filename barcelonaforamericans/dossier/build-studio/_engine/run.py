import pathlib, sys
from playwright.sync_api import sync_playwright
INJECT=("<script>window.PagedConfig={auto:false};</script><script src='../paged.polyfill.js'></script>"
 "<script>(function(){function go(){document.fonts.ready.then(function(){return Promise.all(Array.from(document.images).map(function(i){return i.decode().catch(function(){})}))})"
 ".then(function(){window.PagedPolyfill.preview().then(function(f){window.__pagedDone=f.total;}).catch(function(e){window.__pagedErr=String(e&&e.stack||e)});});}"
 "if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',go);}else{go();}})();</script>")
html=open('_engine/test.html').read().replace('</head>',INJECT+'</head>')
open('_engine/_test.html','w').write(html)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':900,'height':1100}, device_scale_factor=1.5)
    pg.goto(pathlib.Path('_engine/_test.html').resolve().as_uri())
    pg.wait_for_function('window.__pagedDone||window.__pagedErr', timeout=60000)
    err=pg.evaluate('window.__pagedErr'); print('err:',err); print('pages:',pg.evaluate('window.__pagedDone'))
    for i,el in enumerate(pg.query_selector_all('.pagedjs_page')):
        el.screenshot(path=f'_engine/page-{i+1}.png')
    # geometry report
    print(pg.evaluate("""()=>[...document.querySelectorAll('.pagedjs_page')].map((pg,i)=>{const r=pg.getBoundingClientRect();
      return 'P'+(i+1)+': '+[...pg.querySelectorAll('.mg, p, .bleed, .ticket')].map(e=>{const b=e.getBoundingClientRect();return e.className.split(' ')[0]+'@'+Math.round(b.top-r.top)+'-'+Math.round(b.bottom-r.top)+'x'+Math.round(b.left-r.left)}).join(' ')}).join('\\n')"""))
    print(pg.evaluate("""()=>{const e=document.querySelector('.bleed');let out=[];let n=e;while(n&&!n.classList.contains('pagedjs_page')){const cs=getComputedStyle(n);out.push((n.className||n.tagName)+' mt='+cs.marginTop+' pt='+cs.paddingTop+' top='+Math.round(n.getBoundingClientRect().top));n=n.parentElement;}return out.join(' | ')}"""))
    b.close()
