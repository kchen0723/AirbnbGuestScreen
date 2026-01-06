import random
import time
from playwright.sync_api import sync_playwright

def humain_wait(min=1000, max=4000):
    random_time = random.randint(min, max) / 1000
    print(f"waiting for {random_time} seconds")
    time.sleep(random_time)

def open_airbnb():
    chrome_args = [
        "--start-maximized",
        "--disable-extensions",
        "--disable_blink_features=AutomationControlled",
        "--restore-last-session=false",      # 不恢复上次会话
        "--disable-session-crashed-bubble",  # 禁用崩溃后的气泡提示
    ]
    playwright = sync_playwright().start()
    context = playwright.chromium.launch_persistent_context(
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
    page.goto("https://www.airbnb.ca")
    humain_wait()
        
    return playwright, context, page

def find_candidate(page, name=""):
    page.get_by_role("link", name="Switch to hosting").click()
    humain_wait()
    page.get_by_role("link", name="Messages").click()
    humain_wait()

def main():
    pw, context, page = open_airbnb()
    try:
        find_candidate(page)
    finally:
        context.close()
        pw.stop()

if __name__ == "__main__":
    main()