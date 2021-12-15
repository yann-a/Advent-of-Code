from aoc import AOC
import queue

aoc = AOC(15, 2021,  __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')


def at(x, y):
    init = int(input[y % len(input)][x % len(input[0])]) + y // len(input) + x // len(input[0])
    return (init - 1) % 9 + 1


def solve(part=1):
    maxX = len(input[0]) if part == 1 else len(input[0]) * 5
    maxY = len(input) if part == 1 else len(input) * 5

    min_risk = 1_000_000

    q = queue.PriorityQueue()
    q.put((-int(input[0][0]), [], (0, 0)))

    seen = {}
    while True:
        if q.empty():
            break

        (risk, path, (x, y)) = q.get()

        if 0 <= x < maxX and 0 <= y < maxY:
            if (x, y) == (maxX - 1, maxY - 1):
                if risk + at(x, y) < min_risk:
                    min_risk = risk + at(x, y)
                    #print(f'Found min with path {path + [(x, y)]}')

            if (x, y) in seen and seen[(x, y)] <= risk:
                continue
            seen[(x, y)] = risk

            q.put((risk + at(x, y), path + [(x, y)], (x-1, y)))
            q.put((risk + at(x, y), path + [(x, y)], (x+1, y)))
            q.put((risk + at(x, y), path + [(x, y)], (x, y-1)))
            q.put((risk + at(x, y), path + [(x, y)], (x, y+1)))

    return min_risk


p1_sol = solve()
p2_sol = solve(2)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
