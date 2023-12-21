from aoc import AOC

aoc = AOC(21,  2023, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] == 'S':
                sy, sx = y, x

    positions = set([(sy, sx)])
    for _ in range(64):
        new_positions = set()
        for y, x in positions:
            for d in [-1, 1]:
                if input[y + d][x] in '.S': new_positions.add((y + d, x))
                if input[y][x + d] in '.S': new_positions.add((y, x + d))

        positions = new_positions

    return len(positions)

def part2():
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] == 'S':
                sy, sx = y, x

    points = [65, 65 + 131, 65 + 131 * 2]
    values = []
    positions = set([(sy, sx)])
    for i in range(points[-1] + 1):
        if i in points:
            values.append(len(positions))

        new_positions = set()
        for y, x in positions:
            for d in [-1, 1]:
                if input[(y + d) % len(input)][x % len(input[0])] in '.S': new_positions.add((y + d, x))
                if input[y % len(input)][(x + d) % len(input[0])] in '.S': new_positions.add((y, x + d))

        positions = new_positions
    
    # v[0] + n * (v[1] - v[0]) + n * (n - 1) * (v[2] / 2 - v[0] / 2 - (v[1] - v[0]))
    f = lambda n: values[0] + n * (values[1] - values[0]) + n * (n - 1) * (values[2] - 2 * values[1] + values[0]) // 2

    return f(26_501_365 // 131)

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
