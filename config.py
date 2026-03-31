import os


ENVIRONMENTS = {
    "dev": {
        "base_url": "https://practice.expandtesting.com/login",
        "username": "practice",
        "password": "SuperSecretPassword!",
    },
    "stage": {
        "base_url": "https://practice.expandtesting.com/login",
        "username": "practice",
        "password": "SuperSecretPassword!",
    },
    "prod": {
        "base_url": "https://practice.expandtesting.com/login",
        "username": "practice",
        "password": "SuperSecretPassword!",
    },
}


def get_current_env():
    env_name = os.getenv("TEST_ENV", "dev").lower()

    if env_name not in ENVIRONMENTS:
        raise ValueError(
            f"Unknown TEST_ENV '{env_name}'. "
            f"Valid values are: {', '.join(ENVIRONMENTS.keys())}"
        )

    return ENVIRONMENTS[env_name]
