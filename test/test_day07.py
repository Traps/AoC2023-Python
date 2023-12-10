import pytest
import util

from solution import day07a, day07b

def test_day07a_sample():
    assert day07a.solve(util.get_sample(7)) == 6440

def test_day07a_challenge():
    assert day07a.solve(util.get_challenge(7)) == 250254244

def test_day07b_sample():
    assert day07b.solve(util.get_sample(7)) == 5905

def test_day07b_challenge():
    assert day07b.solve(util.get_challenge(7)) == 250087440