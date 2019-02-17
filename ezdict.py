"""
date: 2018-07-29
author: karatheodory@gmail.com

A simple class derived from the python built-in `dict` that allows access to the dictionary values using the syntax
for attributes. Specifically, if `(key, val)` is an item in an `EZdict` `d`, then `val` can be accessed either by
`d[key]` or by `d.key`.

There are obvious limitations, some of which are summarised in the file `examples/oddities.py`.

"""


class EZDict(dict):
    """
    A class derived from the built-in `dict` that allows access to the dictionary values using the dot operator.
    """

    def __init__(self):
        super(EZDict, self).__init__()

    def __getattr__(self, item):
        # print(f'-- Fetching {item}')
        return super(EZDict, self).get(item)

    def __setattr__(self, key, value):
        return super(EZDict, self).__setitem__(key, value)

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, d):
        pass

    @classmethod
    def from_dict(cls, d: dict):

        ezd = EZDict()

        for key, value in d.items():

            if isinstance(value, dict):

                ezd[key] = EZDict.from_dict(value)

            else:

                ezd[key] = value

        return ezd
