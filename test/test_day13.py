import pytest
import util

from solution import day13a, day13b

def test_day13a_sample():
    assert day13a.solve(util.get_sample(13)) == 405

def test_day13a_challenge():
    assert day13a.solve(util.get_challenge(13)) == 27202

def test_day13b_sample():
    assert day13b.solve(util.get_sample(13)) == 400

def test_day13b_challenge():
    assert day13b.solve(util.get_challenge(13)) == 41566