from playwright.sync_api import Page, Locator, expect


class DataTablesPage:
    def __init__(self, page: Page):
        self.page = page
        self.heading = page.get_by_role("heading", name="Data Tables")
        self.table1 = page.locator("table").nth(0)
        self.table2 = page.locator("table").nth(1)

    def load(self):
        self.page.goto(
            "https://practice.expandtesting.com/tables",
            wait_until="domcontentloaded"
        )
        expect(self.heading).to_be_visible()

    def get_row_by_last_name(self, last_name: str) -> Locator:
        return self.table1.locator("tbody tr").filter(has_text=last_name)

    def verify_row_contains_text(self, last_name: str, expected_text: str):
        row = self.get_row_by_last_name(last_name)
        expect(row).to_contain_text(expected_text)

    def verify_email_for_last_name(self, last_name: str, email: str):
        row = self.get_row_by_last_name(last_name)
        expect(row).to_contain_text(email)

    def verify_due_for_last_name(self, last_name: str, due_amount: str):
        row = self.get_row_by_last_name(last_name)
        expect(row).to_contain_text(due_amount)

    def verify_action_link_present(self, last_name: str, link_name: str):
        row = self.get_row_by_last_name(last_name)
        expect(row.get_by_role("link", name=link_name)).to_be_visible()
