import random
import time
from playwright.sync_api import sync_playwright

def humain_wait(min=1000, max=4000):
    random_time = random.randint(min, max)
    time.sleep(random_time / 1000)

def open_airbnb():
    chrome_args = [
        "--start-maximized",
        "--disable-extensions",
        "--disable_blink_features=AutomationControlled"
    ]
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir="./airbnb_profile",
            channel="chrome",
            headless=False,
            no_viewport=True,
            args=chrome_args,
            locale="en-CA",
            timezone_id="America/Vancouver",
            slow_mo=50,
        )
        page = context.pages[0]
        page.goto("https://www.airbnb.ca", wait_until="domcontentloaded")
        humain_wait()
        
    return page

if __name__ == "__main__":
    open_airbnb()