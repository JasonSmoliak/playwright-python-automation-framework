import pytest

from utils.counter_examples import (
    count_browser_usage,
    count_test_results,
)

pytestmark = pytest.mark.ui


def test_counter_examples():

    results = [
        "PASSED",
        "FAILED",
        "PASSED",
        "SKIPPED",
        "FAILED",
        "PASSED",
    ]

    result_counts = count_test_results(
        results
    )

    browsers = [
        "chromium",
        "firefox",
        "chromium",
        "webkit",
        "chromium",
    ]

    browser_counts = count_browser_usage(
        browsers
    )

    print(result_counts)
    print(browser_counts)

    assert result_counts["PASSED"] == 3

    assert result_counts["FAILED"] == 2

    assert browser_counts["chromium"] == 3
