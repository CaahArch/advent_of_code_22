
# outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)
score_per_win = {"lose" : 0,
    "draw" : 3,
    "win": 6}

from advent.daily import read_input

inventory = read_input()
rounds = [elem.split(" ") for elem in inventory.split("\n")]
# print(rounds)

# modify input to use numbers instead of letters
# Score 1 for Rock, 2 for Paper, and 3 for Scissors
for round in rounds:
    # A for Rock, B for Paper, and C for Scissors
    round[0] = ord(round[0].lower()) - 96
    # X for Rock, Y for Paper, and Z for Scissors
    round[1] = ord(round[1].lower()) - 96 - 23
# print(rounds)

#### Part 1 #### 
def calc_score(rounds):
    score = 0
    for round in rounds:
        tmp = round[1]
        if round [0] == round[1]:
            tmp += 3
        elif round[0] == round[1] - 1  or round[0] == round[1] + 2:
            tmp += 6
        # print(f"input: {round}\tscore: {tmp}")
        score += tmp
    return score

print(f"SOLUTION 1: The score is {calc_score(rounds)}")

#### Part 2 #### 
def calc_shape(rounds):
    # X (1) means you need to lose, Y (2) means you need to end the round in a draw, and Z (3) means you need to win
    shapes = []
    for round in rounds:
        my_shape = (round[0] + round[1] - 2) % 3
        if my_shape == 0:
            my_shape = 3
        shapes.append([round[0], my_shape])
    return shapes
    # for i in (zip(rounds, shapes)):
    #     print(i)

print(f"SOLUTION 1: The score is {calc_score(calc_shape(rounds))}")