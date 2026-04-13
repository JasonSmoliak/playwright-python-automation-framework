from pages.data_tables_page import DataTablesPage


def test_verify_doe_row_data(page):
    tables_page = DataTablesPage(page)

    tables_page.load()
    tables_page.verify_row_contains_text("Doe", "Jason")
    tables_page.verify_email_for_last_name("Doe", "jdoe@hotmail.com")
    tables_page.verify_due_for_last_name("Doe", "$100.00")


def test_verify_smith_row_edit_link(page):
    tables_page = DataTablesPage(page)

    tables_page.load()
    tables_page.verify_action_link_present("Smith", "Edit")


def test_verify_bach_row_delete_link(page):
    tables_page = DataTablesPage(page)

    tables_page.load()
    tables_page.verify_action_link_present("Bach", "Delete")
