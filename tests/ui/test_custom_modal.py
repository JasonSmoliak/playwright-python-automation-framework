from playwright.sync_api import expect


def test_custom_modal_open_and_close(page):
    page.set_content("""
    <html>
      <body>
        <button id="open-modal">Open Modal</button>

        <div id="overlay" style="display:none; position:fixed; inset:0; background:rgba(0,0,0,0.4);">
          <div role="dialog" aria-modal="true" aria-labelledby="modal-title"
               style="width:300px; margin:100px auto; background:white; padding:20px;">
            <h2 id="modal-title">Test Modal</h2>
            <p>This is a custom modal window.</p>
            <button id="close-modal">Close</button>
          </div>
        </div>

        <script>
          const overlay = document.getElementById("overlay");
          document.getElementById("open-modal").addEventListener("click", () => {
            overlay.style.display = "block";
          });
          document.getElementById("close-modal").addEventListener("click", () => {
            overlay.style.display = "none";
          });
        </script>
      </body>
    </html>
    """)

    open_button = page.get_by_role("button", name="Open Modal")
    modal = page.get_by_role("dialog")
    title = page.get_by_role("heading", name="Test Modal")
    close_button = page.get_by_role("button", name="Close")

    open_button.click()

    expect(modal).to_be_visible()
    expect(title).to_be_visible()
    expect(modal).to_contain_text("This is a custom modal window.")

    close_button.click()

    expect(modal).not_to_be_visible()
