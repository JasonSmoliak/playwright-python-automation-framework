<h1 align="center">Playwright Python Automation Framework</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Playwright-passing-brightgreen" />
  <img src="https://img.shields.io/badge/Python-3.12-blue" />
  <img src="https://img.shields.io/badge/Pytest-Framework-orange" />
  <img src="https://img.shields.io/badge/Allure-Reporting-purple" />
</p>

<p align="center">
  A modern end-to-end automation framework using Playwright, pytest, and Allure reporting.
</p>
---

## 📁 Project Structure

```text
python-playwright/
├── pages/
│   ├── example_page.py
│   └── login_page.py
├── tests/
│   ├── test_example.py
│   └── test_login.py
├── screenshots/
├── test-results/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── Makefile

## Features

### 🔹 UI Automation (Playwright)
- End-to-end browser automation using Playwright (Python)
- Page Object Model (POM) design pattern for maintainable test structure
- Dynamic UI handling (elements appearing/disappearing, async updates)
- Dropdown, modal, alert, and table interaction coverage
- Robust locator strategies using roles, labels, and test IDs

### 🔹 API Testing & Integration
- API testing using Playwright request context
- Combined API + UI validation workflows
- API-driven test data creation and UI verification
- Mocked API responses using Playwright network interception

### 🔹 Data-Driven Testing
- JSON-based test data management
- Parameterized tests using pytest
- Scalable approach for multiple test scenarios

### 🔹 Test Organization & Execution
- Custom pytest markers:
  - `smoke` (critical path)
  - `regression` (full suite)
  - `ui` (UI tests)
  - `api` (API tests)
- Selective test execution via markers
- Parallel test execution using pytest-xdist
- Makefile commands for simplified test runs

### 🔹 Flaky Test Handling
- Controlled retry logic using pytest-rerunfailures
- Targeted retries for unstable external UI scenarios
- Avoids masking real defects while improving stability

### 🔹 Reporting (Allure)
- Rich test reporting with:
  - Step-level visibility
  - Test hierarchy (Epic / Feature / Story)
  - Screenshot capture on failure
  - Environment metadata (browser, base URL, GitHub info)
  - Custom failure categories (UI, API, config, flaky)
- Clean, professional HTML reports

### 🔹 CI/CD Integration
- GitHub Actions pipeline for automated test execution
- CI runs on every push and pull request
- Environment-aware test execution

### 🔹 Developer Experience
- Makefile for common workflows:
  - Run tests
  - Run subsets (smoke, UI, API)
  - Generate Allure reports
- Clean project structure for scalability
- Reusable fixtures and centralized configuration

🛠 Technologies Used

Python

Playwright

pytest

pytest-xdist

Git

GitHub Actions (CI)

## 🚀 Quick Start / How to Run

### 1️⃣ Clone the repository

git clone https://github.com/jasonsmoliak/playwright-python-automation-framework.git
cd playwright-python-automation-framework

2️⃣ Create and activate virtual environment

python3 -m venv venv
source venv/bin/activate

3️⃣ Install dependencies

pip install -r requirements.txt
playwright install

4️⃣ Run tests

Run all tests:

pytest

Run specific test groups:

# Smoke tests (critical path)
pytest -m smoke

# UI tests only
pytest -m ui

# API tests only
pytest -m api

Or use Makefile commands:

make test
make test-smoke
make test-ui
make test-api

5️⃣ Run tests with retry logic (for flaky scenarioos)

make test-ui-rerun

6️⃣ Generate Allure Report

make allure-results
make allure-serve

This will open a browser with a detailed test report including:

* test steps
* screenshots on failure
* environment info
* categorized failures

7️⃣ Run tests in parallel 

pytest -n auto

🧪 Example Test Coverage

* UI login validation
* Dynamic table data validation
* API + UI combined workflows
* Mocked API success and error scenarios


🐞 Debugging Failures

On failure, the framework automatically saves:

Screenshots
screenshots/

Playwright trace files
test-results/

View a trace:

playwright show-trace test-results/<trace-folder>/trace.zip

🔄 CI Pipeline

This project uses GitHub Actions to run tests automatically on every push and pull request.

Workflow file:

.github/workflows/playwright.yml

🧪 Example Test Scenario

Automated login test for a public demo site.

Valid credentials:

username: practice
password: SuperSecretPassword!

Tests implemented:

Successful login

Invalid login validation

Navigation verification

## 🔮 Future Enhancements

- Dockerized test execution for consistent environments
- Advanced test reporting (Allure history & trends)
- CI pipeline optimization (parallel execution, scheduled runs)
- Additional API mocking scenarios for edge case coverage
- Integration with external test management tools (e.g., TestRail)

👤 Author - Jason Smoliak

Automation practice project demonstrating Playwright UI automation with Python and pytest.

