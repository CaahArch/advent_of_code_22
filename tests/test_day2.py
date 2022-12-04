
import pytest
from advent.day2.rock_paper_scissors import calc_score, calc_shape

### Part 1 ###
def test_winning():
    assert calc_score([[1, 2], ]) == 2 + 6
    assert calc_score([[2, 3], ]) == 3 + 6
    assert calc_score([[3, 1], ]) == 1 + 6

def test_draw():
    assert calc_score([[1, 1], ]) == 1 + 3
    assert calc_score([[2, 2], ]) == 2 + 3
    assert calc_score([[3, 3], ]) == 3 + 3

def test_losing():
    assert calc_score([[1, 3], ]) == 3
    assert calc_score([[2, 1], ]) == 1
    assert calc_score([[3, 2], ]) == 2

### Part 2 ###
def test_shape_win():
    assert calc_shape([[1, 3],]) == [[1, 2]]
    assert calc_shape([[2, 3],]) == [[2, 3]]
    assert calc_shape([[3, 3],]) == [[3, 1]]