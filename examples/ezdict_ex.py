# Library module(s)
from pprint import pprint
# Other module(s)
from ezdict import EZDict

# ----------------------------------------------------------------------------------------------------------------------
# EZDict examples
# ----------------------------------------------------------------------------------------------------------------------
# A dictionary
d = {'first': 'John',
     'last': 'Doe'}

# Create an easy dict
ezd = EZDict.from_dict(d)
# Check the contents of the easy dictionary.
# print(f'ezd = {ezd}')
# Easily access values
print(f'ezd.first = {ezd.first}')
# Easily set values
ezd.first = 'Mary'
print(f'ezd.first = {ezd.first}')

# A dictionary with a nested dictionary
dd = {'first': 'John',
      'last': 'Doe',
      'phones': {
          'work': "123 456 7890",
          'home': "999 999 9999"
      }}

ezdd = EZDict.from_dict(dd)

# Check the contents of the easy dictionary.
# print(f'ezdd = {ezdd}')
# Access nested values
# print(f'ezdd.first = {ezdd.first}')
print(f'ezdd.phones.work = {ezdd.phones.work}')
print(f'ezdd.phones.home = {ezdd.phones.home}')

# ----------------------------------------------------------------------------------------------------------------------
# Pickling
# ----------------------------------------------------------------------------------------------------------------------
import pickle

pickled = pickle.dumps(ezdd)
unpickled = pickle.loads(pickled)

pprint(unpickled)
