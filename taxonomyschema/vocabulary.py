import json

GIT_TO_HTTP = {
    'D': 'DELETE',
    'A': 'POST',
    'M': 'PUT'
}


class VocabularyFactory:
    def __init__(self, git_status, filepath):
        self.http_method = GIT_TO_HTTP[git_status]
        self.filepath = filepath

    def _build_object(self):
        if self.http_method != 'DELETE':
            with open(self.filepath, 'r') as f:
                f_contents = json.load(f)
        return f_contents

    # def _extract_schema_values():
