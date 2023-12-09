import pytest
import util

from solution import day03a, day03b

def test_day03a_sample():
    assert day03a.solve(util.get_sample(3)) == 4361

def test_day03a_challenge():
    assert day03a.solve(util.get_challenge(3)) == 544664

def test_day03b_sample():
    assert day03b.solve(util.get_sample(3)) == 467835

def test_day03b_challenge():
    assert day03b.solve(util.get_challenge(3)) == 84495585