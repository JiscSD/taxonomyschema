import pytest
import json
from os.path import join

fixtures = 'tests/fixtures'


@pytest.fixture
def input_fixtures():
    return join(fixtures, 'input')


@pytest.fixture
def expected_manifest():
    manifest = join(fixtures, 'manifest.json')
    with open(manifest, 'r') as m:
        manifest_json = json.loads(m.read())
    return json.dumps(manifest_json, indent=4)
