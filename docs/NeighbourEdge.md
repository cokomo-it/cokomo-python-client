# NeighbourEdge


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 

## Example

```python
from cokomo.models.neighbour_edge import NeighbourEdge

# TODO update the JSON string below
json = "{}"
# create an instance of NeighbourEdge from a JSON string
neighbour_edge_instance = NeighbourEdge.from_json(json)
# print the JSON string representation of the object
print NeighbourEdge.to_json()

# convert the object into a dict
neighbour_edge_dict = neighbour_edge_instance.to_dict()
# create an instance of NeighbourEdge from a dict
neighbour_edge_form_dict = neighbour_edge.from_dict(neighbour_edge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


