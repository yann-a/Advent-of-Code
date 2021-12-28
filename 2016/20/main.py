from aoc import AOC

aoc = AOC(20,  2016, __file__)

MAX_INT = 1_000_000_000

input = aoc.input.strip().split('\n')

intervals = [list(map(int, line.split('-'))) for line in input]

min_allowed = MAX_INT
for (a1, b1) in intervals:
    for (a2, b2) in intervals:
        if a2 <= b1 + 1 <= b2:
            break
    else:
        min_allowed = min(min_allowed, b1 + 1)

nb_allowed = 0
for (a1, b1) in intervals:
    ip = b1 + 1
    while ip < 2 ** 32 and not any([a2 <= ip <= b2 for (a2, b2) in intervals]):
        nb_allowed += 1
        ip += 1

p1_sol = min_allowed
p2_sol = nb_allowed

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
