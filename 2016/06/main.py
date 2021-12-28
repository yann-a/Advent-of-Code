from aoc import AOC
from collections import defaultdict

aoc = AOC(6,  2016, __file__)

input = aoc.input.strip().split('\n')

message1 = message2 = ''
for col in range(len(input[0])):
    freqs = defaultdict(int)
    for row in range(len(input)):
        freqs[input[row][col]] += 1

    freqs = sorted([(-freqs[c], c) for c in freqs])
    message1 += freqs[0][1]
    message2 += freqs[-1][1]

p1_sol = message1
p2_sol = message2

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
