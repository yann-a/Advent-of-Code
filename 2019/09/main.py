from aoc import AOC
from intcode import *

aoc = AOC(9,  2019, __file__)

input = aoc.input.strip().split('\n')
#input = '104,1125899906842624,99'.strip().split('\n')

def part1():
    program = list(map(int, input[0].split(',')))
    intcode = IntCodeProgram(program, [1])
    intcode.run()
    return intcode.output[0]

def part2():
    program = list(map(int, input[0].split(',')))
    intcode = IntCodeProgram(program, [2])
    intcode.run()
    return intcode.output[0]

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
