import pytest
from numpy import array_equal,array
from ..utils import sigmoid


def test_sigmoid_zero():
    assert sigmoid(0) == 0.5

def test_low_bound_sigmoid():
    assert sigmoid(-1000) == 0.9999

def test_high_bound_sigmoid():
    assert sigmoid(100) == 0.0001

def test_sigmoid_array():
    assert array_equal(sigmoid(array([0, -100, 100])), array([0.5, 0.9999, 0.0001]))
