from aoc import AOC

MAX_INT = 1_000_000

aoc = AOC(9,  2015, __file__)

#input = aoc.get_example(0).strip().split('\n')
input = aoc.input.strip().split('\n')

graph = {}
for line in input:
    cities, length = line.split(' = ')
    cities = cities.split(' to ')

    graph[cities[0]] = graph.get(cities[0], []) + [(cities[1], int(length))]
    graph[cities[1]] = graph.get(cities[1], []) + [(cities[0], int(length))]

def shortest_path(node, seen, nbseen, max_len=False):
    seen = seen.copy()
    seen[node] = True
    nbseen += 1

    if nbseen == len(graph):
        return 0

    if max_len:
        return max([dist + shortest_path(neighbour, seen, nbseen, True) for (neighbour, dist) in graph[node] if not seen[neighbour]])
    else:
        return min([dist + shortest_path(neighbour, seen, nbseen, False) for (neighbour, dist) in graph[node] if not seen[neighbour]])

min_len = MAX_INT
max_len = 0
default_seen = {city: False for city in graph}
for node in graph:
    min_len = min(min_len, shortest_path(node, default_seen, 0))
    max_len = max(max_len, shortest_path(node, default_seen, 0, True))

p1_sol = min_len
p2_sol = max_len

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
