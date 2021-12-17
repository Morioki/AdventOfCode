import pathlib
import sys
import itertools
import numpy as np

def parse(puzzle_input):
    """Parse input"""
    lines = [str(line) for line in puzzle_input.split('\n')]
    points = [ tuple([ tuple([el for el in point.split(',')]) for point in line.split(' -> ')]) for line in lines]

    return points

def part1(data):
    """Solve part 1"""

    # TODO Build empty grid
    matrix = np.zeros((1000,1000),dtype=int)
    # matrix = np.zeros((10,10),dtype=int)

    # print(matrix)

    for segment in data:
        a,b = segment

        ax, ay = a
        bx, by = b


        # ! Temp Begin
        # print(segment)
        if ay != by and ax != bx:
            continue
        # ! Temp End

        # TODO Vertical Lines (where ay = by)
        if ay == by:
            # Look through all points between that line
            # print(f'Line: {a} {b}')
            low = min(int(ax), int(bx))
            high = max(int(ax), int(bx))
            for i in range(low, high+1):
                matrix[i][int(ay)] = matrix[i][int(ay)] + 1

        # TODO Horizontal Lines (where ax = bx)
        if ax == bx:
            # Look through all points between that line
            # print(f'Line: {a} {b}')
            low = min(int(ay), int(by))
            high = max(int(ay), int(by))
            for i in range(low, high+1):
                matrix[int(ax)][i] = matrix[int(ax)][i] + 1

        # print(matrix)
    return np.count_nonzero(matrix > 1)

def part2(data):
    matrix = np.zeros((1000,1000),dtype=int)
    # matrix = np.zeros((10,10),dtype=int)

    # print(matrix)

    for segment in data:
        a,b = segment

        ax, ay = a
        bx, by = b

        # TODO Vertical Lines (where ay = by)
        if ay == by:
            # Look through all points between that line
            # print(f'Line: {a} {b}')
            low = min(int(ax), int(bx))
            high = max(int(ax), int(bx))
            for i in range(low, high+1):
                matrix[i][int(ay)] = matrix[i][int(ay)] + 1
            continue

        # TODO Horizontal Lines (where ax = bx)
        if ax == bx:
            # Look through all points between that line
            # print(f'Line: {a} {b}')
            low = min(int(ay), int(by))
            high = max(int(ay), int(by))
            for i in range(low, high+1):
                matrix[int(ax)][i] = matrix[int(ax)][i] + 1
            continue

        # TODO Diagonal Lines 
        lowX = min(int(ax), int(bx))
        highX = max(int(ax), int(bx))
        lowY = min(int(ay), int(by))
        highY = max(int(ay), int(by))

        ax = int(ax)
        ay = int(ay)
        bx = int(bx)
        by = int(by)

        # * With Diagonals in the 45, we are alawys going horizontal same amt as vertical
        for i in range((highX - lowX) + 1):
            mappedX = ax+i if ax < bx else ax-i
            mappedY = ay+i if ay < by else ay-i
            # print(f'Line: {a} {b}')
            # print(f'Point to Map: ({mappedX},{mappedY})')
            matrix[mappedX][mappedY] = matrix[mappedX][mappedY] + 1
 
        # break
        # print(matrix)
    return np.count_nonzero(matrix > 1)

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