import json
from pathlib import Path
import pytest


@pytest.fixture(scope="session")
def app_url():
    return "https://example.com"

@pytest.fixture
def api_context(playwright):
    context = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )
    yield context
    context.dispose()

@pytest.fixture(scope="session")
def auth_state_file():
    auth_dir = Path(".auth")
    auth_dir.mkdir(exist_ok=True)

    state_file = auth_dir / "state.json"

    state = {
        "cookies": [],
        "origins": [
            {
                "origin": "https://example.com",
                "localStorage": [
                    {"name": "auth_token", "value": "mock-token-123"},
                    {"name": "user_role", "value": "qa_tester"}
                ]
            }
        ]
    }

    with open(state_file, "w") as f:
        json.dump(state, f, indent=2)

    return state_file

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)
        if page:
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)

