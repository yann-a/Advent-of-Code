from aoc import AOC
from collections import defaultdict
import sys

aoc = AOC(6,  2019, __file__)
sys.setrecursionlimit(100_000)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def depth(graph, d, source):
    return d + sum(depth(graph, d + 1, dest) for dest in graph[source])

def part1():
    graph = defaultdict(list)

    for line in input:
        source, dest = line.split(')')
        graph[source].append(dest)

    return depth(graph, 0, 'COM')

def dfs(graph, source, prev, dest):
    if source == dest: return 0
    if prev is not None and len(graph[source]) == 1: return 1_000_000_000

    return 1 + min(dfs(graph, next, source, dest) for next in graph[source] if next != prev)

def part2():
    graph = defaultdict(list)

    for line in input:
        source, dest = line.split(')')
        graph[source].append(dest)
        graph[dest].append(source)

    return dfs(graph, 'YOU', None, 'SAN') - 2

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
