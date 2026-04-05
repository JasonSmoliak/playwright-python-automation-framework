from playwright.sync_api import Page, expect


class DynamicControlsPage:
    def __init__(self, page: Page):
        self.page = page
        self.heading = page.get_by_role("heading", name="Dynamic Controls")
        self.message = page.locator("#message")
        self.input_field = page.locator("#input-example input")

    def checkbox(self):
        return self.page.get_by_role("checkbox")

    def load(self):
        self.page.goto(
            "https://practice.expandtesting.com/dynamic-controls",
            wait_until="domcontentloaded"
        )
        expect(self.heading).to_be_visible()

    def remove_checkbox(self):
        self.page.get_by_role("button", name="Remove").click()

    def add_checkbox(self):
        self.page.get_by_role("button", name="Add").click()

    def enable_input(self):
        self.page.get_by_role("button", name="Enable").click()

    def disable_input(self):
        self.page.get_by_role("button", name="Disable").click()

    def verify_checkbox_is_visible(self):
        expect(self.checkbox()).to_be_visible()

    def verify_checkbox_is_hidden(self):
        expect(self.checkbox()).not_to_be_visible()

    def verify_input_is_disabled(self):
        expect(self.input_field).to_be_disabled()

    def verify_input_is_enabled(self):
        expect(self.input_field).to_be_enabled()

    def verify_message_contains(self, text: str):
        expect(self.message).to_be_visible()
        expect(self.message).to_contain_text(text)
