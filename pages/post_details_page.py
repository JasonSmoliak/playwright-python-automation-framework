from playwright.sync_api import Page, expect


class PostDetailsPage:
    def __init__(self, page: Page):
        self.page = page
        self.heading = page.get_by_role("heading", name="Post Details")
        self.post_card = page.locator('[data-testid="post-card"]')
        self.post_title = page.locator('[data-testid="post-title"]')
        self.post_body = page.locator('[data-testid="post-body"]')
        self.post_user = page.locator('[data-testid="post-user"]')

    def load_post_content(self, title: str, body: str, user_id: int):
        self.page.set_content(f"""
        <html>
          <body>
            <section>
              <h1>Post Details</h1>
              <article data-testid="post-card">
                <h2 data-testid="post-title">{title}</h2>
                <p data-testid="post-body">{body}</p>
                <span data-testid="post-user">{user_id}</span>
              </article>
            </section>
          </body>
        </html>
        """)

    def verify_post_details(self, title: str, body: str, user_id: int):
        expect(self.heading).to_be_visible()
        expect(self.post_card).to_be_visible()
        expect(self.post_title).to_have_text(title)
        expect(self.post_body).to_have_text(body)
        expect(self.post_user).to_have_text(str(user_id))
