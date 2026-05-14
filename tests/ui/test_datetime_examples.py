import pytest

from utils.datetime_examples import (
    format_timestamp,
    generate_report_name,
    get_current_timestamp,
)

pytestmark = pytest.mark.ui


def test_datetime_examples():

    timestamp = get_current_timestamp()

    formatted = format_timestamp()

    report_name = generate_report_name()

    print(timestamp)
    print(formatted)
    print(report_name)

    assert isinstance(formatted, str)

    assert report_name.endswith(".html")

    assert "report_" in report_name
