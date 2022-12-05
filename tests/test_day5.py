
from advent.day5.crane_operator import *

def test_parse_input():
    input = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
    assert parse_move_instructions(input) == [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]]

def test_parse_crate():
    input = """    [D]    
[N] [C]    
[Z] [M] [P]"""
    assert parse_crates(input) == [['N', 'Z'], ['D', 'C', 'M'], ['P']]

def test_move_crate():
    crate = [['N', 'Z'], ['D', 'C', 'M'], ['P']]
    assert move_crate(1, 2, 1, crate) == [['D', 'N', 'Z'], ['C', 'M'], ['P']]
    crate = [['N', 'Z'], ['D', 'C', 'M'], ['P']]
    assert move_crate(2, 2, 1, crate) == [['C', 'D', 'N', 'Z'], ['M'], ['P']]
