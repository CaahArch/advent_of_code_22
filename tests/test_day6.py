
from advent.day6.radio import *

def test_find_first_header():
    assert find_first_header("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert find_first_header("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert find_first_header("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert find_first_header("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11