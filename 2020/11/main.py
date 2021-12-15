from aoc import AOC

aoc = AOC(11,  2020, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')


def nb_neigh(grid, x, y, part=1):
    nb = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx != 0 or dy != 0:
                if part == 1:
                    if 0 <= x + dx < len(grid[0]) and 0 <= y + dy < len(grid):
                        if grid[y + dy][x + dx] == '#':
                            nb += 1
                else:
                    alpha = 1
                    while True:
                        if 0 <= x + alpha*dx < len(grid[0]) and 0 <= y + alpha*dy < len(grid):
                            if grid[y + alpha*dy][x + alpha*dx] in ['#', 'L']:
                                if grid[y + alpha*dy][x + alpha*dx] == '#':
                                    nb += 1
                                break
                        else:
                            break
                        alpha += 1
    return nb


def new_val(grid, x, y, part=1):
    min_neigh_change = 4 if part == 1 else 5

    if grid[y][x] == '.':
        return '.'
    elif grid[y][x] == 'L':
        return '#' if nb_neigh(grid, x, y, part) == 0 else 'L'
    else:
        return 'L' if nb_neigh(grid, x, y, part) >= min_neigh_change else '#'


def apply(grid, part=1):
    return [[new_val(grid, x, y, part) for x in range(len(grid[0]))] for y in range(len(grid))]


def score(grid):
    return sum([sum([1 if x == '#' else 0 for x in line]) for line in grid])


def solve(part):
    grid = [[x for x in line] for line in input]

    while True:
        new_g = apply(grid, part)

        if new_g == grid:
            return score(grid)

        grid = new_g


p1_sol = solve(1)
p2_sol = solve(2)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
