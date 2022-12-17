from aoc import AOC
from collections import defaultdict

aoc = AOC(3,  2018, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(1).strip().split('\n')

def part1():
    canvas = defaultdict(int)
    for claim in input:
        _, claim = claim.split(' @ ')
        pos, size = claim.split(': ')

        pos = list(map(int, pos.split(',')))
        size = list(map(int, size.split('x')))

        for x in range(pos[0], pos[0] + size[0]):
            for y in range(pos[1], pos[1] + size[1]):
                canvas[(x, y)] += 1

    return sum(canvas[t] > 1 for t in canvas)

def part2():
    canvas = defaultdict(int)
    for claim in input:
        _, claim = claim.split(' @ ')
        pos, size = claim.split(': ')

        pos = list(map(int, pos.split(',')))
        size = list(map(int, size.split('x')))

        for x in range(pos[0], pos[0] + size[0]):
            for y in range(pos[1], pos[1] + size[1]):
                canvas[(x, y)] += 1

    for claim in input:
        id, claim = claim.split(' @ ')
        pos, size = claim.split(': ')

        pos = list(map(int, pos.split(',')))
        size = list(map(int, size.split('x')))

        overlaps = False
        for x in range(pos[0], pos[0] + size[0]):
            for y in range(pos[1], pos[1] + size[1]):
                if canvas[(x, y)] > 1:
                    overlaps = True
        
        if not overlaps:
            return id[1:]

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
