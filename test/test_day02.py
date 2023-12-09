import pytest
import util

from solution import day02a, day02b

def test_day02a_sample():
    assert day02a.solve(util.get_sample(2)) == 8

def test_day02a_challenge():
    assert day02a.solve(util.get_challenge(2)) == 2348

def test_day02b_sample():
    assert day02b.solve(util.get_sample(2)) == 2286

def test_day02b_challenge():
    assert day02b.solve(util.get_challenge(2)) == 76008