from pprint import pprint
from configparser import ConfigParser

from ezconfig import EZConfig

fpath = './config.ini'

ezcfg = EZConfig(fpath)
pprint(ezcfg.read())
