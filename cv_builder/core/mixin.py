# -*- coding: utf-8 -*-
"""The 'mixin' module of the 'core' package contains mixin classes used thorough the rest of the package."""

from typing import Any, Dict, Optional


class JSONableMixin(object):
    """Mixin responsible to convert nested classes to a JSON format."""

    def to_dict(self, keep_none: Optional[bool] = True) -> Dict[str, Any]:
        """Return a nested dictionary of the instance attributes.

        Parameters
        ----------
        keep_none : bool, optional
            Whether to keep None values in the dictionary or not, by default True.

        Returns
        -------
        Dict[str, Any]
            The nested dictionary of the instance attributes.

        Raises
        ------
        TypeError
            If keep_none is not bool.
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
