from aoc import AOC

aoc = AOC(11,  2018, __file__)

input = 5093

def power(x, y):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += input
    power_level *= rack_id
    power_level = (power_level // 100) % 10
    power_level -= 5

    return power_level

def part1():
    max_power = 0
    mx = my = 0

    for x in range(1, 300 - 2):
        for y in range(1, 300 - 2):
            power_level = sum(power(x + dx, y + dy) for dx in range(3) for dy in range(3))

            if power_level > max_power:
                mx, my = x, y
                max_power = power_level

    return f'{mx},{my}'

def part2():
    max_power = 0
    mx = my = ms = 0

    power_levels = [[power(x, y) for x in range(1, 301)] for y in range(1, 301)]

    power_levels_to = [[0 for _ in range(300)] for _ in range(300)]
    power_levels_to[0][0] = power_levels[0][0]
    for i in range(1, 300):
        power_levels_to[0][i] = power_levels_to[0][i-1] + power_levels[0][i]
        power_levels_to[i][0] = power_levels_to[i-1][0] + power_levels[i][0]
    for y in range(1, 300):
        for x in range(1, 300):
            power_levels_to[y][x] = power_levels[y][x] + power_levels_to[y-1][x] + power_levels_to[y][x-1] - power_levels_to[y-1][x-1]

    for s in range(1, 301):
        for y in range(1, 301 - s):
            for x in range(1, 301 - s):
                power_level = power_levels_to[y + s - 1][x + s - 1] - power_levels_to[y - 1][x + s - 1] - power_levels_to[y + s - 1][x - 1] + power_levels_to[y - 1][x - 1]

                if power_level > max_power:
                    mx, my, ms = x, y, s
                    max_power = power_level

    return f'{mx+1},{my+1},{ms}'

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
