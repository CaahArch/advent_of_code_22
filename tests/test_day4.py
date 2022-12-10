
from advent.day4.cleaning import * 

def test_all_in_one():
    assert areas_fully_covered(input="""2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
234-236,233-236
6-6,4-6
9-77,6-78
6-78,9-77
2-6,4-8""") == 5
    assert areas_fully_covered("8-20,11-63") == 0