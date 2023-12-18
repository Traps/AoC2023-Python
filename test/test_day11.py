import pytest
import util

from solution import day11a, day11b

def test_day11a_sample():
    assert day11a.solve(util.get_sample(11)) == 374

def test_day11a_challenge():
    assert day11a.solve(util.get_challenge(11)) == 10422930

def test_day11b_sample():
    assert day11b.solve(util.get_sample(11), 10) == 1030
    assert day11b.solve(util.get_sample(11), 100) == 8410

def test_day11b_challenge():
    assert day11b.solve(util.get_challenge(11)) == 699909023130