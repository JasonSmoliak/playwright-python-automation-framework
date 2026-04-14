import json
from pathlib import Path

def test_api_setup_then_ui_validation(browser, api_ui_state_file):
    context = browser.new_context(storage_state=str(api_ui_state_file))
    page = context.new_page()

    page.goto("https://example.com")

    auth_token = page.evaluate("() => localStorage.getItem('auth_token')")
    feature_flag = page.evaluate("() => localStorage.getItem('feature_flag')")
    user_name = page.evaluate("() => localStorage.getItem('user_name')")

    assert auth_token == "api-created-token-456"
    assert feature_flag == "enabled"
    assert user_name == "Jay"

    context.close()
