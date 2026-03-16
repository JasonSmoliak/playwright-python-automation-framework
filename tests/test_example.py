from pages.example_page import ExamplePage


def test_example(page, app_url):
    example_page = ExamplePage(page, app_url)

    example_page.load()
    example_page.click_learn_more()
    example_page.verify_destination_page()

