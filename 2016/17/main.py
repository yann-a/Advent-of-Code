from aoc import AOC
from hashlib import md5
from queue import PriorityQueue

aoc = AOC(17,  2016, __file__)

input = 'awrkjxxr'

def areOpen(passcode, steps):
    h = md5()
    h.update(passcode.encode())
    h.update(steps.encode())

    digest = h.hexdigest()

    return [el in 'bcdef' for el in digest[:4]]

def solve(passcode):
    queue = PriorityQueue()
    queue.put((0, '', 0, 0))

    first_reach = last_reach_len = None

    while not queue.empty():
        (previous_len, previous, x, y) = queue.get()

        if (x, y) == (3, 3):
            if first_reach is None:
                first_reach = previous
            last_reach_len = previous_len
            continue

        doors = areOpen(passcode, previous)

        if x > 0 and doors[2]:
            queue.put((previous_len + 1, previous + 'L', x - 1, y))
        if x < 3 and doors[3]:
            queue.put((previous_len + 1, previous + 'R', x + 1, y))
        if y > 0 and doors[0]:
            queue.put((previous_len + 1, previous + 'U', x, y - 1))
        if y < 3 and doors[1]:
            queue.put((previous_len + 1, previous + 'D', x, y + 1))

    return first_reach, last_reach_len

p1_sol, p2_sol = solve(input)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
