import pytest

from models.post_payload import PostPayload

pytestmark = pytest.mark.api


def test_post_payload_dataclass():

    payload = PostPayload(
        title="Playwright Dataclass Test",
        body="Learning Python dataclasses",
        user_id=1,
    )

    print(payload)

    assert payload.title == "Playwright Dataclass Test"
    assert payload.user_id == 1
