# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rest_api.models.base_model_ import Model
from rest_api import util


class WorkflowTypeVersion(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, workflow_type_version=None):  # noqa: E501
        """WorkflowTypeVersion - a model defined in OpenAPI

        :param workflow_type_version: The workflow_type_version of this WorkflowTypeVersion.  # noqa: E501
        :type workflow_type_version: List[str]
        """
        self.openapi_types = {
            'workflow_type_version': List[str]
        }

        self.attribute_map = {
            'workflow_type_version': 'workflow_type_version'
        }

        self._workflow_type_version = workflow_type_version

    @classmethod
    def from_dict(cls, dikt) -> 'WorkflowTypeVersion':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The WorkflowTypeVersion of this WorkflowTypeVersion.  # noqa: E501
        :rtype: WorkflowTypeVersion
        """
        return util.deserialize_model(dikt, cls)

    @property
    def workflow_type_version(self):
        """Gets the workflow_type_version of this WorkflowTypeVersion.

        an array of one or more acceptable types for the `workflow_type`  # noqa: E501

        :return: The workflow_type_version of this WorkflowTypeVersion.
        :rtype: List[str]
        """
        return self._workflow_type_version

    @workflow_type_version.setter
    def workflow_type_version(self, workflow_type_version):
        """Sets the workflow_type_version of this WorkflowTypeVersion.

        an array of one or more acceptable types for the `workflow_type`  # noqa: E501

        :param workflow_type_version: The workflow_type_version of this WorkflowTypeVersion.
        :type workflow_type_version: List[str]
        """

        self._workflow_type_version = workflow_type_version