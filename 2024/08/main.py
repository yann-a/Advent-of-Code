from aoc import AOC
from collections import defaultdict

aoc = AOC(8,  2024, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

h = len(input)
w = len(input[0])

def lerp(a, b, t):
    return a * (1 - t) + b * t

def lerp_points(a, b, t):
    return (lerp(a[0], b[0], t), lerp(a[1], b[1], t))

def inbounds(p):
    return 0 <= p[0] < h and 0 <= p[1] < w

def part1():
    antenna_types = defaultdict(list)
    antinode = [[False for _ in input] for _ in input[0]]

    for y in range(h):
        for x in range(w):
            if input[y][x] != '.':
                antenna_types[input[y][x]].append((y, x))

    for antenna_type in antenna_types:
        for a1 in antenna_types[antenna_type]:
            for a2 in antenna_types[antenna_type]:
                if a1 == a2:
                    continue

                yn, xn = lerp_points(a1, a2, -1)

                if inbounds((yn, xn)):
                    antinode[yn][xn] = True

    return sum(sum(line) for line in antinode)

def part2():
    antenna_types = defaultdict(list)
    antinode = [[False for _ in input] for _ in input[0]]

    for y in range(h):
        for x in range(w):
            if input[y][x] != '.':
                antenna_types[input[y][x]].append((y, x))

    for antenna_type in antenna_types:
        for a1 in antenna_types[antenna_type]:
            for a2 in antenna_types[antenna_type]:
                if a1 == a2:
                    continue

                dy = a2[0] - a1[0]
                dx = a2[1] - a1[1]

                i = 0
                while 0 <= a1[0] + i * dy < h and 0 <= a1[1] + i * dx < w:
                    antinode[a1[0] + i * dy][a1[1] + i * dx] = True
                    i += 1
                i = 0
                while 0 <= a1[0] + i * dy < h and 0 <= a1[1] + i * dx < w:
                    antinode[a1[0] + i * dy][a1[1] + i * dx] = True
                    i -= 1

    return sum(sum(line) for line in antinode)

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
