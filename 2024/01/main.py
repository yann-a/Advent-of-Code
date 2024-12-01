from aoc import AOC

aoc = AOC(1,  2024, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    l1 = []
    l2 = []

    for line in input:
        a,b = map(int, line.split('   '))
        l1.append(a)
        l2.append(b)

    l1.sort()
    l2.sort()

    return sum(abs(l1[i] - l2[i]) for i in range(len(l1)))

def part2():
    l1 = []
    l2 = []

    for line in input:
        a,b = map(int, line.split('   '))
        l1.append(a)
        l2.append(b)

    l1.sort()
    l2.sort()

    return sum(l2[i] for i in range(len(l2)) if l2[i] in l1)

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
