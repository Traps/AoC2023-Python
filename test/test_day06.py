import pytest
import util

from solution import day06a, day06b

def test_day06a_sample():
    assert day06a.solve(util.get_sample(6)) == 288

def test_day06a_challenge():
    assert day06a.solve(util.get_challenge(6)) == 140220

def test_day06b_sample():
    assert day06b.solve(util.get_sample(6)) == 71503

def test_day06b_challenge():
    assert day06b.solve(util.get_challenge(6)) == 39570185