from aoc import AOC

aoc = AOC(18,  2015, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

def neighbour(grid, x, y):
    nb = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx != 0 or dy != 0:
                if 0 <= x + dx < len(grid):
                    if 0 <= y + dy < len(grid[0]):
                        if grid[x + dx][y + dy] == '#':
                            nb += 1
    return nb

def next_val(grid, x, y, corners_on=False):
    if corners_on and sum([x == 0, x == len(grid) - 1, y == 0, y == len(grid[0]) - 1]) >= 2:
        return '#'

    if grid[x][y] == '#':
        return '#' if neighbour(grid, x, y) in [2, 3] else '.'
    else:
        return '#' if neighbour(grid, x, y) == 3 else '.'

def step(grid, corners_on=False):
    return [[next_val(grid, x, y, corners_on) for y in range(len(grid[0]))] for x in range(len(grid))]

def score(grid):
    return sum([sum([1 if x == '#' else 0 for x in l]) for l in grid])

def run(corners_on=False):
    grid = input

    for i in range(100):
        grid = step(grid, corners_on)

    return score(grid)

p1_sol = run()
p2_sol = run(True)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
