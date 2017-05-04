#!/usr/bin/env python3
import argparse
import json
from taxonomyschema.request import Requestor
from taxonomyschema.vocabulary import VocabularyEncoder, VocabularyManifest
from requests.exceptions import HTTPError


def run(models_dir, url):

    r = Requestor(url)
    data = json.dumps(VocabularyManifest(models_dir), cls=VocabularyEncoder)

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


def main():
    parser = argparse.ArgumentParser(
        description=(
            'Updates Taxonomy Service datamodels via API call'
        )
    )
    parser.add_argument(
        'models',
        type=str,
        default='datamodels',
        help='path to models directory'
    )
    parser.add_argument(
        'url',
        type=str,
        help='url of API to POST models to'
    )
    args = parser.parse_args()

    run(models_dir=args.models, url=args.url)


if __name__ == '__main__':
    main()
