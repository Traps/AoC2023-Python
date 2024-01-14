import pytest
import util

from solution import day19a, day19b

def test_day19a_sample():
    assert day19a.solve(util.get_sample(19)) == 19114

def test_day19a_challenge():
    assert day19a.solve(util.get_challenge(19)) == 398527

def test_day19b_sample():
    assert day19b.solve(util.get_sample(19)) == 167409079868000

def test_day19b_challenge():
    assert day19b.solve(util.get_challenge(19)) == 133973513090020