.PHONY: install test test-headed test-parallel test-parallel-headed trace clean \
        test-dev test-stage test-prod login-dev login-stage login-prod \
        allure-results allure-serve allure-generate allure-open

install:
	pip install -r requirements.txt
	playwright install

test:
	pytest

test-headed:
	pytest --headed

test-parallel:
	pytest -n auto

test-parallel-headed:
	pytest --headed -n 2

trace:
	pytest --headed --tracing=retain-on-failure

test-dev:
	TEST_ENV=dev pytest

test-stage:
	TEST_ENV=stage pytest

test-prod:
	TEST_ENV=prod pytest

login-dev:
	TEST_ENV=dev pytest tests/ui/test_login.py -v --headed

login-stage:
	TEST_ENV=stage pytest tests/ui/test_login.py -v --headed

login-prod:
	TEST_ENV=prod pytest tests/ui/test_login.py -v --headed

clean:
	rm -rf .pytest_cache test-results screenshots .auth __pycache__
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

allure-results:
	pytest --alluredir=allure-results --clean-alluredir
	python scripts/write_allure_environment.py
	python scripts/write_allure_categories.py

allure-serve:
	allure serve allure-results

allure-generate:
	allure generate allure-results -o allure-report --clean

allure-open:
	allure open allure-report
