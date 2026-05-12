import pytest

from utils.sorting_examples import (
    sort_usernames,
    sort_users_by_age,
)

pytestmark = pytest.mark.ui


def test_sorting_examples():

    usernames = [
        "mike",
        "jay",
        "sarah",
    ]

    sorted_names = sort_usernames(usernames)

    users = [
        {"username": "jay", "age": 42},
        {"username": "sarah", "age": 31},
        {"username": "mike", "age": 50},
    ]

    sorted_users = sort_users_by_age(users)

    print(sorted_names)
    print(sorted_users)

    assert sorted_names == [
        "jay",
        "mike",
        "sarah",
    ]

    assert sorted_users[0]["username"] == "sarah"

    assert sorted_users[-1]["username"] == "mike"
