from playwright.sync_api import sync_playwright

# this solution works for some websites. but not for airbnb
def manually_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = browser.new_page()
        page.goto("https://www.airbnb.com")

        input("please manually login, hit return to continue")
        context.storage_state(path="airbnb.json")
        browser.close()

manually_login()