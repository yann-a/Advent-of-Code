from aoc import AOC
from collections import deque

aoc = AOC(11,  2023, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def solve(factor):
    # Expand lines
    lines_to_expand = []
    for i in range(len(input)):
        if all(e != '#' for e in input[i]):
            lines_to_expand.append(i)

    # Expan cols
    cols_to_expand = []
    for i in range(len(input[1])):
        if all(e != '#' for j in range(len(input)) for e in input[j][i]):
            cols_to_expand.append(i)

    # Collect galaxies
    nodes = []
    ptl = 0
    for i in range(len(input)):
        if i in lines_to_expand:
            ptl += 1
            continue

        ptc = 0
        for j in range(len(input[0])):
            if j in cols_to_expand:
                ptc += 1
                continue

            if input[i][j] == '#':
                nodes.append((i + (factor - 1) * ptl, j + (factor - 1) * ptc))

    # Sum distances
    n, s = len(nodes), 0
    for i in range(n):
        for j in range(i):
            s += abs(nodes[i][0] - nodes[j][0]) + abs(nodes[i][1] - nodes[j][1])

    return s

def part1():
    return solve(2)

def part2(factor=1_000_000):
    return solve(factor)

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)