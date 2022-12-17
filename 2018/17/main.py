from aoc import AOC
from functools import cache
import sys

aoc = AOC(17,  2018, __file__)
sys.setrecursionlimit(10_000)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def outer_browse(x, y, maxy, walls, water_pos, at_rest):
    @cache
    def browse(x, y):
        if y > maxy + 1:
            return False

        water_pos.add((x, y))
        maybe_at_rest = set([(x, y)])

        if (x, y + 1) not in walls:
            still = browse(x, y + 1)

            if still:
                d, onground, still = 0, False, True
                while True:
                    water_pos.add((x + d, y))
                    maybe_at_rest.add((x + d, y))
                    if (x + d, y + 1) in walls: onground = True
                    if (x + d, y + 1) not in walls and onground:
                        if not browse(x + d, y + 1):
                            still = False
                            break
                    if (x + d - 1, y) in walls: break

                    d -= 1

                d, onground = 0, False
                while True:
                    water_pos.add((x + d, y))
                    maybe_at_rest.add((x + d, y))
                    if (x + d, y + 1) in walls: onground = True
                    if (x + d, y + 1) not in walls and onground:
                        if not browse(x + d, y + 1):
                            still = False
                            break
                    if (x + d + 1, y) in walls: break

                    d += 1

                if still:
                    for el in maybe_at_rest:
                        at_rest.add(el)

                return still
            return False
        else:
            d, still = 0, True

            while True:
                water_pos.add((x + d, y))
                maybe_at_rest.add((x + d, y))
                if (x + d, y + 1) not in walls:
                    if not browse(x + d, y + 1):
                        still = False
                        break
                if (x + d - 1, y) in walls: break

                d -= 1

            d = 0
            while True:
                water_pos.add((x + d, y))
                maybe_at_rest.add((x + d, y))
                if (x + d, y + 1) not in walls:
                    if not browse(x + d, y + 1):
                        still = False
                        break
                if (x + d + 1, y) in walls: break

                d += 1

            if still:
                for el in maybe_at_rest:
                    at_rest.add(el)

            return still
    
    return browse(x, y)

def print_grid():
    for y in range(miny - 1, maxy + 2):
        for x in range(410, 550):
            if (x, y) in walls: print('#', end='')
            if (x, y) in water_pos: print('*', end='')
            if (x, y) not in walls and (x, y) not in water_pos:
                print(' ', end='')
        print()
def solve():
    walls = set()
    miny, maxy = 1_000_000, -1_000_000
    for line in input:
        p, q = line.split(', ')
        pv, p = p[0], int(p[2:])
        q0, q1 = map(int, q[2:].split('..'))

        for q in range(q0, q1 + 1):
            if pv == 'x': walls.add((p, q))
            else: walls.add((q, p))

        if pv == 'x': miny, maxy = min(miny, q0), max(maxy, q1)
        else: miny, maxy = min(miny, p), max(maxy, p)

    print(miny, maxy)

    water_pos, at_rest = set(), set()
    outer_browse(500, 0, maxy, walls, water_pos, at_rest)
    
    water_pos = set((x, y) for (x, y) in water_pos if miny <= y <= maxy)
    return len(water_pos), len(at_rest)


p1_sol, p2_sol = solve()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
