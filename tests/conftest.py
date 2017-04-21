import pytest
import json
from glob import glob

pytest_plugins = ['helpers_namespace']


def load_json(filepath):
    with open(filepath) as f:
        return json.dumps(json.load(f))


def get_output(filepath):
    return load_json(filepath.replace('input', 'output'))


@pytest.helpers.register
def testdata():
    '''
    loads the tests/fixtures/input, JSON(tests/fixtures/output)
    '''
    input_files = glob('tests/fixtures/input/*')
    return [(f, get_output(f)) for f in input_files]
