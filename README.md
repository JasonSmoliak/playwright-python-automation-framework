# Playwright Python Automation Framework

This project demonstrates a small UI automation framework built with **Playwright**, **Python**, and **pytest** using the **Page Object Model (POM)** design pattern.

The framework includes both **positive and negative test scenarios**, along with debugging features such as **automatic screenshots and Playwright trace files on failure**.

---

## Project Structure

```
python-playwright/
├── pages/
│   ├── example_page.py
│   └── login_page.py
│
├── tests/
│   ├── test_example.py
│   └── test_login.py
│
├── screenshots/
├── test-results/
├── conftest.py
├── pytest.ini
└── requirements.txt
```


---

## Features

- Playwright browser automation
- pytest test runner
- Page Object Model structure
- Positive and negative test scenarios
- Screenshots captured automatically on test failure
- Playwright trace files retained on failure
- GitHub Actions CI pipeline

---

## Technologies Used

- Python
- Playwright
- pytest
- Git
- GitHub Actions (CI)

---

## Setup Instructions

Clone the repository:

git clone https://github.com/jasonsmoliak/playwright-python-automation-framework.git

cd playwright-python-automation-framework


Create a virtual environment:

python3 -m venv venv
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt
playwright install


---

## Running Tests

Run all tests:


Run with visible browser:

pytest --headed

---

## Debugging Failures

When tests fail the framework automatically saves:

**Screenshots**

screenshots/


**Playwright trace files**

test-results/


You can open a trace with:

playwright show-trace test-results/<trace-folder>/trace.zip


---

## CI Pipeline

This project uses **GitHub Actions** to automatically run tests on every push and pull request.

Workflow file:

.github/workflows/playwright.yml


---

## Example Test Scenario

Automated login test for the Expand Testing demo site.

Valid login credentials:

username: practice
password: SuperSecretPassword!


Tests implemented:

- Successful login
- Invalid login validation
- Navigation verification

---

## Future Improvements

Potential enhancements:

- API testing integration
- Test data management
- Parallel execution
- Docker test environment
- Reporting with Allure

---

## Author

Automation practice project built to demonstrate Playwright UI automation with Python.



