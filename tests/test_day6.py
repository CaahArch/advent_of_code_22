
from advent.day6.radio import *

def test_find_start_package():
    assert find_first_header("bvwbjplbgvbhsrlpgdmjqwftvncz", 4) == 5
    assert find_first_header("nppdvjthqldpwncqszvftbrmjlhg", 4) == 6
    assert find_first_header("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4) == 10
    assert find_first_header("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4) == 11

    
def test_find_start_message():
    assert find_first_header("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23
    assert find_first_header("nppdvjthqldpwncqszvftbrmjlhg", 14) == 23
    assert find_first_header("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14) == 29
    assert find_first_header("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14) == 26
