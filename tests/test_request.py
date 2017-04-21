# import pytest
# import json
# from taxonomyschema.vocabulary import Vocabulary, VocabularyEncoder, VocabularyManifest  # noqa: E501


# @pytest.mark.parametrize("schema,expected", pytest.helpers.testdata())
# def test_vocabulary_serialisation(schema, expected):
#     vocab = Vocabulary(schema)
#     result = json.dumps(vocab, cls=VocabularyEncoder)
#     assert expected == result


# def test_vocabulary_manifest(input_fixtures, testdata_manifest):
#     vocab_manifest = VocabularyManifest(input_fixtures)
#     result = json.dumps(vocab_manifest, cls=VocabularyEncoder, indent=4)
#     expected = json.dumps(testdata_manifest, indent=4)
#     assert expected == result
