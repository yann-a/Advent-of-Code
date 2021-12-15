from aoc import AOC
import sys
sys.setrecursionlimit(10_000)

aoc = AOC(11,  2021, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

grid = [list(map(int, i)) for i in input]


def simulate(n, grid):
    nb_flash = 0
    first_all_flash = -1

    def step(grid):
        nb_flash = 0
        flashed = [[False for _ in range(10)] for _ in range(10)]
        grid = [[octopus + 1 for octopus in line] for line in grid]

        def browse(i, j, flashed, grid):
            flashed[i][j] = True
            nb_flash = 1

            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if di != 0 or dj != 0:
                        if 0 <= i + di and i + di < 10:
                            if 0 <= j + dj and j + dj < 10:
                                grid[i + di][j + dj] += 1
                                if not flashed[i + di][j + dj] and grid[i + di][j + dj] > 9:
                                    nb_flash += browse(i + di, j + dj, flashed, grid)
            return nb_flash

        for i, line in enumerate(grid):
            for j, octopus in enumerate(line):
                if octopus > 9 and not flashed[i][j]:
                    nb_flash += browse(i, j, flashed, grid)

        return nb_flash, [[octopus if octopus <= 9 else 0 for octopus in line] for line in grid]

    for i in range(n):
        step_flash, grid = step(grid)
        nb_flash += step_flash
        if first_all_flash < 0 and step_flash == 100:
            first_all_flash = i + 1

    return nb_flash, first_all_flash


p1_sol, _ = simulate(100, grid)
_, p2_sol = simulate(1_000, grid)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
