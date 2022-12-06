
from advent.daily import read_input

def find_first_header(received:str):
    header = ""

    for i in range(len(received) - 5):
        header = received[i: i + 4]
        if len(set(header)) == 4:
            print(f"{header} has no duplicates")
            return i + 4
        else:
            print(f"{header} has duplicates")


received = read_input()
print(f"Solution 1: {find_first_header(received)}")