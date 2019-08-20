from lazywrap import lazywrap
from itertools import *

a = lazywrap(count()) \
    .map(lambda x: x + 1) \
    .chain(count(), count(), count()) \
    .filterfalse(lambda x: x % 2 == 0) \
    .slice(10) \
    .reduce(lambda x, y: x + y)

print(a)
