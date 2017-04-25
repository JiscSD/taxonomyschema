# taxonomyschema

Script to update taxonomy service API with schemas contained in this repository.



## Usage
```
usage: taxonomyschema [-h] schemas url

Updates Taxonomy Service via HTTP service

positional arguments:
  schemas     path to schemas dir
  url         url of API to POST schemas to

optional arguments:
  -h, --help  show this help message and exit
 ```

## Installation
```
make install
```

## Deployment: TODO
Master branch will autodeploy to production.
Develop branch will autodeploy to staging.

## Development
Create a virtualenv then install requirements:
```
make deps
```

## Lint
```
make lint
```

## Validate json schemas bin script
```
./bin/validate-examples.py
```
