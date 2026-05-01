.PHONY: install test test-headed test-parallel test-parallel-headed trace clean \
        test-dev test-stage test-prod login-dev login-stage login-prod \
        allure-results allure-serve allure-generate allure-open \
	test-smoke test-regression test-ui test-api

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

test-smoke:
	pytest -m smoke

test-regression:
	pytest -m regression

test-ui:
	pytest -m ui

test-api:
	pytest -m api

test-ui-rerun:
	pytest -m ui --reruns 2 --reruns-delay 1

test-smoke-rerun:
	pytest -m smoke --reruns 2 --reruns-delay 1
