from aoc import AOC
from queue import PriorityQueue

aoc = AOC(24,  2022, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def can_move(grid, x, y, time):
    if (y == -1 and x == 0) or (y == len(grid) and x == len(grid[0]) - 1):
        return True

    if not(0 <= y < len(grid) and 0 <= x < len(grid[0])):
        return False

    has_wind = False
    has_wind |= grid[y][(x + time) % len(grid[0])] == '<'
    has_wind |= grid[y][(x - time) % len(grid[0])] == '>'
    has_wind |= grid[(y + time) % len(grid)][x] == '^'
    has_wind |= grid[(y - time) % len(grid)][x] == 'v'

    return not has_wind

def part1():
    grid = [line[1:-1] for line in input[1:-1]]

    y, x = 0, input[0].index('.')

    q = PriorityQueue()
    q.put((0, x, y))
    seen = set()

    while not q.empty():
        time, x, y = q.get()

        if (time, x, y) in seen: continue
        seen.add((time, x, y))

        if x == len(grid[0]) - 1 and y == len(grid): return time

        if can_move(grid, x, y, time + 1): q.put((time + 1, x, y))
        for d in [-1, 1]:
            if can_move(grid, x+d, y, time + 1): q.put((time + 1, x+d, y))
            if can_move(grid, x, y+d, time + 1): q.put((time + 1, x, y+d))

def part2():
    grid = [line[1:-1] for line in input[1:-1]]
    goals = [(len(grid[0]) - 1, len(grid)), (0, -1), (len(grid[0]) - 1, len(grid))]

    y, x = 0, input[0].index('.')

    q = PriorityQueue()
    q.put((0, x, y, 0))
    seen = set()

    while not q.empty():
        time, x, y, g = q.get()

        if (time, x, y, g) in seen: continue
        seen.add((time, x, y, g))

        if x == goals[g][0] and y == goals[g][1]:
            g += 1
            if g == len(goals):
                return time

        if can_move(grid, x, y, time + 1): q.put((time + 1, x, y, g))
        for d in [-1, 1]:
            if can_move(grid, x+d, y, time + 1): q.put((time + 1, x+d, y, g))
            if can_move(grid, x, y+d, time + 1): q.put((time + 1, x, y+d, g))

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
