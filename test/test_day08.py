import pytest
import util

from solution import day08a, day08b

def test_day08a_sample():
    assert day08a.solve(util.get_sample(8, 'a', option=0)) == 2
    assert day08a.solve(util.get_sample(8, 'a', option=1)) == 6

def test_day08a_challenge():
    assert day08a.solve(util.get_challenge(8)) == 12643

def test_day08b_sample():
    assert day08b.solve(util.get_sample(8, 'b')) == 6

def test_day08b_challenge():
    assert day08b.solve(util.get_challenge(8)) == 13133452426987