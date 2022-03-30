# -*- coding: utf-8 -*-
"""
language.py
Author: Gilson, K.
"""

from .mixin import JSONableMixin


class Language(JSONableMixin):
    """Language"""

    def __init__(self, name: str, irl_scale: str = None, cefr_level: str = None):
        self.name = name
        self.irl_scale = irl_scale
        self.cefr_level = cefr_level

    def __setattr__(self, name, value):
        # Validation
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
