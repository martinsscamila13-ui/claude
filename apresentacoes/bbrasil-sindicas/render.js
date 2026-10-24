const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  await p.goto('file://' + process.argv[2], { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  if (process.argv[4]) {
    const n = await p.$$eval('section.s', s => s.length);
    const els = await p.$$('section.s');
    for (let i = 0; i < els.length; i++) await els[i].screenshot({ path: `${process.argv[4]}/p${String(i+1).padStart(2,'0')}.png` });
  }
  await p.pdf({ path: process.argv[3], width: '1920px', height: '1080px', printBackground: true, preferCSSPageSize: true });
  await b.close();
})();
