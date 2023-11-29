from aoc import AOC
from collections import defaultdict
from queue import PriorityQueue

aoc = AOC(20,  2019, __file__)

input = aoc.input.split('\n')
#input = open('example', 'r').read().split('\n')

def find_portals():
    portals = defaultdict(list)

    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x].isalpha():
                if x + 1 < len(input[0]) and input[y][x + 1].isalpha():
                    if x + 2 < len(input[0]) and input[y][x + 2] == '.':
                        portals[input[y][x] + input[y][x + 1]].append((y, x + 2))
                    else:
                        portals[input[y][x] + input[y][x + 1]].append((y, x - 1))
                if y + 1 < len(input) and input[y + 1][x].isalpha():
                    if y + 2 < len(input) and input[y + 2][x] == '.':
                        portals[input[y][x] + input[y + 1][x]].append((y + 2, x))
                    else:
                        portals[input[y][x] + input[y + 1][x]].append((y - 1, x))

    return portals

def isouter(y, x):
    return y == 2 or y == len(input) - 3 or x == 2 or x == len(input[0]) - 3

def part1():
    seen = [[False for _ in range(len(input[0]))] for _ in range(len(input))]

    portals = find_portals()

    q = PriorityQueue()
    q.put((0, portals['AA'][0]))

    while not q.empty():
        (p, (y, x)) = q.get()

        if seen[y][x]:
            continue

        if (y, x) == portals['ZZ'][0]:
            return p

        seen[y][x] = True
        for d in [-1, 1]:
            if input[y][x + d] == '.':
                q.put((p + 1, (y, x + d)))
            if input[y + d][x] == '.':
                q.put((p + 1, (y + d, x)))

            portal_names = [name for name in portals if (y, x) in portals[name]]

            if len(portal_names) > 0:
                portal_name = portal_names[0]
                if len(portals[portal_name]) > 1:
                    id = portals[portal_name].index((y, x))
                    oy, ox = portals[portal_name][1 - id]

                    q.put((p + 1, (oy, ox)))

def part2():
    seen = [[[False for _ in range(len(input[0]))] for _ in range(len(input))] for _ in range(1000)]

    portals = find_portals()

    sy, sx = portals['AA'][0]

    q = PriorityQueue()
    q.put((0, (0, sy, sx)))

    while not q.empty():
        (p, (l, y, x)) = q.get()

        if seen[l][y][x]:
            continue

        if l == 0 and (y, x) == portals['ZZ'][0]:
            return p

        seen[l][y][x] = True
        for d in [-1, 1]:
            if input[y][x + d] == '.':
                q.put((p + 1, (l, y, x + d)))
            if input[y + d][x] == '.':
                q.put((p + 1, (l, y + d, x)))

            portal_names = [name for name in portals if (y, x) in portals[name]]

            if len(portal_names) > 0:
                portal_name = portal_names[0]
                if len(portals[portal_name]) > 1:
                    id = portals[portal_name].index((y, x))
                    oy, ox = portals[portal_name][1 - id]

                    if isouter(y, x):
                        if l > 0:
                            q.put((p + 1, (l - 1, oy, ox)))
                    else:
                        q.put((p + 1, (l + 1, oy, ox)))

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
