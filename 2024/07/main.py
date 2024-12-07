from aoc import AOC
from itertools import product

aoc = AOC(7,  2024, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    _s = 0    
    for line in input:
        total, operands = line.split(': ')
        total = int(total)
        operands = list(map(int, operands.split()))

        for operations in product(['+', '*'], repeat=len(operands) - 1):
            s = operands[0]
            for i in range(len(operations)):
                if operations[i] == '+':
                    s += operands[i + 1]
                else:
                    s *= operands[i + 1]

            if s == total:
                _s += total
                break

    return _s

def part2():
    def aux(total, s, operands, i):
        if i == len(operands):
            return s == total

        for operation in ['+', '*', '|']:
            if operation == '+':
                ns = s + operands[i]
            elif operation == '*':
                ns = s * operands[i]
            else:
                ns = int(str(s) + str(operands[i]))

            # Don't iterate over all elements of the product,
            # prune as early as possible since s is increasing
            if ns > total:
                continue

            if aux(total, ns, operands, i + 1):
                return True

        return False

    _s = 0    
    for line in input:
        total, operands = line.split(': ')
        total = int(total)
        operands = list(map(int, operands.split()))

        if aux(total, operands[0], operands, 1):
            _s += total

    return _s

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
