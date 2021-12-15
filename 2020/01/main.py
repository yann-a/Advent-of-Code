from aoc import AOC

aoc = AOC(1,  2020, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

for i in input:
    for j in input:
        if int(i) + int(j) == 2020:
            p1_sol = int(i) * int(j)

        for k in input:
            if int(i) + int(j) + int(k) == 2020:
                p2_sol = int(i) * int(j) * int(k)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
