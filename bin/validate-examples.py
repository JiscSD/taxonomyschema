#!/usr/bin/env python
from glob import glob
import argparse
import os
import sys
from jsonschema import exceptions
sys.path.append(os.getcwd())
from taxonomyschema.schema import Schema  # noqa: E402


def validate_examples(schema, files):
    """
    Validates example JSON files with JSON Schema definitions
    """
    schema = Schema(schema)

    for f in files:
        try:
            schema.validate(f)
        except exceptions.ValidationError as e:
            print('[ERROR]: {filepath} is invalid\n'.format(
                filepath=f
            ))
            print(e)
            raise e


def main(argv=None):
    parser = argparse.ArgumentParser()
    schema_glob = os.path.join(os.getcwd(), 'datamodel', '*.json')
    parser.add_argument('filenames', nargs='*',
                        default=glob(schema_glob),
                        help='JSONSchema files')
    parser.add_argument('-s', '--schema', type=str,
                        default='validation/model.json',
                        help='JSONSchema file path')
    args = parser.parse_args(argv)
    return validate_examples(schema=args.schema, files=args.filenames)


if __name__ == '__main__':
    sys.exit(main())
