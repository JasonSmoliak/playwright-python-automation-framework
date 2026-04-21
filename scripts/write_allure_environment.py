import sys
from pathlib import Path

# Add project root to PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parents[1]))

import os
from config import get_current_env


def main():
    allure_results_dir = Path("allure-results")
    allure_results_dir.mkdir(exist_ok=True)

    env_name = os.getenv("TEST_ENV", "dev")
    browser_name = os.getenv("BROWSER", "chromium")
    env_config = get_current_env()

    environment_file = allure_results_dir / "environment.properties"

    content = [
        f"Environment={env_name}",
        f"Base URL={env_config['base_url']}",
        f"Browser={browser_name}",
        "Framework=pytest",
        "UI Automation=Playwright Python",
    ]

    environment_file.write_text("\n".join(content) + "\n")
    print(f"Wrote {environment_file}")


if __name__ == "__main__":
    main()
