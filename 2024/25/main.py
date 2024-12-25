from aoc import AOC

aoc = AOC(25,  2024, __file__)

input = aoc.input.strip().split('\n\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    keys = []
    locks = []

    for element in input:
        element = element.split('\n')

        heights = [sum(element[y][x] == '#' for y in range(7)) - 1 for x in range(5)]

        if element[0] == '#' * 5:
            locks.append(heights)
        else:
            keys.append(heights)

    s = 0
    for k in keys:
        for l in locks:
            if all(a + b <= 5 for (a, b) in zip(k, l)):
                s += 1

    return s

def part2():
    return 0

p1_sol = part1()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
