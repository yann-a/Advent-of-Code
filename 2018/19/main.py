from aoc import AOC

aoc = AOC(19,  2018, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

operations = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr']

def sim_operation(op, i1, i2, o, registers):
    if op == 'addr': registers[o] = registers[i1] + registers[i2]
    elif op == 'addi': registers[o] = registers[i1] + i2
    elif op == 'mulr': registers[o] = registers[i1] * registers[i2]
    elif op == 'muli': registers[o] = registers[i1] * i2
    elif op == 'banr': registers[o] = registers[i1] & registers[i2]
    elif op == 'bani': registers[o] = registers[i1] & i2
    elif op == 'borr': registers[o] = registers[i1] | registers[i2]
    elif op == 'bori': registers[o] = registers[i1] | i2
    elif op == 'setr': registers[o] = registers[i1]
    elif op == 'seti': registers[o] = i1
    elif op == 'gtir': registers[o] = 1 if i1 > registers[i2] else 0
    elif op == 'gtri': registers[o] = 1 if registers[i1] > i2 else 0
    elif op == 'gtrr': registers[o] = 1 if registers[i1] > registers[i2] else 0
    elif op == 'eqir': registers[o] = 1 if i1 == registers[i2] else 0
    elif op == 'eqri': registers[o] = 1 if registers[i1] == i2 else 0
    elif op == 'eqrr': registers[o] = 1 if registers[i1] == registers[i2] else 0

def part1():
    ip_reg = int(input[0][3:])
    ip = 0
    registers = [0] * 6
    while True:
        registers[ip_reg] = ip
        op, i1, i2, o = input[ip + 1].split()
        sim_operation(op, int(i1), int(i2), int(o), registers)
        ip = registers[ip_reg] + 1

        if ip < 0 or len(input) - 2 < ip:
            break

    return registers[0]

def part2():
    # Somme des diviseurs de 10 551 355
    N = 10_551_355
    s = 0
    for n in range(1, N + 1):
        if N % n == 0:
            s += n
    return s

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
