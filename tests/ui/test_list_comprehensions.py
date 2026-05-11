import pytest

from utils.list_comprehension_examples import (
    generate_test_emails,
    get_active_users,
)

pytestmark = pytest.mark.ui


def test_list_comprehensions():

    users = [
        {"username": "jay", "active": True},
        {"username": "sarah", "active": False},
        {"username": "mike", "active": True},
    ]

    active_users = get_active_users(users)

    emails = generate_test_emails(3)

    print(active_users)
    print(emails)

    assert active_users == ["jay", "mike"]

    assert emails == [
        "qa_user_0@example.com",
        "qa_user_1@example.com",
        "qa_user_2@example.com",
    ]
