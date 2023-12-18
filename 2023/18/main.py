from aoc import AOC
from collections import defaultdict
import numpy as np

aoc = AOC(18,  2023, __file__)

input = aoc.input.strip().split('\n')
#input = open('example', 'r').read().strip().split('\n')

joints = {'UR': 'F', 'LD': 'F', 'UL': '7', 'RD': '7', 'DR': 'L', 'LU': 'L', 'DL': 'J', 'RU': 'J'}

def part1():
    y, x = 0, 0
    walls = set([(y, x)])
    turns = {}
    for i in range(len(input)):
        line = input[i]
        nextline = input[(i + 1) % len(input)]
        direction, length, _ = line.split()
        nextdirection, _, _ = nextline.split()

        for _ in range(int(length)):
            x = x + (direction == 'R') - (direction == 'L')
            y = y + (direction == 'D') - (direction == 'U')
            walls.add((y, x))
            turns[(y, x)] = '|' if direction in 'UD' else '-'

        turns[(y, x)] = joints[direction + nextdirection]

    miny = min(point[0] for point in walls)
    maxy = max(point[0] for point in walls)
    minx = min(point[1] for point in walls)
    maxx = max(point[1] for point in walls)

    area = 0
    for y in range(miny, maxy + 1):
        inside = False
        for x in range(minx, maxx + 1):
            if (y, x) in walls:
                if turns[(y, x)] in '|F7':
                    inside = not inside
            else:
                area += inside

    return area + len(walls)

def extract(colorcode):
    return 'RDLU'[int(colorcode[-2])], int(colorcode[2:-2], 16)

# https://stackoverflow.com/a/30408825
# Shoelace formula
def PolyArea(x, y):
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))

def part2():
    y, x = 0, 0
    nb_pts = 0
    xs, ys = [], []

    for i in range(len(input)):
        line = input[i]
        _, _, colorcode = line.split()

        direction, length = extract(colorcode)

        x = x + length * ((direction == 'R') - (direction == 'L'))
        y = y + length * ((direction == 'D') - (direction == 'U'))

        nb_pts += length
        xs.append(x)
        ys.append(y)

    A = int(PolyArea(xs, ys))
    
    # Add half squares lying on the outside (similar to Pick's theorem)
    return A + 1 + nb_pts // 2

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
