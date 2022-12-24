from aoc import AOC
from functools import cache
import sys

aoc = AOC(18,  2022, __file__)

sys.setrecursionlimit(100_000)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    cubes = [list(map(int, line.split(','))) for line in input]
    
    s = 0
    for x, y, z in cubes:
        for d in [-1, 1]:
            if [x + d, y, z] not in cubes: s += 1
            if [x, y + d, z] not in cubes: s += 1
            if [x, y, z + d] not in cubes: s += 1

    return s

def dfs(x, y, z, seen, cubes):
    @cache
    def _dfs(x, y, z):
        seen.add((x, y, z))
        for d in [-1, 1]:
            if (x + d, y, z) not in seen and [x + d, y, z] not in cubes: _dfs(x + d, y, z)
            if (x, y + d, z) not in seen and [x, y + d, z] not in cubes: _dfs(x, y + d, z)
            if (x, y, z + d) not in seen and [x, y, z + d] not in cubes: _dfs(x, y, z + d)

        if len(seen) > 5_000:
            raise OverflowError()

    _dfs(x, y, z)

def part2():
    cubes = [list(map(int, line.split(','))) for line in input]
    
    """
    s = 0
    for x, y, z in cubes:
        for d in [-1, 1]:
            if [x + d, y, z] not in cubes: s += 1
            if [x, y + d, z] not in cubes: s += 1
            if [x, y, z + d] not in cubes: s += 1

    ts = 0
    totally_seen = set()
    for x, y, z in cubes:
        for d in [-1, 1]:
            if [x + d, y, z] not in cubes and (x + d, y, z) not in totally_seen:
                seen = set()
                try:
                    dfs(x + d, y, z, seen, cubes)
                except:
                    continue
                
                ins = 0
                for x, y, z in seen:
                    for d in [-1, 1]:
                        if (x + d, y, z) not in seen: ins += 1
                        if (x, y + d, z) not in seen: ins += 1
                        if (x, y, z + d) not in seen: ins += 1

                totally_seen = totally_seen.union(seen)
                ts += ins

    return s - ts
    """
    s = 0
    for x, y, z in cubes:
        for d in [-1, 1]:
            if [x + d, y, z] not in cubes:
                try:
                    dfs(x + d, y, z, set(), cubes)
                except:
                    s += 1
            if [x, y + d, z] not in cubes:
                try:
                    dfs(x, y + d, z, set(), cubes)
                except:
                    s += 1
            if [x, y, z + d] not in cubes:
                try:
                    dfs(x, y, z + d, set(), cubes)
                except:
                    s += 1

    return s

def get(x, y, z, dim, delta):
    i1 = x + delta * (dim == 0)
    i2 = y + delta * (dim == 1)
    i3 = z + delta * (dim == 2)

    return [i1, i2, i3]

def browse(cubes, npos, cache):
    if tuple(npos) in cache: return cache[tuple(npos)]
    if npos in cubes: return False

    seen = []
    def _browse(npos):
        if len(seen) > 5_000:
            raise OverflowError()

        if any(abs(p) > 30 for p in npos): return False

        seen.append(npos)
        for dim in range(3):
            for delta in [-1, 1]:
                npos2 = get(npos[0], npos[1], npos[2], dim, delta)
                if npos2 not in seen and npos2 not in cubes:
                    _browse(npos2)

    try:
        _browse(npos)
        for pos in seen:
            cache[tuple(pos)] = True
        return True
    except:
        for pos in seen:
            cache[tuple(pos)] = False
        return False

def part2():
    outside = part1()

    cubes = [list(map(int, line.split(','))) for line in input]
    cache = {}
    s = 0

    for x, y, z in cubes:
        for dim in range(3):
            for delta in [-1, 1]:
                npos = get(x, y, z, dim, delta)

                if npos not in cubes:
                    if browse(cubes, npos, cache):
                        s += 1

    return outside - s

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
