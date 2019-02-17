import configparser
import json
from ezdict import EZDict

# ======================================================================================================================


def _build(d: dict, L: list, data: dict):
    if L:
        if L[0] not in d.keys():
            d[L[0]] = {}
        _build(d[L[0]], L[1:], data)
    else:
        # print(f'd = {d}')
        # print(f'L = {L}')
        d.update(data)

# ======================================================================================================================


def _cast(x):
    """
    Auxiliary function used to cast strings read from the config file to more useful types. For example, it will
    convert any of the strings true, TRUE, True, etc, to True (bool).

    :param x:
    :return:
    """

    # -- At the moment, it is guaranteed that x is a string, however we may want to add a type check in the future
    # -- or raise an exception.

    # Logical
    cases = ['true', 'yes', 'on']
    if x.lower() in cases:
        return True

    cases = ['false', 'no', 'off']
    if x.lower() in cases:
        return False

    try:
        y = float(x)
        return y if '.' in x else int(x)
    except ValueError:
        return x

    # return x

# ======================================================================================================================


class EZConfig:

    def __init__(self, fpath, interpolation='extended', sep='.'):

        self.fpath = fpath
        self.sep = sep
        self._data = None

        ext = fpath.split('.')[-1]

        if ext in ['ini', 'cfg']:

            self.fintype = 'cfg'

            if interpolation == 'extended':
                interpolation_obj = configparser.ExtendedInterpolation()
            else:
                interpolation_obj = configparser._UNSET

            self.cfgparser = configparser.ConfigParser(interpolation=interpolation_obj)

        elif ext in ['json']:

            self.fintype = 'json'

    # ------------------------------------------------------------------------------------------------------------------

    def _read(self):
        """
        Called by `data.setter`; reads a file using the configparser and assigns the result to `self._data`.
        """

        JSON = 'json'

        if self.fintype != JSON:

            # Read the config file using the objects config parser that was created during initialisation.
            self.cfgparser.read(self.fpath)

            # Start building the return value of the function.
            result = {}

            for section in self.cfgparser.sections():
                _build(result, section.split(self.sep),
                       {key: _cast(val) for key, val in self.cfgparser[section].items()})

            self._data = EZDict.from_dict(result)

        else:

            self._data = EZDict.from_dict(json.load(open(self.fpath, 'r')))

    # ------------------------------------------------------------------------------------------------------------------

    @property
    def data(self):
        if self._data is not None:
            # print('-- File already loaded')
            return self._data
        else:
            # print('-- Loading file')
            self._read()
            return self._data

    @data.setter
    def data(self):
        pass
