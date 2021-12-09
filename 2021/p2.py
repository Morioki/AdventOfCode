import pathlib
import sys
import itertools

def parse(puzzle_input):
    """Parse input"""
    return [tuple(line.split()) for line in puzzle_input.split('\n')]
    

def part1(data):
    """Solve part 1"""
    horizontalPos = 0
    depth = 0

    for command, val in data:
        if(command=="forward"):
            horizontalPos += int(val)
        elif(command=="up"):
            depth -= int(val)
        elif(command=="down"):
            depth += int(val)
        else:
            print("PROBLEM")

    # print(f'Horizontal Position: {horizontalPos}\nDepth: {depth}')
    return horizontalPos * depth

def part2(data):
    """Solve part 2"""
    horizontalPos = 0
    depth = 0
    aim = 0

    for command, val in data:
        if(command=="forward"):
            horizontalPos += int(val)
            depth += (aim * int(val))
        elif(command=="up"):
            aim -= int(val)
        elif(command=="down"):
            aim += int(val)
        else:
            print("PROBLEM")

    # print(f'Horizontal Position: {horizontalPos}\nDepth: {depth}')
    return horizontalPos * depth

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