# coding: utf-8

"""
    Cokomo Public Api

    ## 👉 [Please see the CoKoMo documentation for more information.](https://cokomo-it.de/docs/start/api/documentation/)

    The version of the OpenAPI document: v1
    Contact: cokomo-team@haw-hamburg.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from cokomo.models.competence_base import CompetenceBase
from cokomo.models.competence_level import CompetenceLevel

class LearningGoal(BaseModel):
    """
    LearningGoal
    """
    id: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    underlying_competence_base: Optional[CompetenceBase] = Field(None, alias="underlyingCompetenceBase")
    associated_competence_level: Optional[CompetenceLevel] = Field(None, alias="associatedCompetenceLevel")
    __properties = ["id", "type", "underlyingCompetenceBase", "associatedCompetenceLevel"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> LearningGoal:
        """Create an instance of LearningGoal from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of underlying_competence_base
        if self.underlying_competence_base:
            _dict['underlyingCompetenceBase'] = self.underlying_competence_base.to_dict()
        # override the default output from pydantic by calling `to_dict()` of associated_competence_level
        if self.associated_competence_level:
            _dict['associatedCompetenceLevel'] = self.associated_competence_level.to_dict()
        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LearningGoal:
        """Create an instance of LearningGoal from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LearningGoal.parse_obj(obj)

        _obj = LearningGoal.parse_obj({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "underlying_competence_base": CompetenceBase.from_dict(obj.get("underlyingCompetenceBase")) if obj.get("underlyingCompetenceBase") is not None else None,
            "associated_competence_level": CompetenceLevel.from_dict(obj.get("associatedCompetenceLevel")) if obj.get("associatedCompetenceLevel") is not None else None
        })
        return _obj


