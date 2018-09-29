# Library module(s)
from pprint import pprint
# Other module(s)
from ezdict import EZDict

# ----------------------------------------------------------------------------------------------------------------------
# EZConfig examples
# ----------------------------------------------------------------------------------------------------------------------
from ezconfig import EZConfig

fpath = './config.ini'

ezcfg = EZConfig(fpath).read()

# Try it out
print(f'ezcfg.section.level1.level2 = {ezcfg.section.level1.level2}')
print(f'ezcfg.section.level1.level2.some_key = {ezcfg.section.level1.level2.some_key}')
print(f'ezcfg.section.level1.yet_another_key = {ezcfg.section.level1.yet_another_key}')

# for section, conts in ezcfg.items():
#     print(f'section: {section} ')
#     for key, val in conts.items():
#         print(f'    {key}: {val}')
#         # print(f'    {type(key)}: {type(val)}')

# ----------------------------------------------------------------------------------------------------------------------
# Read a json file
# ----------------------------------------------------------------------------------------------------------------------
fpath = './config.json'
ezcfg = EZConfig(fpath).read()
print(f'ezcfg.files.paths.data.input = {ezcfg.files.paths.data.input}')
print(f'ezcfg.files.paths.data.output = {ezcfg.files.paths.data.output}')