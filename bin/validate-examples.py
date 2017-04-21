#!/usr/bin/env python
from glob import glob
import argparse
import os
import sys
sys.path.append(os.getcwd())
from taxonomyschema.validate import validate_examples  # noqa: E402


def run(argv=None):
    parser = argparse.ArgumentParser()
    schema_glob = os.path.join(os.getcwd(), 'datamodel', '*.json')
    parser.add_argument('filenames', nargs='*',
                        default=glob(schema_glob), help='JSONSchema files')
    parser.add_argument('valid', nargs='*',
                        default='examples/valid', help='Valid directory')
    parser.add_argument('invalid', nargs='*',
                        default='examples/invalid', help='Invalid directory')
    args = parser.parse_args(argv)
    return validate_examples(args.filenames, args.valid, args.invalid)


if __name__ == '__main__':
    sys.exit(run())
