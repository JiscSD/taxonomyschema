install:
	@pip install -r requirements-to-freeze.txt --upgrade
	@pip freeze > requirements.txt

test:
	@pytest

test-integration:
	@pytest -c tox_integration.ini

debug:
	@pytest --pdb

.PHONY: test setup deps
