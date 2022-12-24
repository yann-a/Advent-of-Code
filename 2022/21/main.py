from aoc import AOC
from collections import defaultdict

aoc = AOC(21,  2022, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def compute(operations, operation, results):
    operands = operations[operation]

    if operation in results: pass
    elif len(operations[operation]) == 1: results[operation] = int(operations[operation][0])
    else:
        compute(operations, operands[0], results)
        compute(operations, operands[2], results)
        results[operation] = eval(str(results[operands[0]]) + operands[1] + str(results[operands[2]]))

def compute_literal(operations, operation, results):
    operands = operations[operation]

    if operation in results: pass
    elif operation == 'humn': results[operation] = 'hmn'
    elif len(operations[operation]) == 1: results[operation] = int(operations[operation][0])
    else:
        compute_literal(operations, operands[0], results)
        compute_literal(operations, operands[2], results)
        if isinstance(results[operands[0]], int) and isinstance(results[operands[2]], int):
            results[operation] = eval(str(results[operands[0]]) + operands[1] + str(results[operands[2]]))
        else:
            results[operation] = '(' + str(results[operands[0]]) + operands[1] + str(results[operands[2]]) + ')'

def part1():
    operations = {}
    for line in input:
        name, operation = line.split(': ')
        operation = operation.split()

        operations[name] = operation

    results = {}
    compute(operations, 'root', results)
    return int(results['root'])

def part2_check(value):
    operations = {}
    for line in input:
        name, operation = line.split(': ')
        operation = operation.split()

        operations[name] = operation

    operations['root'][1] = '=='
    operations['humn'][0] = value
    
    results = {}
    compute(operations, 'root', results)
    return results['root']

def part2():
    operations = {}
    appears_in = {}
    for line in input:
        name, operation = line.split(': ')
        operation = operation.split()

        operations[name] = operation

        if len(operation) > 1:
            appears_in[operation[0]] = name
            appears_in[operation[2]] = name

    operations['root'][1] = '=='

    from_human_to_root = []
    node = 'humn'
    while node != 'root':
        from_human_to_root.append(node)
        node = appears_in[node]
    from_human_to_root.append('root')

    desired_value = 0
    for i in range(len(from_human_to_root) - 2, -1, -1):
        node = from_human_to_root[i]
        prev_node = from_human_to_root[i+1]

        other_index = 2 if operations[prev_node][0] == node else 0
        results = {}
        compute(operations, operations[prev_node][other_index], results)
        other_value = results[operations[prev_node][other_index]]

        if operations[prev_node][1] == '==': desired_value = other_value
        elif operations[prev_node][1] == '+': desired_value = desired_value - other_value
        elif operations[prev_node][1] == '-': desired_value = other_value + (-1 if other_index == 0 else 1) * desired_value
        elif operations[prev_node][1] == '*': desired_value = desired_value // other_value
        elif operations[prev_node][1] == '/': 
            if other_index == 0: desired_value = other_value // desired_value
            else: desired_value = other_value * desired_value

    if part2_check(desired_value):
        return int(desired_value)

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
