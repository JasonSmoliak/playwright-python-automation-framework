import pytest
from playwright.sync_api import expect


pytestmark = pytest.mark.ui


def test_mock_api_response_displays_user_data(page):
    mock_user = {
        "id": 1,
        "name": "Jay Sunshine",
        "role": "QA Automation Engineer",
    }

    def handle_user_route(route):
        route.fulfill(
            status=200,
            content_type="application/json",
            json=mock_user,
        )

    page.route("**/api/user/1", handle_user_route)

    page.set_content("""
    <html>
      <body>
        <h1>User Profile</h1>
        <button id="load-user">Load User</button>

        <section data-testid="user-card" style="display:none;">
          <h2 data-testid="user-name"></h2>
          <p data-testid="user-role"></p>
        </section>

        <script>
          document.getElementById("load-user").addEventListener("click", async () => {
            const response = await fetch("https://example.com/api/user/1");
            const user = await response.json();

            document.querySelector('[data-testid="user-name"]').textContent = user.name;
            document.querySelector('[data-testid="user-role"]').textContent = user.role;
            document.querySelector('[data-testid="user-card"]').style.display = "block";
          });
        </script>
      </body>
    </html>
    """)

    page.get_by_role("button", name="Load User").click()

    expect(page.get_by_test_id("user-card")).to_be_visible()
    expect(page.get_by_test_id("user-name")).to_have_text("Jay Sunshine")
    expect(page.get_by_test_id("user-role")).to_have_text("QA Automation Engineer")
