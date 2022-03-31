# -*- coding: utf-8 -*-
"""
language.py
Author: Gilson, K.
"""

from typing import Any

from .mixin import JSONableMixin


class Language(JSONableMixin):
    """Language: inherit from 'JSONableMixin'.

    Attributes:
        name (str): language name.
        irl_scale (str, optional): IRL Scale level of competence. Defaults to None.
        cefr_level (str, optional): CEFR Level of competence. Defaults to None.
    """

    def __init__(
        self, name: str, irl_scale: str = None, cefr_level: str = None
    ) -> None:
        """Initialize the Language class instance.

        Args:
            name (str): language name.
            irl_scale (str, optional): IRL Scale level of competence. Defaults to None.
            cefr_level (str, optional): CEFR Level of competence. Defaults to None.
        """
        self.name = name
        self.irl_scale = irl_scale
        self.cefr_level = cefr_level

    def __setattr__(self, name: str, value: Any) -> None:
        """Validate the attributes of the Language class.

        Args:
            name (str): name of the attribute.
            value (Any): value of the attribute.

        Raises:
            TypeError: if a value is not a str.
            AttributeError: if the irl_scale value is unknown.
            AttributeError: if the cefr_level value is unknown.
        """
        # Validation
        if value is not None and not isinstance(value, str):
            raise TypeError(f"'{name}' expect a str.")

        if name == "irl_scale" and value is not None:
            irl_list = [
                "No Proficiency",
                "Elementary Proficiency",
                "Limited Working Proficiency",
                "Professional Working Proficiency",
                "Full Professional Proficiency",
                "Bilingual",
                "Native",
            ]
            if value.title() not in irl_list:
                raise AttributeError(
                    f"IRL Scale '{value}' unknown.\nShould be part of list:\n{irl_list}"
                )
        elif name == "cefr_level" and value is not None:
            cefr_list = [
                "A1",
                "A2",
                "B1",
                "B2",
                "C1",
                "C2",
            ]
            if value.upper() not in cefr_list:
                raise AttributeError(
                    f"CEFR Level '{value}' unknown.\nShould be part of list:\n{cefr_list}"
                )

        # Set
        if value is None:
            self.__dict__[name] = value
        else:
            if name == "irl_scale":
                self.__dict__[name] = value.title()
            elif name == "cefr_level":
                self.__dict__[name] = value.upper()
            else:
                self.__dict__[name] = value
