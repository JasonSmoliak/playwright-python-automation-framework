import pytest

from utils.type_hint_examples import (
    create_test_user,
    get_supported_browsers,
)

pytestmark = pytest.mark.ui


def test_type_hints_example():

    user = create_test_user(
        username="qa_user",
        role="admin",
    )

    browsers = get_supported_browsers()

    print(user)
    print(browsers)

    assert user["username"] == "qa_user"

    assert "chromium" in browsers
