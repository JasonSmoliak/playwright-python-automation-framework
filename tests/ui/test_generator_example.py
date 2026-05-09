import pytest

from utils.simple_generator import countdown_generator

pytestmark = pytest.mark.ui


def test_countdown_generator():

    numbers = []

    for number in countdown_generator(5):
        print(number)

        numbers.append(number)

    assert numbers == [5, 4, 3, 2, 1]
