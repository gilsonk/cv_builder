# -*- coding: utf-8 -*-
"""
education.py
Author: Gilson, K.
"""

from typing import Any

from .mixin import JSONableMixin


class Education(JSONableMixin):
    """Education: inherit from 'JSONableMixin'.

    Attributes:
        school (str): the name of the school responsible for the education.
        degree (str): the name of the degree awarded.
        start (int): the start date of the degree, under YYYY format.
        end (int, optional): the end date fo the degree, under YYYY format. Defaults to None.
    """

    def __init__(self, school: str, degree: str, start: int, end: int = None) -> None:
        """Initialize the Education class instance.

        Args:
            school (str): the name of the school responsible for the education.
            degree (str): the name of the degree awarded.
            start (int): the start date of the degree, under YYYY format.
            end (int, optional): the end date fo the degree, under YYYY format. Defaults to None.
        """
        self.school = school
        self.degree = degree
        self.start = start
        self.end = end

    def __setattr__(self, name: str, value: Any):
        """Validate the attributes of the Education class.

        Args:
            name (str): name of the attribute.
            value (Any): value of the attribute.

        Raises:
            TypeError: if 'start' or 'end' are not an int.
            AttributeError: if 'start' or 'end' have and incorrect length.
            TypeError: if 'school' or 'degree' are not a str.
        """
        if name in ["start", "end"] and value is not None:
            if not isinstance(value, int):
                raise TypeError(f"'{name}' expect an int.")
            elif len(str(value)) != 4:
                raise AttributeError(
                    f"{name} '{value}' has an incorrect lenght.\nShould be 4 characters in the YYYY format."
                )
        else:
            if value is not None and not isinstance(value, str):
                raise TypeError(f"'{name}' expect a str.")

        self.__dict__[name] = value
