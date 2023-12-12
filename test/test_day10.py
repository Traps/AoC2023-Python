import pytest
import util

from solution import day10a, day10b

def test_day10a_sample():
    assert day10a.solve(util.get_sample(10, 'a', 0)) == 4
    assert day10a.solve(util.get_sample(10, 'a', 1)) == 4
    assert day10a.solve(util.get_sample(10, 'a', 2)) == 8
    assert day10a.solve(util.get_sample(10, 'a', 3)) == 8

def test_day10a_challenge():
    assert day10a.solve(util.get_challenge(10)) == 6831

def test_day10b_sample():
    assert day10b.solve(util.get_sample(10, 'b', 0)) == 4
    assert day10b.solve(util.get_sample(10, 'b', 1)) == 4
    assert day10b.solve(util.get_sample(10, 'b', 2)) == 8
    assert day10b.solve(util.get_sample(10, 'b', 3)) == 10
    assert day10b.solve(util.get_sample(10, 'b', 4)) == 10

def test_day10b_challenge():
    assert day10b.solve(util.get_challenge(10)) == 305