import pytest

from utils.args_kwargs_examples import (
    create_test_user,
    log_test_steps,
)

pytestmark = pytest.mark.ui


def test_args_and_kwargs():

    log_test_steps(
        "Open login page",
        "Enter credentials",
        "Click login button",
    )

    user = create_test_user(
        username="qa_user",
        role="admin",
        active=True,
    )

    print(user)

    assert user["username"] == "qa_user"

    assert user["active"] is True
