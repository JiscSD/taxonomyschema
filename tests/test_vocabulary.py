import json
from taxonomyschema.vocabulary import VocabularyEncoder, VocabularyManifest  # noqa: E501


def test_vocabulary_manifest(input_fixtures, expected_manifest):
    vocab_manifest = VocabularyManifest(input_fixtures)
    result = json.dumps(vocab_manifest, cls=VocabularyEncoder, indent=4)
    assert expected_manifest == result
