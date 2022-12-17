from aoc import AOC
from collections import defaultdict

aoc = AOC(7,  2018, __file__)

input = aoc.input.strip().split('\n')
#input = aoc.get_example(0).strip().split('\n')

def get_graph():
    nodes = set()
    graphin = defaultdict(set)
    graphout = defaultdict(set)
    for line in input:
        line = line.split()

        graphout[line[1]].add(line[7])
        graphin[line[7]].add(line[1])

        nodes.add(line[1])
        nodes.add(line[7])

    available = set()
    for node in nodes:
        if node not in graphin:
            available.add(node)

    return nodes, graphin, graphout, available

def part1():
    _, graphin, graphout, available = get_graph()

    r = ''
    while len(available) > 0:
        node = min(available)

        r += node
        available.remove(node)

        for next_node in graphout[node]:
            graphin[next_node].remove(node)

            if len(graphin[next_node]) == 0:
                available.add(next_node)

    return r

def part2():
    nodes, graphin, graphout, available = get_graph()

    r, second = '', 0
    disp_after = defaultdict(int)
    next_available = [0 for _ in range(5)]
    ending_at = defaultdict(set)

    for node in available:
        disp_after[node] = 0

    while len(r) < len(nodes):
        for worker in range(len(next_available)):
            if next_available[worker] <= second and len(available) > 0:
                for node in sorted(available):
                    if disp_after[node] <= second:
                        available.remove(node)

                        ending_time = second + 60 + ord(node) - ord('A') + 1
                        next_available[worker] = ending_time
                        ending_at[ending_time].add(node)

                        for next_node in graphout[node]:
                            graphin[next_node].remove(node)
                            disp_after[next_node] = max(disp_after[next_node], ending_time)

                            if len(graphin[next_node]) == 0:
                                available.add(next_node)
        
                        break

        for node in sorted(ending_at[second]):
            r += node

        second += 1
            
    return second - 1


p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)