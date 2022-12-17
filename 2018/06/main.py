from aoc import AOC
from collections import defaultdict

aoc = AOC(6,  2018, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    coords = list(map(lambda l: list(map(int, l.split(', '))), input))
    mx, Mx = min(coord[0] for coord in coords), max(coord[0] for coord in coords)
    my, My = min(coord[1] for coord in coords), max(coord[1] for coord in coords)

    els_border = set()
    els = defaultdict(int)

    for x in range(mx, Mx + 1):
        for y in range(my, My + 1):
            closest, min_d = -1, 1_000_000

            for i in range(len(coords)):
                cx, cy = coords[i]

                d = abs(x - cx) + abs(y - cy)

                if d < min_d:
                    closest, min_d = i, d
                elif d == min_d:
                    closest, min_d = None, d

            if closest is not None:
                els[closest] += 1

                if x == mx or x == Mx or y == my or y == My:
                    els_border.add(closest)

    sorted_els = sorted([(els[i], i) for i in els], reverse=True)
    for ct, el in sorted_els:
        if el not in els_border:
            return ct

def part2():
    coords = list(map(lambda l: list(map(int, l.split(', '))), input))
    mx, Mx = min(coord[0] for coord in coords), max(coord[0] for coord in coords)
    my, My = min(coord[1] for coord in coords), max(coord[1] for coord in coords)

    nb_pts = 0
    r = 0
    while True:
        mod = False
        for x in range(mx - r, Mx + r + 1):
            for y in range(my - r, My + r + 1):
                if r == 0 or x == mx - r or x == Mx + r or y == my - r or y == My + r:
                    if sum(abs(x - cx) + abs(y - cy) for (cx, cy) in coords) < 10_000:
                        nb_pts += 1
                        mod = True
        
        r += 1
        if not mod:
            break

    return nb_pts

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)