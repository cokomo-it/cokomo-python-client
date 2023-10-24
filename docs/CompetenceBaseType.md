# CompetenceBaseType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**abbreviation** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from cokomo.models.competence_base_type import CompetenceBaseType

# TODO update the JSON string below
json = "{}"
# create an instance of CompetenceBaseType from a JSON string
competence_base_type_instance = CompetenceBaseType.from_json(json)
# print the JSON string representation of the object
print CompetenceBaseType.to_json()

# convert the object into a dict
competence_base_type_dict = competence_base_type_instance.to_dict()
# create an instance of CompetenceBaseType from a dict
competence_base_type_form_dict = competence_base_type.from_dict(competence_base_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


