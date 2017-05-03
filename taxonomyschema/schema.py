import json
from jsonschema import validate


class Schema:
    """
    Loads a JSONSchema file and exposes validate method
    """

    def __init__(self, filepath):
        self.schema = self._load(filepath)

    def _load(self, filepath):
        with open(filepath) as f:
            return json.load(f)

    def validate(self, instance_path):
        target = self._load(instance_path)
        validate(target, self.schema)
