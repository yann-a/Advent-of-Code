from aoc import AOC
from math import ceil

aoc = AOC(24,  2019, __file__)

input = aoc.input.strip().split('\n')
#input = open('example', 'r').read().strip().split('\n')

def compute_repr_part1(grid):
    line_to_binary = lambda line: ''.join(map(lambda c: '0' if c == '.' else '1', line))
    grid_binary = ''.join(map(line_to_binary, grid))

    return int(grid_binary, 2)

def evolve_grid_part1(grid):
    neighbours = [[0 for _ in range(5)] for _ in range(5)]

    for y in range(5):
        for x in range(5):
            if grid[y][x] == '#':
                for dx in [-1, 1]:
                    if 0 <= x + dx < 5:
                        neighbours[y][x + dx] += 1
                for dy in [-1, 1]:
                    if 0 <= y + dy < 5:
                        neighbours[y + dy][x] += 1

    for y in range(5):
        for x in range(5):
            if grid[y][x] == '#':
                grid[y][x] = '#' if neighbours[y][x] == 1 else '.'
            else:
                grid[y][x] = '#' if 1 <= neighbours[y][x] <= 2 else '.'

def part1():
    grid = list(map(list, input))
    grid_history = []

    while True:
        repr = compute_repr_part1(grid)

        if repr in grid_history:
            break

        grid_history.append(repr)
        evolve_grid_part1(grid)

    s = 0
    for y in range(5):
        for x in range(5):
            if grid[y][x] == '#':
                s += pow(2, y * 5 + x)

    return s

def evolve_grid_part2(grids):
    neighbours = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(len(grids) + 2)]
    grids = [[['.' for _ in range(5)] for _ in range(5)]] + grids + [[['.' for _ in range(5)] for _ in range(5)]]

    for layer in range(len(neighbours)):
        for y in range(5):
            for x in range(5):
                if grids[layer][y][x] == '#':
                    for dx in [-1, 1]:
                        if x + dx == -1:
                            neighbours[layer - 1][2][1] += 1
                        elif x + dx == 5:
                            neighbours[layer - 1][2][3] += 1
                        elif x + dx == 2 and y == 2:
                            for ny in range(5):
                                nx = 0 if x == 1 else 4
                                neighbours[layer + 1][ny][nx] += 1
                        else:
                            neighbours[layer][y][x + dx] += 1
                    for dy in [-1, 1]:
                        if y + dy == -1:
                            neighbours[layer - 1][1][2] += 1
                        elif y + dy == 5:
                            neighbours[layer - 1][3][2] += 1
                        elif y + dy == 2 and x == 2:
                            for nx in range(5):
                                ny = 0 if y == 1 else 4
                                neighbours[layer + 1][ny][nx] += 1
                        else:
                            neighbours[layer][y + dy][x] += 1

    for layer in range(len(neighbours)):
        for y in range(5):
            for x in range(5):
                if grids[layer][y][x] == '#':
                    grids[layer][y][x] = '#' if neighbours[layer][y][x] == 1 else '.'
                else:
                    grids[layer][y][x] = '#' if 1 <= neighbours[layer][y][x] <= 2 else '.'

    return grids

def part2(M):
    grids = [list(map(list, input))]

    for _ in range(M):
        grids = evolve_grid_part2(grids)

    bugs = 0
    for layer in range(len(grids)):
        for y in range(5):
            for x in range(5):
                if grids[layer][y][x] == '#':
                    bugs += 1

    return bugs

p1_sol = part1()
p2_sol = part2(200)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
