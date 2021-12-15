from aoc import AOC

aoc = AOC(9,  2020, __file__)

#input = aoc.get_example(0).strip().split('\n')
#PREAMBLE_SIZE = 5
input = aoc.input.strip().split('\n')
PREAMBLE_SIZE = 25

input = [int(i) for i in input]

# Part 1
p1_sol = 0
for k, number in enumerate(input[PREAMBLE_SIZE:]):
    isok = False
    for i in range(-PREAMBLE_SIZE, -1):
        if (number - input[PREAMBLE_SIZE + k + i]) in input[PREAMBLE_SIZE + k + i + 1:PREAMBLE_SIZE + k]:
            isok = True
    if not isok:
        p1_sol = number
        break

# Part 2
first, last, s = 0, 0, input[0]
while True:
    if s == p1_sol:
        p2_sol = min(input[first: last + 1]) + max(input[first: last + 1])
        break
    elif s < p1_sol:
        last += 1
        s += input[last]
    else:
        s -= input[first]
        first += 1

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
