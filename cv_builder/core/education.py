# -*- coding: utf-8 -*-
"""The 'education' module of the 'core' package contains classes related to the Education layer of the data model."""

from typing import Any, Optional

from cv_builder.core.mixin import JSONableMixin


class Education(JSONableMixin):
    """Education: inherit from 'JSONableMixin'.

    Parameters
    ----------
    school : str
        The name of the school responsible for the education.
    degree : str
        The name of the degree awarded.
    start : int
        The start date of the degree, under YYYY format.
    end : int, optional
        The end date fo the degree, under YYYY format, by default None.
    """

    def __init__(
        self, school: str, degree: str, start: int, end: Optional[int] = None
    ) -> None:
        """Initialize the Education class instance."""
        self.school = school
        self.degree = degree
        self.start = start
        self.end = end

    def __setattr__(self, name: str, value: Any):
        """Validate the attributes of the Education class.

        Parameters
        ----------
        name : str
            Name of the attribute.
        value : Any
            Value of the attribute.

        Raises
        ------
        TypeError
            If 'start' or 'end' are not an int.
        AttributeError
            If 'start' or 'end' have and incorrect length.
        TypeError
            If 'school' or 'degree' are not a str.
        """
        if name in ["start", "end"] and value is not None:
            if not isinstance(value, int):
                raise TypeError(f"'{name}' expect an int.")
            elif len(str(value)) != 4:
                raise AttributeError(
                    f"{name} '{value}' has an incorrect length.\nShould be 4 characters in the YYYY format."
                )
        else:
            if value is not None and not isinstance(value, str):
                raise TypeError(f"'{name}' expect a str.")

        self.__dict__[name] = value
