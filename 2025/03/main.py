from aoc import AOC

aoc = AOC(3,  2025, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    s = 0
    for line in input:
        line = list(map(int, line))

        m = max(line[:-1])
        i = line.index(m)
        m2 = max(line[i + 1:])

        s += 10 * m + m2

    return s

def part2():
    s = 0
    for line in input:
        line = list(map(int, line))

        cs = 0
        i = 0
        for j in range(len(line) - 12, len(line)):
            m = max(line[i:j + 1])
            i = i + line[i:j + 1].index(m) + 1

            cs = 10 * cs + m

        s += cs

    return s

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
