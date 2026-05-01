import pytest
import allure
from playwright.sync_api import expect

@pytest.mark.api
@pytest.mark.smoke
def test_get_post(api_context):
    response = api_context.get("/posts/1")

    expect(response).to_be_ok()

    body = response.json()
    assert body["id"] == 1
    assert "title" in body


@pytest.mark.api
@pytest.mark.regression
def test_create_post(api_context):
    payload = {
        "title": "Playwright API test",
        "body": "Learning API automation with Python",
        "userId": 1
    }

    response = api_context.post("/posts", data=payload)

    expect(response).to_be_ok()

    body = response.json()
    assert body["title"] == "Playwright API test"
    assert body["body"] == "Learning API automation with Python"
    assert body["userId"] == 1

def test_api_then_ui(page, api_context):
    # Step 1: API call (setup)
    response = api_context.get("/posts/1")
    assert response.ok

    # Step 2: UI validation
    page.goto("https://jsonplaceholder.typicode.com/posts/1")

    content = page.locator("body").inner_text()
    assert "id" in content
