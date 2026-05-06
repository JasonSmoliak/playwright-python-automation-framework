import json
import os
from datetime import datetime
from pathlib import Path

import allure
import pytest

from env_config.config_loader import load_env_config
from pages.login_page import LoginPage
from pages.dynamic_table_page import DynamicTablePage
from pages.dropdown_page import DropdownPage
from pages.post_details_page import PostDetailsPage

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
    return load_env_config()

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

@pytest.fixture
def login_page(page, app_url):
    return LoginPage(page, app_url)


@pytest.fixture
def dynamic_table_page(page):
    return DynamicTablePage(page)


@pytest.fixture
def dropdown_page(page):
    return DropdownPage(page)


@pytest.fixture
def post_details_page(page):
    return PostDetailsPage(page)

@pytest.fixture
def post_payload_factory():
    def _create_post_payload(
        title="Default Post Title",
        body="Default post body created by factory",
        user_id=1,
    ):
        return {
            "title": title,
            "body": body,
            "userId": user_id,
        }

    return _create_post_payload

@pytest.fixture
def page_factory(page, app_url):
    def _create_page_object(page_class, *args, **kwargs):
        try:
            return page_class(page, app_url, *args, **kwargs)
        except TypeError:
            return page_class(page, *args, **kwargs)

    return _create_page_object

@pytest.fixture
def user_session_factory(browser):
    def _create_user_session(role="standard"):

        context = browser.new_context()
        page = context.new_page()

        if role == "admin":
            storage = {
                "role": "admin",
                "token": "admin-token-123",
            }

        elif role == "guest":
            storage = {
                "role": "guest",
                "token": "guest-token-456",
            }

        else:
            storage = {
                "role": "standard",
                "token": "standard-token-789",
            }

        page.goto("https://example.com")

        page.evaluate(
            """(storage) => {
                localStorage.setItem("user_role", storage.role);
                localStorage.setItem("auth_token", storage.token);
            }""",
            storage,
        )

        return {
            "context": context,
            "page": page,
            "role": storage["role"],
            "token": storage["token"],
        }

    return _create_user_session
