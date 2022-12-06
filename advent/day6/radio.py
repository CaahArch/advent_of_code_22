
from advent.daily import read_input

def find_first_header(received:str, len_marker:int):

    for i in range(len(received) - len_marker + 1):
        header = received[i: i + len_marker]
        if (duplicates := len(set(header))) == len_marker:
            print(f"{header} has no duplicates")
            return i + len_marker
        # else:
            # print(f"{header} has {len_marker - duplicates} duplicates")


received = read_input()
print(f"Solution 1: {find_first_header(received, 4)}")
print(f"Solution 2: {find_first_header(received, 14)}")