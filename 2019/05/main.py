from aoc import AOC

aoc = AOC(5,  2019, __file__)

input = aoc.input.strip().split('\n')
#input = '3,0,4,0,99'.strip().split('\n')

def getvalue(program, pos, mode):
    if mode == 0: return program[pos]
    elif mode == 1: return pos
    else: raise OverflowError 

def run(program, inp, out):
    pc = inp_id = 0
    while True:
        full_inst = program[pc]
        inst, modes = full_inst % 100, full_inst // 100
        if inst == 1:
            program[program[pc + 3]] = getvalue(program, program[pc + 1], modes % 10) + getvalue(program, program[pc + 2], (modes // 10) % 10)
            pc += 4
        elif inst == 2:
            program[program[pc + 3]] = getvalue(program, program[pc + 1], modes % 10) * getvalue(program, program[pc + 2], (modes // 10) % 10)
            pc += 4
        elif inst == 3:
            program[program[pc + 1]] = inp[inp_id]
            inp_id += 1
            pc += 2
        elif inst == 4:
            out.append(getvalue(program, program[pc + 1], modes % 10))
            pc += 2
        elif inst == 5:
            if getvalue(program, program[pc + 1], modes % 10) != 0:
                pc = getvalue(program, program[pc + 2], (modes // 10) % 10)
            else:
                pc += 3
        elif inst == 6:
            if getvalue(program, program[pc + 1], modes % 10) == 0:
                pc = getvalue(program, program[pc + 2], (modes // 10) % 10)
            else:
                pc += 3
        elif inst == 7:
            if getvalue(program, program[pc + 1], modes % 10) < getvalue(program, program[pc + 2], (modes // 10) % 10):
                program[program[pc + 3]] = 1
            else:
                program[program[pc + 3]] = 0
            pc += 4
        elif inst == 8:
            if getvalue(program, program[pc + 1], modes % 10) == getvalue(program, program[pc + 2], (modes // 10) % 10):
                program[program[pc + 3]] = 1
            else:
                program[program[pc + 3]] = 0
            pc += 4
        elif inst == 99: return
        else: raise OverflowError

def part1():
    program = list(map(int, input[0].split(',')))
    inp, out = [1], []
    run(program, inp, out)

    return out[-1]

def part2():
    program = list(map(int, input[0].split(',')))
    inp, out = [5], []
    run(program, inp, out)

    return out[-1]

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
