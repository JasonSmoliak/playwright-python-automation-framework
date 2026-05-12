import pytest

from utils.enumerate_examples import (
    find_failed_tests,
    format_test_steps,
)

pytestmark = pytest.mark.ui


def test_enumerate_examples():

    steps = [
        "Open login page",
        "Enter credentials",
        "Click login button",
    ]

    formatted_steps = format_test_steps(steps)

    results = [
        "PASSED",
        "FAILED",
        "PASSED",
        "FAILED",
    ]

    failed_indexes = find_failed_tests(results)

    print(formatted_steps)
    print(failed_indexes)

    assert formatted_steps == [
        "Step 1: Open login page",
        "Step 2: Enter credentials",
        "Step 3: Click login button",
    ]

    assert failed_indexes == [2, 4]
