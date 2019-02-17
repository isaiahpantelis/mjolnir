# -- Library module(s)
from pprint import pprint
# -- Project module(s)
from ezdict import EZDict

# ----------------------------------------------------------------------------------------------------------------------
# EZConfig examples
# ----------------------------------------------------------------------------------------------------------------------
from ezconfig import EZConfig

# ----------------------------------------------------------------------------------------------------------------------
# EZConfig examples
# ----------------------------------------------------------------------------------------------------------------------
# -- Read .ini file
print('\n-- .ini example\n')

fpath = './config.ini'

ezcfg = EZConfig(fpath).data

# pprint(ezcfg)

print(f'ezcfg.input = {ezcfg.input}')
print(f'ezcfg.output = {ezcfg.output}')
print(f'ezcfg.output.db = {ezcfg.output.db}')

# -- Read a json file
print('\n-- .json example\n')

fpath = './config.json'
ezcfg = EZConfig(fpath).data
print(f'ezcfg.db.ip = {ezcfg.db.ip}')

# ----------------------------------------------------------------------------------------------------------------------
# EZDict examples
# ----------------------------------------------------------------------------------------------------------------------
print('\n-- EZDict examples\n')

# -- A dictionary
d = {'first': 'John',
     'last': 'Doe'}

# -- Create an easy dict
ezd = EZDict.from_dict(d)

# Check the contents of the easy dictionary.
pprint(ezd)

# -- Easily access values
print(f'ezd.first = {ezd.first}')

# -- Easily set values
ezd.first = 'Mary'
print(f'ezd.first = {ezd.first}')

# -- A dictionary with a nested dictionary
dd = {'first': 'John',
      'last': 'Doe',
      'phones': {
          'work': "123 456 7890",
          'home': "999 999 9999"
      }}

ezdd = EZDict.from_dict(dd)

# -- Check the contents of the easy dictionary.
print(ezdd)

# -- Access nested values
print(f'ezdd.phones.work = {ezdd.phones.work}')
print(f'ezdd.phones.home = {ezdd.phones.home}')

# ----------------------------------------------------------------------------------------------------------------------
# Pickling
# ----------------------------------------------------------------------------------------------------------------------
import pickle

pickled = pickle.dumps(ezdd)
unpickled = pickle.loads(pickled)

print('\n-- unpickled:')
pprint(unpickled)