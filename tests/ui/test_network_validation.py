import pytest
from playwright.sync_api import expect

def test_ui_triggers_api_and_validate_response(page):
    page.set_content("""
    <button id="load">Load Post</button>
    <div id="title"></div>

    <script>
      document.getElementById("load").addEventListener("click", async () => {
        const res = await fetch("https://jsonplaceholder.typicode.com/posts/1");
        const data = await res.json();
        document.getElementById("title").textContent = data.title;
      });
    </script>
    """)

    with page.expect_response("**/posts/1") as response_info:
        page.click("#load")

    response = response_info.value
    data = response.json()

    # API validation
    assert data["id"] == 1
    assert "title" in data

    # UI validation
    expect(page.locator("#title")).to_have_text(data["title"])
