import pytest
import util

from solution import day04a, day04b

def test_day04a_sample():
    assert day04a.solve(util.get_sample(4)) == 13

def test_day04a_challenge():
    assert day04a.solve(util.get_challenge(4)) == 24175

def test_day04b_sample():
    assert day04b.solve(util.get_sample(4)) == 30

def test_day04b_challenge():
    assert day04b.solve(util.get_challenge(4)) == 18846301