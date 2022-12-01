from aoc import AOC

aoc = AOC(1,  2022, __file__)

input = aoc.input.strip().split('\n\n')
#input = aoc.get_example(0).strip().split('\n\n')

def part1():
    m = 0
    for i in input:
        m = max(m, sum(map(int, i.split())))
    return m

def part2():
    c = []
    for i in input:
        c.append(sum(map(int, i.split())))

    c.sort()
    return c[-3] + c[-2] + c[-1]

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)