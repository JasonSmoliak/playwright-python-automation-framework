from api.base_client import BaseApiClient


class PostsClient(BaseApiClient):
    def __init__(self, api_context):
        super().__init__(api_context)
        self.base_path = "/posts"

    def get_post(self, post_id):
        return self.get(f"{self.base_path}/{post_id}")

    def create_post(self, payload):
        return self.post(self.base_path, payload)

    def update_post(self, post_id, payload):
        return self.put(f"{self.base_path}/{post_id}", payload)

    def delete_post(self, post_id):
        return self.delete(f"{self.base_path}/{post_id}")
