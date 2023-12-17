from aoc import AOC
from queue import PriorityQueue

aoc = AOC(17,  2023, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def solve(mind, maxd):
    q = PriorityQueue()
    q.put((0, 0, 0, None)) # total_heat, y, x, forbidden_dir
    seen = set()
    heats = {}

    while not q.empty():
        heat, y, x, fdir = q.get()

        if y == len(input) - 1 and x == len(input[0]) - 1:
            return heat

        if (y, x, fdir) in seen:
            continue

        seen.add((y, x, fdir))

        for dir in DIRS:
            if dir == fdir or (-dir[0], -dir[1]) == fdir:
                continue

            cumul_heat = 0
            for dist in range(1, maxd + 1):
                ny = y + dir[0] * dist
                nx = x + dir[1] * dist

                if not (0 <= ny < len(input) and 0 <= nx < len(input[0])):
                    break

                cumul_heat += int(input[ny][nx])

                if dist < mind:
                    continue

                if (ny, nx, dir) in heats and heats[(ny, nx, dir)] <= cumul_heat:
                    continue
                heats[(ny, nx, dir)] = cumul_heat
                q.put((heat + cumul_heat, ny, nx, dir))

def part1():
    return solve(1, 3)

def part2():
    return solve(4, 10)

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
