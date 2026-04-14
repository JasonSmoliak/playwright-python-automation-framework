from playwright.sync_api import expect
from pages.post_details_page import PostDetailsPage


def test_create_post_via_api_then_verify_in_ui(page, api_context):
    payload = {
        "title": "Playwright Combined Test",
        "body": "Created through API and verified in UI",
        "userId": 101,
    }

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
        title="Playwright Combined Test",
        body="Created through API and verified in UI",
        user_id=101,
    )
