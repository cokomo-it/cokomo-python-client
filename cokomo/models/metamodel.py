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


from typing import List, Optional
from pydantic import BaseModel, Field, conlist
from cokomo.models.competence_base_type import CompetenceBaseType
from cokomo.models.edge_type import EdgeType

class Metamodel(BaseModel):
    """
    Metamodel
    """
    competence_base_types: Optional[conlist(CompetenceBaseType)] = Field(None, alias="competenceBaseTypes")
    edge_types: Optional[conlist(EdgeType)] = Field(None, alias="edgeTypes")
    __properties = ["competenceBaseTypes", "edgeTypes"]

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
    def from_json(cls, json_str: str) -> Metamodel:
        """Create an instance of Metamodel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in competence_base_types (list)
        _items = []
        if self.competence_base_types:
            for _item in self.competence_base_types:
                if _item:
                    _items.append(_item.to_dict())
            _dict['competenceBaseTypes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in edge_types (list)
        _items = []
        if self.edge_types:
            for _item in self.edge_types:
                if _item:
                    _items.append(_item.to_dict())
            _dict['edgeTypes'] = _items
        # set to None if competence_base_types (nullable) is None
        # and __fields_set__ contains the field
        if self.competence_base_types is None and "competence_base_types" in self.__fields_set__:
            _dict['competenceBaseTypes'] = None

        # set to None if edge_types (nullable) is None
        # and __fields_set__ contains the field
        if self.edge_types is None and "edge_types" in self.__fields_set__:
            _dict['edgeTypes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Metamodel:
        """Create an instance of Metamodel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Metamodel.parse_obj(obj)

        _obj = Metamodel.parse_obj({
            "competence_base_types": [CompetenceBaseType.from_dict(_item) for _item in obj.get("competenceBaseTypes")] if obj.get("competenceBaseTypes") is not None else None,
            "edge_types": [EdgeType.from_dict(_item) for _item in obj.get("edgeTypes")] if obj.get("edgeTypes") is not None else None
        })
        return _obj


