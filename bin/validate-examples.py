#!/usr/bin/env python
from glob import glob
from jsonschema import exceptions
import argparse
import os
import sys
sys.path.append(os.getcwd())
from taxonomyschema.schema import Schema


def check_examples(files, valid_dir, invalid_dir):

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


def run(argv=None):
    schema_glob = os.path.join(os.getcwd(), 'datamodel', '*')
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', default=glob(schema_glob), help='JSONSchema files')
    parser.add_argument('valid', nargs='*', default='examples/valid', help='Valid files directory')
    parser.add_argument('invalid', nargs='*', default='examples/invalid', help='Valid files directory')
    args = parser.parse_args(argv)
    return check_examples(args.filenames, args.valid, args.invalid)


if __name__ == '__main__':
    sys.exit(run())
