from aoc import AOC
from collections import defaultdict

aoc = AOC(7,  2025, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    h, w = len(input), len(input[0])

    xs = None
    for x in range(w):
        if input[0][x] == 'S':
            xs = x
            break

    xs = set([xs])
    y = 0
    split = 0
    while y + 1 < h:
        nxs = set()
        y += 1

        for x in xs:
            if input[y][x] == '^':
                nxs.add(x - 1)
                nxs.add(x + 1)
                split += 1
            else:
                nxs.add(x)

        xs = nxs

    return split

def part2():
    h, w = len(input), len(input[0])

    xs = None
    for x in range(w):
        if input[0][x] == 'S':
            xs = x
            break

    xs = {xs: 1}
    y = 0
    while y + 1 < h:
        nxs = defaultdict(int)
        y += 1

        for x in xs:
            if input[y][x] == '^':
                nxs[x - 1] += xs[x]
                nxs[x + 1] += xs[x]
            else:
                nxs[x] += xs[x]

        xs = nxs

    return sum(xs.values())

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
