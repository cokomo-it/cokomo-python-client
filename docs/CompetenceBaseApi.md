# cokomo.CompetenceBaseApi

All URIs are relative to *https://cokomo.code4you.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**competence_base_id_details_get**](CompetenceBaseApi.md#competence_base_id_details_get) | **GET** /CompetenceBase/{id}/details | 
[**competence_base_id_get**](CompetenceBaseApi.md#competence_base_id_get) | **GET** /CompetenceBase/{id} | 
[**competence_base_id_neighbours_get**](CompetenceBaseApi.md#competence_base_id_neighbours_get) | **GET** /CompetenceBase/{id}/neighbours | 


# **competence_base_id_details_get**
> CompetenceBase competence_base_id_details_get(id)



### Example

```python
import time
import os
import cokomo
from cokomo.models.competence_base import CompetenceBase
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
    except Exception as e:
        print("Exception when calling CompetenceBaseApi->competence_base_id_details_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**CompetenceBase**](CompetenceBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **competence_base_id_get**
> CompetenceBase competence_base_id_get(id)



### Example

```python
import time
import os
import cokomo
from cokomo.models.competence_base import CompetenceBase
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
        api_response = api_instance.competence_base_id_get(id)
        print("The response of CompetenceBaseApi->competence_base_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompetenceBaseApi->competence_base_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**CompetenceBase**](CompetenceBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **competence_base_id_neighbours_get**
> Neighbour competence_base_id_neighbours_get(id, depth=depth)



### Example

```python
import time
import os
import cokomo
from cokomo.models.neighbour import Neighbour
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
    depth = 10 # int |  (optional) (default to 10)

    try:
        api_response = api_instance.competence_base_id_neighbours_get(id, depth=depth)
        print("The response of CompetenceBaseApi->competence_base_id_neighbours_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompetenceBaseApi->competence_base_id_neighbours_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **depth** | **int**|  | [optional] [default to 10]

### Return type

[**Neighbour**](Neighbour.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

