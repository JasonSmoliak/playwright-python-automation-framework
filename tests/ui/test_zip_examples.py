import pytest

from utils.zip_examples import (
    compare_test_results,
    pair_users_and_roles,
)

pytestmark = pytest.mark.ui


def test_zip_examples():

    expected = [
        "PASSED",
        "FAILED",
        "PASSED",
    ]

    actual = [
        "PASSED",
        "FAILED",
        "FAILED",
    ]

    comparisons = compare_test_results(
        expected,
        actual,
    )

    users = [
        "jay",
        "sarah",
        "mike",
    ]

    roles = [
        "admin",
        "viewer",
        "editor",
    ]

    paired = pair_users_and_roles(
        users,
        roles,
    )

    print(comparisons)
    print(paired)

    assert comparisons == [
        True,
        True,
        False,
    ]

    assert paired == [
        "jay -> admin",
        "sarah -> viewer",
        "mike -> editor",
    ]
