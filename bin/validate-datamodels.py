#!/usr/bin/env python

from jsonschema import validate
from collections import namedtuple
import glob
import json


Config = namedtuple('Config', 'schema_dir instance_pass_dir instance_fail_dir')
config = Config('datamodel', 'examples/valid', 'examples/invalid')


def check_examples(c):

    for f in glob('%s/*'.format(c.schema_dir)):
        with open(f) as schema:
            validate(json.loads(schema), )
