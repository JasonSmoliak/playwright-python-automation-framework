import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.ui


def test_slow_api_shows_loading_then_data(page):
    page.set_content("""
    <button id="load">Load Data</button>
    <p id="loading" style="display:none;">Loading...</p>
    <p id="result"></p>

    <script>
      document.getElementById("load").addEventListener("click", async () => {
        document.getElementById("loading").style.display = "block";

        await new Promise(resolve => setTimeout(resolve, 1500));

        const data = { title: "Loaded after delay" };

        document.getElementById("loading").style.display = "none";
        document.getElementById("result").textContent = data.title;
      });
    </script>
    """)

    loading = page.locator("#loading")
    result = page.locator("#result")

    page.get_by_role("button", name="Load Data").click()

    expect(loading).to_be_visible()
    expect(result).to_have_text("Loaded after delay")
    expect(loading).to_be_hidden()
