from aoc import AOC
from collections import namedtuple

aoc = AOC(22,  2023, __file__)

input = aoc.input.strip().split('\n')
#input = open('example', 'r').read().strip().split('\n')

Brick = namedtuple("Brick", "sx sy sz ex ey ez")

def lower_x(brick1, brick2):
    return max(brick1.sx, brick1.ex) < min(brick2.sx, brick2.ex)

def lower_y(brick1, brick2):
    return max(brick1.sy, brick1.ey) < min(brick2.sy, brick2.ey)

def is_above(brick1, brick2):
    not_intersect_x = lower_x(brick1, brick2) or lower_x(brick2, brick1)
    not_intersect_y = lower_y(brick1, brick2) or lower_y(brick2, brick1)

    not_intersect = not_intersect_x or not_intersect_y
    intersect = not not_intersect

    return intersect and min(brick1.sz, brick1.ez) > max(brick2.sz, brick2.ez)

def is_resting_on(brick1, brick2):
    return min(brick1.sz, brick1.ez) - 1 == max(brick2.sz, brick2.ez)

def part1():
    bricks = []
    for line in input:
        start, end = line.split('~')
        brick = Brick(*map(int, start.split(',')), *map(int, end.split(',')))

        bricks.append(brick)

    bricks.sort(key=lambda brick: min(brick.sz, brick.ez))

    above = [[] for _ in bricks]
    for i in range(len(bricks)):
        for j in range(len(bricks)):
            if is_above(bricks[i], bricks[j]):
                above[i].append(j)

    supported_by = [[] for _ in bricks]
    for i in range(len(bricks)):
        while min(bricks[i].sz, bricks[i].ez) > 1 and not any(is_resting_on(bricks[i], bricks[j]) for j in above[i]):
            bricks[i] = Brick(bricks[i].sx, bricks[i].sy, bricks[i].sz - 1, bricks[i].ex, bricks[i].ey, bricks[i].ez - 1)
        else:
            for j in above[i]:
                if is_resting_on(bricks[i], bricks[j]):
                    supported_by[i].append(j)

    is_the_only_supporter_of_some_brick = set()
    for i in range(len(bricks)):
        if len(supported_by[i]) == 1:
            is_the_only_supporter_of_some_brick.add(supported_by[i][0])

    return len(bricks) - len(is_the_only_supporter_of_some_brick)        

def part2():
    bricks = []
    for line in input:
        start, end = line.split('~')
        brick = Brick(*map(int, start.split(',')), *map(int, end.split(',')))

        bricks.append(brick)

    bricks.sort(key=lambda brick: min(brick.sz, brick.ez))

    above = [[] for _ in bricks]
    for i in range(len(bricks)):
        for j in range(len(bricks)):
            if is_above(bricks[i], bricks[j]):
                above[i].append(j)

    supported_by = [[] for _ in bricks]
    for i in range(len(bricks)):
        while min(bricks[i].sz, bricks[i].ez) > 1 and not any(is_resting_on(bricks[i], bricks[j]) for j in above[i]):
            bricks[i] = Brick(bricks[i].sx, bricks[i].sy, bricks[i].sz - 1, bricks[i].ex, bricks[i].ey, bricks[i].ez - 1)
        else:
            for j in above[i]:
                if is_resting_on(bricks[i], bricks[j]):
                    supported_by[i].append(j)

    s = 0
    for i in range(len(bricks)):
        fell = [False for _ in range(len(bricks))]
        fell[i] = True

        for j in range(len(bricks)):
            if len(supported_by[j]) > 0 and all(fell[k] for k in supported_by[j]):
                fell[j] = True

        s += sum(fell) - 1

    return s

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
