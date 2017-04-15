import pytest
import json
from vocabulary.vocabulary import *


@pytest.mark.parametrize(('git_status', 'filepath'), [
    ('A', 'test/fixtures/input/01.json'),
    ('M', 'test/fixtures/input/02.json')
])
def test_answer(git_status, filepath):
    result = VocabularyFactory(money)
    with open('test/fixtures/output/01.json') as f:
        expected = json.loads(f)
    assert expected == result
