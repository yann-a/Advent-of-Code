from aoc import AOC
from intcode import *

aoc = AOC(21,  2019, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    program = list(map(int, input[0].split(',')))
    intcode = IntCodeProgram(program)

    springscript_program = """
        NOT A T
        OR T J
        NOT B T
        OR T J
        NOT C T
        OR T J
        AND D J
        WALK
    """

    for line in springscript_program.strip().split('\n'):
        for c in line.strip():
            intcode.addInput(ord(c))
        intcode.addInput(ord('\n'))

    intcode.run()

    while len(intcode.output) > 0:
        r = intcode.getOutput()
        try:
            print(chr(r), end='')
        except:
            return r

def part2():
    program = list(map(int, input[0].split(',')))
    intcode = IntCodeProgram(program)

    springscript_program = """
        NOT A T
        OR T J
        NOT B T
        AND D T
        OR T J
        NOT C T
        AND D T
        AND H T
        OR T J
        RUN
    """

    for line in springscript_program.strip().split('\n'):
        for c in line.strip():
            intcode.addInput(ord(c))
        intcode.addInput(ord('\n'))

    intcode.run()

    while len(intcode.output) > 0:
        r = intcode.getOutput()
        try:
            print(chr(r), end='')
        except:
            return r

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
