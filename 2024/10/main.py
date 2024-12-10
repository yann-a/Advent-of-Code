from aoc import AOC

aoc = AOC(10,  2024, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

DIR4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def dfs1(y, x):
    if input[y][x] == '9':
        return set([(y, x)])

    s = set()
    for dy, dx in DIR4:
        if 0 <= y + dy < len(input) and 0 <= x + dx < len(input[0]):
            if int(input[y + dy][x + dx]) == int(input[y][x]) + 1:
                s |= dfs1(y + dy, x + dx)

    return s

def part1():
    s = 0
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] == '0':
                s += len(dfs1(y, x))

    return s

def dfs2(y, x):
    if input[y][x] == '9':
        return 1

    s = 0
    for dy, dx in DIR4:
        if 0 <= y + dy < len(input) and 0 <= x + dx < len(input[0]):
            if int(input[y + dy][x + dx]) == int(input[y][x]) + 1:
                s += dfs2(y + dy, x + dx)

    return s

def part2():
    s = 0
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] == '0':
                s += dfs2(y, x)

    return s

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
