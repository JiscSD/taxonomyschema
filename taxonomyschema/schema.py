import json
from jsonschema import validate
from os.path import basename, join


class Schema:
    """
    Loads a JSONSchema file and exposes validation method
    """
    def __init__(self, filepath):
        self.schema = self._load(filepath)
        self.filename = basename(filepath)

    def _load(self, filepath):
        with open(filepath) as f:
            return json.load(f)

    def _load_instance(self, instance_dir):
        return self._load(self.get_instance_path(instance_dir))

    def get_instance_path(self, instance_dir):
        return join(instance_dir, self.filename)

    def validate(self, instance_dir):
        target = self._load_instance(instance_dir)
        validate(target, self.schema)
