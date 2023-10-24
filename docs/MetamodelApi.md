# cokomo.MetamodelApi

All URIs are relative to *https://cokomo.code4you.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metamodel_get**](MetamodelApi.md#metamodel_get) | **GET** /Metamodel | 


# **metamodel_get**
> Metamodel metamodel_get()



### Example

```python
import time
import os
import cokomo
from cokomo.models.metamodel import Metamodel
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
    api_instance = cokomo.MetamodelApi(api_client)

    try:
        api_response = api_instance.metamodel_get()
        print("The response of MetamodelApi->metamodel_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetamodelApi->metamodel_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Metamodel**](Metamodel.md)

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

