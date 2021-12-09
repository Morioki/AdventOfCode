import pathlib
import sys
import itertools

def parse(puzzle_input):
    """Parse input"""
    return [int(line) for line in puzzle_input.split()]

def threes(puzzle_input):
    a,b,c = itertools.tee(puzzle_input, 3)
    next(b, None)
    next(c, None)
    next(c, None)
    return zip(a,b,c)

def part1(data):
    """Solve part 1"""
    countIncreased = 0
    prevItem = None

    for row in data:
        if prevItem == None:
            prevItem = row
            continue
        
        if prevItem < row:
            countIncreased += 1;
        prevItem = row
    
    return countIncreased

def part2(data):
    """Solve part 2"""

    depthIncreased = 0
    prevDepth = None

    for a, b, c in threes(data):
        depth = a+b+c

        if prevDepth == None:
            prevDepth = depth
            continue

        if prevDepth < depth:
            depthIncreased += 1
        prevDepth = depth

    return depthIncreased

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