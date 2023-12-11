import pytest
import util

from solution import day09a, day09b

def test_day09a_sample():
    assert day09a.solve(util.get_sample(9)) == 114

def test_day09a_challenge():
    assert day09a.solve(util.get_challenge(9)) == 2174807968

def test_day09b_sample():
    assert day09b.solve(util.get_sample(9)) == 2

def test_day09b_challenge():
    assert day09b.solve(util.get_challenge(9)) == 1208