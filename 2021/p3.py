import pathlib
import sys
import itertools

def parse(puzzle_input):
    """Parse input"""
    return [str(line) for line in puzzle_input.split()]
    # return [tuple(line.split()) for line in puzzle_input.split('\n')]

def getZeroOneFreq(data, pos):
    zeroFreq = 0
    oneFreq = 0
    for el in data:
        oneFreq += 1 if el[pos] == "1" else 0
        zeroFreq += 1 if el[pos] == "0" else 0

    return zeroFreq, oneFreq

def parseGammaAndEpsilon(data):
    gammaRate = ""
    epsilonRate = ""

    for pos in range(len(data[1])):
        zeroFreq, oneFreq = getZeroOneFreq(data, pos)
        
        # print(f'Position {pos}:\n One Freq: {oneFreq}\n Zero Freq: {zeroFreq}')
        gammaRate += "1" if oneFreq >= zeroFreq else "0"
        epsilonRate += "1" if oneFreq <= zeroFreq else "0"

    return gammaRate, epsilonRate

def parseOxyRating(data):
    workingSet = data
    for pos in range(len(workingSet[1])):
        # print(f'Checking pos: {pos}')
        if len(workingSet) == 1:
            return workingSet[0]

        zeroFreq, oneFreq = getZeroOneFreq(workingSet,pos)
        # print(f' Zero Freq: {zeroFreq}\n One Freq: {oneFreq}')
        if zeroFreq > oneFreq:
            # Keep the records with 0 in pos
            workingSet = [ record for record in workingSet if record[pos] == "0"]
        else:
            workingSet = [ record for record in workingSet if record[pos] == "1"]

    return workingSet[0]

def parseCO2Rating(data):
    workingSet = data
    for pos in range(len(workingSet[1])):
        # print(f'Checking pos: {pos}')
        if len(workingSet) == 1:
            return workingSet[0]

        zeroFreq, oneFreq = getZeroOneFreq(workingSet,pos)
        # print(f' Zero Freq: {zeroFreq}\n One Freq: {oneFreq}')
        if zeroFreq <= oneFreq:
            # Keep the records with 0 in pos
            workingSet = [ record for record in workingSet if record[pos] == "0"]
        else:
            workingSet = [ record for record in workingSet if record[pos] == "1"]

    return workingSet[0] 

def part1(data):
    """Solve part 1"""
    gamma, epsilon = parseGammaAndEpsilon(data)
    gammaInt = int(gamma, 2)
    epsilonInt = int(epsilon, 2)

    return gammaInt * epsilonInt

def part2(data):
    """Solve part 2"""
    oxyRating = parseOxyRating(data)
    co2Rating = parseCO2Rating(data)

    oxyInt = int(oxyRating, 2)
    co2Int = int(co2Rating, 2)

    return oxyInt * co2Int

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