from pages.dynamic_table_page import DynamicTablePage


def test_chrome_cpu_matches_label(page):
    dynamic_table_page = DynamicTablePage(page)

    dynamic_table_page.load()
    dynamic_table_page.verify_chrome_cpu_matches_label()
