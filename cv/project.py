# -*- coding: utf-8 -*-
"""
project.py
Author: Gilson, K.
"""

from typing import List

from .mixin import JSONableMixin


class Project(JSONableMixin):
    """Projects"""

    def __init__(
        self,
        name: str = None,
        redacted: str = None,
        position: str = None,
        start: int = None,
        end: int = None,
        description: List[str] = None,
        activities: List[str] = None,
        confidential: bool = True,
    ):
        self.name = name
        self.redacted = redacted
        self.position = position
        self.start = start
        self.end = end
        self.description = description
        self.activities = activities
        self.confidential = confidential

    def __setattr__(self, name, value):
        if name in ["start", "end"] and value is not None:
            if len(str(value)) != 6:
                raise AttributeError(
                    f"{name} '{value}' has an incorrect lenght.\nShould be 6 characters in the YYYYMM format."
                )

        self.__dict__[name] = value

    # Description
    def add_description(self, new_description):
        if self.description is None:
            self.description = []
        self.description.append(new_description)

    def remove_description(self, old_description):
        self.description.remove(old_description)

    def reorder_description(self, order):
        self.description = [self.description[i] for i in order]

    # Activities
    def add_activity(self, new_activity):
        if self.activities is None:
            self.activities = []
        self.activities.append(new_activity)

    def remove_activity(self, old_activity):
        self.activities.remove(old_activity)

    def reorder_activity(self, order):
        self.activities = [self.activities[i] for i in order]
