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

    def read(self):

        self.cfgparser.read(self.fpath)

        tmp_dict = {}

        for section in self.cfgparser.sections():
            tmp_dict[section] = {key: val for key, val in self.cfgparser[section].items()}

        return EZDict.from_dict(tmp_dict)
