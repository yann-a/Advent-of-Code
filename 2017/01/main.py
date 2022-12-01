from aoc import AOC

aoc = AOC(1,  2017, __file__)

input = aoc.input.strip()

p1_sol = sum([int(input[i-1]) * (input[i-1] == input[i]) for i in range(len(input))])
p2_sol = sum([int(input[i]) * (input[i] == input[(i + len(input)//2) % len(input)]) for i in range(len(input))])

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
