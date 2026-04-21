import json
from pathlib import Path


def main() -> None:
    allure_results_dir = Path("allure-results")
    allure_results_dir.mkdir(exist_ok=True)

    categories = [
        {
            "name": "UI locator and timeout issues",
            "messageRegex": ".*(TimeoutError|Locator\\.fill|to_be_visible|to_contain_text|element\\(s\\) not found).*",
            "matchedStatuses": ["failed", "broken"]
        },
        {
            "name": "Assertion mismatches",
            "messageRegex": ".*(AssertionError|expected to contain text|to_have_url|mismatch).*",
            "matchedStatuses": ["failed"]
        },
        {
            "name": "API and test data issues",
            "messageRegex": ".*(FileNotFoundError|JSONDecodeError|Could not extract|Process .* not found|CPU column not found).*",
            "matchedStatuses": ["failed", "broken"]
        },
        {
            "name": "Import and environment configuration issues",
            "messageRegex": ".*(ModuleNotFoundError|ImportError|No module named|Unknown TEST_ENV).*",
            "matchedStatuses": ["failed", "broken"]
        },
        {
            "name": "Potentially flaky external site behavior",
            "messageRegex": ".*(strict mode violation|redirected|unexpected value|ad|interstitial).*",
            "matchedStatuses": ["failed", "broken"],
            "flaky": True
        }
    ]

    categories_file = allure_results_dir / "categories.json"
    categories_file.write_text(json.dumps(categories, indent=2), encoding="utf-8")
    print(f"Wrote {categories_file}")


if __name__ == "__main__":
    main()
