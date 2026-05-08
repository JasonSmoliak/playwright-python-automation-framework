import pytest
import time

from utils.timing_decorator import measure_execution_time

pytestmark = pytest.mark.ui


@measure_execution_time
def slow_operation():
    time.sleep(2)


def test_timing_decorator():
    slow_operation()

    assert True
