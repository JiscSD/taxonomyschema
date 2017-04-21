install:
	@pip install -r requirements.txt
	@pre-commit install

deps:
	@pip install -r requirements-to-freeze.txt --upgrade
	@pip freeze > requirements.txt

lint:
	@pre-commit run \
		--allow-unstaged-config \
		--all-files \
		--verbose

test:
	@pytest

test-integration:
	@pytest -c tox_integration.ini

debug:
	@pytest --pdb

.PHONY: install deps lint test* debug
