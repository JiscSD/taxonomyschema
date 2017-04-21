from jsonschema import exceptions
from taxonomyschema.schema import Schema


def validate_examples(files, valid_dir, invalid_dir):

    for f in files:
        schema = Schema(f)

        # check valid examples
        try:
            schema.validate(valid_dir)
        except exceptions.ValidationError as e:
            print('[ERROR]: {filepath} is invalid\n'.format(
                filepath=schema.get_instance_path(valid_dir)
            ))
            print(e)
            raise e

        # check invalid examples
        try:
            schema.validate(invalid_dir)
            print('[ERROR]: {filepath} should be invalid\n'.format(
                filepath=schema.get_instance_path(valid_dir)
            ))
            raise
        except exceptions.ValidationError:
            pass
