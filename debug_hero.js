const puppeteer = require('puppeteer');
(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.setViewport({ width: 1920, height: 1080 });
    await page.goto('http://localhost:8000');
    await new Promise(r => setTimeout(r, 2000));
    
    const data = await page.evaluate(() => {
        const burger = document.getElementById('burger-container');
        const bRect = burger.getBoundingClientRect();
        
        const l1 = document.getElementById('layer-1');
        const l1Rect = l1.getBoundingClientRect();
        
        const label = document.getElementById('label-l1');
        const labelRect = label.getBoundingClientRect();
        const labelStyle = window.getComputedStyle(label);
        
        return {
            burger: { y: bRect.y, height: bRect.height, scale: window.getComputedStyle(burger).transform },
            l1: { y: l1Rect.y, transform: window.getComputedStyle(l1).transform },
            label: { y: labelRect.y, opacity: labelStyle.opacity, display: labelStyle.display }
        };
    });
    console.log("DEBUG DATA:", JSON.stringify(data, null, 2));
    await browser.close();
})();
