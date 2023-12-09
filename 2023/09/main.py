from aoc import AOC

aoc = AOC(9,  2023, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    s = 0

    for line in input:
        numbers = list(map(int, line.split()))

        steps = []

        while any(n != 0 for n in numbers):
            steps.append(numbers)
            numbers = []

            for i in range(len(steps[-1]) - 1):
                numbers.append(steps[-1][i + 1] - steps[-1][i])

        nv = 0
        for i in range(len(steps) - 1, -1, -1):
            nv = steps[i][-1] + nv

        s += nv

    return s

def part2():
    s = 0

    for line in input:
        numbers = list(map(int, line.split()))

        steps = []

        while any(n != 0 for n in numbers):
            steps.append(numbers)
            numbers = []

            for i in range(len(steps[-1]) - 1):
                numbers.append(steps[-1][i + 1] - steps[-1][i])

        nv = 0
        for i in range(len(steps) - 1, -1, -1):
            nv = steps[i][0] - nv

        s += nv

    return s

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)