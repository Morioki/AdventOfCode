import pathlib
import sys
import itertools

def parse(puzzle_input):
    """Parse input"""
    return [str(line) for line in puzzle_input.split()]
    # return [tuple(line.split()) for line in puzzle_input.split('\n')]

def calcGammaAndEpsilon(data):
    gammaRate = ""
    epsilonRate = ""

    for pos in range(len(data[1])):
        zeroFreq = 0
        oneFreq = 0
        for el in data:
            oneFreq += 1 if el[pos] == "1" else 0
            zeroFreq += 1 if el[pos] == "0" else 0
        
        print(f'Position {pos}:\n One Freq: {oneFreq}\n Zero Freq: {zeroFreq}')
        gammaRate += "1" if oneFreq >= zeroFreq else "0"
        epsilonRate += "1" if oneFreq <= zeroFreq else "0"

    pass
    

def part1(data):
    """Solve part 1"""
    gamma = calcGammaAndEpsilon(data)
    # print(data)
    pass

def part2(data):
    """Solve part 2"""
    pass

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