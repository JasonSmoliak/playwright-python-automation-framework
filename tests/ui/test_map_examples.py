import pytest

from utils.map_examples import (
    convert_prices_to_float,
    normalize_usernames,
)

pytestmark = pytest.mark.ui


def test_map_examples():

    usernames = [
        "JAY",
        "SARAH",
        "MIKE",
    ]

    normalized = normalize_usernames(
        usernames
    )

    prices = [
        "$19.99",
        "$5.50",
        "$100.00",
    ]

    converted_prices = convert_prices_to_float(
        prices
    )

    print(normalized)
    print(converted_prices)

    assert normalized == [
        "jay",
        "sarah",
        "mike",
    ]

    assert converted_prices == [
        19.99,
        5.50,
        100.00,
    ]
