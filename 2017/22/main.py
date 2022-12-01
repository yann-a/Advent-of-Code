from aoc import AOC

aoc = AOC(22,  2017, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    l = len(input)

    on = set()
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == '#':
                on.add((i - l // 2, j - l // 2))

    cx, cy = 0, 0
    d = 0

    caused_infection = 0
    for _ in range(10_000):
        if (cx, cy) in on:
            d = (d + 1) % 4
            on.remove((cx, cy))
        else:
            d = (d - 1) % 4
            on.add((cx, cy))
            caused_infection += 1

        cy = cy + (d == 1) - (d == 3)
        cx = cx + (d == 2) - (d == 0)

    return caused_infection

def part2():
    l = len(input)

    on, w, f = set(), set(), set()
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == '#':
                on.add((i - l // 2, j - l // 2))

    cx, cy = 0, 0
    d = 0

    caused_infection = 0
    for _ in range(10_000_000):
        if (cx, cy) in on:
            d = (d + 1) % 4
            on.remove((cx, cy))
            f.add((cx, cy))
        elif (cx, cy) in w:
            w.remove((cx, cy))
            on.add((cx, cy))
            caused_infection += 1
        elif (cx, cy) in f:
            d = (d + 2) % 4
            f.remove((cx, cy))
        else:
            d = (d - 1) % 4
            w.add((cx, cy))

        cy = cy + (d == 1) - (d == 3)
        cx = cx + (d == 2) - (d == 0)

    return caused_infection

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
