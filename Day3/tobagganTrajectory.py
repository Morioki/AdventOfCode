def tree_collision(lines, xInc, yInc):
    treeCount = 0
    x = 0
    for y in range(0, len(lines), yInc):
        if lines[y][x] == '#':
            treeCount += 1
        x = (x + xInc) % (len(lines[0]))
    return treeCount

with open('input.txt', 'r') as f:
    data = f.read().splitlines()

treeCount = tree_collision(data, 3, 1)

print('Puzzle 1: ' + str(treeCount))

result = treeCount
result *= tree_collision(data, 1, 1)
result *= tree_collision(data, 5, 1)
result *= tree_collision(data, 7, 1)
result *= tree_collision(data, 1, 2)

print('Puzzle 2: ' + str(result))
