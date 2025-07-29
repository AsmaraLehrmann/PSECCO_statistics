import os
import csv
import datetime
import asyncio
from playwright.async_api import async_playwright

async def get_follower_count(handle):
    url = f"https://bsky.app/profile/{handle}"
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url, wait_until='networkidle')
        locator = page.locator("a:has(span:text('Followers')) span").nth(1)
        await locator.wait_for()
        count = await locator.inner_text()
        await browser.close()
        return count

async def main():
    handle = "polarsecco.bsky.social"
    count = await get_follower_count(handle)
    today = datetime.date.today().isoformat()

    os.makedirs("data", exist_ok=True)
    with open("data/bsky_followers.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([today, handle, count])
    print(f"{today}: {handle} has {count} followers")

if __name__ == "__main__":
    asyncio.run(main())
