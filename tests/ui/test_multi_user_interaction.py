import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.ui


def test_user_a_creates_message_user_b_sees_it(browser):
    shared_messages = []

    context_a = browser.new_context()
    context_b = browser.new_context()

    user_a = context_a.new_page()
    user_b = context_b.new_page()

    def render_app(page, username):
        page.set_content(f"""
        <h1>Team Chat</h1>

        <p data-testid="current-user">{username}</p>

        <input id="message" placeholder="Message">
        <button id="send">Send</button>

        <ul id="messages"></ul>

        <script>
          window.renderMessages = (messages) => {{
            const list = document.getElementById("messages");
            list.innerHTML = "";

            messages.forEach((message) => {{
              const item = document.createElement("li");
              item.textContent = message.user + ": " + message.text;
              list.appendChild(item);
            }});
          }};

          document.getElementById("send").addEventListener("click", () => {{
            window.lastMessage = {{
              user: "{username}",
              text: document.getElementById("message").value
            }};
          }});
        </script>
        """)

    render_app(user_a, "User A")
    render_app(user_b, "User B")

    user_a.locator("#message").fill("Hello from User A")
    user_a.get_by_role("button", name="Send").click()

    user_a_message = user_a.evaluate("() => window.lastMessage")
    shared_messages.append(user_a_message)

    user_b.evaluate(
        "(messages) => window.renderMessages(messages)",
        shared_messages,
    )

    expect(user_b.locator("#messages")).to_contain_text(
        "User A: Hello from User A"
    )

    expect(user_a.get_by_test_id("current-user")).to_have_text("User A")
    expect(user_b.get_by_test_id("current-user")).to_have_text("User B")

    context_a.close()
    context_b.close()
