from ezdict import EZDict
from pprint import pprint

d = {'one': 1, 'has space': 2, '__repr__': 'muahaha', 'with': 'love'}

print(f'\n-- d')
pprint(d)

ezd = EZDict.from_dict(d)

print(f'\n-- ezd')
pprint(ezd)

# -- CASE #1
print()
print(f"ezd['one'] = {ezd['one']}")
print(f'ezd.one = {ezd.one}')

# -- CASE #2
print()
print(f"ezd['has space'] = {ezd['has space']}")
# print(f"ezd.has space = {ezd.has space}")  # error
# print(f"ezd.'has space' = {ezd.'has space'}")  # error

# -- CASE #3
print()
print(f"ezd['__repr__'] = {ezd['__repr__']}")
print(f"ezd.__repr__ = {ezd.__repr__}")
print(f"ezd.__repr__() = {ezd.__repr__()}")

# -- CASE #4
print()
print(f"ezd['with'] = {ezd['with']}")
# print(f"ezd.with = {ezd.with}")  # error