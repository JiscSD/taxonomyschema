import pytest
import json
from taxonomyschema.vocabulary import Vocabulary, VocabularyEncoder


@pytest.mark.parametrize("schema,expected", pytest.helpers.testdata())
def test_vocabulary_serialisation(schema, expected):
    vocab = Vocabulary(schema)
    result = json.dumps(vocab, cls=VocabularyEncoder)
    assert expected == result
