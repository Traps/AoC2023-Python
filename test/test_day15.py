import pytest
import util

from solution import day15a, day15b

def test_day15a_sample():
    assert day15a.solve(util.get_sample(15)) == 1320

def test_day15a_challenge():
    assert day15a.solve(util.get_challenge(15)) == 504449

def test_day15b_sample():
    assert day15b.solve(util.get_sample(15)) == 145

def test_day15b_challenge():
    assert day15b.solve(util.get_challenge(15)) == 262044