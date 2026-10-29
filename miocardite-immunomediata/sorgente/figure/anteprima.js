// Anteprima PNG di una figura SVG con i font del documento: node anteprima.js fig.svg out.png larghezza_mm
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const [svgPath, out, mm] = process.argv.slice(2);
  const svg = fs.readFileSync(svgPath, 'utf8');
  const base = path.resolve(__dirname, '..');
  const html = `<!doctype html><html><head><link rel="stylesheet" href="file://${base}/fonts.css"></head>
  <body style="margin:0;background:#fff"><div id="f" style="width:${mm || 180}mm">${svg}</div></body></html>`;
  const tmp = path.join(base, '_anteprime', 'figura.html');
  fs.mkdirSync(path.dirname(tmp), { recursive: true });
  fs.writeFileSync(tmp, html.replace(/file:\/\/[^"]*fonts\.css/, '../fonts.css'));
  const browser = await chromium.launch();
  const page = await browser.newPage({ deviceScaleFactor: 1.6 });
  await page.goto('file://' + tmp, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await (await page.$('#f')).screenshot({ path: out });
  await browser.close();
})();
