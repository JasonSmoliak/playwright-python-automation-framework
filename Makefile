.PHONY: install test test-headed test-parallel test-parallel-headed trace clean

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

clean:
	rm -rf .pytest_cache test-results screenshots __pycache__
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

