from playwright.sync_api import Page, expect


class JsDialogsPage:
    def __init__(self, page: Page):
        self.page = page
        self.heading = page.get_by_role("heading", name="JavaScript Dialogs")
        self.js_alert_button = page.get_by_role("button", name="Js Alert")
        self.js_confirm_button = page.get_by_role("button", name="Js Confirm")
        self.js_prompt_button = page.get_by_role("button", name="Js Prompt")
        self.response_text = page.locator("#dialog-response")

    def load(self):
        self.page.goto(
            "https://practice.expandtesting.com/js-dialogs",
            wait_until="domcontentloaded"
        )
        expect(self.heading).to_be_visible()

    def trigger_alert(self):
        self.js_alert_button.click()

    def trigger_confirm(self):
        self.js_confirm_button.click()

    def trigger_prompt(self):
        self.js_prompt_button.click()

    def verify_response_contains(self, text: str):
        expect(self.response_text).to_contain_text(text)
