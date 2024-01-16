import pytest
import util

from solution import day20a

def test_day20a_sample():
    assert day20a.solve(util.get_sample(20, option=0)) == 32000000
    assert day20a.solve(util.get_sample(20, option=1)) == 11687500

def test_day20a_challenge():
    assert day20a.solve(util.get_challenge(20)) == 818649769