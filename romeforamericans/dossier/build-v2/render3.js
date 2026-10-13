// render3.js — dossier3.html -> dossier.pdf
// Furniture via Chromium header/footer template. Paper background painted by the template
// with an explicit font-size (Chromium clips 0-size templates) and full-bleed fill div.
// @page:first margin:0 keeps the cover full-bleed; interior @page margins (0.95/0.92in)
// are the strip the template paints into. printBackground + color-adjust:exact make the fill print.
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  // Portable: the build directory is this script's own, not the container's.
  const BUILD = __dirname;
  const htmlPath = 'file://' + path.join(BUILD, 'dossier3.html');
  const outPath = path.join(BUILD, 'dossier.pdf');

  const browser = await chromium.launch({
    // executablePath omitted: let playwright resolve its own chromium
    args: ['--no-sandbox','--disable-setuid-sandbox','--font-render-hinting=none']
  });
  const page = await browser.newPage({ deviceScaleFactor: 2 });
  await page.setViewportSize({ width: 816, height: 1056 });
  await page.goto(htmlPath, { waitUntil: 'networkidle', timeout: 120000 });
  await page.evaluate(async () => { if (document.fonts && document.fonts.ready) await document.fonts.ready; });
  await page.waitForTimeout(2800);

  // Chromium clips the template unless font-size is set on the root template div.
  // The absolutely-positioned fill paints the whole margin strip paper; the text sits inside it.
  const headerTpl = `<div style="font-size:8px;width:100%;height:100%;margin:0;padding:0;position:relative;-webkit-print-color-adjust:exact;">
     <div style="position:absolute;top:-40px;left:-40px;right:-40px;bottom:-6px;background:#F6EEDB;"></div>
     <div style="position:absolute;left:82px;right:82px;top:36px;
        font-family:'Courier New',monospace;font-size:8px;letter-spacing:1.4px;
        color:#7A6B4E;text-transform:uppercase;display:flex;justify-content:space-between;">
        <span>Rome, Solved.</span><span>La Tavola &#183; A Decision Manual</span></div>
     </div>`;
  const footerTpl = `<div style="font-size:8px;width:100%;height:100%;margin:0;padding:0;position:relative;-webkit-print-color-adjust:exact;">
     <div style="position:absolute;top:-6px;left:-40px;right:-40px;bottom:-40px;background:#F6EEDB;"></div>
     <div style="position:absolute;left:82px;right:82px;bottom:34px;
        font-family:'Courier New',monospace;font-size:8px;color:#7A6B4E;
        display:flex;justify-content:space-between;align-items:center;">
        <span>Rome for Americans</span>
        <span style="color:#C9A84C;">&#9670;</span>
        <span class="pageNumber"></span></div>
     </div>`;

  await page.pdf({
    path: outPath,
    width: '8.5in',
    height: '11in',
    printBackground: true,
    preferCSSPageSize: true,
    displayHeaderFooter: true,
    headerTemplate: headerTpl,
    footerTemplate: footerTpl,
    margin: { top: '1.02in', bottom: '1.0in', left: '0in', right: '0in' }
  });

  await browser.close();
  console.log('PDF written:', outPath);
})().catch(e => { console.error(e); process.exit(1); });
