#!python3

# input: inventory of elves as list of lists of ints
# output: how many calories are carried by the elf carrying the most

import os
script_dir = os.path.dirname(__file__)

with open(script_dir + "/input1.txt", "r") as file:
    inventory = file.read()

elves = [elem.split("\n") for elem in inventory.split("\n\n")]
print(f"inventory items: {len(inventory)}\ncarried by {len(elves)} elves")

sum_per_elf = [sum([int(c) if c != '' else 0 for c in elf]) for elf in elves]
print(sum_per_elf)

#### Part 1 #### 
big_stack_of_food = max(sum_per_elf)
print(f"SOLUTION 1: The most calories which are carried one elf is {big_stack_of_food}")

#### Part 2 #### 
top3 = 0
for i in range(3):
    top3 += max(sum_per_elf)
    sum_per_elf.remove(max(sum_per_elf))
print(f"SOLUTION 2: The top 3 elves carry {top3} calories together")
