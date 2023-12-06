from aoc import AOC

aoc = AOC(6,  2023, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    times = list(map(int, input[0].split()[1:]))
    records = list(map(int, input[1].split()[1:]))

    s = 1

    for i in range(len(times)):
        nb = 0

        for j in range(times[i]):
            if j * (times[i] - j) > records[i]:
                nb += 1

        s *= nb

    return s

def part2():
    time = int(''.join(input[0].split()[1:]))
    record = int(''.join(input[1].split()[1:]))

    nb = 0

    for j in range(time):
        if j * (time - j) > record:
            nb += 1

    return nb

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)