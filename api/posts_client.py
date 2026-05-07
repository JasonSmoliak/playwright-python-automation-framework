from api.base_client import BaseApiClient


class PostsClient(BaseApiClient):
    def __init__(self, api_context):
        super().__init__(api_context)
        self.base_path = "/posts"

    def get_post(self, post_id):
        response = self.api_context.get(f"{self.base_path}/{post_id}")
        return self.assert_ok(response, action=f"GET post {post_id}")

    def create_post(self, payload):
        response = self.api_context.post(
            self.base_path,
            data=payload,
        )
        return self.assert_ok(response, action="CREATE post")

    def update_post(self, post_id, payload):
        response = self.api_context.put(
            f"{self.base_path}/{post_id}",
            data=payload,
        )
        return self.assert_ok(response, action=f"UPDATE post {post_id}")

    def delete_post(self, post_id):
        response = self.api_context.delete(
            f"{self.base_path}/{post_id}"
        )
        return self.assert_ok(response, action=f"DELETE post {post_id}")
