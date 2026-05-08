import json
import os
from pathlib import Path

from dotenv import load_dotenv


def load_env_config(env):
    load_dotenv()

    config_file = Path(f"env_config/{env}.json")

    if not config_file.exists():
        raise FileNotFoundError(
            f"Environment config not found: {config_file}"
        )

    with open(config_file) as f:
        config = json.load(f)

    username_key = config.get("username_env")
    password_key = config.get("password_env")

    if username_key:
        config["username"] = os.getenv(username_key)

    if password_key:
        config["password"] = os.getenv(password_key)

    if not config.get("username"):
        raise ValueError(f"Username not found for ENV={env}")

    if not config.get("password"):
        raise ValueError(f"Password not found for ENV={env}")

    return config
