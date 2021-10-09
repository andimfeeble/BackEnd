from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.webkit.launch(headless=False)
    page = browser.new_page()
    page.goto("http://playwright.dev")
    print(page.title())
    browser.close()