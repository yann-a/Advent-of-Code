from aoc import AOC

aoc = AOC(16,  2018, __file__)

input = aoc.input.strip().split('\n\n\n\n')
#input = aoc.get_example(0).strip().split('\n\n\n\n')

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

def set_equiv(op, opcode, op_to_opcode, opcode_to_op):
    op_to_opcode[op] = set([opcode])
    opcode_to_op[opcode] = set([op])

    for _op in operations:
        if _op != op:
            if opcode in op_to_opcode[_op]:
                op_to_opcode[_op].remove(opcode)

    for _opcode in range(16):
        if _opcode != opcode:
            if op in opcode_to_op[_opcode]:
                opcode_to_op[_opcode].remove(op)

def part1():
    s = 0
    for test in input[0].split('\n\n'):
        test = test.split('\n')
        initial_registers = test[0][8:]
        opcode, i1, i2, o = map(int, test[1].split())
        final_registers = eval(test[2][8:])

        nb_op = 0
        for op in operations:
            registers = eval(initial_registers)
            sim_operation(op, i1, i2, o, registers)

            if registers == final_registers:
                nb_op += 1

        if nb_op >= 3:
            s += 1
    
    return s

def part2():
    opcode_to_op = {op_code: set(operations) for op_code in range(16)}
    op_to_opcode = {op: set(range(16)) for op in operations}
    for test in input[0].split('\n\n'):
        test = test.split('\n')
        initial_registers = test[0][8:]
        opcode, i1, i2, o = map(int, test[1].split())
        final_registers = eval(test[2][8:])

        for op in operations:
            registers = eval(initial_registers)
            sim_operation(op, i1, i2, o, registers)
            
            if registers != final_registers:
                if op in opcode_to_op[opcode]:
                    opcode_to_op[opcode].remove(op)

                    if len(opcode_to_op[opcode]) == 1:
                        real_op = list(opcode_to_op[opcode])[0]
                        set_equiv(real_op, opcode, op_to_opcode, opcode_to_op)

                if opcode in op_to_opcode[op]:
                    op_to_opcode[op].remove(opcode)

                    if len(op_to_opcode[op]) == 1:
                        real_opcode = list(op_to_opcode[op])[0]
                        set_equiv(op, real_opcode, op_to_opcode, opcode_to_op)

    for _ in range(2):
        for opcode in range(16):
            if sum(opcode in op_to_opcode[op] for op in operations) == 1:
                op = [op for op in operations if opcode in op_to_opcode[op]][0]
                set_equiv(op, opcode, op_to_opcode, opcode_to_op)

    opcode_to_op = {opcode: list(opcode_to_op[opcode])[0] for opcode in range(16)}

    registers = [0, 0, 0, 0]
    for instruction in input[1].split('\n'):
        opcode, i1, i2, o = map(int, instruction.split())
        sim_operation(opcode_to_op[opcode], i1, i2, o, registers)

    return registers[0]

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
