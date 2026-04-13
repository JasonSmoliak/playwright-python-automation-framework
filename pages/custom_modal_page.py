from playwright.sync_api import Page, expect


class CustomModalPage:
    def __init__(self, page: Page):
        self.page = page
        self.open_modal_button = page.get_by_role("button", name="Click for JS Confirm")
        self.modal = page.locator(".modal, [role='dialog']")
        self.modal_title = self.modal.locator("h1, h2, h3, .modal-title")
        self.modal_body = self.modal.locator(".modal-body, .modal-content, p")
        self.close_button = self.modal.get_by_role("button", name="Close")

    def load(self):
        self.page.goto(
            "https://practice.expandtesting.com/js-dialogs",
            wait_until="domcontentloaded"
        )

    def open_modal(self):
        self.open_modal_button.click()

    def verify_modal_visible(self):
        expect(self.modal).to_be_visible()

    def verify_modal_title_contains(self, text: str):
        expect(self.modal_title).to_contain_text(text)

    def verify_modal_body_visible(self):
        expect(self.modal_body).to_be_visible()

    def close_modal(self):
        self.close_button.click()

    def verify_modal_hidden(self):
        expect(self.modal).not_to_be_visible()
