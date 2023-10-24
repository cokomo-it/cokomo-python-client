# LearningGoal


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**underlying_competence_base** | [**CompetenceBase**](CompetenceBase.md) |  | [optional] 
**associated_competence_level** | [**CompetenceLevel**](CompetenceLevel.md) |  | [optional] 

## Example

```python
from cokomo.models.learning_goal import LearningGoal

# TODO update the JSON string below
json = "{}"
# create an instance of LearningGoal from a JSON string
learning_goal_instance = LearningGoal.from_json(json)
# print the JSON string representation of the object
print LearningGoal.to_json()

# convert the object into a dict
learning_goal_dict = learning_goal_instance.to_dict()
# create an instance of LearningGoal from a dict
learning_goal_form_dict = learning_goal.from_dict(learning_goal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


