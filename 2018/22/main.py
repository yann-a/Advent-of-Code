from aoc import AOC
from queue import PriorityQueue

aoc = AOC(22,  2018, __file__)

depth = 9465
tx, ty = 13,704

#depth = 510
#tx, ty = 10,10

ok_gear = [set([1, 2]), set([0, 1]), set([0, 2])]
SIZE_BEYOND_TARGET = 1000

def part1():
    geo_index = [[0 for _ in range(ty + SIZE_BEYOND_TARGET)] for _ in range(tx + SIZE_BEYOND_TARGET)]
    erosion_level = [[0 for _ in range(ty + SIZE_BEYOND_TARGET)] for _ in range(tx + SIZE_BEYOND_TARGET)]
    s = 0
    for x in range(tx + SIZE_BEYOND_TARGET):
        for y in range(ty + SIZE_BEYOND_TARGET):
            if x == 0 and y == 0: geo_index[x][y] = 0
            elif x == tx and y == ty: geo_index[x][y] = 0
            elif y == 0: geo_index[x][y] = x * 16_807
            elif x == 0: geo_index[x][y] = y * 48_271
            else: geo_index[x][y] = erosion_level[x-1][y] * erosion_level[x][y-1]

            geo_index[x][y] = geo_index[x][y] % (20_183 * 3)
            erosion_level[x][y] = (geo_index[x][y] + depth) % 20_183

            if x <= tx and y <= ty:
                s += erosion_level[x][y] % 3

    return s, erosion_level

def part2(erosion_level):
    q = PriorityQueue()
    q.put((0, 0, 0, 2))
    seen = set()

    while True:
        d, x, y, g = q.get()

        if (x, y, g) in seen: continue
        seen.add((x, y, g))

        if x == tx and y == ty and g == 2: return d

        for delta in [-1, 1]:
            if 0 <= x + delta and g in ok_gear[erosion_level[x + delta][y] % 3]: q.put((d + 1, x + delta, y, g))
            if 0 <= y + delta and g in ok_gear[erosion_level[x][y + delta] % 3]: q.put((d + 1, x, y + delta, g))
            for ng in ok_gear[erosion_level[x][y] % 3]:
                if ng != g: q.put((d + 7, x, y, ng))

p1_sol, erosion_level = part1()
p2_sol = part2(erosion_level)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
