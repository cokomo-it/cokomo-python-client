# CompetenceLevel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**level** | **int** |  | [optional] 

## Example

```python
from cokomo.models.competence_level import CompetenceLevel

# TODO update the JSON string below
json = "{}"
# create an instance of CompetenceLevel from a JSON string
competence_level_instance = CompetenceLevel.from_json(json)
# print the JSON string representation of the object
print CompetenceLevel.to_json()

# convert the object into a dict
competence_level_dict = competence_level_instance.to_dict()
# create an instance of CompetenceLevel from a dict
competence_level_form_dict = competence_level.from_dict(competence_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


