from aoc import AOC
import networkx as nx

aoc = AOC(25,  2023, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(1).strip().split('\n')

def part1():
    G = nx.Graph()
    for line in input:
        source, dests = line.split(': ')
        dests = dests.split()

        for d in dests:
            G.add_edge(source, d, capacity = 1)

    nodes_to_cut = nx.minimum_edge_cut(G)

    assert(len(nodes_to_cut) == 3)

    for node in nodes_to_cut:
        G.remove_edge(node[0], node[1])

    sizes = []
    for component in nx.connected_components(G):
        sizes.append(len(component))

    assert(len(sizes) == 2)

    return sizes[0] * sizes[1]

p1_sol = part1()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
