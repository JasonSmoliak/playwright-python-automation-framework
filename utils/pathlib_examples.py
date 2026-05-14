from pathlib import Path


def create_log_file():

    logs_dir = Path("logs")

    logs_dir.mkdir(exist_ok=True)

    log_file = logs_dir / "test_log.txt"

    log_file.write_text(
        "Playwright test execution complete"
    )

    return log_file


def get_file_name(path):

    return Path(path).name
