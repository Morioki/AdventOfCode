import pathlib
import sys
import numpy as np

def updateBoard(board, ball):
    return np.where(board == ball, -100, board)

def checkBoardForVictor(board):
    #  Check Rows for victory
    for i in range(board.shape[0]):
        if np.all(board[i] == board[i][0]):
            return True

    #  Check Columns for victory
    board = board.T
    for i in range(board.shape[0]):
        if np.all(board[i] == board[i][0]):
            return True

    return False

def calculateBoard(board):
    return np.sum(np.where(board<0, 0, board))


def parse(puzzle_input):
    """Parse input"""
    # print(puzzle_input)

    puzzle_input = puzzle_input.splitlines()
    balls = [int(item) for item in puzzle_input[0].split(',')]
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
    for ball in balls:
        for i in range(len(boards)):
            boards[i] = updateBoard(boards[i], ball)
            if checkBoardForVictor(boards[i]):
                return calculateBoard(boards[i]) * ball

    return -1

# ! Solution is likely horribly unoptimal
def part2(balls, boards):
    """Solve part 2"""
    winningScore = -1
    winningInfo = None
    winningBoards = []
    for ball in balls:
        for i in range(len(boards)):
            if i in winningBoards: continue
            boards[i] = updateBoard(boards[i], ball)
            if checkBoardForVictor(boards[i]):
                winningBoards.append(i)
                winningInfo = (boards[i], ball)
                winningScore = calculateBoard(boards[i]) * ball

    # print(winningInfo)
    return winningScore

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