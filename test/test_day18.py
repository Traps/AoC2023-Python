import pytest
import util

from solution import day18a, day18b

def test_day18a_sample():
    assert day18a.solve(util.get_sample(18)) == 62

def test_day18a_challenge():
    assert day18a.solve(util.get_challenge(18)) == 31171

def test_day18b_sample():
    assert day18b.solve(util.get_sample(18)) == 952408144115

def test_day18b_challenge():
    assert day18b.solve(util.get_challenge(18)) == 131431655002266