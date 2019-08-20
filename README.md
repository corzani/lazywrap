# Lazy Wrap

A simple wrap around Python's itertools.

```python
import operator

from lazywrap import lazywrap
from itertools import count


def is_even(x):
    return x % 2 == 0


something = lazywrap(count()) \
    .map(lambda x: x + 1) \
    .filter(lambda x: x > 10) \
    .filterfalse(is_even) \
    .chain(count(50)) \
    .slice(30) \
    .reduce(operator.add)

# or   .to_list()
# or .to_iterator()

print(something)
```