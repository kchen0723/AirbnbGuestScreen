from playwright.sync_api import sync_playwright
import time

# this solution works for some websites. but not for airbnb
def manually_create_profile():
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir="./airbnb_profile",
            channel="msedge",
            headless=False,
            # args=[
            #     "--disable_blink_features=AutomationControlled"
            # ]
        )
        page = context.pages[0]
        page.goto("https://www.airbnb.ca")

        input("now it would auto login")
        context.close()
        time.sleep(2)
        print("done")


manually_create_profile()