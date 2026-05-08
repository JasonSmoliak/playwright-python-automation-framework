import pytest

from playwright.async_api import async_playwright

pytestmark = pytest.mark.ui


@pytest.mark.asyncio
async def test_async_playwright_example():
    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=False)

        page = await browser.new_page()

        await page.goto("https://example.com")

        title = await page.title()

        assert title == "Example Domain"

        await browser.close()
