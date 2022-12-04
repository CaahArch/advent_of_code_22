
from advent.daily import read_input

def split_in_half(rucksack: str):
    return rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]

def double_one_out(rucksack: list):
    for c in rucksack[0]:
        if c in rucksack[1]:
            return c

def item_to_priority(item):
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38

### Part 1 ###
all_rucksacks = [split_in_half(items) for items in read_input().split('\n')]
double_items = [double_one_out(r) for r in all_rucksacks]
# print(double_items)
priorities = [item_to_priority(i) for i in double_items]

print(f"Solution 1 is {sum(priorities)}")

