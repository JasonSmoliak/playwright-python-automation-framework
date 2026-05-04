from pathlib import Path

import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.ui


def test_upload_single_file(page):
    upload_file = Path("test_data/files/sample_upload.txt").resolve()

    page.set_content("""
    <h1>File Upload</h1>

    <label for="file-upload">Upload file</label>
    <input id="file-upload" type="file">

    <p id="file-name"></p>

    <script>
      document.getElementById("file-upload").addEventListener("change", (event) => {
        const file = event.target.files[0];
        document.getElementById("file-name").textContent = file ? file.name : "";
      });
    </script>
    """)

    page.locator("#file-upload").set_input_files(str(upload_file))

    expect(page.locator("#file-name")).to_have_text("sample_upload.txt")
