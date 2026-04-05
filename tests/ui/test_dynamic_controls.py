from pages.dynamic_controls_page import DynamicControlsPage


def test_remove_and_add_checkbox(page):
    dynamic_page = DynamicControlsPage(page)

    dynamic_page.load()
    dynamic_page.verify_checkbox_is_visible()

    dynamic_page.remove_checkbox()
    dynamic_page.verify_message_contains("It's gone!")
    dynamic_page.verify_checkbox_is_hidden()

    dynamic_page.add_checkbox()
    dynamic_page.verify_message_contains("It's back!")
    dynamic_page.verify_checkbox_is_visible()


def test_enable_input_field(page):
    dynamic_page = DynamicControlsPage(page)

    dynamic_page.load()
    dynamic_page.verify_input_is_disabled()

    dynamic_page.enable_input()
    dynamic_page.verify_message_contains("It's enabled!")
    dynamic_page.verify_input_is_enabled()
