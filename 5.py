import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.airbnb.ca/")
    page.get_by_test_id("cypress-headernav-profile").click()
    page.get_by_role("link", name="Log in or sign up").click()
    page.get_by_test_id("social-auth-button-email").click()
    page.get_by_test_id("email-login-email").fill("nga96@163.com")
    page.get_by_test_id("signup-login-submit-btn").click()
    page.get_by_test_id("email-signup-password").click()
    # page.get_by_test_id("email-signup-password").fill("")
    page.get_by_test_id("signup-login-submit-btn").click()
    page.get_by_role("button", name="Email").click()
    page.get_by_role("textbox", name="Enter digit 1 of the code you").click()
    page.get_by_role("textbox", name="Enter digit 1 of the code you").fill("9")
    page.get_by_role("textbox", name="Enter digit 2 of the code you").fill("7")
    page.get_by_role("textbox", name="Enter digit 3 of the code you").fill("2")
    page.get_by_role("textbox", name="Enter digit 4 of the code you").fill("2")
    page.get_by_role("textbox", name="Enter digit 5 of the code you").fill("5")
    page.get_by_role("textbox", name="Enter digit 6 of the code you").fill("5")
    page.get_by_role("link", name="Switch to hosting").click()
    page.get_by_role("button", name="Accept all").click()
    page.get_by_role("link", name="Messages").click()
    page.get_by_role("link", name="Calendar").click()
    page.get_by_role("button", name="Angus$1,044.07 Currently").click()
    page.get_by_role("link", name="View full itinerary").click()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Show profile").click()
    page1 = page1_info.value
    page1.get_by_role("button", name="Show all 3 reviews").click()
    page1.get_by_role("tabpanel", name="From Hosts ,").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
