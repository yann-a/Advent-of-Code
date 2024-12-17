from aoc import AOC
import z3

aoc = AOC(17,  2024, __file__)

input = aoc.input.strip().split('\n\n')
#input = aoc.get_example(0).strip().split('\n\n')

def get_combo(operand, regs):
    if 0 <= operand <= 3:
        return operand
    else:
        return regs['ABC'[operand - 4]]

def part1():
    registers = input[0].split('\n')
    regs = {}
    for line in registers:
        line = line[9:].split(': ')
        regs[line[0]] = int(line[1])
    prog = list(map(int, input[1][9:].split(',')))
    output = []

    pc = 0
    while 0 <= pc < len(prog):
        op = prog[pc]
        if op == 0:
            regs['A'] //= (2 ** get_combo(prog[pc + 1], regs))
        elif op == 1:
            regs['B'] ^= prog[pc + 1]
        elif op == 2:
            regs['B'] = (get_combo(prog[pc + 1], regs) % 8)
        elif op == 3:
            if regs['A'] != 0:
                pc = prog[pc + 1]
                continue
        elif op == 4:
            regs['B'] ^= regs['C']
        elif op == 5:
            v = (get_combo(prog[pc + 1], regs) % 8)
            if v == 0:
                output.append(0)
            while v > 0:
                output.append(v % 10)
                v //= 10
        elif op == 6:
            regs['B'] = regs['A'] // (2 ** get_combo(prog[pc + 1], regs))
        elif op == 7:
            regs['C'] = regs['A'] // (2 ** get_combo(prog[pc + 1], regs))
        else:
            assert False
        pc += 2

    return ','.join(map(str, output))

def part2():
    prog = list(map(int, input[1][9:].split(',')))
    output_pt = 0

    s = z3.Solver()

    a_val = z3.BitVec('A', 3 * len(prog) + 1)
    regs = {
        'A': a_val,
        'B': z3.BitVecVal(0, 3 * len(prog) + 1),
        'C': z3.BitVecVal(0, 3 * len(prog) + 1)
    }

    pc = 0
    while output_pt < len(prog):
        op = prog[pc]
        if op == 0:
            regs['A'] >>= get_combo(prog[pc + 1], regs)
        elif op == 1:
            regs['B'] ^= prog[pc + 1]
        elif op == 2:
            regs['B'] = get_combo(prog[pc + 1], regs) % 8
        elif op == 3:
            pc = prog[pc + 1]
            continue
        elif op == 4:
            regs['B'] ^= regs['C']
        elif op == 5:
            val = get_combo(prog[pc + 1], regs) % 8
            s.add(val == prog[output_pt])
            output_pt += 1
        elif op == 6:
            regs['B'] = regs['A'] >> get_combo(prog[pc + 1], regs)
        elif op == 7:
            regs['C'] = regs['A'] >> get_combo(prog[pc + 1], regs)
        else:
            assert False
        pc += 2

    # Get all solutions
    min_sol = 1_000_000_000_000_000_000_000_000_000
    while s.check() == z3.sat:
        sol = s.model()[a_val].as_long()
        min_sol = min(min_sol, sol)
        s.add(a_val != sol)

    return min_sol

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
