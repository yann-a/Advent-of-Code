from aoc import AOC
from collections import defaultdict
import random

aoc = AOC(23,  2018, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(1).strip().split('\n')

def part1():
    nanobots = []
    maxi, maxr = -1, 0
    for i, line in enumerate(input):
        pos, r = line.split()
        pos = list(map(int, pos[5:-2].split(',')))
        r = int(r[2:])

        nanobots.append((pos, r))
        if r > maxr:
            maxi = i
            maxr = r

    (x, y, z), r = nanobots[maxi]
    return sum(abs(x - ox) + abs(y - oy) + abs(z - oz) <= r for (ox, oy, oz), _ in nanobots)

def find_clique(bots_graph, clique, candidates, excluded):
    # https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
    if len(candidates) == 0 and len(excluded) == 0: return [clique] 

    cliques = []
    pivot = random.choice(list(candidates.union(excluded)))
    for bot in list(candidates.difference(bots_graph[pivot])):
        cliques.extend(find_clique(bots_graph, clique | {bot}, candidates & bots_graph[bot], excluded & bots_graph[bot]))
        candidates.remove(bot)
        excluded.add(bot)

    return cliques

def part2():
    nanobots = []
    for i, line in enumerate(input):
        pos, r = line.split()
        pos = list(map(int, pos[5:-2].split(',')))
        r = int(r[2:])

        nanobots.append((pos, r))

    bots_graph = defaultdict(set)
    for i in range(len(nanobots)):
        (x1, y1, z1), r1 = nanobots[i]
        for j in range(i):
            (x2, y2, z2), r2 = nanobots[j]

            if abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2) <= r1 + r2:
                bots_graph[i].add(j)
                bots_graph[j].add(i)

    #print(bots_graph)
    cliques = find_clique(bots_graph, set(), set(list(range(len(nanobots)))), set())
    #print(cliques)
    max_clique = max(cliques, key=len)
    #print(max_clique)

    m = 0
    for i in max_clique:
        (x, y, z), r = nanobots[i]
        m = max(m, max(abs(x) + abs(y) + abs(z) - r, 0))
    return m

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
