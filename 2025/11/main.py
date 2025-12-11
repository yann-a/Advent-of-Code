from aoc import AOC
from collections import defaultdict
from functools import cache

aoc = AOC(11,  2025, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    graph = defaultdict(set)

    for line in input:
        source, targets = line.split(': ')
        targets = targets.split()

        for target in targets:
            graph[source].add(target)

    @cache
    def nb_paths(node):
        if node == 'out':
            return 1
        return sum(nb_paths(next) for next in graph[node])

    return nb_paths('you')

def part2():
    graph = defaultdict(set)

    for line in input:
        source, targets = line.split(': ')
        targets = targets.split()

        for target in targets:
            graph[source].add(target)

    @cache
    def nb_paths(node, dac, fft):
        if node == 'out':
            return dac and fft
        return sum(nb_paths(next, dac or node == 'dac', fft or node == 'fft') for next in graph[node])

    return nb_paths('svr', False, False)

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
