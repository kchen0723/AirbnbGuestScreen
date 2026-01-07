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
        "--hide-crash-restore-bubble",
        "--restore-last-session=false",      # 不恢复上次会话
        "--disable-session-crashed-bubble",  # 禁用崩溃后的气泡提示
        "--disable-session-crashed-bubble", 
        "--hide-crash-restore-bubble", 
        "--disable-features=SessionRestore,ForceSessionRestore",
    ]
    playwright = sync_playwright().start()
    context = playwright.chromium.launch_persistent_context(
        user_data_dir="./airbnb_profile",
        channel="msedge",
        headless=False,
        no_viewport=True,
        args=chrome_args,
        locale="en-CA",
        timezone_id="America/Vancouver",
        slow_mo=50,
    )
    time.sleep(3)
    last_page = context.new_page()
    time.sleep(1)
    pages = context.pages
    for item in list(pages):
        if item != last_page:
            try:
                item.close()
            except:
                pass

    last_page.goto("https://www.airbnb.ca")
    humain_wait()
        
    return playwright, context, last_page

def find_candidate(page, name=""):
   page.get_by_role("link", name="Switch to hosting").click()
   humain_wait()
   page.get_by_role("link", name="Messages").click()
   humain_wait()

   inbox = page.get_by_role("group", name="List of Conversations")
   humain_wait()
   inbox.locator('div[data-listrow="true"]').first.wait_for()
   messages = inbox.locator('div[data-listrow="true"]').all()
   humain_wait()
   print(f"in total we have {len(messages)} messages")
   # for message in messages:
   #    humain_wait()
   #    summary = message.locator("a span").first.inner_text()
   #    print(summary)
   
   name = name.lower()
   is_found = False
   for message in messages:
      humain_wait()
      summary = message.locator("a span").first.inner_text().lower()
      print(summary)
      if(summary.find(name) != -1):
          print(f"finding the person {name} message")
          message.click()
          humain_wait()
          is_found = True
          break
   return is_found

def find_home_details(page):
   detail_section=page.get_by_test_id("orbital-panel-details")
   humain_wait()
   detail_section.wait_for(state="visible")
   humain_wait()
   guest_section = detail_section.get_by_test_id("hrd-sbui-about-guest-section")
   humain_wait()
   name = guest_section.locator("h3").inner_text()
   humain_wait()
   print(name)
   details = guest_section.locator("span.tffussy").all_inner_texts()
   humain_wait()
   print(details)
   return name, details

def find_reviews(page):
   with page.expect_popup() as review_page_popup:
        page.get_by_role("link", name="Show profile").click()
   humain_wait()
   review_page = review_page_popup.value
   humain_wait()
   show_all_button = review_page.get_by_role("button").get_by_text("Show", exact=False)
   humain_wait()
   while show_all_button.count() > 0:
      show_all_button.click()
      humain_wait()
      show_all_button = review_page.get_by_role("button").get_by_text("Show", exact=False)
      humain_wait()
   humain_wait()

   review_tabs = review_page.locator("#user-profile-review-tabs")
   humain_wait()
   review_groups = review_tabs.get_by_role("group").all()
   humain_wait()
   review_data = []
   for group in review_groups:
       content = group.locator('div[id^="review-"] > div').first.inner_text()
      #  humain_wait()
       review_data.append(content)
   print(review_data)
   review_page.close()
   humain_wait()
   return review_data

def main():
    pw, context, page = open_airbnb()
    try:
        is_found = find_candidate(page, "Amir")
        if is_found:
            name, details = find_home_details(page)
            review_data = find_reviews(page)
            print("now we can call ai")
    finally:
        if context:
            context.close()
            time.sleep(2)

        if pw:
            pw.stop()

if __name__ == "__main__":
    main()