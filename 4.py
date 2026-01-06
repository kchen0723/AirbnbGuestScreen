from playwright.sync_api import sync_playwright

# this solution works for some websites. but not for airbnb
def manually_create_profile():
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir="./airbnb_profile",
            channel="chrome",
            headless=False,
            # args=[
            #     "--disable_blink_features=AutomationControlled"
            # ]
        )
        page = context.pages[0]
        page.goto("https://www.airbnb.ca")

        input("now it would auto login")
        context.close()

manually_create_profile()