from aoc import AOC
from intcode import *

aoc = AOC(19,  2019, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    program = list(map(int, input[0].split(',')))
    
    s = 0
    for x in range(50):
        for y in range(50):
            intcode = IntCodeProgram(program, [x, y])
            intcode.run()
            if intcode.getOutput() == 1:
                s += 1

    return s

def testpos(program, x, y):
    intcode = IntCodeProgram(program, [x, y])
    intcode.run()
    return intcode.getOutput() == 1

def part2():
    program = list(map(int, input[0].split(',')))
    
    x, y = 4, 6
    while True:
        if testpos(program, x, y):
            if testpos(program, x+99, y-99):
                return x * 10_000 + y - 99

            y += 1
        else:
            x += 1
    
p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
