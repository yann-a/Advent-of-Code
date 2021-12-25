from aoc import AOC

aoc = AOC(3,  2015, __file__)

input = aoc.input.strip().split('\n')

def part1(instructions):
    x = y = 0
    visited = set([(x, y)])
    for c in instructions:
        if c == '^': y += 1
        if c == 'v': y -= 1
        if c == '<': x -= 1
        if c == '>': x += 1

        visited.add((x, y))

    return len(visited)

def part2(instructions):
    xs = ys = xr = yr = 0
    visiteds, visitedr = set([(xs, ys)]), set([(xr, yr)])
    santas_turn = True

    for c in instructions:
        dx, dy = 0, 0
        if c == '^': dy += 1
        if c == 'v': dy -= 1
        if c == '<': dx -= 1
        if c == '>': dx += 1

        if santas_turn:
            xs += dx
            ys += dy
            visiteds.add((xs, ys))
        else:
            xr += dx
            yr += dy
            visitedr.add((xr, yr))

        santas_turn = not santas_turn

    return len(visiteds.union(visitedr))

p1_sol = part1(input[0])
p2_sol = part2(input[0])

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
