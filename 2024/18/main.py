from aoc import AOC
import networkx as nx

aoc = AOC(18,  2024, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

DIR4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIR8 = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

N = 70

def part1():
    G = nx.Graph()

    for y in range(N + 1):
        for x in range(N + 1):
            for i, (dy, dx) in enumerate(DIR4):
                if i == 0 or i == 3: continue

                G.add_edge((y, x), (y + dy, x + dx))

    for line in input[:1024]:
        y, x = map(int, line.split(','))

        G.remove_node((y, x))

    return nx.shortest_path_length(G, (0, 0), (N, N))

def reachable(end_index):
    G = nx.Graph()

    for y in range(N + 1):
        for x in range(N + 1):
            for i, (dy, dx) in enumerate(DIR4):
                if i == 0 or i == 3: continue

                if 0 <= y + dy <= N and 0 <= x + dx <= N:
                    G.add_edge((y, x), (y + dy, x + dx))

    for line in input[:end_index]:
        y, x = map(int, line.split(','))
        G.remove_node((y, x))

    try:
        a = nx.shortest_path_length(G, (0, 0), (N, N))
        return True
    except:
        return False

def part2():
    m, M = 1024, len(input)
    max_reachable = 1024

    while m <= M:
        mid = (m + M) // 2

        if reachable(mid):
            max_reachable = max(max_reachable, mid)
            m = mid + 1
        else:
            M = mid - 1

    return input[max_reachable]

# Not even that slow, input isn't huge
def part2bis():
    i = 1024
    while reachable(i):
        i += 1

    return input[i - 1]

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)
