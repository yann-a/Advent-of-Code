from aoc import AOC
from queue import PriorityQueue

aoc = AOC(13,  2016, __file__)

input = 1358

def isEmpty(x, y):
    z = x * x + 3 * x + 2 * x * y + y + y * y
    z += input

    nb_1 = sum([c == '1' for c in bin(z)])

    return nb_1 % 2 == 0

def neighbours(x, y):
    neigh = []
    for d in [-1, 1]:
        if x + d >= 0:
            neigh.append((x + d, y))
        if y + d >= 0:
            neigh.append((x, y + d))
    return neigh

def solve():
    queue = PriorityQueue()
    queue.put((0, 1, 1))
    seen = set()
    nb_steps_3139 = None
    nb_reachable_under_50 = None
    while nb_steps_3139 is None or nb_reachable_under_50 is None:
        (score, x, y) = queue.get()

        if (x, y) in seen:
            continue

        if nb_reachable_under_50 is None and score > 50:
            nb_reachable_under_50 = len(seen)

        seen.add((x, y))

        if (x, y) == (31, 39):
            nb_steps_3139 = score

        for (x, y) in neighbours(x, y):
            if isEmpty(x, y):
                queue.put((score + 1, x, y))

    return nb_steps_3139, nb_reachable_under_50

p1_sol, p2_sol = solve()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
