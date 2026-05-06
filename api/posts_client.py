class PostsClient:
    def __init__(self, api_context):
        self.api_context = api_context
        self.base_path = "/posts"

    def get_post(self, post_id):
        response = self.api_context.get(f"{self.base_path}/{post_id}")

        assert response.ok, (
            f"GET post failed with status {response.status}"
        )

        return response

    def create_post(self, payload):
        response = self.api_context.post(
            self.base_path,
            data=payload,
        )

        assert response.ok, (
            f"CREATE post failed with status {response.status}"
        )

        return response

    def update_post(self, post_id, payload):
        response = self.api_context.put(
            f"{self.base_path}/{post_id}",
            data=payload,
        )

        assert response.ok, (
            f"UPDATE post failed with status {response.status}"
        )

        return response

    def delete_post(self, post_id):
        response = self.api_context.delete(
            f"{self.base_path}/{post_id}"
        )

        assert response.ok, (
            f"DELETE post failed with status {response.status}"
        )

        return response
