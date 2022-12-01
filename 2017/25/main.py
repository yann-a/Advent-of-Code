from aoc import AOC
from collections import defaultdict

aoc = AOC(25,  2017, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    trans = {
        'A': [(1, 1, 'B'), (0, -1, 'C')],
        'B': [(1, -1, 'A'), (1, 1, 'C')],
        'C': [(1, 1, 'A'), (0, -1, 'D')],
        'D': [(1, -1, 'E'), (1, -1, 'C')],
        'E': [(1, 1, 'F'), (1, 1, 'A')],
        'F': [(1, 1, 'A'), (1, 1, 'E')],
    }

    tape = defaultdict(int)
    ptr = 0
    state = 'A'

    for _ in range(12_261_543):
        tape[ptr], dptr, state = trans[state][tape[ptr]]
        ptr += dptr

    return sum(tape[ptr] for ptr in tape)

p1_sol = part1()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
