import pytest

from utils.defaultdict_examples import (
    group_test_results,
    group_users_by_role,
)

pytestmark = pytest.mark.ui


def test_defaultdict_examples():

    users = [
        {"username": "jay", "role": "admin"},
        {"username": "sarah", "role": "viewer"},
        {"username": "mike", "role": "admin"},
    ]

    grouped_users = group_users_by_role(
        users
    )

    results = [
        ("test_login", "PASSED"),
        ("test_api", "FAILED"),
        ("test_search", "PASSED"),
    ]

    grouped_results = group_test_results(
        results
    )

    print(grouped_users)
    print(grouped_results)

    assert grouped_users["admin"] == [
        "jay",
        "mike",
    ]

    assert grouped_results["PASSED"] == [
        "test_login",
        "test_search",
    ]
