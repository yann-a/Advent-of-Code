from aoc import AOC
from operator import *
from collections import defaultdict

aoc = AOC(8,  2017, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

funcs = {
    '>': gt,
    '<': lt,
    '>=': ge,
    '<=': le,
    '==': eq,
    '!=': ne
}

mem = defaultdict(int)
overall_max = 0
for line in input:
    tokens = line.split()

    if funcs[tokens[5]](mem[tokens[4]], int(tokens[6])):
        mem[tokens[0]] += (2*(tokens[1] == 'inc') - 1) * int(tokens[2])
        overall_max = max(overall_max, mem[tokens[0]])

p1_sol = max([mem[r] for r in mem])
p2_sol = overall_max

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
