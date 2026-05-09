from typing import Dict, List


def create_test_user(
    username: str,
    role: str,
) -> Dict[str, str]:

    return {
        "username": username,
        "role": role,
    }


def get_supported_browsers() -> List[str]:

    return [
        "chromium",
        "firefox",
        "webkit",
    ]
