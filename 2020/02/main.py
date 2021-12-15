from aoc import AOC

aoc = AOC(2,  2020, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

p1_sol = 0
p2_sol = 0

for line in input:
    policy, letter, password = line.split()
    m, M = policy.split('-')
    c = sum([1 if l == letter[0] else 0 for l in password])

    if int(m) <= c <= int(M):
        p1_sol += 1

for line in input:
    policy, letter, password = line.split()
    m, M = policy.split('-')

    if ((password[int(m)-1] == letter[0]) != (password[int(M)-1] == letter[0])):
        p2_sol += 1

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
