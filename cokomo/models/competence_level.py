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
from pydantic import BaseModel, StrictInt, StrictStr

class CompetenceLevel(BaseModel):
    """
    CompetenceLevel
    """
    id: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    level: Optional[StrictInt] = None
    __properties = ["id", "type", "title", "level"]

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
    def from_json(cls, json_str: str) -> CompetenceLevel:
        """Create an instance of CompetenceLevel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        # set to None if title (nullable) is None
        # and __fields_set__ contains the field
        if self.title is None and "title" in self.__fields_set__:
            _dict['title'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CompetenceLevel:
        """Create an instance of CompetenceLevel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CompetenceLevel.parse_obj(obj)

        _obj = CompetenceLevel.parse_obj({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "title": obj.get("title"),
            "level": obj.get("level")
        })
        return _obj


