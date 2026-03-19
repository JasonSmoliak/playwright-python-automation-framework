import re
from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.get_by_role("button", name="Login")
        self.logout_button = page.get_by_role("link", name="Logout")
        self.flash_message = page.locator("#flash")

    def load(self):
        self.page.goto(
            "https://practice.expandtesting.com/login",
            wait_until="domcontentloaded"
        )

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def verify_successful_login(self):
        expect(self.page).to_have_url(re.compile(r".*/secure$"))
        expect(self.flash_message).to_contain_text("You logged into a secure area!")
        expect(self.logout_button).to_be_visible()

    def verify_failed_login(self):
        expect(self.flash_message).to_contain_text("Your username is invalid!")

