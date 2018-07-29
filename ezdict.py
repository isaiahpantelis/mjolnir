"""
date: 2018-07-29
author: karatheodory@gmail.com

This is a simple class derived from the python built-in `dict`; it's sole purpose is to function as a dictionary but
also provide access to the dictionary values using the dot notation:

If (key, val) is an item in an ezdict d, then `val` can be accessed either by `d[key]` or by `d.key`.

There are obvious limitations:

    #.  For `d.key` to work `key` can only be such that `d.key` is a legal expression.
    #.  For `d.key` to work *correctly*, `d.key` should refer to the same object as `d[key]`. Think, e.g., of `key`
        being a string containing spaces.
    #.  The function that internally dispatches `d.key` will *intercept method calls*. If you want specific methods to
        continue being available,
"""


class EZDict(dict):

    def __init__(self):
        super(EZDict, self).__init__()

    def __getattr__(self, item):
        return super(EZDict, self).get(item)

    def __setattr__(self, key, value):
        return super(EZDict, self).__setitem__(key, value)

    @classmethod
    def from_dict(cls, d: dict):

        ezd = EZDict()

        for key, value in d.items():

            if isinstance(value, dict):

                ezd[key] = EZDict.from_dict(value)

            else:

                ezd[key] = value

        return ezd