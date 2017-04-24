deps:
	@pip install -r requirements-to-freeze.txt --upgrade
	@pip freeze > requirements.txt

install:
	@pip install -r requirements.txt
	@pre-commit install

clean:
	@pip uninstall -r requirements.txt
	@pip freeze > requirements.txt

lint:
	@pre-commit run \
		--allow-unstaged-config \
		--all-files \
		--verbose

test:
	@pytest

debug:
	@pytest --pdb

.PHONY: install deps lint test* debug clean
