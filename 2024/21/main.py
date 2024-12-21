from aoc import AOC
import networkx as nx
from functools import cache

aoc = AOC(21,  2024, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(3).strip().split('\n')

DIR4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIR8 = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

ARROW_CORR = {
    (-1, 0): '^',
    (0, 1): '>',
    (1, 0): 'v',
    (0, -1): '<'
}
RARROW_CORR = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}

digit_keypad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [None, '0', 'A']
]
dir_keypads = [
    [None, '^', 'A'],
    ['<', 'v', '>']
]

def make_graph(layout):
    G = nx.DiGraph()
    for y in range(len(layout)):
        for x in range(len(layout[0])):
            if layout[y][x] is None:
                continue
            for dy, dx in DIR4:
                if 0 <= y + dy < len(layout) and 0 <= x + dx < len(layout[0]) and layout[y + dy][x + dx] is not None:
                    G.add_edge(layout[y][x], layout[y + dy][x + dx], dir=ARROW_CORR[(dy, dx)])

    return G

def make_full_graph():
    # Make big graph where each node records the position of each robot
    keypad1 = digit_keypad
    keypad2 = keypad3 = dir_keypads

    G = nx.DiGraph()
    for y1 in range(len(keypad1)):
        for x1 in range(len(keypad1[0])):
            if keypad1[y1][x1] is None:
                continue

            for y2 in range(len(keypad2)):
                for x2 in range(len(keypad2[0])):
                    if keypad2[y2][x2] is None:
                        continue

                    for y3 in range(len(keypad3)):
                        for x3 in range(len(keypad3[0])):
                            if keypad3[y3][x3] is None:
                                continue

                            # Press on arrows
                            for dy3, dx3 in DIR4:
                                ny3, nx3 = y3 + dy3, x3 + dx3

                                if 0 <= ny3 < len(keypad3) and 0 <= nx3 < len(keypad3[0]):
                                    G.add_edge((y1, x1, y2, x2, y3, x3), (y1, x1, y2, x2, ny3, nx3), action=ARROW_CORR[(dy3, dx3)])
                            # Press on A
                            if keypad3[y3][x3] in '^v><':
                                dy2, dx2 = RARROW_CORR[keypad3[y3][x3]]
                                ny2, nx2 = y2 + dy2, x2 + dx2

                                if 0 <= ny2 < len(keypad2) and 0 <= nx2 < len(keypad2[0]):
                                    G.add_edge((y1, x1, y2, x2, y3, x3), (y1, x1, ny2, nx2, y3, x3), action='A')
                            else:
                                if keypad2[y2][x2] in '^v><':
                                    dy1, dx1 = RARROW_CORR[keypad2[y2][x2]]
                                    ny1, nx1 = y1 + dy1, x1 + dx1

                                    if 0 <= ny1 < len(keypad1) and 0 <= nx1 < len(keypad1[0]):
                                        G.add_edge((y1, x1, y2, x2, y3, x3), (ny1, nx1, y2, x2, y3, x3), action='A')
                                else: 
                                    # Extra nodes to gather all states where the keypad bot is on the same cell
                                    G.add_edge((y1, x1, y2, x2, y3, x3), (y1, x1), action='A')

    return G
                                
def part1():
    keypad1 = digit_keypad
    keypad2 = keypad3 = dir_keypads

    G = make_full_graph()
    
    s = 0
    for line in input:
        numerical_value = int(line[:-1])
        path_length = 0
        
        p = (3, 2, 0, 2, 0, 2)
        for c in line:
            for y in range(len(keypad1)):
                for x in range(len(keypad1[0])):
                    if keypad1[y][x] == c:
                        d = (y, x)

            path = nx.shortest_path(G, p, d)
            path_length += len(path) - 1
            p = path[-2]

        s += numerical_value * path_length

    return s

def shortest_path_to_edges(graph, sp):
    # Turn the result of all_pairs_all_shortest_paths into the list of edge directions for each path
    for k1 in sp:
        for k2 in sp[k1]:
            for i, path in enumerate(sp[k1][k2]):
                seq = ''
                for n1, n2 in zip(path, path[1:]):
                    seq += graph.get_edge_data(n1, n2)['dir']
                sp[k1][k2][i] = seq

def solve(nb_dir_keypads):
    digit_graph = make_graph(digit_keypad)
    dirs_graph = make_graph(dir_keypads)
    
    digits_all_sp = dict(nx.all_pairs_all_shortest_paths(digit_graph))
    dirs_all_sp = dict(nx.all_pairs_all_shortest_paths(dirs_graph))

    shortest_path_to_edges(digit_graph, digits_all_sp)
    shortest_path_to_edges(dirs_graph, dirs_all_sp)

    layers = [digits_all_sp] + [dirs_all_sp] * nb_dir_keypads

    @cache
    def compute_sp(layer, k1, k2):
        # Length of the fastest path at layer layer to go from key k1 to key k2
        if layer == nb_dir_keypads + 1:
            return 1

        m = float('inf')
        for p in layers[layer][k1][k2]:
            r = sum(compute_sp(layer + 1, n1, n2) for n1, n2 in zip(('A' + p), ('A' + p + 'A')[1:]))
            m = min(m, r)

        return m

    s = 0
    for line in input:
        s += int(line[:-1]) * sum(compute_sp(0, k1, k2) for k1, k2 in zip('A' + line, line))

    return s

def part1bis(): 
    return solve(2)

def part2():
    return solve(25)

p1_sol = part1bis()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
