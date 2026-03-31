from pathlib import Path


def test_load_mock_auth_state(browser, auth_state_file):
    context = browser.new_context(storage_state=str(auth_state_file))
    page = context.new_page()

    page.goto("https://example.com")
    token = page.evaluate("() => localStorage.getItem('auth_token')")
    role = page.evaluate("() => localStorage.getItem('user_role')")

    assert token == "mock-token-123"
    assert role == "qa_tester"

    context.close()
