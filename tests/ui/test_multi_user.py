import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.ui


def test_two_users_independent_sessions(browser):
    context1 = browser.new_context()
    context2 = browser.new_context()

    page1 = context1.new_page()
    page2 = context2.new_page()

    page1.goto("https://example.com")
    page2.goto("https://example.com")

    page1.evaluate("""() => {
        localStorage.setItem("user", "UserA");
    }""")

    page2.evaluate("""() => {
        localStorage.setItem("user", "UserB");
    }""")

    user1 = page1.evaluate("localStorage.getItem('user')")
    user2 = page2.evaluate("localStorage.getItem('user')")

    assert user1 == "UserA"
    assert user2 == "UserB"

    context1.close()
    context2.close()
