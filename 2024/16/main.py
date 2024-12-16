from aoc import AOC
import networkx as nx
from collections import defaultdict
from functools import cache

aoc = AOC(16,  2024, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(2).strip().split('\n')

h = len(input)
w = len(input[0])

DIR4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIR8 = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

def part1():
    G = nx.Graph()

    for y in range(h):
        for x in range(w):
            if input[y][x] in 'SE.':
                for d in range(4):
                    G.add_edge((y, x, d), (y, x, (d + 1) % 4), weight=1000)
                    G.add_edge((y, x, d), (y, x, (d - 1) % 4), weight=1000)
                for i, (dy, dx) in enumerate(DIR4):
                    if input[y + dy][x + dx] in 'SE.':
                        G.add_edge((y, x, i), (y + dy, x + dx, i), weight=1)

    return min(nx.dijkstra_path_length(G, (h - 2, 1, 1), (1, w - 2, 0)), nx.dijkstra_path_length(G, (h - 2, 1, 1), (1, w - 2, 1)))

def part2():
    dist = defaultdict(lambda: 1_000_000_000_000)
    prev = defaultdict(set)
    Q = set()
    Q.add((h - 2, 1, 1))
    dist[(h - 2, 1, 1)] = 0

    # Dijkstra while keeping all predecessors
    while not len(Q) == 0:
        (y, x, dir) = min(Q, key=lambda n: dist[n])
        Q.remove((y, x, dir))

        # Rotations
        alt = dist[(y, x, dir)] + 1000
        for nnode in [(y, x, (dir + 1) % 4), (y, x, (dir - 1) % 4)]:
            if alt < dist[nnode]:
                dist[nnode] = alt
                prev[nnode] = {(y, x, dir)}
                Q.add(nnode)
            elif alt == dist[nnode]:
                prev[nnode].add((y, x, dir))

        # Movements
        dy, dx = DIR4[dir]
        alt = dist[(y, x, dir)] + 1
        nnode = (y + dy, x + dx, dir)
        if input[y + dy][x + dx] in 'SE.':
            if alt < dist[nnode]:
                dist[nnode] = alt
                prev[nnode] = {(y, x, dir)}
                Q.add(nnode)
            elif alt == dist[nnode]:
                prev[nnode].add((y, x, dir))

    # Trace back steps to count tiles
    tiles_set = set()

    @cache
    def browse_backwards(node):
        tiles_set.add((node[0], node[1]))
        for nnode in prev[node]:
            browse_backwards(nnode)

    mdist = min(dist[(1, w - 2, 0)], dist[(1, w - 2, 1)])
    for end_node in [(1, w - 2, 0), (1, w - 2, 1)]:
        if dist[end_node] == mdist:
            browse_backwards(end_node)
    
    return len(tiles_set)

def part2_better(min_dist):
    # Initially took a huge amount of time because I added the same edges multiple times
    G = nx.Graph()

    for y in range(h):
        for x in range(w):
            if input[y][x] in 'SE.':
                for d in range(4):
                    G.add_edge((y, x, d), (y, x, (d + 1) % 4), weight=1000)
                for i, (dy, dx) in enumerate(DIR4):
                    if i == 0 or i == 3:
                        continue

                    if input[y + dy][x + dx] in 'SE.':
                        G.add_edge((y, x, i), (y + dy, x + dx, i), weight=1)

    tiles_set = set()
    for end_node in [(1, w - 2, 0), (1, w - 2, 1)]:
        if nx.shortest_path_length(G, (h - 2, 1, 1), end_node, weight='weight') == min_dist:
            for path in nx.all_shortest_paths(G, (h - 2, 1, 1), end_node, weight='weight'):
                for node in path:
                    tiles_set.add((node[0], node[1]))
    
    return len(tiles_set)

p1_sol = part1()
#p2_sol = part2()
p2_sol = part2_better(p1_sol)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
