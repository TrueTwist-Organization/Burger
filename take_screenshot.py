from playwright.sync_api import sync_playwright
import time

def take_screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})
        page.goto("file:///Users/jinal/Downloads/Food/index.html")
        # Scroll down to trigger the exploded view
        page.evaluate("window.scrollTo(0, document.body.scrollHeight / 2)")
        time.sleep(2)  # wait for GSAP animation
        page.screenshot(path="burger_test.png")
        browser.close()

if __name__ == '__main__':
    take_screenshot()
