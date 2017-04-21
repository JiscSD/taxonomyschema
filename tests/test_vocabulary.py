import pytest
import json
# from glob import glob
# from taxonomyschema.vocabulary import *
from taxonomyschema.vocabulary import Vocabulary, VocabularyEncoder
# import taxonomyschema.vocabulary


def load_json(filepath):
    with open(filepath) as f:
        return json.dumps(json.load(f))


testdata = [
    ('tests/fixtures/input/APC.json', 'tests/fixtures/output/APC.json'),
]


@pytest.mark.parametrize("schema,expected", testdata)
def test_vocabulary_serialisation(schema, expected):
    result = Vocabulary(schema)
    assert load_json(expected) == json.dumps(result, cls=VocabularyEncoder)
