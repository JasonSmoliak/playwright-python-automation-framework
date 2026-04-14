import re
from playwright.sync_api import Page, expect


class DynamicTablePage:
    def __init__(self, page: Page):
        self.page = page
        self.heading = page.get_by_role("heading", name="Dynamic Table")
        self.table = page.get_by_role("table")
        self.chrome_cpu_label = page.locator("p.bg-warning")

    def load(self):
        self.page.goto(
            "https://practice.expandtesting.com/dynamic-table",
            wait_until="domcontentloaded"
        )
        expect(self.heading).to_be_visible()

    def get_cpu_value_for_process(self, process_name: str) -> str:
        headers = self.table.locator("thead th")
        header_count = headers.count()

        cpu_column_index = None
        for i in range(header_count):
            header_text = headers.nth(i).inner_text().strip()
            if header_text == "CPU":
                cpu_column_index = i
                break

        if cpu_column_index is None:
            raise ValueError("CPU column not found")

        rows = self.table.locator("tbody tr")
        row_count = rows.count()

        for i in range(row_count):
            row = rows.nth(i)
            if process_name in row.inner_text():
                cells = row.locator("td")
                return cells.nth(cpu_column_index).inner_text().strip()

        raise ValueError(f"Process '{process_name}' not found in table")

    def get_chrome_cpu_label_value(self) -> str:
        label_text = self.chrome_cpu_label.inner_text().strip()
        match = re.search(r"Chrome CPU:\s*([\d.]+%)", label_text)

        if not match:
            raise ValueError(f"Could not extract Chrome CPU value from label: {label_text}")

        return match.group(1)

    def verify_chrome_cpu_matches_label(self):
        table_cpu = self.get_cpu_value_for_process("Chrome")
        label_cpu = self.get_chrome_cpu_label_value()
        assert table_cpu == label_cpu, (
            f"Chrome CPU mismatch: table={table_cpu}, label={label_cpu}"
        )
