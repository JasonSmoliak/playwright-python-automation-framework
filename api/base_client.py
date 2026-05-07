import json

from utils.logger import get_logger


class BaseApiClient:
    def __init__(self, api_context):
        self.api_context = api_context
        self.logger = get_logger(self.__class__.__name__)

    def _format_body(self, response):
        try:
            return json.dumps(response.json(), indent=2)
        except Exception:
            return response.text()

    def _log_request(self, method, endpoint, payload=None):
        self.logger.info(f"REQUEST: {method} {endpoint}")

        if payload is not None:
            self.logger.info(
                "REQUEST PAYLOAD:\n"
                f"{json.dumps(payload, indent=2)}"
            )

    def _log_response(self, response):
        self.logger.info(f"RESPONSE STATUS: {response.status}")
        self.logger.info(
            "RESPONSE BODY:\n"
            f"{self._format_body(response)}"
        )

    def _request(self, method, endpoint, payload=None):
        self._log_request(method, endpoint, payload)

        if method == "GET":
            response = self.api_context.get(endpoint)
        elif method == "POST":
            response = self.api_context.post(endpoint, data=payload)
        elif method == "PUT":
            response = self.api_context.put(endpoint, data=payload)
        elif method == "DELETE":
            response = self.api_context.delete(endpoint)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        self._log_response(response)
        return response

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

    def get(self, endpoint):
        response = self._request("GET", endpoint)
        return self.assert_ok(response, action=f"GET {endpoint}")

    def post(self, endpoint, payload):
        response = self._request("POST", endpoint, payload)
        return self.assert_ok(response, action=f"POST {endpoint}")

    def put(self, endpoint, payload):
        response = self._request("PUT", endpoint, payload)
        return self.assert_ok(response, action=f"PUT {endpoint}")

    def delete(self, endpoint):
        response = self._request("DELETE", endpoint)
        return self.assert_ok(response, action=f"DELETE {endpoint}")
