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

### Updating data models

The script `update_data_models.py` can be used to update the data models based on a JSON file containing enumerators.

The `enumeration.json` file can be located in the [rdss-message-api-docs](https://github.com/JiscRDSS/rdss-message-api-docs/blob/master/schemas/enumeration.json).

*Usage*

```
python update_data_models.py path/to/enumeration.json --output_path <optional output location>
```

**Arguments**

 - `file_path` (*required*): Path to json file containing enumerators.
 - `--output_path`: Path to store the output data models (defaults to `output/`).

*Example*

```
python update_data_models.py enumeration.json --output_path datamodels/
```
