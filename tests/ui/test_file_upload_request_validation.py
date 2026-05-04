from pathlib import Path

import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.ui


def test_file_upload_request_contains_file(page):
    upload_file = Path("test_data/files/sample_upload.txt").resolve()

    def handle_route(route):
        request = route.request

        assert request.method == "POST"
        assert "multipart/form-data" in request.headers["content-type"]

        body = request.post_data

        assert "sample_upload.txt" in body

        route.fulfill(
            status=200,
            content_type="application/json",
            json={"status": "uploaded"},
        )

    page.route("**/upload", handle_route)

    page.set_content("""
    <h1>Upload File</h1>

    <input id="file" type="file">
    <button id="upload">Upload</button>

    <p id="result"></p>

    <script>
      document.getElementById("upload").addEventListener("click", async () => {
        const fileInput = document.getElementById("file");
        const formData = new FormData();
        formData.append("file", fileInput.files[0]);

        const res = await fetch("https://example.com/upload", {
          method: "POST",
          body: formData
        });

        const data = await res.json();
        document.getElementById("result").textContent = data.status;
      });
    </script>
    """)

    page.locator("#file").set_input_files(str(upload_file))

    page.click("#upload")

    expect(page.locator("#result")).to_have_text("uploaded")
