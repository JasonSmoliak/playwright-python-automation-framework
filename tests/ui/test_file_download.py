from pathlib import Path

import pytest

pytestmark = pytest.mark.ui


def test_download_file_and_verify_contents(page):
    downloads_dir = Path("downloads")
    downloads_dir.mkdir(exist_ok=True)

    expected_text = "This is a downloaded file."
    save_path = downloads_dir / "sample_download.txt"

    page.set_content(f"""
    <h1>File Download</h1>

    <a id="download-link"
       href="data:text/plain;charset=utf-8,This%20is%20a%20downloaded%20file."
       download="sample_download.txt">
       Download file
    </a>
    """)

    with page.expect_download() as download_info:
        page.get_by_role("link", name="Download file").click()

    download = download_info.value

    assert download.suggested_filename == "sample_download.txt"

    download.save_as(save_path)

    assert save_path.exists()
    assert save_path.read_text() == expected_text
