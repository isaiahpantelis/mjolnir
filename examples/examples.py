# Library module(s)
from pprint import pprint
# Other module(s)
from ezdict import EZDict

# A dictionary
d = {'first': 'John',
     'last': 'Doe'}

# Create an "easy" dictionary
ezd = EZDict.from_dict(d)
# Check the contents of the easy dictionary.
print(f'ezd = {ezd}')
# Easily access values
print(f'ezd.first = {ezd.first}')
# Easily set values
ezd.first = 'Mary'
print(f'ezd.first = {ezd.first}')

# A dictionary with a nested dictionary
dd = {'first': 'John',
      'last': 'Doe',
      'phones': {
          'work': 416,
          'home': 523
      }}

ezdd = EZDict.from_dict(dd)

# Check the contents of the easy dictionary.
print(f'ezdd = {ezdd}')
# Access a nested value
print(f'ezdd.phones.work = {ezdd.phones.work}')

# ----------------------------------------------------------------------------------------------------------------------
# Pickling
# ----------------------------------------------------------------------------------------------------------------------
import pickle

pickled = pickle.dumps(ezdd)
unpickled = pickle.loads(pickled)

print(unpickled)

# ----------------------------------------------------------------------------------------------------------------------
# EZConfig examples
# ----------------------------------------------------------------------------------------------------------------------
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