import os
from pathlib import Path

from config import get_current_env


def main() -> None:
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

    environment_file.write_text("\n".join(content) + "\n", encoding="utf-8")
    print(f"Wrote {environment_file}")


if __name__ == "__main__":
    main()
