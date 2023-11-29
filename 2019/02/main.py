from aoc import AOC

aoc = AOC(2,  2019, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def run(program):
    pc = 0
    while True:
        if program[pc] == 1: program[program[pc + 3]] = program[program[pc + 1]] + program[program[pc + 2]]
        elif program[pc] == 2: program[program[pc + 3]] = program[program[pc + 1]] * program[program[pc + 2]]
        elif program[pc] == 99: return
        else: raise OverflowError

        pc += 4

def part1(noun=12, verb=2):
    program = list(map(int, input[0].split(',')))
    program[1:3] = [noun, verb]
    run(program)

    return program[0]

def part2():
    for noun in range(0, 100):
        for verb in range(0, 100):
            if part1(noun, verb) == 19690720:
                return 100 * noun + verb

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
