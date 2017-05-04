[![Build Status](https://travis-ci.org/JiscRDSS/taxonomyschema.svg?branch=develop)](https://travis-ci.org/JiscRDSS/taxonomyschema)

# taxonomyschema
Updates the taxonomy service API with datamodels contained in this repository.


### Branch Convention
Branches map to environments:
- Master branch will deploy to production.
- Develop branch will deploy to staging.


### CLI Installation
```
make install
```


### CLI Usage
```
usage: taxonomyschema [-h] models url

Updates Taxonomy Service datamodels via API call

positional arguments:
  models      path to models directory
  url         url of API to POST models to

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

### Validate the datamodels using JSONSchema
```
./bin/validate-datamodels.py
```
