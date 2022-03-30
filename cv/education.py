# -*- coding: utf-8 -*-
"""
education.py
Author: Gilson, K.
"""

from .mixin import JSONableMixin


class Education(JSONableMixin):
    """Education"""

    def __init__(self, school: str, degree: str, start: int, end: int = None):
        self.school = school
        self.degree = degree
        self.start = start
        self.end = end

    def __setattr__(self, name, value):
        if name in ["start", "end"] and value is not None:
            if len(str(value)) != 4:
                raise AttributeError(
                    f"{name} '{value}' has an incorrect lenght.\nShould be 6 characters in the YYYYMM format."
                )

        self.__dict__[name] = value
