from aoc import AOC

aoc = AOC(4,  2022, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')


def part1():
    s = 0
    for line in input:
        a1, a2 = line.split(',')
        m1, M1 = map(int, a1.split('-'))
        m2, M2 = map(int, a2.split('-'))

        if (m1 <= m2 and M1 >= M2) or (m2 <= m1 and M2 >= M1):
            s += 1
    
    return s

def part2():
    s = 0
    for line in input:
        a1, a2 = line.split(',')
        m1, M1 = map(int, a1.split('-'))
        m2, M2 = map(int, a2.split('-'))

        if not(M2 < m1 or M1 < m2):
            s += 1
    
    return s


p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)