# Playwright Python Automation Framework

![Playwright Tests](https://github.com/jasonsmoliak/playwright-python-automation-framework/actions/workflows/playwright.yml/badge.svg)

This project demonstrates a UI automation framework built with **Playwright**, **Python**, and **pytest** using the **Page Object Model (POM)** design pattern.

The framework includes both **positive and negative test scenarios**, along with debugging features such as **automatic screenshots and Playwright trace files on failure**, and **parallel test execution**.

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

⚙️ Setup Instructions

Clone the repository:

git clone https://github.com/jasonsmoliak/playwright-python-automation-framework.git
cd playwright-python-automation-framework

Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies and browsers:

pip install -r requirements.txt
playwright install

▶️ Running Tests

Run all tests:

pytest

Run with visible browser:

pytest --headed

🧰 Using Makefile (Recommended)
### Environment-specific commands

```bash
make test-dev
make test-stage
make test-prod

make login-dev
make login-stage
make login-prod
```

⚡ Parallel Execution

Run tests in parallel:

pytest -n auto

Or:

make test-parallel

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

🔮 Future Improvements

API testing integration

Test data management

Environment configuration (dev/stage/prod)

Reporting with Allure

Dockerized test execution

👤 Author - Jason Smoliak

Automation practice project demonstrating Playwright UI automation with Python and pytest.

