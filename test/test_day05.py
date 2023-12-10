import pytest
import util

from solution import day05a, day05b

def test_day05a_sample():
    assert day05a.solve(util.get_sample(5)) == 35

def test_day05a_challenge():
    assert day05a.solve(util.get_challenge(5)) == 318728750

def test_day05b_sample():
    assert day05b.solve(util.get_sample(5)) == 46

def test_day05b_challenge():
    assert day05b.solve(util.get_challenge(5)) == 37384986