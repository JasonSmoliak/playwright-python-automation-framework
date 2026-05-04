import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.ui


def test_download_file(page):
    page.set_content("""
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

    downloaded_path = download.path()
    assert downloaded_path is not None
