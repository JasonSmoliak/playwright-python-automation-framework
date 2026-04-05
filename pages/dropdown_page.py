from playwright.sync_api import Page, expect


class DropdownPage:
    def __init__(self, page: Page):
        self.page = page
        self.heading = page.get_by_role("heading", name="Dropdown List")
        self.simple_dropdown = page.locator("#dropdown")
        self.elements_per_page = page.locator("#elementsPerPageSelect")
        self.country_dropdown = page.locator("#country")

    def load(self):
        self.page.goto(
            "https://practice.expandtesting.com/dropdown",
            wait_until="domcontentloaded"
        )
        expect(self.heading).to_be_visible()

    def select_simple_option_by_label(self, label: str):
        self.simple_dropdown.select_option(label=label)

    def verify_simple_option_selected(self, value: str):
        expect(self.simple_dropdown).to_have_value(value)

    def select_elements_per_page(self, value: str):
        self.elements_per_page.select_option(value)

    def verify_elements_per_page_selected(self, value: str):
        expect(self.elements_per_page).to_have_value(value)

    def select_country_by_label(self, label: str):
        self.country_dropdown.select_option(label=label)

    def verify_country_selected(self, value: str):
        expect(self.country_dropdown).to_have_value(value)
