import pytest
import time

from utils.timer_context import TimerContext

pytestmark = pytest.mark.ui


def test_timer_context():
    with TimerContext():

        time.sleep(2)

    assert True
