import pytest

from utils.filter_examples import (
    get_active_users,
    get_failed_tests,
)

pytestmark = pytest.mark.ui


def test_filter_examples():

    results = [
        "PASSED",
        "FAILED",
        "PASSED",
        "FAILED",
    ]

    failed = get_failed_tests(results)

    users = [
        {"username": "jay", "active": True},
        {"username": "sarah", "active": False},
        {"username": "mike", "active": True},
    ]

    active_users = get_active_users(users)

    print(failed)
    print(active_users)

    assert failed == [
        "FAILED",
        "FAILED",
    ]

    assert active_users == [
        {"username": "jay", "active": True},
        {"username": "mike", "active": True},
    ]
