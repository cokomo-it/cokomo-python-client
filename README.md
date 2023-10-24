# CokomoPythonClient
## 👉 [Please see the CoKoMo documentation for more information.](https://cokomo-it.de/docs/start/api/documentation/)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/cokomo-it/cokomo-python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/cokomo-it/cokomo-python-client.git`)

Then import the package:
```python
import cokomo
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cokomo
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import cokomo
from cokomo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://cokomo.code4you.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cokomo.Configuration(
    host = "https://cokomo.code4you.com"
)



# Enter a context with an instance of the API client
with cokomo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cokomo.CompetenceBaseApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.competence_base_id_details_get(id)
        print("The response of CompetenceBaseApi->competence_base_id_details_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CompetenceBaseApi->competence_base_id_details_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CompetenceBaseApi* | [**competence_base_id_details_get**](docs/CompetenceBaseApi.md#competence_base_id_details_get) | **GET** /CompetenceBase/{id}/details | 
*CompetenceBaseApi* | [**competence_base_id_get**](docs/CompetenceBaseApi.md#competence_base_id_get) | **GET** /CompetenceBase/{id} | 
*CompetenceBaseApi* | [**competence_base_id_neighbours_get**](docs/CompetenceBaseApi.md#competence_base_id_neighbours_get) | **GET** /CompetenceBase/{id}/neighbours | 
*LearningGoalApi* | [**learning_goal_id_details_get**](docs/LearningGoalApi.md#learning_goal_id_details_get) | **GET** /LearningGoal/{id}/details | 
*LearningGoalApi* | [**learning_goal_id_get**](docs/LearningGoalApi.md#learning_goal_id_get) | **GET** /LearningGoal/{id} | 
*MetamodelApi* | [**metamodel_get**](docs/MetamodelApi.md#metamodel_get) | **GET** /Metamodel | 


## Documentation For Models

 - [CompetenceBase](docs/CompetenceBase.md)
 - [CompetenceBaseType](docs/CompetenceBaseType.md)
 - [CompetenceLevel](docs/CompetenceLevel.md)
 - [EdgeType](docs/EdgeType.md)
 - [LearningGoal](docs/LearningGoal.md)
 - [Metamodel](docs/Metamodel.md)
 - [Neighbour](docs/Neighbour.md)
 - [NeighbourEdge](docs/NeighbourEdge.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author

cokomo-team@haw-hamburg.de

