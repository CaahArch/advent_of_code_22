
from advent.daily import read_input

def split_in_half(rucksack: str):
    return rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]

def double_one_out(rucksack: list) -> str:
    same = set(rucksack[0])
    for r in rucksack[1:]:
        same = set([c for c in r if c in same])
        if len(same) == 1:
            return next(iter(same))
    return same

def item_to_priority(item):
    if len(item) > 1:
        item = item[0]
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38

### Part 1 ###
all_rucksacks = read_input().split('\n')
double_items = [double_one_out(split_in_half(r)) for r in all_rucksacks]
# print(double_items)
priorities = [item_to_priority(i) for i in double_items]

print(f"Solution 1 is {sum(priorities)}")

### Part 2 ###
def elves_form_groups(all_rucksacks):
    "s -> (s0, s1, s2), (s1, s2, s3), (s2, s3, 4), ..."
    a = iter(all_rucksacks)
    return zip(a, a, a)
    
badges = [double_one_out(group) 
    for group in elves_form_groups(all_rucksacks)]
priorities = [item_to_priority(i) for i in badges]

print(f"Solution 1 is {sum(priorities)}")
