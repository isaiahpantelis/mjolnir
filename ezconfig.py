import configparser
from ezdict import EZDict


class EZConfig:

    def __init__(self, fpath, interpolation='extended', sep='/'):

        if interpolation == 'extended':
            interpolation_obj = configparser.ExtendedInterpolation()
        else:
            interpolation_obj = configparser._UNSET

        self.cfgparser = configparser.ConfigParser(interpolation=interpolation_obj)
        self.fpath = fpath

    def _cast(self, x):
        """
        Auxiliary function used to cast strings read from the config file to more useful types. For example, it will
        convert any of the strings true, TRUE, True, etc, to True (bool).

        :param x:
        :return:
        """

        # At the moment, it is guaranteed that x is a string, however we may want to add a check in the future in case
        # unexpected uses.

        # Logical
        cases = ['true', 'yes', 'on']
        if x.lower() in cases:
            return True

        cases = ['false', 'no', 'off']
        if x.lower() in cases:
            return False

        try:
            y = float(x)
            return y
        except ValueError:
            return x

        return x

    def read(self):
        """
        It returns a new object instead of adding data to self. The reason is that if the data read from the config file
        were added to self as a dictionary, then access with the '.' operator would involve one more arbitrarily named
        variable: self.X = ...

        :return:
        """

        # Read the config file using the objects config parser that was created during initialisation.
        self.cfgparser.read(self.fpath)

        # Start building the return value of the function.
        tmp_dict = {}

        for section in self.cfgparser.sections():
            tmp_dict[section] = {key: self._cast(val) for key, val in self.cfgparser[section].items()}

        return EZDict.from_dict(tmp_dict)
