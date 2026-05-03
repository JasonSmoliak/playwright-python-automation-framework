import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.ui


def test_flaky_api_retry_then_success(page):
    call_count = {"count": 0}

    def handle_route(route):
        call_count["count"] += 1

        # First call fails
        if call_count["count"] == 1:
            route.fulfill(
                status=500,
                content_type="application/json",
                json={"error": "Temporary failure"},
            )
        else:
            # Second call succeeds
            route.fulfill(
                status=200,
                content_type="application/json",
                json={"title": "Recovered after retry"},
            )

    page.route("**/api/data", handle_route)

    page.set_content("""
    <button id="load">Load Data</button>
    <p id="result"></p>

    <script>
      async function fetchWithRetry() {
        try {
          const res = await fetch("https://example.com/api/data");

          if (!res.ok) throw new Error("Fail");

          return await res.json();
        } catch (e) {
          // retry once
          const retryRes = await fetch("https://example.com/api/data");
          return await retryRes.json();
        }
      }

      document.getElementById("load").addEventListener("click", async () => {
        const data = await fetchWithRetry();
        document.getElementById("result").textContent = data.title;
      });
    </script>
    """)

    page.click("#load")

    expect(page.locator("#result")).to_have_text("Recovered after retry")

    assert call_count["count"] == 2
