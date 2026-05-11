from exceptions.api_exceptions import ApiResponseError


def validate_status_code(status_code):

    if status_code >= 400:

        raise ApiResponseError(
            "API request failed",
            status_code,
        )

    return True
