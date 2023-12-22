import pytest
import util

from solution import day16a, day16b

def test_day16a_sample():
    assert day16a.solve(util.get_sample(16)) == 46

def test_day16a_challenge():
    assert day16a.solve(util.get_challenge(16)) == 8389

def test_day16b_sample():
    assert day16b.solve(util.get_sample(16)) == 51

def test_day16b_challenge():
    assert day16b.solve(util.get_challenge(16)) == 8564