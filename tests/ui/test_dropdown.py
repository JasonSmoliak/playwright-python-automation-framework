from pages.dropdown_page import DropdownPage


def test_select_simple_dropdown_option(page):
    dropdown_page = DropdownPage(page)

    dropdown_page.load()
    dropdown_page.select_simple_option_by_label("Option 1")
    dropdown_page.verify_simple_option_selected("1")


def test_select_elements_per_page(page):
    dropdown_page = DropdownPage(page)

    dropdown_page.load()
    dropdown_page.select_elements_per_page("50")
    dropdown_page.verify_elements_per_page_selected("50")


def test_select_country(page):
    dropdown_page = DropdownPage(page)

    dropdown_page.load()
    dropdown_page.select_country_by_label("Canada")
    dropdown_page.verify_country_selected("CA")
