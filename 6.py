import asyncio
from playwright.async_api import async_playwright
from playwright_stealth import Stealth

async def main():
    async with Stealth().use_async(async_playwright()) as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://bot.sannysoft.com/")
        await page.screenshot(path="stealth.png")

asyncio.run(main())
