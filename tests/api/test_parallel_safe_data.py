import pytest

from utils.data_factory import unique_post_payload

pytestmark = pytest.mark.api


def test_create_unique_post(posts_client):
    payload = unique_post_payload()

    response = posts_client.create_post(payload)

    body = response.json()

    assert body["title"] == payload["title"]
    assert body["body"] == payload["body"]
