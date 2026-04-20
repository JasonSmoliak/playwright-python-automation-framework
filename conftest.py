import json
import os
from datetime import datetime
from pathlib import Path

import allure
import pytest

from config import get_current_env


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)
        if page:
            os.makedirs("screenshots", exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshots/{item.name}_{timestamp}.png"

            screenshot_bytes = page.screenshot(path=filename, full_page=True)

            allure.attach(
                screenshot_bytes,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG,
            )


@pytest.fixture(scope="session")
def env_config():
    return get_current_env()


@pytest.fixture(scope="session")
def app_url(env_config):
    return env_config["base_url"]


@pytest.fixture(scope="session")
def credentials(env_config):
    return {
        "username": env_config["username"],
        "password": env_config["password"],
    }


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
                    {"name": "user_role", "value": "qa_tester"},
                ],
            }
        ],
    }

    with open(state_file, "w") as f:
        json.dump(state, f, indent=2)

    return state_file


@pytest.fixture(scope="function")
def api_ui_state_file():
    auth_dir = Path(".auth")
    auth_dir.mkdir(exist_ok=True)

    state_file = auth_dir / "api_ui_state.json"

    state = {
        "cookies": [],
        "origins": [
            {
                "origin": "https://example.com",
                "localStorage": [
                    {"name": "auth_token", "value": "api-created-token-456"},
                    {"name": "feature_flag", "value": "enabled"},
                    {"name": "user_name", "value": "Jay"},
                ],
            }
        ],
    }

    with open(state_file, "w") as f:
        json.dump(state, f, indent=2)

    return state_file
