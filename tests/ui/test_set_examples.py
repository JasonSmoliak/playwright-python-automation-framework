import pytest

from utils.set_examples import (
    find_duplicate_values,
    get_unique_usernames,
)

pytestmark = pytest.mark.ui


def test_set_examples():

    usernames = [
        "jay",
        "sarah",
        "jay",
        "mike",
        "mike",
    ]

    unique_users = get_unique_usernames(usernames)

    duplicates = find_duplicate_values(usernames)

    print(unique_users)
    print(duplicates)

    assert unique_users == {
        "jay",
        "sarah",
        "mike",
    }

    assert duplicates == {
        "jay",
        "mike",
    }
