from aoc import AOC

aoc = AOC(6,  2024, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

h = len(input)
w = len(input[0])

DIRS = [(-1, 0), (0, 1), [1, 0], (0, -1)]

def find_guard():
    for y in range(h):
        for x in range(w):
            if input[y][x] == '^':
                return (y, x)

def print_grid(grid, all_guard_pos):
    for y in range(h):
        for x in range(w):
            if grid[y][x] == '#':
                print('#', end='')
            elif (y, x) in all_guard_pos:
                print('X', end='')
            else:
                print(' ', end='')
        print()

def part1():
    guard_pos = find_guard()
    guard_dir = 0
    all_guard_pos = set([guard_pos])

    def move_guard(guard_pos, guard_dir):
        new_pos = (guard_pos[0] + DIRS[guard_dir][0], guard_pos[1] + DIRS[guard_dir][1])
        while (0 <= new_pos[0] < h and 0 <= new_pos[1] < w) and input[new_pos[0]][new_pos[1]] == '#':
            guard_dir = (guard_dir + 1) % 4
            new_pos = (guard_pos[0] + DIRS[guard_dir][0], guard_pos[1] + DIRS[guard_dir][1])

        return new_pos, guard_dir, (0 <= new_pos[0] < h and 0 <= new_pos[1] < w)

    while True:
        new_pos, guard_dir, isin = move_guard(guard_pos, guard_dir)

        if not isin:
            return len(all_guard_pos)

        guard_pos = new_pos
        all_guard_pos.add(guard_pos)

def part2():
    def explore_grid(grid, guard_pos, guard_dir, all_guard_pos, all_guard_pos_dir, placed_obstacle, obstacle_pos):
        obst_pos = set()

        def move_guard(guard_pos, guard_dir):
            new_pos = (guard_pos[0] + DIRS[guard_dir][0], guard_pos[1] + DIRS[guard_dir][1])
            while (0 <= new_pos[0] < h and 0 <= new_pos[1] < w) and grid[new_pos[0]][new_pos[1]] == '#':
                guard_dir = (guard_dir + 1) % 4
                new_pos = (guard_pos[0] + DIRS[guard_dir][0], guard_pos[1] + DIRS[guard_dir][1])

            return new_pos, guard_dir, (0 <= new_pos[0] < h and 0 <= new_pos[1] < w)

        while True:
            new_pos, new_guard_dir, isin = move_guard(guard_pos, guard_dir)

            if not isin:
                break
            if (new_pos, new_guard_dir) in all_guard_pos_dir:
                obst_pos.add(obstacle_pos)
                break
            if new_pos not in all_guard_pos and not placed_obstacle:
                new_grid = [line[:] for line in grid]
                new_grid[new_pos[0]][new_pos[1]] = '#'
                obst_pos |= explore_grid(new_grid, guard_pos, guard_dir, all_guard_pos.copy(), all_guard_pos_dir.copy(), True, new_pos)

            guard_pos = new_pos
            guard_dir = new_guard_dir
            all_guard_pos.add(guard_pos)
            all_guard_pos_dir.add((guard_pos, guard_dir))

        return obst_pos

    guard_pos = find_guard()
    guard_dir = 0
    all_guard_pos = set([guard_pos])
    all_guard_pos_dir = set([(guard_pos, guard_dir)])

    grid = [list(line) for line in input]

    return len(explore_grid(grid, guard_pos, guard_dir, all_guard_pos, all_guard_pos_dir, False, None))

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
