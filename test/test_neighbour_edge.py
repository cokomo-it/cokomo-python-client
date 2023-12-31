# coding: utf-8

"""
    Cokomo Public Api

    Public API Documentation for Cokomo system

    The version of the OpenAPI document: v1
    Contact: cokomo-team@haw-hamburg.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cokomo.models.neighbour_edge import NeighbourEdge  # noqa: E501

class TestNeighbourEdge(unittest.TestCase):
    """NeighbourEdge unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NeighbourEdge:
        """Test NeighbourEdge
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NeighbourEdge`
        """
        model = NeighbourEdge()  # noqa: E501
        if include_optional:
            return NeighbourEdge(
                id = '',
                type = '',
                direction = ''
            )
        else:
            return NeighbourEdge(
        )
        """

    def testNeighbourEdge(self):
        """Test NeighbourEdge"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
