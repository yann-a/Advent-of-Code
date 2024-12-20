from aoc import AOC
import networkx as nx

aoc = AOC(20,  2024, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

DIR2 = [(1, 0), (0, 1)]
DIR4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIR8 = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

h = len(input)
w = len(input[0])

def part1():
    G = nx.Graph()

    walls = set()
    start = None
    end = None
    
    for y in range(h):
        for x in range(w):
            if input[y][x] == 'E':
                end = (y, x)
            elif input[y][x] == 'S':
                start = (y, x)

            if input[y][x] in '.ES':
                for dy, dx in DIR2:
                    if 0 <= y + dy < h and 0 <= x + dx < w and input[y + dy][x + dx] in '.ES':
                        G.add_edge((y, x), (y + dy, x + dx))
            else:
                walls.add((y, x))

    normal_time = nx.shortest_path_length(G, start, end)
    s = 0
    for y, x in walls:
        made_connections = False
        for dy, dx in DIR4:
            if 0 <= y + dy < h and 0 <= x + dx < w and input[y + dy][x + dx] in '.ES':
                made_connections = True
                G.add_edge((y, x), (y + dy, x + dx))

        if made_connections:
            time = nx.shortest_path_length(G, start, end)
            if normal_time - time >= 100:
                s += 1

            G.remove_node((y, x))

    return s

def part2():
    G = nx.Graph()

    start = None
    end = None
    
    for y in range(h):
        for x in range(w):
            if input[y][x] == 'E':
                end = (y, x)
            elif input[y][x] == 'S':
                start = (y, x)

            if input[y][x] in '.ES':
                for dy, dx in DIR2:
                    if 0 <= y + dy < h and 0 <= x + dx < w and input[y + dy][x + dx] in '.ES':
                        G.add_edge((y, x), (y + dy, x + dx))

    length_start = nx.single_source_shortest_path_length(G, start)
    length_end = nx.single_source_shortest_path_length(G, end)

    s = 0
    for (y1, x1) in G.nodes:
        for (y2, x2) in G.nodes:
            if abs(y1 - y2) + abs(x2 - x1) <= 20:
                l = length_start[(y1, x1)] + abs(y1 - y2) + abs(x2 - x1) + length_end[(y2, x2)]

                if l <= length_start[end] - 100:
                    s += 1

    return s

def part1bis():
    G = nx.Graph()

    start = None
    end = None
    
    for y in range(h):
        for x in range(w):
            if input[y][x] == 'E':
                end = (y, x)
            elif input[y][x] == 'S':
                start = (y, x)

            if input[y][x] in '.ES':
                for dy, dx in DIR2:
                    if 0 <= y + dy < h and 0 <= x + dx < w and input[y + dy][x + dx] in '.ES':
                        G.add_edge((y, x), (y + dy, x + dx))

    length_start = nx.single_source_shortest_path_length(G, start)
    length_end = nx.single_source_shortest_path_length(G, end)

    s = 0
    for (y1, x1) in G.nodes:
        for (y2, x2) in G.nodes:
            if abs(y1 - y2) + abs(x2 - x1) <= 2:
                l = length_start[(y1, x1)] + abs(y1 - y2) + abs(x2 - x1) + length_end[(y2, x2)]

                if l <= length_start[end] - 100:
                    s += 1

    return s

p1_sol = part1bis()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
