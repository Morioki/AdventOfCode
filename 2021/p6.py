import pathlib
import sys
import itertools
import numpy as np

def parse(puzzle_input):
    """Parse input"""
    return [int(line) for line in puzzle_input.split(',')]

def nextGeneration(data):
    # print(f'Initial: {data}')
    newGeneration = list(map(lambda a : a-1, data))
    
    for i in range(len(newGeneration)):
        if newGeneration[i] == -1:
            newGeneration[i] = 6
            newGeneration.append(8)


    # print(f'New: {newGeneration}')
    return newGeneration

# Could make this entire thing a dataClass instead of a list
def initialCounts(data):
    array = [0] * 9
    array[0] = data.count(0)
    array[1] = data.count(1)
    array[2] = data.count(2)
    array[3] = data.count(3)
    array[4] = data.count(4)
    array[5] = data.count(5)
    array[6] = data.count(6)
    array[7] = data.count(7)
    array[8] = data.count(8)
    return array

def nextGeneration_Adv(data):
    # print(f'Initial: {data}')

    countOfZeros = data.pop(0)
    data[6] = data[6] + countOfZeros
    data.append(countOfZeros)

    # print(f'After: {data}')
    return data

def part1(data):
    """Solve part 1"""
    # nextGeneration(data=data)
    for i in range(80):
        data = nextGeneration(data)
    
    return len(data)

def part2(data):
    """Solve part 2"""
    proc = initialCounts(data)

    for i in range(256):
        # print(f'Iteration: {i}')
        proc = nextGeneration_Adv(proc)

    return sum(proc)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))