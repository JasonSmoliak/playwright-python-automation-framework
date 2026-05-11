class ApiResponseError(Exception):

    def __init__(self, message, status_code):

        self.status_code = status_code

        super().__init__(
            f"{message} | Status Code: {status_code}"
        )
