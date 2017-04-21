import json
from os.path import basename, splitext


class VocabularyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, Vocabulary):
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


# url = "http://localhost:8080"
# data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
# headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
# r = requests.post(url, data=json.dumps(data), headers=headers)
