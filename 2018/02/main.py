from aoc import AOC

aoc = AOC(2,  2018, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    c2 = c3 = 0
    for id in input:
        if any(id.count(l) == 2 for l in id): c2 += 1
        if any(id.count(l) == 3 for l in id): c3 += 1

    return c2 * c3

def part2():
    for id1 in input:
        for id2 in input:
            if sum(l != m for (l, m) in zip(id1, id2)) == 1:
                return ''.join(l for (l, m) in zip(id1, id2) if l == m)

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)