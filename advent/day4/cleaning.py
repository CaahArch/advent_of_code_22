from advent.daily import read_input

def parse_cleaning_plan(input:str):
    result = []
    for pair in input.split('\n'):
        tmp = []
        for elf in pair.split(','):
            start, stop = elf.split("-")
            tmp.append(list(range(int(start), int(stop)+1)))
        result.append(tmp)
        print(f"{pair} ---> {tmp}")
    return result

def areas_fully_covered(input:str):
    double = 0
    for pair in input.split('\n'):
        [start1, stop1], [start2, stop2] = [[int(x) for x in elf.split("-")] for elf in pair.split(',')]
        if start1 <= start2 and stop1 >= stop2:
            double += 1
            print(f"overlap: {pair} (2 within 1)")
        elif start1 >= start2 and stop1 <= stop2:
            double += 1
            print(f"overlap: {pair} (1 within 2)")
    return double


def areas_partially_covered(input:str):
    double = 0
    for pair in input.split('\n'):
        [start1, stop1], [start2, stop2] = [[int(x) for x in elf.split("-")] for elf in pair.split(',')]
        if start1 <= start2 <= stop1:
            double += 1
            # print(f"overlap: {pair} (2 within 1)")
        elif start2 <= start1 <= stop2:
            double += 1
            # print(f"overlap: {pair} (1 within 2)")
        else:
            print(f"no overlap: {pair}")
    return double

def main():
    cleaning_plan = read_input()
    # print(f"Solution 1: {areas_fully_covered(cleaning_plan)}")
    print(f"Solution 2: {areas_partially_covered(cleaning_plan)}")

if __name__ == "__main__":
    main()