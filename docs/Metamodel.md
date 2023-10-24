# Metamodel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**competence_base_types** | [**List[CompetenceBaseType]**](CompetenceBaseType.md) |  | [optional] 
**edge_types** | [**List[EdgeType]**](EdgeType.md) |  | [optional] 

## Example

```python
from cokomo.models.metamodel import Metamodel

# TODO update the JSON string below
json = "{}"
# create an instance of Metamodel from a JSON string
metamodel_instance = Metamodel.from_json(json)
# print the JSON string representation of the object
print Metamodel.to_json()

# convert the object into a dict
metamodel_dict = metamodel_instance.to_dict()
# create an instance of Metamodel from a dict
metamodel_form_dict = metamodel.from_dict(metamodel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


