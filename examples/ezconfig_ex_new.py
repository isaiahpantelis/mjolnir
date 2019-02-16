# -- Library module(s)
from pprint import pprint
# -- Project module(s)
from ezdict import EZDict

# ----------------------------------------------------------------------------------------------------------------------
# EZConfig examples
# ----------------------------------------------------------------------------------------------------------------------
from ezconfig import EZConfig

# ----------------------------------------------------------------------------------------------------------------------
# Read ini file
# ----------------------------------------------------------------------------------------------------------------------
print('\n-- .ini example\n')

fpath = './config.ini'

ezcfg = EZConfig(fpath).data

# pprint(ezcfg)

print(f'ezcfg.data.db = {ezcfg.db}')
print(f'ezcfg.data.db.port = {ezcfg.db.port}')

# -- Try it out

# ----------------------------------------------------------------------------------------------------------------------
# Read a json file
# ----------------------------------------------------------------------------------------------------------------------
print('\n-- json example\n')

fpath = './config.json'
ezcfg = EZConfig(fpath).data
print(f'ezcfg.files.paths.data.input = {ezcfg.files.paths.data.input}')
print(f'ezcfg.files.paths.data.output = {ezcfg.files.paths.data.output}')