from aoc import AOC

aoc = AOC(1,  2015, __file__)

input = aoc.input.strip().split('\n')

floor = 0
p2_sol = -1
for i, c in enumerate(input[0]):
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1
    if floor < 0 and p2_sol == -1:
        p2_sol = i + 1
p1_sol = floor

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
