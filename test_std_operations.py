from std_operations import *

def test_add():
    assert Add(-3.14,1) == -2.14
    assert Add(3**2, 4**2) ==5**2

def test_subtraction():
    assert Subtract(-3,1) == -4
