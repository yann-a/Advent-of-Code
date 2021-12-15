from aoc import AOC

aoc = AOC(17,  2020, __file__)

input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

def neighbour(grid, x, y, z, w=None):
    nb = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                if w is None:
                    if dx != 0 or dy != 0 or dz != 0:
                        if 0 <= x + dx < len(grid):
                            if 0 <= y + dy < len(grid[0]):
                                if 0 <= z + dz < len(grid[0][0]):
                                    if grid[x + dx][y + dy][z + dz] == '#':
                                        nb += 1
                else:
                    for dw in range(-1, 2):
                        if dx != 0 or dy != 0 or dz != 0 or dw != 0:
                            if 0 <= x + dx < len(grid):
                                if 0 <= y + dy < len(grid[0]):
                                    if 0 <= z + dz < len(grid[0][0]):
                                        if 0 <= w + dw < len(grid[0][0][0]):
                                            if grid[x + dx][y + dy][z + dz][w + dw] == '#':
                                                nb += 1
    return nb

def get(grid, x, y, z, w=None):
    if w is None:
        return grid[x][y][z]
    else:
        return grid[x][y][z][w]

def next_val(grid, x, y, z, w=None):
    if get(grid, x, y, z, w) == '#':
        return '#' if neighbour(grid, x, y, z, w) in [2, 3] else '.'
    else:
        return '#' if neighbour(grid, x, y, z, w) == 3 else '.'

def step(grid, dim=3):
    if dim == 3:
        return [[[next_val(grid, x, y, z) for z in range(len(grid[0][0]))] for y in range(len(grid[0]))] for x in range(len(grid))]
    else:
        return [[[[next_val(grid, x, y, z, w) for w in range(len(grid[0][0][0]))] for z in range(len(grid[0][0]))] for y in range(len(grid[0]))] for x in range(len(grid))]

def score(grid, dim=3):
    if dim == 3:
        return sum([sum([sum([1 if x == '#' else 0 for x in l]) for l in ll]) for ll in grid])
    else:
        return sum([sum([sum([sum([1 if x == '#' else 0 for x in L]) for L in l]) for l in ll]) for ll in grid])

grid3 = [[['.' for _ in range(13)] for _ in range(len(input) + 12)] for _ in range(len(input[0]) + 12)]
for i in range(len(input)):
    for j in range(len(input[i])):
        grid3[j + 6][i + 6][6] = input[i][j]
grid4 = [[[['.' for _ in range(13)] for _ in range(13)] for _ in range(len(input) + 12)] for _ in range(len(input[0]) + 12)]
for i in range(len(input)):
    for j in range(len(input[i])):
        grid4[j + 6][i + 6][6][6] = input[i][j]

for i in range(6):
    grid3 = step(grid3)
    grid4 = step(grid4, 4)

p1_sol = score(grid3)
p2_sol = score(grid4, 4)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
