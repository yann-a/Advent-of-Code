from aoc import AOC
from functools import cache

aoc = AOC(12,  2023, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(1).strip().split('\n')

def startgroup(record, check, i, j):
    if j >= len(check):
        return 0

    for k in range(check[j]):
        if i + k >= len(record):
            return 0
    
        if record[i + k] in '#?':
            continue
        elif record[i + k] == '.':
            return 0

    if i + check[j] < len(record) and record[i + check[j]] == '#':
        return 0

    return nbways(record, check, i + check[j] + 1, j + 1)

@cache # record, check, index in record, index in check
def nbways(record, check, i, j):
    if i >= len(record) and j >= len(check):
        return 1
    elif i >= len(record):
        return 0

    if record[i] == '.':
        return nbways(record, check, i + 1, j)
    elif record[i] == '#':
        return startgroup(record, check, i, j)
    elif record[i] == '?':
        return startgroup(record, check, i, j) + nbways(record, check, i + 1, j)

def part1():
    s = 0
    for line in input:
        record, check = line.split()
        check = list(map(int, check.split(',')))

        s += nbways(record, tuple(check), 0, 0)
    
    return s

def part2():
    s = 0
    for line in input:
        record, check = line.split()
        record = '?'.join([record] * 5)
        check = list(map(int, check.split(',')))

        s += nbways(record, tuple(check * 5), 0, 0)
    
    return s

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
