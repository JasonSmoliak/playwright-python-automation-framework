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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)
        if page:
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)

