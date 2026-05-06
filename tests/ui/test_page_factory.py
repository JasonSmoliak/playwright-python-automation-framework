import pytest

from pages.login_page import LoginPage
from pages.dropdown_page import DropdownPage

pytestmark = pytest.mark.ui


def test_page_factory_creates_login_page(page_factory, credentials):
    login_page = page_factory(LoginPage)

    login_page.load()
    login_page.login(credentials["username"], credentials["password"])
    login_page.verify_successful_login()


def test_page_factory_creates_dropdown_page(page_factory):
    dropdown_page = page_factory(DropdownPage)

    dropdown_page.load()
    dropdown_page.select_simple_option_by_label("Option 1")
    dropdown_page.verify_simple_option_selected("1")
