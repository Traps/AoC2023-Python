import pytest
import util

from solution import day08a

def test_day08a_sample():
    assert day08a.solve(util.get_sample(8, option=0)) == 2
    assert day08a.solve(util.get_sample(8, option=1)) == 6

def test_day08a_challenge():
    assert day08a.solve(util.get_challenge(8)) == 12643