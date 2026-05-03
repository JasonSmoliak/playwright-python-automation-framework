import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.ui


def test_fetch_real_response_and_modify_one_field(page):
    def handle_route(route):
        response = route.fetch()
        data = response.json()

        data["title"] = "Partially Modified by Playwright"

        route.fulfill(
            response=response,
            json=data,
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

    expect(page.locator("#title")).to_have_text("Partially Modified by Playwright")
    expect(page.locator("#body")).not_to_be_empty()
