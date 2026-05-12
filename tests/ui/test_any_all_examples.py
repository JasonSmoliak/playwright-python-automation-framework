import pytest

from utils.any_all_examples import (
    all_tests_passed,
    any_test_failed,
)

pytestmark = pytest.mark.ui


def test_any_all_examples():

    passing_results = [
        "PASSED",
        "PASSED",
        "PASSED",
    ]

    mixed_results = [
        "PASSED",
        "FAILED",
        "PASSED",
    ]

    all_passed = all_tests_passed(
        passing_results
    )

    any_failed = any_test_failed(
        mixed_results
    )

    print(all_passed)
    print(any_failed)

    assert all_passed is True

    assert any_failed is True
