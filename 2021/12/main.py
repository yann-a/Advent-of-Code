from aoc import AOC

aoc = AOC(12,  2021, __file__)

#input = aoc.get_example(5).strip().split('\n')
input = aoc.input.strip().split('\n')

# Init graph
graph = {}
for line in input:
    c = line.split('-')

    graph[c[0]] = graph.get(c[0], []) + [c[1]]
    graph[c[1]] = graph.get(c[1], []) + [c[0]]

# Depth first search


def browse(node, seen, smallVisitedTwice):
    seen = seen.copy()
    seen[node] = True
    paths = 1 if node == 'end' else 0

    for neighbour in graph[node]:
        if neighbour.isupper() or not seen[neighbour]:
            paths += browse(neighbour, seen, smallVisitedTwice)
        elif neighbour not in ['start', 'end'] and not smallVisitedTwice:
            paths += browse(neighbour, seen, True)

    return paths


p1_sol = browse('start', {k: False for k in graph}, True)
p2_sol = browse('start', {k: False for k in graph}, False)

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
