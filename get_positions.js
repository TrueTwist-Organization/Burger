const puppeteer = require('puppeteer');
(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto('http://localhost:8000');
    await new Promise(r => setTimeout(r, 2000));
    const pos = await page.evaluate(() => {
        const l1 = document.getElementById('layer-1').getBoundingClientRect();
        const l8 = document.getElementById('layer-8').getBoundingClientRect();
        return { l1: {y: l1.y, height: l1.height}, l8: {y: l8.y, height: l8.height} };
    });
    console.log("POSITIONS:", JSON.stringify(pos));
    await browser.close();
})();
