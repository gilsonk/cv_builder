# -*- coding: utf-8 -*-
"""
mixin.py
Author: Gilson, K.
"""


class JSONableMixin(object):
    def to_dict(self, keep_none=True):
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
