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

🚀 Features

Playwright browser automation

pytest test runner

Page Object Model (POM)

Positive and negative test coverage

Parallel execution with pytest-xdist

Automatic screenshots on failure

Playwright trace files on failure

GitHub Actions CI pipeline

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
make install
make test
make test-headed
make test-parallel
make test-parallel-headed
make trace

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

👤 Author

Automation practice project demonstrating Playwright UI automation with Python and pytest.

---

# 💡 What this does for you

This version makes your repo:

- **Easy to scan in 10 seconds**
- Clearly **structured**
- Shows **real-world tooling (CI, parallel, debugging)**
- Looks like something used in an actual QA team

---

# 🧠 One small but powerful next move

Add this as your **GitHub repo description (top right)**:

> Playwright + Python automation framework with pytest, POM design, CI pipeline, parallel execution, and failure debugging (screenshots + traces)

Short, keyword-rich, recruiter-friendly.

---

If you want next, I can show you **exactly how to talk through this project in an interview** — that’s where this really starts paying off.

