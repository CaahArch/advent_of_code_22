
from advent.day3.rucksack import *

def test_split_in_half():
    assert split_in_half("vJrwpWtwJgWrhcsFMMfFFhFp") == ("vJrwpWtwJgWr", "hcsFMMfFFhFp")
    assert split_in_half("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL") == ("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL")
    assert split_in_half("PmmdzqPrVvPwwTWBwg") == ("PmmdzqPrV", "vPwwTWBwg")

def test_double_one_out():
    assert double_one_out(("vJrwpWtwJgWr", "hcsFMMfFFhFp")) == "p"
    assert double_one_out(("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL")) == "L"
    assert double_one_out(("PmmdzqPrV", "vPwwTWBwg")) == "P"

def test_item_to_priority():
    assert item_to_priority('a') == 1
    assert item_to_priority('z') == 26
    assert item_to_priority('A') == 27
    assert item_to_priority('Z') == 52

def test_form_groups():
    assert list(elves_form_groups([1, 2, 3, 4, 5, 6])) == [(1, 2, 3), (4, 5, 6)]
    assert list(elves_form_groups([
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw"
        ])) == [(
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg"
        ), (
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw"
        )]