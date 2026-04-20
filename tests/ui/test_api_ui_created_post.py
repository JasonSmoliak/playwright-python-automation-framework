import json
from pathlib import Path
import pytest
from playwright.sync_api import expect
from pages.post_details_page import PostDetailsPage


def load_post_test_data():
    data_file = Path("test_data/posts.json")
    with open(data_file, "r") as f:
        return json.load(f)


test_data = load_post_test_data()


@pytest.mark.parametrize(
    "payload",
    test_data,
    ids=[item["title"] for item in test_data]
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
