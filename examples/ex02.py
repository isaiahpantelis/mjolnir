from pprint import pprint
from configparser import ConfigParser

from ezconfig import EZConfig

fpath = './config.ini'

# # Use #1: get back all sections
# ezcfg = EZConfig(fpath).read()
# print(f'ezcfg.data.cds_folder = {ezcfg.data.cds_folder}')
#
# # Use #2: get back a specific section
# ezcfg = EZConfig(fpath).read().data
# print(f'ezcfg = {ezcfg}')

# Test casting
ezcfg = EZConfig(fpath).read()

for section, conts in ezcfg.items():
    print(f'section: {section} ')
    for key, val in conts.items():
        print(f'    {key}: {val}')
        # print(f'    {type(key)}: {type(val)}')

print(ezcfg.datain.xfolder)