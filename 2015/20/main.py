from aoc import AOC
from math import sqrt, floor

aoc = AOC(20,  2015, __file__)

input = 36_000_000
MAX_INT = 1_000_000

houses_1 = [0] * MAX_INT
houses_2 = [0] * MAX_INT

for elf in range(1, MAX_INT):
    for i in range(elf, MAX_INT, elf):
        houses_1[i] += 10 * elf

        if i < 50 * (elf + 1):
            houses_2[i] += 11 * elf

min1 = min2 = 0
while houses_1[min1] < input:
    min1 += 1
while houses_2[min2] < input:
    min2 += 1

p1_sol = min1
p2_sol = min2

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
