from aoc import AOC
from queue import PriorityQueue
from functools import cache

import sys
sys.setrecursionlimit(10_000)

aoc = AOC(23,  2023, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

DIRS = [(0, 1, '>'), (0, -1, '<'), (1, 0, 'v'), (-1, 0, '^')]
SLOPES = '><v^'

def part1():
    path = set([(0, 1)])
    def dfs(y, x):
        if y == len(input) - 1 and x == len(input[0]) - 2:
            return len(path) - 1

        m = 0
        for dy, dx, slope in DIRS:
            if input[y][x] in SLOPES and input[y][x] != slope:
                continue

            if not (0 <= y + dy < len(input) and 0 <= x + dx < len(input[0])):
                continue

            if (y + dy, x + dx) in path or input[y + dy][x + dx] == '#':
                continue

            path.add((y + dy, x + dx))
            m = max(m, dfs(y + dy, x + dx))
            path.remove((y + dy, x + dx))

        if m == 0:
            return -1_000_000
        return m
    return dfs(0, 1)


def part2():
    important_nodes = [(0, 1), (len(input) - 1, len(input[0]) - 2)]
    ok_dirs = [[(1, 0)], [(-1, 0)]]
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] == '#':
                continue

            ok_dirs_ = []
            for dy, dx, _ in DIRS:
                if 0 <= y + dy < len(input) and 0 <= x + dx < len(input[0]) and input[y + dy][x + dx] != '#':
                    ok_dirs_.append((dy, dx))

            if len(ok_dirs_) > 2:
                important_nodes.append((y, x))
                ok_dirs.append(ok_dirs_)

    neighbours = [[] for _ in range(len(important_nodes))]
    for i in range(len(important_nodes)):
        for dy, dx in ok_dirs[i]:
            y, x = important_nodes[i]
            ny, nx = y + dy, x + dx
            l = 1
            while (ny, nx) not in important_nodes:
                py, px = y, x
                y, x = ny, nx
                dfound = 0
                ds = []
                for dy, dx, _ in DIRS:
                    if 0 <= y + dy < len(input) and 0 <= x + dx < len(input[0]) and input[y + dy][x + dx] != '#' and (y + dy, x + dx) != (py, px):
                        ny, nx = y + dy, x + dx
                        dfound += 1
                        ds.append((dy, dx))

                assert(dfound == 1)
                l += 1

            neighbours[i].append((important_nodes.index((ny, nx)), l))

    path = set([0])
    def dfs(i):
        if i == 1:
            return 0
        
        m = 0
        for j, l in neighbours[i]:
            if j not in path:
                path.add(j)
                m = max(m, l + dfs(j))
                path.remove(j)

        if m == 0:
            return -1_000_000
        return m
    
    return dfs(0)

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
