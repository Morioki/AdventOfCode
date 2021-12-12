import pathlib
import sys
import numpy as np

def parse(puzzle_input):
    """Parse input"""
    # print(puzzle_input)

    puzzle_input = puzzle_input.splitlines()
    balls = puzzle_input[0].split(',')
    boards = []

    board = np.empty(5, dtype=int)

    resetFlag = False
    for val in puzzle_input:
        if val == puzzle_input[0]:
            continue;
        if val == '':
            # Append Board 
            if board.size == 25:
                boards.append(board)
            # Reset Board 
            resetFlag = True
            continue
    
        line = [int(item) for item in val.split()]
        if resetFlag:
            board = np.array(line)
            resetFlag = False
        else:
            board = np.vstack((board, line))
    
    return balls, boards


def part1(balls, boards):
    """Solve part 1"""
    print(balls)
    print(boards)
    pass

def part2(balls, boards):
    """Solve part 2"""
    pass

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    balls, boards = parse(puzzle_input)
    solution1 = part1(balls, boards)
    solution2 = part2(balls, boards)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))