import pytest
import util

from solution import day17a

def test_day17a_sample():
    assert day17a.solve(util.get_sample(17)) == 102

def test_day17a_challenge():
    assert day17a.solve(util.get_challenge(17)) == 1013

# def test_day17b_sample():
#     assert day17b.solve(util.get_sample(17)) == ??

# def test_day17b_challenge():
#     assert day17b.solve(util.get_challenge(17)) == ??