[![Build Status](https://travis-ci.org/JiscRDSS/taxonomyschema.svg?branch=develop)](https://travis-ci.org/JiscRDSS/taxonomyschema)

# taxonomyschema
Updates the taxonomy service API with schemas contained in this repository.


### Branching Convention
Branches map to environments:
- Master branch will deploy to production.
- Develop branch will deploy to staging.


### CLI Installation
```
make install
```


### CLI Usage
```
usage: taxonomyschema [-h] schemas url

Updates Taxonomy Service via HTTP service

positional arguments:
  schemas     path to schemas dir
  url         url of API to POST schemas to

optional arguments:
  -h, --help  show this help message and exit
 ```





-----------------------------------------------------------

## Developer Setup

Create a virtualenv then install requirements:
```
make deps
```

### Test
```
make lint
```

### Lint
```
make lint
```

### Validate example JSON schemas
```
./bin/validate-examples.py
```
