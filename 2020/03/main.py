from aoc import AOC

aoc = AOC(3,  2020, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')


def check(slope_x, slope_y):
    x, y = 0, 0
    c = 0

    while y < len(input) - slope_y:
        x, y = x + slope_x, y + slope_y
        if x >= len(input[0]):
            x -= len(input[0])
        if input[y][x] == '#':
            c += 1

    return c


p1_sol = check(3, 1)
p2_sol = check(1, 1) * p1_sol * check(5, 1) * check(7, 1) * check(1, 2)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
