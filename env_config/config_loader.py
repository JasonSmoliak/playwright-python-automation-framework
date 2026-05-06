import json
import os
from pathlib import Path


def load_env_config():
    env = os.getenv("ENV", "dev")

    config_file = Path(f"env_config/{env}.json")

    if not config_file.exists():
        raise FileNotFoundError(
            f"Environment config not found: {config_file}"
        )

    with open(config_file) as f:
        return json.load(f)
