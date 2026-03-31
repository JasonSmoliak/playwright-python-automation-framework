import re
from playwright.sync_api import Page, expect


class ExamplePage:
    def __init__(self, page: Page):
        self.page = page
        self.learn_more_link = page.get_by_role("link", name="Learn more")

    def load(self):
        self.page.goto("https://example.com")

    def click_learn_more(self):
        self.learn_more_link.click()

    def verify_destination_page(self):
        expect(self.page).to_have_url(re.compile(r".*/help/example-domains$"))
