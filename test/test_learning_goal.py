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

from cokomo.models.learning_goal import LearningGoal  # noqa: E501

class TestLearningGoal(unittest.TestCase):
    """LearningGoal unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LearningGoal:
        """Test LearningGoal
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LearningGoal`
        """
        model = LearningGoal()  # noqa: E501
        if include_optional:
            return LearningGoal(
                id = '',
                type = '',
                underlying_competence_base = cokomo.models.competence_base.CompetenceBase(
                    id = '', 
                    title = '', 
                    short_description = '', 
                    type = '', ),
                associated_competence_level = cokomo.models.competence_level.CompetenceLevel(
                    id = '', 
                    type = '', 
                    title = '', 
                    level = 56, )
            )
        else:
            return LearningGoal(
        )
        """

    def testLearningGoal(self):
        """Test LearningGoal"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()