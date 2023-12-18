import pytest
import util

from solution import day12a, day12b

def test_day12a_sample():
    assert day12a.solve(util.get_sample(12)) == 21

def test_day12a_challenge():
    assert day12a.solve(util.get_challenge(12)) == 7260

def test_day12b_sample():
    assert day12b.solve(util.get_sample(12)) == 525152

def test_day12b_challenge():
    assert day12b.solve(util.get_challenge(12)) == 1909291258644