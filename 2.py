from playwright.sync_api import sync_playwright

def automatically_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="airbnb.json")
        page = browser.new_page()
        page.goto("https://www.airbnb.com")
        
        browser.close()

automatically_login()