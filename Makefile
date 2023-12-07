.PHONY: install
install:
	python -m pip install --upgrade pip
	pip install -e .[dev] --upgrade --upgrade-strategy eager
	pre-commit install

.PHONY: format
format:
	ruff format .
	ruff check . --fix
	mypy . --ignore-missing-imports

.PHONY: pytest
pytest:
	pytest --cov-report term-missing --cov=src tests/ -s