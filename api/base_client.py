from utils.logger import get_logger


class BaseApiClient:
    def __init__(self, api_context):
        self.api_context = api_context
        self.logger = get_logger(self.__class__.__name__)

    def assert_ok(self, response, action="API request"):
        if response.ok:
            self.logger.info(
                f"{action} succeeded with status {response.status}"
            )
        else:
            self.logger.error(
                f"{action} failed with status {response.status}. "
                f"Response body: {response.text()}"
            )

        assert response.ok, (
            f"{action} failed with status {response.status}. "
            f"Response body: {response.text()}"
        )

        return response
