# EdgeType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**abbreviation** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from cokomo.models.edge_type import EdgeType

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeType from a JSON string
edge_type_instance = EdgeType.from_json(json)
# print the JSON string representation of the object
print EdgeType.to_json()

# convert the object into a dict
edge_type_dict = edge_type_instance.to_dict()
# create an instance of EdgeType from a dict
edge_type_form_dict = edge_type.from_dict(edge_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


