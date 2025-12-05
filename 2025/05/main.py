from aoc import AOC

aoc = AOC(5,  2025, __file__)

input = aoc.input.strip().split('\n\n')
#input = aoc.get_example(0).strip().split('\n\n')

def part1():
    fresh, queries = input
    fresh = [tuple(map(int, line.split('-'))) for line in fresh.split('\n')]
    queries = list(map(int, queries.split('\n')))

    s = 0
    for i in queries:
        for j in fresh:
            if j[0] <= i <= j[1]:
                s += 1
                break

    return s

def part2():
    fresh, queries = input
    fresh = [tuple(map(int, line.split('-'))) for line in fresh.split('\n')]
    queries = list(map(int, queries.split('\n')))

    tot_fresh = []

    for _a, _b in fresh:
        current = [(_a, _b)]

        for c, d in tot_fresh:
            next_current = []

            for a, b in current:
                if a < c:
                    next_current.append((a, min(c - 1, b)))
                if d < b:
                    next_current.append((max(d + 1, a), b))

            current = next_current

        tot_fresh += current

    return sum(b - a + 1 for a, b in tot_fresh)

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
