from aoc import AOC
from collections import defaultdict

aoc = AOC(8,  2018, __file__)

input = list(map(int, aoc.input.strip().split('\n')[0].split()))
#input = list(map(int, aoc.get_example(0).strip().split('\n')[0].split()))

def read_node(children, metadata, node, i):
    nb_children, nb_metadata = input[i:i + 2]

    next_node = node + 1
    i += 2
    for c in range(nb_children):
        children[node].append(next_node)
        i, next_node = read_node(children, metadata, next_node, i)

    for m in range(nb_metadata):
        metadata[node].append(input[i + m])
    
    return i + nb_metadata, next_node

def read_tree():
    children = defaultdict(list)
    metadata = defaultdict(list)

    next_node = i = 0
    while i < len(input):
        i, next_node = read_node(children, metadata, next_node, i)

    return children, metadata

def sum_metadata(children, metadata, i):
    return sum(metadata[i]) + sum(sum_metadata(children, metadata, j) for j in children[i])

def get_value(children, metadata, i):
    if len(children[i]) == 0: return sum(metadata[i])
    else:
        s = 0
        for c in metadata[i]:
            if c <= len(children[i]):
                s += get_value(children, metadata, children[i][c-1])
        return s
    
def part1():
    children, metadata = read_tree()
    return sum_metadata(children, metadata, 0)    

def part2():
    children, metadata = read_tree()
    return get_value(children, metadata, 0)

p1_sol = part1()
p2_sol = part2()

# Submit
print('Part 1:', p1_sol)
#aoc.submit(1, p1_sol)
print('Part 2:', p2_sol)
#aoc.submit(2, p2_sol)