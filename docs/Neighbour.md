# Neighbour


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**short_description** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**relation** | [**NeighbourEdge**](NeighbourEdge.md) |  | [optional] 
**neighbours** | [**List[Neighbour]**](Neighbour.md) |  | [optional] 

## Example

```python
from cokomo.models.neighbour import Neighbour

# TODO update the JSON string below
json = "{}"
# create an instance of Neighbour from a JSON string
neighbour_instance = Neighbour.from_json(json)
# print the JSON string representation of the object
print Neighbour.to_json()

# convert the object into a dict
neighbour_dict = neighbour_instance.to_dict()
# create an instance of Neighbour from a dict
neighbour_form_dict = neighbour.from_dict(neighbour_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


