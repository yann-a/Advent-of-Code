from aoc import AOC

aoc = AOC(2,  2017, __file__)

input = aoc.input.strip().split('\n')

p1_sol = sum([max(l) - min(l) for line in input if (l := list(map(int, line.split())))])
p2_sol = sum([el1 // el2 for line in input if (l := list(map(int, line.split()))) for el1 in l for el2 in l if el1 != el2 and el1 % el2 == 0])

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
