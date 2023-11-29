from aoc import AOC
from intcode import *
from queue import PriorityQueue

aoc = AOC(15,  2019, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    program = list(map(int, input[0].split(',')))
    intcode = IntCodeProgram(program)
    seen = set()
    intcodes = {(0, 0): intcode}

    q = PriorityQueue()
    q.put((0, 0, 0))

    while not q.empty():
        dist, x, y = q.get()
        seen.add((x, y))

        if len(intcodes[(x, y)].output) > 0 and intcodes[(x, y)].output[-1] == 0: continue
        if len(intcodes[(x, y)].output) > 0 and intcodes[(x, y)].output[-1] == 2: return dist

        for d in range(1, 5):
            nx = x + (d == 4) - (d == 3)
            ny = y + (d == 1) - (d == 2)

            if (nx, ny) not in seen:
                q.put((dist + 1, nx, ny))
                intcodes[(nx, ny)] = intcodes[(x, y)].copy()
                intcodes[(nx, ny)].addInput(d)
                intcodes[(nx, ny)].run()

def part2():
    program = list(map(int, input[0].split(',')))
    intcode = IntCodeProgram(program)
    seen = set()
    intcodes = {(0, 0): intcode}

    q = PriorityQueue()
    q.put((0, 0, 0))
    while not q.empty():
        dist, x, y = q.get()
        seen.add((x, y))

        if len(intcodes[(x, y)].output) > 0 and intcodes[(x, y)].output[-1] == 0: continue
        if len(intcodes[(x, y)].output) > 0 and intcodes[(x, y)].output[-1] == 2: sx, sy = x, y

        for d in range(1, 5):
            nx = x + (d == 4) - (d == 3)
            ny = y + (d == 1) - (d == 2)

            if (nx, ny) not in seen:
                q.put((dist + 1, nx, ny))
                intcodes[(nx, ny)] = intcodes[(x, y)].copy()
                intcodes[(nx, ny)].addInput(d)
                intcodes[(nx, ny)].run()

    seen = set([(sx, sy)])
    outside_bound = set([(sx, sy)])
    seconds = -1
    while len(outside_bound) > 0:
        seconds += 1
        new_outside_bound = set()
        for x, y in outside_bound:
            for d in range(1, 5):
                nx = x + (d == 4) - (d == 3)
                ny = y + (d == 1) - (d == 2)

                if (nx, ny) not in seen and (nx, ny) in intcodes:
                    seen.add((nx, ny))
                    if len(intcodes[(nx, ny)].output) > 0 and intcodes[(nx, ny)].output[-1] != 0:
                        new_outside_bound.add((nx, ny))

        outside_bound = new_outside_bound

    return seconds

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
