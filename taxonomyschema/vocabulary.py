import json
from os.path import join
from glob import glob


class VocabularyEncoder(json.JSONEncoder):
    """
    Encodes a Vocuabulary class to JSON
    """

    def default(self, obj):
        if isinstance(obj, Vocabulary) or isinstance(obj, VocabularyManifest):
            return obj.to_json()

        return json.JSONEncoder.default(self, obj)


class Vocabulary():
    """
    Loads a Vocabulary model definition
    that is serialisable with json.dumps()
    """

    def __init__(self, filepath):
        model = self._load(filepath)
        self.vocabularyId = model['vocabularyId']
        self.vocabularyName = model['vocabularyName']
        self.vocabularyValues = model['vocabularyValues']

    def _load(self, filepath):
        with open(filepath) as f:
            return json.load(f)

    def to_json(self):
        return self.__dict__


class VocabularyManifest():
    """
    Loads all JSON schemas in a directory
    and generates a manifest of Vocabulary instances
    """

    def __init__(self, dirpath):
        schema_files = sorted(glob(join(dirpath, '*.json')))
        self.manifest = [Vocabulary(f) for f in schema_files]

    def to_json(self):
        return self.manifest
