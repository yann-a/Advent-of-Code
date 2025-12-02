from aoc import AOC

aoc = AOC(2,  2025, __file__)

input = aoc.input.strip()
#input = aoc.get_example(0).strip().replace('\n', '')

def part1():
    s = 0
    for couple in input.strip().split(','):
        a, b = map(int, couple.split('-'))

        for _i in range(a, b + 1):
            i = str(_i)

            if len(i) % 2 == 0 and i[:len(i) // 2] == i[len(i) // 2:]:
                s += _i

    return s

def part2():
    s = 0
    for couple in input.strip().split(','):
        a, b = map(int, couple.split('-'))

        for _i in range(a, b + 1):
            i = str(_i)

            for j in range(1, len(i) // 2 + 1):
                if len(i) % j == 0 and all(i[:j] == i[k * j:(k + 1) * j] for k in range(len(i) // j)):
                    s += _i
                    break

    return s

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
