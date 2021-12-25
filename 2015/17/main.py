from aoc import AOC
from itertools import combinations

aoc = AOC(17,  2015, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

containers = list(map(int, input))

def part1():
    nb_comb = 0
    for i in range(len(containers)):
        for comb in combinations(containers, i):
            if sum(comb) == 150:
                nb_comb += 1
    
    return nb_comb

def part2():
    for i in range(len(containers)):
        nb_comb = 0
        for comb in combinations(containers, i):
            if sum(comb) == 150:
                nb_comb += 1

        if nb_comb != 0:
            return nb_comb

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
