
from advent.day3.rucksack import split_in_half, double_one_out, item_to_priority

def test_split_in_half():
    assert split_in_half("vJrwpWtwJgWrhcsFMMfFFhFp") == ("vJrwpWtwJgWr", "hcsFMMfFFhFp")
    assert split_in_half("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL") == ("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL")
    assert split_in_half("PmmdzqPrVvPwwTWBwg") == ("PmmdzqPrV", "vPwwTWBwg")

def test_odd_one_out():
    assert double_one_out(("vJrwpWtwJgWr", "hcsFMMfFFhFp")) == "p"
    assert double_one_out(("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL")) == "L"
    assert double_one_out(("PmmdzqPrV", "vPwwTWBwg")) == "P"

def test_item_to_priority():
    assert item_to_priority('a') == 1
    assert item_to_priority('z') == 26
    assert item_to_priority('A') == 27
    assert item_to_priority('Z') == 52