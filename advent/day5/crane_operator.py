
import re
from advent.daily import read_input

def parse_move_instructions(input):
    return [[int(i) for i in re.findall(r"\d+", move)] for move in input.split("\n")]

def parse_crates(crates:str):
    crates = crates.split('\n')
    # number of stacks: len+1 / 4
    num_stacks = re.findall(r"\w", crates[-1])
    crates_list = []
    for i, c in enumerate(num_stacks):
        crates_list.append([])
        for s in range(len(crates)):
            # crate is at position 1 + 4s
            crate = crates[s][1+4*i]
            if crate not in ['', ' ']:
                crates_list[i].append(crate)
            # if empty, skip
    return crates_list

def move_crate(amount:int, origin:int, target:int, stacks:list):
    for i in range(amount):
        moving = stacks[origin-1].pop(0)
        stacks[target-1].insert(0, *moving)
    return stacks

def move_crate_9001(amount:int, origin:int, target:int, stacks:list):
    moving = stacks[origin-1][:amount]
    stacks[target-1] = moving + stacks[target-1]
    del stacks[origin-1][:amount]

def main():
    crates, move_intructions = read_input().split("\n 1   2   3   4   5   6   7   8   9 \n\n")

    stacks = parse_crates(crates)
    moves = parse_move_instructions(move_intructions)

    for m in moves:
        move_crate_9001(*m, stacks)

    print(f"Solution 1: {''.join([x[0] for x in stacks])}")

if __name__ == "__main__":
    main()