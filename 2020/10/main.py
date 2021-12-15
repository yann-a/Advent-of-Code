from aoc import AOC

aoc = AOC(10,  2020, __file__)

#input = aoc.get_example(1).strip().split('\n')
input = aoc.input.strip().split('\n')

input = [0] + sorted([int(i) for i in input])
input.append(max(input) + 3)

nb_1 = sum([1 if input[i] - input[i-1] == 1 else 0 for i in range(1, len(input))])
nb_3 = sum([1 if input[i] - input[i-1] == 3 else 0 for i in range(1, len(input))])

mem = {}


def dp(i, last_value):
    if (i, last_value) in mem: return mem[(i, last_value)]
    if i == len(input):
        if last_value == input[-1]: return 1
        else: return 0
    elif last_value + 3 < input[i]: return 0
    else:
        mem[(i, last_value)] = dp(i + 1, last_value) + dp(i + 1, input[i])
        return mem[(i, last_value)]


p1_sol = nb_1 * nb_3
p2_sol = dp(1, 0)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
