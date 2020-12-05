inFile = open('reportRepairInput.txt', 'r')
lines = inFile.readlines()

result = 0 
for line in lines:
    for compLine in lines:
        if( int(line) + int(compLine) == 2020):
            result = int(line) * int(compLine)

print('Puzzle 1: ' + str(result))

result2 = 0 
for line in lines:
    for line2 in lines:
        for line3 in lines:
            if( int(line) + int(line2) + int(line3) == 2020):
                result2 = int(line) * int(line2) * int(line3)

print('Puzzle 2: ' + str(result2))