import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.api


def test_create_post_using_payload_factory(api_context, post_payload_factory):
    payload = post_payload_factory(
        title="Factory Created Post",
        body="This payload was created by a pytest factory fixture",
        user_id=777,
    )

    response = api_context.post("/posts", data=payload)

    expect(response).to_be_ok()

    body = response.json()

    assert body["title"] == "Factory Created Post"
    assert body["body"] == "This payload was created by a pytest factory fixture"
    assert body["userId"] == 777
