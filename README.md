# Lazy Wrap

A simple wrap around Python's itertools that makes simple chaining common operations like `map`,
 `filter`, `reduce`, `filterfalse`, `slice`, `dropwhile`, `takewhile`, `dropwhile` and `chain`.

Lazywrap can be built on top of every iterable object:

```python
from lazywrap import lazywrap
from itertools import count

x = lazywrap([1,2,3,4]) # Finite iterators
y = lazywrap('hello!')
z = lazywrap((x % 10 for x in count())) # Infinite iterators
```

## examples

```python
import lazywrap
from operator import add

message = lazywrap.of('HELLO WARP').slice(5).chain(' ', 'world').map(lambda ch: ch.lower()).reduce(add)
print(message) # hello world
```

```python
import operator
import lazywrap
from itertools import count


def is_even(x):
    return x % 2 == 0


something = lazywrap.of(count()) \
    .map(lambda x: x + 1) \
    .filter(lambda x: x > 10) \
    .filterfalse(is_even) \
    .chain(count(50)) \
    .slice(30) \
    .reduce(operator.add)

# or .to_list()
# or .to_iterator()

print(something)
```