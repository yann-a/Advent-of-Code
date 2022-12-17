from aoc import AOC

aoc = AOC(21,  2018, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

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
    # Last three lines of program check whether r0 = r5, so we just need to get the value of r5 at that point
    ip_reg = int(input[0][3:])
    ip = 0
    registers = [0] * 6
    while True:
        registers[ip_reg] = ip
        op, i1, i2, o = input[ip + 1].split()
        sim_operation(op, int(i1), int(i2), int(o), registers)
        ip = registers[ip_reg] + 1

        if ip == 28:
            break

    return registers[5]

def part2():
    seen, last = set(), 0
    ip_reg = int(input[0][3:])
    ip = 0
    registers = [0] * 6
    while True:
        registers[ip_reg] = ip
        op, i1, i2, o = input[ip + 1].split()
        sim_operation(op, int(i1), int(i2), int(o), registers)
        ip = registers[ip_reg] + 1

        if ip == 28:
            if registers[5] in seen: return last
            last = registers[5]
            seen.add(registers[5])

def part22():
    seen, last = set(), 0
    ip_reg, ip = 1, 0
    r = [0] * 6
    while True:
        r[ip_reg] = ip
        if ip == 0: r[5] = 123
        elif ip == 1: r[5] &= 456
        elif ip == 2: r[5] = 1 if r[5] == 72 else 0
        elif ip == 3: r[1] = r[5] + r[1]
        elif ip == 4: r[1] = 0
        elif ip == 5: r[5] = 0
        elif ip == 6: r[4] = r[5] | 65_536
        elif ip == 7: r[5] = 3_935_295
        elif ip == 8: r[2] = r[4] & 255
        elif ip == 9: r[5] += r[2]
        elif ip == 10: r[5] &=  16_777_215
        elif ip == 11: r[5] *= 65_899
        elif ip == 12: r[5] &= 16_777_215
        elif ip == 13: r[2] = 1 if 256 > r[4] else 0
        elif ip == 14: r[1] += r[2]
        elif ip == 15: r[1] += 1
        elif ip == 16: r[1] = 27
        elif ip == 17: r[2] = 0
        elif ip == 18: r[3] = r[2] + 1
        elif ip == 19: r[3] *= 256
        elif ip == 20: r[3] = 1 if r[3] > r[4] else 0
        elif ip == 21: r[1] = r[3] + r[1]
        elif ip == 22: r[1] += 1
        elif ip == 23: r[1] = 25
        elif ip == 24: r[2] += 1
        elif ip == 25: r[1] = 17
        elif ip == 26: r[4] = r[2]
        elif ip == 27: r[1] = 7
        elif ip == 28: r[2] = 1 if r[5] == r[0] else 0
        elif ip == 29: r[1] += r[2]
        elif ip == 30: r[1] = 5
        ip = r[ip_reg] + 1

        if ip == 28:
            if r[5] in seen: return last
            last = r[5]
            seen.add(r[5])
 
p1_sol = part1()
p2_sol = part22()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
aoc.submit(2, p2_sol)
