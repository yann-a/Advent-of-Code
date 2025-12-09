from aoc import AOC

aoc = AOC(9,  2025, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    corners = [list(map(int, line.split(','))) for line in input]

    m = 0
    for i, (yi, xi) in enumerate(corners):
        for j, (yj, xj) in enumerate(corners[:i]):
            m = max(m, (max(yi, yj) - min(yi, yj) + 1) * (max(xi, xj) - min(xi, xj) + 1))

    return m

def part2():
    corners = [list(map(int, line.split(','))) for line in input]

    m = 0
    for i, (yi, xi) in enumerate(corners):
        for j, (yj, xj) in enumerate(corners[:i]):
            size = (max(yi, yj) - min(yi, yj) + 1) * (max(xi, xj) - min(xi, xj) + 1)

            if size > m:
                # Check that:
                #   - one point of the rectangle is inside
                #   - no polygon edge is going through the rectangle

                y, x = min(yi, yj) + 1, min(xi, xj) + 1
                if not sum(b == d and b < x and min(a, c) < y < max(a, c) for (a, b), (c, d) in zip(corners, corners[1:] + [corners[0]])) % 2 == 1:
                    continue

                if any(
                    not (min(a, c) >= max(yi, yj) or max(a, c) <= min(yi, yj) or min(b, d) >= max(xi, xj) or max(b, d) <= min(xi, xj))
                    for (a, b), (c, d) in zip(corners, corners[1:] + [corners[0]])
                ):
                    continue

                m = max(m, size)

    return m

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
