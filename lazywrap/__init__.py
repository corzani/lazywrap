from itertools import *
from functools import *


def lazywrap(__iterator):
    return LazyWrap(__iterator)


class LazyWrap:
    def __set_op(self, operation):
        self.__iterator = operation
        return self

    def __init__(self, __iterator):
        self.__iterator = __iterator

    def map(self, __function):
        return self.__set_op(map(__function, self.__iterator))

    def filter(self, __function):
        return self.__set_op(filter(__function, self.__iterator))

    def filterfalse(self, __function):
        return self.__set_op(filterfalse(__function, self.__iterator))

    def to_iterator(self):
        return self.__iterator

    def to_list(self):
        return list(self.__iterator)

    def slice(self, *args, **kwargs):
        return self.__set_op(islice(self.__iterator, *args, **kwargs))

    def dropwhile(self, predicate):
        return self.__set_op(dropwhile(predicate, self.__iterator))

    def takewhile(self, predicate):
        return self.__set_op(takewhile(predicate, self.__iterator))

    def chain(self, *iterables):
        return self.__set_op(chain(self.__iterator, *iterables))

    def reduce(self, __function, *args, **kwargs):
        return reduce(__function, self.__iterator, *args, **kwargs)
