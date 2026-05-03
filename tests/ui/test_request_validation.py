import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.ui


def test_validate_request_payload_from_ui(page):
    page.set_content("""
    <h1>Create Post</h1>
    <input id="title" placeholder="Title">
    <textarea id="body" placeholder="Body"></textarea>
    <button id="submit">Submit</button>
    <p id="result"></p>

    <script>
      document.getElementById("submit").addEventListener("click", async () => {
        const payload = {
          title: document.getElementById("title").value,
          body: document.getElementById("body").value,
          userId: 1
        };

        const response = await fetch("https://jsonplaceholder.typicode.com/posts", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(payload)
        });

        const data = await response.json();
        document.getElementById("result").textContent = data.title;
      });
    </script>
    """)

    page.locator("#title").fill("Playwright Request Test")
    page.locator("#body").fill("Validating request payload from UI")

    with page.expect_request("**/posts") as request_info:
        page.get_by_role("button", name="Submit").click()

    request = request_info.value
    payload = request.post_data_json

    assert request.method == "POST"
    assert payload["title"] == "Playwright Request Test"
    assert payload["body"] == "Validating request payload from UI"
    assert payload["userId"] == 1

    expect(page.locator("#result")).to_have_text("Playwright Request Test")
