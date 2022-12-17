from aoc import AOC
from collections import defaultdict

aoc = AOC(12,  2018, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    pots = input[0][15:]
    leftmost_pot = 0

    rules = defaultdict(lambda : '.')
    for line in input[2:]:
        start, end = line.split(' => ')
        rules[start] = end

    for i in range(20):
        pots = ''.join(rules[('....'+pots+'....')[i:i+5]] for i in range(len(pots)+4))
        leftmost_pot -= 2

    return sum(leftmost_pot + i for i in range(len(pots)) if pots[i] == '#')

def part2():
    pots = input[0][15:]
    leftmost_pot = 0

    rules = defaultdict(lambda : '.')
    for line in input[2:]:
        start, end = line.split(' => ')
        rules[start] = end

    for i in range(102):
        pots = ''.join(rules[('....'+pots+'....')[i:i+5]] for i in range(len(pots)+4))
        leftmost_pot -= 2

    # motif shifts 1 towards right per iteration from iteration 102

    return sum(leftmost_pot + i + 50000000000 - 102 for i in range(len(pots)) if pots[i] == '#')

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
