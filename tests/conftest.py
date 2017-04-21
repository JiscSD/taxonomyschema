import pytest
import json
from glob import glob
from os.path import join

pytest_plugins = ['helpers_namespace']


@pytest.fixture
def input_fixtures():
    return 'tests/fixtures/input'


def get_output(filepath):
    outpath = filepath.replace('input', 'output')
    with open(outpath) as f:
        return json.dumps(json.load(f))


@pytest.helpers.register
def testdata():
    '''
    loads the tests/fixtures/input, JSON(tests/fixtures/output)
    '''
    input_files = glob(join(input_fixtures(), '*.json'))
    return [(f, get_output(f)) for f in input_files]


@pytest.fixture
def testdata_manifest():
    '''
    loads the tests/fixtures/input, JSON(tests/fixtures/output)
    '''
    input_files = sorted(glob(join(input_fixtures(), '*.json')))
    return [json.loads(get_output(f)) for f in input_files]
