import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.ui


def test_api_failure_shows_error(page):
    def handle_route(route):
        route.fulfill(
            status=500,
            content_type="application/json",
            json={"error": "Server error"},
        )

    page.route("**/api/data", handle_route)

    page.set_content("""
    <button id="load">Load Data</button>
    <p id="error" style="display:none; color:red;"></p>

    <script>
      document.getElementById("load").addEventListener("click", async () => {
        try {
          const res = await fetch("https://example.com/api/data");
          if (!res.ok) throw new Error("Failed to load");

        } catch (e) {
          const el = document.getElementById("error");
          el.textContent = "Failed to load";
          el.style.display = "block";
        }
      });
    </script>
    """)

    page.click("#load")

    expect(page.locator("#error")).to_have_text("Failed to load")
