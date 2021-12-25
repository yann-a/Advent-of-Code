from aoc import AOC
from functools import reduce
from itertools import combinations

MAX_INT = 1_000_000_000_000

aoc = AOC(24,  2015, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = list(map(int, aoc.input.strip().split('\n')))
N = sum(input)

def balance(nb_groups=3):
    nb = 0
    while True:
        nb += 1
        print(nb)
        min_qe = MAX_INT

        for c in combinations(input, nb):
            c = list(c)
            if sum(c) == N // nb_groups:
                min_qe = min(min_qe, reduce(lambda x, y: x * y, c))
        
        if min_qe != MAX_INT:
            return min_qe

p1_sol = balance()
p2_sol = balance(4)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
