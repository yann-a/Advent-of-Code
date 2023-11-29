from aoc import AOC
from intcode import *
from itertools import permutations

aoc = AOC(7,  2019, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    m = 0
    for p in permutations(range(5)):
        val = 0
        for i in range(5):
            program = list(map(int, input[0].split(',')))
            inp = [p[i], val]
            intcode = IntCodeProgram(program, inp)
            intcode.run()
            val = intcode.getOutput()
        m = max(m, val)
    return m

def test_permutation(p):
    program = list(map(int, input[0].split(',')))
    programs = [IntCodeProgram(program[:], [p[i]]) for i in range(5)]

    val = 0
    while True:
        for i in range(5):
            programs[i].addInput(val)
            done = programs[i].run()
            val = programs[i].getOutput()

            if done and i == 4: return val

def part2():
    m = 0
    for p in permutations(range(5, 10)):
        m = max(m, test_permutation(p))
    return m

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
