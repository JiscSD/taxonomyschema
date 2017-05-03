#!/usr/bin/env python3
import argparse
import json
from taxonomyschema.request import Requestor
from taxonomyschema.vocabulary import VocabularyEncoder, VocabularyManifest
from requests.exceptions import HTTPError
from os import path, makedirs


def run(schema_dir, url):

    r = Requestor(url)
    data = json.dumps(VocabularyManifest(schema_dir), cls=VocabularyEncoder)

    try:
        resp = r.update_service(data)
    except HTTPError:
        resp_json = resp.json()
        if 'error' in resp_json:
            print('[ERROR]: API update failed')
            for e in resp_json['error']:
                print('code: {}'.format(getattr(e, 'code', '')))
                print('message: {}'.format(getattr(e, 'message', '')))
                print('')


def writemodels(in_dir, out_dir):

    if not path.exists(out_dir):
        makedirs(out_dir)

    for model in VocabularyManifest(in_dir).manifest:
        filename = path.join(out_dir, '{}.json'.format(model.vocabularyName))
        with open(filename, 'w') as f:
            json.dump(model, f, cls=VocabularyEncoder,
                      sort_keys=True, indent=4)


def main():
    parser = argparse.ArgumentParser(
        description=(
            'Updates Taxonomy Service datamodels via API call'
        )
    )
    parser.add_argument(
        'models',
        type=str,
        default='datamodel',
        help='path to models directory'
    )
    parser.add_argument(
        'outdir',
        type=str,
        default='outdir',
        help='path to out directory'
    )
    # parser.add_argument(
    #     'url',
    #     type=str,
    #     help='url of API to POST models to'
    # )
    args = parser.parse_args()
    # run(schema_dir=args.models, url=args.url)
    writemodels(in_dir=args.models, out_dir=args.outdir)


if __name__ == '__main__':
    main()
