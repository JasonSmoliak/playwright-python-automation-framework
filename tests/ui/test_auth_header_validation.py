import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.ui


def test_ui_sends_auth_header_with_api_request(page):
    def handle_route(route):
        headers = route.request.headers

        assert headers["authorization"] == "Bearer mock-token-abc123"
        assert headers["x-test-client"] == "playwright"

        route.fulfill(
            status=200,
            content_type="application/json",
            json={"message": "Secure data loaded"},
        )

    page.route("**/api/secure-data", handle_route)

    page.goto("https://example.com")

    page.evaluate("""() => {
        document.body.innerHTML = `
            <button id="load">Load Secure Data</button>
            <p id="result"></p>
        `;

        localStorage.setItem("auth_token", "mock-token-abc123");

        document.getElementById("load").addEventListener("click", async () => {
            const token = localStorage.getItem("auth_token");

            const response = await fetch("/api/secure-data", {
                method: "GET",
                headers: {
                    "Authorization": `Bearer ${token}`,
                    "X-Test-Client": "playwright"
                }
            });

            const data = await response.json();
            document.getElementById("result").textContent = data.message;
        });
    }""")

    with page.expect_response("**/api/secure-data") as response_info:
        page.get_by_role("button", name="Load Secure Data").click()

    response = response_info.value
    assert response.status == 200

    expect(page.locator("#result")).to_have_text("Secure data loaded")
