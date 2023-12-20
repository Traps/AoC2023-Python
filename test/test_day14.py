import pytest
import util

from solution import day14a, day14b

def test_day14a_sample():
    assert day14a.solve(util.get_sample(14)) == 136

def test_day14a_challenge():
    assert day14a.solve(util.get_challenge(14)) == 106517

def test_day14b_sample():
    assert day14b.solve(util.get_sample(14)) == 64

def test_day14b_challenge():
    assert day14b.solve(util.get_challenge(14)) == 79723