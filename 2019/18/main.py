from aoc import AOC
from collections import defaultdict, deque

aoc = AOC(18,  2019, __file__)


# Warning: takes a long time (~20m on my machine). run using pypy
input = aoc.input.strip().split('\n')
input2 = open('input2', 'r').read().strip().split('\n') #Modified by hand for part 2
#input = aoc.get_example(9).strip().split('\n')

def reachablekeys(game_map, x, y, inv_keys):
    q = deque()
    q.append((x, y))
    distance = {(x, y): 0}
    keys = {}

    while q:
        x, y = q.popleft()

        for ny, nx in [(y, x + 1), (y, x - 1), (y + 1, x), (y - 1, x)]:
            if game_map[ny][nx] == '#':
                continue
            elif (nx, ny) in distance:
                continue
            distance[(nx, ny)] = distance[(x, y)] + 1
            if game_map[ny][nx].islower() and game_map[ny][nx] not in inv_keys:
                keys[game_map[ny][nx]] = (distance[(nx, ny)], nx, ny)
            elif game_map[ny][nx].isupper() and game_map[ny][nx].lower() not in inv_keys:
                continue

            q.append((nx, ny))

    return keys

def totalreachable(game_map, starts, inv_keys):
    keys = {}
    for i, (x, y) in enumerate(starts):
        k = reachablekeys(game_map, x, y, inv_keys)
        for name in k:
            d, nx, ny = k[name]
            keys[name] = (d, nx, ny, i)

    return keys

seen = {}
def find_min(game_map, starts, nb_keys, inv_keys):
    if (tuple(starts), inv_keys) in seen:
        return seen[tuple(starts), inv_keys]

    if len(inv_keys) == nb_keys:
        m = 0
    else:
        rkeys = totalreachable(game_map, starts, inv_keys)

        m = 1_000_000_000
        for key in rkeys:
            d, nx, ny, i = rkeys[key]
            nstarts = [(nx, ny) if j == i else (x, y) for j, (x, y) in enumerate(starts)]
            m = min(m, d + find_min(game_map, nstarts, nb_keys, ''.join(sorted(inv_keys + key))))

        seen[tuple(starts), inv_keys] = m
    return m

def solve(game_map):
    nb_keys = 0
    starts = []
    for line in range(len(game_map)):
        for col in range(len(game_map[line])):
            if game_map[line][col] == '@':
                starts.append((col, line))
            if game_map[line][col].islower():
                nb_keys += 1

    return find_min(game_map, starts, nb_keys, '')

def part1():
    return solve(input)

def part2():
    return solve(input2)

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
