from aoc import AOC

aoc = AOC(6,  2020, __file__)

#input = aoc.get_example(1).strip().split('\n\n')
input = aoc.input.strip().split('\n\n')

p1_sol = 0
p2_sol = 0
for group in input:
    counted = {}
    for person in group.split('\n'):
        for q in person:
            if q not in counted:
                p1_sol += 1
                counted[q] = 1
            else:
                counted[q] += 1

    for q in counted:
        if counted[q] == len(group.split('\n')):
            p2_sol += 1

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
