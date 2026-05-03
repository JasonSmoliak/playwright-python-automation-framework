import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.ui


def test_intercept_and_modify_api_response(page):
    def handle_route(route):
        route.fulfill(
            status=200,
            content_type="application/json",
            json={
                "userId": 1,
                "id": 1,
                "title": "Modified by Playwright",
                "body": "This response was intercepted before the UI saw it.",
            },
        )

    page.route("**/posts/1", handle_route)

    page.set_content("""
    <h1>Post Viewer</h1>
    <button id="load">Load Post</button>
    <h2 id="title"></h2>
    <p id="body"></p>

    <script>
      document.getElementById("load").addEventListener("click", async () => {
        const response = await fetch("https://jsonplaceholder.typicode.com/posts/1");
        const data = await response.json();

        document.getElementById("title").textContent = data.title;
        document.getElementById("body").textContent = data.body;
      });
    </script>
    """)

    page.get_by_role("button", name="Load Post").click()

    expect(page.locator("#title")).to_have_text("Modified by Playwright")
    expect(page.locator("#body")).to_have_text(
        "This response was intercepted before the UI saw it."
    )
