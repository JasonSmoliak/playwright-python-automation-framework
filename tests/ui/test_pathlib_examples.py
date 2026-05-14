import pytest

from utils.pathlib_examples import (
    create_log_file,
    get_file_name,
)

pytestmark = pytest.mark.ui


def test_pathlib_examples():

    log_file = create_log_file()

    file_name = get_file_name(
        "screenshots/login_failure.png"
    )

    print(log_file)
    print(file_name)

    assert log_file.exists()

    assert file_name == "login_failure.png"
