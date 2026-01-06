# first, use this command to run chrome with special user-data-dir.
# this solution does not work
# "C:\Program Files\Google\Chrome\Application\chrome.exe" --user-data-dir=C:\LocalGit\AirbnbGuestScreen\airbnb_profile

# 介绍一下playwright-stealth
# playwright codegen
import random
import time
# import playwright_stealth
from playwright.sync_api import sync_playwright

def human_type(page, id, content):
    page.click("#id")
    page.keyboard.type(content, delay=random.randint(100, 200))

def humain_wait(min=1000, max=4000):
    random_time = random.randint(min, max)
    time.sleep(random_time / 1000)

def humain_mouse_move_once(page, min=1000, max=4000):
    random_time = random.randint(min, max)
    viewport = page.viewport_size
    if viewport:
        x = random.randint(0, viewport["width"])
        y = random.randint(0, viewport["height"])
        page.mouse.move(x, y)
        time.sleep(random_time)
    

# this solution works for some websites. but not for airbnb
def use_special_prifile():
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir="./airbnb_profile",
            channel="chrome",
            headless=False,
            no_viewport=True,
            args=[
                "--start-maximized",
                "--disable-extensions",
                "--disable_blink_features=AutomationControlled"
            ],
            locale="en-CA",
            timezone_id="America/Vancouver",
            slow_mo=50,
        )
        page = context.pages[0]
        # playwright_stealth.Stealth(page)
        page.goto("https://www.airbnb.ca", wait_until="domcontentloaded")
        humain_wait()

        input("now it would auto login")
        context.close()

use_special_prifile()