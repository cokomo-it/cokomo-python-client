# cokomo.LearningGoalApi

All URIs are relative to *https://cokomo.code4you.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**learning_goal_id_details_get**](LearningGoalApi.md#learning_goal_id_details_get) | **GET** /LearningGoal/{id}/details | 
[**learning_goal_id_get**](LearningGoalApi.md#learning_goal_id_get) | **GET** /LearningGoal/{id} | 


# **learning_goal_id_details_get**
> LearningGoal learning_goal_id_details_get(id)



### Example

```python
import time
import os
import cokomo
from cokomo.models.learning_goal import LearningGoal
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
    api_instance = cokomo.LearningGoalApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.learning_goal_id_details_get(id)
        print("The response of LearningGoalApi->learning_goal_id_details_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LearningGoalApi->learning_goal_id_details_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**LearningGoal**](LearningGoal.md)

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

# **learning_goal_id_get**
> LearningGoal learning_goal_id_get(id)



### Example

```python
import time
import os
import cokomo
from cokomo.models.learning_goal import LearningGoal
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
    api_instance = cokomo.LearningGoalApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.learning_goal_id_get(id)
        print("The response of LearningGoalApi->learning_goal_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LearningGoalApi->learning_goal_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**LearningGoal**](LearningGoal.md)

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

