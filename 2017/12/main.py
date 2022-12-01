from aoc import AOC
from collections import defaultdict

aoc = AOC(12,  2017, __file__)

input = aoc.input.strip().split('\n')

graph = defaultdict(set)
for line in input:
    line = line.split(' <-> ')
    graph[line[0]] = set(line[1].split(', '))

def browse(node, seen):
    if node in seen:
        return 0
    seen.add(node)

    return 1 + sum([browse(neighbour, seen) for neighbour in graph[node]])

seen = set()
p1_sol = browse('0', seen)

nb_groups = 1
for node in graph:
    if node not in seen:
        nb_groups += 1
        browse(node, seen)
p2_sol = nb_groups

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
