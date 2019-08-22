import lazywrap
from itertools import *


def test_map():
    assert lazywrap.of([]).map(lambda x: x + 1).to_list() == []
    assert lazywrap.of([1, 2, 3, 4]).map(lambda x: x + 1).to_list() == [2, 3, 4, 5]


def test_filter():
    assert lazywrap.of([]).filter(lambda x: x > 1).to_list() == []
    assert lazywrap.of([0, 1, 2, 3]).filter(lambda x: x > 1).to_list() == [2, 3]


def test_slice():
    assert lazywrap.of(count()).slice(5).to_list() == [0, 1, 2, 3, 4]
    assert lazywrap.of(count()).slice(10, 15).to_list() == [10, 11, 12, 13, 14]
    assert lazywrap.of(count()).slice(10, 20, 4).to_list() == [10, 14, 18]
