import pytest
from solution import factorial


def test_factorial_zero():
    assert factorial(0) == 1


def test_factorial_one():
    assert factorial(1) == 1


def test_factorial_small():
    assert factorial(5) == 120


def test_factorial_medium():
    assert factorial(7) == 5040


def test_negative_input():
    with pytest.raises(ValueError):
        factorial(-5)
