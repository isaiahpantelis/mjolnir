"""
date: 2018-07-29
author: karatheodory@gmail.com

This is a simple class derived from the python built-in `dict`; it's sole purpose is to function as a dictionary, but
also provide access to the dictionary values using the dot operator:

If `(key, val)` is an item in an `EZdict` `d`, then `val` can be accessed either by `d[key]` or by `d.key`.

There are obvious limitations:

    #.  For `d.key` to work `key` can only be such that `d.key` is a legal expression.
    #.  For `d.key` to work *correctly*, `d.key` should refer to the same object as `d[key]`. Think, e.g., of `key`
        being a string containing spaces.
    #.  The function that internally dispatches `d.key` will *intercept method calls*. Therefore, for such method calls
        to continue working with `EZdict` in the same way as with the built-in `dict`, they have to be added as
        key-value pairs: (method name, reference to method implementation)


For example, if ``d`` is an object of type ``EZDict`` and::

    d = {key: value}

then ``value`` can be
accessed using either one of the following two ways:

#. ``d[key]`` (== value)
#. ``d.key`` (== value)

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
