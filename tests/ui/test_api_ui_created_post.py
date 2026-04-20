import pytest
from playwright.sync_api import expect
from pages.post_details_page import PostDetailsPage


@pytest.mark.parametrize(
    "payload",
    [
        {
            "title": "Playwright Combined Test",
            "body": "Created through API and verified in UI",
            "userId": 101,
        },
        {
            "title": "Second API UI Test",
            "body": "Another record flowing from API to UI",
            "userId": 202,
        },
        {
            "title": "Third Combined Scenario",
            "body": "Parameterized test data example",
            "userId": 303,
        },
    ],
)
def test_create_post_via_api_then_verify_in_ui(page, api_context, payload):
    response = api_context.post("/posts", data=payload)
    expect(response).to_be_ok()

    created_post = response.json()

    post_details_page = PostDetailsPage(page)
    post_details_page.load_post_content(
        title=created_post["title"],
        body=created_post["body"],
        user_id=created_post["userId"],
    )
    post_details_page.verify_post_details(
        title=payload["title"],
        body=payload["body"],
        user_id=payload["userId"],
    )
