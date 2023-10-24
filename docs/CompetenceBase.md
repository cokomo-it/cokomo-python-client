# CompetenceBase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**short_description** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from cokomo.models.competence_base import CompetenceBase

# TODO update the JSON string below
json = "{}"
# create an instance of CompetenceBase from a JSON string
competence_base_instance = CompetenceBase.from_json(json)
# print the JSON string representation of the object
print CompetenceBase.to_json()

# convert the object into a dict
competence_base_dict = competence_base_instance.to_dict()
# create an instance of CompetenceBase from a dict
competence_base_form_dict = competence_base.from_dict(competence_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


