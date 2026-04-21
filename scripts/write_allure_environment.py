import os
import sys
from pathlib import Path

# Add project root to PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parents[1]))

from config import get_current_env


def main() -> None:
    allure_results_dir = Path("allure-results")
    allure_results_dir.mkdir(exist_ok=True)

    env_name = os.getenv("TEST_ENV", "dev")
    browser_name = os.getenv("BROWSER", "chromium")
    env_config = get_current_env()

    github_ref_name = os.getenv("GITHUB_REF_NAME", "local")
    github_sha = os.getenv("GITHUB_SHA", "local")
    github_run_id = os.getenv("GITHUB_RUN_ID", "local")
    github_repository = os.getenv("GITHUB_REPOSITORY", "local")
    github_workflow = os.getenv("GITHUB_WORKFLOW", "local")

    environment_file = allure_results_dir / "environment.properties"

    content = [
        f"Environment={env_name}",
        f"Base URL={env_config['base_url']}",
        f"Browser={browser_name}",
        "Framework=pytest",
        "UI Automation=Playwright Python",
        f"GitHub Repository={github_repository}",
        f"GitHub Workflow={github_workflow}",
        f"GitHub Branch={github_ref_name}",
        f"Git Commit={github_sha}",
        f"GitHub Run ID={github_run_id}",
    ]

    environment_file.write_text("\n".join(content) + "\n", encoding="utf-8")
    print(f"Wrote {environment_file}")


if __name__ == "__main__":
    main()
