import pytest
import util

from solution import day01a, day01b

def test_day01a_sample():
    assert day01a.solve(util.get_sample(1, 'a')) == 142

def test_day01a_challenge():
    assert day01a.solve(util.get_challenge(1)) == 55816

def test_day01b_sample():
    assert day01b.solve(util.get_sample(1, 'b')) == 281

def test_day01b_challenge():
    assert day01b.solve(util.get_challenge(1)) == 54980