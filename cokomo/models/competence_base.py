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

class CompetenceBase(BaseModel):
    """
    CompetenceBase
    """
    id: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    short_description: Optional[StrictStr] = Field(None, alias="shortDescription")
    type: Optional[StrictStr] = None
    __properties = ["id", "title", "shortDescription", "type"]

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
    def from_json(cls, json_str: str) -> CompetenceBase:
        """Create an instance of CompetenceBase from a JSON string"""
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

        # set to None if title (nullable) is None
        # and __fields_set__ contains the field
        if self.title is None and "title" in self.__fields_set__:
            _dict['title'] = None

        # set to None if short_description (nullable) is None
        # and __fields_set__ contains the field
        if self.short_description is None and "short_description" in self.__fields_set__:
            _dict['shortDescription'] = None

        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CompetenceBase:
        """Create an instance of CompetenceBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CompetenceBase.parse_obj(obj)

        _obj = CompetenceBase.parse_obj({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "short_description": obj.get("shortDescription"),
            "type": obj.get("type")
        })
        return _obj

