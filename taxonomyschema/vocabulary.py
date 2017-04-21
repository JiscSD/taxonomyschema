import json
from os.path import basename, splitext, join
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
    Loads a JSONSchema vocabulary definition
    that is serialisable with json.dumps()
    """

    def __init__(self, filepath):
        schema = self._load(filepath)
        self.vocabularyId = schema['properties']['id']['default']
        self.vocabularyName = splitext(basename(filepath))[0]
        self.vocabularyValues = self._map_values(
            schema['properties']['vocabulary']['enum'])

    @staticmethod
    def _map_values(values):
        return [{'valueId': i + 1, 'valueName': v}
                for i, v in enumerate(values)]

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
