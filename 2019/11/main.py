from aoc import AOC
from intcode import *
from collections import defaultdict

aoc = AOC(11,  2019, __file__)

input = aoc.input.strip().split('\n')

def part1():
    program = list(map(int, input[0].split(',')))
    intcode = IntCodeProgram(program, [0])
    
    on = defaultdict(int)
    x, y, d = 0, 0, 0
    while not intcode.run():
        nc = intcode.getOutput()
        on[(x, y)] = 1 - on[(x, y)]

        nd = intcode.getOutput()
        if nd == 0: d = (d - 1) % 4
        else: d = (d + 1) % 4
        x = x + (d == 1) - (d == 3)
        y = y + (d == 0) - (d == 2)
        intcode.addInput(on[(x, y)])

    return len(on)

def part2():
    program = list(map(int, input[0].split(',')))
    intcode = IntCodeProgram(program, [1])
    
    on = defaultdict(int)
    on[(0, 0)] = 1
    x, y, d = 0, 0, 0
    while not intcode.run():
        nc = intcode.getOutput()
        on[(x, y)] = nc

        nd = intcode.getOutput()
        if nd == 0: d = (d - 1) % 4
        else: d = (d + 1) % 4
        x = x + (d == 1) - (d == 3)
        y = y + (d == 0) - (d == 2)
        intcode.addInput(on[(x, y)])

    for y in range(0, -6, -1):
        for x in range(43):
            print('#' if on[(x, y)] == 1 else ' ', end='')
        print()

p1_sol = part1()
part2()
p2_sol = 'EGZCRKGK'

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
