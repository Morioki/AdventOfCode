import re

pat = '(\d+)-(\d+)\s([a-z]):\s([a-z]+)'
inFile = open('input.txt', 'r')
lines = inFile.readlines()

correct1 = 0
correct2 = 0
for line in lines:
    m = re.match(pat, line)
    if m:
        if int(m.group(1)) <= m.group(4).count(m.group(3)) <= int(m.group(2)):
            correct1 += 1

        if m.group(4)[int(m.group(1))-1] == m.group(3) or m.group(4)[int(m.group(2))-1] == m.group(3):
            if m.group(4)[int(m.group(1))-1] != m.group(4)[int(m.group(2))-1]:
                correct2 += 1
        
print('Puzzle 1: ' + str(correct1))
print('Puzzle 2: ' + str(correct2))
