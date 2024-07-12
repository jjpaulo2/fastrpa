SOURCE = fastrpa


install:
	@poetry install --no-root

check_format:
	@poetry run ruff format $(SOURCE) --check

format:
	@poetry run ruff format $(SOURCE)

check_lint:
	@poetry run ruff check $(SOURCE)

lint:
	@poetry run ruff check $(SOURCE) --fix

check_types:
	@poetry run mypy $(SOURCE)
