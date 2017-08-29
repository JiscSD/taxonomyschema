"""Script to convert the enumeration.json to the data model."""
import json
import argparse
import os
import errno


def main():
    """Script entrypoint."""
    args = _parse_args()
    with open(args.file_path) as f:
        enum_dict = json.load(f)
        _ensure_dir_exists(args.output_path)
        _process_enum_dict(enum_dict, args.output_path)


def _create_model(output_path, vid, name, enum_list):
    """Create a new model item."""

    vocab_values = []
    value_id = 1
    for val in enum_list:
        vocab_values.append({
            'valueId': value_id,
            'valueName': val
        })
        value_id += 1

    model_dict = {
        "vocabularyId": vid,
        "vocabularyName": name,
        "vocabularyValues": vocab_values
    }

    full_path = os.path.join(output_path, '{}.json'.format(name))
    with open(full_path, 'w') as outfile:
        json_str = json.dumps(
            model_dict, sort_keys=True, indent=4, separators=(',', ': '))
        outfile.write(json_str)


def _process_enum_dict(enum_dict, output_path):
    """Process the enum dict and output the models to given path."""
    definitions = enum_dict['definitions']
    vocab_id = 1
    for k, v in definitions.items():
        enum_list = v['enum']
        _create_model(output_path, vocab_id, k, enum_list)
        vocab_id += 1


def _ensure_dir_exists(path):
    """Ensure that the directory at given path exists."""
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def _parse_args():
    """Parse the arguments provided for this script."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'file_path',
        help='Path to file containing enums.'
    )
    parser.add_argument(
        '--output_path',
        default='output/',
        help='Path to output the data models.'
    )
    return parser.parse_args()


if __name__ == '__main__':
    main()
