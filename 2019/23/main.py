from aoc import AOC
from intcode import *

aoc = AOC(23,  2019, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    program = list(map(int, input[0].split(',')))
    computers = [IntCodeProgram(program, [i]) for i in range(50)]

    while True:
        for computer in computers: computer.run()

        for computer in computers:
            if len(computer.output) > 0:
                dest = computer.getOutput()
                x = computer.getOutput()
                y = computer.getOutput()

                if dest == 255: return y
                computers[dest].addInput(x)
                computers[dest].addInput(y)

        for computer in computers:
            if len(computer.input) == 0:
                computer.addInput(-1)

def part2():
    program = list(map(int, input[0].split(',')))
    computers = [IntCodeProgram(program, [i]) for i in range(50)]

    last_nat_y = None
    last_nat = (0, 0)

    while True:
        idle = True
        for computer in computers: computer.run()

        for computer in computers:
            if len(computer.output) > 0:
                dest = computer.getOutput()
                x = computer.getOutput()
                y = computer.getOutput()

                if dest == 255: last_nat = (x, y)
                else:
                    computers[dest].addInput(x)
                    computers[dest].addInput(y)
                idle = False

        if idle:
            if last_nat[1] == last_nat_y:
                return last_nat_y

            computers[0].addInput(last_nat[0])
            computers[0].addInput(last_nat[1])
            last_nat_y = last_nat[1]

        for computer in computers:
            if len(computer.input) == 0:
                computer.addInput(-1)

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
