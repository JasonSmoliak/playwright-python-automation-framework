class BaseApiClient:
    def __init__(self, api_context):
        self.api_context = api_context

    def assert_ok(self, response, action="API request"):
        assert response.ok, (
            f"{action} failed with status {response.status}. "
            f"Response body: {response.text()}"
        )
        return response
