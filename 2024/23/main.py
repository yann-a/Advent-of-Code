from aoc import AOC
import networkx as nx

aoc = AOC(23,  2024, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def part1():
    G = nx.Graph()
    for line in input:
        a, b = line.split('-')
        G.add_edge(a, b)
    
    s = 0
    for clique in  nx.enumerate_all_cliques(G):
        if len(clique) == 3:
            if any(n[0] == 't' for n in clique):
                s += 1

    return s

def part2():
    G = nx.Graph()
    for line in input:
        a, b = line.split('-')
        G.add_edge(a, b)
    
    l, c = 0, None
    for clique in  nx.enumerate_all_cliques(G):
        if len(clique) > l:
            l, c = len(clique), clique

    return ','.join(sorted(c))

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
