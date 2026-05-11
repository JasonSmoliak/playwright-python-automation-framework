import pytest

from exceptions.api_exceptions import ApiResponseError
from utils.api_validator import validate_status_code

pytestmark = pytest.mark.api


def test_custom_api_exception():

    with pytest.raises(ApiResponseError) as exc_info:

        validate_status_code(500)

    print(exc_info.value)

    assert "Status Code: 500" in str(exc_info.value)
