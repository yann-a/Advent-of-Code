from aoc import AOC

aoc = AOC(4,  2025, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    h, w = len(input), len(input[0])

    s = 0
    for y in range(h):
        for x in range(w):
            if input[y][x] == '@':
                nb = 0
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if 0 <= y + dy < h and 0 <= x + dx < w and input[y + dy][x + dx] == '@':
                            nb += 1
                s += (nb <= 4)

    return s

def part2():
    h, w = len(input), len(input[0])
    seen = [[False for _ in range(w)] for _ in range(h)]

    s = 0
    while True:
        cs = s
        for y in range(h):
            for x in range(w):
                if not seen[y][x] and input[y][x] == '@':
                    nb = 0
                    for dy in range(-1, 2):
                        for dx in range(-1, 2):
                            if 0 <= y + dy < h and 0 <= x + dx < w and input[y + dy][x + dx] == '@' and not seen[y + dy][x + dx]:
                                nb += 1
                    s += (nb <= 4)
                    if nb <= 4:
                        seen[y][x] = True

        if cs == s:
            break

    return s

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
