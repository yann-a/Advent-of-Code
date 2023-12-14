from aoc import AOC

aoc = AOC(14,  2023, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    s = 0
    for col in range(len(input[0])):
        pnr = 0
        for line in range(len(input)):
            if input[line][col] == 'O':
                s += len(input) - pnr 
                pnr += 1
            elif input[line][col] == '#':
                pnr = line + 1

    return s

def load(grid):
    s = 0
    for line in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[line][col] == 'O':
                s += len(grid) - line

    return s

def tiltvert(grid, dir):
    for col in range(len(grid[0])):
        pnr = 0 if dir == 'n' else len(grid) - 1
        for line in range(len(grid)):
            cell = grid[line][col] if dir == 'n' else grid[len(grid) - line - 1][col]
            if cell == 'O':
                if dir == 'n': grid[line][col] = '.'
                else: grid[len(grid) - line - 1][col] = '.'
                grid[pnr][col] = 'O'

                pnr += (1 if dir == 'n' else -1)
            elif cell == '#':
                pnr = line + 1 if dir == 'n' else len(grid) - line - 2

def tilthoriz(grid, dir):
    for line in range(len(grid)):
        pnr = 0 if dir == 'w' else len(grid[0]) - 1
        for col in range(len(grid[0])):
            cell = grid[line][col] if dir == 'w' else grid[line][len(grid[0]) - col - 1]
            if cell == 'O':
                if dir == 'w': grid[line][col] = '.'
                else: grid[line][len(grid[0]) - col - 1] = '.'
                grid[line][pnr] = 'O'

                pnr += (1 if dir == 'w' else -1)
            elif cell == '#':
                pnr = col + 1 if dir == 'w' else len(grid[0]) - col - 2

def tilt(grid, dir):
    if dir in 'ns': tiltvert(grid, dir)
    elif dir in 'we': tilthoriz(grid, dir)

def cycle(grid):
    for dir in 'nwse':
        tilt(grid, dir)

def repr(grid):
    s = ''
    for line in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[line][col] == 'O':
                s += '0'
            elif grid[line][col] == '#':
                s += '1'
            else:
                s += '2'

    return int(s, 3)

N = 1_000_000_000

def part2():
    grid = list(map(list, input))

    hist = [repr(grid)]
    while True:
        cycle(grid)
        r = repr(grid)

        if r in hist:
            break

        hist.append(r)

    prev = hist.index(r)
    new = len(hist)

    r = (N - prev) % (new - prev)

    for _ in range(r):
        cycle(grid)

    return load(grid)

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
