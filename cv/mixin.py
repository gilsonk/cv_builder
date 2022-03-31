# -*- coding: utf-8 -*-
"""
mixin.py
Author: Gilson, K.
"""

from typing import Optional


class JSONableMixin(object):
    """JSONableMixin: mixin for nested dictionaries objects."""

    def to_dict(self, keep_none: Optional[bool] = True) -> dict:
        """Return a nested dictionary of the instance attributes.

        Args:
            keep_none (bool, optional): whether to keep None values in the dictionary or not. Defaults to True.

        Raises:
            TypeError: if keep_none is not bool.

        Returns:
            dict: the nested dictionary of the instance attributes.
        """
        if not isinstance(keep_none, bool):
            raise TypeError("'keep_none' expect a bool.")

        dic = {}
        for key, value in self.__dict__.items():
            if isinstance(value, JSONableMixin):
                dic[key] = value.to_dict(keep_none)
            elif isinstance(value, list):
                lst = []
                for item in value:
                    if isinstance(item, JSONableMixin):
                        lst.append(item.to_dict(keep_none))
                    else:
                        if item is not None or keep_none == True:
                            lst.append(item)

                if lst or keep_none == True:
                    dic[key] = lst
            else:
                if value is not None or keep_none == True:
                    dic[key] = value

        return dic
